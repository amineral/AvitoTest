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
- Transaction: /api/transaq?{query_params}
    - query_params:
    - required:
        - from=id
        - to=id
        - value=int/float
    - optional:
        - currency=RUB(default)


#### Visit /api/help for details