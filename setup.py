from setuptools import setup, find_packages

setup(
    name='fastapi-starter',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn',
        'click',
        'pydantic'
    ],
    entry_points={
        'console_scripts': [
            'fastapi-starter=fastapi_starter.cli:cli',
        ],
    },
    author='Seu Nome',
    description='Biblioteca para criar projetos FastAPI com estrutura completa',
)
