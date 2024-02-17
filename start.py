import requests
import time
import os
from itertools import islice
cp2 = os.path.dirname(os.path.realpath(__file__) + '\\')
cp = cp2[:-8]



### CHANGE YOUR FILENAMES HERE ###

forbiddenfa = cp + "wforbidden.txt"

foundfa = cp + "wfound.txt"

nffa = cp + "w404.txt"

latest2 = cp + "latest.txt"

wlist = cp + "wordlist.txt"





### IF YOU DON'T KNOW WHAT YOU'RE DOING, DONT TOUCH CODE FROM HERE ###
def cls():
    for i in range(0, 50):
        print(" ")

cls()






inputurl = input('input your Website (make sure that the last digit IS a "/" example: "https://www.example.com/"): ')

cls()





print("current directory: " + cp + "\n")





with open(wlist) as f:
    text = f.readlines()
    wlistlen = len(text)




with open(latest2) as lines:
    for line in islice(lines, 1):
        latestline = int(line)



latestquestion = input("Start from latest line? (line " + str(latestline) + ") Y/N ")
if latestquestion.lower() == "y":
    try:
        wordlist = open(cp + "wordlist.txt", 'r')
        Linese = wordlist.readlines()
        Lines = Linese[latestline:wlistlen]
        count = latestline - 1
    except:
        cls()
        print("an error occured. please try again with 'n'")
elif latestquestion.lower() == "n":
    wordlist = open(cp + "wordlist.txt", 'r')
    Lines = wordlist.readlines()
    count = 0
    
    
    
    the_file = open(forbiddenfa,"w")
    the_file.write("")


    the_file = open(foundfa,"w")
    the_file.write("")


    the_file = open(nffa,"w")
    the_file.write("")

else:
    print("wrong info provided, only use Y/N.")
    time.sleep(3)
    exit()



url = inputurl + line.strip() + "/"
'''
response = requests.get(str(url + "<enter dir here>"))
print(response)
print(response.content)
time.sleep(99999)'''




for line in Lines:
    count += 1
    latest = open(latest2,"w")
    latest.write(str(count))


    url = inputurl + line.strip() + "/"
    os.system("title " + str(count) + url)
    response = requests.get(str(url))
    if '<Response [404]>' in str(response):
        print(str(count) + ": ERROR 404: " + line.strip())
        the_file = open(nffa,"a")
        the_file.write(str(count) + ": " + url + "\n")

    elif '<Response [403]>' in str(response):
        print(str(count) + ': FORBIDDEN   ' + line.strip())
        the_file = open(forbiddenfa,"a")
        the_file.write(str(count) + ": " + url + "\n")
    
    elif 'Here you can enter your own requirement if you want...' in str(response.content):
        print(str(count) + ': <ALSO ENTER SOMETHING HERE>   ' + line.strip())
        the_file = open(forbiddenfa,"a")
        the_file.write(str(count) + ": " + url + "\n")

    else:
        print(str(count) + ': FOUND   ' + line.strip())
        the_file = open(foundfa,"a")
        the_file.write(str(count) + ": " + url + "\n")

