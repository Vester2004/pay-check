from datetime import date
#samler info#
løn = int((75.5)) 
tid = int(input("hvor mange timer har du arbejdet idag:"))
ialt = int((tid*løn))
dag = str(date.today())
txt = str((tid,'timer',ialt,"kroner","dato",dag))



#åber filien#
with open("løn.txt","+a") as file1:
    file1.write(txt+"\n")
    file1.close()

