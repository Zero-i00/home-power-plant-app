# Home Power Plant Backend

## Требования

- Python 3.12+
- PostgreSQL

## Установка

### 1. Создайте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate  # Windows
```

### 2. Установите зависимости

```bash
pip install fastapi uvicorn sqlalchemy asyncpg pydantic-settings
```

### 3. Создайте базу данных PostgreSQL

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE power_plant_db;
CREATE USER power_plant_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE power_plant_db TO power_plant_user;
```

### 4. Создайте файл `.env`

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

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| `POSTGRES_HOST` | Хост PostgreSQL | `localhost` |
| `POSTGRES_PORT` | Порт PostgreSQL | `5432` |
| `POSTGRES_DB` | Имя базы данных | `power_plant_db` |
| `POSTGRES_USER` | Пользователь БД | `postgres` |
| `POSTGRES_PASSWORD` | Пароль БД | `12345678` |
| `APP_PORT` | Порт приложения | `8000` |
| `APP_HOST` | Хост приложения | `localhost` |
| `APP_MODE` | Режим (`DEVELOPING`/`PRODUCTION`) | `DEVELOPING` |

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
