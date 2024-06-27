# create a payment receipt for Fruits

p1_name,p1_price = "Mangoes",50.40
p2_name,p2_price = "Bananas",30.30
p3_name,p3_price = "Apples",70.20
p4_name,p4_price = "Graphes",80.0
p5_name,p5_price = "Pine apple",100.50

shop_name = "Best Fruits Seller"
shop_address = "near Shivaji Chauk"
shop_city = "Pune"

Message = "Thank you for shopping with us..."

print("\t\tRECEIPT")
print("*"*50)

print("\t\t{}".format(shop_name.title()))
print("\t\t{}".format(shop_address))
print("\t\t{}".format(shop_city))

print("*"*50)

print("\t Product Name \t Product Price")

print("\t{}\t\t${}".format(p1_name.title(),p1_price))
print("\t{}\t\t${}".format(p2_name.title(),p2_price))
print("\t{}\t\t${}".format(p3_name.title(),p3_price))
print("\t{}\t\t${}".format(p4_name.title(),p4_price))
print("\t{}\t${}".format(p5_name.title(),p5_price))

print("="*50)

print("\t\t\t Total ")

total = p1_price + p2_price + p3_price + p4_price + p5_price
print("\t\t\t${}".format(total))

print("="*50)

print("\n\t{}\n".format(Message))

print("*"*50)

