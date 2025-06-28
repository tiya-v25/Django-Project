# Django Assignment

This repository contains a Django-based backend project developed as part of an internship assignment. The project demonstrates proficiency in Django REST Framework, asynchronous task handling using Celery with Redis, and Telegram bot integration. It also follows clean code and version control practices.

---

## Features

### ✅ Django REST Framework
- Modular project structure using apps.
- Django REST Framework for API development.
- Views and routing handled in a scalable manner.

### ✅ Celery with Redis
- Asynchronous task processing using Celery.
- Redis as the message broker.
- Example task: `print_username()` tested and executed using `.delay()`.

### ✅ Telegram Bot Integration
- Developed using `python-telegram-bot`.
- Handles `/start` command.
- Automatically registers the Telegram user into the database.

### ✅ Clean Git Repository
- Proper use of `.gitignore` to exclude unnecessary files such as `__pycache__`, `.env`, `db.sqlite3`, etc.
- Descriptive commits.
- All relevant files pushed; sensitive or build files excluded.

---

## Technology Stack

- **Backend:** Django, Django REST Framework
- **Task Queue:** Celery
- **Broker:** Redis
- **Bot:** python-telegram-bot
- **Environment Management:** python-dotenv
- **Database:** SQLite3

---

## Project Setup

### 1. Clone the repository
```bash
git clone https://github.com/tiya-v25/Django-Project.git
cd Django-Project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Redis server
```bash
redis-server
```

### 4. Start Django development server
```bash
python manage.py runserver
```

### 5. Start Celery worker
```bash
celery -A server worker --pool=solo -l info
```

### 6. Run the Telegram bot
```bash
python telegram_bot.py
```

> Ensure the `.env` file contains the required Telegram bot token:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```

---

## Project Structure

```
├── core/                # Main Django application
├── server/              # Django project configuration
├── templates/           # HTML templates
├── telegram_bot.py      # Telegram bot script
├── manage.py
├── .env                 # Environment variables (excluded from repo)
├── requirements.txt
├── .gitignore
└── README.md
```

---


## Conclusion

This project fulfills all the requirements of the backend internship assignment, demonstrating:
- REST API development
- Background task execution with Celery
- Integration with Telegram bot API
- Clean and secure code management

