#!/bin/sh
cp ./agent/daemon.py /usr/local/lib/narcissujsk/
cp ./agent/run.sh /usr/local/lib/narcissujsk/
cp ./agent/stop.sh /usr/local/lib/narcissujsk/
cp ./agent/narcissujsk.service  /lib/systemd/system/
systemctl narcissujsk start
