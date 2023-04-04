'''
James is a businessman. He is on a tight schedule this week. The week starts on Monday
at 00:00 and ends on Sunday at 24:00. His
schedule consists of M meetings he needs to take part in. Each of them will take place in a period of time,
beginning and ending on the same day (there are no two ongoing meetings at the same time). james is very tired,
thus he needs to find the longest possible time slot to sleep. In other words, he wants to find the longest period
of time when there are no ongoing meetings. The sleeping break can begin and end on different days and should begin
and end in the same week.

You are given a string containing M lines. wach line is a substring representing one meeting in the schedule,
in the format "Ddd hh:mm-hh:mm"."Ddd" is a three-letter abbreviation for the day of the week when the meeting takes
place: "Mon" (monday), "Tue", "Wed", "Thu", "Frid", "Sat", "Sun". "hh:mm-hh:mm" means the beginning time and the
ending time of the meeting (form 00:00 to 24:00 inclusive).

The given times represent exact moments of time. So, there are exactly five minutes between 13:40 and 13:45.

For example, given a string:

"Sun 10:00-20:00 Fri 05:00-10:00 Fri 16:30-23:50 Sat 10:00-24:00 Sun 01:00-04:00 Sat 02:00-06:00 Tue 03:30-18:15 Tue 19:00-20:00 Wed 04:25-15:14 Wed 15:14-22:40 Thu 00:00-23:59 Mon 05:00-13:00 Mon 15:00-21:00"

The longest time slot when James can sleep is 505 minutes, since James can sleep from Tuesday 20:00 to Wednesday
04:25, which gives 8 hours and 25 minutes = 505 minutes.

Also, for a string:

"Mon 01:00-23:00 Tue 01:00-23:00 Wed 01:00-23:00 Thu 01:00-23:00 Fri 01:00-23:00 Sat 01:00-23:00 Sun 01:00-21:00"

James should sleep on Sunday from 21:00 to 24:00 (180 minutes).

Write a function:
def solution(S)

that, given a string S representing the schedule, returns the length of the longest time slot when James can sleep
(in minutes).

Assume that:
M is an integer within the range [1..100];
Each line of the input string is in the format "Ddd hh:mm-hh:mm" and lines are separated with newline characters;
There cannot be two ongoing meetings at any time;
Each meeting lasts at least 1 minute.

In your solution, focus on correctness. the performance of your solution will not be the focus ot the assessment.
'''


def solution(S):
    # Convert day names to day numbers
    day_numbers = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

    # Convert schedule to list of meeting start and end times in minutes since start of week
    meetings = []
    for line in S.split("\n"):
        day, start_end = line.split()
        start, end = start_end.split("-")
        start_minutes = day_numbers[day] * 24 * 60 + int(start[:2]) * 60 + int(start[3:])
        end_minutes = day_numbers[day] * 24 * 60 + int(end[:2]) * 60 + int(end[3:])
        meetings.append((start_minutes, end_minutes))

    # Sort meetings by start time
    meetings.sort()

    # Find longest sleep period
    latest_end = -1
    longest_sleep = 0
    for start, end in meetings:
        if start > latest_end:
            longest_sleep = max(longest_sleep, start - latest_end)
        latest_end = max(latest_end, end)

    # Add any remaining sleep time after last meeting
    if latest_end < day_numbers["Mon"] * 24 * 60:
        # Last meeting ends before Monday
        longest_sleep = max(longest_sleep, (day_numbers["Mon"] - 7) * 24 * 60 - latest_end)
    elif latest_end >= (day_numbers["Mon"] + 7) * 24 * 60:
        # Last meeting ends after next Monday
        longest_sleep = max(longest_sleep, (day_numbers["Mon"] + 7) * 24 * 60 - latest_end)
    else:
        # Last meeting ends on or after Monday
        longest_sleep = max(longest_sleep,
                            (day_numbers["Mon"] + 7) * 24 * 60 - latest_end + day_numbers["Mon"] * 24 * 60)

    # Convert the longest sleep period to minutes
    return longest_sleep


# assert solution("Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat
# 02:00-06:00" "\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon
# 05:00-13:00" "\nMon 15:00-21:00") == 505 assert solution("Mon 01:00-23:00\nTue 01:00-23:00\nWed 01:00-23:00\nThu
# 01:00-23:00\nFri 01:00-23:00\nSat 01:00-23:00" "\nSun 01:00-21:00") == 180

print(solution('Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat '
               '02:00-06:00\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon '
               '05:00-13:00\nMon 15:00-21:00'))
# Output: 505

print(solution('Mon 01:00-23:00\nTue 01:00-23:00\nWed 01:00-23:00\nThu 01:00-23:00\nFri 01:00-23:00\nSat '
               '01:00-23:00\nSun 01:00-21:00'))
# Output: 180
