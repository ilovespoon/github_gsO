#25.01.17
#Andri Snær Didriksen Ásmundsson


skra=input("skýra skrá ")
skra=skra+".txt"
minskra = open(skra,'w+')
bleyta = input("Sláðu inn texta innihald")
minskra.write(bleyta+"\n")
minskra = exit
minskra = open(skra,'a')
texti = input("Sláðu inn texta :")
minskra.write(texti+"\n")
texti2 = input("Sláðu inn annan texta :")
minskra.write(texti+"\n")
texti3 = input("Sláðu aftur inn annan texta :")
minskra.write(texti+"\n")
minskra = exit
minskra = open(skra,"r")
print(minskra.read())
minskra.close
