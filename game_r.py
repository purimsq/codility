def solution(A, B):
    #converts a time string in "HH:MM" format to the total number of minutes since midnight.
    def time_to_minutes(t):
        hh, mm = map(int, t.split(':'))
        return hh * 60 + mm

     #calculates the number of full 15-minute intervals between a given start and end time in minutes.
    def count_full_rounds(start, end):
        if start % 15 != 0:
            start += 15 - (start % 15)
        if start >= end:
            return 0
        return (end - start) // 15

      #start time to midnight (1440 minutes).
    start_time = time_to_minutes(A)
    end_time = time_to_minutes(B)


    if start_time <= end_time:
        return count_full_rounds(start_time, end_time)
    else:
        return count_full_rounds(start_time, 1440) + count_full_rounds(0, end_time)


print(solution("12:01", "12:44"))  
print(solution("20:00", "06:00")) 
print(solution("00:00", "23:59")) 
print(solution("12:03", "12:03"))  
