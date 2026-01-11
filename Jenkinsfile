pipeline {
    agent any
    
    environment {
        PROJECT_NAME = 'image-analyzer'
        VERSION = "${env.BUILD_ID}"
        PYTHONPATH = "${WORKSPACE}/src"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                python --version
                pip --version
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                python -m pytest src/tests/ -v
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${PROJECT_NAME}:${VERSION}")
                }
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                docker stop ${PROJECT_NAME} || true
                docker rm ${PROJECT_NAME} || true
                docker run -d \
                    --name ${PROJECT_NAME} \
                    -p 8081:8081 \
                    ${PROJECT_NAME}:${VERSION}
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}