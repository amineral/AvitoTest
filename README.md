# AvitoTest

## API Documentation

### Quickstart
- Create virtual enviroment: virtualenv venv
- Activate it: source venv/bin/activate
- Install dependencies: pip install -r requirements.txt
- Start server: python3 manage.py runserver

### Endpoints
- root: https://127.0.0.1/api/
- Help page: /api/help
- Client list: /api/client
- Client details: /api/client/{id}
- Transaction: /api/transaq/?{query_params}
    - query_params:
    - required:
        - from=id
        - to=id
        - value=int
    - optional:
        - currency=RUB(default)

### Added TTLCache
- to minimize requests to exchange API(50 per day) programm caching exchange values for 3600 sec after last request to API
- exchange API: https://openexchangerates.org/api
- if you haven't internet connection set ./avito_app/config.py -> EXCHANGE_IS_ACTIVE = False

### Examples
- 127.0.0.1/api/transaq?from=1&to=2&value=100&currency=USD
- 127.0.0.1/api/client
- 127.0.0.1/api/client/1
- 127.0.0.1/api/operation
- 127.0.0.1/api/operation/1

#### Visit /api/help for details