import random

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.extend(["elderberry", "fig", "grape"])
fruits += ["honeydew", "kiwi", "lemon"]

print(fruits)

#random_fruit = random.choice(fruits)

while True:
    fruit = random.choice(fruits)
    like = input(f"Do you like {fruit}? (yes/no)")
    if like.lower() == "yes":
        new_fruit = input(f"Name another fruit to add: ")
        fruits.append(new_fruit)
    elif like.lower() == "no":
        print(f"Removing {fruit} from the list.")
        fruits.remove(fruit)
    elif like.lower() == "stop":
        break