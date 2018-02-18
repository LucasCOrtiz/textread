#!/home/lucas/anaconda3/envs/py3L/bin/python
lines=[]
with open('mobydick.txt','rt') as in_file: 
    contents = in_file.read()
    print(contents)
    for line in contents.strip():
        lines.append(line)

