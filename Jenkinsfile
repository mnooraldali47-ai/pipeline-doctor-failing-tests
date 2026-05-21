pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest -v'
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
