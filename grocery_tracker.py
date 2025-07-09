import json
from datetime import datetime, timedelta

# File to store grocery data
DATA_FILE = "grocery_data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"groceries": []}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)

def add_item(name, quantity, expiry_date):
    data = load_data()
    data["groceries"].append({
        "name": name,
        "quantity": quantity,
        "expiry_date": expiry_date
    })
    save_data(data)
    print(f"✅ Added {name} (Expires: {expiry_date})")

def check_expiry():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    alert_items = []
    
    for item in data["groceries"]:
        if item["expiry_date"] <= today:
            alert_items.append(item["name"])
    
    if alert_items:
        print("⚠️ ALERT: These items expire today or have expired:")
        print(", ".join(alert_items))
    else:
        print("✅ No items expiring today!")

def generate_shopping_list(min_quantity=2):
    data = load_data()
    shopping_list = []
    
    for item in data["groceries"]:
        if item["quantity"] <= min_quantity:
            shopping_list.append(item["name"])
    
    if shopping_list:
        print("🛒 Shopping List (Low Stock):")
        print(", ".join(shopping_list))
    else:
        print("✅ No items need restocking!")

# Example Usage
if __name__ == "__main__":
    print("🏪 Smart Grocery Tracker")
    while True:
        print("\nOptions:")
        print("1. Add Grocery Item")
        print("2. Check Expiry Alerts")
        print("3. Generate Shopping List")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Item name: ")
            quantity = int(input("Quantity: "))
            expiry = input("Expiry date (YYYY-MM-DD): ")
            add_item(name, quantity, expiry)
        elif choice == "2":
            check_expiry()
        elif choice == "3":
            generate_shopping_list()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")
