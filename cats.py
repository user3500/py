#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Luna", 2)
cat2 = Cat("Ruby", 2)
cat3 = Cat("Nook", 1)

# 2 Create a function that finds the oldest cat

def get_oldest(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(get_oldest(cat1.age, cat2.age, cat3.age))
