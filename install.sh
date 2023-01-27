#! /usr/bin/env bash

python3 -m pip install -r ./requirements.txt

sudo cp -r ./bin/migrate /usr/local/bin/migrate
sudo cp -r ./src /usr/local/lib/migrate
