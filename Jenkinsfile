pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')  // Poll GitHub every 5 minutes
    }
    environment {
        IMAGE_NAME = "kathanshah1893/jdsession13-backend"
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }

       stage('Push Docker Image') {
    steps {
        bat """
        echo kathan@1234 | docker login -u kathanshah1893 --password-stdin
        docker push %IMAGE_NAME%:latest
        """
    }
}

        stage('Deploy to Minikube') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-windows', variable: 'KUBECONFIG')]) {
                    bat """
                    echo Using kubeconfig from credentials
                    kubectl config use-context minikube
                    kubectl set image deployment/jdsession13-backend jdsession13-backend=%IMAGE_NAME%:latest
                    kubectl rollout status deployment/jdsession13-backend
                    """
                }
            }
        }
    }
}
