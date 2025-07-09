# Build the Docker image
docker build -t pythonwebappsawstraingingwithjagan .

# Run the Docker container, mapping port 5000 of the container to port 5000 on the host
docker run -p 5000:5000 pythonwebappsawstraingingwithjagan

## How to create the docker file  #####
Now, let's write the Dockerfile to containerize this application:

Base Image: Use Python 3 as the base image.
Working Directory: Set /app as the working directory.
Dependencies: Copy the requirements.txt file and install the dependencies.
Application Code: Copy the app.py file into the container.
Port: Expose the port that Flask uses, which is 5000 by default.
Run Command: Use flask run to start the application.
Create a file named Dockerfile with the following content:
