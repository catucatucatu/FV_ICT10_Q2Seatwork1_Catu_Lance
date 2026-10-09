from pyscript import document,display

def checkname(e):
    document.getElementById('output').innerHTML = "" # clears the previous
    fname = document.getElementById('first').value.strip() # get value of first name and strips spaces
    lname = document.getElementById('last').value.strip() # get value of last name and strips spaces
    fullname = f"{fname} {lname}" # combines the two
    clubmembers = ['Alfred Cases', 'Lance Catu', 'Maiselle Marin', 'Sabine Agacita', 'Edrian Correa', 'Zeeke Fernandez'] # people in the club
    check_status = fullname in clubmembers # checks if they are in the club
    checkagain = int(check_status) # true = 1 false = 0
    messages = ((f"Sorry {fullname}, your name is not on the list."), (f"Congratulations {fullname}! You are part of the Dance Club!")) # tuple messages
    result = messages[checkagain] # check again can be index 0 or 1
    display(result, target='output1') # displays by index of the tuple
