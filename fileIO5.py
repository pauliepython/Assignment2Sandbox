
items = ["Blackbook Additional 1 ", "Testentry2_appended"]
itemsfile = open("items.txt", "a")

for item in items:
    itemsfile.write(str(item))
    itemsfile.write("\n")
itemsfile.close




