[![Python app test with Github Actions](https://github.com/RKAnonymous/python-for-devops/actions/workflows/devops.yml/badge.svg)](https://github.com/RKAnonymous/python-for-devops/actions/workflows/devops.yml)
![Python app test with Github Actions](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiVnRJLzh4OUh0S2ZLQUQ5OVp1QkM1Q1Z0NmIzNzg0NHpjaDFpUXQvNmN2Ny9lZ24zZmN6WkxvQnBLMnRlZlRvZHBFSE5QZTZrVE5sY1hvRnM4NkliMHRNPSIsIml2UGFyYW1ldGVyU3BlYyI6IkFHamlIZU4yS2pLOUJpa0giLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg?logo=Python&logoColor=yellow)](https://www.python.org/downloads/release/python-360/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.85.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)


# python-for-devops
Python practice for DevOps techs

## Scaffold

1. Create a Python Virtual Environment `python3 -m venv ~/venv` or `virtualenv ~/venv`
2. Create empty files `Makefile`, `Dockerfile`, `main.py`, `requirements.txt`, `mylib/__init__.py`
3. Populate `Makefile`
4. Setup CI pipeline, i.e. check code for issues like lint errors

![lint-error](https://user-images.githubusercontent.com/104907216/193566005-29973d8b-57c1-4c53-8e84-ea19e6b298f8.png)

5. Build CLI using Python Fire library `./my_cli.py --help` to test logic
