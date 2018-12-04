FLASK_APP=tutorial
SRC_DIR=$(CURDIR)/${FLASK_APP}
TESTING_DIR=$(CURDIR)/tests

dev:
	flask run --host=127.0.0.1 --port=8000

prod:
	set FLASK_ENV=production&& set FLASK_DEBUG=0&& flask run --host=0.0.0.0 --port=3000
