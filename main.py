Tasks = []
Complete = []

def showTasks():
    while True:
        for t in Tasks:
            print(t)
        done = input("\nDone? Y or N: ")
        if done.upper() == "Y":
            break
        else:
            continue

def addTask():
    while True:
        task = input("\nEnter new task or N: ")
        if task.upper() == "N":
            break
        else:
            Tasks.append(task)
            continue


def remTask():
    while True:
        task = input("\nEnter task name for removal or N: ")
        if task.upper() == "N":
            break
        elif task in Tasks:
            Tasks.remove(task)
            continue

if __name__ == "__main__":
    print("\nTASK TRACKER")
    while True:
        print("\nOptions\n-------------")
        print("1. Current tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        option = int(input("\nEnter option: "))
        if option == 1:
            showTasks()
        elif option == 2:
            addTask()
        elif option == 3:
            remTask()
        elif option == 4:
            print("\nCome back ;(")
            break
        else:
            print("\nInvalid option")