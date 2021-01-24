#!/bin/bash

mkdir -p /crypto-trader-bot/log
python3 /crypto-trader-bot/src/listener.py >> /crypto-trader-bot/log/bot.log 2>&1
