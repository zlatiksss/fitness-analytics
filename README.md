# Fitness Analytics System
**Полноценная End-to-End система фитнес-аналитики в реальном времени**  
Генерация данных(py-script) → PostgreSQL → дашборды в Redash → анализ данных в jupyter



***Структура проекта***

C:\fitness-analytics\
├── docker-compose.yml # контейнер хранения системы\
├── generator/ # Генератор фитнес-данных\
│ ├── Dockerfile # Запись образа генератора\
│ ├── requirements.txt # Установка psycopg2-binary==2.9.9 в Dockerfile\
│ └── fitness_generator.py\
├── notebooks/ # Jupyter Notebooks и HTML-визуализации\
│ ├── activity_histogram.html\
│ ├──hourly_activity.html\
│ └── fitness_analysis.ipynb\
├── README.md\
└── screens.png




       

## Быстрый запуск - преимущество докера
\
\
\
\
***Команды управления(работаем с помощью терминала)***

# Распаковка проекта
>cd C:\fitness-analytics

# Запуск системы
>docker compose up -d --build

# Статус всех сервисов
>docker compose ps

# Логи (реального времени)
>docker compose logs -f fitness_generator
>docker compose logs -f redash_server

# Перезапуск
>docker compose restart

# Полная остановка (данные сохранятся)
>docker compose down

# Полная очистка (удаление всех данных)
>docker compose down -v

***После полного запуска системы, в браузере, можем перейти по следующим ссыылкам: http://localhost:8080 -сервис Redash с дашбордом, http://localhost:8888 -сервис jupyter c notebook***

## Перейдём к просмотру notebook:
В репозитории находится файл fitness_analysis.ipynb, в нём содержится анализ данных через запросы в БД 


## Перейдём к просмотру дашборда и их Query:
В репозитории находится серия файлов вида:screens (-).png
Ниже следует список(описание скриншота - имя скриншота):\
\
Query статистика активности - screens (1).png\
Query живой мониторинг - screens (2).png\
Query топ пользователей - screens (3).png\
Query последние события - screens (4).png\
Dashboards - screens (5).png\
Dashboards - screens (6).png\
Dashboards - screens (7).png
