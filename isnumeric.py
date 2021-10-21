test = input("podaj liczbe: ")

    
    
if isinstance(test,int):
    print("1")
else:
    print("0")
    
if test.isnumeric():
    print(f"{test} nie jest liczba")
    if isinstance(test,int):
        print(f"{test} jest liczba typu int")
    else:
        print(f"{test} jest liczba ale jest typu str, zaraz to naprawie")
        test = int(test)
print(type(test))