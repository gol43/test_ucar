# test_ucar

## Описание проекта

- REST API для создания и обработки сообщений об инцедентах.
- Проект реализован по собственной интерпретации паттерна репозиторий и луковой архитектуры.
- dataclass не использовал ввиду их крайней избытычности для столь мелкого проекта.

*По любым вопросам по коду, писать в телеграмм, который указан в конце документа
---

### Шаги установки 
1. **Склонируйте репозиторий**:
```bash
    git clone https://github.com/gol43/test_ucar.git 

    cd test_ucar
```

2. **Создайте и активируйте виртуальное окружение**:
```bash
    python -m venv venv

    source venv/bin/activate
```

3. **Установите зависимости**:
```bash
    pip install -r requirements.txt
```

---

### Примеры запуска

1. **Создать файл .env в корне с данными (пример)** 
```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
POSTGRES_DB=test_incedent
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```

2. **Создание образов и запуск контейнера**
```bash
docker compose up -d
```

3. **Создание миграций и их применение**
```bash
docker exec -it incidents_app bash

alembic revision --autogenerate -m "initial"

alembic upgrade head
```

4. **Работа с проектом**

Нужно перейти по ссылке swagger: http://127.0.0.1:8000/api/v1/ucar/docs#/


5. **Особенность проверки обработчиков**

--Примеры запросов, для создания записи об инциденте

```bash
- curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/incedents/create_incedent/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Самокат на станции №12 не отвечает на запросы клиента",
  "source": "operator",
  "status": "pending"
}
' 
```

```bash
- curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/incedents/create_incedent/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Отчёт о продажах за вчерашний день не выгрузился в систему BI",
  "source": "monitoring",
  "status": "in_progress"
}
'
```

```bash
- curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/incedents/create_incedent/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Партнёрская точка выдачи заказов не подключается к серверу",
  "source": "partner",
  "status": "resolved"
}
'
```

-- Пример запроса получения всех записей
```bash
-curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/incedents/get_all_incedents/' \
  -H 'accept: application/json'
```

-- Пример изменения статуса у конкретной записи
```bash
- curl -X 'PATCH' \
  'http://127.0.0.1:8000/api/v1/incedents/update_status/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "status": "resolved"
}'
```

--- 

## 👨‍💻 Автор

Проект разработан:  
**Сайгушев Дамир Даниярович**  
- GitHub: [gol43](https://github.com/gol43)  
- Telegram: [@spongedmw](https://t.me/spongedmw)

---
