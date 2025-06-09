import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_transaction(ttype, category, amount):
    data = load_data()
    data.append({
        "type": ttype,
        "category": category,
        "amount": amount,
        "date": datetime.now().isoformat()
    })
    save_data(data)

def get_statistics():
    data = load_data()
    income = sum(item["amount"] for item in data if item["type"] == "доход")
    expenses = sum(item["amount"] for item in data if item["type"] == "расход")
    return f"Доходы: {income} руб\nРасходы: {expenses} руб\nБаланс: {income - expenses} руб"

