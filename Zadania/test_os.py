iport os

path = 'text.txt'
if os.path.exists(path).st_size > 0:
    print("File not empty")
else:print ("Empty file")

print((os.path.exists(path)))
