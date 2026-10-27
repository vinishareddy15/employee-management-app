pipeline {
    agent any

    stages {

        stage('Verify Environment') {
            steps {
                sh 'java -version'
                sh 'git --version'
                sh 'docker --version'
            }
        }

        stage('Build Backend Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t backend-app .'
                }
            }
        }

        stage('Build Frontend Image') {
            steps {
                dir('frontend') {
                    sh 'docker build -t frontend-app .'
                }
            }
        }

        stage('List Images') {
            steps {
                sh 'docker images'
            }
        }
    }
}
