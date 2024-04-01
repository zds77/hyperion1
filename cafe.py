#cafe.py

menu = ["cheesecake", "waffles", "pudding", "brownie"]

stock = {"cheesecake": 10,
         "waffles": 11,
         "pudding": 8,
         "brownie": 6
         }

price = {"cheesecake": 7.95,
         "waffles": 7.50,
         "pudding": 6.30,
         "brownie": 5.90
         }
sum = 0
for item in menu:
    item_value = (stock[item] * price[item])
    sum + item_value

print(sum)