test_wallet = "0x0039f22efb07a647557c7c5d17854cfd6d489ef3"

response = requests.post(GRAPH_URL, json=build_query(test_wallet))

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
