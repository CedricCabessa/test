stage 'clone'
node {
     git url: 'https://github.com/CedricCabessa/test.git'
     stash "source"
}

stage 'build'
parallel "random-string-1": {
    node("linux_1") {
      unstash "source"
      sh "./build.sh one"
      echo "it was linux_1"
    }
}, "random-string-2": {
    node("linux_2") {
      unstash "source"
      sh "./build.sh two"
      echo "it was linux_2"
    }
}

stage 'archive'
node {
     archive "test"
}
