# minibot


Aquest repositori és un demostrador de com es poden crear experiències
conversacionals en català, utilitzant tecnologies lingüístiques lliures. 

Està construït amb tecnologies de codi obert de reconeixement de la parla
(STT), síntesi de la parla (TTS) i comprensió de la llengua (NLU). Aquest
repositor té el servidor central de la comprensió de la llengua NLU amb RASA,
els seus connectors al microservei de STT basat en
[Vosk](https://github.com/alphacep/vosk-server), i de TTS basat en
[🐸 Coqui TTS](https://github.com/projecte-aina/tts-api). Es pot interactuar 
amb el xatbot mitjançant una interfície que és disponible
[aquí.](https://github.com/projecte-aina/rasa-voice-interface)

L'arquitectura complet és:

<a target="_blank" title="RASA voice bot" href="https://medium.com/rasa-blog/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools-c05c4ec698c6"><img alt="Generalitat logo" src="https://www.datocms-assets.com/30881/1614699195-fpqdurvj6bpyxacbe4dgr.png"></a>

El demo complet està disponible al [https://bot.aina.bsc.es/](https://bot.aina.bsc.es/).

A més per un desplegament còmode i senzill, aquest repositori també inclou els
fitxers de docker-compose que s'ha utiltizat pel desplegament del demo del
projecte Aina.

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

## Preguntes i respostes
[Document](https://docs.google.com/document/d/1ZOC0wRiWv2Ogmc3kf7xQtD-HhZrFjaF00zKGes5ct90/edit?usp=sharing) amb les preguntes i respostes que pot gestionar el minibot 


## Documentació
* [laguage support](https://rasa.com/docs/rasa/language-support/)
* [installation](https://rasa.com/docs/rasa/installation/)


## Install required models

```bash 
python -m pip install --no-cache-dir --upgrade -r models_requirements.txt
```

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

## Finançament

Aquest projecte té el suport de la the [Generalitat de
Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html) dins del
marc del [Projecte
AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

This work is funded by the [Generalitat de
Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en))
within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

<a target="_blank" title="Generalitat de Catalunya" href="https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina/"><img alt="Generalitat logo" src="https://bot.aina.bsc.es/logos/gene.png" width="400"></a>

