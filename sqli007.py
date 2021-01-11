
try:
    from search_engines import Bing
    import requests
    from bs4 import BeautifulSoup
    from termcolor import colored
except:
    print("Please Try :python3 setup.py install;pip3 install -r requirements.txt or Try :python3 setup.py install;pip install -r requirements.txt")
# to search
errors = {
    # MySQL
    "you have an error in your sql syntax;",
    "warning: mysql",
    "mysqli_fetch_array()",
    # SQL Server
    "unclosed quotation mark after the character string",
    # Oracle
    "quoted string not properly terminated",
}

oss = "1234567890"
print("\n")
print(colored(" /$$$$$$$$/$$/$$$$$$$         /$$                        ", 'green'))
print(colored("| $$_____| $| $$__  $$       | $$                        ", 'green'))
print(colored("| $$     | $| $$  \ $$/$$$$$$| $$   /$$ /$$$$$$  /$$$$$$ ", 'green'))
print(colored("| $$$$$  | $| $$$$$$$/$$__  $| $$  /$$//$$__  $$/$$__  $ ", 'green'))
print(colored("| $$__/  | $| $$____| $$  \ $| $$$$$$/| $$$$$$$| $$  \__ ", 'green'))
print(colored("| $$     | $| $$    | $$  | $| $$_  $$| $$_____| $$      ", 'green'))
print(colored("| $$$$$$$| $| $$    |  $$$$$$| $$ \  $|  $$$$$$| $$      ", 'green'))
print(colored("|________|__|__/     \______/|__/  \__/\_______|__/      ", 'green'))
print(colored("                                                                                    ", 'green'))
print(colored("                                                                                    ", 'green'))
print(colored("                                                                                    ", 'green'))
print(colored("Warning :I made this tool to help you Pentest your website,I Am Not Responsible of any Illegal Use", 'red'))
print("\n")
print(colored("My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ", 'blue'))
print(colored("My Github : https://github.com/thepokar", 'blue'))
print(colored("To Extract Websites on The Same Server : https://hackertarget.com/reverse-ip-lookup/", 'blue'))
print("\n")
print(colored("-----------------------------------------------------------------", 'yellow'))

print(colored("For Sites List: 1", 'red'))
print(colored("For Site : 2", 'red'))
engine = Bing()

nu = int(input("Enter Choice : "))
if nu == 1:
    fi = str(input("Enter Sites File ====> "))
    try:
        fl = open(fi, "r")
        fo = fl.readlines()
    except:
        print("Please Check Your File !")
    print(colored("Working !",'yellow'))
    print(colored("----------------------------",'yellow'))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

    for fw in fo:
        try:
            results = engine.search("site:"+str(fw)+" php?")
            links = results.links()
            for j in links:
                try:
                    if str(j[-1]) in oss:
                        print("[!] Trying ===> "+str(j))
                        page = requests.get(str(j) + "%21", headers=headers)
                        for error in errors:
                            
                            if error in page.content.decode().lower():
                                print(colored("[+] Sql Injection Found ====> " + str(j) + "  Saved In vuln.txt", 'green'))
                                op = open("vuln.txt", "a")
                                op.write(str(j))
                                op.write("\n")
                            else:
                                pass
                    
                    else:
                        pass
                except:
                    print("Broken Link !")
        except:
            print("Please Try Again Later !")
            break
if nu == 2:
    fw = str(input("Enter Website Url Without http:// ====> "))
    print(colored("Working !",'yellow'))
    print(colored("----------------------------",'yellow'))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

    try:
        results = engine.search("site:"+str(fw)+" php?")
        links = results.links()
        for j in links:
            try:
                if str(j[-1]) in oss:
                    print("[!] Trying ===> "+str(j))
                    page = requests.get(str(j) + "%21", headers=headers)
                    for error in errors:
                        if error in page.content.decode().lower():
                            print(colored("[+] Sql Injection Found ====> " + str(j) + "  Saved In vuln.txt", 'green'))
                            op = open("vuln.txt", "a")
                            op.write(str(j))
                            op.write("\n")
                        else:
                            pass
                else:
                    pass
            except:
                print("Broken Link !")
    except:
        print("Please Try Again Later !")

print("Finshed !")
