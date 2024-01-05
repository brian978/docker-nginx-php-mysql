default:
	echo "Please select a valid option"

start:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose stop
	docker-compose up -d

cli:
	docker exec -it starter-app-php /bin/bash

cleanup:
	docker-compose down
