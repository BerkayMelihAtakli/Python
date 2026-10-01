disk_free = 20
if disk_free > 20:
     print("Schijfruimte goed: meer dan 20% vrij")


if disk_free < 20:
    print ("Waarschuwing: minder dan 20% schijfruimte vrij")


if disk_free >= 20:
    print("Schijfruimte voldoende: 20% of meer vrij")


if disk_free <= 20:
    print("Let op: 20% of minder schijfruimte vrij")

if disk_free == 20:
    print("Status: Er is exact 20% schijfruimte vrij")


if disk_free != 20:
    print(f"Schijfruimte wijkt af van 20% (huidig: {disk_free}%)")
