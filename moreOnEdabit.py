import datetime
import calendar

date = datetime.date.today().month
year = datetime.date.today().year

def wash_hands(N, nM):
    if date % 2 == 1 and date != 8 and calendar.isleap(year) == False and date != 2:
        print(str(int(N)*21*int(nM)*31/60) + " minutes")
 
    elif date % 2 == 0 and calendar.isleap(year) == False and date != 2:
        print(str((N)*21*int(nM)*30/60) + " minutes")
        
    elif calendar.isleap(year) == False and date == 2:
        print(str(int(N)*21*int(nM)*28/60) + " minutes")
        
    elif calendar.isleap(year) == True and date == 2:
        print(str(int(N)*21*int(nM)*29/60) + " minutes")
    
wash_hands(8,7)
        
        


        
        
     
    
        