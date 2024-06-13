# Getting started with Docker for Perl developers

* What problems does Docker solve?

* Fixing dependencies in Perl - Makefile.PL  [Carton](https://metacpan.org/dist/Carton)

* Fixing other, non-Perl dependencies? (OS, database etc.)

* Image vs Container

* Perl Specific images
    * [Perl](https://hub.docker.com/_/perl)

* [slides](https://code-maven.com/slides/docker/perl)

* [Getting started with Perl on Docker](https://perlmaven.com/getting-started-with-perl-on-docker)
* [Distributing a Perl script using Docker container](https://perlmaven.com/distributing-perl-script-using-docker)
* [Dancer in Docker](https://perlmaven.com/dancer-in-docker)
* [Hello World with Mojolicious in Docker](https://perlmaven.com/hello-world-with-mojolicious-in-docker)
* [Counter using Dancer2 and Redis in a Docker container](https://perlmaven.com/counter-dancer2-redis-docker)



* [Docker compose PostgreSQL server](https://code-maven.com/slides/docker/docker-compose-postgresql-server)


* [Docker compose Perl and PostgreSQL]((https://github.com/szabgab/docker-compose-perl-postgresql)

* PostgreSQL

```
docker compose up
```

```
docker compose exec client bash

export PGPASSWORD=password
echo "SELECT CURRENT_TIME" | psql -h pg-db-server -U username mydb
```


* Perl and PostgreSQL
