import sys
import TeamsProject

class UserInterface():
    def __init__(self):
        pass

    def mainMenu(self):
        done = False
        while done == False:
            print("""========== MAIN MENU =============
            1. Enter all new Team(s)
            2. Displaying All Teams
            3. Saving Team Records to a File
            4. Using ID Read Individual Team
            5. Read Particular Type Of Team 
            6. Update Team in a File
            7. Delete Team
            8. Total number of Teams
            9. Teams Paid Fees
            10. Apply for Cancellation of Participation
            11. Load & Display Status of Teams 
            12. Exit
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                f = 'y'       
                while(f == "y"):
                    TeamsProject.add_new_team()
                    f = input("Do you want to add more teams? Press y for yes and n for no: ") 
                    TeamsProject.Team.id_count +=1  
            elif choice == 2:
                TeamsProject.display_all_teams()
            elif choice == 3:
                TeamsProject.write_to_file()
            elif choice == 4:
                TeamsProject.display_team_based_on_id() 
            elif choice == 5:
                TeamsProject.display_team_type()
            elif choice == 6:
                TeamsProject.update_team() 
            elif choice == 7:
                TeamsProject.delete_team()
            elif choice == 8:
                TeamsProject.num_of_teams()
            elif choice == 9:
                TeamsProject.teams_paid_fee()
            elif choice == 10:
                TeamsProject.cancellation()
            elif choice == 11:
                TeamsProject.status_of_teams()
            elif choice == 12:
                done = True

obj = UserInterface()
obj.mainMenu()
