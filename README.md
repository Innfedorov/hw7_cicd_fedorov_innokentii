# CI/CD для ML-модели

## Стратегия развертывания
Выбрана **Blue-Green**. Две версии сервиса работают параллельно. Переключение трафика мгновенное, откат — секунды.

## Запуск
1. Склонировать репозиторий
2. Собрать образ: `docker build -t ml-service:v1.0.0 .`
3. Запустить blue-версию: `docker-compose -f docker-compose.blue.yml up -d`
4. Проверить health: `curl http://localhost:8081/health`

## CI/CD
- GitHub Actions проверяет код и собирает Docker-образ
- Деплой на сервер выполняется автоматически при пуше в master
