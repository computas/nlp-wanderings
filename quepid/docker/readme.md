# Elastic enterprise search

Setup of elasticsearch enterprise locally with Quepid.

## Setup

Adapted from [https://github.com/o19s/quepid/wiki/Installation-Guide](https://github.com/o19s/quepid/wiki/Installation-Guide).

1.Set the elastic version and password and load the environment variables:

```shell
# Linux
source env.sh
```

2.Run `docker-compose pull` to load the docker images.

3.Run `docker-compose up -d redis mysql` to start the dependencies. Count to 10 to give them a chance to fire up!  

4.Run `docker-compose run --rm app bin/rake db:setup` to setup an empty database with the schema.

5.Create an administrator user.

```sh
docker-compose run app thor user:create -a mab@computas.com Administrator mysuperstrongpassword
```

5.Run `docker-compose up -d` to start the apps.

6.Open [kibana](http://localhost:5601). Bruk username:`elastic` og passord:`changeme`.

7.Open [quepid](http://localhost:3000). Log in with your admin user or create a user via the Web interface.