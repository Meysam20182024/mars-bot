#!/bin/bash

echo "Установка Mars Bot systemd-сервиса..."

# Копируем сервис
cp marsbot.service /etc/systemd/system/marsbot.service

# Обновляем systemd
systemctl daemon-reexec
systemctl daemon-reload

# Включаем автозапуск
systemctl enable marsbot

# Запускаем бот
systemctl start marsbot

# Показываем статус
systemctl status marsbot --no-pager
