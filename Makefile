setup:
	pip install -r requirements.txt -r requirements_dev.txt

test:
	nosetests tests

lint:
	flake8