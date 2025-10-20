# 🛒 Shopping List Sync

Автоматическая синхронизация списка покупок из Google Keep в Telegram.

## 📋 Возможности

- ✅ Получение списка покупок из Google Keep
- ✅ Отправка списка в Telegram с красивым форматированием
- ✅ Автоматическая очистка списка после отправки
- ✅ Запуск по расписанию через GitHub Actions
- ✅ Возможность ручного запуска

## 🚀 Настройка

### 1. Создайте Telegram бота

1. Откройте [@BotFather](https://t.me/BotFather) в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям и получите токен бота
   - Формат: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

### 2. Получите Chat ID

Вариант 1 (простой):
1. Откройте [@userinfobot](https://t.me/userinfobot) в Telegram
2. Получите ваш Chat ID (например: `123456789`)

Вариант 2 (через API):
1. Напишите что-нибудь вашему боту
2. Откройте в браузере: `https://api.telegram.org/bot<YourBotToken>/getUpdates`
3. Найдите значение `"chat":{"id":123456789}`

### 3. Получите Google App Password

1. Перейдите в [Google Account Settings](https://myaccount.google.com/)
2. Выберите "Security" → "2-Step Verification"
3. В разделе "App passwords" создайте новый пароль для приложения
4. Используйте этот пароль как `MASTER_TOKEN`

### 4. Настройте переменные окружения

#### Для локального запуска:

Создайте файл `.env`:
```env
MASTER_TOKEN=ваш_google_app_password
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

#### Для GitHub Actions:

Добавьте секреты в репозиторий:

`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

Создайте 3 секрета:
- `MASTER_TOKEN` - Google App Password
- `TELEGRAM_BOT_TOKEN` - токен Telegram бота
- `TELEGRAM_CHAT_ID` - ID чата в Telegram

⚠️ **Важно**: В GitHub Secrets значения вставляйте **без кавычек**!

## 📅 Расписание

По умолчанию скрипт запускается каждый день в 14:00 UTC.

Чтобы изменить расписание, отредактируйте cron в `.github/workflows/scheduled-shopping-list.yml`:

```yaml
schedule:
  - cron: '0 14 * * *'  # Каждый день в 14:00 UTC
```

### Примеры расписаний:

- `0 8 * * *` - каждый день в 8:00 UTC
- `0 */6 * * *` - каждые 6 часов
- `0 8 * * 1` - каждый понедельник в 8:00 UTC
- `0 8 1 * *` - первое число каждого месяца в 8:00 UTC

## 🔧 Установка и запуск

### Локально:

```bash
# Установите зависимости
pip install -r requirements.txt

# Запустите скрипт
python main.py
```

### На GitHub Actions:

1. Настройте секреты (см. пункт 4 выше)
2. Push код в репозиторий
3. Перейдите в раздел "Actions"
4. Выберите "Scheduled Shopping List Sync"
5. Нажмите "Run workflow" для ручного запуска

## 🎯 Как это работает

1. Скрипт подключается к Google Keep с вашим токеном
2. Получает список непроверенных элементов из заметки
3. Форматирует список с эмодзи и Markdown
4. Отправляет сообщение в Telegram
5. Если отправка успешна - очищает список в Google Keep

## 📝 Пример сообщения в Telegram

```
🛒 Список покупок:

☐ Молоко
☐ Хлеб
☐ Яйца
☐ Сыр
```

## 🔒 Безопасность

- ✅ Файл `.env` добавлен в `.gitignore`
- ✅ Секреты хранятся в GitHub Secrets
- ✅ Используется Google App Password, а не основной пароль
- ✅ Telegram Bot API использует HTTPS

## 🐛 Troubleshooting

### MASTER_TOKEN: ✗ Missing
- Проверьте наличие файла `.env`
- Убедитесь, что в `.env` нет кавычек вокруг значений
- Для GitHub Actions: проверьте наличие секрета `MASTER_TOKEN`

### TELEGRAM_BOT_TOKEN: ✗ Missing
- Проверьте правильность токена бота от @BotFather
- Убедитесь, что токен без кавычек
- Для GitHub Actions: проверьте наличие секрета `TELEGRAM_BOT_TOKEN`

### Ошибка аутентификации Google
- Убедитесь, что включена двухфакторная аутентификация
- Используйте App Password, а не основной пароль
- Проверьте правильность email адреса в `main.py`

### Telegram бот не отправляет сообщения
- Убедитесь, что вы написали боту хотя бы одно сообщение
- Проверьте правильность Chat ID
- Проверьте, что бот не заблокирован

## 📦 Структура проекта

```
.
├── .github/
│   └── workflows/
│       └── scheduled-shopping-list.yml  # GitHub Actions
├── main.py                              # Основной скрипт
├── requirements.txt                     # Зависимости
├── .env                                 # Переменные (не в git)
├── .gitignore                           # Исключения git
└── README.md                            # Документация
```

## 📄 Лицензия

MIT