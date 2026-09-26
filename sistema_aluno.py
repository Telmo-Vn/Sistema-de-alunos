





lista_aluno = []
while True:
    print("1 - Cadastro aluno\n2 - Lista alunos\n3 - Buscar aluno\n4 - Ver situação\n5 - Remover aluno\n6 - Sair")
    

    
    while True:
        try :
            escolha = int(input(""))
            break
        except ValueError:
            print("Escolha invalida. Por favor escolha uma das opçãoes validas")
            print("1 - Cadastro aluno\n2 - Lista alunos\n3 - Buscar aluno\n4 - Ver situação\n5 - Remover aluno\n6 - Sair")
    

    match escolha:
        case 1:
                while True:
                    
                    nome = str(input("Digite o Nome do Aluno: "))
                    idade = int(input("Digite a Idade do Aluno: "))
                    nota = float(input("Digite a Nota do Aluno: "))
                    
                    resposta = str((input)("Deseja cadastrar mais algun aluno [S/N]: "))
                    

                    lista_aluno.append({

                            'nome':nome,
                            'idade':idade,
                            'nota':nota
            
                    })
 
                    
                    if resposta == 'n' or resposta == 'N':
                        break
                    elif resposta == 's' or resposta == "S":
                        continue
                    else:
                        print("Opção invalida")
                        break

                        
        case 2:
            contador = 0
            for alunos in lista_aluno:
                contador = contador + 1
                print(f"Aluno {contador}\n {alunos['nome']}\n Idade {alunos['idade']}\n Nota {alunos['nota']}\n")


        case 3:
            if not lista_aluno:
                print("Nenhum aluno cadastrado")
                continue
            procura_aluno = str(input("Digite o nome do Aluno: "))
            encontrou = False
            for alunos in lista_aluno:
                if procura_aluno == alunos['nome']:
                    encontrou = True
                    break

            if encontrou:
                print(f"Aluno encontrado!:\n {alunos['nome']}\n Idade {alunos['idade']}\n Nota {alunos['nota']}")
            else:
                print("Aluno não encontrado")

                
    if escolha == 6:
        break
    elif escolha > 6 or escolha <1 :
        print("Escolha invalida. Por favor escolha uma das opçãoes validas")

