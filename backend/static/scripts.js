document.addEventListener('DOMContentLoaded', function () {
    // Handle form submission
    document.getElementById('create-repo-form').addEventListener('submit', function (event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const description = document.getElementById('description').value;

        fetch('/create_repo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, description })
        })
        .then(response => response.json())
        .then(data => {
            alert('Repository created successfully!');
            // Optionally update the repo list or clear form fields
            document.getElementById('create-repo-form').reset();
            loadRepos(); // Function to reload the list of repos
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while creating the repository.');
        });
    });

    // Function to load existing repos
    function loadRepos() {
        fetch('/repos')
            .then(response => response.json())
            .then(data => {
                const repoList = document.getElementById('repo-list');
                repoList.innerHTML = '';
                data.forEach(repo => {
                    const li = document.createElement('li');
                    li.textContent = repo.name;
                    repoList.appendChild(li);
                });
            });
    }

    loadRepos(); // Load repos when the page loads
});
