# Sistema de Autenticação de Usuários em Python

Este projeto implementa um sistema de autenticação de usuários em Python, com interface gráfica personalizada, utilizando as bibliotecas CustomTkinter e SQL Alchemy. 

Desenvolvido com a abordagem TDD, seguindo os princípios de Clean Code e a metodologia SOLID, garante a segurança dos dados dos usuários e um código de fácil manutenção.

## Funcionalidades

- Cadastro de usuários com validação de campos, garantindo dados corretos e completos.
- Login de usuários com autenticação, verificando a identidade do usuário e a validade das credenciais.
- Criptografia dos dados de senha armazenados no banco de dados, protegendo a confidencialidade das informações sensíveis.
- Interface gráfica personalizada e intuitiva, proporcionando uma experiência amigável para os usuários.
- Implementação da abordagem TDD (Test-Driven Development), onde os testes são escritos antes da implementação do código, assegurando a qualidade e a robustez do sistema.

## Pré-requisitos

- Python 3.10.x instalado
- Bibliotecas:
    - CustomTkinter (para a interface gráfica)
    - SQL Alchemy (para conexão com o banco de dados)
    - Pytest (para execução dos testes)
    - SQLite3 (já vem instalada com o Python)

## Instalação

1. Clone o repositório para o seu ambiente local:
`git clone https://github.com/MauPxt/SistemaLoginCadastro.git`

2. Acesse o diretório do projeto: `cd sistema-login-cadastro`

3. (Opcional) Crie um ambiente virtual para o projeto: `python -m venv venv` e ative-o: `source venv/bin/activate`

4. Instale as dependências do projeto: `pip install -r requirements.txt`


## Utilização

1. Execute o arquivo `main.py` para iniciar a aplicação: `python src/main.py`

2. A aplicação abrirá uma janela de interface gráfica onde você poderá realizar o cadastro de usuários e fazer login.

## Testes

![tests_result.png](tests_results.png)

O projeto utiliza a abordagem TDD (Test-Driven Development) e contém testes unitários para os principais componentes. Para executar os testes, utilize o seguinte comando: `python -m pytest tests/`


## Contribuição

Contribuições são bem-vindas! Se você encontrou algum problema, tem alguma sugestão ou deseja adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
