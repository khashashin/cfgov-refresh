pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS') 
    }
    stages {
        stage('Unit Testing') {
            steps {
                parallel(
                    "Front-End Tests": {
                        sleep 2
                        echo 'Hello front-end!'
                    },
                    "Back-End Tests": {
                        sleep 2
                        echo 'Hello back-end!'
                        exit 1
                    },
                    "Acceptance Tests": {
                        sleep 5
                        echo 'Hello acceptance!'
                    }
                )
            }
        }
        stage('Coverage') {
            steps {
                parallel(
                    "Front-End Coverage": {
                        sleep 1
                        echo 'Hello front-end coverage!'
                    },
                    "Back-End Coverage": {
                        sleep 1
                        echo 'Hello back-end coverage!'
                    }
                )
            }
        }
    }
}
