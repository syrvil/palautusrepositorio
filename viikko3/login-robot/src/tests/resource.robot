# Tuodaan AppLibrary.py:ssä toteutetut Test Casejen käyttämät avainsanat.
# Avainsanat ovat metdien nimiä
*** Settings ***
Library  ../AppLibrary.py 

# Alla "Input login Command" avainsanoilla kutsutaan AppLibrary.py:ssä olevaa 
# metodia input ja annetaan sille  parametriksi sana login
#
# Alla "Input Credentials" avainsanoilla kutsutaan AppLibrary.py:ssä olevaa
# metodia input ja annetaan sille parametriksi kaksi muuttujaa ${username} ja ${password}
#  
*** Keywords ***
Input Login Command
    Input  login

Input New Command
    Input  new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
