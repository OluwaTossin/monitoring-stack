pipeline {
    agent any
    environment {
        // Define environment variables if needed
        DOCKER_IMAGE = 'my-app-image'
        ECR_REGISTRY = '147360193006.dkr.ecr.region.amazonaws.com'
        ECR_REPOSITORY = 'my-app-repo'
        IMAGE_TAG = 'latest'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Log in to the Docker registry
                    sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
                    
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE} ."
                    
                    // Tag the Docker image
                    sh "docker tag ${DOCKER_IMAGE}:latest ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}"
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Running test steps...'
                // Your testing commands go here
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Push the Docker image to ECR
                    sh "docker push ${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}"
                }
            }
        }
    }
    post {
        always {
            // Steps to clean up after the pipeline runs
        }
    }
}
