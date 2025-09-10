## Психология — Telegram-бот-консультант на aiogram 3

Бот для быстрой связи со специалистом: пользователь пишет вопрос, бот собирает контактные данные (имя, username, id) и пересылает сообщение админу(ам) в Telegram. Работает на aiogram 3 (Python 3.12) в режиме polling.

### Для чего нужен
- Быстрый первичный контакт с психологом без публичных чатов
- Сбор обращения в одном сообщении и отправка администраторам/специалистам
- хранение ссылок на соцсети специалиста
- Простая конфигурация получателей через переменные окружения

### Как это работает (пользовательский сценарий)
1) Пользователь нажимает «Связаться со мной»
2) Пишет вопрос в ответ на запрос бота
3) Подтверждает отправку
4) Бот пересылает сообщение указанным администраторам; пользователю приходит подтверждение

### Возможности
- **Aiogram 3**: чистая маршрутизация через `Router`
- **Пересылка обращений**: содержимое + имя, username, user_id
- **Гибкая конфигурация админов**: через переменные окружения `ADM*_ID`
- **Контейнеризация**: готовые `Dockerfile` и `docker-compose.yaml`

### Требования
- Python 3.12+
- Telegram Bot Token (получите у `@BotFather`)

### Быстрый старт (локально)
1) Клонируйте репозиторий
```bash
git clone <URL-ВАШЕГО-РЕПОЗИТОРИЯ>.git
cd психология
```

2) Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Linux/macOS
source venv/bin/activate
```

3) Установите зависимости
```bash
pip install -r requirements.txt
```

4) Создайте файл `.env` в корне проекта
```bash
echo BOT_TOKEN=ваш_токен > .env
echo ADM1_ID=111111111 >> .env
echo ADM2_ID=222222222 >> .env
echo ADM3_ID=333333333 >> .env
```

5) Запустите бота
```bash
python start.py
```

### Запуск в Docker
Собрать и запустить контейнер:
```bash
docker build -t psychology-bot .
docker run --rm -it --env-file .env psychology-bot python start.py
```

### Запуск через Docker Compose
В `docker-compose.yaml` прописана сервисная команда. Убедитесь, что `.env` рядом с `docker-compose.yaml` содержит `BOT_TOKEN`.
```bash
docker compose up --build -d
```

Остановить:
```bash
docker compose down
```

### Структура проекта
- `start.py` — входная точка, запуск `Dispatcher.start_polling`
- `handlers/` — обработчики апдейтов, подключаются в `start.py`
- `keyboards/` — клавиатуры и разметка
- `requirements.txt` — зависимости проекта
- `Dockerfile`, `docker-compose.yaml` — контейнеризация

### Переменные окружения
- `BOT_TOKEN` — токен вашего Telegram-бота
- `ADMIN_IDS` — список Telegram user_id администраторов

### Публикация на GitHub (быстрые команды)
Если репозиторий ещё не инициализирован:
```bash
git init
git add .
git commit -m "Initial commit: aiogram bot"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

### Лицензия
MIT.


