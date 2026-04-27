
pessoas = []

while True:
    
    print ("1 cadrastar")
    print ("2 login")
    print ("3 sair")

    opção = input("escolha uma opção")

    if opção == "1" :
        usuario = input("digie seu usuario")
        senha = input("digite sua senha")
        pessoa = {"nome" : usuario ,"senha" : senha }
        pessoas.append(pessoa)
        print("cadrasto realizado com sucesso")
    
    elif opção == "2":
        usuario = input("digite seu usuario")
        senha = input("digite sua senha")
        encontrou = False

        for pessoa in pessoas:
            if pessoa["nome"] == usuario and pessoa["senha"] == senha:
                encontrou = True
                print("login feito com sucesso")
            
    
    elif opção == "3":
        print("saindo do sistema")
        break


    
    




    
    
    