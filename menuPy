import re

def formatar_data(data_str):
    partes = data_str.split('/')
    if len(partes) == 3:
        dia, mes, ano = partes
        return dia, mes, ano
    return None

def formatar_telefone(telefone_str):
    return re.sub(r"[^\d]", "", telefone_str)

def formatar_cnpj(cnpj_str):
    return re.sub(r"[^\d]", "", cnpj_str)

def criar_senha():
    while True:
        senha = input("Crie sua senha: ")
        senha_confirmada = input("Digite novamente sua senha: ")
        if senha == senha_confirmada:
            print("Senha criada com sucesso!")
            return senha
        print("As senhas não são iguais. Tente novamente.")

def validar_login(tipo_usuario, login, senha):
    while True:
        email_ou_cnpj = input(f"Digite seu {'e-mail' if tipo_usuario == 'candidato' else 'CNPJ'}: ")
        senha_input = input("Digite sua senha: ")
        
        if email_ou_cnpj != login or senha_input != senha:
            print("\nSenha ou e-mail/CNPJ incorretos!")
        else:
            print(f"\nBem-vindo(a), {login}!")
            break

def cadastrar_candidato():
    print("\nCadastro de Candidato:")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    while True:
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        data_formatada = formatar_data(data_nascimento)
        if data_formatada:
            dia, mes, ano = data_formatada
            break
        print("Data inválida. Tente novamente.")

    sexo = input("Sexo (Homem, Mulher, Outro, Não declarado): ")
    telefone = input("Celular (DDD + número): ")
    telefone_formatado = formatar_telefone(telefone)
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    numero_residencia = input("Número da residência: ")
    cep = input("CEP (XXXXX-XXX): ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    print("\nFormação acadêmica:")
    formacao = input("Possui formação acadêmica? (Sim/Não): ")
    if formacao.lower() == "sim":
        curso = input("Curso: ")
        instituicao = input("Instituição: ")
        ano_inicio = input("Ano de início: ")
        ano_conclusao = input("Ano de conclusão: ")

    experiencia = input("Possui experiência de trabalho? (Sim/Não): ")
    if experiencia.lower() == "sim":
        empresas = input("Empresas onde trabalhou: ")
        cargos = input("Cargos ocupados: ")

    idiomas = input("Fluente em quais idiomas? ")
    linguagens_programacao = input("Linguagens de programação que possui mais habilidade: ")

    senha = criar_senha()
    candidato = {
        'nome': nome,
        'telefone': telefone_formatado,
        'email': email,
        'sexo': sexo,
        'endereco': endereco,
        'cep': cep,
        'bairro': bairro,
        'cidade': cidade,
        'estado': estado,
        'formacao': formacao,
        'experiencia': experiencia,
        'idiomas': idiomas,
        'linguagens_programacao': linguagens_programacao,
        'senha': senha
    }
    
    print("\nCadastro de Candidato concluído!")
    return candidato

def cadastrar_empresa():
    print("\nCadastro de Empresa:")
    nome_empresa = input("Nome da empresa: ")
    cnpj = input("CNPJ (XX.XXX.XXX/XXXX-XX): ")
    cnpj_formatado = formatar_cnpj(cnpj)
    tipo_servico = input("Tipo de serviço da empresa: ")
    descricao = input("Descrição da empresa: ")
    email_empresa = input("E-mail: ")
    codigo_acesso = criar_senha()  # Usando a mesma função para criar um código de acesso

    empresa = {
        'nome': nome_empresa,
        'cnpj': cnpj_formatado,
        'tipo_servico': tipo_servico,
        'descricao': descricao,
        'email': email_empresa,
        'codigo_acesso': codigo_acesso
    }

    print("\nCadastro de Empresa concluído!")
    return empresa

def exibir_menu():
    print("\nMenu de Opções:")
    print("1 - Cadastrar candidato")
    print("2 - Cadastrar empresa")
    print("3 - Sobre o processo seletivo")
    print("4 - Vagas disponíveis")
    print("5 - Página para candidato")
    print("6 - Página para empresa")
    print("7 - Sobre a Busines")
    print("8 - Sair")

def main():
    candidatos = []
    empresas = []
    while True:
        exibir_menu()
        escolha = int(input("\nEscolha uma opção: "))
        
        if escolha == 1:
            candidato = cadastrar_candidato()
            candidatos.append(candidato)
        elif escolha == 2:
            empresa = cadastrar_empresa()
            empresas.append(empresa)
        elif escolha == 3:
            print("\nO processo seletivo funciona da seguinte forma:...")
        elif escolha == 4:
            print("\nVagas disponíveis: Vendas, Marketing, RH, Tecnologia, Financeiro.")
        elif escolha == 5:
            print("\nPágina do candidato:")
            login = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            for candidato in candidatos:
                if candidato['email'] == login and candidato['senha'] == senha:
                    print(f"\nBem-vindo, {candidato['nome']}!")
                    break
            else:
                print("E-mail ou senha incorretos.")
        elif escolha == 6:
            print("\nPágina da empresa:")
            login_empresa = input("Digite o CNPJ da empresa: ")
            senha_empresa = input("Digite o código de acesso: ")
            for empresa in empresas:
                if empresa['cnpj'] == login_empresa and empresa['codigo_acesso'] == senha_empresa:
                    print(f"\nBem-vindo, {empresa['nome']}!")
                    break
            else:
                print("CNPJ ou código de acesso incorretos.")
        elif escolha == 7:
            print("\nBusines - Soluções de sucesso.")
        elif escolha == 8:
            print("\nObrigado por utilizar nossos serviços!")
            break
        else:
            print("Escolha inválida!")

if __name__ == "__main__":
    main()
