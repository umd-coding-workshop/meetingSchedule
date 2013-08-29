# generates all possible permutations of a rotating schedule of four days

schedule = ("monday", "tuesday", "thursday", "friday")

for day in range(0,4):
    print schedule[day]
    
   
def all_perms(schedule):
    if len(schedule) <=1:
        yield schedule
    else:
        for perm in all_perms(schedule[1:]):
            for i in range(len(schedule)):
                #nb schedule[0:1] works in both string and list contexts
                yield perm[:i] + schedule[0:1] + perm[i:]

pattern = all_perms(schedule)
for i in pattern:
    print (i)
