install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or # pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main tests/test_*.py 
build:
	#containerization
	docker build -t deploy-fastapi .
deploy:
	#deploy

all: install lint test deploy