free_str = input("Vrije ruimte (%): ")   # bijv. "5" of "85"

# Fix: cast de invoer naar een int() voor een numerieke vergelijking
if int(free_str) > 20:
    print("Genoeg ruimte, backup starten!")
else:
    print("Te weinig ruimte")