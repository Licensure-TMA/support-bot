#!/bin/bash

# Остановить и удалить старый контейнер, если он существует
docker stop bot_sup || true
docker rm bot_sup || true

# Удалить старый образ
docker rmi aleksglebov/licensure:bot_sup || true

# Получить последнюю версию образа из Docker Hub
docker pull aleksglebov/licensure:bot_sup

# Запустить новый контейнер
docker run -d --name bot_sup -e TOKEN_SUP="$TOKEN_SUP" aleksglebov/licensure:bot_sup

echo "Deployment completed successfully."