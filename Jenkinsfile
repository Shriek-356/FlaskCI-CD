pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git url: 'https://github.com/Shriek-356/FlaskCI-CD.git', branch: 'master'
      }
    }
    stage('Build') {
      steps {
        echo 'Test thành công'
      }
    }
    stage('Deploy') {
            steps {
                bat 'robocopy . D:\\wwwroot\\mysite *.html /E /MIR /NFL /NDL /NJH /NJS /NP'
            }
    }
  }
}