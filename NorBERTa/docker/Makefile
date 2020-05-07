

APP_NAME  = norberta200506
RESOURCE_GROUP := $(APP_NAME)resgr
ACR = $(APP_NAME)acr
export NS := $(APP_NAME)ns
DOCKERFILE=norberta-dockerfile
REGISTRY = $(APP_NAME)reg
IMAGE_REPO = $(ACR).azurecr.io
VERSION  := 0.1
export NAME := $(IMAGE_REPO)/$(APP_NAME):$(VERSION)
AKS_CLUSTER = $(APP_NAME)cl

# general

# install: az-create-cluster az-context
# clean: az-delete-cluster
# dist-clean: clean az-delete-acr
# maintainer-clean: dist-clean az-delete-rg

# az

az-create-rg:
	az group create --name $(RESOURCE_GROUP) --location "West Europe"

az-delete-rg:
	az group delete --name $(RESOURCE_GROUP) --yes --no-wait

az-create-acr:
	az acr create --name $(ACR) --resource-group $(RESOURCE_GROUP) --sku Basic --admin-enabled true

az-delete-acr:
	az acr create --name $(ACR)

az-acr-signin:
	az acr credential show --name $(ACR)

az-acr-login:
	az acr login --subscription $(AZ_SUBSCRIPTION) --resource-group $(RESOURCE_GROUP) --username $(AZ_USERNAME) --name $(ACR)

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

# az aks

az-create-cluster:
	# todo: do it thorugh rm - https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-rm-template
	az aks create --resource-group $(RESOURCE_GROUP) --name $(AKS_CLUSTER) --node-count 1 --enable-addons monitoring --generate-ssh-keys --attach-acr $(ACR)

az-delete-cluster:
	az aks delete --resource-group $(RESOURCE_GROUP) --name $(AKS_CLUSTER)

az-context:
	az aks get-credentials --resource-group $(RESOURCE_GROUP) --name $(AKS_CLUSTER)


## k8s

kub-create-ns:
	kubectl create namespace $(NS)

kub-status:
	@echo Services:
	@echo ---------
	@kubectl get svc -o wide --namespace $(NS)
	@echo
	@echo Pods:
	@echo ---------
	@kubectl get pods -o wide --namespace $(NS)
	@echo
	@echo Deployments:
	@echo ---------
	@kubectl get deployment -o wide --namespace $(NS)
	@echo
	@echo Nodes:
	@echo ---------
	@kubectl get nodes -o wide --namespace $(NS)
	@echo
	@echo Secrets:
	@echo ---------
	@kubectl get secret -o wide --namespace $(NS)
	@echo
	@echo Namespaces:
	@echo ---------
	@kubectl get namespaces

kub-create-service:
	kubectl create -f norberta-service.yaml

kub-create-deploy:
	kubectl create -f norberta-deployment.yaml

kub-delete-deploy:
	kubectl delete -f norberta-deployment.yaml

kub-log-pod:
	$(eval POD := $(shell kubectl get pods --namespace $(NS) | grep $(APP_NAME) | cut -d' ' -f1))
	@kubectl logs $(POD) --namespace=$(NS)

kub-describe-pod:
	$(eval POD := $(shell kubectl get pods --namespace $(NS) | grep $(APP_NAME) | cut -d' ' -f1))
	kubectl describe pod $(POD) --namespace=$(NS)

kub-shell:
	$(eval POD := $(shell kubectl get pods --namespace $(NS) | grep $(APP_NAME) | cut -d' ' -f1))
	kubectl exec -it $(POD) --namespace=$(NS) /bin/bash
