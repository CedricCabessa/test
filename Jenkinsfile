stage 'clone'
node {
     git url: 'https://github.com/CedricCabessa/test.git'
}

stage 'build'
parallel "random-string-1": {
    node {
      sh "./build.sh one"
      archive "test"
      echo "it was linux_1"
    }
}, "random-string-2": {
    node {
      sh "./build.sh two"
      archive "test"
      echo "it was linux_2"
    }
}
