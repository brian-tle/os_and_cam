# For getting HW / Sys info
import psutil, platform
from datetime import datetime

import os.path
from os import path

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def getSysInfo():
	get_time = datetime.now()
	timestamp = get_time.strftime("%B %d, %Y :: %H:%M:%S")

	dumbstring = "=" * 50
	shortstring = "=" * 10
	try:
		if (path.exists("sys_log32.txt")):
			with open("sys_log32.txt", "a") as f:
				print("Writing to log...")
				f.write(timestamp)
				f.write("\n\n" + shortstring + " System Information " + shortstring)
				uname = platform.uname()
				f.write(f"\nSystem: {uname.system}")
				f.write(f"\nNode Name: {uname.node}")
				f.write(f"\nRelease: {uname.release}")
				f.write(f"\nVersion: {uname.version}")
				f.write(f"\nMachine: {uname.machine}")
				f.write(f"\nProcessor: {uname.processor}")

				# Boot Time
				f.write("\n\n" + shortstring + " Boot Time " + shortstring)
				boot_time_timestamp = psutil.boot_time()
				bt = datetime.fromtimestamp(boot_time_timestamp)
				f.write(f"\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

				f.write("\n\n" + shortstring + " CPU Info " + shortstring)
				# number of cores
				f.write("\nPhysical cores:" + str(psutil.cpu_count(logical=False)))
				f.write("\nTotal cores:" + str(psutil.cpu_count(logical=True)))
				# CPU frequencies
				cpufreq = psutil.cpu_freq()
				f.write(f"\nMax Frequency: {cpufreq.max:.2f}Mhz")
				f.write(f"\nMin Frequency: {cpufreq.min:.2f}Mhz")
				f.write(f"\nCurrent Frequency: {cpufreq.current:.2f}Mhz")
				# CPU usage
				f.write("\nCPU Usage Per Core:")
				for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
				    f.write(f"\nCore {i}: {percentage}%")
				f.write(f"\nTotal CPU Usage: {psutil.cpu_percent()}%")

				# Memory Information
				f.write("\n\n" + shortstring + " Memory Information " + shortstring)
				# get the memory details
				svmem = psutil.virtual_memory()
				f.write(f"\nTotal: {get_size(svmem.total)}")
				f.write(f"\nAvailable: {get_size(svmem.available)}")
				f.write(f"\nUsed: {get_size(svmem.used)}")
				f.write(f"\nPercentage: {svmem.percent}%")

				f.write("\n\n" + shortstring + "SWAP " + shortstring)
				# get the swap memory details (if exists)
				swap = psutil.swap_memory()
				f.write(f"\nTotal: {get_size(swap.total)}")
				f.write(f"\nFree: {get_size(swap.free)}")
				f.write(f"\nUsed: {get_size(swap.used)}")
				f.write(f"\nPercentage: {swap.percent}%")

				# Disk Information
				f.write("\n\n" + shortstring + " Disk Information " + shortstring)
				f.write("\nPartitions and Usage:")
				# get all disk partitions
				partitions = psutil.disk_partitions()
				for partition in partitions:
				    f.write(f"\n=== Device: {partition.device} ===")
				    f.write(f"\n  Mountpoint: {partition.mountpoint}")
				    f.write(f"\n  File system type: {partition.fstype}")
				    try:
				        partition_usage = psutil.disk_usage(partition.mountpoint)
				    except PermissionError:
				        # this can be catched due to the disk that
				        # isn't ready
				        continue
				    f.write(f"\n  Total Size: {get_size(partition_usage.total)}")
				    f.write(f"\n  Used: {get_size(partition_usage.used)}")
				    f.write(f"\n  Free: {get_size(partition_usage.free)}")
				    f.write(f"\n  Percentage: {partition_usage.percent}%")
				# get IO statistics since boot
				disk_io = psutil.disk_io_counters()
				f.write(f"\nTotal read: {get_size(disk_io.read_bytes)}")
				f.write(f"\nTotal write: {get_size(disk_io.write_bytes)}")

				# Network information
				f.write("\n\n" + shortstring + " Network Information " + shortstring)
				# get all network interfaces (virtual and physical)
				if_addrs = psutil.net_if_addrs()
				for interface_name, interface_addresses in if_addrs.items():
				    for address in interface_addresses:
				        f.write(f"\n=== Interface: {interface_name} ===")
				        if str(address.family) == 'AddressFamily.AF_INET':
				            f.write(f"\n  IP Address: {address.address}")
				            f.write(f"\n  Netmask: {address.netmask}")
				            f.write(f"\n  Broadcast IP: {address.broadcast}")
				        elif str(address.family) == 'AddressFamily.AF_PACKET':
				            f.write(f"\n  MAC Address: {address.address}")
				            f.write(f"\n  Netmask: {address.netmask}")
				            f.write(f"\n  Broadcast MAC: {address.broadcast}")
				# get IO statistics since boot
				net_io = psutil.net_io_counters()
				f.write(f"\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}")
				f.write(f"\nTotal Bytes Received: {get_size(net_io.bytes_recv)}")
				f.write("\n\n" + dumbstring + "\n\n")
		else:
			with open("sys_log32.txt", "w") as f:
				print("Creating new log...")
				f.write(timestamp)
				f.write("\n\n" + shortstring + " System Information " + shortstring)
				uname = platform.uname()
				f.write(f"\nSystem: {uname.system}")
				f.write(f"\nNode Name: {uname.node}")
				f.write(f"\nRelease: {uname.release}")
				f.write(f"\nVersion: {uname.version}")
				f.write(f"\nMachine: {uname.machine}")
				f.write(f"\nProcessor: {uname.processor}")

				f.write("\n\n" + shortstring + " Boot Time " + shortstring)
				boot_time_timestamp = psutil.boot_time()
				bt = datetime.fromtimestamp(boot_time_timestamp)
				f.write(f"\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

				f.write("\n\n" + shortstring + " CPU Info " + shortstring)
				f.write("\nPhysical cores:" + str(psutil.cpu_count(logical=False)))
				f.write("\nTotal cores:" + str(psutil.cpu_count(logical=True)))
				cpufreq = psutil.cpu_freq()
				f.write(f"\nMax Frequency: {cpufreq.max:.2f}Mhz")
				f.write(f"\nMin Frequency: {cpufreq.min:.2f}Mhz")
				f.write(f"\nCurrent Frequency: {cpufreq.current:.2f}Mhz")
				f.write("\nCPU Usage Per Core:")
				for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
				    f.write(f"\nCore {i}: {percentage}%")
				f.write(f"\nTotal CPU Usage: {psutil.cpu_percent()}%")

				f.write("\n\n" + shortstring + " Memory Information " + shortstring)
				svmem = psutil.virtual_memory()
				f.write(f"\nTotal: {get_size(svmem.total)}")
				f.write(f"\nAvailable: {get_size(svmem.available)}")
				f.write(f"\nUsed: {get_size(svmem.used)}")
				f.write(f"\nPercentage: {svmem.percent}%")

				f.write("\n\n" + shortstring + "SWAP " + shortstring)
				swap = psutil.swap_memory()
				f.write(f"\nTotal: {get_size(swap.total)}")
				f.write(f"\nFree: {get_size(swap.free)}")
				f.write(f"\nUsed: {get_size(swap.used)}")
				f.write(f"\nPercentage: {swap.percent}%")

				f.write("\n\n" + shortstring + " Disk Information " + shortstring)
				f.write("\nPartitions and Usage:")
				partitions = psutil.disk_partitions()
				for partition in partitions:
				    f.write(f"\n=== Device: {partition.device} ===")
				    f.write(f"\n  Mountpoint: {partition.mountpoint}")
				    f.write(f"\n  File system type: {partition.fstype}")
				    try:
				        partition_usage = psutil.disk_usage(partition.mountpoint)
				    except PermissionError:
				        continue
				    f.write(f"\n  Total Size: {get_size(partition_usage.total)}")
				    f.write(f"\n  Used: {get_size(partition_usage.used)}")
				    f.write(f"\n  Free: {get_size(partition_usage.free)}")
				    f.write(f"\n  Percentage: {partition_usage.percent}%")
				disk_io = psutil.disk_io_counters()
				f.write(f"\nTotal read: {get_size(disk_io.read_bytes)}")
				f.write(f"\nTotal write: {get_size(disk_io.write_bytes)}")

				f.write("\n\n" + shortstring + " Network Information " + shortstring)
				if_addrs = psutil.net_if_addrs()
				for interface_name, interface_addresses in if_addrs.items():
				    for address in interface_addresses:
				        f.write(f"\n=== Interface: {interface_name} ===")
				        if str(address.family) == 'AddressFamily.AF_INET':
				            f.write(f"\n  IP Address: {address.address}")
				            f.write(f"\n  Netmask: {address.netmask}")
				            f.write(f"\n  Broadcast IP: {address.broadcast}")
				        elif str(address.family) == 'AddressFamily.AF_PACKET':
				            f.write(f"\n  MAC Address: {address.address}")
				            f.write(f"\n  Netmask: {address.netmask}")
				            f.write(f"\n  Broadcast MAC: {address.broadcast}")
				net_io = psutil.net_io_counters()
				f.write(f"\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}")
				f.write(f"\nTotal Bytes Received: {get_size(net_io.bytes_recv)}")
				f.write("\n\n" + dumbstring + "\n\n")
	except Exception as e:
		print("SysInfo Creation error: " + str(e))