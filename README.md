# coffee-shop-challenge
This project models a coffee shop domain using object-oriented programming in Python. It implements three main models — `Customer`, `Coffee`, and `Order` — with object relationships, validations, and business logic.

# Features
<!-- Models -->
**Customer**
  - Has a name (1–15 characters)
  - Can create multiple orders
**Coffee**
  - Has a name (≥3 characters)
  - Cannot be changed once set
**Order**
  - Belongs to one customer and one coffee
  - Has a price (float between 1.0 and 10.0)

<!-- Relationships -->
- `Customer.orders()` → List of all orders for a customer
- `Customer.coffees()` → Unique list of coffees ordered by a customer
- `Coffee.orders()` → List of all orders for a coffee
- `Coffee.customers()` → Unique list of customers who ordered the coffee

<!-- Aggregations -->
- `Customer.create_order(coffee, price)` → Creates a new order
- `Coffee.num_orders()` → Returns number of orders for that coffee
- `Coffee.average_price()` → Returns average price for that coffee

<!-- Bonus -->
- `Customer.most_aficionado(coffee)` → Returns the customer who spent the most on a specific coffee

## Setup Instructions

<!-- Clone the repository -->
```bash
git clone git@github.com:< username >/coffee-shop-challenge.git
cd coffee-shop-challenge

# Install dependencies
- pipenv install
- pipenv shell

# Run Debug Script
- python debug.py

# Run Tests
- pytest

## Folder Structure
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py


## Author
 - Mercy Mumbe [https://github.com/Mumbe-stack]

