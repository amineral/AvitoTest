# AvitoTest

- Сервис работает на SQLite, потому что мой мак выдает странные ошибки при попытке установить постгрес или мускл. Если разберусь, то уберу эту запись.
- В проекте сразу залита база с двумя пользователями для тестов.
- Так же пользователей можно добавить через админку (./admin/ login: admin, password: 123456)

## API Documentation

### Quickstart
- Create virtual enviroment: virtualenv venv
- Activate it: source venv/bin/activate
- Install dependencies: pip install -r requirements.txt
- Start server: python3 manage.py runserver

### Endpoints
- root: https://127.0.0.1/api/
- Help page: /api/help/
- Client list: /api/client/
- Operation list /api/operations/
- Bank operation list /api/bankoper/
- All endpoints you can find on help page or index page /api/

### Added TTLCache
- to minimize requests to exchange API(50 per day) programm caching exchange values for 3600 sec after last request to API
- exchange API: https://openexchangerates.org/api
- if you haven't internet connection set ./avito_app/config.py -> EXCHANGE_IS_ACTIVE = False

### Examples
- 127.0.0.1/api/transaq/?from=1&to=2&value=100&currency=USD
- 127.0.0.1/api/depo/?id=1&value=100&currency=EUR
- 127.0.0.1/api/client
- 127.0.0.1/api/client/1
- 127.0.0.1/api/operation
- 127.0.0.1/api/operation/1

#### Visit /api/help for details
