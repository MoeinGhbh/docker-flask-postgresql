$ docker-compose up -d --build
$ docker-compose exec web python manage.py create_db

$ docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev

psql (12.2)
Type "help" for help.

hello_flask_dev=# \l
                                        List of databases
      Name       |    Owner    | Encoding |  Collate   |   Ctype    |      Access privileges
-----------------+-------------+----------+------------+------------+-----------------------------
 hello_flask_dev | hello_flask | UTF8     | en_US.utf8 | en_US.utf8 |
 postgres        | hello_flask | UTF8     | en_US.utf8 | en_US.utf8 |
 template0       | hello_flask | UTF8     | en_US.utf8 | en_US.utf8 | =c/hello_flask             +
                 |             |          |            |            | hello_flask=CTc/hello_flask
 template1       | hello_flask | UTF8     | en_US.utf8 | en_US.utf8 | =c/hello_flask             +
                 |             |          |            |            | hello_flask=CTc/hello_flask
(4 rows)

hello_flask_dev=# \c hello_flask_dev
You are now connected to database "hello_flask_dev" as user "hello_flask".

hello_flask_dev=# \dt
          List of relations
 Schema | Name  | Type  |    Owner
--------+-------+-------+-------------
 public | users | table | hello_flask
(1 row)

hello_flask_dev=# \q


add an entrypoint.sh file to the "web" directory to verify that Postgres is up and healthy before creating the database table and running the Flask development server:

chmod +x services/web/entrypoint.sh



sudo docker volume ls
sudo docker inspect docker-flask-nginx-postgresql_postgres_data

docker-compose exec web python manage.py seed_db

Despite adding Postgres, we can still create an independent Docker image for Flask by not setting the DATABASE_URL environment variable. To test, build a new image and then run a new container:

docker build -f ./services/web/Dockerfile -t hello_flask:latest ./services/web
docker run -p 5001:5000 \
    -e "FLASK_APP=project/__init__.py" -e "FLASK_ENV=development" \
    hello_flask python /usr/src/app/manage.py run -h 0.0.0.0


chmod +x services/web/entrypoint.prod.sh

add nginx:

$ docker-compose -f docker-compose.yml down -v
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec web python manage.py create_db

http://localhost:1337