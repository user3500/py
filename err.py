#Error Handling

while True:
    try:
        age = int(input("Enter your age> "))
        10/age
        print(age)
    except ValueError:
        print("enter a number")
    except ZeroDivisionError:
        print("Cannot enter 0!")
    else:
        print("Thank you")
        break
    finally:
        print("Finished.")
