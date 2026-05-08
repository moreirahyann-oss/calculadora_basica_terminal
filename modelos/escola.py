
alunos_media = []

while True:
    print("1 adicionar aluno")
    print("2 ver alunos")
    print("3 calcular media")
    print("4 buscar aluno")
    print("5 sair")

    opção = input("escolha uma opção \n")
    
    if opção == "1":
        nome = input("digite seu nome \n").lower()
        notas = input("digite suas notas \n").split()
        lista_de_notas = []
        for nota in notas:
           lista_de_notas.append(int(nota))
        alunos_media.append([nome , lista_de_notas])
    elif opção == "2":
        print(alunos_media)
    elif opção == "3":
        soma = 0
        try:
            for nota in lista_de_notas:
                soma += nota
            media = soma / len(lista_de_notas)
            print(media)
        except ZeroDivisionError:
            print("não ha nenhum numero")
    elif opção == "4":
        
            buscar = input("digite o nome do aluno que deseja buscar \n").lower()
            encontrado = False
            for aluno in alunos_media:
                
                if buscar == aluno[0]:
                   print(f"o aluno foi encontrado {buscar}")
                   encontrado = True
                else:
                    print("o aluno não foi encontrado")
                

    else:      
        print("saindo do sistema")
        break