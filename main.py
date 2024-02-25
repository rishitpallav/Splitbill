members = {"ash": 0, "ana": 0, "k": 0, "r": 0, "g": 0, "d": 0}
paidTo = ["project"]
value = 0.0
while len(paidTo) >= 1:
  # Detching details on bill
  paidBy = input("Who paid the bill? ")
  if paidBy == "":
    break
  paidTo = input("Bill used by: ").split(" ")
  price = float(input("Enter price: "))
  
  value = float(price / len(paidTo))

  members[paidBy] += price

  for name in paidTo:
    members[name] -= value
  print(members)

print("SUMMARY:")
print(members)