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


chmod +x services/web/entrypoint.sh

sudo docker volume ls
sudo docker inspect docker-flask-nginx-postgresql_postgres_data