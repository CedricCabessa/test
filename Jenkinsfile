stage('Build') {
    node {
        git https://github.com/CedricCabessa/test.git
	sh "echo plop > test"
        stash includes: 'test', name: 'app'
    }
}