# Diplom_2
# Тесты API Stellar Burgers

Набор автотестов на Python для проверки API сервиса Stellar Burgers:
- регистрация пользователя
- авторизация пользователя
- создание заказа

## Технологии
- Python 3.10+
- pytest
- requests
- allure-pytest
- faker

## Установка
1. Клонировать проект.
2. Установить зависимости:
     - pip install -r requirements.txt

3. Установить Allure (если не установлен):
   - Windows: через Scoop/Chocolatey или скачать архив с сайта Allure.
   - Проверка: allure --version

## Запуск тестов
- Запустить все тесты:
  - pytest -v

- Запустить конкретный файл:
  - pytest -v tests/test_user_creation.py

- Запустить конкретный тест:
  - pytest -v tests/test_create_order.py::TestCreateOrder::test_create_order_with_auth_and_ingredients_success

## Allure-отчет
- Сгенерировать результаты:
  - pytest -v --alluredir=allure-results
- Открыть отчет локально:
  - allure serve allure-results
- Сгенерировать статический отчет:
  - allure generate allure-results -o allure-report --clean

## Что покрыто тестами
1. Создание пользователя (POST /api/auth/register)
   - успешное создание уникального пользователя
   - попытка создать уже существующего пользователя (403, "User already exists")
   - отсутствие одного из обязательных полей (403, "Email, password and name are required fields")

2. Авторизация пользователя (POST /api/auth/login)
   - успешная авторизация зарегистрированного пользователя
   - ошибка при неверных учетных данных (401, "email or password are incorrect")

3. Создание заказа (POST /api/orders)
   - с авторизацией и валидными ингредиентами (200)
   - без авторизации, с валидными ингредиентами (200)
   - с авторизацией, без ингредиентов (400, "Ingredient ids must be provided")
   - без авторизации и без ингредиентов (400, "Ingredient ids must be provided")
   - с неверным хешем ингредиентов (500)

4. Справочные данные
   - получение ингредиентов (GET /api/ingredients) для подготовки валидных ID

## Структура проекта
- conftest.py — фикстуры (создание/удаление пользователей, подготовка данных)
- data/
  - urls.py — базовые URL и эндпоинты
  - messages.py — ожидаемые сообщения об ошибках/успехе
- helpers/
  - user_generator.py — генератор случайных пользователей (faker)
  - user_helper.py — обертки над запросами пользователя
  - order_helper.py — обертки над запросами заказов
- tests/
  - test_user_creation.py — тесты регистрации
  - test_user_login.py — тесты авторизации
  - test_create_order.py — тесты создания заказа

### Дерево файлов
```text
Diplom_2/
├─ conftest.py                 # общие фикстуры pytest (создание/удаление пользователей)
├─ README.md                   # описание проекта, запуск, отчеты, структура
├─ data/                       # константы и справочные данные
│  ├─ messages.py              # ожидаемые сообщения об ошибках/успехе
│  └─ urls.py                  # базовый URL и эндпоинты API
├─ helpers/                    # вспомогательные утилиты и обертки над запросами
│  ├─ order_helper.py          # методы для работы с заказами
│  ├─ user_generator.py        # генератор случайных данных пользователя
│  └─ user_helper.py           # методы для работы с пользователями
└─ tests/                      # тестовые сценарии
   ├─ test_create_order.py     # тесты создания заказа
   ├─ test_user_creation.py    # тесты регистрации пользователя
   └─ test_user_login.py       # тесты авторизации пользователя
```

## Принципы и соглашения
- Все тесты изолированы; данные пользователя очищаются в teardown фикстур.
- Для шагов и фич тестов используются декораторы Allure.
- Базовый URL и эндпоинты вынесены в data/urls.py.
- Ожидаемые сообщения собраны в data/messages.py.

## Эндпоинты
- Базовый URL: https://stellarburgers.education-services.ru
- Регистрация: /api/auth/register
- Логин: /api/auth/login
- Данные пользователя: /api/auth/user
- Ингредиенты: /api/ingredients
- Заказы: /api/orders
