def start_backup():
    print("Backup gestart...")

disk_free = None   # test ook met: 0, 15, 80

# Guard 1: is er een meting?
if disk_free is None:
    print("Geen meting beschikbaar")
    exit()

# Guard 2: schijf helemaal vol?
if disk_free == 0:
    print("Schijf helemaal vol")
    exit()

# Guard 3: te weinig ruimte? (Bijvoorbeeld onder de 20%)
if disk_free < 20:
    print(f"Te weinig ruimte: {disk_free}%")
    exit()

print(f"Ruimte OK: {disk_free}%")
start_backup()