# define a function
def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_amount=(discount_percent/100)*price
        final_price=price-discount_amount
        return final_price
    else:
        return price
    
 # ask user for price and discount

price = float(input("Enter the original price: "))
discount_percent=float(input("Enter the discount percentage:"))
final_price=calculate_discount(price, discount_percent)

if discount_percent>=20:
    print("Final price after discount is:", final_price)
else:
    print("No discount applied. Price remains:", final_price)
