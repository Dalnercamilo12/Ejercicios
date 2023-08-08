def main():
    print("ingrese dos numeros para realizar operaciones con los mismos.")
    num_1= int(input("ingrese el primer numero:"))
    num_2= int(input("ingrese el segundo numero:"))
    suma= sumar(num_1,num_2)
    resta= restar(num_1,num_2)
    multiplicacion= multiplicar(num_1,num_2)
    divicion= dividir(num_1,num_2)
    print(f"los numeros digitados son : {num_1} y {num_2}")
    print(f"la suma de los numeros digitados es: {suma}")
    print(f"la resta de los numeros digitados es: {resta}")
    print(f"la multiplicacion de los numeros digitados es: {multiplicacion}")
    print(f"la division de los numeros digitados es: {divicion}")
def sumar(num1,num2):
    total = num1 + num2
    return total
def restar(num1,num2):
    total = num1 - num2
    return total
def multiplicar(num1,num2):
    total= num1 * num2
    return total
def dividir(num1,num2):
    total = num1/num2
    return total
main()