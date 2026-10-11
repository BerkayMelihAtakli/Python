disk_free = 51

if disk_free < 10:
    print(f"KRITIEK: {disk_free}% vrij — direct opruimen!")
elif disk_free < 20:
    print(f"LAAG: {disk_free}% vrij — ruim zo snel mogelijk op")
elif disk_free < 50:
    print(f"HALVERWEGE: {disk_free}% vrij — houd het in de gaten")
else:
    print(f"OK: {disk_free}% vrij — genoeg ruimte")

    # Waarom elif?
    # 'elif' stopt direct bij de eerste ware voorwaarde.
    # Losse 'if'-statements zouden ongewenst meerdere meldingen printen.