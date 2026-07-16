# Verbum-
El centro de todo centro.
🟠 Verbum.

«La Plataforma Integral de Inteligencia Empresarial para Cuba»

"Status" (https://img.shields.io/badge/Estado-En%20Desarrollo-orange)
"License" (https://img.shields.io/badge/Licencia-Propietaria-gold)
"AI" (https://img.shields.io/badge/AI-Verbum%20Core-black)
"Country" (https://img.shields.io/badge/Cuba-Digital-orange)

---

Nuestra visión

Verbum es una plataforma de inteligencia empresarial diseñada para transformar conocimiento en decisiones.

No es un chatbot.

No es un buscador de leyes.

No es un ERP.

Es un ecosistema de inteligencia artificial que integra conocimiento jurídico, gestión documental, análisis empresarial, transformación digital y apoyo a la toma de decisiones.

---

Módulos

- ⚖️ Verbum Lex
- 💼 Verbum Business
- 🌍 Verbum Invest
- 🛡️ Verbum Compliance
- 📊 Verbum Risk
- 💳 Verbum Finance
- 🤖 Verbum AI
- 📑 Verbum Docs
- 📈 Verbum Analytics

---

Objetivos

✔ Reducir tiempos administrativos

✔ Automatizar documentación

✔ Centralizar normativa

✔ Facilitar inversión

✔ Ayudar a MiPyMEs

✔ Impulsar la transformación digital

✔ Crear inteligencia empresarial para Cuba

---

Arquitectura

Verbum Core

↓

Motor IA

↓

Motor Jurídico

↓

Motor Empresarial

↓

Motor Documental

↓

Motor Financiero

↓

API

↓

Aplicación Web

↓

Aplicación Móvil

---

Tecnologías

Flutter

FastAPI

Python

PostgreSQL

SQLite

Docker

GitHub

OpenAI Compatible

---

Estado

🚧 Arquitectura en desarrollo.

---

Autor

Armando Omar Bermúdez Vila

Director General

Verbum Tech Solution

---

Lema

Del conocimiento a la decisión.

---

Infra - Scaffold mínimo

Se añadió un scaffold mínimo de infraestructura para convertir este repositorio en el "núcleo" ejecutable del ecosistema.

Archivos incluidos en este bloque:

- app/main.py: entrypoint FastAPI y montaje de routers en /v1
- app/api/v1/health.py: endpoint /v1/health para checks de disponibilidad
- app/api/v1/info.py: endpoint /v1/info con metadatos de la aplicación
- app/core/config.py: configuración central (Pydantic BaseSettings)
- app/models/common.py: schemas Pydantic mínimos para infra
- .env.example: variables de entorno de ejemplo
- Dockerfile: imagen mínima para ejecutar la app

Alcance y restricciones de este bloque:

- No se añadió lógica de negocio (Lex, Finance, Business, etc.).
- No se añadió integración con bases de datos, Temporal, proveedores de IA ni autenticación.
- No se añadieron migraciones ni workers.
- OpenAPI y documentación se sirven con la configuración estándar de FastAPI.

Cómo ejecutar localmente (rápido):

1) desde la raíz del repo crear un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
pip install "fastapi" "uvicorn[standard]"
```

2) ejecutar la app:

```bash
uvicorn app.main:app --reload --port 8000
```

3) revisar:

- http://localhost:8000/v1/health
- http://localhost:8000/v1/info
- Documentación interactiva: http://localhost:8000/docs

Próximos pasos propuestos (tras revisar este bloque):

- Añadir pyproject.toml y gestión de dependencias.
- Añadir docker-compose para desarrollo (Postgres, Temporal).
- Scaffold para NexoRouter, Temporal y conexión a DB (en bloques separados y controlados).

Si estás de acuerdo, continuamos con el siguiente bloque cuando lo autorices.
