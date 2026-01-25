ChurnSense

Capacity-Constrained Retention Targeting | Decision-Support Analytics

Overview

ChurnSense is a decision-support analytics project that demonstrates how customer retention strategies change under real-world capacity constraints.

Rather than optimizing for churn risk alone, this project reframes churn analytics as a value-maximization problem, aligning outreach decisions with limited operational capacity.

The solution is implemented as an interactive Power BI dashboard designed to support business reviews, prioritization discussions, and what-if scenario analysis.

Business Problem

Customer Experience and Success teams operate under finite outreach capacity (e.g., call center volume, account manager bandwidth, campaign limits).

Traditional churn models rank customers by likelihood to churn, but this approach fails to answer a critical operational question:

Who should we contact first when we cannot contact everyone?

Without incorporating customer value, teams risk allocating scarce resources to high-risk but low-impact accounts, reducing overall business outcomes.

Business Question

Given limited outreach capacity, which customers should be prioritized to maximize retained expected value?

Solution Summary

ChurnSense treats retention targeting as a capacity-constrained optimization problem by:

Ranking customers by Expected Value (EV) rather than churn risk alone

Simulating fixed outreach capacity scenarios

Quantifying value captured vs. value left on the table

Supporting transparent, data-driven prioritization decisions

This aligns analytics output directly with business execution and operational planning.

Data

Source:
Telco Customer Churn Dataset — Kaggle
https://www.kaggle.com/datasets/rhonarosecortez/telco-customer-churn

Dataset Characteristics:

7,043 customer records

Demographics, service usage, contract attributes

Billing data and churn outcomes

Key Fields Used:

Churn

MonthlyCharges

tenure

Contract

InternetService

Engineered Features:

Churn probability proxy (p_churn)

Expected Value (EV)

Risk deciles

Eligibility flags

EV-based customer rank

Analytical Approach
1. Expected Value Modeling

Customer prioritization is based on Expected Value, defined as:

Expected Value = Churn Probability × Retention Value Proxy


This converts churn prediction into a business-relevant decision metric.

2. Risk Segmentation

Customers are segmented into risk deciles to analyze how churn risk and value interact.

Key insight:

High churn risk does not necessarily imply high recoverable value.

3. Capacity-Constrained Selection

Outreach capacity is treated as a hard operational constraint

Customers are ranked by Expected Value (highest first)

Cumulative EV is calculated as capacity increases

Diminishing returns beyond capacity are explicitly measured

Dashboard Pages
Page 1 — Capacity-Constrained Retention Targeting

Purpose:
Enable decision-makers to understand how much value can realistically be captured given current outreach limits.

Key Metrics:

Total Accounts

Eligible Accounts

Accounts Contacted (Capacity)

Total Expected Value

Expected Value Captured

Coverage of Eligible Customers

Primary Insight:
A relatively small subset of customers captures a disproportionate share of total retention value.

![Capacity-Constrained Retention Targeting](image.png)

Page 2 — Decision Logic & Tradeoffs

Purpose:
Explain why EV-based prioritization outperforms risk-only approaches.

Key Visuals:

Expected Value by Risk Decile

Cumulative Expected Value vs. Outreach Volume

Expected Value Captured vs. Left on the Table

Primary Insight:
Most retention value is captured early; marginal returns flatten rapidly beyond outreach capacity.

![Decision Logic and Tradeoffs](image-1.png)

Key Insights

Expected value is heavily concentrated in top-ranked customers

Risk-only targeting misallocates limited outreach resources

Capacity-aware prioritization improves ROI per contact

Analytics must align with operational constraints, not just model accuracy

Business Impact

This framework enables Customer Experience and Success teams to:

Treat customer outreach as a data product

Support executive decision-making with transparent metrics

Align analytics with operational capacity and SLA realities

Improve retention ROI without increasing headcount

Tools & Technologies

Power BI

DAX measures

What-if parameters

Interactive filtering

Data Modeling

Business-rule-driven feature engineering

GitHub

Version-controlled analytics project

Repository Structure


Future Enhancements

Replace probability proxy with trained churn model

Incorporate contact cost and channel effectiveness

Add uplift modeling for treatment optimization

Deploy via Power BI Service with governance and RLS

Author

Brandon Theard
Business Intelligence | Decision-Support Analytics | Data Science

This project is designed to reflect how analytics supports real-world business decisions under uncertainty, aligned with Customer Experience & Success (CE&S) use cases.