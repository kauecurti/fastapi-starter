# FastAPI Starter - Estruturas de Projeto 🚀

Bem-vindo ao **FastAPI Starter**! Este CLI é sua ferramenta definitiva para iniciar projetos FastAPI com uma variedade de estruturas organizacionais, cada uma adaptada a diferentes cenários e necessidades de desenvolvimento. Com apenas um comando, você pode escolher entre **10 templates incríveis** e começar a desenvolver com rapidez, escalabilidade e organização! 😎

---

## 📂 Estruturas Disponíveis

### 1. AWS Structure (`create_aws_structure`) ☁️
Projetado para aplicações que serão implantadas na AWS.
- **Inclui:** Diretórios para templates de CloudFormation e SAM, exemplo de integração com boto3 para listar buckets do S3 e scripts para deploy.
- **Ideal para:** Aplicações nativas na nuvem, serverless, e integrações com AWS (Lambda, S3, DynamoDB, etc.).

---

### 2. Default Structure (`create_default_structure`) 🔹
A estrutura clássica para iniciar um projeto FastAPI com uma base robusta.
- **Inclui:** Diretórios para Kubernetes, código fonte em `src/`, testes, Dockerfile, compose.yaml e arquivos de CI/CD.
- **Ideal para:** Projetos que exigem uma base completa e organizada desde o início.

---

### 3. Minimal Structure (`create_minimal_structure`) ⚡
Uma versão enxuta, contendo somente o essencial para rodar sua API.
- **Inclui:** Um único arquivo de servidor em `src/`, testes básicos e dependências mínimas.
- **Ideal para:** Protótipos, provas de conceito e projetos simples onde menos é mais.

---

### 4. Advanced Structure (`create_advanced_structure`) 🚀
Uma arquitetura modular e bem organizada, ideal para aplicações de médio porte.
- **Inclui:** Diretórios para endpoints, configuração centralizada, modelos, schemas e integração Docker.
- **Ideal para:** APIs que crescem com o tempo e necessitam de uma organização mais refinada.

---

### 5. Enterprise Structure (`create_enterprise_structure`) 🏢
Voltada para grandes projetos corporativos que exigem escalabilidade, segurança e organização rigorosa.
- **Inclui:** Estrutura baseada em domínios com diretórios para serviços, repositórios, autenticação e migrações de banco de dados, além de CI/CD robusto.
- **Ideal para:** Aplicações empresariais complexas que precisam de alta performance e manutenção contínua.

---

### 6. Microservice Structure (`create_microservice_structure`) 🏗️
Projetada para arquiteturas de microsserviços, onde cada serviço é independente e escalável.
- **Inclui:** Estrutura enxuta para cada microsserviço com suporte à orquestração local via Docker Compose e integração com API Gateway.
- **Ideal para:** Sistemas distribuídos, onde a modularidade e independência de serviços são essenciais.

---

### 7. Scalable Structure (`create_scalable_structure`) 📈
Preparada para projetos que precisam crescer rapidamente e suportar alto volume de tráfego.
- **Inclui:** Divisão em módulos, workers para tarefas assíncronas, integração com cache (ex.: Redis), manifestos para Kubernetes e monitoramento de performance.
- **Ideal para:** Projetos que demandam escalabilidade horizontal e vertical com alta performance.

---

### 8. Modular Structure (`create_modular_structure`) 🔧
Uma arquitetura altamente modular que facilita a reutilização de código e a manutenção contínua.
- **Inclui:** Diretórios organizados por módulos independentes com integração de endpoints e configurações globais, além de suporte para testes e containerização via Docker.
- **Ideal para:** Equipes que desejam manter um código organizado, reutilizável e de fácil manutenção.

---

### 9. External API Structure (`create_externalapi_structure`) 🌐
Projetada para aplicações que precisam se comunicar com APIs externas.
- **Inclui:** Um exemplo de rota que realiza chamadas a APIs externas usando a biblioteca `requests`, além de exemplos de testes e configuração de Docker.
- **Ideal para:** Projetos que consomem serviços externos e necessitam de integração rápida com APIs de terceiros.

---

### 10. GraphQL Structure (`create_graphql_structure`) 🗨️
Integra FastAPI com GraphQL utilizando a biblioteca Strawberry, permitindo que você crie uma API GraphQL de forma simples.
- **Inclui:** Definição do schema GraphQL, configuração de rotas para o endpoint GraphQL (HTTP e WebSocket) e exemplo de consulta.
- **Ideal para:** Projetos que preferem a flexibilidade do GraphQL em vez de REST.

---

## 🚀 Como Usar

### 1. Instalação

Instale o FastAPI Starter em modo editável:
```bash
pip install fastapi-starter-template
   ```


**📌 Criando um Novo Projeto:**
   ```bash
    Utilize o CLI para criar um novo projeto, especificando o template desejado:

   fastapi-starter init meu_projeto --template <template>
   ```

## 🚀 Como Usar

1. Exemplos:
   
 ```bash
    aws
    default
    minimal
    advanced
    enterprise
    microservice
    scalable
    modular
```
2. Execute o servidor:
   
bash
   uvicorn src.server:app --reload

3. Acesse a API em http://127.0.0.1:8000

## 🏗️ Deploy

- **Docker**: docker-compose up
- **AWS Lambda**: Utilize os scripts em scripts/ e Terraform
- **Kubernetes**: Aplique os manifestos em infra/k8s/

---
📢 **Dúvidas?** Abra uma issue no repositório! 🚀