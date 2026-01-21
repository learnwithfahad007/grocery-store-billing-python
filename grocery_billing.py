print("====== GROCERY STORE BILLING SYSTEM ======")

items = []

while True:
    name = input("Enter item name (or type 'done'): ")

    if name.lower() == "done":
        break

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    total = quantity * price
    items.append([name, quantity, price, total])

grand_total = 0
for item in items:
    grand_total += item[3]

discount = 0
if grand_total > 100:
    discount = grand_total * 0.10
elif grand_total > 50:
    discount = grand_total * 0.05

final_amount = grand_total - discount

print("\n========== RECEIPT ==========")
print(f"{'Item':15}{'Qty':10}{'Price':10}{'Total':10}")
print("-" * 45)

for item in items:
    print(f"{item[0]:15}{item[1]:10}{item[2]:10.2f}{item[3]:10.2f}")

print("-" * 45)
print(f"{'Subtotal:':35}{grand_total:.2f}")
print(f"{'Discount:':35}{discount:.2f}")
print(f"{'Final Amount:':35}{final_amount:.2f}")
print("=============================")
