# Quick Docker Setup
This project shows some startup steps to configure and run docker image of python based flask application. 
Below assignments have been performed as part of ineuron course - "Industry ready data science projects". 

## Assignment 1:
Demonstrate minimum 15 basic docker command with explanation and screenshot.

1. 'version' command displays the details of 'client' (host os) and 'server' (docker hypervised linux server also known as deamon). If the deamon is not running, the server part will give error and docker will not run.
```
docker --version
```
![image](https://user-images.githubusercontent.com/54409180/195363513-7d38c315-29d2-4d90-a633-0da799db94ce.png)

2. Below command shows all the docker images present in current system:
```
docker images
```
![image](https://user-images.githubusercontent.com/54409180/195365902-64582612-5c87-4d69-a66c-497bcb01bcea.png)

3. Below command shows list of running containers:
```
docker ps
```
![image](https://user-images.githubusercontent.com/54409180/195367125-32184a61-ef81-410b-9158-d3c701cd42ed.png)

 - Adding "-a" after 'ps' shows the list of stopped containers also.
```
docker ps -a
```
![image](https://user-images.githubusercontent.com/54409180/195368313-6706a3fe-b602-4e5a-96d4-525100f9b7f6.png)

4. 'pull' command downloads the image from Docker Hub and saves to local machine. If the image was already present, then it will not download it again from Docker hub and display the message that image is up to date.
```
docker pull <image-name>
```
![image](https://user-images.githubusercontent.com/54409180/195369470-2738cf04-3e39-418b-898c-4d61f982cc83.png)

5. 'run' command builds a container using the image. If EXPOSE details are not given in Dockerfile of the image, then the mapping of port between image (application) and the container (host machine) must be provided otherwise it can be skipped.
```
docker run -p <local-machine-port>: <Server-port> <image-name>
```
 - with ports mapping
 
![image](https://user-images.githubusercontent.com/54409180/195372719-b3a14cec-05a4-4779-bb74-a993a5edd6e3.png)

 - without port mapping
 
![image](https://user-images.githubusercontent.com/54409180/195372258-a8ec3aae-5b21-46de-9bcb-eebe1334ff20.png)

6. When container runs using above commands, it shows all the execution steps in the same terminal which locks the terminal for other tasks. To avoid this, we can start a container in the dettached mode.
```
docker run -d <image>
```
![image](https://user-images.githubusercontent.com/54409180/195374325-162187b0-f39f-498f-8f53-9ea518a3a9db.png)

7. To stop an existing container:
```
docker stop <container-id or name>
```
![image](https://user-images.githubusercontent.com/54409180/195373138-bc7c7117-216a-4bc2-8358-531dde90c88b.png)

8. To delete a container:
 ```
 docker rm <container-id or name>
 ```
  - Multiple ids can be passed separated with whitespaces. **Note:** Container must be stopped before running the remove command.
 ![image](https://user-images.githubusercontent.com/54409180/195375312-851d46e9-7219-4263-84b4-55fdf4d40f5c.png)

9. To delete an image: 
```
docker rmi <image-name>
```
 - **Note:** There must not be any container created (running or stopped) which uses this image. Remove the containers before deleting the image.

![image](https://user-images.githubusercontent.com/54409180/195376309-7ac7efb0-4c8d-42c0-9130-6953ca1a361f.png)

10. To create image using 'Dockerfile':
```
docker build . -f Dockerfile -t <image-name>
```
![image](https://user-images.githubusercontent.com/54409180/195378275-0b85a0c2-8963-4ec4-80a5-b8cbcb39b433.png)

- Dockerfile of a Flask application is shown below:

![image](https://user-images.githubusercontent.com/54409180/195378736-eae7e5b4-47b4-4ca9-b42a-76f191594389.png)

- Follow steps in this url to create docker image of a basic python flask application : https://docs.docker.com/language/python/build-images/

11. Once image is created we can publish it to Docker Hub repositry. Other users can 'pull' this image to create and run the container in their system. Use 'docker login' command to login to the docker hub account.
```
docker push <username>/<image-name>
```
- username: docker hub account name
- image-name: name of the image we created using build command.
![image](https://user-images.githubusercontent.com/54409180/195382966-bc3a3b32-5c31-4070-b38d-633845e4a6d2.png)

- Once image has been published, it will appear in the docker hub repository.
![image](https://user-images.githubusercontent.com/54409180/195400741-9f29db14-1031-4022-aadd-53670d375e54.png)

--------------------------------------------------------------------------------------------------------
## Assignment 2:
Hello World Docker Image Run Hello World Docker Image Locally.

a. Initially there is no images present in my local system:

![image](https://user-images.githubusercontent.com/54409180/195526347-fbbbff5a-748d-446d-bd3b-9c2988fd9e6f.png)

b. Downloading the 'Hello Word Docker' Image from docker hub. 

```
docker pull hello-world
```
docker pull command will download the latest image of 'hello-world' official image from docker hub.
![image](https://user-images.githubusercontent.com/54409180/195527422-93adc756-16d7-4051-81c9-6fe94d18c4a5.png)

--------------------------------------------------------------------------------------------------------
## Assignment 3:
Create a hello world fastapi application. Create a Dockerfile for your fastapi hello world application. Build Docker image using Docker file. Run docker image build in previous step. Push your Docker image to Docker Hub.

--------------------------------------------------------------------------------------------------------
## Assignment 4:
Automate Assignment below task using github action.

Build Docker Image
Push Docker Image to Docker hub.
