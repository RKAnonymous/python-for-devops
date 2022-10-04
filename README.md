[![Python app test with Github Actions](https://github.com/RKAnonymous/python-for-devops/actions/workflows/devops.yml/badge.svg)](https://github.com/RKAnonymous/python-for-devops/actions/workflows/devops.yml)
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
