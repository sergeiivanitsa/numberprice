# Telegram Mini App для оценки стоимости автомобильных номеров

Этот проект представляет собой Telegram бота, который позволяет пользователям рассчитать стоимость автомобильного номера по заданным правилам.

## Структура проекта

Проект состоит из нескольких частей:

1. **bot.py** – Логика работы Telegram бота. Бот запускается с командой `/start`, затем предлагает пользователю ввести номер автомобиля для расчета стоимости.
2. **server.py** – Сервер, который обрабатывает POST-запросы с веб-формы в Mini App. Он проверяет корректность номера, рассчитывает его стоимость и возвращает результат пользователю.
3. **HTML/JS** – Интерфейс для ввода номера и отображения результата расчета стоимости.
4. **requirements.txt** – Список зависимостей, необходимых для работы проекта.
5. **nginx.conf** – Конфигурационный файл для Nginx для настройки обратного прокси.
6. **bash script** – Скрипт для автоматической установки всех зависимостей, настройки серверного окружения и получения SSL сертификата.

## Логика расчета стоимости номера

Стоимость номеров рассчитывается на основе следующих правил:

1. **Три одинаковых цифры** – 600 тыс.
2. **Три одинаковых буквы** – 300 тыс.
3. **Номера, в которых первые две цифры это 0 (например, 001, 002, ...)** – 500 тыс.
4. **Последние две цифры – ноль (например, 100, 200, ...)** – 250 тыс.
5. **Три одинаковых цифры и три одинаковых буквы** – 1 млн.
6. **Зеркальные цифры** (например, 1x1, 2x2, 3x3) – 70 тыс.
7. **Трехбуквенные слова** (например, ВОР, ЛОХ, ДОМ, РАК) – 300 тыс.

## Установка

Для развертывания проекта на сервере, выполните следующие шаги:

### 1. Установка необходимых зависимостей

На сервере должна быть установлена операционная система Ubuntu. Если pip и Python не установлены, следуйте инструкциям:

```bash
# Обновите пакеты
sudo apt update
sudo apt upgrade -y

# Установите Python 3 и pip
sudo apt install python3 python3-pip -y

# Установите виртуальное окружение
sudo apt install python3-venv -y

# Создайте виртуальное окружение
python3 -m venv venv

# Активируйте виртуальное окружение
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
