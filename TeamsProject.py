import datetime
import csv

all_Teams = []
class Team:
    joining_date = datetime.date.today()
    id_count = 0
    def __init__(self, name:str,type:str, fee_paid:bool, fee:float, participation:str, date=joining_date , id=id_count):
        
        self.__id = Team.id_count + 1
        self.__date = date
        self.__name = name
        self.__type = type
        self.__participation = participation
        self.__fee_paid = fee_paid
        self.__fee = fee
        
        
    def set_id(self,id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_type(self,type):
        self.__type = type
    def set_fee_paid(self,fee_paid):
        self.__fee_paid = fee_paid
    def set_fee(self,fee):
        self.__fee = fee
    def set_participation(self,participation):
        self.__participation = participation
    def set_date(self,date):
            self.__date = date
    
    def get_name(self):return self.__name
    def get_type(self): return self.__type
    def get_fee_paid(self):return self.__fee_paid
    def get_fee(self):return self.__fee
    def get_id(self): return self.__id
    def get_date(self): return self.__date
    def get_participation(self): return self.__participation
    
    def __str__(self):
        Team.write_to_file(self)
        return f"{self.__id}, {self.__name}, {self.__type}, {self.__fee_paid}, {self.__fee}, {self.__participation},{self.__date} \n"
    
    def write_to_file(self):
        file = open("file.txt", 'a')
        file.write(f"{self.__id}, {self.__name}, {self.__type}, {self.__fee_paid}, {self.__fee}, {self.__participation}, {self.__date} \n")
        
    
    
    # A function to create instances of a Team class and saving objects in all_Teams
    @classmethod
    def add_new_team(cls):
        name = input("Enter Team Name: ")
        type = input("Enter Team Type: ")
        fee_paid = bool(input("If Fee is Paid? "))
        fee = float(input("Enter amount of Fee Paid: "))
        participate = bool(input("Team is participating? "))
        team_obj = Team(name,type,fee_paid, fee, participate)
        all_Teams.append(team_obj)
    
    
    # A function to display all teams    
    def display_all_teams():
        print("----------------------------------------------------")
        print('ID--NAME---TYPE---FEEPAID---FEE---PARTICIPATE---DATE')
        for index in all_Teams:
            print(index)
    
    # Function to Display Teams using Team ID value
    def read_team_based_on_id():
        requested_id = input("Enter team ID to view: ")  
        rows = []
        f = open("file.txt", 'r')
        reader = f.readlines()
        for row in reader:
            rows.append(row)
            
        for r in rows:
            if requested_id in r[0]:
                print(r)
            
    # Function to Display Teams using Team Type (Girls / Boys)   
    def read_team_type():
        requested_type = input("Enter type of team to view: ")
        rows = []
        f = open("file.txt", 'r')
        reader = f.readlines()
        for row in reader:
            rows.append(row)
            
        print(len(rows))    
        for r in rows:
            if requested_type in r:
                print(r)
    
    #Function to Display Total Number of Teams            
    def num_of_teams():
        rows = []
        f = open("file.txt", 'r')
        reader = f.readlines()
        for row in reader:
            rows.append(row)
            
        print(len(rows)) 
    
    #Function to Update Teams               
    def update_team():
        update_req = input("Enter id of team for update? ")
        update_col = input("What you want to update : ") 
        rows = []
        
        f = open("file.txt", 'r')
        reader = f.readlines()
        for values in reader:
            words = values.split(', ')
            if update_req == words[0]:
                if update_col == "Name":
                    new_name = input("Enter new team name: ")
                    words[1] = new_name
                elif update_col == "Type":
                    new_type = input("Enter new team type: ")
                    words[2] = new_type
                elif update_col == "Fee-Paid":
                    new_fee = input("Enter if fee is paid?  ")
                    words[3] = new_fee
                elif update_col == "Fee":
                    new_type = input("Enter amount of fee: ")
                    words[4] = new_type
                else:
                    print("Column access is not allowed")
                updated_rec = ", ".join(words)
                rows.append(updated_rec)
            else:
                rows.append(values)
        print(rows)
        f.close()
        
        file = open("file.txt", 'w')
        for r in rows:
            file.writelines(r)        
        file.close()
    
    #Function to Delete Team Based on Given Team ID
    def delete_team():
        del_tem_id = input("Enter ID of team to delete: ")
        rows= []
        f = open("file.txt", 'r')
        reader = f.readlines()
        print(reader)
        for values in reader:
            words = values.split(', ')
            if del_tem_id == words[0]:
                del values
            else:
                rows.append(values)
        print(rows)
        f.close()
        
        file = open("file.txt", 'w')
        for r in rows:
            file.writelines(r)        
        file.close()
            
    
    #Function to Calculate % of Teams Who has Paid The Fee
    def teams_paid_fee():
        paid_fee_yes = []       
        
        f = open("file.txt", 'r')
        reader = f.readlines()
        for values in reader:
            words = values.split(', ')
            print(words[3])
            if words[3] == "True":
                rec = ", ".join(words)
                paid_fee_yes.append(rec)
        
        total_rec = len(reader)
        len_paid_fee_yes = len(paid_fee_yes)
        percentage = (len_paid_fee_yes / total_rec) * 100
        
        print("-----------------------------------------------------")
        print("Percentage of teams paid the fee are: ", round(percentage))
            
    #Function to Cancel Team Participation Based on Given Team ID
    def cancellation():
        team_id = input("Enter team ID to cancel participation: ")  
        rows = []
        f = open("file.txt", 'r')
        reader = f.readlines()
        for values in reader:
            words = values.split(', ')
            if team_id == words[0]:
                words[1] = " "
                words[2] = " "
                words[3] = " "
                words[4] = " "
                words[5] = "Cancel"
                
                update = ", ".join(words)
                rows.append(update)
                
            else:
                rows.append(values)
        
        print(rows)
        f.close()
        
        file = open("file.txt", 'w')
        for r in rows:
            file.writelines(r)        
        file.close()
                 
                       
def main():
    done = False
    while done == False:
        print("""====== MAIN MENU ======
            1. Add New Team
            2. Saving and Displaying All Teams
            3. Using ID Read Individual Team
            4. Read Particular Type Of Team 
            5. Update Team
            6. Delete Team
            7. Total number of Teams
            8. Teams Paid Fees
            9. Apply for Cancellation of Participation
            10. Exit
            """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            f = 'y'       
            while(f == "y"):
                Team.add_new_team() 
                f = input("Do you want to add more teams? Press y for yes and n for no: ") 
                Team.id_count +=1  
        elif choice == 2:
            Team.display_all_teams()
        elif choice == 3:
            Team.read_team_based_on_id() 
        elif choice == 4:
            Team.read_team_type()
        elif choice == 5:
            Team.update_team() 
        elif choice == 6:
            Team.delete_team()
        elif choice == 7:
            Team.num_of_teams()
        elif choice == 8:
            Team.teams_paid_fee()
        elif choice == 9:
            Team.cancellation()
        elif choice == 10:
            exit()

main()

    
    
    