#Ísar Daði Pálsson
#25.1.2017

skjalanafn = input("Sláðu inn heiti fyrir skránna þína")
skjalanafnid = skjalanafn+ ".txt"
minskra=open(skjalanafnid, "w+")

stuff = input("Sláðu inn texta")
minskra.write(stuff+"\n")
minskra.close

