setup:
	pip install -r requirements.txt -r requirements_dev.txt

test:
	python tests/test_algorithms.py