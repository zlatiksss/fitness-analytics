# Fitness Analytics Dashboard

**Полноценная End-to-End система фитнес-аналитики в реальном времени**  
Генерация данных → PostgreSQL → Redash + дашборды 

## Структура проекта
C:\fitness-analytics
├── docker-compose.yml # контейнер хранения системы
├── generator/ # Генератор фитнес-данных 
│ ├── Dockerfile # Запись образа генератора
│ ├── requirements.txt # Установка psycopg2-binary==2.9.9 в Dockerfile 
│ └── fitness_generator.py 
└── README.md 


## Быстрый запуск - преимущество докера

# Работаем с помощью терминала

# Распаковка проекта
cd C:\fitness-analytics

# Запуск системы
docker compose up -d --build

# Статус всех сервисов
docker compose ps

# Логи (реального времени)
docker compose logs -f fitness_generator
docker compose logs -f redash_server

# Перезапуск
docker compose restart

# Полная остановка (данные сохранятся)
docker compose down

# Полная очистка (удаление всех данных)
docker compose down -v


## Быстрый запуск - преимущество докера
Перейдём к просмотру дашборда:
1. После полного запуска системы, в браузере, переходим по следующей ссылке: http://localhost:8080
Попадём на страницу Redash, где и расположен дашборд с 4 визуализациями:
