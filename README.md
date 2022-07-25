# Consumo de propiedades
## Microservicio

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Build Status](https://img.shields.io/badge/build-develop-blue.svg)](https://shields.io/)


## Caracteristicas
- Este microservicio consumo la base de datos y regresa las propiedades de acuerdo a los parametros enviados mendiante una peticion HTTP-GET


## Datos tecnicos
tecnologias y librerias utilizadas:

- [Python] - Tecnologia de alto nivel multiparadigma
- [http] - Libreria para la creacion de servidores web
- [json] - Libreria para trabajo de datos con el formato JSON

## Dudas durante el proceso

- [Servicio] - Como crear un microservicio sin usar ningun framework
- [Decorador-Router] - Como utilizar un decorador como un captador de rutas
- [Validar-Parametros] - Validar los parametros que envian y evitar envio de otros


## Resolucion de dudas
- [Servicio] - Durante este proceso pase por la invetigacion sobre crear un API sin utilizar un framework, hasta que llegando a la documentacion
De la tecnologia, encontre con como se creaba nativamente un servidor web, de esta manera encontre la forma de crear un servicio API, 
Sin utilizar alguna framework dedicado para este servicio

- [Decorador-Router] - Tomando de referencia otros frameworks que he utilizado, investigue la manera de como creaban un decorador para asignar
Las rutas sin tener que crear un objecto directo, tal como lo hace DJANGO, siguiendo la idea de Flask y FastAPI, encontre que agregando las rutas a un 
diccionario podriamos ejecutar la funcion sin problema alguno pasando los datos de la funcion al servidor, buscando por el path que se asigno
al momento de crear la aplicacion

- [Validar-Parametros] - Esta forma la solucione creando variables constantes, donde las variables sean los paramentros que enviaremos
de esta manera no podrian pasarnos por alto algun metodo de inyeccion


# Entorno Virtual
## Para este caso se utilizo virtualenv
## Uso 
```sh
virtualenv .venv
source .venv/bin/activate
python3 server.py
```

