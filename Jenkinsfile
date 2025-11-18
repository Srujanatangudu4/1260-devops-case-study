pipeline{
    agent any
    stages
    {
        stage('Build Docker Image'){
            steps{
                echo "Build Docker Image"
                bat "docker build -t kubedemoapp:v1 ."
            }
        }
        stage('Docker Login'){
            steps{
                bat 'docker login -u srujanatangudu4 -p Srujana@2004'
            }
        }
        stage('push Docker Image to Docker Hub'){
            steps{
                echo "push Docker Image to Docker Hub"
                bat "docker tag kubedemoapp:v1 Srujanatangudu4/sample:kubeimage1"
                bat "docker push Srujanatangudu4/sample:kubeimage1"
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
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
