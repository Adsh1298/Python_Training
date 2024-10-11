food_items = {
    'Idly': 25,
    'Masala Dosa': 65,
    'Coffee': 15,
    'Tea': 15,
    'Rice_item': 35
}

bill_amount = 0
items = {}
is_processing = True
while is_processing:
    print('************************Menu**********************')
    for key, value in food_items.items():
        print(f'{key.upper()}: {value:.2f}')
    item = input('Enter the food item from the list above: or (Q) to Quit ').title()
    if(item.lower() == 'q'):
        break
    elif item not in food_items.keys():
        print('This item is not available with us !!!')
        break
    quantity = int(input('Enter the quantity of the food you want: '))
    items[item] = food_items[item] * quantity
    # print(food_items[item])
    # for k, v in items.items():
    #     print(f'{k} : {v}')

print('#################Total Bill#################')
for key in items.keys():
    bill_amount += items[key]
    print(f'Item Name: {key},',
          f'UnitPrice: Rs.{food_items[key]},',
          f'Quantity: {items[key]/food_items[key]},',
          f'Total: {items[key]:.2f}')
print(f'The total bill: {bill_amount}')