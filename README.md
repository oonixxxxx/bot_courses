# Telegram Shop Bot

🤖 Telegram бот для интернет-магазина с интерактивным каталогом товаров

## 📌 Основные возможности

- Просмотр товаров по категориям
- Навигация по товарам с описаниями и ценами
- Интуитивно понятное меню
- Система помощи пользователям

## 🛠 Технологии

- Python 3.10+
- Aiogram 3.x (асинхронная библиотека для Telegram Bot API)
- Asyncio для асинхронной работы

## ⚙️ Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/telegram-shop-bot.git
cd telegram-shop-bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и добавьте ваш токен бота:
```env
TOKEN=your_telegram_bot_token
```

4. Запустите бота:
```bash
python main.py
```

## 🗂 Структура проекта

```
telegram-shop-bot/
├── main.py                # Точка входа
├── config.py              # Конфигурация
├── catalog.py             # Данные каталога
├── requirements.txt       # Зависимости
├── .env.example           # Пример env-файла
├── keyboards/             # Интерактивные клавиатуры
│   ├── __init__.py
│   ├── main.py
│   ├── categories.py
│   └── items.py
└── handlers/              # Обработчики команд
    ├── __init__.py
    ├── start.py
    ├── categories.py
    ├── items.py
    ├── navigation.py
    └── help.py
```

## 🌟 Особенности архитектуры

- Модульная структура
- Четкое разделение ответственности
- Легкость расширения функционала
- Поддержка асинхронного выполнения

## 📈 Планы по развитию

- [ ] Добавление корзины покупок
- [ ] Интеграция платежной системы
- [ ] Система отзывов
- [ ] Админ-панель для управления товарами

## 🤝 Как внести вклад

1. Форкните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/AmazingFeature`)
3. Сделайте коммит изменений (`git commit -m 'Add some AmazingFeature'`)
4. Запушьте ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

---

> **Note**: Для работы бота требуется Python 3.10 или новее. Перед первым запуском не забудьте установить все зависимости.
```