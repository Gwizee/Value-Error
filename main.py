try:
    num = int(input("Enter a number: "))
    print("number is", num)
except ValueError as error :
    print("Exception:", error)