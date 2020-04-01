filename='D6/inp.txt'
orbits = []
solar_system = dict()
with open(filename) as f:
    for lines in f.readlines():
        orbits.append(lines)
        orbits[-1] = lines[-1].strip('\n').split(')')
        
        #solar_system[orbits[-1][1]]=Planet(prbits[-1][0],orbits[-1][1])

#build tree
root = Planet(orbits[0][0])
for i in range(1,len(orbits)):
    roots.childs

class Planet:
    def __init__(self, parent_orbit, childs = []]):
        self.parent_orbit =parent_orbit
        self.childs = childs
        self.nooc = None
        if self.parent_orbit = 'COM':
            self.nooc=1
        
    def number_of_orbits():
        return

    def get_nooc(self):
        return self.nooc
    
def Count_Recursive(p):
    count = 0 
    if p.parent_orbit = 'COM':
        count += p.get_nooc()
    else:
        count += Count_Recursive(p.parent_orbit)
    return count
