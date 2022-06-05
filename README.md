# Microservice application with Kafka
This is the demo sample microservice application with Kafka.  

Clone project to your repository, then type  
```
docker-compose up
```
command to start the application.  

The application is configured to run in development mode, such why the things 
like environment variables included in docker-compose configuration file 
or Postgres password and username are existed in the project with no hide. 
Do not pass your secrets throw in real production. Use GitHub secrets or another 
way to hide private data. `docker-compose.yml` also defines the development mode by mounting
volumes right from the root directory code, so you can change the code on the fly. Restart service by stopping with `ctrl + C` and use
```
docker-compose down
```
command to safe containers stopping. And start it again with the command to start.

