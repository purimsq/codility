def solution(A):
    A.sort()  # Sort the array
    n = len(A)
    if n == 1:
        return 1
    
    max_spike_length = 0
    
    # Iterate through each element as a possible peak
    for peak in range(n):
        # Length of the increasing part
        inc_length = peak
        
        #  maximum index of the decreasing part
        dec_index = peak
        while dec_index < n - 1 and A[dec_index] < A[dec_index + 1]:
            dec_index += 1
        
        # Length of the decreasing part
        dec_length = 0
        for i in range(dec_index, n - 1):
            if A[i] > A[i + 1]:
                dec_length += 1
            else:
                break
        
        # Total spike length: inc_length + dec_length + 1 (counting the peak)
        spike_length = inc_length + dec_length + 1
        
       
        max_spike_length = max(max_spike_length, spike_length)
    
    return max_spike_length

print(solution([1, 2]))               
print(solution([2, 5, 3, 2, 4, 1]))   
print(solution([2, 3, 3, 2, 2, 2, 1])) 
