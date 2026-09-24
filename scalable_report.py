import yaml


def load_devices():
    with open("devices.yaml", "r") as file:
        data = yaml.safe_load(file)

    return data["devices"]


def print_device_report(devices):
    print("\nNETWORK OPERATIONAL REPORT")
    print("==========================")

    for device in devices:
        print(
            device["hostname"],
            "|",
            device["device_type"],
            "|",
            device["management_ip"],
            "|",
            device["location"],
            "|",
            device["status"]
        )


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
