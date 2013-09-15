import unittest
import argparse
from itertools import permutations

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
all_options = permutations(['M','T','H','F']) # errant line. I don't THINK it's needed any more





def analyze_sequence(seq):
    """Analyze a sequence of days in a week and return a list of spans between days."""
    
    spans = []
    for j in range(len(seq)):
        thisWeek = seq[j]
        nextWeek = seq[(j+1) % len(seq)]
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

def all_perms(days):
    daysSliced = (days[:len(days)-1]) # eliminate equivalent schedules by permutating first len(days)-1 values then append last value
    daysLast = (days[len(days)-1:])    
    daysLast = daysLast[0]
    
    schedule = []
    temp = permutations(daysSliced)
    for i in temp:    
        i = list(i) # convert to list to allow appending
        i.append(daysLast)    
        schedule.append(i)
    return(schedule)

def main():
    """Command line execution."""
    
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

    schedule0 = [monday,tuesday,thursday,friday]
    schedule1 = [tuesday,thursday,monday,friday]
    schedule2 = [thursday,tuesday,monday,friday]
    schedule3 = [monday,tuesday,wednesday]
    schedule4 = [monday, tuesday, thursday, friday, sunday]
    
    def test_analyze_sequence(self):
        self.assertEqual(analyze_sequence(self.schedule0),  [8,9,8,3])
        self.assertEqual(analyze_sequence(self.schedule1),  [9,4,11,4])
        self.assertEqual(analyze_sequence(self.schedule2),  [5,6,11,6])
        self.assertEqual(analyze_sequence(self.schedule3),  [8,8,5])
        
    def test_get_shortest_span(self):
        self.assertEqual(get_shortest_span(analyze_sequence(self.schedule0)),  3)
        self.assertEqual(get_shortest_span(analyze_sequence(self.schedule1)),  4)
        self.assertEqual(get_shortest_span(analyze_sequence(self.schedule2)),  5)
        self.assertEqual(get_shortest_span(analyze_sequence(self.schedule3)),  5)

    def test_get_candidates(self):
        self.assertEqual(len(get_candidates(all_perms(self.schedule0))), 6)
        self.assertEqual(len(get_candidates(all_perms(self.schedule3))), 2)

    def test_get_sequences_with_longest_minimum(self):
        candidates = get_candidates(all_perms(self.schedule0))
        longestMinimum = get_longest_minimum(candidates)
        finalists = get_sequences_with_longest_minimum(candidates, longestMinimum)
        self.assertEqual(len(finalists), 1)
        self.assertEqual(finalists[0]['Sequence'], ['Thursday', 'Tuesday', 'Monday', 'Friday'])

        candidates = get_candidates(all_perms(self.schedule4))
        longestMinimum = get_longest_minimum(candidates)
        finalists = get_sequences_with_longest_minimum(candidates, longestMinimum)
        self.assertEqual(len(finalists), 2)
 
if __name__ == '__main__':

    # Parse command-line options
    parser = argparse.ArgumentParser(description='Determine the optimal rotating schedule for coding workshop meetings.')

    parser.add_argument('-t', '--test', action='store_true',
                        help='run unit tests instead of schedule analysis')
    parser.add_argument('-d', '--days', action='store',
                        help='alternate days to analyze; specify as a list')
    
    args = parser.parse_args()

    if args.days:
        days = eval(args.days)
        
    if args.test:
        # Run tests only then exit
        suite = unittest.TestLoader().loadTestsFromTestCase(MeetingScheduleTestCase)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        # Perform schedule analysis
        main()

