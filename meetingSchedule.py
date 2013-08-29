sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

schedule = [monday, tuesday, thursday, friday]

shortestSpan = 15

for j in range(0,4):
    thisWeek = schedule[j]
    nextWeek = schedule[(j+1) % 4]
    timeBetween = nextWeek + 7 - thisWeek
    print "There are %s days between week %s and week %s" % (timeBetween, j+1, j+2)
    if timeBetween < shortestSpan:
        shortestSpan = timeBetween

print "The shortest time between meetings is " + str(shortestSpan) + " days"


