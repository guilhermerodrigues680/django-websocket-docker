<h1 align="center">
  <br>
  <a><img src="https://github.com/guilhermerodrigues680/django-websocket-docker/blob/master/docs/images/django-logo-positive.svg" alt="django" height="208" width="208"></a>
  <a><img src="https://github.com/guilhermerodrigues680/django-websocket-docker/blob/master/docs/images/docker.svg" alt="docker" height="208" width="208"></a>
  <br>
  Django , Websocket e Docker
  <br>
</h1>

<h2 align="center">Chat ultilizando Websocket com Django Channels e conteinerização de aplicação com Docker</h2>

<p align="center">
    <a alt="Python 3"><img src="https://img.shields.io/badge/Python-3-orange.svg" /></a>
    <a alt="Django v2.2.3"><img src="https://img.shields.io/badge/Django-2.2.3-brightgreen.svg" /></a>
    <a alt="Django Channels v2.2.0"><img src="https://img.shields.io/badge/Django%20Channels-2.2.0-yellowgreen.svg" /></a>
    <a alt="Docker v18"><img src="https://img.shields.io/badge/Docker-v18-orange.svg" /></a>
    <a alt="License MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
</p>

### Tabela de Conteúdo ###
1. [Executando a aplicação fora do Docker](#Executando-a-aplicação-fora-do-Docker)
2. [Executando a aplicação no Docker](#Executando-a-aplicação-no-Docker)
3. [Usando a aplicação](#Usando-a-aplicação)
4. [Contributor](#Contributor)
5. [License](#License)


### Executando a aplicação fora do Docker ###

```sh
# Criar venv
python3 -m venv myvenv
# Ative a venv
source myvenv/bin/activate
# Acesse a pasta mysite que contém o código da aplicação
cd mysite
# Atualizar o pip3 (Gerenciador de pacotes python3)
python3 -m pip install --upgrade pip
# O arquivo "requirements.txt" guarda as dependências que serão instaladas utilizando o pip install
pip install -r requirements.txt
# Inicie o web server de desenvolvimento do Django
python3 manage.py runserver 0.0.0.0:8000
# Após estes procedimentos a aplição estará responde na porta 8000
```


### Executando a aplicação no Docker ###

**Dica:** Use o [Play with Docker](https://labs.play-with-docker.com/) para testar a aplicação online sem instalar nada!  

```sh
# Acesse a pasta mysite que contém o código da aplicação
cd mysite
# Inicie o container da aplicação (Primeiro plano)
docker-compose up --build
# OU Inicie o container da aplicação em Segundo plano
docker-compose up -d --build
# Após estes procedimentos a aplição estará responde na porta 8000
```


### Usando a aplicação ###

Acesse o chat em: `http://ip:8000/chat`  
Ex: A maquina que esta executando a aplicação possui o ip 192.168.15.2, assim,  
o chat será acessado em: `http://192.168.15.2:8000/chat`  

Após acessar o chat, digite o nome da sala que deseja usar para bate-papo (pode ser qualquer nome)  
E pressione a tecla `ENTER` ou clique no botão `enter`  
Faça o mesmo (entre na mesma sala) em outra aba do navegador, ou em outro navegador ou em algum dispositivo que esteja na mesma rede  

A página que se abriu é onde serão trocadas as mensagens do bate-papo.  
As mensagens são sincronizadas em todos os dispositivos que estão com a mesma sala aberta.  


### Contributor ###
[LinkedIn: Guilherme Rodrigues](https://www.linkedin.com/in/guilherme-r-54380b106/)

### License ###
This project is licensed under the terms of the MIT license.