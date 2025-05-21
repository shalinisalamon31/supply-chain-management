Class InventoryItem:
def _init_(self, name, quantity, price):
self.name = name
self.quantity = quantity
self.price = price
def str(self):
return f"(self.name) Qty: (self.quantity), Price: $(self.price:.2f)"
Class SupplyChainManager:
def _init_(self):
self.inventory()
def add item(self, name, quantity, price):
if name in self.inventory:
self.inventory[name].quantity += quantity
else:
self.inventory [name] InventoryItem (name, quantity, price) print (f"[+] Added/Updated item: (name), Quantity: (quantity), Price: ${price:.2f)")
def display inventory(self):
print("\n Current Inventory:")
if not self.inventory:
print("Inventory is empty.")
for item in self.inventory.values():
print (item)
def process order(self, name, quantity):
if name not in self.inventory:
print (f"[!] Item (name)' not found in inventory.") return
item= self.inventory [name]
If item.quantity>= quantity:
item.quantity - quantity
total cost quantity item.price print (f"[✔] Order processed for (quantity) (name) (3). Total cost: ${total_cost:.2f)")
else:
def restock item(self, name, quantity):
if name in self.inventory:
self.inventory [name].quantity += quantity
print (f"[+] Restocked (quantity) (name) (9). New Quantity: (self.inventory[name].quantity)")
else:
print (f"[!] Cannot restock. Item (name)' not found in inventory.")
def restock item(self, name, quantity):
if name in self.inventory:
self.inventory [name].quantity += quantity
print (f"[+] Restocked (quantity) (name) (s). New Quantity: (self.inventory[name].quantity)")
else:
print (f"[!] Cannot restock. Item (name)' not found in inventory.")
Sample Execution
3cm = SupplyChainManager()
Adding items
scm.add item("Laptop", 10, 800.00)
scm.add item("Mouse", 50, 15.00)
om.add item("Keyboard", 30, 25.00)
Display inventory
scm.display_inventory()
Process orders
cm.process order ("Mouse", 5)
scm.process order ("Keyboard", 40) Should trigger insufficient stock
Restock iten
scm.restock item("Keyboard", 20)
Display final inventory
3cm.display_inventory()         
