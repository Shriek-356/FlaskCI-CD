pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git url: 'https://github.com/Shriek-356/FlaskCI-CD.git', branch: 'master'
      }
    }
    stage('Build') {
      steps { echo 'Test thành công' }
    }
    stage('Deploy') {
      steps {
        bat '''
          robocopy myapp D:\\wwwroot\\mysite *.html /E /NFL /NDL /NJH /NJS /NP
          set RC=%ERRORLEVEL%
          if %RC% LEQ 3 ( exit /B 0 ) else ( exit /B %RC% )
        '''
      }
    }
  }
}
