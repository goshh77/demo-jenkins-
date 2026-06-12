pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                credentialsId: 'github-creds',
                url: 'https://github.com/goshh77/demo-jenkins-.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t kivo-demo-app .'
            }
        }

        stage('Verify Image') {
            steps {
                sh 'docker images'
            }
        }
    }
}