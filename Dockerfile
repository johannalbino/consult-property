# Pega a imagem do debian com o python3 instalado
FROM python:3.8-slim-buster

# Remove o delay do log
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

# Cria a pasta do projeto /code
RUN mkdir /code

# Coloca o /code como diretório principal
WORKDIR /code

# Adiciona o requirements.txt na pasta code
ADD requirements.txt /code/

# Instala as dependencias do projeto no docker
RUN pip install -r requirements.txt

# Adicionar o código no /code/
ADD . /code/

# Executa os testes
RUN pytest

# Valida pep8
RUN flake8

EXPOSE 8000

ENTRYPOINT gunicorn app:app --reload -k uvicorn.workers.UvicornWorker