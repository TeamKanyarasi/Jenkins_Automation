#!/bin/bash
sudo apt update
sudo apt-get upgrade -y
sudo apt-get install nginx
sudo apt-get enable nginx
sudo apt-get start nginx