#Ísar Daði Pálsson
#25.1.2017

skjalanafn = input("Sláðu inn heiti fyrir skránna þína")
skjalanafnid = skjalanafn+ ".txt"
minskra=open(skjalanafnid, "w+")

stuff = input("Sláðu inn texta")
minskra.write(stuff+"\n")
minskra.close

minskra=open(skjalanafnid, "a")
vinnslutexti1=input("Bættu við texta í skránna")
minskra.write(vinnslutexti1+"\n")
vinnslutexti2=input("Bættu við öðrum texta í skránna")
minskra.write(vinnslutexti2+"\n")
vinnslutexti3=input("Bættu við enn örðum texta í skránna")
minskra.write(vinnslutexti3+"\n")
minskra.close

