setup:
	pip install -r requirements.txt -r requirements_dev.txt

lint:
	flake8

test:
	nosetests

run:
	python server.py
