
print("FizzBuzz")
'''
Escribe un programa que imprima los números del 1 al 100. Pero para los múltiplos de 3, imprime la palabra "Fizz" en lugar del número, 
y para los múltiplos de 5, imprime "Buzz". Para los números que son múltiplos de tanto 3 como 5, imprime "FizzBuzz".

'''

for num in range(1, 101, 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


print("")
print("Sumatoria y promedio")
'''
Haz un programa que solicite número al usuario hasta que el usuario ingrese 0, en ese caso el programa tiene que calcular la suma de los números ingresados 
anteriormente y el promedio
'''
validate = True
summatory = 0

while validate != False:

    num = int(input("Ingrese un número: "))

    if num == 0:
        validate = False
    else:
        summatory = summatory + num

print("Suma total: ", summatory)