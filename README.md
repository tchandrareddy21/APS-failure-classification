<h1 align="center">APS Failure Detection</h1>

## Project Overview

### Problem Statement

- The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.
- This is a Binary Classification problem, in which the positive class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

### Solution Proposed

- In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.
- **The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.**

#### Cost-metric of miss-classification

| True class/ Predicted class | True class | Negative |
|-----------------------------|------------|----------|
| Positive                    | -          | Cost_1   |
| Negative                    | Cost_2     | -        |

- The total cost of a prediction model is the sum of `Cost_1` multiplied by the number of Instances with type 1 failure and `Cost_2` with the number of instances with type 2 failure, resulting in a `Total_cost`. In this case `Cost_1` refers to the cost that an unnecessary check needs to be done by a mechanic at a workshop, while `Cost_2` refer to the cost of missing a faulty truck, which may cause a breakdown. 
- **Total_cost = Cost_1 * No_Instances + Cost_2 * No_Instances.**
- From the above problem statement we could observe that, we have to reduce false positives and false negatives. More importantly we have to **reduce false negatives, since cost incurred due to false negative is 50 times higher than the false positives.**

#### Number of Instances

- The training set contains 60000 examples in total in which 59000 belong to the negative class and 1000 positive class. The test set contains 16000 examples.
- Number of Attributes: 171
- It is an **imbalanced** dataset

## Tech Stack used
1. Python
2. Machine Learning
3. FastAPI
4. Docker
5. MongoDB

## Infrastructure used
1. Amazon S3
2. Amazon EC2
3. Amazon ECR
4. GitHub Actions

## Architectures
### Data Collection

### Project Architecture

### Deployment Architecture

## How to run?

### Running the app locally using GitHub repository

#### Step 1: Clone the repository
```pycon
git clone https://github.com/tchandrareddy21/APS-failure-classification.git
```
#### Step 2: Create the conda environment and activate the environment
```pycon
conda create -n aps-failure-classification python=3.11 -y
```
```pycon
conda activate aps-failure-classification
```

#### Step 3: Install the requirements
```pycon
pip install -r requirements.txt
```

#### Step 4: Create .env file and add the secrets
```pycon
touch .env
```

```python
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_DEFAULT_REGION=""
MONGODB_URL=""
```

#### Step 5: Run the application
```pycon
python app.py
```
- To train the model use train route
```pycon
http://localhost:8080 
```
- To predict on new data use predict route
```pycon
http://localhost:8080
```

### Running the app using Docker

#### Step 1: Check if Dockerfile is available in the project directory

#### Step 2: Build the docker image by replacing with your secrets values
```pycon
docker build -t aps-failure-classification \
    --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> \
    --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> \
    --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> \
    --build-arg MONGODB_URL=<MONGODB_URL> .
```
#### Step 3: when you run the below command it will show the docker image with name _**aps-failure-classification**_
```pycon
docker images
```

#### Step 4: To run the docker image
```pycon
docker run -d -p 8080:8080 aps-failure-classification
```
- To train the model
```pycon
http://localhost:8080/train 
```
- To predict on new data
```pycon
http://localhost:8080/predict
```

### To deploy the project to cloud (AWS Account is needed)
#### Step 1: Create an AWS account and then login to your account
#### Step 2: You can use your root account or create a new account by using AWS Identity and Access Management (IAM) service (Best create an IAM user).
#### Step 3: Create an IAM user and add the following policies:
- AmazonS3FullAccess => To Store artifacts and models
- AmazonEC2FullAccess => It is used to create a virtual machine
- EC2InstanceConnect => To connect to virtual machine
- AmazonEC2ContainerRegistryFullAccess => To save docker image in AWS


```pycon
AmazonS3FullAccess
AmazonEC2FullAccess
EC2InstanceConnect
AmazonEC2ContainerRegistryFullAccess
```

#### Step 4: Create S3 bucket
- While creating the S3 bucket, the name should be unique.

#### Step 5: Create ECR repository to store / save docker image

#### Step 6: Create EC2 machine
1. Give the names as 'aps-failure-classification'
2. Choose AMI as ubuntu machine.
3. t2.small is an instance type.
4. If you want to connect with putty, create a .pem file.
5. For network select http, https and allow from anywhere.
6. Use 16GB as storage
&. Now review the settings and launch the instance.

#### Step 7: Select the machine and click on connect

#### Step 8: Install Docker in EC2 machine
```pycon
sudo apt update -y
```
```pycon
sudo apt upgrade -y
```
```pycon
curl -fsSL https://get.docker.com -o get-docker.sh
```
```pycon
sudo sh get-docker.sh
```
- Every time if you want to run commands, you need to use **_sudo_**. To avoid it run the below command
```pycon
sudo usermod -aG docker ubuntu
```
```pycon
newgrp docker
```

#### Step 9: Configure EC2 as self-hosted runner
1. Open your GitHub repository.
2. Go to the APS-failure-classification repository and then click on settings.
3. Now go to Actions, and then select runner.
4. Select Linux and run the commands show there in EC2.
    ```pycon
    Group name: keep default (press enter)
    name of the runner: self-hosted
    addition label: keep default (press enter)
    work folder: keep default (press enter)
    ```
5. To activate runner, execute below command
    ```pycon
   ./run.sh
    ```
6. Go to Actions secrets and variables and then add the secrets
   ```pycon
   AWS_ACCESS_KEY_ID
   AWS_SECRET_ACCESS_KEY
   AWS_REGION
   AWS_ECR_LOGIN_URI
   ECR_REPOSITORY_NAME
   MONGO_DB_URL
   ```
7. Now go to do any changes(other than README.md) in the repository code and push it. It will start the workflow.
8. Now go to EC2 dashboard and open public DNS url and then remove **_`s`_** from **`https`** then url may lokk like similir to below one.
   ```pycon
   http://ec2-3-93-46-151.compute-1.amazonaws.com/
   ```
10. In the UI shown select the train route to train the model or predict route to predict the route
   
