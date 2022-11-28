# minibot

Bot petitet de prova, per intentar incorporar-li veu.

## Instruccions bàsiques
0) crear en venv
```
python3 -m venv myvenv
```

1) activar el venv
```
source myvenv/bin/activate
```
Instal·lar els requirements si no s'ha fet abans:
```
pip install -r requirements.txt
```

2) entrenar
```
rasa train
```

3) provar-lo 
```
rasa shell
```
\restart: torna a començar la conversa
\stop: surt de la conversa

### altres instruccions útils:
* rasa data validate: comprova la consistència de les dades
* rasa test: avalua els models a partir de les converses de test (demoment no en tenim)
* rasa interactive: fa una sessió d'aprenentatge interactiu
* rasa shell nlu: per veure en el terminal les mètriques de cada interacció

## Per fer-lo córrer en un navegador
1) Haver clonat [aquest repo](https://github.com/petr7555/rasa-dev-tutorial/) i instal·lat el venv.

2) En el directori on tenim el minibot

```
rasa run --cors "*"
```

3) En un altre terminal:

```
cd rasa-dev-tutorial/
souce venv/bin/activate
cd webchat/
npx http-server .
``` 

4) Obrir el navegador i anar a http://127.0.0.1:8080/

## Preguntes i respostes
[Document](https://docs.google.com/document/d/1ZOC0wRiWv2Ogmc3kf7xQtD-HhZrFjaF00zKGes5ct90/edit?usp=sharing) amb les preguntes i respostes que pot gestionar el minibot 



## Documentació
* [laguage support](https://rasa.com/docs/rasa/language-support/)
* [installation](https://rasa.com/docs/rasa/installation/)

## Build rasa docker image

To build rasa docker image use: 

```bash
docker build -t bsctemu/aina-minibot:latest -t bsctemu/aina-minibot:<YOUR_VERSION> .
```

Then, push the image to docker hub:

```bash
docker push bsctemu/aina-minibot:<YOUR_VERSION>
```


## Build custom actions docker image (action server)

If you made any changes to the custom actions, then build the image with:
``` bash
docker build . -t bsctemu/aina-minibot-custom-actions-server:<YOUR_VERSION> -f DockerfileActions
docker tag bsctemu/aina-minibot-custom-actions-server:<YOUR_VERSION> bsctemu/aina-minibot-custom-actions-server:latest
docker push bsctemu/aina-minibot-custom-actions-server:latest

```

## Deploy via docker compose (using Rasa X)

Download and run Rasa X install script
```bash
curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/1.1.4/install.sh
sudo bash ./install.sh
```

Clone this repo
```bash
git clone https://github.com/projecte-aina/minibot.git
```

Copy docker-compose.override.yml to Rasa X folder
```bash
cp minibot/rasax/docker-compose.override.yml /etc/rasa/docker-compose.override.yml
```

Start Rasa X and create new user for Rasa X admin panel 
```bash
cd /etc/rasa
docker compose up -d
sudo python3 rasa_x_commands.py create --update admin admin <some password here>
```
