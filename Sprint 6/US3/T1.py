enemy_x     = [40, 180, 300, 420]
enemy_speed = [3, 5, 2, 4]
alive = [True, True, True, True]

alive[0] = False

enemy_x.insert(2, 999)




print(f"x - {enemy_x}), speed - {enemy_speed}, alive - {alive}")

print(enemy_x[1])