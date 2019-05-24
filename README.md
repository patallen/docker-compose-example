To build containers:

- `docker-compose build`


To start (will build if not yet built):

- `docker-compose up`


To stop:

- `docker-compose stop`


To remove containers:

- `docker-compose kill`


To migrate db:

- `docker-compose run --rm flask_app flask db migrate -m "<message here>"`


To upgrade db:
- `docker-compose run cargo flask_app flask db upgrade`
