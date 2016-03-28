node('linux_1') {
     stage 'clone'
     git url: 'https://github.com/CedricCabessa/test.git'

     stage 'build'
     sh "./build.sh"
     archive "test"

     stage 'package'
     echo "$node"
}
