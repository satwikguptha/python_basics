# q3_shopping_cart.py

# -----------------------------
# Part A - Spot the Bug
# -----------------------------

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))

# -----------------------------
# Part B - Correct Version
# -----------------------------

def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B Output:")
print(add_item("apple"))
print(add_item("banana"))

# -----------------------------
# Part C - Shopping Cart System
# -----------------------------

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }
    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print("\nTuple Modification Error:")
        print(e)
        # Tuples are immutable and cannot be modified after creation.


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount = total * (cart["discount"] / 100)
    return total - discount


# Customer 1
cart1 = create_cart("Satwik", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

# Customer 2
cart2 = create_cart("Rahul", 5)

add_to_cart(cart2, "Book", 300, 3)
add_to_cart(cart2, "Pen", 20, 5)

print("\nCustomer 1 Cart:")
print(cart1)

print("\nCustomer 2 Cart:")
print(cart2)

print("\nCustomer 1 Total:", calculate_total(cart1))
print("Customer 2 Total:", calculate_total(cart2))

# Prove carts are independent
cart1["items"].append({
    "name": "Keyboard",
    "price": 1500,
    "qty": 1
})

print("\nAfter modifying Cart1:")
print("Cart1 Items:", cart1["items"])
print("Cart2 Items:", cart2["items"])

# Tuple immutability demonstration
price_info = (1000, "Laptop")
update_price(price_info, 1200)

# --------------------------------------
# Discussion Points
# --------------------------------------

# Why is discount=0 safe but cart=[] dangerous?
# discount=0 is immutable, so it cannot be changed accidentally.
# cart=[] is mutable and the same list object is reused across function calls.

# Difference between rebinding and mutating?
# Rebinding: x = [1,2] -> x = [3,4]
# Mutating: x.append(5)

# Mutable:
# list, dict, set

# Immutable:
# tuple, str, int

# When a list is passed into a function and modified,
# changes reflect outside because both variables refer
# to the same list object in memory.