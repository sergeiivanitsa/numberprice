#!/bin/bash

# Установка зависимостей
apt update
apt install -y python3 python3-pip nginx certbot python3-certbot-nginx

# Установка pip-зависимостей
pip3 install -r requirements.txt

# Настройка Nginx
cp nginx.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/
nginx -t && systemctl restart nginx

# Получение SSL-сертификата
certbot --nginx -d vm3784024.stark-industries.solutions --non-interactive --agree-tos -m your-email@example.com

# Запуск бота и сервера
nohup python3 bot.py &
nohup python3 server.py &
