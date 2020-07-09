import sys
test=open("rawtext.txt")
tran=open("tts.txt",'w')
for line in test:
    tran.write(line.replace(",","").replace("?"," ").replace("3","tre").replace("2","to").replace("."," ").replace("-","").lower())
    print(line.replace(",","").replace("?"," ").replace("3","tre").replace("2","to").replace("."," ").lower())



test1=open("tale.txt")
orginal=open("orginal.txt",'w')
e=""
for line in test1:
    if len(line)==1:
        continue
    e=e+line.replace(",","").replace("?"," ").strip().replace("\"","").replace("!","").replace("."," ").replace("-","").lower()
orginal.write(e)

print(e)
