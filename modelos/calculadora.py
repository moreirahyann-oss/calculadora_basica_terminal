# pergunta qual o numero desejado
numero1 = int(input("digite o primeiro numero"))
numero2 = int(input("digite o segundo numero"))
# pergunta qual a operação desejada
operação = input("peça uma operaçao +, -, *, /")
# usa a operaçao escolhida e calcula
if operação == "+":
    resultado1 = numero1 + numero2
    print(resultado1)
elif operação == "-":
    resultado2 = numero1 - numero2
    print(resultado2)
elif operação == "*":
    resultado3 = numero1 * numero2
    print(resultado3)
elif operação == "/":
    resultado4 = numero1 / numero2
