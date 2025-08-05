// Jenkinsfile (Declarative Pipeline)
// This file defines the Continuous Integration pipeline for your Django project.
// It uses 'uv' for Python dependency management and runs stages within a Python Docker container.

pipeline {
    // Define the agent where the pipeline will run.
    // We're now telling Jenkins to run all steps within a specific Docker image.
    agent {
        docker {
            image 'python:3.12-slim-bookworm' // Use a Python 3.12 image
            args '-u root' // Run as root inside the container for installation steps
        }
    }

    // Define the stages of your CI pipeline
    stages {
        // Stage 1: Checkout - Pull your Django project code from Git.
        // This stage now runs inside the 'python:3.12-slim-bookworm' container.
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        // Stage 2: Install uv and Create Virtual Environment
        // This stage also runs inside the Python Docker container.
        stage('Setup Environment') {
            steps {
                echo 'Ensuring uv is installed and setting up Python virtual environment...'
                // Install uv inside the Python Docker container.
                sh 'pip install uv'

                // Create a virtual environment using uv. It will typically create it in .venv
                // This venv will be inside the workspace within the Docker container.
                sh 'uv venv'

                echo 'Virtual environment created with uv.'
            }
        }

        // Stage 3: Install Dependencies - Install Python packages from pyproject.toml using uv.
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies using uv...'
                // Install dependencies defined in pyproject.toml into the .venv
                // uv will automatically use the .venv created in the previous step.
                sh 'uv pip install .'

                // Also install the 'dev' dependency group for linters/test runners
                sh 'uv pip install --group dev'

                echo 'Dependencies installed.'
            }
        }

        // Stage 4: Run Tests - Execute Django's unit tests.
        stage('Run Tests') {
            steps {
                echo 'Running Django tests...'
                // Execute Django tests using uv run, which handles activating the venv.
                sh 'uv run python manage.py test'
                echo 'Tests completed.'
            }
        }
    }

    // Post-build actions (optional, but good practice)
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
        cleanup {
             deleteDir()
        }
    }
}