agenda = {}

def menu():
    print("#--------------------------------------------------------#")
    print("#        A G E N D A  D E  E N D E R E Ç O S             #")
    print("#--------------------------------------------------------#")
    print("#   OPÇÕES                                               #")
    print("#   1 - CADASTRAR NOME                                   #")
    print("#   2 - CONSULTAR NOME                                   #")
    print("#   3 - EXCLUIR NOME                                     #")
    print("#   4 - LISTAR TODOS OS NOME                             #")
    print("#   5 - ZERAR AGENDA                                     #")
    print("#   6 - DESENVOLVEDORES                                  #")
    print("#   7 - SAIR                                             #")                                           
    print("#--------------------------------------------------------#")

def cadastro_nome():
    nome = input("DIGITE O NOME QUE DESEJA CADASTRAR OU '0' PARA VOLTAR AO MENU: ")
    if nome == '0':
        return
    endereco = input("DIGITE AQUI SEU ENDEREÇO: ")
    telefone = float(input("DIGITE AQUI SEU NUMERO DE TELEFONE: "))
    agenda[nome] = {"endereco": endereco, "telefone": telefone}
    print("NOME, ENDEREÇO E TELEFONE CADASTRADOS COM SUCESSO !!")

def apagar_nome():
    nome = input("DIGITE AQUI O NOME QUE DESEJA APAGAR OU '0' PARA VOLTAR AO MENU: ")
    if nome == '0':
        return
    if nome in agenda:
        del agenda[nome]
        print("NOME APAGADO COM SUCESSO !!")
    else:
        print("NOME NÃO ENCONTRADO, TENTE NOVAMENTE !!")

def consultar_nome():
    nome = input("QUAL NOME DESEJA CONSULTAR: ")
    if nome in agenda:
        print("NOME JA CADASTRADO !!")
        print("Endereço: ", agenda[nome]["endereco"])
        print("Telefone: ", agenda[nome]["telefone"])
    else:
        print("NOME NÃO CADASTRADO !!")

def listar_nomes():
    print("AQUI ESTÃO TODOS OS NOMES CADASTRADOS: ")
    for nome, info in agenda.items():
        print("--------------------------------")
        print("| Nome:                        |", nome)
        print("| Endereço:                    |",info["endereco"])
        print("| Telefone:                    |", info["telefone"])
        print("--------------------------------")

def apagar_agenda():
    agenda.clear()
    print("AGENDA ZERADA COM SUCESSO !!")

def desenvolvedores():
    print("-------------------------------------------------------------------------------------------------------------")
    print("| DESENVOLVEDORES: Luis Filipe Soaes Lima - 202313575 & Yan Teixeira Demuner da Cruz - 202311099               |")
    print("-------------------------------------------------------------------------------------------------------------")
while True:
    menu()
    opcao = int(input("DIGITE A OPÇÃO DESEJADA (1 a 7): "))

    if opcao <= 0 or opcao > 7:
        print("OPÇÃO INVALIDA, TENTE NOVAMENTE !!")
    elif opcao == 1:
        cadastro_nome()
    elif opcao == 2:
        consultar_nome()
    elif opcao == 3:
        apagar_nome()
    elif opcao == 4:
        listar_nomes()
    elif opcao == 5:
        apagar_agenda()
    elif opcao == 6:
        desenvolvedores()
    elif opcao == 7:
        print("SAINDO...PROGRAMA FINALIZADO !!")
        break
