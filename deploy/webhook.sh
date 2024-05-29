#!/bin/bash

# Путь к скрипту deploy.sh
DEPLOY_SCRIPT=/home/defendershow/bot/deploy/deploy.sh

# Запустить скрипт развертывания
$DEPLOY_SCRIPT

# Вернуть ответ веб-хуку
echo "Deployment triggered successfully."