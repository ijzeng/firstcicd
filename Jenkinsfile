node {
    def app

    stage('Cloning repo') {
        /* Cloning the Repository */

        checkout scm
    }

    stage('Building image') {
        /* This is Dockerizing */

        app = docker.build("ultimaterockie/cicdapp")
    }

    stage('Testing image') {
        
        app.inside {
            echo "Test passed"
        }
    }

    stage('Pushing image') {
    
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
            } 
                echo "Dockerizing image and push to DockerHub"
    }
}
