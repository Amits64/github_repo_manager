from setuptools import setup, find_packages

setup(
    name='github_repo_manager',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'github_repo_manager=github_repo_manager.main:create_github_repo',
        ],
    },
)

