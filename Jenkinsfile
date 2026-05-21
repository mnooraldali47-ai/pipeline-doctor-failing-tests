pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '--user root'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -v'
            }
        }
    }

    post {
        failure {
            echo 'BUILD FEHLGESCHLAGEN: pytest hat fehlgeschlagene Tests gefunden.'
        }
        success {
            echo 'Build erfolgreich.'
        }
    }
}
