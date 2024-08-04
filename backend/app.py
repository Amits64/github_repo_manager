import sys
import os
from flask import Flask, request, jsonify, render_template

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from github_repo_manager.github import create_github_repo, list_github_repos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/repos', methods=['GET'])
def get_repos():
    repos = list_github_repos()
    return jsonify(repos)

@app.route('/create_repo', methods=['POST'])
def create_repo():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    result = create_github_repo(name, description)
    return jsonify(result)

@app.route('/repo/<repo_name>', methods=['GET'])
def repo_details(repo_name):
    # Add logic to fetch and display details of a specific repository
    return render_template('repo_details.html', repo_name=repo_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
