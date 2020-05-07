# purpose

This directory is for running norberta in kubernetes

# todo

Roughly 

1. tie in with azure devops
2. tie in arm
3. tie in with mlops

# prerequisites

* Only tested on linux
* Presupposes
  * a working az client installation
  * a subscription 

All is configured and managed through `make`. 

Copy `setsecret.sh.template` to `setsecret.sh`. It is gitignored. Edit the file with your particulars. Source it; 

```
(200506norberta_py37) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ source setsecret.sh
```

  
# config

```
(200506norberta_py37) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make az-create-rg
az group create --name norberta200506rg --location "West Europe"
{
  "id": "/subscriptions/<..>/resourceGroups/norberta200506rg",
  "location": "westeurope",
  "managedBy": null,
  "name": "norberta200506rg",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
(200506norberta_py37) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make az-create-acr
<..>
(200506norberta_py37) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make az-acr-signin
az acr credential show --name norberta200506acr
{
  "passwords": [
    {
      "name": "password",
      "value": "<..>"
    },
    {
      "name": "password2",
      "value": "<..>"
    }
  ],
  "username": "<..>"
}
```

As is explained on https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image, save the passwords. 

Then login to ACR; 

```
(200506norberta_py37) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make docker-login
```

# docker image management

Build; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make docker-build
```

Push; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make docker-push
```

Run (for debug and dev purposes):

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make docker-run
docker run -it norberta200506acr.azurecr.io/norberta200506:0.1 bash
root@0f585b7ccda7:/workspace# 
```

# aks cluster config

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make az-create-cluster
```

and then 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make az-context
```

# aks ops

With all this, we should be up and running; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-status
Services:
---------
No resources found.

Pods:
---------
No resources found.

Nodes:
---------
NAME                                STATUS   ROLES   AGE   VERSION    INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
aks-nodepool1-4848477-vmss0049954   Ready    agent   25m   v1.15.10   <..>          <none>        Ubuntu 16.04.6 LTS   4.15.0-1077-azure   docker://3.0.10+azure

Secrets:
---------
No resources found.
Namespaces:
---------
NAME              STATUS   AGE
default           Active   27m
kube-node-lease   Active   27m
kube-public       Active   27m
kube-system       Active   27m
```

Create a namespace; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-create-ns
```

# development cycle

## pod

deploy; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-create-deploy
```

check sanity; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-describe-pod
``` 

or 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-log-pod
``` 

login to pod; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-shell
``` 

delete deployment; 

```
(base) yarc@yarc-mainII ~/repository/git/github/nlp-wanderings/NorBERTa/docker $ make kub-delete-deploy
``` 
