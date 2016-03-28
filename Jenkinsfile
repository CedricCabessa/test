stage 'clone'
node {
     git url: 'https://github.com/CedricCabessa/test.git'
}

stage 'build'
parallel "random-string-1": {
    node("linux-1") {
      sh "./build.sh one"
      archive "test"
      echo "it was linux_1"
    }
}, "random-string-2": {
    node("linux-2") {
      sh "./build.sh two"
      archive "test"
      echo "it was linux_2"
    }
}
