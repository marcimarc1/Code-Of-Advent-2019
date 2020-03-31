inp = [1,1,1,4,99,5,6,0,99]

def check(l,pos):

  if l[pos]==1:
    x = l[l[pos+1]] + l[l[pos+2]]
    l[l[pos+3]] = x
  elif l[pos]==2:
    x = l[l[pos+1]] * l[l[pos+2]]
    l[l[pos+3]] = x
  elif l[pos]==99:
    return l
  return l  

test = inp
#test = [1,9,10,3,2,3,11,0,99,30,40,50]
i=0
while i <len(test):
  if test[i] == 99:
    break
  else:
    test = check(test, i)
    i = i+4 #instruction pointer
print(test[0])