pipeline {
    agent any

    environment {
        PROJECT_ID = "harsha-498909"
        REGION = "us-central1"
        REPOSITORY = "jenkins-images"
        IMAGE_NAME = "kivo-demo-app"
        IMAGE_URI = "us-central1-docker.pkg.dev/harsha-498909/jenkins-images/kivo-demo-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Tag Image') {
            steps {
                sh '''
                docker tag ${IMAGE_NAME}:latest ${IMAGE_URI}
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                docker push ${IMAGE_URI}
                '''
            }
        }

        stage('Deploy Cloud Run') {
            steps {
                sh '''
                gcloud run deploy ${IMAGE_NAME} \
                --image ${IMAGE_URI} \
                --region ${REGION} \
                --platform managed \
                --allow-unauthenticated
                '''
            }
        }
    }
}