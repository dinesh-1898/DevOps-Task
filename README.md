# DevOps Task 

A simple Flask application created for Docker and AWS ECS deployment.

## Technologies

- Python
- Flask
- Docker
- Amazon ECR
- Amazon ECS
- AWS Fargate

## Build Docker Image

docker build -t devops-app:latest .

## Run Container

docker run -d -p 5000:5000 --name devops-app devops-app:latest

## Verify Container

docker ps

## Test Application

curl http://localhost:5000

Expected Output:

ECS Deployment Successful!

## Status API

curl http://localhost:5000/status
