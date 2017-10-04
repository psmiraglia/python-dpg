venv:
	virtualenv -p python3 .venv

install:
	python setup.py install

test:
	python setup.py test
