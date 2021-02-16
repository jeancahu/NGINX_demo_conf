#!/bin/bash

## Install
sudo pacman -S nginx fcgiwrap

## Start FCGI service
sudo fcgiwrap -s unix:fcgiwrap.socket

## Server up
sudo /usr/bin/nginx -c my_nginx_static.conf -p "$PWD"

## Server stop
sudo kill -s 15 $( cat nginx/nginx.pid )

exit 0
