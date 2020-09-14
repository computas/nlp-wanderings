# Elastic enterprise search

Test of elastic enterprise search.

Inspiration example [docker-compose](https://discuss.elastic.co/t/enterprise-search-docker-compose/239783). 

Added features:

- Added kibana
- Update to use elasticsearch native realm for authentication, so that kibana can be connected to enterprise search

## Setup

1.Set the elastic version and password and load the environment variables:

```bash
source .env
```

2.Run `docker-compose up`

3.Recover credentials for enterprise search by running:

```bash
docker-compose logs enterprisesearch | grep "Default user credentials have been setup." -A 2
```

3.Open [localhost:3002](http://localhost:3002) and log in, or start [kibana][http://localhost:5601] and go to `App Search`.

## Known issues

- Enterprise search complains that Elasticsearch runs on a OSS licence, and then dies. Even though I added a healthcheck to wait for elasticsearch, it seems that the issue is something else. You have to start enterprise search again and it will work. It is annoying but not a critical issue.
