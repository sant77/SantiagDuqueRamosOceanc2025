![Static Badge](https://img.shields.io/badge/Orquestador-langchain-green?style=flat&logo=langchain)
![Static Badge](https://img.shields.io/badge/Python-3.9%2F3.11-green?style=flat&logo=python)
![Static Badge](https://img.shields.io/badge/Conteiner-docker-blue?style=flat&logo=docker)
![Static Badge](https://img.shields.io/badge/Service-fastapi-blue?style=flat&logo=fastapi)
![Static Badge](https://img.shields.io/badge/Database-postgresql-blue?style=flat&logo=postgresql)
![Static Badge](https://img.shields.io/badge/LLM-Gemini-blue?style=flat&logo=googlegemini)

# Mars Weather API👽

Este proyecto permite consultar, almacenar y analizar datos meteorológicos de Marte obtenidos a través de la API InSight: Mars Weather Service de la NASA.

El flujo general es:

1. Obtención de datos desde la API de la NASA.

2. Almacenamiento en PostgreSQL para mantener un histórico de temperaturas marcianas.

3. Interacción con un agente orquestado con LangChain y Gemini, que responde preguntas sobre el clima en Marte usando los datos almacenados.

## Endpoints Principales 🌐

### `GET /mars_weather/get_data`
Obtiene registros meteorológicos de Marte desde la API de la NASA y los guarda en la base de datos.

Si un registro ya existe, se actualiza con la información más reciente.

### `POST /mars_weather/get_data_db`
Consulta un registro de la base de datos correspondiente a un sol marciano específico.

cuerpo de la petición:

```bash
    {
    "sol":día_marciano
    }
```
## Chat con Samanta

Puedes chatear con Samanta a través de http://localhost:8501/ para obtener respuesta de los datos guardados.
<img align='center' src="images/samanta.jpg" width="500">

Los datos guardados son los siguientes:

- sol (int): Número del día marciano.
- average_temperature (float): Temperatura promedio en grados Celsius.
- max_temperature (float): Temperatura máxima en grados Celsius.
- min_temperature (float): Temperatura mínima en grados Celsius.
- season (str): Estación del año en Marte.
- month_ordinal (int): Mes del año en Marte (1-12).
- date_start (datetime): Fecha y hora terrestre de inicio de la toma de datos.
- date_end (datetime): Fecha y hora de terrestre de la toma de datos.
# Organización del proyecto 🛠

## Organización del API
- controllers/: → Define los endpoints de la API.
- services/: → Lógica de negocio.
- helpers/: → Utilidades y conexión a la base de datos.
- data/: → Modelos y funciones CRUD.

## Organización del agente

- agent/: → Define las herramientas y promt del agente

# Despligue 🐋

## 1️⃣Variables de entorno
Crea un archivo .env en la raíz del proyecto con las siguientes variables:
```bash
    NASA_API_KEY=your_nasa_api_key
    GOOGLE_API_KEY=your_google_api_key
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=your_database
    POSTGRES_PORT=5432
    POSTGRES_URI=postgresql://user:password@host:5432/database
    POSTGRES_URI_LOCAL=postgresql://user:password@localhost:5432/database

```

## 2️⃣Ejecutar comando 🐳
Ejecuta el siguiente comando para construir y levantar los contenedores:

```bash
    docker compose -p mars_agent up -d
```

# Test

Se ejecutaron varios promt para observar la respuesta del agente
<img align='center' src="images/test.jpg" width="500">
<img align='center' src="images/test2.jpg" width="500">

# Links de documentación externa🔗

- [API de la NASA](https://api.nasa.gov/)

- [Langchain tool](https://python.langchain.com/docs/tutorials/sql_qa/)

