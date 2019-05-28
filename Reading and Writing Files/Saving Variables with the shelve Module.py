import shelve
shefFile = shelve.open("mydata")
 
cats = ['aa','aa']
shefFile['cat'] = cats
shefFile.close()
