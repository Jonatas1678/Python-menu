import json
import re
from datetime import datetime
from pathlib import Path


DATA_FILE = Path(__file__).with_name("dados_busines.json")
VAGAS_PADRAO = [
    "Desenvolvedor(a) Python Júnior",
    "Analista de RH",
    "Assistente Financeiro",
    "Especialista em Vendas",
]


def carregar_dados():
    if not DATA_FILE.exists():
        return {"candidatos": [], "empresas": []}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return {"candidatos": [], "empresas": []}

    dados.setdefault("candidatos", [])
    dados.setdefault("empresas", [])
    return dados


def salvar_dados(dados):
    with DATA_FILE.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


def pedir_texto(mensagem, minimo=1):
    while True:
        valor = input(mensagem).strip()
        if len(valor) >= minimo:
            return valor
        print("Entrada inválida. Tente novamente.")


def pedir_opcao(mensagem, opcoes):
    opcoes_validas = {str(opcao) for opcao in opcoes}
    while True:
        escolha = input(mensagem).strip()
        if escolha in opcoes_validas:
            return escolha
        print("Opção inválida. Escolha uma das opções do menu.")


def validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        return None


def pedir_data(mensagem):
    while True:
        data = input(mensagem).strip()
        data_validada = validar_data(data)
        if data_validada:
            return data_validada
        print("Data inválida. Use o formato dd/mm/aaaa.")


def normalizar_telefone(telefone):
    return re.sub(r"\D", "", telefone)


def pedir_telefone():
    while True:
        telefone = normalizar_telefone(input("Celular com DDD: "))
        if len(telefone) in {10, 11}:
            return telefone
        print("Telefone inválido. Informe DDD e número.")


def validar_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))


def pedir_email(mensagem, emails_existentes=None):
    emails_existentes = emails_existentes or set()
    while True:
        email = input(mensagem).strip().lower()
        if not validar_email(email):
            print("E-mail inválido.")
            continue
        if email in emails_existentes:
            print("Este e-mail já está cadastrado.")
            continue
        return email


def normalizar_cnpj(cnpj):
    return re.sub(r"\D", "", cnpj)


def pedir_cnpj(cnpjs_existentes=None):
    cnpjs_existentes = cnpjs_existentes or set()
    while True:
        cnpj = normalizar_cnpj(input("CNPJ da empresa: "))
        if len(cnpj) != 14:
            print("CNPJ inválido. Informe 14 dígitos.")
            continue
        if cnpj in cnpjs_existentes:
            print("Este CNPJ já está cadastrado.")
            continue
        return cnpj


def criar_segredo(rotulo):
    while True:
        segredo = input(f"Crie {rotulo}: ").strip()
        confirmacao = input(f"Digite novamente {rotulo}: ").strip()
        if len(segredo) < 4:
            print("Use pelo menos 4 caracteres.")
            continue
        if segredo != confirmacao:
            print("Os valores não conferem.")
            continue
        return segredo


def exibir_menu():
    print("\n=== Busines | Plataforma de Talentos ===")
    print("1 - Cadastrar candidato")
    print("2 - Cadastrar empresa")
    print("3 - Sobre o processo seletivo")
    print("4 - Vagas disponíveis")
    print("5 - Área do candidato")
    print("6 - Área da empresa")
    print("7 - Sobre a Busines")
    print("8 - Sair")


def cadastrar_candidato(dados):
    print("\nCadastro de Candidato")
    emails_existentes = {item["email"] for item in dados["candidatos"]}

    nome = pedir_texto("Nome: ")
    sobrenome = pedir_texto("Sobrenome: ")
    data_nascimento = pedir_data("Data de nascimento (dd/mm/aaaa): ")

    print("\nSexo:")
    print("1 - Homem")
    print("2 - Mulher")
    print("3 - Outro")
    print("4 - Prefiro não informar")
    escolha_sexo = pedir_opcao("Escolha uma opção: ", ["1", "2", "3", "4"])
    if escolha_sexo == "1":
        sexo = "Homem"
    elif escolha_sexo == "2":
        sexo = "Mulher"
    elif escolha_sexo == "3":
        sexo = pedir_texto("Informe seu sexo: ")
    else:
        sexo = "Prefiro não informar"

    telefone = pedir_telefone()
    email = pedir_email("E-mail: ", emails_existentes)
    endereco = pedir_texto("Endereço: ")
    numero_residencia = pedir_texto("Número da residência: ")
    cep = pedir_texto("CEP: ")
    bairro = pedir_texto("Bairro: ")
    cidade = pedir_texto("Cidade: ")
    estado = pedir_texto("Estado: ")
    formacao = pedir_texto("Formação acadêmica: ")
    instituicao = pedir_texto("Instituição de ensino: ")
    experiencia = pedir_texto("Resumo da experiência profissional: ")
    idiomas = pedir_texto("Idiomas: ")
    linguagens = pedir_texto("Principais habilidades técnicas: ")
    senha = criar_segredo("sua senha")

    candidato = {
        "nome": nome,
        "sobrenome": sobrenome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
        "numero_residencia": numero_residencia,
        "cep": cep,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "formacao": formacao,
        "instituicao": instituicao,
        "experiencia": experiencia,
        "idiomas": idiomas,
        "linguagens": linguagens,
        "senha": senha,
    }
    dados["candidatos"].append(candidato)
    salvar_dados(dados)

    print(f"\nCadastro concluído para {nome} {sobrenome}.")
    print("Seus dados foram salvos e poderão ser usados no login.")


def cadastrar_empresa(dados):
    print("\nCadastro de Empresa")
    cnpjs_existentes = {item["cnpj"] for item in dados["empresas"]}

    nome_empresa = pedir_texto("Nome da empresa: ")
    cnpj = pedir_cnpj(cnpjs_existentes)
    tipo_servico = pedir_texto("Tipo de serviço prestado: ")
    descricao = pedir_texto("Descrição da empresa: ")
    email = pedir_email("E-mail corporativo: ")
    vagas_texto = pedir_texto("Vagas oferecidas (separe por vírgula): ")
    vagas = [vaga.strip() for vaga in vagas_texto.split(",") if vaga.strip()]
    codigo_acesso = criar_segredo("seu código de acesso")

    empresa = {
        "nome": nome_empresa,
        "cnpj": cnpj,
        "tipo_servico": tipo_servico,
        "descricao": descricao,
        "email": email,
        "vagas": vagas or VAGAS_PADRAO[:],
        "codigo_acesso": codigo_acesso,
    }
    dados["empresas"].append(empresa)
    salvar_dados(dados)

    print(f"\nEmpresa {nome_empresa} cadastrada com sucesso.")
    print("Os dados foram salvos e o login já está disponível.")


def listar_vagas(dados):
    vagas = []
    for empresa in dados["empresas"]:
        for vaga in empresa.get("vagas", []):
            vagas.append((vaga, empresa["nome"]))

    if not vagas:
        print("\nNenhuma vaga cadastrada por empresas ainda.")
        print("Exibindo vagas padrão da plataforma:")
        for vaga in VAGAS_PADRAO:
            print(f"- {vaga}")
        return

    print("\nVagas disponíveis:")
    for vaga, empresa in vagas:
        print(f"- {vaga} | Empresa: {empresa}")


def login_candidato(dados):
    print("\nÁrea do Candidato")
    email = input("Digite seu e-mail: ").strip().lower()
    senha = input("Digite sua senha: ").strip()

    for candidato in dados["candidatos"]:
        if candidato["email"] == email and candidato["senha"] == senha:
            print(f"\nBem-vindo(a), {candidato['nome']}!")
            print(f"Localidade: {candidato['cidade']} - {candidato['estado']}")
            print(f"Formação: {candidato['formacao']} | Instituição: {candidato['instituicao']}")
            print(f"Habilidades: {candidato['linguagens']}")
            return

    print("E-mail ou senha incorretos.")


def login_empresa(dados):
    print("\nÁrea da Empresa")
    cnpj = normalizar_cnpj(input("Digite o CNPJ da empresa: "))
    codigo = input("Digite o código de acesso: ").strip()

    for empresa in dados["empresas"]:
        if empresa["cnpj"] == cnpj and empresa["codigo_acesso"] == codigo:
            print(f"\nBem-vindo(a), {empresa['nome']}!")
            print(f"Serviço: {empresa['tipo_servico']}")
            print(f"Descrição: {empresa['descricao']}")
            print("Vagas anunciadas:")
            for vaga in empresa["vagas"]:
                print(f"- {vaga}")
            print(f"Candidatos cadastrados na plataforma: {len(dados['candidatos'])}")
            return

    print("CNPJ ou código de acesso incorretos.")


def exibir_processo_seletivo():
    print("\nProcesso seletivo")
    print("A Busines centraliza os cadastros, organiza perfis e conecta candidatos às vagas anunciadas pelas empresas.")
    print("Após o cadastro, os dados ficam salvos localmente para consultas e logins posteriores.")


def exibir_sobre():
    print("\nBusines - Soluções de sucesso")
    print("Plataforma de cadastro de candidatos e empresas com foco em recrutamento simplificado.")
    print("Esta versão prioriza fluxo consistente, validações básicas e persistência local em JSON.")


def main():
    dados = carregar_dados()
    while True:
        exibir_menu()
        escolha = pedir_opcao("\nEscolha uma opção: ", [str(numero) for numero in range(1, 9)])

        if escolha == "1":
            cadastrar_candidato(dados)
        elif escolha == "2":
            cadastrar_empresa(dados)
        elif escolha == "3":
            exibir_processo_seletivo()
        elif escolha == "4":
            listar_vagas(dados)
        elif escolha == "5":
            login_candidato(dados)
        elif escolha == "6":
            login_empresa(dados)
        elif escolha == "7":
            exibir_sobre()
        else:
            print("\nObrigado por utilizar a Busines.")
            break


if __name__ == "__main__":
    main()
