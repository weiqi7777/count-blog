pipeline {
  agent any
  stages {
    stage('stage 1') {
      parallel {
        stage('stage 1') {
          agent any
          steps {
            echo 'stage 1/step 1'
          }
        }
        stage('') {
          agent any
          steps {
            echo 'stage 1/step 2'
          }
        }
      }
    }
    stage('stage 2') {
      parallel {
        stage('stage 2') {
          steps {
            echo 'stage 2/step  1'
          }
        }
        stage('') {
          steps {
            echo 'stage 2/step 2'
          }
        }
      }
    }
    stage('stage 3') {
      steps {
        echo 'stage 3/step 1'
      }
    }
  }
}