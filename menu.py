from ast import Break, If
from asyncore import ExitNow

print("Bem vindo a Busines!")
escolha = 0 
while escolha != 8:
    print("\n\tMenu de Opções:")
    print("\n1 - Página de cadastro para candidato(a)")
    print("2 - Página de cadastro para empresa")
    print("3 - Sobre o processo seletivo")
    print("4 - Vagas disponiveis")
    print("5 - Página para candidato(a)")
    print("6 - Página para empresa")
    print("7 - Sobre a Busines")
    print("8 - Sair do menu")
    escolha = int(input("\nDigite a opção escolhida: "))
#__________________________________________________1________________________________________________________________#
    if escolha == 1:
        print("\nPágina de cadastro candidato: ")
        nome = input("\nNome: ") 
        sobrenome = input("Sobrenome: ")
        while True:
            data = input("Data do seu nascimento(Ex: dd/mm/aaaa): ")
            data = data.split("/")
            if len(data) == 3:
                dia = data[0]
                mes = data[1]
                ano = data[2]
                print(nome, f"Nasceu no dia {dia} do mês {mes} no ano de {ano}")
                break
            elif len(data) != 3:
                print("Você deve digitar no formato dd/mm/aaaa")
            else:
                print("")
        print("\nSexo: ")        
        escolhaa = 0 
        while escolhaa != 4:
            um = ("Homem")
            print("1 - Homem")
            dois = ("Mulher")
            print("2 - Mulher")
            print("3 - Outro")
            quatro = ("Não declarado")
            print("4 - Não declarar")
            sexoo = {um, dois, quatro}
            escolhaa = int(input("\nDigite a opção escolhida: "))
            if escolhaa == 1:
                escolhat = print({um})
                break
            elif escolhaa == 2:
                escolhat = print({dois})
                break
            elif escolhaa == 3:
                sexo= input("Digite seu sexo: ")
                tres = (sexo)
                escolhat = print({tres})
                break
            elif escolhaa == 4:
                escolhat = print({quatro})
                break
            elif escolhaa >= 5:
                print("\nEscolha inválida!")
        else:
            print("\nEscolha inválida!\n ")
        cel = input("Celular com DDD(Ex: (ddd)XXXXX-XXXX): ")
        cel = cel.split("(" and ")" and "-")
        login = input("E-mail: ")
        endereco = input("Endereço: ")
        numero = int(input("Número da sua residência: "))
        while True:
            cep = input("CEP(Ex:XXXXX-XXX): ")
            cep = cep.split("-")
            if len(cep) == 2:
                part1 = cep[0]
                part2 = cep[1]
                break
            elif len(cep) != 2:
                print("Você deve digitar no formato XXXXX-XXX")
            else:
                print("")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado =input("Estado: ")
        print("Seu endereço é:", endereco, ",", numero, ",", bairro, ",", cidade, "-", estado)
        print("\nPossue formação acadêmica?")
        escolhaa1 = 0 
        while escolhaa1 != 3:
            print("1 - Possuo")
            print("2 - Não possuo")
            print("3 - Estou me formando")
            escolhaa1 = int(input("\nDigite a opção escolhida: "))
            if escolhaa1 == 1:
                fa = input("Digite sua formação acadêmica: ")
                input("Digite a instituição acadêmica: ")
                int(input("Ano que iniciou o curso acadêmico: "))
                int(input("Ano de conclusão do curso acadêmico: "))
                break
            elif escolhaa1 == 2:
                print("")
                break
            elif escolhaa1 == 3:
                fa = input("Digite sua formação acadêmica: ")
                input("Digite a instituição acadêmica: ")
                int(input("Ano que entrou no curso acadêmico: "))
                int(input("Ano previsto para o término: "))
                break
            elif escolhaa1 >= 4:
                print("\nEscolha inválida!\n")
        else:
            print("\nEscolha inválida!\n")
        input("Fluente em quais idiomas? ")
        input("Linguagens de programação que você possui mais habilidade: ")
        print("\nPossue experiência no mercado de trabalho?")
        escolhaa2 = 0 
        while escolhaa2 != 3:
            print("1 - Possuo")
            print("2 - Não possuo")
            print("3 - Estou trabalhando")
            escolhaa2 = int(input("\nDigite a opção escolhida: "))
            if escolhaa2 == 1:
                input("Empresas que já trabalhou: ")
                input("Cargos que já ocupou nas empresas: ")
                while True:
                    data1 = input("Data que entrou no último emprego(Ex: dd/mm/aaaa): ")
                    data1 = data1.split("/")
                    if len(data1) == 3:
                        dia = data1[0]
                        mes = data1[1]
                        ano = data1[2]
                        print(nome, f"Entrou no último emprego no dia {dia} do mês {mes} no ano de {ano}")
                        break
                    elif len(data1) != 3:
                        print("Você deve digitar no formato dd/mm/aaaa")
                    else:
                        print("")
                while True:
                    data2 = input("Data que saiu do último emprego(Ex: dd/mm/aaaa): ")
                    data2 = data2.split("/")
                    if len(data2) == 3:
                        dia = data2[0]
                        mes = data2[1]
                        ano = data2[2]
                        print(nome, f"Saiu do último emprego no dia {dia} do mês {mes} no ano de {ano}")
                        break
                    elif len(data2) != 3:
                        print("Você deve digitar no formato dd/mm/aaaa")
                    else:
                        print("")
            elif escolhaa2 == 2:
                print()
                break
            elif escolhaa2 == 3:
                input("Nome das empresas que já trabalhou: ")
                input("Nome da empresa que você está trabalhando: ")
                input("Cargo que ocupa na atual empresa: ")
                input("Cargos que já ocupou nas empresas: ")
                while True:
                    data3 = input("Data que entrou no último emprego(Ex: dd/mm/aaaa): ")
                    data3 = data3.split("/")
                    if len(data3) == 3:
                        dia = data3[0]
                        mes = data3[1]
                        ano = data3[2]
                        print(nome, f"Entrou no último emprego no dia {dia} do mês {mes} no ano de {ano}")
                        break
                    elif len(data3) != 3:
                        print("Você deve digitar no formato dd/mm/aaaa")
                    else:
                        print("")
                while True:
                    data4 = input("Data que saiu do último emprego(Ex: dd/mm/aaaa): ")
                    data4 = data4.split("/")
                    if len(data4) == 3:
                        dia = data4[0]
                        mes = data4[1]
                        ano = data4[2]
                        print(nome, f"Saiu do último emprego no dia {dia} do mês {mes} no ano de {ano}")
                        break
                    elif len(data4) != 3:
                        print("Você deve digitar no formato dd/mm/aaaa")
                    else:
                        print("")
                while True:
                    data5 = input("Data que entrou no atual emprego(Ex: dd/mm/aaaa): ")
                    data5 = data5.split("/")
                    if len(data5) == 3:
                        dia = data5[0]
                        mes = data5[1]
                        ano = data5[2]
                        print(nome, f"Entrou no emprego atual no dia {dia} do mês {mes} no ano de {ano}")
                        break
                    elif len(data5) !=3:
                        print("Você deve digitar no formato dd/mm/aaaa")
                    else:
                        print("")
                break
            elif escolhaa2 >= 4:
                print("\nEscolha inválida!\n")
        else:
            print("\nEscolha inválida!\n ")
        senha = input("\nCrie sua senha: ")
        se = input("Digite novamente sua senha: ")
        i=0
        while True:
            try:
                print("")
            except:
                print("")
            if se != senha:
                print("\nAs senhas não estão iguais!")
                senha = input("\nCrie sua senha: ")
                se = input("Digite novamente sua senha: ")
            else:
                print("Senha criada com sucesso!")
                break
        print('\nPara fazer login na "Página para candidato", será solicitado o seu e-mail e sua senha.')
        print(nome, "Obrigado pelo seu cadastro!")

        candidato = [nome, cel, login, escolhat]
        print (candidato, "\n")
#_____________________________________________________________2_________________________________________________________________________#
    elif escolha == 2:
        print("Página de cadastro para empresa: ")
        empresa = input("\nNome da empresa: ")
        while True:
            cnpj1 = input("CNPJ da empresa(Ex: XX.XXX.XXX/XXXX-XX): ")
            cnpj1 = cnpj1.split("." and "-" and "/")
            if len(cnpj1) == 5:
                part1 = cnpj1[0]
                part2 = cnpj1[1]
                part3 = cnpj1[2]
                part4 = cnpj1[3]
                part5 = cnpj1[4]
                break
            elif len(cnpj1) != 5:
                print("Você deve digitar no formato XX.XXX.XXX/XXXX-XX")
            else:
                print("")
        ts = input("Tipo de serviço da empresa: ")
        dsc = input("Descreva sobre  a empresa: ")
        input("E-mail: ")
        cda = input("Crie seu código de acesso: ")
        cdaa = input("Digite novamente o código de acesso: ")
        while True:
            try:
                cda = input("Crie seu código de acesso: ")
                cdaa = input("Digite novamente o código de acesso: ")
            except:
                print("Os código de acesso não estão iguais!")
            if cdaa != cda:
                print("\nOs código de acesso não estão iguais!")
                cda = input("Crie seu código de acesso: ")
                cdaa = input("Digite novamente o código de acesso: ")
            else:
                print("Código de acesso criado com sucesso!")
                break
        print('\nPara fazer o login na "Página para empresa", será solicitado o CNPJ da empresa e o código de acesso aqui criado.')
        print(empresa, "Obrigado por apostar e confiar na gente!")

        fornecer = [empresa, cnpj1]
        print(fornecer)
#_________________________________________________3_________________________________________________________________#
    elif escolha == 3:
        print("\nPágina sobre o processo seletivo:")
        print("\nDepois que o candidato faz seu cadastro aqui com a gente, o nosso sistema colhe as informações fornecidas pelo candidato e já coloca na candidatura para a(s) vaga(s) que mais combina com as características do candidato - empresa.")
#__________________________________________________4_______________________________________________________________#
    elif escolha == 4:
        print("\nVagas disponiveis:")
        print("\nVendas & Marketing" )
        print("Tecnologia")
        print("RH")
        print("Auxiliar financeiro")
#____________________________________________________5______________________________________________________________#
    elif escolha == 5:
        print("\nPágina do candidato.")
        log = input("\nDigite o seu e-mail: ")
        senha1 = input("Digite sua senha: ")
        while True:
            if log != login:
                print("\nSenha ou Email incorretos!")
                log = input("\nDigite o seu e-mail: ")
                senha1 = input("Digite sua senha: ")
            elif senha1 != senha:
                print("\nSenha ou Email incorretos!")
                log = input("\nDigite o seu e-mail: ")
                senha1 = input("Digite sua senha: ")
            else:
                print("\n", nome, "Seja bem vindo(a)!")
                break
        print(f"\nSeus dados estão sendo analisados pelas empresas parceiras e qualquer novidade que aparecer, você será informado(a) pelo email", login)
        print(nome, f"Nasceu no dia {dia} do mês {mes} no ano de {ano}")
        candidi = [cidade, "-", estado]
        print("Mora em ", candidi)
#_____________________________________________________6_____________________________________________________________#
    elif escolha == 6:
        print("\nPágina da empresa.")
        cnpj = input("CNPJ da empresa(Ex: XX.XXX.XXX/XXXX-XX): ")
        cnpj = cnpj.split("." and "-" and "/")
        cda1 = input("Código de acesso: ")
        while True:
            if cnpj != cnpj1:
                print("\nCódigo de acesso ou CNPJ incorreto!")
                cnpj = input("\nCNPJ da empresa(Ex: XX.XXX.XXX/XXXX-XX): ")
                cnpj = cnpj.split("." and "-" and "/")
                cda1 = input("Código de acesso:: ")
            elif cda1 != cdaa:
                print("\nCódigo de acesso ou CNPJ incorreto!")
                cnpj = input("\nCNPJ da empresa(Ex: XX.XXX.XXX/XXXX-XX): ")
                cnpj = cnpj.split("." and "-" and "/")
                cda1 = input("Código de acesso:: ")
            else:
                print("\n", fornecer, "\n", dsc)
                break
        print("Tipo de serviço prestado pela empresa: ", ts)
        print("\nVagas disponiveis:")
        print("\nAuxiliar financeiro")
        print("RH")
        print("Tecnologia")
        print("Vendas & Marketing" )
        print("\nEsses são os canditatos para a empresa ", fornecer)
        print("\n-Adriana Barbosa")
        print("-Caroline Rocha")
        print("-Fernanda Caetano")
        print("-Guilherme Aldeia")
        print("-João Vitor")
        print("-Jônatas Lima Barbosa")        
        print("-Jorge Henrique")
        print("-Rafael Martins")
        print("-Vitor Madureira")
#____________________________________________________7_____________________________________________________________#
    elif escolha == 7:
        print("\nBusines - Soluções de sucesso")
        print("\nSomos uma uma empresa que recebe informações das pessoas que queirão trabalhar, também recebemos informações de empresas que precisão de pessoas qualificadas para as vagas disponiveis.")
        print("A nossa função é fazer um match entre a pessoa candidata e a empresa que nos contratou afim de encontrar profissionais para as vagas disponiveis.\n")
#_____________________________________________________8____________________________________________________________#
    elif escolha == 8:
      print("\nObrigado!\n")
      print("A Busines agradece!")
      break
#______________________________________________________9___________________________________________________________#
    elif escolha >= 9:
        print("\nEscolha inválida!")
else:
    print("\nEscolha inválida!")
