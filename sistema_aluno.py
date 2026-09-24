



while True:
    print("1 - Cadastro aluno\n2 - Lista alunos\n3 - Buscar aluno\n4 - Ver situação\n5 - Remover aluno\n6 - Sair")
    

    
    while True:
        try :
            escolha = int(input(""))
            break
        except ValueError:
            print("Escolha invalida. Por favor escolha uma das opçãoes validas")
            print("1 - Cadastro aluno\n2 - Lista alunos\n3 - Buscar aluno\n4 - Ver situação\n5 - Remover aluno\n6 - Sair")
    



    if escolha == 6:
        break
    elif escolha > 6 or escolha <1 :
        print("Escolha invalida. Por favor escolha uma das opçãoes validas")

