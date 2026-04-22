'''Fraud Transaction Detector

Given a list of transactions:

Detect suspicious ones based on:
Amount > threshold
Same user multiple transactions within short time
Use:
loops + conditions
Store flagged data in dictionary'''
# Sample transaction data
transactions = [
    {"user": "Aman", "amount": 5000, "time": 1},
    {"user": "Rahul", "amount": 15000, "time": 2},
    {"user": "Aman", "amount": 7000, "time": 3},
    {"user": "Aman", "amount": 2000, "time": 4},
    {"user": "Neha", "amount": 25000, "time": 5},
    {"user": "Rahul", "amount": 3000, "time": 6},
]     
# Threshold for flagging transactions
threshold = 10000
# Dictionary to store flagged transactions
flagged_transactions = {}
# Loop through transactions to detect fraud
for transaction in transactions:
    user = transaction["user"]
    amount = transaction["amount"]
    time = transaction["time"]
    
    # Check if amount exceeds threshold
    if amount > threshold:
        flagged_transactions.setdefault(user, []).append(transaction)
    
    # Check for multiple transactions by the same user within a short time (e.g., 2 units)
    if user in flagged_transactions:
        for flagged in flagged_transactions[user]:
            if abs(time - flagged["time"]) <= 2 and flagged != transaction:
                flagged_transactions[user].append(transaction)
                break
# Print flagged transactions
print("Flagged Transactions:")
for user, transactions in flagged_transactions.items():
    print(f"User: {user}")
    for transaction in transactions:
        print(f"  Amount: {transaction['amount']}, Time: {transaction['time']}")
