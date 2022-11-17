
import numpy as np

# Wellcome to the user

print("\nWellcome to the stuck pipe table. Programm written by Jose Ricardi in python")

# user choice

choice = input(
    '\nWould you like to know the type of mechanism stuck pipe that is in the hole? "Y" or "N"\n').lower()

print("\n")
if choice == "y":
    print("\nPlease answer the below quiz...\n")

    # Oil rig draw

    print('''
                /\ 
               /\/\ 
               |/\|
              //\/\\
              |\/\/|
             \|/\/\|   .''`/
      \''.    \`'. |  ||  /
       \ ||   |\ |||  || /
       _\||__/__\||_\_||/___
       |___________________|
        |  |   |   |   |  |
  ~~~~~~|~~|~~~|~~~|~~~|~~|~~~~~~''')

    print("\n")

    # Question 1 pior motion before sticking

    validation = ("a", "b", "c", "d", "e", "moving up", "rotating up",
                  "rotating up", "rotating down", "static", "down free", "down restricted",
                  "down impossible", "rotate free", "rotate restricted", "rotate impossible",
                  "circulation not restricted", "circulation restricted", "circulation impossible")

    table_values = ([0, 0, 0], [1, 0, 2], [0, 0, 2], [
                    0, 2, 2], [2, 0, 0], [2, 0, 2], [2, 2, 0])

    # Question 1 pior motion before sticking
    move_up = input(
        "Q-1 How was the pipe moving prior the sticking? \n (a) Moving Up \n (b) Rotating Up \n (c) Moving Down \n (d) Rotating Down \n (e) Static\n").lower()

    def q1_moving_up():
        global move_up
        while move_up not in validation:
            print("\nValueError. Please enter a valid input.\n")
            move_up = input(
                "Q-1 How was the pipe moving prior the sticking? \n (a) Moving Up \n (b) Rotating Up \n (c) Moving Down \n (d) Rotating Down \n (e) Static\n").lower()
            continue
            break
        if move_up == "a" or move_up == "moving up":
            move_up = np.array((table_values[5]))

        elif move_up == "b" or move_up == "rotating up":
            move_up = np.array(table_values[2])

        elif move_up == "c" or move_up == "moving down":
            move_up = np.array(table_values[1])

        elif move_up == "d" or move_up == "rotaing down":
            move_up = np.array(table_values[2])

        elif move_up == "e" or move_up == "static":
            move_up = np.array(table_values[6])

    q1_moving_up()
    
    # Question 2 motion after sticking
    after_up = input(
        "Q-2 How was the pipe moving after the sticking? \n (a) Down Free \n (b) Down Restricted \n (c) Down Impossible\n").lower()

    def q2_motion_after_sticking():
        global after_up
        while after_up not in validation:
            print("\nValueError. Please enter a valid input.\n")
            after_up = input(
                "Q-2 How was the pipe moving after the sticking? \n (a) Down Free \n (b) Down Restricted \n (c) Down Impossible\n").lower()
            continue
            break
        if after_up == "a" or after_up == "down free":
            after_up = np.array(table_values[2])

        elif after_up == "b" or after_up == "down restricted":
            after_up = np.array(table_values[1])

        elif after_up == "c" or after_up == "down impossible":
            after_up = np.array(table_values[0])

    q2_motion_after_sticking()
    
    # Question 3 rotation motion after sticking
    rotation = input(
        "Q-3 How was the pipe rotating after the sticking? \n (a) Rotate Free\n (b) Rotate Restricted\n (c) Rotate Impossible\n").lower()

    def q3_rotation_sticking():
        global rotation
        while rotation not in validation:
            print("\nValueError. Please enter a valid input.\n")
            rotation = input(
                "Q-3 How was the pipe rotating after the sticking? \n (a) Rotate Free\n (b) Rotate Restricted\n (c) Rotate Impossible\n").lower()
            continue
            break
        if rotation == "a" or rotation == "rotate free":
            rotation = np.array(table_values[2])

        elif rotation == "b" or rotation == "rotate restricted":
            rotation = np.array(table_values[5])

        elif rotation == "c" or rotation == "rotate impossible":
            rotation = np.array(table_values[0])

    q3_rotation_sticking()
    
    # Question 4 pressure after the sticking
    circulation = input(
        "Q-4 How was the circulating pressure after the sticking? \n (a) Circulation Not Restricted\n (b) Circulation Restricted\n (c) Circulation Impossible\n ").lower()

    def q4_circulation():
        global circulation
        while circulation not in validation:
            print("\nValueError. Please enter a valid input.\n")
            circulation = input(
                "Q-4 How was the circulating pressure after the sticking? \n (a) Circulation Not Restricted\n (b) Circulation Restricted\n (c) Circulation Impossible\n ").lower()
            continue
            break
        if circulation == "a" or circulation == "circulation not restricted":
            circulation = np.array(table_values[3])

        elif circulation == "b" or circulation == "circulation restricted":
            circulation = np.array(table_values[6])

        elif circulation == "c" or circulation == "circulation impossible":
            circulation = np.array(table_values[0])

    result_q4 = circulation
    q4_circulation()

    result = move_up + after_up + rotation + circulation

    # Checking conditions to print type of stuck pype

    if result[0] > result[1] and result[0] > result[2]:
        print(
            f'The result of the table is: {result}. The most likely possible mechanism of stuck pipe is "Pack-off / Bridge-off"\n')
    elif result[1] > result[0] and result[1] > result[2]:
        print(
            f'The result of the table is: {result}. The most likely possible mechanism of stuck pipe is "Differential Sticking"\n')
    elif result[2] > result[0] and result[2] > result[1]:
        print(
            f'The result of the table is: {result}. The most likely possible mechanism of stuck pipe is "Wellbore Geometry"\n')
else:
    print("Ok!... Thanks bye bye...\n")
