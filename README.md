# Shopping List Automation

Автоматизированный скрипт для синхронизации списка покупок из Google Keep с Make.com webhook.

## Описание

Этот проект автоматически:
1. Подключается к Google Keep
2. Получает список покупок из указанной заметки
3. Отправляет данные в Make.com webhook
4. Очищает список покупок после отправки

## Настройка

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Скопируйте `.env.example` в `.env` и заполните значения:

```bash
cp .env.example .env
```

Отредактируйте `.env` файл:

```env
MASTER_TOKEN=your_google_app_password_here
X_MAKE_APIKEY=your_make_api_key_here
```

### 3. Получение Google App Password

1. Перейдите в [Google Account Settings](https://myaccount.google.com/)
2. Выберите "Security" → "2-Step Verification"
3. В разделе "App passwords" создайте новый пароль для приложения
4. Используйте этот пароль как `MASTER_TOKEN`

### 4. Настройка GitHub Secrets

Для работы GitHub Actions необходимо добавить секреты в ваш репозиторий:

1. Перейдите в настройки репозитория: `Settings` → `Secrets and variables` → `Actions`
2. Добавьте следующие секреты:
   - `MASTER_TOKEN`: ваш Google App Password
   - `X_MAKE_APIKEY`: ваш API ключ Make.com

### 5. Настройка расписания

GitHub Actions настроен на запуск каждый день в 8:00 UTC. Чтобы изменить расписание:

1. Откройте `.github/workflows/scheduled-shopping-list.yml`
2. Измените cron выражение в секции `schedule`:

```yaml
schedule:
  # Пример: каждый день в 10:00 UTC (13:00 MSK)
  - cron: '0 10 * * *'
```

#### Примеры cron расписаний:

- `0 8 * * *` - каждый день в 8:00 UTC
- `0 */6 * * *` - каждые 6 часов
- `0 8 * * 1` - каждый понедельник в 8:00 UTC
- `0 8 1 * *` - первое число каждого месяца в 8:00 UTC

## Запуск

### Локальный запуск

```bash
python main.py
```

### Автоматический запуск

После настройки GitHub Actions скрипт будет запускаться автоматически по расписанию.

Также можно запустить вручную:
1. Перейдите в раздел "Actions" вашего репозитория
2. Выберите "Scheduled Shopping List Sync"
3. Нажмите "Run workflow"

## Структура проекта

```
.
├── .github/
│   └── workflows/
│       └── scheduled-shopping-list.yml  # GitHub Actions workflow
├── main.py                              # Основной скрипт
├── requirements.txt                     # Python зависимости
├── .env.example                         # Пример файла с переменными
├── .env                                 # Ваши переменные (не включается в git)
└── README.md                            # Документация
```

## Безопасность

- Файл `.env` добавлен в `.gitignore` и не попадает в репозиторий
- Секретные данные хранятся в GitHub Secrets
- Используется Google App Password вместо основного пароля

## Troubleshooting

### Ошибка аутентификации Google
- Убедитесь, что включена двухфакторная аутентификация
- Используйте App Password, а не основной пароль
- Проверьте правильность email адреса

### Ошибка webhook
- Проверьте правильность URL webhook
- Убедитесь, что API ключ Make.com корректен
- Проверьте настройки webhook в Make.com