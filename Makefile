default:
	echo "Please select a valid option"

start:
	python3 scripts/run.py

stop:
	docker-compose stop

restart:
	docker-compose stop
	python3 scripts/run.py

cli:
	python3 scripts/cli.py

cleanup:
	docker-compose down
