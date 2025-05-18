# from customer import Customer
# from coffee import Coffee
# from order import Order

# # Create customers
# alice = Customer("Alice")
# bob = Customer("Bob")
# carl = Customer("Carl")

# # Create coffee types
# latte = Coffee("Latte")
# espresso = Coffee("Espresso")
# mocha = Coffee("Mocha")

# # Create orders
# alice.create_order(latte, 4.5)
# alice.create_order(mocha, 5.0)
# bob.create_order(latte, 6.0)
# bob.create_order(latte, 3.5)
# carl.create_order(espresso, 2.5)

# # View orders for Alice
# print(f"{alice.name}'s Orders:")
# for order in alice.orders():
#     print(f"- {order.coffee.name} at ${order.price}")

# # View unique coffees Alice ordered
# print(f"{alice.name}'s Coffees: {[coffee.name for coffee in alice.coffees()]}")

# # View all orders for Latte
# print(f"\nOrders for {latte.name}:")
# for order in latte.orders():
#     print(f"- {order.customer.name} paid ${order.price}")

# # Coffee stats
# print(f"\n{latte.name} has {latte.num_orders()} orders")
# print(f"Average price of {latte.name}: ${latte.average_price():.2f}")

# # Bonus: Who spent the most on Latte?
# aficionado = Customer.most_aficionado(latte)
# if aficionado:
#     print(f"\nMost aficionado for {latte.name}: {aficionado.name}")
# else:
#     print(f"No orders yet for {latte.name}")
