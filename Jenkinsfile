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
        // CHỌN 1 trong 2 khối dưới đây:

        // --- A: PowerShell Copy-Item ---
        // bat 'powershell -NoProfile -Command "Copy-Item -Path myapp\\* -Include *.html,*.css,*.js -Destination D:\\wwwroot\\mysite -Recurse -Force"'

        // --- B: Robocopy + normalize exit code ---
        bat '''
          robocopy myapp D:\\wwwroot\\mysite *.html *.css *.js /E /NFL /NDL /NJH /NJS /NP
          set RC=%ERRORLEVEL%
          if %RC% LEQ 3 ( exit /B 0 ) else ( exit /B %RC% )
        '''
      }
    }
  }
}
