
import urllib.request

fhand = urllib.request.urlopen('http://127.0.0.1:3000/romeo.txt')
for line in fhand:

    print(line.decode().strip())
