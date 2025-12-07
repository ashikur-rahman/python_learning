test = [
    {'id': 1, 'name': 'KFC', 'average_rating': 4.5}, 
    {'id': 2, 'name': 'McDonalds', 'average_rating': 3.0}
    ]

key=lambda x: x["average_rating"]
print(key(test[0]))