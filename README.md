#  DevOps API Project

![CI](https://img.shields.io/github/actions/workflow/status/Filipcardos/devops-api-project/ci.yml?style=for-the-badge)
![Docker](https://img.shields.io/badge/docker-ready-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

API REST em Flask com PostgreSQL, containerizada com Docker e testada/validada via GitHub Actions.

 Deploy: https://devops-api-project.onrender.com/

## Sobre

Projeto prático de DevOps que demonstra o ciclo completo de uma aplicação: código, testes automatizados, containerização, integração contínua e deploy em cloud.

## Tecnologias

- Python 3.11 / Flask
- PostgreSQL
- Docker / Docker Compose
- GitHub Actions (CI/CD)
- pytest
- Render (deploy)

## Funcionalidades

- Endpoint raiz com status da API
- Health check (`/health`)
- Verificação de conectividade com o banco (`/db-status`)
- Tratamento de erros (404 e 500) com resposta JSON padronizada

## Arquitetura

```text
Cliente → API Flask (Docker) → PostgreSQL
              ↓
      CI/CD (GitHub Actions)
              ↓
        Deploy (Render)
```

## Estrutura do projeto

```text
devops-api-project/
├── app/
│   ├── main.py
│   ├── db.py
│   └── requirements.txt
├── tests/
│   └── test_main.py
├── conftest.py
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── .github/workflows/ci.yml
```

## Como executar localmente

```bash
git clone https://github.com/Filipcardos/devops-api-project.git
cd devops-api-project

cp .env.example .env

docker compose up --build
```

A API ficará disponível em `http://localhost:5000`.

## Variáveis de ambiente

Definidas em `.env.example`:

| Variável       | Descrição                       | Padrão     |
|----------------|----------------------------------|------------|
| `PORT`         | Porta da aplicação                | `5000`     |
| `FLASK_DEBUG`  | Ativa modo debug do Flask         | `false`    |
| `DB_HOST`      | Host do PostgreSQL                | `db`       |
| `DB_PORT`      | Porta do PostgreSQL               | `5432`     |
| `DB_USER`      | Usuário do banco                  | `devops`   |
| `DB_PASSWORD`  | Senha do banco                    | `devops`   |
| `DB_NAME`      | Nome do banco                     | `devopsdb` |

## Docker

```bash
docker compose up --build
```

Sobe a API e um container PostgreSQL. O Dockerfile roda a aplicação com usuário não-root e inclui `HEALTHCHECK`.

## Testes

```bash
pip install -r requirements-dev.txt
pytest
```

Cobrem: resposta da rota principal, health check, rota inexistente (404) e verificação de status do banco.

## CI/CD

Pipeline em `.github/workflows/ci.yml`, executado a cada push/PR na branch `main`:

1. Instala dependências
2. Executa os testes com `pytest`
3. Faz build da imagem Docker
4. Sobe o container e valida o `/health` com `curl`

## Deploy

Aplicação publicada no Render: https://devops-api-project.onrender.com/

> Observação: o plano gratuito do Render pode "hibernar" a aplicação após período de inatividade, tornando a primeira requisição mais lenta.

## Endpoints

| Método | Rota         | Descrição                          |
|--------|--------------|-------------------------------------|
| GET    | `/`          | Mensagem de status da API           |
| GET    | `/health`    | Health check                        |
| GET    | `/db-status` | Verifica conectividade com o banco  |

## Exemplos de requisições

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/db-status
```

## Conceitos demonstrados

- API REST com Flask
- Persistência com PostgreSQL
- Containerização e orquestração com Docker/Docker Compose
- Testes automatizados com pytest
- Pipeline de CI/CD com GitHub Actions
- Boas práticas: variáveis de ambiente, `.gitignore`, tratamento de erros

## Autor

Filipe Oliveira Cardoso

