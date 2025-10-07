#DM4ACT4
#STANLEE WYLSON D CARREON

#01
#CP NUMBER SLICING AND FORMATTING
def phonenumber_fix():
    phonenumber = input("Enter phone number:")

    fixed = phonenumber.replace(" ", "").replace("-", "")

    formatting = f"({fixed[0:3]}){fixed[3:6]}-{fixed[6:]}"
    print(formatting)

phonenumber_fix()
print("\n")

#02
#RECEIPT FORMATTING
def receipt(item,price,quantity):

    total = price*quantity
    print(f"Product {item} amount of {quantity} priced each at {price} total is ${total:.2f}")

productname = input("enter product name")
productprice = float(input("enter product price"))
productquantity = float(input("enter product quantity"))
receipt(productname,productprice,productquantity)
print("\n")


#03
#USERNAME CHECKER IF NUMBER AND LETTERS AND BETWEEN 5 AND 12
def username_fix(username):
    return username.isalnum() and 5 <= len(username) <= 12

user = input("Enter username:")
print(username_fix(user), "\n")

#04
#CREDIT CARD SECURITY
def creditcard(card_number):
    card_number = str(card_number)
    return "*" * (len(card_number) - 4) + card_number[-4:]

cardnumber = input("Enter card number: ")
print(creditcard(cardnumber))
