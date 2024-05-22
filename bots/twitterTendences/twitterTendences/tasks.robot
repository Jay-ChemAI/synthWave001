# Bot for extract most recent tendences in global twitter
*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Process
Library           json
Library           BuiltIn
Library           special.py
*** Variables ***
${URL}                    https://getdaytrends.com/es/
${BROWSER}                CHROME
${CHROME_DRIVER_PATH}     ${CURDIR}${/}lib/chromedriver-win64/chromedriver.exe

*** Test Cases ***
Start
    ${result}=    Enter the page and scrapt tendences

***Keywords***
Enter the page and scrapt tendences
    ${new_folder}    Set Variable    dataset
    Create Directory    ${new_folder}
    ${DOWNLOAD_DIR}    Set Variable    ${CURDIR}${/}${new_folder}
    Set Environment Variable    webdriver.chrome.driver    ${CHROME_DRIVER_PATH}
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --headless
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    ${prefs}=    Create Dictionary    download.default_directory    ${DOWNLOAD_DIR}
    Call Method    ${chrome_options}    add_experimental_option    prefs    ${prefs}
    Create Webdriver    Chrome    options=${chrome_options}
    Go To    ${URL}
    Sleep   4
   # ${DOWNLOAD_DIR}    Set Variable    ${CURDIR}${/}dataset
    ${all_text}=    Set Variable    ${EMPTY}
    FOR    ${i}    IN RANGE    1    11
        ${text}=    Get Text    xpath=(//td[@class='main']//a)[${i}]
        ${json_text}=    Convert To Json    ${i}    ${text}
        ${all_text}=    Catenate    ${all_text}    ${json_text}\n
    END
    Create File    ${CURDIR}${/}tendences.txt    ${all_text}
    Close Browser
