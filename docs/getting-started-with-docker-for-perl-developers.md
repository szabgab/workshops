# Getting started with Docker for Perl developers


## Announcement

During this workshop you will learn why and how to use Docker in general and in particular for Perl-based projects.

First we briefly discuss the motivation behind using Docker. Then go over several use-cases using applications and libraries written in Perl.

The workshop includes presentations, discussion, and hands-on work.

The workshop will be via Zoom (link will be announced close to the event)
Language: English.
Workshop lead: [Gabor Szabo](https://szabgab.com/)
Requirements: Familiarity with writing Perl will be enough.
Length: up to 3 hours.
Cost: This workshop is free of charge thanks to the people who support me via one of the following systems: [Github sponsor](https://github.com/sponsors/szabgab/), [Patreon](https://www.patreon.com/szabgab), or directly via [PayPal](https://www.paypal.com/paypalme/szabgab).



## Notes

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


docker exec -it crazy_ardinghelli bash


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
