# Projeto Busines

Sistema em Python para cadastro e autenticação de candidatos e empresas em um fluxo simples de recrutamento.

## Evoluções implementadas

- Cadastro de candidatos com validação de data, telefone e e-mail.
- Cadastro de empresas com validação e normalização de CNPJ.
- Persistência local em `dados_busines.json`, mantendo os dados após fechar o programa.
- Login funcional para candidato e empresa usando os dados cadastrados.
- Listagem de vagas baseada nas empresas cadastradas.
- Código reorganizado em funções menores e reutilizáveis.

## Estrutura

```text
menu.py       # Versão inicial do projeto
menuNovo.py   # Versão evoluída com persistência e validações
README.md     # Documentação
```

## Como executar

```bash
python menuNovo.py
```

## Fluxo principal

1. Cadastre candidatos e empresas.
2. Os dados são gravados automaticamente em `dados_busines.json`.
3. Use a área do candidato ou da empresa para testar o login.
4. Consulte as vagas disponíveis no menu principal.

## Observações

- O projeto usa apenas bibliotecas padrão do Python.
- `menu.py` foi mantido como versão legada para comparação.
- Arquivos locais do editor e o banco JSON foram adicionados ao `.gitignore`.
