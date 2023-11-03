default:
	echo "Please select a valid option"

install:
	sh scripts/install_laravel.sh

start:
	sh scripts/run.sh

stop:
	docker-compose stop

restart:
	docker-compose stop
	sh scripts/run.sh

cli:
	docker-compose run --rm -it php /bin/bash

cleanup:
	docker-compose down
