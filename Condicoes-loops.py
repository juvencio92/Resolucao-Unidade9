
import random

cont = 0

for x in range(5):
    secret = random.randint(1, 30)

    palpite =int(input("Digite o palpite : "))
    cont += 1

    if palpite == secret:
        print("Você acertou parabêns !!!")
        break
    elif palpite > secret:
        print("O seu palpite é maior  que o número secreto " + str(secret))
   # elif palpite <secret:
   #     print("Palpite menor do que o número da sorte!!!")
    else:
        print("Seu palpite é menor que o número secreto " + str(secret))

print(" Você tentou " + str(cont))

print("\n") # Apenas para saltar de linha
############## Converter kilometros para milhas

print("Olá bem vindo ao conversor de unidades")

op ="sim"
while op == 'sim':

    kilometros = input("Ensira o valor em kilometros : ")
    kilometros=float(kilometros)
    print(str(kilometros) + " É igual a : " + str(float(0.62*kilometros)) + " Milhas")

    print(" Deseja efetuar nova conversão ? [nao/sim]")
    op=input("Escolha 'sim ' para continuar e 'não ' para sair do conversor ")

print("Esoolhe a opção não o programa terminou")

print("\n") # Apenas para saltar de linha

########################################## exercicio 9 .2 ##########################

number = input("Insira um número entre 1 e 100 número  entre: ")
number = int(number)

for num in range(1, number+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

print("\n") # Apenas para saltar de linha
############################## Passar a frase e minúscula ###########################

hoje = "Today is a beautyful day "

print("{0}".format(hoje.lower()))
print("%s" %(hoje.lower()))                   # As várias formas de imprimir
print(f"{hoje.lower()}")

