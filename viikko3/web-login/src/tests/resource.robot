*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${OHTU_URL}  http://${SERVER}/ohtu

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # seuraava rivi on kommentoitu toistaiseksi pois
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Main Page
    Go To  ${HOME_URL}

Register Page Should Be Open
    Title Should Be  Register

### Tehtävä 7.
Go To Register Page
    Go To  ${REGISTER_URL}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

### Tehtävä 8.
Go To Ohtu Page
    Go To  ${OHTU_URL}

Ohtu Page Should Be Open
    Title Should Be  Ohtu Application main page