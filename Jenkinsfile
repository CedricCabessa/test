node('linux_1') {
     stage 'clone'
     git url: 'https://github.com/CedricCabessa/test.git'

     stage 'build'
     sh "./build.sh"
     archive "test"

     stage 'package'
     echo "it was linux_1"
}

node('linux_2') {
     stage 'clone'
     git url: 'https://github.com/CedricCabessa/test.git'

     stage 'build'
     sh "./build.sh"
     archive "test"

     stage 'package'
     echo "it was linux_2"
}
