# Currency conversion

## Assumptions
Hopefully I did not get the question wrong, but I assume that we are building a currency exchange which shows the exchange rates of various currencies with USD

## How to use this project
1. Generate a Django secret. Sample code to run on cmd line:
```
python3 -c 'import secrets; print(secrets.token_hex(100))'
```

2. Define environment variables and save it into a .env file
```
DJANGO_SECRET: Django project secret generated in step 1
DJANGO_DEBUG: True/False
```
3. Install Docker and Docker compose. [Link](https://docs.docker.com/get-docker/)


### Running the project
```
docker compose up
```

### Running tests
```
docker compose run web python manage.py test
```

## Endpoints

### 1. Get currency list
```
GET /currency/
```
This will return all the currencies exchange rate with USD.

Filters
```
/currency/?filters=currency~USD
```
You can filter by currencies, using a delimiter of "~" in the url

Sort
```
/currency/?order_by=currency
```
You can sort in ascending/descending order for "currency" and "rate"

### 2. Sync currency list
```
POST /sync_currency/
```
This will get all the exchange rates from the yfinance package and create/update the sqlite database. This endpoint is done as I imagine that we can use a cron service to call this endpoint periodically to update the sqlite database.

## Improvements
1. Authentication and permissions, especially for the `sync_currency` endpoint which should only be accessible to the admins
2. There should be more error handling for the yfinance package.
3. Logging should be implemented for the actual projects
