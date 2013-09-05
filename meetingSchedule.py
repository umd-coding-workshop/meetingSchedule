import unittest

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
    """Generate all permutations of a given list of days."""
    
    if len(days) <=1:
        yield days
    else:
        for perm in all_perms(days[1:]):
            for i in range(len(days)):
                #nb schedule[0:1] works in both string and list contexts
                yield perm[:i] + days[0:1] + perm[i:]

def analyze_sequence(seq):
    """Analyze a sequence of days in a week and return a list of spans between days."""
    
    spans = []
    for j in range(len(seq)):
        thisWeek = seq[j]
        nextWeek = seq[(j+1) % 4]
        timeBetween = nextWeek + 7 - thisWeek
        spans.append(timeBetween)

    return spans

def get_shortest_span(spans):
    """Get the shortest span from a list of spans."""
    return min(spans)
    
def main():
    """Command line execution."""
    
    days = [monday, tuesday, thursday, friday]

    # see http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained for figuring out how this works.
    schedule = all_perms(days)
    option = 1
    for i in schedule:
        print("\nOption " + str(option) + ":")
        print("  sequence: " + str([week[n] for n in i]))

        spans = analyze_sequence(i)
        print("  spans: " + str(spans))

        shortestSpan = get_shortest_span(spans)
        print("  shortest span: " + str(shortestSpan))
        option = option + 1
    
class MeetingScheduleTestCase(unittest.TestCase):
    """Unit tests for meetingSchedule."""
    
    def test_analyze_sequence(self):
        self.assertEqual(analyze_sequence([monday,tuesday,thursday,friday]),  [8,9,8,3])
        self.assertEqual(analyze_sequence([tuesday,thursday,monday,friday]),  [9,4,11,4])
        self.assertEqual(analyze_sequence([thursday,tuesday,monday,friday]),  [5,6,11,6])

    def test_get_shortest_span(self):
        self.assertEqual(get_shortest_span(analyze_sequence([monday,tuesday,thursday,friday])),  3)
        self.assertEqual(get_shortest_span(analyze_sequence([tuesday,thursday,monday,friday])),  4)
        self.assertEqual(get_shortest_span(analyze_sequence([thursday,tuesday,monday,friday])),  5)
        
if __name__ == '__main__':
    test = unittest.main(exit=False)
    
    if (test.result.wasSuccessful()):
        main()

