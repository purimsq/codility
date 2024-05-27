def solution(A):
    from collections import defaultdict
    
    # Dictionary to track doctor appearances across hospitals
    doctor_days = defaultdict(set)
    
    # Iterate through the schedule matrix
    for hospital_id in range(len(A)):
        for day_id in range(len(A[0])):
            doctor_id = A[hospital_id][day_id]
            doctor_days[doctor_id].add((hospital_id, day_id))
    
    # Count doctors who work at more than one hospital
    multi_hospital_doctors = sum(1 for doctor, days in doctor_days.items() if len(set(day[0] for day in days)) > 1)
    
    return multi_hospital_doctors


print(solution([[1, 2, 2], [3, 1, 4]]))  
print(solution([[1, 1, 5, 2, 3], [4, 5, 6, 4, 3], [9, 4, 4, 1, 5]]))  
print(solution([[4, 3], [5, 5], [6, 2]]))  