.PHONY: clean all

all: run

run: venv banco
	source venv/bin/activate; \
	export FLASK_ENV=development; \
	flask run

shell: venv banco
	source venv/bin/activate; \
	export FLASK_ENV=development; \
	flask shell

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv/
	source venv/bin/activate; \
	pip install --upgrade pip; \
	pip install wheel; \
	pip install -r requirements.txt

banco: /tmp/teste.db

/tmp/teste.db: venv migrations
	source venv/bin/activate; \
	flask db upgrade

migrations:
	source venv/bin/activate; \
	flask db init; \
	flask db migrate; \

clean:
	find . -name "*.pyc" -type f -delete
	find . -name __pycache__ -type d -exec rm -rf {} 2> /dev/null +
	find . -name "*.egg-info" -type d -exec rm -rf {} 2> /dev/null +
	find . -type d -empty -delete
	test ! -d venv || rm -r venv
	test ! -f /tmp/teste.db || rm -r /tmp/teste.db
