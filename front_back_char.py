#Given a string, return a new string where the first and last chars have been exchanged

def front_back(world):
    if len(world) == 1:
        return world
    else:    
        return world[-1] + world[1:-1] + world[0]
    
    
    
print(front_back('clarusway'))
print(front_back('a'))
print(front_back('ab'))