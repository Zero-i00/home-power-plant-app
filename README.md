# Home Power Plant Backend

## Требования

- Python 3.12+
- PostgreSQL

## Установка

### 1. Создайте виртуальное окружение

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2. Установите зависимости

```bash
pip install fastapi uvicorn sqlalchemy asyncpg pydantic-settings
или
pip install -r requirements.txt	
```

### 3. Создайте файл `.env`

Создайте файл `.env` в папке `backend/`:

```env
# PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=power_plant_db
POSTGRES_USER=power_plant_user
POSTGRES_PASSWORD=your_password

# Application
APP_PORT=8000
APP_HOST=localhost
APP_NAME=Home Power Plant
APP_MODE=DEVELOPING
```
## Запуск

```bash
python main.py
```

Или через uvicorn напрямую:

```bash
uvicorn main:app --reload --host localhost --port 8000
```

API будет доступен по адресу: http://localhost:8000

Документация Swagger: http://localhost:8000/docs
