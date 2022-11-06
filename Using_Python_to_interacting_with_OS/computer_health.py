#!/usr/bin/env python3
import shutil
import psutil

def check_disk(disk):
	du = shutil.disk_usage(disk)
	free = (du.free / du.total) * 100
	return free > 20
def check_cpu():
	a = psutil.cpu_percent(1)
	return a < 70

if not check_cpu() or not check_disk("/"):
	print("Too much load and not enough space..")
else:
	print("Working fine..")