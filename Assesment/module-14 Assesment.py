def display_menu():
    print("press 1 for manger!! ")
    print("press 2 for customer!!")


def manager():
    print("*************Welcome To Fruit Market Manager !!****************")

    mobile_no=int(input("Enter Mobile Number : "))
    if len(str(mobile_no))==10:
        print("")
    else:
        print("Plz Enter 10 Digit Mobile No!!")
        return
    import random
    otp=random.randint(1001,9999)
    print("OTP Is : ",otp)
    Enter_OTP=int(input("Enter OTP : "))

    password = input("Enter password: ")
    confirm_password= input("Enter Confirm Password : ")
    if password == confirm_password:
        print("*****Manager Login Successfully!!*****")
    else:
        print("Passwod Is Does Not Match,PLZ try Again")

def add_fruit():
    fruit = input("Enter Fruit Name : ")
    qty = int(input("Enter Fruit Qty : "))
    price = int(input("Enter Price : "))

def view_fruits():
    print("Available Fruit Stock !!")
    fruit = {1:'Banana',
    2:'Apple',
    3:'Mango',
    4:'Cheery'}
    for key, value in fruit.items():
        print(f"{key}: {value}")

def Update_fruitss():
    print("Updated Fruit Stock!!")
    fruits={
    1:{"Name ": "Apple",  "price": 50,  "qty": 40},
    2:{"Name ": "Mango",  "price": 100, "qty": 20},
    3:{"Name ": "Cherry", "price": 70,  "qty": 50},
    4:{"Name ": "Banana", "price": 55,  "qty": 30}, }
    print("\nNo | Name   | Price | Quantity")
    for key, details in fruits.items():
        print(f"{key} | {details['Name ']} | {details['price']} | {details['qty']}")
    
    fruit_id = int(input("Enter Fruit Id : "))
    if fruit_id in fruits:
       update_qty = int(input("Enter New Quantity : "))
       fruits[fruit_id]["qty"] = update_qty
       print(f"updated{fruits[fruit_id]['Name ']} stock {update_qty}!")

    else:
        print("Invalid Id!!")




def customer():
    print("***************Welcome To The Fruit Market Store !!**************")
    Email = input("Enter Email Address : ")
    Password = input("Enter Password : ")
    Confirm_password = input("Enter Confirm Password : ")

    if Password == Confirm_password:
        print("Login Successfully!!")
    else:
        print("Password Is Does Not Match, Plz Try Again Later!!")

def display_fruits():
    fruits={
    1:{"Name ": "Apple",  "price": 50,  "qty": 40},
    2:{"Name ": "Mango",  "price": 100, "qty": 20},
    3:{"Name ": "Cherry", "price": 70,  "qty": 50},
    4:{"Name ": "Banana", "price": 55,  "qty": 30}, }
    print("\nNo | Name | Price | Quantity")
    for key, details in fruits.items():
        print(f"{key} | {details['Name ']} | {details['price']} | {details['qty']}")
    
    fruit_id = int(input("Enter Fruit ID to purchase: "))
    if fruit_id in fruits:
        quantity = int(input(f"Enter Quantity for {fruits[fruit_id]['Name ']}: "))
        total_price = fruits[fruit_id]['price'] * quantity
        print(f"Total Amount: {total_price}")
    else:
        print("Invalid Fruit ID!")
   

print("***************Welcome To Fruit Market!!****************")
    
def manger_menu():
    while True:
        print("\n******Welcome To Fruit Market Manger In Stock!!******")
        print("press 1 for  Add Fruit Stock!!")
        print("press 2 View Fruit Stock")
        print("press 3 Update Fruit Stock")
        print("press 4 exit!!")

        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            add_fruit()

        elif ch == 2:
            view_fruits()

        elif ch == 3:
            Update_fruitss()

        elif ch == 4:
            print("Thank You!!")
            break

        else:
            print("Invalid Choice!!")
            break

def customer_menu():
    while True:
        print("\n************Welcome TO FRuit market!!*****")
        print("press 1 fruit display menu!!")
        print("Press 2 Exit !!")
        
        ch1 = int(input("Enter Your Choice : "))
        if ch1 == 1:
            display_fruits()

        elif ch1 == 2:
            print("Thank You!!")
            break

        else:
            print("Invalid Choice!!")
            break



def main():

    while True:
        display_menu()
        ch2 = int(input("Enter Your Choice : "))
        if ch2 == 1:
            manager()
            manger_menu()
            break
        
        elif ch2 == 2:
            customer()
            customer_menu()
            break

        else:
            print("Thank You!!")
            break

main()