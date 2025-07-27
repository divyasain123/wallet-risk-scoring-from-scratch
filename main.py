import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the collected data
df = pd.read_csv("compound_wallets_data.csv")

# Clean and handle missing values
df.fillna(0, inplace=True)

# Drop wallet_id temporarily for normalization
wallets = df['wallet_id']
features = df.drop(columns=['wallet_id'])

# Normalize using MinMaxScaler
scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# Convert back to DataFrame
norm_df = pd.DataFrame(normalized_features, columns=features.columns)

# Weight assignment to each feature (you can change these!)
weights = {
    'health': 0.4,
    'num_tokens': 0.1,
    'borrow_total': 0.3,
    'supply_total': 0.2
}

# Compute weighted score
norm_df['score'] = (
    norm_df['health'] * weights['health'] +
    norm_df['num_tokens'] * weights['num_tokens'] +
    norm_df['borrow_total'] * weights['borrow_total'] +
    norm_df['supply_total'] * weights['supply_total']
)

# Scale score to 0–1000
norm_df['score'] = (norm_df['score'] * 1000).astype(int)

# Final output
final_df = pd.DataFrame({
    'wallet_id': wallets,
    'score': norm_df['score']
})

final_df.to_csv("wallet_scores.csv", index=False)
print("✅ Risk scoring complete. Saved to 'wallet_scores.csv'")
