*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User    
    Create User  kalle  kalle123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  kalle123
    Output Should Contain  New user registered
    
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password 
    Input Credentials  ka  kalle123
    Output Should Contain  Username must have at least 3 characters

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  Kalle  kalle123
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  ka
    Output Should Contain  Password must have at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password cannot contain olnly letters
    