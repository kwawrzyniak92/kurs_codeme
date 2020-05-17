# num = input("podaj swoje liczby całkowite podzielone (,) :")
# num = num.split(",")
# if num[0] == num [-1]:
#     print("Sa takie same")
# else:
#     print ("nie sa takie same")

numbers = int(input("Ile liczb chcesz dodac:"))
my_numbers = []
for num in range(numbers):
    num = float(input("Podaj Liczbe :"))
    my_numbers.append(num)

    print(my_numbers)
    if my_numbers [0] == my_numbers [-1]:
        print ("Sa takie same")
    else:
        print("Nie są takie same")