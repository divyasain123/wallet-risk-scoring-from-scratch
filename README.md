# 💼 Wallet Risk Scoring From Scratch

This project assigns a risk score (0–1000) to on-chain Ethereum wallets based on their lending and borrowing behavior on the **Compound V2 protocol**.

The goal is to evaluate wallet activity using real blockchain data, normalize it, and compute a meaningful risk score. This was developed as part of the **Social Summer of Code 2025 Round 2 assignment**.

---

## 📡 Data Collection Method

We used **The Graph's Compound V2 Subgraph** (`graphprotocol/compound-v2`) to query each wallet's on-chain interaction with the lending protocol.

For each wallet, the following data points were retrieved:
- Health score (as reported by Compound)
- Total borrowed amount
- Total supplied amount
- Number of tokens interacted with

The data was fetched using GraphQL queries and saved to `compound_wallets_data.csv`.

---

## 📊 Feature Selection Rationale

The selected features reflect financial behavior and protocol engagement:

- **Health Score**: Indicates risk of liquidation (lower = more risky).
- **Borrow Total**: Outstanding debt — large borrowings may indicate risk exposure.
- **Supply Total**: Higher supplied amounts suggest stability and contribution.
- **Number of Tokens**: Reflects wallet diversification and engagement.

---

## 🧠 Scoring Method

1. Missing values are filled with `0` for inactive or unrecognized wallets.
2. Features are normalized using **Min-Max Scaling**.
3. Weighted formula is used to compute a raw score:
   ```python
   score = (
       0.4 * health +
       0.1 * num_tokens +
       0.3 * borrow_total +
       0.2 * supply_total
   )
