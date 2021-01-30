# Makefile
#
#

all: config start wait import
	@echo make all

config:
	./bin/config

start:
	./bin/start

wait:
	@echo wait for grafana to start up
	sleep 10

import:
	./bin/import

export:
	./bin/export

reset:
	./bin/reset

logrotate:
	./bin/logrotate
