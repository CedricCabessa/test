stage 'clone'
node {
     git url: 'https://github.com/CedricCabessa/test.git'
}

stage 'build'
parallel "first-ui": {
    BuildIt ("first-ui")
}, "second-ui": {
    BuildIt ("second-ui")
}, "first-ws": {
    BuildIt ("first-ws")
}, "second-ws": {
    BuildIt ("second-ws")
}

def BuildIt(module) {
    echo module
}

// parallel "linux_1": node {
//        sh "./build.sh one"
//        archive "test"
//        echo "it was linux_1"
// }, "linux_2": node {
//        sh "./build.sh two"
//        archive "test"
//        echo "it was linux_2"
// }


