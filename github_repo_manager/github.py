import requests
from github_repo_manager.config import GITHUB_API_URL, GITHUB_TOKEN

def create_github_repo(name, description):
    url = f"{GITHUB_API_URL}/user/repos"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    data = {'name': name, 'description': description, 'private': False}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def list_github_repos():
    url = f"{GITHUB_API_URL}/user/repos"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()
