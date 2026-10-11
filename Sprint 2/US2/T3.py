disk_free = 55
cpu_load  = 70

# TODO: gebruik chained comparison voor safe_to_backup
safe_to_backup = ???   # 20 <= disk_free < 100 AND 0 <= cpu_load < 80

# TODO: gebruik ternary om de status te omschrijven
status = ???   # "veilig" als safe_to_backup, anders "onveilig"

# TODO: schrijf in één f-string: vrije ruimte %, cpu %, status
print(f???)