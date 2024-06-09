import json


def generateSchedule():
    with open("lineage-build-targets", "r") as f:
        buildTargetFile = f.read()

    targets = []
    for line in buildTargetFile.split("\n"):
        if not line or line.startswith("#"):
            continue

        device, branch = line.split()
        target = {}
        target["device"] = device
        target["branch"] = branch
        targets.append(target)

    schedule = []
    for i in range(14):
        schedule.append([])

    i = 0
    for device in targets:
        schedule[i].append(device)
        i += 1
        if i == 14:
            i = 0

    with open("schedule.json", "w") as f:
        json.dump(schedule, f)


if __name__ == "__main__":
    generateSchedule()
