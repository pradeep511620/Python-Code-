import psutil


def get_disk_usage():
    partitions = psutil.disk_partitions()

    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"Mountpoint: {partition.mountpoint}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"Total: {usage.total / (1024 ** 3):.2f} GB")
        print(f"Used: {usage.used / (1024 ** 3):.2f} GB")
        print(f"Free: {usage.free / (1024 ** 3):.2f} GB")
        print(f"Percentage Used: {usage.percent}%")
        print()


if __name__ == "__main__":
    get_disk_usage()
