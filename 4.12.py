my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('hamburger')
friend_foods.append('sushi')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)
