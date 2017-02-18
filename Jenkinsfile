pipeline {
    agent {
        label 'slave1'
    }
    stages {
        stage("Build") {
            steps {
                git "https://github.com/CedricCabessa/test.git"
                sh "echo plop > test"
            }
        }
    }
}
