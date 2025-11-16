
import csv

def add_expense():
    date=input("Date (YYYY-MM-DD): ")
    item=input("Item: ")
    cost=input("Amount: ")
    with open("expenses.csv","a",newline="") as f:
        w=csv.writer(f)
        w.writerow([date,item,cost])
    print("Expense Added!")

def show_summary():
    total=0
    with open("expenses.csv") as f:
        r=csv.reader(f)
        for row in r:
            if row:
                total+=float(row[2])
    print("Total Spent:", total)

while True:
    print("1.Add Expense 2.Summary 3.Exit")
    ch=input("Choose: ")
    if ch=="1": add_expense()
    elif ch=="2": show_summary()
    else: break
