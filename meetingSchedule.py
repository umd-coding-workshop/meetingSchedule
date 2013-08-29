week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

# this next bit from http://code.activestate.com/recipes/252178/

def all_perms(days):
    if len(days) <=1:
        yield days
    else:
        for perm in all_perms(days[1:]):
            for i in range(len(days)):
                #nb schedule[0:1] works in both string and list contexts
                yield perm[:i] + days[0:1] + perm[i:]

days = [monday, tuesday, thursday, friday]

# see http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained for figuring out how this works.
schedule = all_perms(days)
option = 1
for i in schedule:
    print "Option " + str(option) + ":"
    shortestSpan = 15
    longestSpan = 0
    for j in range(len(i)):
        #print j
        #print i[j]
        dayCode = i[j]
        print "Week " + str(j+1) + ": " + str(week[dayCode])

    for j in range(len(i)):
        thisWeek = i[j]
        nextWeek = i[(j+1) % 4]
        timeBetween = nextWeek + 7 - thisWeek
        print "There are %s days between week %s and week %s meetings" % (timeBetween, j+1, j+2)
        if timeBetween < shortestSpan:
            shortestSpan = timeBetween
    print "The shortest time between meetings is " + str(shortestSpan) + " days"    
    option = option + 1