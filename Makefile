APP_DIR = ./sample/

run:
	flask --app $(APP_DIR)core run

run_debug:
	flask --app $(APP_DIR)core run --debug

env:
	. .venv/bin/activate
