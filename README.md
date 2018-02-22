## Requirements

- Debian 9
- Docker
- Docker Compose

### Debian

Well debian is not really required but this s what I used

### Installing docker

Refer to [docs.docker.com](https://docs.docker.com)

```shell
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```

or 

```shell
# curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable"
# apt-get update
# apt-get install docker-ce
# usermod -aG docker $USER
```

### Installing docker compose

```shell
# curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-Linux-x86_64 -o /usr/bin/docker-compose
# chmod 755 /usr/bin/docker-compose
```

on raspberry PI

```shell
apt-get install python-pip
pip install docker-compose
```

## Installing and starting the bot

```shell
git clone REPO
cd crypto-trader-bot
make
tail -f bot.log
```

## Stopping the bot

```shell
make stop
```

## Restarting the bot

```shell
make restart
```

# Reset bot by cleaning local trades 
```shell
make reset
```

# Export grafana datasources and dashboard
```shell
make export
```

# Import grafana datasources and dashboard
```shell
make import
make restart
```
