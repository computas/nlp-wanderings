export ELASTIC_VERSION=7.6.0
docker build -t "custom/elasticsearch:latest" --build-arg ELASTIC_VERSION=$ELASTIC_VERSION -f elasticsearch/Dockerfile .
docker build -t "custom/kibana:latest" --build-arg ELASTIC_VERSION=$ELASTIC_VERSION -f kibana/Dockerfile .

