# cfo.ai integration — 11 October 2026

## Completed model retry — supersedes the earlier blockers below

Authenticated cfo MCP tools became available and the saved model was created and independently read back. [Open Bakaya Financial Plan — Assumptions](https://app.cfo.ai/s/p_AQGWpgYkOTYzMzUxMTgtNWY4OC00ZGEzLTlkMDEtYjExYjZiMDI4ZDRmDWRlZmF1bHRfbGF5ZXI).

The page holds an assumptions disclosure, an editable three-package unit-economics table, and a monthly revenue/burn/runway table. Unit economics readback returned all 24 cells with zero formula errors and matched the CSV's six base/stress contribution outputs. Monthly readback returned ten rows across 24 months with complete calculation/delivery coverage and zero formula errors. Main Scenario retains zero assumed volumes; cash and fixed costs remain null, so burn/runway remain null. These are assumptions, not observed zero sales or cash.

A separate `Bakaya Illustrative Demand — Not Actuals` scenario tests invented sensitivity inputs of ten self-serve packets, two ten-packet monthly bundles and five extras monthly. Saved readback returns INR31,983 gross revenue, INR25,833.85 base contribution and INR9,383.85 stress contribution per month, before fixed costs. Cash, fixed costs, burn and runway remain null. This scenario's past displayed months are also hypothetical, not historical actuals. No exchange rate or cash was invented.

Changelog entries 279742–279748 record page/table/scenario/formula writes. The model retains editable inputs and linked formulas; it is not a screenshot or workbook upload. No share grant, bank connection, purchase, billing change or private claim-document transfer was made. The browser opened the saved page and its actual spreadsheet export downloaded successfully; two sheets and the expected contribution values were read back. The earlier locally generated workbook remains a separate artifact.

## Validation limits and next inputs

Earlier browser/MCP attempts were blocked; the completed model and export above supersede those historical failures. Prices, refund rate, payment fees, delivery costs and demand remain unvalidated assumptions. Review them before pricing decisions; provide measured cash, fixed costs and customer demand to calculate meaningful burn/runway.

At INR600 delivery cost, monthly included packets lose INR125.095 each and extras lose INR220.95 before fixed costs. Do not hide those losses with blended direct-sales revenue.

One observed claude-haiku planning call on 10 October used 358 prompt and 72 completion tokens, with provider-reported USD0.0007898. This is a single call, not a completed packet cost. The shared allowance is USD15/key/30 days; remaining balance is unknown. No exchange rate is assumed.

No billing, bank connection, notification or private claim-document transfer was performed.
