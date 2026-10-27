disk_free = float(input("Disk free percentage: "))
consumption_per_hour = float(input("Consumption per hour: "))


total_hours = disk_free / consumption_per_hour

# Normale deling (/) geeft een kommagetal (zoals 12.3), terwijl // (floor division) alleen het hele getal overhoudt (12)


total_minutes = total_hours * 60


hours = total_minutes / 60
minutes = total_minutes % 60


print(f"web01 | disk free  {disk_free}% |  log time {hours}h {minutes}min")