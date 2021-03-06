#Web Search
#Developed by              : PythonCoder8
#Requires Pip installation : pip install google
#Description               : Search web for query and retrieve a selected amount of URLs
#Only tested with Python version 3.8.5. May not work on Python version 3.8 or under

#########################################################################################

try:
    from time import time
    from googlesearch import search
    import sys
    import webbrowser

    #Print title using variables and delete after using variables to clear up RAM
    width = 40
    titletxt = 'Web-Search'
    title = titletxt.center(width)
    print(title)
    del width
    del titletxt
    del title

    search_query = input('\nWhat do you want to search for on the web?: ')
    result_num = input('How many results do you want to retrieve from the web?: ')

    #Verify user input
    try:
        int_result_num = int(result_num)
    except:
        sys.exit('The number of results you wanted to retrieve was not a number. Exiting program...')

    #Display web results
    print('The top %d results from the web are:' %(int_result_num))

    start = time()
    for url in search(search_query, tld='com', stop=int_result_num):
        print(url + " - %s" %(url.split('/')[2]))
    end = time()

    print('Found %d results from the web in %s' %(int_result_num, end - start) + ' seconds.')

    #Delete time variables to clear RAM
    del start
    del end

    #Ask user if they want to open the links in the web browser with validation
    open_in_browser = input('Do you want to open the given URLs in your web browser (Y/N)? ')

    if open_in_browser.upper() == 'Y':
        for url in search(search_query, tld='com', stop=int_result_num):
            webbrowser.open(url)

    elif open_in_browser.upper() == 'N':
        sys.exit('Ok! Bye!')

    else:
        while open_in_browser.upper() != 'Y' and open_in_browser.upper() != 'N':
            open_in_browser = input('Invalid response! Do you want to open the given URLs in your web browser (Y/N)? ')

            if open_in_browser.upper() == 'Y':
                for url in search(search_query, tld='com', stop=int_result_num):
                    webbrowser.open(url)

            elif open_in_browser.upper() == 'N':
                sys.exit('Ok! Bye!')
except:
    print("Something went wrong.")
