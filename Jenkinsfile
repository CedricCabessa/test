stage 'clone'
node {
     git url: 'https://github.com/CedricCabessa/test.git'
}

stage 'build'
parallel "random-string-1": {
    node("linux_1") {
      sh "./build.sh one"
      archive "test"
      echo "it was linux_1"
    }
}, "random-string-2": {
    node("linux_2") {
      sh "./build.sh two"
      archive "test"
      echo "it was linux_2"
    }
}
