# Readme

## Instrucciones para correr el script

### 1. Crear el ambiente virtual
`python3 -m venv venv`


### 2. Activar el entorno virtual
`venv\Scripts\activate`

### 3. Instala las dependencias
`pip install -r requirements.txt`

### 4. Crea tu archivo .env usando como ejemplo el archivo `.env.template` y setea las variables

### 5. Usa el siguiente comando para levantar el servidor
`uvicorn app:app --reload`

### 6. Sube tu imagen que deseas analizar con OCR en la ruta por default
`http://127.0.0.1:8000`


### [DEMO](https://ocr-azure-production.up.railway.app/)