from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path

DATA_DIR = Path(os.getenv("BAKAYA_DATA_DIR", Path(__file__).resolve().parents[1] / "data"))


def connect():
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    conn=sqlite3.connect(DATA_DIR/"bakaya.sqlite3",timeout=15)
    conn.execute("CREATE TABLE IF NOT EXISTS cases (id TEXT PRIMARY KEY, payload TEXT NOT NULL)")
    return conn


class ConcurrentCaseUpdate(RuntimeError):
    pass


def save_case(case: dict, expected_revision: int | None = None):
    with connect() as conn:
        if expected_revision is not None:
            conn.execute("BEGIN IMMEDIATE")
            row=conn.execute("SELECT payload FROM cases WHERE id=?",(case["id"],)).fetchone()
            if not row or json.loads(row[0])["revision"]!=expected_revision:
                raise ConcurrentCaseUpdate("Case changed while agent was working; resume against latest reviewer decisions")
        conn.execute("INSERT INTO cases(id,payload) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload",(case["id"],json.dumps(case)))


def get_case(case_id: str):
    with connect() as conn:
        row=conn.execute("SELECT payload FROM cases WHERE id=?",(case_id,)).fetchone()
    return json.loads(row[0]) if row else None


def list_cases():
    with connect() as conn:
        rows=conn.execute("SELECT payload FROM cases ORDER BY rowid DESC").fetchall()
    return [json.loads(row[0]) for row in rows]


def upload_dir(case_id):
    # IDs are created by server and validated on API lookup.
    path=DATA_DIR/"uploads"/case_id
    path.mkdir(parents=True,exist_ok=True)
    return path
