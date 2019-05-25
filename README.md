### Example docker-compose setup with flask/postgres/redis

#### Setup
1. `cd` into directory containing `docker-compose.yaml`
2. `docker-compose build`
3. `docker-compose run --rm flask_app flask db upgrade`
4. `docker-compose up`

#### Example App Usage

List Events:
```
curl localhost:5000/events
```

Add Event: 
```
curl -d '{"price":10.99, "date":"06-10-2019", "name": "Kelp, The Musical"}' -H "Content-Type: application/json" -X POST localhost:5000/events
```

#### Common Commands

Build containers:
```
docker-compose build
```

Start Containers (will build if not yet built):
```
docker-compose up
```

Stop Containers:
```
docker-compose stop
```

Remove Containers:
```
docker-compose kill
```

Create Database Migration:
```
docker-compose run --rm flask_app flask db migrate -m "<message here>"
```

Upgrade Database:
```
docker-compose run --rm flask_app flask db upgrade
```

To attach to running instance:
```
docker-compose exec <container> /bin/bash
```
