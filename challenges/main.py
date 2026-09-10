def split_bill(bill, tip_percent, people):
    tip = bill * (tip_percent / 100)
    total_bill = bill + tip
    amount_per_person = total_bill / people

    return round(amount_per_person, 2)

print(split_bill(100, 10, 2))