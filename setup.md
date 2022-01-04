# Setup product service:

## Setup
1.  Create virtual environment
virtualenv -v python3.8 env
2.  Enable environment and install requires package
source env/bin/activate
pip install -r requirements.txt
3.  Create an postgres database filter_api
4.  export following environment variable
export DATABASE_URL=postgresql://<user_name>:<password>@<db_host>/filter_api
5.  Migrate database
alembic upgrade heads
6. run server.
uvicorn product_api.app:app --reload --port 8000

## Using curl and swagger.
This project is base on FastAPI framework, as a result it come with interactive swagger page
which allow user to test apis endpoint.
To access swagger page: http://localhost:8000/api

get filter data 
curl -X 'GET' \
  'http://localhost:8000/api/filter/?page=1&size=100' \
  -H 'accept: application/json'

add filter to database
curl -X 'POST' \
  'http://localhost:8000/api/filter/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "search": [
    "name:vpn",
    "name:remote"
  ],
  "sort": "price:asc",
  "price": "20-50",
  "date": "2022-01-01T13:40:40.603227"
}'