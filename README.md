# Nombre del Proyecto

**Microservicio offers**

Este microservicio permite la gestión de las ofertas desde su creación,
eliminación, listados donde muestra todas las ofertas, también filtros
de ofertas propias o de otros usuarios y consulta sobre una oferta en específico. Requiere un nivel de autorización el cual es obtenido consultando
al microservicio de users tras un tocken pasado en como authorization. 


## Índice

1. [Estructura](#estructura)
2. [Ejecución](#ejecución)
3. [Uso](#uso)
4. [Pruebas](#pruebas)
5. [Autor](#autor)

## Estructura

La siguientes es la estructura de archivo de carpetas utilizados para el 
microservicio offers:

```plaintext
.
├── Dockerfile
├── Pipfile
├── README.md
├── .env.development
├── .env.template
├── .env.test
├── src
│   ├── blueprints
│   │   ├── database_managment.py
|   |   ├── offer.py
|   |   └── ping.py
│   ├── clients
│   │   └── user_client.py
│   ├── commands
│   │   ├── __init__.py
│   │   ├── base_command.py
│   │   ├── create_offer.py
│   │   ├── delete_offer.py
│   │   ├── get_list_offer.py
│   │   ├── get_offer.py
│   │   ├── pong.py
│   │   └── reset.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── errors.py
│   ├── models
│   |   ├── __init__.py
│   |   └── model.py
│   ├── utils
│   |   └── uuid.py
│   ├── __init__.py
│   └── main.py
└── tests
    ├── blueprints
    |   ├── test_database_managment.py
    |   ├── test_offer.py
    |   └── test_ping.py
    ├── clients
    |   └── test_user_client.py
    ├── commands
    |   ├── test_create_offer.py
    |   ├── test_delete_offer.py
    |   └── test_get_offer.py
    ├── utils
    |   └── test_uuid.py
    ├── __init__.py
    └── conftest.py
```

## Ejecución

Se utiliza la versión de python 3.9

**Con docker (recomendado)**

Para ejecutar el microservicio de offers requiere tener instalado el demonio de docker y seguir los siguientes pasos de:

1. Crear un archivo .env.development en la carpeta de offer donde dentro de este 
definirá las variables de entorno para conectarse a la base de datos con la
conexión preestablecida que está en el docker-compose.yml y al servicio de users, de la siguiente manera:

DB_USER=admin

DB_PASSWORD=miso4301

DB_HOST=offers_db

DB_PORT=5432

DB_NAME=offerdb

USERS_PATH=http://users:3000

2. Posicionese en la raíz de todo el proyecto donde encontrará un archivo docker-compose.yml

3. Ejecute el comando que levantará un contenedor para el microservicio offer y otro contenedor para la base de datos en postgresql
```bash
docker compose up -d offers offers_db
```

**IMPORTANTE:** Recuerde que debe también levantar el microservicio de users, debido a que offers requiere de la autorización que users da sobre los tokens,
de lo contrario las peticiones resultarán en un error de conexión hacia el microservicio de users. 

**Con pipenv**
Para usar esta opción recuerde instalar primero pipenv en su máquina y siga los
siguientes pasos:

1. Iniciar el shell de pipenv
```bash
pipenv shell
```

2. Instalar las dependencias
```bash
pipenv install
```

3. Conexion a la base de datos
Para esto tiene dos opciones
**opcion a:**
- Crear una base de datos postgreSQL en su máquina local
- Poner todos los datos de esa conexión en el archivo .env.development

DB_USER=

DB_PASSWORD=

DB_HOST=

DB_PORT=

DB_NAME=

USERS_PATH=http://users:3000

**opcion b:**
- Levantar la base de datos de sqlite que fue definida en el proyecto
para los tests
- Poner todos los datos de esa conexión en el archivo .env.test

DB_USER=

DB_PASSWORD=

DB_HOST=

DB_PORT=

DB_NAME=

USERS_PATH=http://users:3000

- Descomentar la línea que contiene MODE_TEST="test" del archivo .env.test

4. Correr el microservicio
```bash
FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3003
```

**IMPORTANTE:** Recuerde que debe también levantar el microservicio de users, debido a que offers requiere de la autorización que users da sobre los tokens,
de lo contrario las peticiones resultarán en un error de conexión hacia el microservicio de users. 

## Uso

Para usar el microservicio puede usar la siguiente colección de postman en la carpeta de Offers
https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

**IMPORTANTE:** Recuerde que para poder usar el microservicio debe primero correr el endpoint de users de "Creación de usuarios" y luego el de "Generaación de token" para obtener un token valido que permita realizar las peticiones a offers.

A continuación encontrará algunos endpoints principales del microservicio,
los endpoints completos los verá en el postman mencionado anteriormente.

### 1. Creación de una oferta

Crea una oferta con los datos proporcionados, solo un usuario autorizado puede realizar esta operación.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/offers</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>

```Authorization: Bearer token```
</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
{
    "postId": id post relacionado a la oferta,
    "description": descripcion de la oferta,
    "size": tamaño que sea SMALL MEDIUM o LARGE,
    "fragile": true o false,
    "offer": precio de la oferta
}
```
</td>
</tr>
</table>

### 2. Listar todas las ofertas

Acá usted puede observar el listado de todas las ofertas registradas en la aplicación

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/offers</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>

```Authorization: Bearer token```
</td>
</tr>
<tr>
<td> Cuerpo </td>
<td> N/A </td>
</tr>
</table>

### 3. Consultar oferta específica

Retorna una oferta específica de acuerdo con el id suministrado, solo un usuario autorizado puede realizar esta operación.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/offers/{id}</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> id: identificador de la oferta </td>
</tr>
<tr>
<td> Encabezados </td>
<td>

```Authorization: Bearer token```
</td>
</tr>
<tr>
<td> Cuerpo </td>
<td> N/A </td>
</tr>
</table>


### 4. Eliminar oferta específica

Elimina una oferta específica de acuerdo con el id suministrado, solo un usuario autorizado puede realizar esta operación.

<table>
<tr>
<td> Método </td>
<td> DELETE </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/offers/{id}</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> id: identificador de la oferta </td>
</tr>
<tr>
<td> Encabezados </td>
<td>

```Authorization: Bearer token```
</td>
</tr>
<tr>
<td> Cuerpo </td>
<td> N/A </td>
</tr>
</table>

### 5. Consulta de salud del servicio

Usado para verificar el estado del servicio.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/offers/ping</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td> N/A </td>
</tr>
</table>

### 6. Restablecer base de datos

Usado para limpiar la base de datos del servicio.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>/offers/reset</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td> N/A </td>
</tr>
</table>

## Pruebas

Para correr las puebas del proyecto ejecutar los siguientes comandos: 

```bash
pipenv shell
```
```bash
pipenv run pytest --cov=src -v -s --cov-fail-under=70
```
o

```bash
pytest --cov=src -v -s --cov-fail-under=70
```
## Autor

Tomas Octavio Rodriguez Herrera