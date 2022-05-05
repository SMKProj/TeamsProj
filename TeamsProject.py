import datetime
from os import remove

all_Teams = []

#begining of Team class
class Team:
    joining_date = datetime.date.today()
    id_count = 1
    def __init__(self, name,type, fee_paid, fee, date=joining_date , id=id_count):
        
        self.__id = Team.id_count + 1
        self.__date = date
        self.__name = name
        self.__type = type
        self.__fee_paid = fee_paid
        self.__fee = fee
        self.teams = []
          
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
    def set_date(self,date):
            self.__date = date
    
    def get_name(self):return self.__name
    def get_type(self): return self.__type
    def get_fee_paid(self):return self.__fee_paid
    def get_fee(self):return self.__fee
    def get_id(self): return self.__id
    def get_date(self): return self.__date

    
    
    def __repr__(self):
        return self.__id + self.__name  + self.__type + self.__fee_paid + self.__fee + self.__date

#end of Team class
#################################################################

        
# function to add new teams
def add_new_team():
    Team.set_id = Team.id_count
    Team.set_name = input("Enter team name :")
    Team.set_type = input("Enter team type : ")
    fee_paid = input("Enter Y/N if fee is paid? ")
    Team.set_fee_paid = fee_paid
    if fee_paid == "Y":
        Team.set_fee = float(input("Enter fee amount paid? "))
    else:
        Team.set_fee = 0.0
    Team.set_date = str(Team.joining_date)
    all_Teams.append([Team.set_id,Team.set_name, Team.set_type,Team.set_fee_paid, Team.set_fee, Team.set_date])
    
# function to display all teams
def display_all_teams():
    print("----------------------------------------------------")
    print('ID---NAME---TYPE---FEEPAID---FEE----DATE')
    for teams in all_Teams:
        print(teams)

#Function to Save Team Records to a File
def write_to_file():
    file = open("file.txt", 'w')
    for instances in all_Teams:
        file.writelines(str(instances) + "\n")
    file.close()
    print("The records has been saved to a file")
    
#Function to Display Total Number of Teams            
def num_of_teams():
    tot_teams = str(len(all_Teams))   
    print("----------------------------------------")    
    print("Total Number of Teams are: " + tot_teams) 
    
# display teams from file based on ID
def display_team_based_on_id():
    requested_id = int(input("Enter team ID to view: "))
    for row in all_Teams:
        rid = row[0]
        if requested_id == rid:
            print("-------------------------------------")
            print(row)

# Function to Display Teams using Team Type (Girls / Boys)   
def display_team_type():
    requested_type = input("Enter type of team to view: ")
    print("-------------------------------------")
    for row in all_Teams:
        rtype= row[2]
        if requested_type == rtype:
            print(row)

#Function to Delete Team Based on Given Team ID
def delete_team():
    del_team_id = int(input("Enter ID of team to delete: "))
    # deleting team from a file   
    rows= []
    for row in all_Teams:
        rid = row[0]
        if del_team_id == rid:
            all_Teams.remove(row)

        
    print("Team id: " + str(del_team_id) + " has been deleted" )    
    
    file = open("file.txt", 'w')
    for r in all_Teams:
        file.writelines(str(r) + "\n")        
    file.close()    


#Function to Calculate % of Teams Who has Paid The Fee
def teams_paid_fee():
    paid_fee_yes = []  
    for values in all_Teams:
        f = values[4]
        if f != 0.0:
            paid_fee_yes.append(f)
         
    total_rec = len(all_Teams)
    len_paid_fee_yes = len(paid_fee_yes)
    percentage = str(round((len_paid_fee_yes / total_rec) * 100))
            
    print("-----------------------------------------------------")
    print("Percentage of teams who paid the fee are: (rec_paidfee/totalrec)*100 : " + percentage + "%")


#########################################

#Function to Update Teams in a File               
def update_team():
    update_req = int(input("Enter id of team for update? "))
    print("""
                    a. Enter "Name" to update team names
                    b. Enter "Type" to update team names
                   
            """)
    update_col = input("What you want to update : ") 
    
    for values in all_Teams:
        if update_req == values[0]:
            if update_col == "Name":
                values[1] = input("Enter new name for team: ")
                print(update_col + " has been updated")
            elif update_col == "Type":
                values[2] = input("Enter new type for team: ")
                print(update_col + " has been updated")
            else:
                print("Column access is not allowed")
    
    file = open("file.txt", 'w')
    for r in all_Teams:
        file.writelines(str(r) + "\n")        
    file.close()   

#############################################
#Function to Cancel Team Participation Based on Given Team ID
def cancellation():
    team_id = int(input("Enter team ID to cancel participation: "))  
    rows = []
    cancellation_date = str(datetime.date.today())
    for values in all_Teams:
        if values[0] == team_id:
            values[1] = ""
            values[2] = "Participation"
            values[3] = "Cancelled"
            values[4] = ""
            values[5] = cancellation_date
           
    
    print("-----------------------------------------------------------")
    print("Team with ID ("+ str(team_id) + ") participation has been cancelled")   
    
    file = open("file.txt", 'w')
    for r in all_Teams:
        file.writelines(str(r) + "\n")        
    file.close()

#################################################

# Load from file.txt current status of teams
def status_of_teams():
    f = open("file.txt", 'r')
    reader = f.readlines()
    print("-------------Current Status Of Teams-----------------------------")
    print('ID-----NAME-----TYPE-----FEEPAID-----FEE-------DATE')
    for values in reader:
        print(values)
    f.close()       
