# A voting System

A voting system in which there are some admings, can make candidte lists and users can login and vote to those candidates.

The final result should be accessible publicly.

## init the project

1. init git
2. conda
   `conda create -n [NAME] python=[PYTHON-VERSION like 3.12 or 3.13 ...]`
3. poetry
   `poetry init`
   `poetry add PACKAGE`
   `poetry remove PACKAGE`
   `poetry install`
   `poetry update`
   `make poetry-export`

## Project Description

### A route that we can manage admins

1. An endpoint to register admins
2. An endpoint to login as admin
3. An endpoint to validate the admin

## Hosts for database in docker

### If you are using a composer or a docker service the host should refer to that service name

### If you are going to refer to your local machine (imagine you have installed postgres on your machine directly) and you

want to use it in conjunciton with your docker application. host.docker.internal

### A service on internet

Eaasily point to the domain name there

## Testing

For testing, we use `pytest` and `pytest-html` packages.
