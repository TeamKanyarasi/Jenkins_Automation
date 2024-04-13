#!/bin/bash
sudo apt update
sudo apt-get upgrade -y
sudo apt-get install nginx
sudo systemctl enable nginx
sudo systemctl start nginx
