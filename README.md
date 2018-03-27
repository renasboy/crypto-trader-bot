## Requirements

- Debian 9 / Raspbian
- Docker
- Docker Compose

### Debian / Raspbian

Well debian/raspbian is not really required but this s what I used

### Installing docker

Refer to [docs.docker.com](https://docs.docker.com)

docker on debian

```shell
# curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable"
# apt-get update
# apt-get install docker-ce
# usermod -aG docker $USER
```

or

docker on raspbian

```shell
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
$ sudo usermod -aG docker $USER
```


### Installing docker compose

docker compose on debian

```shell
# curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-Linux-x86_64 -o /usr/bin/docker-compose
# chmod 755 /usr/bin/docker-compose
```

or

docker compose on raspbian

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
cp conf/bl3p_example_conf conf/bl3p_eur_btc.conf

vim src/bl3p_eur_btc.conf

# set the EXCHANGE to the desired exchange (bl3p, binance or cobinhood)
# set the PUBLIC and PRIVATE keys when available
# set SYMBOL_X to available symbols in the exchange
# set MAX_SYMBOL_X_PERCENTAGE to percentage amount from available to use
# set DRY_RUN to 1 in order to only show what the bot would do
# set BOT_ALGO to on of the available algos (boring_but_safe, ro_cano)
```

## Install and start up containers

```shell
make
```

## Check what is going on in the logs

```shell
tail -f log/bot.log
```

