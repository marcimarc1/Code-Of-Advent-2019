import time

def check_increasing(number): 
    for i in range(len(number)-1):
        if int(number[i])>int(number[i+1]):
            return False
    return True

def check_double(number):
    d = {}
    for i in range(len(number)-1):
         if int(number[i])==int(number[i+1]):
            if number[i] in d.keys():
                 d[number[i]] = d[number[i]]+1
            else:
                d[number[i]] = 2
    for keys in d.keys():
        if d[keys]==2:
            #print(number)
            return True
    return False

def check_double2(number):
    for i in range(len(number)-2):
         if int(number[i])==int(number[i+1]):
            if int(number[i])!=int(number[i+2]):
                return True
    return False

ts = time.time()
count = 0 
for i in range(356261,846303+1):
    if check_increasing(str(i)):
        if check_double(str(i)):
            count += 1
te = time.time()-ts
print(te)
print(count)

print('NEw round')
ts = time.time()
count = 0 
for i in range(356261,846303+1):
    if check_increasing(str(i)):
        if check_double2(str(i)):
            count += 1
te = time.time()-ts
print(te)
print(count)