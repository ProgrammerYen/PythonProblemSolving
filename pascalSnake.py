import re
def to_underscore(string):
    # your code here
    try:
        int(string)
        return str(string)
    
    except:
        return "_".join([i.lower() for i in re.findall('[A-Z][a-z]*[0-9]*', string)])