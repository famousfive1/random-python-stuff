g = open("file.txt", 'w')

with open("file_unf.txt") as f:
    for line in f.readlines():
        dx = line.rfind('+')
        line = line[dx+2:].lower().replace('?','').replace(',','').replace('!','')
        line = line.replace('-','').replace('..','').replace('\'','').replace('\"', '')
        line = line.split('.')
        for l in line:
            g.write(l)
g.close()
