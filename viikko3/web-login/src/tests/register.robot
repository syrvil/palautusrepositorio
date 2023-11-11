# A new user account can be created if a proper unused username 
# and a proper password are given

*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
#Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Welcome Page Should Be Open    

Register With Too Short Username And Valid Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Registration Should Fail With Message  Username must have at least 3 characters

Register With Valid Username And Invalid Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Register Credentials
    Registration Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Register Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Register Credentials
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Register Page
    Register Page Should Be Open
    Set Username  kalle
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
    Go To Register Page
    Register Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Register Credentials
    Registration Should Fail With Message  Passwords do not match
    #
    Go To Login Page
    #Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Register Credentials
    Click Button  Register        

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
