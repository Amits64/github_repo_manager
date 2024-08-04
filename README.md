[![CI](https://github.com/Amits64/github_repo_manager/actions/workflows/main.yml/badge.svg)](https://github.com/Amits64/github_repo_manager/actions/workflows/main.yml)

# GitHub Repo Manager

## Overview

**GitHub Repo Manager** is a Python application designed to simplify the management of GitHub repositories. It provides functionality to create, list, and manage GitHub repositories programmatically using the GitHub API. This tool is ideal for developers who need to automate GitHub repository operations or integrate them into their workflows.

## Features

- **Create GitHub Repositories**: Programmatically create new repositories on GitHub.
- **Manage Repository Settings**: Update repository details and settings.
- **List Repositories**: Retrieve and display information about repositories.
- **Enhanced Logging**: Detailed logging of operations and errors.

## Getting Started

### Prerequisites

- **Python 3.9+**: Ensure you have Python 3.9 or later installed.
- **GitHub Account**: You need a GitHub account with a Personal Access Token (PAT) for authentication.
- **Docker**: Optional, for running the application in a Docker container.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:YourUsername/github_repo_manager.git
   cd github_repo_manager
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the root directory of the project and add your GitHub Personal Access Token:

   ```env
   GITHUB_TOKEN=your_personal_access_token
   ```

### Running the Application

#### Running with Python

1. **Create a New Repository**:

   ```python
   from github_repo_manager.github import create_github_repo

   create_github_repo("new-repo-name", "Description of the new repository")
   ```

2. **List All Repositories**:

   ```python
   from github_repo_manager.github import list_github_repos

   repos = list_github_repos()
   for repo in repos:
       print(repo['name'])
   ```

#### Running with Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t github_repo_manager .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -it --rm \
     -e GITHUB_TOKEN=your_personal_access_token \
     github_repo_manager
   ```

   Replace `your_personal_access_token` with your actual GitHub PAT. The `-it` flag runs the container in interactive mode, and `--rm` ensures the container is removed after it exits.

### Running Tests

To ensure the application is working correctly, run the unit tests:

```bash
python3 -m unittest discover -s tests
```

### Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**: Create your own fork of the repository on GitHub.
2. **Create a Branch**: Create a new branch for your changes.
3. **Make Changes**: Implement your changes and write tests.
4. **Submit a Pull Request**: Push your changes to your fork and open a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For questions or support, please contact [Amit Singh](mailto:chauhanamit090@hotmail.com).

---

**Note:** Replace placeholder text (like `your_personal_access_token`, `YourUsername`, etc.) with your actual information.


**GitHub Repo Manager** is developed and maintained by [Amits64](https://github.com/Amits64).


### Additional Notes:

- **Docker Build and Run Instructions**: These instructions are included for those who prefer using Docker to run the application. Make sure your `Dockerfile` is correctly set up to copy the required files and set up the environment.

- **Environment Variables in Docker**: Using the `-e` flag to pass the GitHub PAT as an environment variable ensures that sensitive information is not hardcoded into the Docker image.

Feel free to adjust the file based on any additional details or specific instructions relevant to your project.