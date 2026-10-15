disk_free = 21
cpu_load  = 99

# TODO: gebruik chained comparison voor safe_to_backup
safe_to_backup = 20 <= disk_free <= 100 and 0 <= cpu_load <= 100


# TODO: gebruik ternary om de status te omschrijven
status = "veilig" if safe_to_backup else "onveilig"

# TODO: schrijf in één f-string: vrije ruimte %, cpu %, status
print(f"Vrije schrijfruimte: {disk_free}, cpu_load: {cpu_load}, status: {status}")