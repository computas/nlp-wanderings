

APP_NAME  = norberta200506
RESOURCE_GROUP = $(APP_NAME)rg
ACR = $(APP_NAME)acr
export NS := $(APP_NAME)ns
DOCKERFILE=norberta-dockerfile
REGISTRY = $(APP_NAME)reg
IMAGE_REPO = $(ACR).azurecr.io
VERSION  := 0.1
export NAME := $(IMAGE_REPO)/$(APP_NAME):$(VERSION)

# az

az-create-rg:
	az group create --name $(RESOURCE_GROUP) --location "West Europe"

az-create-acr:
	az acr create --name $(ACR) --resource-group $(RESOURCE_GROUP) --sku Basic --admin-enabled true

az-acr-signin:
	az acr credential show --name $(ACR)

az-acr-login:
	az acr login --subscription $(AZ_SUBSCRIPTION) --resource-group $(RESOURCE_GROUP) --username $(AZ_USERNAME)

## docker

docker-build:
	# need parent dir context
	cd ..;  docker build -f docker/$(DOCKERFILE) -t $(NAME) .

docker-push:
	echo Pushing $(NAME)
	@NAME=$(NAME); docker push $(NAME)

docker-login:
	docker login $(ACR).azurecr.io --username $(ACR)

docker-run:
	docker run -it $(NAME) bash

## k8s

kub-status:
	@echo Services:
	@echo ---------
	@kubectl get svc -o wide --namespace $(NS)
	@echo
	@echo Pods:
	@echo ---------
	@kubectl get pods -o wide --namespace $(NS)
	@echo
	@echo Nodes:
	@echo ---------
	@kubectl get nodes -o wide --namespace $(NS)
	@echo
	@echo Secrets:
	@echo ---------
	@kubectl get secret -o wide --namespace $(NS)
	@echo Namespaces:
	@echo ---------
	@kubectl get namespaces

