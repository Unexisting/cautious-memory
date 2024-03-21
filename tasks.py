def movement():
 path = ("move forward", 10, "move backwards", 5, "turn left", 2, "turn right", 1)
 return path


def run_task2():
    print("Moving...")
    local_var = movement()
    for pt in range(0, len(local_var) ,2):
     print(f"{local_var[pt]} for {local_var[pt+1]} step")


run_task2()