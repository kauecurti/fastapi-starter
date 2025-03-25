import os
import sys
import click

@click.group()
def cli():
    """CLI para inicializar um projeto FastAPI com a estrutura completa."""
    pass

@cli.command()
@click.argument('project_name')
def init(project_name):
    """
    Cria a estrutura completa do projeto a partir do diretório informado.
    
    Exemplo:
      fastapi-starter init meu_projeto
    """
    try:
        base = os.path.join(os.getcwd(), project_name)

        # Verifica se o diretório já existe
        if os.path.exists(base):
            click.echo(f"O diretório '{base}' já existe.")
            use_existing = click.confirm("Deseja usar esse diretório existente?", default=True)
            if not use_existing:
                click.echo("Operação cancelada.")
                sys.exit(1)
        else:
            create_new = click.confirm("O diretório não existe. Deseja criar um novo projeto?", default=True)
            if create_new:
                os.makedirs(base)
            else:
                click.echo("Operação cancelada.")
                sys.exit(1)

        # Cria os diretórios principais (mesmo que já existam, exist_ok=True evita erro)
        directories = [
            os.path.join(base, "k8s"),
            os.path.join(base, "src", "app", "motor"),
            os.path.join(base, "tests"),
        ]
        for d in directories:
            os.makedirs(d, exist_ok=True)

        # Arquivo: src/app/motor/__init__.py
        motor_init = os.path.join(base, "src", "app", "motor", "__init__.py")
        with open(motor_init, "w") as f:
            f.write("# Módulo motor\n")

        # Arquivo: src/server.py - Aplicação FastAPI com rotas de exemplo
        server_file = os.path.join(base, "src", "server.py")
        with open(server_file, "w") as f:
            f.write(
                "from fastapi import FastAPI, HTTPException\n"
                "from pydantic import BaseModel\n\n"
                "app = FastAPI()\n\n"
                "# Simulação de banco de dados em memória\n"
                "db = []\n\n"
                "class Item(BaseModel):\n"
                "    id: int\n"
                "    name: str\n"
                "    description: str = None\n\n"
                "@app.get('/')\n"
                "def read_root():\n"
                "    return {\"message\": \"API FastAPI rodando\"}\n\n"
                "@app.get('/items/{item_id}')\n"
                "def read_item(item_id: int):\n"
                "    for item in db:\n"
                "        if item['id'] == item_id:\n"
                "            return item\n"
                "    raise HTTPException(status_code=404, detail='Item não encontrado')\n\n"
                "@app.post('/items/')\n"
                "def create_item(item: Item):\n"
                "    db.append(item.dict())\n"
                "    return item\n\n"
                "@app.put('/items/{item_id}')\n"
                "def update_item(item_id: int, item: Item):\n"
                "    for i, existing in enumerate(db):\n"
                "        if existing['id'] == item_id:\n"
                "            db[i] = item.dict()\n"
                "            return item\n"
                "    raise HTTPException(status_code=404, detail='Item não encontrado')\n\n"
                "@app.delete('/items/{item_id}')\n"
                "def delete_item(item_id: int):\n"
                "    global db\n"
                "    db = [item for item in db if item['id'] != item_id]\n"
                "    return {\"message\": \"Item deletado\"}\n"
            )

        # Arquivo: tests/__init__.py (pode ser vazio)
        tests_init = os.path.join(base, "tests", "__init__.py")
        with open(tests_init, "w") as f:
            f.write("# Inicializa pacote de testes\n")

        # Arquivo: requirements.txt
        req_file = os.path.join(base, "requirements.txt")
        with open(req_file, "w") as f:
            f.write("fastapi\nuvicorn\nclick\npydantic\n")

        # Arquivo: azure-pipelines.yaml (exemplo simples)
        azure_file = os.path.join(base, "azure-pipelines.yaml")
        with open(azure_file, "w") as f:
            f.write(
                "trigger:\n"
                "  - main\n\n"
                "pool:\n"
                "  vmImage: 'ubuntu-latest'\n\n"
                "steps:\n"
                "  - script: echo Building the project...\n"
                "    displayName: 'Build Step'\n"
            )

        # Arquivo: .dockerignore
        dockerignore_file = os.path.join(base, ".dockerignore")
        with open(dockerignore_file, "w") as f:
            f.write(
                "__pycache__\n"
                "*.pyc\n"
                "venv/\n"
                ".git\n"
            )

        # Arquivo: .env (exemplo de variáveis de ambiente)
        env_file = os.path.join(base, ".env")
        with open(env_file, "w") as f:
            f.write("DEBUG=True\nPORT=8000\n")

        # Arquivo: .gitignore
        gitignore_file = os.path.join(base, ".gitignore")
        with open(gitignore_file, "w") as f:
            f.write(
                "venv/\n"
                "__pycache__/\n"
                "*.pyc\n"
                ".env\n"
                ".dockerignore\n"
            )

        # Arquivo: .gitmodules (exemplo, se houver submódulos)
        gitmodules_file = os.path.join(base, ".gitmodules")
        with open(gitmodules_file, "w") as f:
            f.write("# Exemplo de configuração de submódulos\n")

        # Arquivo: compose.yaml (docker-compose)
        compose_file = os.path.join(base, "compose.yaml")
        with open(compose_file, "w") as f:
            f.write(
                "version: '3.8'\n"
                "services:\n"
                "  web:\n"
                "    build: .\n"
                "    ports:\n"
                "      - \"8000:8000\"\n"
                "    volumes:\n"
                "      - ./src:/app\n"
            )

        # Arquivo: Dockerfile (configurado com imagem oficial Python)
        dockerfile_file = os.path.join(base, "Dockerfile")
        with open(dockerfile_file, "w") as f:
            f.write(
                "FROM python:3.9-slim\n\n"
                "WORKDIR /app\n\n"
                "# Copia e instala as dependências\n"
                "COPY requirements.txt ./\n"
                "RUN pip install --no-cache-dir -r requirements.txt\n\n"
                "# Copia o código fonte\n"
                "COPY src ./src\n\n"
                "EXPOSE 8000\n\n"
                "CMD [\"uvicorn\", \"src.server:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n"
            )

        # Arquivo: jenkinsfile (exemplo básico de pipeline)
        jenkinsfile_file = os.path.join(base, "jenkinsfile")
        with open(jenkinsfile_file, "w") as f:
            f.write(
                "pipeline {\n"
                "  agent any\n"
                "  stages {\n"
                "    stage('Build') {\n"
                "      steps {\n"
                "        sh 'echo Building project'\n"
                "      }\n"
                "    }\n"
                "    stage('Test') {\n"
                "      steps {\n"
                "        sh 'echo Running tests'\n"
                "      }\n"
                "    }\n"
                "  }\n"
                "}\n"
            )

        # Arquivo: README.md
        readme_file = os.path.join(base, "README.md")
        with open(readme_file, "w") as f:
            f.write(
                f"# {project_name}\n\n"
                "Projeto criado com FastAPI Starter.\n\n"
                "## Estrutura do Projeto\n"
                "- k8s/ : Manifestos do Kubernetes\n"
                "- src/ : Código fonte da aplicação\n"
                "  - app/ : Módulos da aplicação (motor, etc.)\n"
                "  - server.py : Arquivo principal do FastAPI\n"
                "- tests/ : Testes automatizados\n"
                "- requirements.txt : Dependências\n"
                "- Dockerfile, compose.yaml, azure-pipelines.yaml, jenkinsfile: Arquivos de CI/CD e Docker\n\n"
                "## Como rodar localmente\n\n"
                "1. Instale as dependências:\n"
                "   ```bash\n"
                "   pip install -r requirements.txt\n"
                "   ```\n"
                "2. Rode a aplicação:\n"
                "   ```bash\n"
                "   uvicorn src.server:app --reload\n"
                "   ```\n"
            )

        click.echo(f"Projeto '{project_name}' criado com sucesso!")
    except Exception as e:
        click.echo(f"Erro ao criar o projeto: {e}")
        sys.exit(1)

if __name__ == '__main__':
    cli()
