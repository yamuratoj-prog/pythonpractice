import json



def save(expenses, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)


def load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    book = {"такси": 3000, "кофе": 1500}
    save(book, "expenses.json")
    data = load("expenses.json")
    print(data)

if __name__ == "__main__":
    main()
