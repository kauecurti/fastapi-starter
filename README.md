# FastAPI Starter - Estruturas de Projeto 🚀

Bem-vindo ao **FastAPI Starter**! Este CLI permite que você inicie seu projeto FastAPI escolhendo entre **8 estruturas** distintas, cada uma ideal para diferentes cenários de desenvolvimento. Escolha a que melhor se adapta às suas necessidades e comece a desenvolver com rapidez e organização! 😎

---

## 📂 Estruturas Disponíveis

### 1️⃣ AWS Structure (create_aws_structure) ☁️
Projetado para aplicações que serão implantadas na AWS.  
**Inclui:**  
- Diretórios para templates de CloudFormation e SAM  
- Exemplo de integração com boto3 para listar buckets do S3  
- Scripts para deploy e configurações para ambiente serverless

**Ideal para:** Aplicações nativas na nuvem, serverless, e integrações com AWS (Lambda, S3, DynamoDB, etc.).

---

### 2️⃣ Default Structure (create_default_structure) 🔹
A estrutura clássica para iniciar um projeto FastAPI com organização robusta.  
**Inclui:**  
- Diretórios para Kubernetes, código fonte em `src/`, e testes  
- Exemplo de servidor FastAPI com rota simples  
- Dockerfile, compose.yaml, e arquivos de CI/CD

**Ideal para:** Projetos que exigem uma base completa e organizada desde o início.

---

### 3️⃣ Minimal Structure (create_minimal_structure) ⚡
Uma versão enxuta, contendo somente o essencial para rodar sua API.  
**Inclui:**  
- Código fonte mínimo em `src/` com um único arquivo de servidor  
- Testes básicos e dependências essenciais

**Ideal para:** Protótipos, provas de conceito e projetos simples onde menos é mais.

---

### 4️⃣ Advanced Structure (create_advanced_structure) 🚀
Uma estrutura modular e bem organizada, perfeita para aplicações de médio porte.  
**Inclui:**  
- Diretórios para endpoints, configuração centralizada, modelos e schemas  
- Exemplo de rota avançada e Dockerfile configurado  
- Suporte para ambientes de desenvolvimento com CI/CD

**Ideal para:** APIs que crescem com o tempo e necessitam de uma organização mais refinada.

---

### 5️⃣ Enterprise Structure (create_enterprise_structure) 🏢
Voltada para grandes projetos corporativos que exigem escalabilidade, segurança e organização rigorosa.  
**Inclui:**  
- Estrutura baseada em domínios com diretórios para serviços, repositórios e autenticação  
- Scripts e configurações para migrações de banco de dados e CI/CD robusto  
- Dockerfile, compose.yaml e integração com pipelines de deploy

**Ideal para:** Aplicações empresariais complexas que precisam de alta performance e manutenção contínua.

---

### 6️⃣ Microservice Structure (create_microservice_structure) 🏗️
Projetada para arquiteturas de microsserviços, onde cada serviço é independente e escalável.  
**Inclui:**  
- Estrutura enxuta para cada microsserviço, com API Gateway e orquestração local via Docker Compose  
- Exemplo de integração com serviços isolados e rotas simples

**Ideal para:** Sistemas distribuídos, onde a modularidade e independência de serviços são essenciais.

---

### 7️⃣ Scalable Structure (create_scalable_structure) 📈
Preparada para projetos que precisam crescer rapidamente e suportar alto volume de tráfego.  
**Inclui:**  
- Divisão clara em módulos, com workers para tarefas assíncronas e integração com cache (ex.: Redis)  
- Arquivos para implantação em Kubernetes e monitoramento de performance  
- Exemplo de rotas e estrutura preparada para escalabilidade

**Ideal para:** Projetos que demandam escalabilidade horizontal e vertical, com alta performance.

---

### 8️⃣ Modular Structure (create_modular_structure) 🔧
Uma arquitetura altamente modular, facilitando a reutilização de código e manutenção contínua.  
**Inclui:**  
- Diretórios organizados por módulos independentes com endpoints e configurações globais  
- Exemplo de integração entre módulos e uma API principal que agrega as funcionalidades
- Suporte para testes e containerização via Docker

**Ideal para:** Equipes que desejam manter um código organizado, reutilizável e de fácil manutenção.

---

## 🚀 Como Usar

1. **Instale o FastAPI Starter (modo editável):**
   ```bash
   pip install -e .
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