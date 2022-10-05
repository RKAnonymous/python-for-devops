install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
format:
	#format code
	black *.py mylib/*.py tests/*.py
lint:
	#flake8 or # pylint
	pylint --disable=R,C *.py mylib/*.py tests/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main tests/test_*.py 
build:
	#containerization
	docker build -t deploy-fastapi .
run:
	#run docker image
	docker run -p 127.0.0.1:8080:8080 deploy-fastapi
deploy:
	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 297691715759.dkr.ecr.us-east-1.amazonaws.com
	docker build -t python-wiki .
	docker tag python-wiki:latest 297691715759.dkr.ecr.us-east-1.amazonaws.com/python-wiki:latest
	docker push 297691715759.dkr.ecr.us-east-1.amazonaws.com/python-wiki:latest

all: install lint test deploy