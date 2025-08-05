// Jenkinsfile (Scripted Pipeline)
// This file defines the Continuous Integration pipeline for your Django project.
// It uses 'uv' for Python dependency management.

// Define the agent where the pipeline will run.
// 'any' means Jenkins will pick any available agent.
// For our current setup, this will run on the Jenkins master node (inside its Docker container).
agent any

// Define the stages of your CI pipeline
stages {
    // Stage 1: Checkout - Pull your Django project code from Git.
    stage('Checkout') {
        steps {
            echo 'Checking out source code...'
            // The 'checkout scm' step pulls the code from the configured SCM (Git in our case)
            // into the workspace.
            checkout scm
        }
    }

    // Stage 2: Setup Environment - Create a Python virtual environment and install uv.
    stage('Setup Environment') {
        steps {
            echo 'Ensuring uv is installed and setting up Python virtual environment...'
            // Install uv globally in the Jenkins container if not present.
            // This is typically needed only once per Jenkins agent/container setup.
            sh 'pip install uv'

            // Create a virtual environment using uv. It will typically create it in .venv
            sh 'uv venv'

            echo 'Virtual environment created with uv.'
        }
    }

    // Stage 3: Install Dependencies - Install Python packages from pyproject.toml using uv.
    stage('Install Dependencies') {
        steps {
            echo 'Installing Python dependencies using uv...'
            // Install dependencies defined in pyproject.toml into the .venv
            // 'uv pip install .' will install your project's dependencies and your project itself
            // in editable mode if it's a package.
            // If you only want to install dependencies and not the project itself,
            // you might use 'uv pip install --no-deps --group dev' for dev dependencies
            // or 'uv pip install --no-deps' for runtime dependencies.
            // For a Django project, 'uv pip install .' is often appropriate to ensure
            // the project itself is discoverable if it has internal imports.
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
            // Execute Django tests using the python executable from the uv virtual environment.
            // uv provides a 'run' command that handles activation for you.
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
    // Clean up the workspace after the build, regardless of success or failure.
    // This is good practice to ensure clean builds and save disk space.
    cleanup {
        deleteDir()
    }
}