import re

def overs_left(total_overs,overs_left):
    no_of_balls_of_total_overs=(int(str(total_overs).split('.')[0])*6)+int(str(total_overs).split('.')[1])
    no_of_balls_of_overs_left=(int(str(overs_left).split('.')[0])*6)+int(str(overs_left).split('.')[1])
    remaining_balls_left=no_of_balls_of_total_overs-no_of_balls_of_overs_left
    remaining_overs_left=float(str(remaining_balls_left//6)+'.'+str(remaining_balls_left%6))
    return remaining_overs_left

Team1=input('Enter the first batting team name : ')
Team2=input('Enter the second batting team name : ')

first_innings=input('\nIs the first innings completed (Yes/No) : ')

try:
    if re.search('No',first_innings,re.IGNORECASE):
        Total_Overs=float(input('\nTotal number of overs : '))
        Overs_Played=float(input('Number of overs played till now : '))
        Runs_Scored=int(input('Runs scored till now : '))
        if Overs_Played<=Total_Overs:
            Current_Run_Rate=Runs_Scored/Overs_Played
            print('\n{}\'s Current Run Rate : {}\n'.format(Team1,'%.2f' % Current_Run_Rate))
            remaining_overs=overs_left(Total_Overs,Overs_Played)

            if ((Overs_Played / Total_Overs) * 100)>=20 and remaining_overs>=2:
                print('Projected Score at Current Run Rate ({}): {}'.format('%.2f' % Current_Run_Rate,int(Runs_Scored+(Current_Run_Rate*remaining_overs))))
                print('Projected Score at {} rpo : {}'.format('%.2f' % (int(Current_Run_Rate)+1),
                                                              int(Runs_Scored + ((int(Current_Run_Rate)+1) * remaining_overs))))
                print('Projected Score at {} rpo : {}'.format('%.2f' % (int(Current_Run_Rate)+3),
                                                              int(Runs_Scored + ((int(Current_Run_Rate)+3) * remaining_overs))))
                print('Projected Score at {} rpo : {}'.format('%.2f' % (int(Current_Run_Rate)+5),
                                                              int(Runs_Scored + ((int(Current_Run_Rate)+5) * remaining_overs))))
        else:
            print('Overs played is exceeding the total overs limit....Try Again')

    elif re.search('Yes',first_innings,re.IGNORECASE):
        target=int(input('What is the target for {} : '.format(Team2)))
        Total_Overs=float(input('Total number of overs : '))
        Required_Run_Rate=target/Total_Overs
        print('Required Run rate per over for {} : {}\n'.format(Team2,'%.2f' % Required_Run_Rate))

        second_innings=input('Is the second innings started (Yes/No) : ')

        if re.search('Yes', second_innings, re.IGNORECASE):
            Overs_Played = float(input('Number of overs played till now : '))
            Runs_Scored = int(input('Runs scored till now : '))
            if Overs_Played <= Total_Overs:
                Current_Run_Rate=Runs_Scored/Overs_Played
                print('\n{}\'s Current Run Rate : {}'.format(Team2, '%.2f' % Current_Run_Rate))
                remaining_overs = overs_left(Total_Overs, Overs_Played)
                Required_Run_Rate = (target-Runs_Scored) / remaining_overs
                print('Required Run rate per over for {} to chase the target : {}\n'.format(Team2, '%.2f' % Required_Run_Rate))
                print('Lets get this done')
            else:
                print('Overs played is exceeding the total overs limit....Try Again')
        elif re.search('No', second_innings, re.IGNORECASE):
            print('\nLet the chase begin!!!')
        else:
            print('Invalid Input...Please Enter Either Yes/No')
    else:
        print('Invalid Input....Please Enter Either Yes/No')

except ValueError:
    print('\nPlease provide a valid value')

finally:
    print('\nProgram Ends...Bye!!!')