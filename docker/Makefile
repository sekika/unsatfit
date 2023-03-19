all:
	cat Readme.md

install:
	docker build -t swrcfit:1.0 .

run:
	docker run --name swrcfit -d --mount type=bind,source=$(PWD)/../swrcfit,destination=/var/www/html -p 80:80 swrcfit:1.0
	docker exec -t swrcfit /bin/bash -c "chmod 777 /var/www/html/img"

stop:
	docker stop swrcfit
	docker rm swrcfit

sh:
	docker exec -i -t swrcfit /bin/bash

update:
	docker exec -t swrcfit /bin/bash -c "apt update && apt upgrade -y && apt clean"
