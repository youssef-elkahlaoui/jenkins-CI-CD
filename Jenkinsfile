pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/youssef-elkahlaoui/jenkins-CI-CD'
            }
        }

        stage('Setup Venv') {
            steps {
                echo 'Setting up virtual environment...'
                sh """
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh """
                . venv/bin/activate
                python -m pytest test_app.py -v
                """
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh """
                . venv/bin/activate
                nohup gunicorn --bind 0.0.0.0:5000 app:app > gunicorn.log 2>&1 &
                echo Gunicorn started on http://localhost:5000
                """
            }
        }
    }
}
