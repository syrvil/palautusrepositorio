*** Settings ***
Resource  resource.robot
Resource  login_resource.robot 
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page and Page Should Be Open

*** Test Cases ***
Register With Valid Username And Password
    Set Username  valle
    Set Password  valle123
    Set Password Confirmation  valle123
    Submit Register Credentials
    Register Should Succeed 

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Registration Should Fail With Message  Username must have at least 3 characters

Register With Valid Username And Invalid Password
    Set Username  nalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Register Credentials
    Registration Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Register Credentials
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  kille
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Welcome Page Should Be Open    
    Go To Ohtu Page
    Ohtu Page Should Be Open
    Click Button  Logout 
    #
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  pelle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Register Credentials
    Registration Should Fail With Message  Passwords do not match
    #
    Go To Login Page
    #Login Page Should Be Open
    Set Username  pelle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password