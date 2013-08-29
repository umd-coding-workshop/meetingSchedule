week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

shortestSpan = 15
longestSpan = 0

def all_perms(days):
    if len(days) <=1:
        yield days
    else:
        for perm in all_perms(days[1:]):
            for i in range(len(days)):
                #nb schedule[0:1] works in both string and list contexts
                yield perm[:i] + days[0:1] + perm[i:]

days = [monday, tuesday, thursday, friday]


schedule = all_perms(days)
for i in schedule:
    print (i)
    for j in range(len(i)):
        #print j
        #print i[j]
        dayCode = i[j]
        print week[dayCode]


'''
for j in range(0,4):
    thisWeek = schedule[j]
    nextWeek = schedule[(j+1) % 4]
    timeBetween = nextWeek + 7 - thisWeek
    print "There are %s days between week %s and week %s" % (timeBetween, j+1, j+2)
    if timeBetween < shortestSpan:
        shortestSpan = timeBetween

print "The shortest time between meetings is " + str(shortestSpan) + " days"
'''

