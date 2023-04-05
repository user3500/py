from random import randint
import sys
first = int(sys.argv[1])
second = int(sys.argv[2])
answer = randint(first,second)


while True:
    try:
        guess = int(input("guess a number 1-10 "))
        if guess > 0 and guess < 11:
            if guess == answer:
                print("You are a genius")
                break
        else:
            print("hey bozo i said 1-10")
    except ValueError:
        print("Value error")
        continue


