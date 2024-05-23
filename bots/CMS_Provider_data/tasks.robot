# Bot for downloading database from CMS website
*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Process
Library           json
Library           BuiltIn

*** Variables ***
${URL}                    https://data.cms.gov/provider-data/dataset/6jpm-sxkc
${BROWSER}                CHROME
${CHROME_DRIVER_PATH}     ${CURDIR}${/}lib/chromedriver-win64/chromedriver.exe

*** Test Cases ***
Start the download
    ${result}=    Download Full Dataset and Capture Result
    ${pythonresult}=    Python
***Keywords***
Download Full Dataset and Capture Result
    ${result}=    Run Keyword And Return Status    Download Full Dataset
    [Return]    ${result}

Download Full Dataset
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
    Sleep   2
    Click Element      xpath= (//span[text()='Download full dataset ('])[1]
    Sleep   2
    Click Element      xpath= //*[@id="dialog--9"]/div[1]/main[1]/div[2]/div[1]/button[1]
    Sleep   2
    Close Browser
Python
    ${file}    Set Variable    ${CURDIR}${/}newcsv.py
    ${py}    Run Process    python    ${file}
