import random

def calculation(a,b):

    final_user = sum(a)
    final_machine = sum(b)
    print(f"\nyour total score : {final_user}\n"f"machine total score : {final_machine}\n")
    if final_user > final_machine:
        print(f"OH MY GOODNESS YOU WON AGAINST ME...!!!!\n""         PLAY AGAIN......")
    elif final_user == final_machine:
        print("!!!!!!!!!!!!!!!! DRAW MATCH !!!!!!!!!!!!!!! TRY AGAIN !!!!!!!!!!!!!!")
    else:
        print("I told you in the begining, you can't win against me \n""you can try once more also..........")
    return None

def score(a,b):
    print("===============================================")
    user_points = []
    machine_points = []
    points1 = 0  # user initial points
    points2 = 0  # machine initial points

    for i in range(len(a)):

        if a[i] == b[i]:

            points1 = 0  
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)

            pass
        elif a[i] == 1 and b[i] == 2: # snake wins against water --->>> points for user 
            points1 = 1
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 1 and b[i] == 3: # snake looses against gun --->>> points for machine
            points1 = 0 
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 2 and b[i] == 1: # water looses against snake --->>> points for the machine 
            points1 = 0
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 2 and b[i] == 3: # water wins against the gun --->>> points for the user 
            points1 = 0
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 3 and b[i] == 1: # gun wins against the sanake --->>> points for the user
            points1 = 1
            points2 = 0
            user_points.append(points1)
            machine_points.append(points2)
            pass
        elif a[i] == 3 and b[i] == 2: # gun looses against the water --->>> points for the machine 
            points1 = 0
            points2 = 1
            user_points.append(points1)
            machine_points.append(points2)
            pass
        print(f"user points : {user_points}\n"f"machine points : {machine_points}")
        print("###################################################################")
    calculation(user_points,machine_points) 
    return None 


def develop(series):
    print("==========================================================")
    user = []
    machine =[]
    if series != 3 and series != 5:
        print("ERROR....!!!!\n""you can choose either 3 or 5 only.....\n""Thankyou")
    elif series == 3 or 5:
        for i in range(series):
            user_action = int(input("enter the corresponding action to value :\n"" 1 = snake \n"" 2 = water \n"" 3 = gun\n"))
            user.append(user_action)
            machine_action = random.randint(1,3)
            # print(f"this is machine action {machine_action}")
            machine.append(machine_action)
            print(f"user input by till this time --->>> {user}\n"f"machine input by till this time --->>> {machine}")
    
        score(user,machine)

    return None





if __name__ == "__main__":
    print("<<<< WELCOME TO GAME>>>>\n""             BE READY TO ***LOOSE***")

    series = int(input("eneter the series you wish to play either 3 or 5 \n"))
    start = develop(series)







