# Tuodaan resource.robot tiedosto, jossa on kaikki tarvittavat kirjastot ja muuttujat
# Test Setup -kohdassa määritellään avainsant, joka suoritetaan ennen jokaista testiä
# -> määrittety *** Keywords *** -kohdassa

*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

# Create User on toteutettu AppLibary.py tiedostossa
# Input Login Command on toteutettu resource.robot tiedostossa kohda
# *** Keywords ***

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  kalle1234
    Output Should Contain  Invalid username or password
    
Login With Nonexistent Username
    Input Credentials  kalle2  kalle123
    Output Should Contain  Invalid username or password