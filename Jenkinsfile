stage 'clone'
node {
     git url: 'https://github.com/CedricCabessa/test.git'
}

stage 'build'
parallel (
     node("linux_1") {
       sh "./build.sh"
       archive "test"
       echo "it was linux_1"
     },
     node("linux_2") {
       sh "./build.sh"
       archive "test"
       echo "it was linux_2"
     }
)

