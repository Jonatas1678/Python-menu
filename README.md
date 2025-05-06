
# Projeto de Cadastro de Candidatos e Empresas

Este é um sistema de cadastro e login para candidatos e empresas, onde candidatos podem se inscrever em processos seletivos e empresas podem cadastrar suas vagas. O sistema também permite que as empresas publiquem informações sobre seus serviços e as vagas disponíveis.

## Funcionalidades

- **Cadastro de Candidato**: O candidato preenche suas informações pessoais, formação acadêmica, experiências anteriores e habilidades.
- **Cadastro de Empresa**: A empresa pode cadastrar seu CNPJ, tipo de serviço, descrição e vagas disponíveis.
- **Login de Candidato e Empresa**: Candidatos e empresas podem se autenticar utilizando e-mail/código de acesso e senha.
- **Exibição de Vagas**: Candidatos podem ver as vagas disponíveis e as empresas podem gerenciar seus anúncios.
- **Processo Seletivo**: O sistema fornece informações sobre o processo seletivo em andamento.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Regex**: Para validação e formatação de entradas como CNPJ, telefone e data.
- **Funções Modularizadas**: Organização do código em funções para garantir modularidade e fácil manutenção.

## Estrutura do Projeto

```
- menu.py            # Arquivo principal que contém a lógica do sistema (versão inicial)
- menuNovo.py         # Arquivo com melhorias e novas funcionalidades
- README.md          # Documento de documentação do projeto
```

## Como Usar

### 1. Cadastro de Candidato

Ao escolher a opção de cadastro de candidato, o usuário preencherá suas informações pessoais, como nome, data de nascimento, telefone, e-mail, endereço e outros dados relacionados à sua formação acadêmica e experiência de trabalho.

### 2. Cadastro de Empresa

A empresa pode cadastrar seu nome, CNPJ, descrição, serviços prestados e um código de acesso para autenticação.

### 3. Login

Tanto candidatos quanto empresas podem realizar o login inserindo suas credenciais (e-mail/cnpj e senha) para acessar suas páginas e gerenciar as informações.

### 4. Menu de Opções

O sistema possui um menu interativo, com as seguintes opções:
- **Cadastrar Candidato**
- **Cadastrar Empresa**
- **Sobre o Processo Seletivo**
- **Vagas Disponíveis**
- **Página para Candidato**
- **Página para Empresa**
- **Sobre a Busines**
- **Sair**

### 5. Validações

O sistema realiza validações básicas, como:
- Formatação de datas e telefones.
- Verificação de e-mail e CNPJ no processo de login.

## Como Executar o Projeto

Para executar o projeto, basta garantir que você tenha o Python instalado em seu computador e rodar o seguinte comando:

```bash
python menu.py
```

Ou, se você preferir usar a versão mais recente do código:

```bash
python menuNovo.py
```

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch para sua funcionalidade (`git checkout -b minha-nova-funcionalidade`).
3. Comite suas alterações (`git commit -am 'Adicionando nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin minha-nova-funcionalidade`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
