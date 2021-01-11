default:
	echo "Please select an action from: run, stop or cli"

run:
	python3 scripts/run.py

stop:
	docker-compose stop

cli:
	python3 scripts/cli.py
