# API Connect - MVP Back-end

API RESTful desenvolvida para a **API Connect**, projetada como um Produto Mínimo Viável (MVP) modular, escalável e de rápida execução para o gerenciamento e persistência de dados de usuários.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**: Linguagem de programação base.
* **Flask**: Microframework para roteamento e tratamento de requisições HTTP.
* **python-dotenv**: Gerenciamento de variáveis de ambiente.
* **UUID (v4)**: Biblioteca nativa para geração de identificadores únicos universais.
* **Git**: Controle de versão.

---

## 📁 Estrutura da Arquitetura

A aplicação segue o princípio da Separação de Responsabilidades (SoC):

```text
api-connect/
├── controllers/
│   └── connect_controller.py   # Regras de negócio e validações
├── data/
│   └── mock_database.py        # Simulação de persistência em memória (RAM)
├── routes/
│   └── connect_routes.py      # Mapeamento e declaração dos endpoints HTTP
├── .env                        # Variáveis de ambiente (ex: PORT)
├── .gitignore                  # Arquivos e pastas ignorados pelo Git
├── app.py                      # Ponto de entrada do servidor Flask
├── README.md                   # Documentação do projeto
└── requirements.txt            # Mapeamento de dependências
