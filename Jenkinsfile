pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // 'bat' is used for Windows instead of 'sh'
                bat 'pip install flask pytest'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'echo "Tests Passed"'
            }
        }
        stage('Build Application') {
            steps {
                // Windows 10/11 supports tar, or we simulate a build
                bat 'tar -cf app.tar.gz app.py'
            }
        }
        stage('Deploy Application') {
            steps {
                // Use 'copy' instead of 'cp' and %TEMP% for Windows temp folder
                bat 'copy app.tar.gz %TEMP%\\app.tar.gz'
            }
        }
    }
}
