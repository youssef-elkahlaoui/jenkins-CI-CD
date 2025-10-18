pipeline{
    agent any

    triggers {
        cron('H/1 * * * *')
        pollSCM('H/2 * * * *')
    }

    stages{
        stage('Checkout'){
            steps{
                echo 'Checking out code...'
                git branch: 'main', url: 'https://github.com/youssef-elkahlaoui/jenkins-CI-CD'
            }
        }
        stage('Setup Venv'){
            steps{
                echo 'Setting up virtual environment...'
                sh """
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }
        stage('Run Tests'){
            when {
                not {
                    changeset "**/README.md"
                }
            }
            parallel {
                stage('Test App 1') {
                    steps{
                        echo 'Running test_app.py...'
                        sh """
                        . venv/bin/activate
                        python -m pytest test_app.py -v
                        """
                    }
                }
                stage('Test App 2') {
                    steps{
                        echo 'Running test_app_2.py...'
                        sh """
                        . venv/bin/activate
                        python -m pytest test_app_2.py -v
                        """
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying application...'
                sh """
                . venv/bin/activate
                gunicorn --bind 127.0.0.1:5000 app:app &
                echo Gunicorn started on http://127.0.0.1:5000
                """
            }
        }
    }
}
