## Requirements

- Debian 9
- Docker
- Docker Compose

### Debian

Well debian is not really required but this s what I used

### Installing docker

Refer to [docs.docker.com](https://docs.docker.com)

```shell
# curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable"
# apt-get update
# apt-get install docker-ce
# usermod -aG docker $USER
```

or

docker on raspberry PI

```shell
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
$ sudo usermod -aG docker $USER
```


### Installing docker compose

```shell
# curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-Linux-x86_64 -o /usr/bin/docker-compose
# chmod 755 /usr/bin/docker-compose
```

or

docker compose on raspberry PI

```shell
$ sudo apt-get install python-pip
$ sudo pip install docker-compose
```

## Installing and starting the bot


## Clone the repo

```shell
git clone https://github.com/renasboy/crypto-trader-bot
cd crypto-trader-bot
```

## Configure the bot and choose the exchange
```shell
vim src/bot.py
# set the constant EXCHANGE to the desired exchange (bl3p, binance or kraken)
```

## Congigure the exchange and set the API keys
```shell
vim src/bl3p.py
vim src/binance.py
vim src/kraken.py
# set the public and private API key
```

## Install and start up containers

```shell
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
