import requests
import sys
import codecs
import os
import time

def end():
    steve = 1
p1 = "https://duckduckgo.com/?q="
p2 = input().replace(" ", "+")
p3 = p1 + p2
timeout = 0
def find():
    global timeout
    timeout += 1
    print(timeout)
    try:
        #time.sleep(1)
        res = requests.get(p3)
        res.raise_for_status()
        playFile = open('RomeoAndJuliet1.txt', 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)

        playFile.close()

        f = codecs.open('RomeoAndJuliet1.txt',encoding='utf-8')
        contents = f.read()
        newcontents = contents.replace('"','*').replace("'", '^')
        page = newcontents
        i = page.index("Abstract") + 11 
        defn = page[i: page.index("*", i)]
        f.close
        if timeout == 8:
            print('timed out')
            exit()
        if defn == '' or defn == 't' or defn == 'rce':
            find()
        if defn != '' and defn != 't' and defn != 'rce' and defn != 'err':
            open(p2.replace("+", " ") + '.txt', "w").write(defn)
            print(defn)
            end()
    except:
            print('err')
            open(p2.replace("+", " ") + '.txt', "w").write('err')
            end()
find()
end()
os.remove("RomeoAndJuliet1.txt")
