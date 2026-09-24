devices = [
    {
        "hostname": "RTR1",
        "device_type": "Router",
        "management_ip": "192.168.1.1",
        "location": "Headquarters",
        "status": "Operational",
        "cpu_usage": 35,
        "memory_usage": 42,
        "uptime": 120,
        "backup_status": "Successful"
    },
    {
        "hostname": "RTR2",
        "device_type": "Router",
        "management_ip": "192.168.1.2",
        "location": "Branch Office",
        "status": "Operational",
        "cpu_usage": 82,
        "memory_usage": 61,
        "uptime": 45,
        "backup_status": "Successful"
    },
    {
        "hostname": "SW1",
        "device_type": "Switch",
        "management_ip": "192.168.1.10",
        "location": "Headquarters",
        "status": "Operational",
        "cpu_usage": 28,
        "memory_usage": 50,
        "uptime": 200,
        "backup_status": "Successful"
    },
    {
        "hostname": "SW2",
        "device_type": "Switch",
        "management_ip": "192.168.1.11",
        "location": "Headquarters",
        "status": "Down",
        "cpu_usage": 0,
        "memory_usage": 0,
        "uptime": 0,
        "backup_status": "Failed"
    },
    {
        "hostname": "SW3",
        "device_type": "Switch",
        "management_ip": "192.168.2.10",
        "location": "Branch Office",
        "status": "Operational",
        "cpu_usage": 40,
        "memory_usage": 88,
        "uptime": 67,
        "backup_status": "Successful"
    },
    {
        "hostname": "AP1",
        "device_type": "Access Point",
        "management_ip": "192.168.1.20",
        "location": "Headquarters",
        "status": "Operational",
        "cpu_usage": 25,
        "memory_usage": 38,
        "uptime": 90,
        "backup_status": "Successful"
    },
    {
        "hostname": "AP2",
        "device_type": "Access Point",
        "management_ip": "192.168.2.20",
        "location": "Branch Office",
        "status": "Operational",
        "cpu_usage": 55,
        "memory_usage": 62,
        "uptime": 3,
        "backup_status": "Successful"
    },
    {
        "hostname": "FW1",
        "device_type": "Firewall",
        "management_ip": "192.168.1.254",
        "location": "Headquarters",
        "status": "Operational",
        "cpu_usage": 48,
        "memory_usage": 72,
        "uptime": 150,
        "backup_status": "Failed"
    }
]
def print_device_report():
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
def print_device_type_totals():
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

def print_attention_report():
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
    

print_device_report()
print_device_type_totals()
print_attention_report()
