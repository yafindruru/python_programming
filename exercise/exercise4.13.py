buffet = ('rice', 'noodles', 'chicken', 'soup', 'salad')
for food in buffet:
    print(food)
try:
    buffet[0] = 'bread'
except TypeError as error:
    print(f"Python rejected the change: {error}")
buffet = ('rice', 'noodles', 'chicken', 'tofu', 'fruit')
print("Revised menu:")
for food in buffet:
    print(food)