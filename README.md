# Rick and Morty API

This project provides an API REST API built using Flask that allows users to retrieve information about characters from the Rick and Morty universe. The API is containerized using Docker and can be deployed easily using Kubernetes or Helm.

## Features
- **REST API**: Provides data on Rick and Morty characters.
- **Endpoints**: Retrieve character details such as name, location, and species.
- **Dockerized**: The application is containerized and can be pulled from Docker Hub.
- **Helm and Kubernetes Support**: Easily deployable in Kubernetes using Helm.

## Requirements
- Docker
- Python 
- Kubernetes & Helm 

## installation


### 1. *Clone this repository:*

```bash
https://github.com/tomernos/rick-and-morty-restful-api.git
```

### 2. *Build the docker image locally*



```bash
docker build -t rick-and-morty-api .
```

### 3. *Run the docker container*

```bash
docker run -d -p 5000:5000 rick-and-morty-api
```
This will run the application on port 5000.

### 4. Access the API

The API will now be available at **http://localhost:5000** (or your server IP if deployed on a cloud platform).

## API Endpoints:

### 1. /healthcheck 
 - **Description**: Returns the health status of the API

### 2. /characters
 - **Description**: Fetch a list of all characters.