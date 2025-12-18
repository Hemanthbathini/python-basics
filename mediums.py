
# try:

#     username = input("enter your name: ")
#     password = int(input("enter your password(numbers only): "))

#     if username == "hemanth" and password == 123:
#         print("Login Successful!")
#     else:
#         print("Access Denied!")

# except ValueError:
#     print("the input should only be number or string")

# import hashlib
# import hmac
# import time
# from getpass import getpass


# SALT = "fixed_salt_for_learning_only"


# def hash_password(password: str) -> str:
#     return hashlib.sha256((SALT + password).encode("utf-8")).hexdigest()


# USERS = {
#     "hemanth": hash_password("123"),
#     "admin": hash_password("admin123"),
# }


# def authenticate(username: str, password: str) -> bool:
#     if username not in USERS:
#         return False

#     entered_hash = hash_password(password)
#     stored_hash = USERS[username]

#     return hmac.compare_digest(entered_hash, stored_hash)


# def login(max_attempts: int = 3, lock_seconds: int = 10) -> None:
#     attempts_left = max_attempts

#     while attempts_left > 0:
#         username = input("Enter username: ").strip().lower()
#         password = getpass("Enter password: ")

#         if authenticate(username, password):
#             print(f"\nLogin successful! Welcome, {username}")
#             return
#         else:
#             attempts_left -= 1
#             print(f"\nAccess denied. Attempts left: {attempts_left}")

#     print(f"\nToo many failed attempts. Locked for {lock_seconds} seconds...")
#     time.sleep(lock_seconds)
#     print("You can try again now.")


# if __name__ == "__main__":
#     login()
# print("welcome to the BMI calculator")
# try:
#     user_height = float(input("enter your height in meters: "))
#     weight = float(input("enter your weight in kg: "))

#     if user_height <= 0 and weight <= 0:
#         print("height and must be greater than 0")

#     else:
#         BMI = weight/(user_height*user_height)
#         BMI = round(BMI,2)
#         print(f"\nyour bmi value is {BMI}")

#         if BMI < 18.5:
#             print("underweight")
#         elif BMI < 25:
#             print("normal weight")
#         elif BMI < 30:
#             print("overweight")
#         else:
#             print("obese")

# except ValueError:
#     print("Input should only be numbers")

# try:
#     price = float(input("enter the price for the product: "))
#     age = int(input("enter your age: "))

#     if price <= 0 and age <= 0:
#         print("price and age values should be greater than 0")

#     else: 
#         if age < 18:
#             discount = 0.10
#         elif age <= 60:
#             discount = 0.05
#         else:
#             discount = 0.20

#         discount_amount = price * discount
#         final_price = price - discount_amount
#         print(f"Discount amount: {discount_amount}")
#         print(f"discount applied {discount*100:.0f}%")
#         print(f"final price is {final_price}")

# except ValueError:
#     print("input should only be numbers")


