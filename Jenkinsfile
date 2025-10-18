pipeline{
    agent any

    triggers {
        cron('H/5 * * * *')
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
                bat """
                python -m venv venv
                .\\venv\\Scripts\\activate
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
                        bat """
                        .\\venv\\Scripts\\activate
                        python -m pytest test_app.py -v
                        """
                    }
                }
                stage('Test App 2') {
                    steps{
                        echo 'Running test_app_2.py...'
                        bat """
                        .\\venv\\Scripts\\activate
                        python -m pytest test_app_2.py -v
                        """
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying application...'
                bat """
                .\\venv\\Scripts\\activate
                start /B gunicorn --bind 127.0.1.1:5000 app:app > gunicorn.log 2>&1 &
                echo Gunicorn started on http://127.0.1.1:5000
                """
            }
        }
    }
}
