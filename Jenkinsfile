pipeline {
    agent none
    stages {
        stage("Build slave1") {
	    agent { label "slave1" }
	    steps {
                git "https://github.com/CedricCabessa/test.git"
                sh "echo slave1 > test"
            }
        }
	stage("Build slave2") {
	    agent { label "slave2" }
	    steps {
                git "https://github.com/CedricCabessa/test.git"
                sh "echo slave2 > test"
            }
        }
    }
}
