# purpose

This directory is for running norberta in kubernetes

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

