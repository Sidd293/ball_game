pipeline {
      agent {docker { image 'python:3' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip install -r requirements.txt' 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python index.py' 
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'

            }
        }
    }
}
