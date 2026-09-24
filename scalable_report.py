import yaml


def load_devices():
    with open("devices.yaml", "r") as file:
        data = yaml.safe_load(file)

    return data["devices"]


def print_device_report(devices):
    print("\nNETWORK OPERATIONAL REPORT")
    print("==========================")

    for device in devices:
        print("\nHostname:", device["hostname"])
        print("Device Type:", device["device_type"])
        print("Management IP:", device["management_ip"])
        print("Location:", device["location"])
        print("Status:", device["status"])
        print("CPU Usage:", device["cpu_usage"], "%")
        print("Memory Usage:", device["memory_usage"], "%")
        print("Uptime:", device["uptime"], "days")
        print("Backup Status:", device["backup_status"])

def print_device_type_totals(devices):
    device_types = {}

    for device in devices:
        device_type = device["device_type"]

        if device_type in device_types:
            device_types[device_type] += 1
        else:
            device_types[device_type] = 1

    print("\nDEVICE TYPE TOTALS")
    print("==================")

    for device_type in device_types:
        print(device_type, ":", device_types[device_type])


def print_location_totals(devices):
    locations = {}

    for device in devices:
        location = device["location"]

        if location in locations:
            locations[location] += 1
        else:
            locations[location] = 1

    print("\nLOCATION TOTALS")
    print("===============")

    for location in locations:
        print(location, ":", locations[location])


def print_attention_report(devices):
    print("\nDEVICES NEEDING ATTENTION")
    print("=========================")

    for device in devices:
        issues = []

        if device["cpu_usage"] > 80:
            issues.append("High CPU")

        if device["memory_usage"] > 80:
            issues.append("High memory")

        if device["backup_status"] == "Failed":
            issues.append("Failed backup")

        if device["uptime"] < 7:
            issues.append("Low uptime")

        if device["status"] != "Operational":
            issues.append("Not operational")

        if len(issues) > 0:
            print(device["hostname"])

            for issue in issues:
                print(" -", issue)


devices = load_devices()

print_device_report(devices)
print_attention_report(devices)
