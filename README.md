# Back end code challenge

## Requeriments
    - Python 3
    - pip
    - pm2

## Install Dependencies
    - pip install -r requirements.txt

## Run Server For develop:
    - python server.py

## Run With pm2
    - pm2 start server.py --name pyton-api --interpreter=python 
## For Unit Test run:
    - python -m unittest

## For test end point
    - Use postman collection to access to the endpoint
    GET /search
    URL http://localhost:5050/search
Params
| Name          | Value         |  Description                      | Mandatory |
| q             | String        |  Word To search in db             |  true     |
| latitude      | String        |  City latitude                    |  true     |
| longitude     | String        |  City longitude                   |  true     |
| page          | Integer       |  Page for pagination data result  |  false    |
| rows          | Integer       |  Limit for pagination data result |  false    |