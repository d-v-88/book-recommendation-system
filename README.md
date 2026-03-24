# book-recommendation-system

## Workflow for code update

- config.yaml
- entity
- config/configuration.py
- components
- pipline
- main.py
- app.py

# How to rum?

### STEPS:

Clone the repository

```bash
https://github.com/d-v-88/book-recommendation-system.git
```

### STEP 01 - Create a conda environment afteropening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```

### STEP 02- Install the requirements

```bash
pip install -r requirements.txt
```

OR

```bash
python -m pip install -r requirements.txt
```

New run,

```bash
streamlit run app.py
```

# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

# Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t entbappy/stapp:latest .
```

```bash
docker images -a
```

```bash
docker run -d -p 8501:8501 entbappy/stapp
```

```bash
docker ps
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login
```

```bash
docker push d-v-88/bookapp:latest
```

```bash
docker rmi d-v-88/bookapp:latest
```

```bash
docker pull d-v-88/bookapp
```
