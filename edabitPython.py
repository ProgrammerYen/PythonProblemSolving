from datetime import date

today = date.today()
dateFormatted = today.strftime("%B %d")

def normalize(sentence):
    if dateFormatted != "October 22":
        print(str(sentence).capitalize() + "!")
        
    else:
        print(str(sentence).upper())
    
normalize("Hello There")
    
                     