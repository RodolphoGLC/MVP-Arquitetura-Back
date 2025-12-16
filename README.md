# 🎴 Pokémon Team Builder

Aplicação **full stack** para criação, edição e gerenciamento de **times Pokémon**, permitindo montar equipes de forma visual e intuitiva, com dados oficiais obtidos da **PokéAPI**.

O projeto é composto por:
- **Front-end** em React
- **Back-end** em FastAPI
- **Banco de dados** PostgreSQL

Toda a aplicação é executada em conjunto utilizando **Docker Compose**, garantindo um ambiente padronizado e fácil de subir.

---

## ✨ Funcionalidades

### Back-end
- CRUD completo de times Pokémon
- Associação de Pokémon a um time
- Persistência dos dados em PostgreSQL
- API REST documentada com Swagger

---

## 🌐 API Externa

O projeto utiliza a **PokéAPI** para obter informações oficiais dos Pokémon, porém apenas no front

---

## 🛠️ Tecnologias Utilizadas

### Back-end
- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn

### Banco de Dados
- PostgreSQL

### Infraestrutura
- Docker
- Docker Compose

---

## 🔗 Integração com o Front-end

O back-end se comunica com o front, responsável por:

- Exibir as informações dos times
- Pedir as requisições (Get, Post, Put e Delete)

A comunicação ocorre via **HTTP (REST)** utilizando `fetch`.

---

## 🚀 Como Rodar o Projeto

⚠️ **Este back-end não deve ser executado isoladamente.**  
Ele depende do front-end e do banco de dados.

---

### Pré-requisitos

- Docker
- Docker Compose

---

### ▶️ Subindo Front + Back

Na **raiz do projeto** (onde está o `docker-compose.yml`), execute:

```bash
docker compose up --build
```

Este comando irá:

- Subir o banco PostgreSQL
- Subir o back-end (FastAPI)
- Subir o front-end (React)

---

## 🌐 Acessos

| Serviço | URL |
|------|-----|
| Front-end | http://localhost:5173 |
| Back-end (API) | http://localhost:8000 |
| Swagger | http://localhost:8000/docs |
| Redoc | http://localhost:8000/redoc |

---

## ⚙️ Observações Importantes

- Não é necessário rodar `npm install`
- O front já está configurado para consumir a API via Docker Network
- Comunicação HTTP realizada com `fetch`
- O front e o back devem rodar na **mesma stack Docker**

---

## 📌 Considerações Finais

Este projeto foi desenvolvido com foco em:

- Arquitetura Full Stack
- Integração entre front-end e back-end
- Uso de APIs REST
- Containerização com Docker