

import random
while True:
   escolha = input("pedra , papel ou tesoura?")
   escolha = escolha.lower()
   computador = ["pedra" , "papel" , "tesoura"]

   escolha_computador = random.choice(computador)
   print ("o computador escolheu " , escolha_computador)
   if escolha == escolha_computador:
      print("empate")
   elif escolha == "pedra" and escolha_computador == "tesoura":
      print("pedra ganha de tesoura (pedra quebra tesoura)")
   elif escolha == "pedra" and escolha_computador == "papel":
      print("papel ganha de pedra (papel combre pedra)")
   elif  escolha == "papel" and escolha_computador == "tesoura":
      print("papel perde para a tesoura (tesoura corta papel)")
   elif escolha == "tesoura" and escolha_computador == "pedra":
      print("pedra ganha de tesoura (pedra quebra tesoura)")
   elif escolha == "tesoura" and escolha_computador == "papel":
      print("tesoura ganha de papel (tesoura corta papel)")
   elif escolha == "papel" and escolha_computador == "pedra":
      print("papel ganha de pedra (papel cobre pedra)")
   escolha = input("quer continuar s ou n")
   if escolha == "n":
      break