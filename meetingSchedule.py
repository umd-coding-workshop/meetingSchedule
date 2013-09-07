import unittest

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

"""N.B. day names here are variables standing in for numbers
See lines 5-11"""
days = [monday, tuesday, thursday, friday]

# this next bit from http://code.activestate.com/recipes/252178/

def all_perms(days):
    """Generate all permutations of a given list of days.
    Remove duplicates based on the circular nature of the list,
    eg, MTHF = THFM = HFMT = FMTH
    """
    
    if len(days) <=1:
        yield days
    else:
        for perm in all_perms(days[1:]):
            for i in range(len(days)-1):
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

def get_candidates(schedule):
    option = 1
    # Start of list of lists to keep track of schedules, shortest spans between meetings
    # and longest spans between meetings
    candidates = []
    for i in schedule:
        sequence = [week[n] for n in i]

        spans = analyze_sequence(i)

        shortestSpan = get_shortest_span(spans)
        
        longestSpan = get_longest_span(spans)
        
        candidate = { 'Option' : option,
                      'Spans' : spans,
                      'ShortestSpan' : shortestSpan,
                      'LongestSpan' : longestSpan,
                      'Sequence' : sequence }
                      
        candidates.append(candidate)
        option = option + 1        

    return candidates

def get_shortest_span(spans):
    """Get the shortest span from a list of spans."""
    return min(spans)

def get_longest_span(spans):
    """Get the longest span from a list of spans."""
    return max(spans)

def get_longest_minimum(candidates):    
    return max([c['ShortestSpan'] for c in candidates])

def get_sequences_with_longest_minimum(candidates, longestMinimum):
    finalists = []
    for i in range(len(candidates)):
        if candidates[i]['ShortestSpan'] == longestMinimum:
            finalists.append(candidates[i])
    return finalists

def print_selections(selections):
     for selection in selections:
        print("\nOption " + str(selection['Option']) + ":")
        print("  sequence: " + str(selection['Sequence']))
        print("  spans: " + str(selection['Spans']))
        print("  shortest span: " + str(selection['ShortestSpan']))
        print("  longest span: " + str(selection['LongestSpan']))
     return()
    
def main():
    """Command line execution."""

    # see http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained for figuring out how this works.
    schedule = all_perms(days)

    candidates = get_candidates(schedule)
    
    print("All the possibilities: ")
    print_selections(candidates)
    
    longestMinimum = get_longest_minimum(candidates)
    print("\nLongest minimum of all!: " + str(longestMinimum)) 
    
    finalists = get_sequences_with_longest_minimum(candidates, longestMinimum)
    print("Schedule(s) with the longest minimum: " )
    print_selections(finalists)
    
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

    def test_get_candidates(self):
        self.assertEqual(len(get_candidates(all_perms(days))), 6)

    def test_get_sequences_with_longest_minimum(self):
        candidates = get_candidates(all_perms(days))
        longestMinimum = get_longest_minimum(candidates)
        finalists = get_sequences_with_longest_minimum(candidates, longestMinimum)
        self.assertEqual(len(finalists), 1)
        self.assertEqual(finalists[0]['Sequence'], ['Thursday', 'Tuesday', 'Monday', 'Friday'])
        
if __name__ == '__main__':
    test = unittest.main(exit=False)
    
    if (test.result.wasSuccessful()):
        main()

