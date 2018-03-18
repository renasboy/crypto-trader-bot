# Makefile
#
# make docker
# Creates the docker container with influxdb and grafana
#
# 
#

all: conf deps start import
	@echo make all

conf:
	@test -n "`uname -m | fgrep arm`" && sed -i 's@grafana/grafana:latest@fg2it/grafana-armhf:v5.0.3@g' docker-compose.yml || echo

deps:
	@echo install requirements

start:
	@echo starting up docker
	docker-compose -f docker-compose.yml up -d

restart:
	@echo starting up docker
	docker restart crypto_trader_bot

stop:
	@echo stop docker
	docker-compose -f docker-compose.yml down

import:
	@echo wait for grafana to start up
	sleep 5
	@echo delete old datasource from grafana
	curl -X DELETE "http://admin:s3cr3t@localhost:3000/api/datasources/name/influx" -H "Content-Type: application/json" -H "Accept: application/json"
	@echo
	@echo import datasource to grafana
	curl -X POST "http://admin:s3cr3t@localhost:3000/api/datasources" -H "Content-Type: application/json" -H "Accept: application/json" --data-binary @datasource.json
	@echo
	@echo delete old dashboards from grafana
	curl -X DELETE "http://admin:s3cr3t@localhost:3000/api/dashboards/db/crypto-trader-bot" -H "Content-Type: application/json" -H "Accept: application/json"
	@echo
	curl -X DELETE "http://admin:s3cr3t@localhost:3000/api/dashboards/db/ma-re" -H "Content-Type: application/json" -H "Accept: application/json"
	@echo
	@echo import dashboard to grafana
	curl -X POST "http://admin:s3cr3t@localhost:3000/api/dashboards/db" -H "Content-Type: application/json" -H "Accept: application/json" --data-binary @dashboard.json
	@echo
	curl -X POST "http://admin:s3cr3t@localhost:3000/api/dashboards/db" -H "Content-Type: application/json" -H "Accept: application/json" --data-binary @dashboard-ma-re.json
	@echo

export:
	@echo making a backup of previous files
	cp datasource.json datasource.json.backup
	cp dashboard.json dashboard.json.backup
	cp dashboard-ma-re.json dashboard-ma-re.json.backup
	@echo export datasource from grafana
	curl "http://admin:s3cr3t@localhost:3000/api/datasources/name/influx" > datasource.json
	@echo export dashboard from grafana
	curl "http://admin:s3cr3t@localhost:3000/api/dashboards/db/crypto-trader-bot" | sed 's/"id":[0-9]*/"id":null/' > dashboard.json
	@echo export dashboard from grafana
	curl "http://admin:s3cr3t@localhost:3000/api/dashboards/db/ma-re" | sed 's/"id":[0-9]*/"id":null/' > dashboard-ma-re.json

reset:
	@echo reset influx trade
	curl -X POST "http://localhost:8086/query?u=root&p=root&db=crypto_trader_bot&q=DROP+measurement+trade" -H "Content-Type: application/json" -H "Accept: application/json"	
