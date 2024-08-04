import requests
import json
import base64
from github_repo_manager.config import GITHUB_API_URL
from github_repo_manager.logger import logger

def create_github_repo():
    github_token = input("Enter your GitHub Personal Access Token: ")
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    repo_name = input("Enter the name of the repository: ")
    private = input("Should the repository be private? (yes/no): ").lower() == 'yes'
    description = input("Enter the description of the repository (optional): ")
    issues = input("Enable issues? (yes/no): ").lower() == 'yes'
    wiki = input("Enable wiki? (yes/no): ").lower() == 'yes'
    homepage = input("Enter the homepage URL (optional): ")
    gitignore_template = input("Enter the gitignore template (default is 'Python'): ") or 'Python'
    include_readme = input("Include a README.md file? (yes/no): ").lower() == 'yes'

    repo_data = {
        'name': repo_name,
        'private': private,
        'description': description,
        'has_issues': issues,
        'has_wiki': wiki,
        'homepage': homepage,
        'auto_init': False,
        'gitignore_template': gitignore_template if gitignore_template else None,
        'has_projects': False,
    }

    try:
        response = requests.post(f'{GITHUB_API_URL}/user/repos', headers=headers, data=json.dumps(repo_data))
        response.raise_for_status()
        
        if response.status_code == 201:
            logger.info(f'Successfully created repository {repo_name}')
            if include_readme:
                readme_content = input("Enter the content for the README.md file: ")
                create_readme(github_token, repo_name, readme_content)
        else:
            logger.error(f'Failed to create repository {repo_name}. Response: {response.content}')
    except requests.exceptions.RequestException as e:
        logger.error(f'Error creating repository: {e}')

def create_readme(github_token, repo_name, content):
    github_username = input("Enter your GitHub username: ")
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    readme_data = {
        'message': 'Add README.md',
        'content': base64.b64encode(content.encode()).decode('utf-8')
    }

    try:
        response = requests.put(f'{GITHUB_API_URL}/repos/{github_username}/{repo_name}/contents/README.md', headers=headers, data=json.dumps(readme_data))
        response.raise_for_status()
        
        if response.status_code == 201:
            logger.info(f'Successfully added README.md to repository {repo_name}')
        else:
            logger.error(f'Failed to add README.md to repository {repo_name}. Response: {response.content}')
    except requests.exceptions.RequestException as e:
        logger.error(f'Error adding README.md: {e}')

