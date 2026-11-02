enemy_x     = [40, 180, 300, 420]
enemy_speed = [3, 5, 2, 4]
alive = [True, True, True, True]

print("--- BEFORE ---")

for i in range(len(enemy_x)):
    print(f"Enemy {i}: x = {enemy_x[i]}, speed = {enemy_speed[i]}, alive = {alive[i]}")

enemy_x.insert(2, 999)


print("--- AFTER ---")

for i in range(len(enemy_speed)):
    print(f"enemy {i}: x = {enemy_x[i]}, speed = {enemy_speed[i]}, alive =  {alive[i]}")


