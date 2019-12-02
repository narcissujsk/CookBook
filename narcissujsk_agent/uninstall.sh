#!/bin/sh
service narcissujsk stop
rm -f /usr/local/lib/narcissujsk/daemon.py
rm -f /usr/local/lib/narcissujsk/run.sh
rm -f /usr/local/lib/narcissujsk/stop.sh
rm -f /lib/systemd/system/narcissujsk.service
