pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t colorapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u srujanatangudu4 -p Srujana@2004'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag colorapp:v1 srujanatangudu4/sample:colorapp1"
                bat "docker push srujanatangudu4/sample:colorapp1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Successful'
        }
        failure {
            echo 'Unsuccessful'
        }
    }
}
