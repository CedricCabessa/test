stage('Build') {
    node {
        git https://github.com/CedricCabessa/test.git
        sh './build.sh ${NODE_NAME}'
        stash includes: 'test', name: 'app'
    }
}