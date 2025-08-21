pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing dependencies..."
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    echo "Running Selenium tests..."
                    source venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q --junitxml=reports/test-results.xml
                '''
            }
        }

        stage('Publish Test Report') {
            steps {
                junit 'reports/test-results.xml'
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh 'rm -rf venv || true'
        }
        failure {
            echo "Build failed!"
        }
        success {
            echo "Build succeeded!"
        }
    }
}
