



def vmaxSumTwoNoOverlap (A, L, M):
   
  
    maxMStartFrom = [0]*100
    
    currentMax = 0
    currentSum = 0
    
    for i in range(len(A)-1,0,-1):
      currentSum += A[i]
      
      if (i < len(A) - M) :
        currentSum -= A[i + M]
      
      
      if (i <= len(A)- M) :
        currentMax = max(currentMax, currentSum)
        maxMStartFrom[i] = currentMax
      
  
    
    maxMEndAt = [0]*100
    currentSumL = 0
    currentSumM = 0
    currentMaxM = 0
    
    
    maxSum = 0
    
    
    for i in range(len(A)) :
      currentSumM += A[i]
      if (i > M - 1) :
        currentSumM -= A[i - M]
      
      
      if (i >= M - 1) :
        currentMaxM = max(currentMaxM, currentSumM)
        maxMEndAt[i] = currentMaxM
      
      
      
      currentSumL += A[i]
      if (i > L - 1) :
        currentSumL -= A[i - L]
      
      
      if (i >= L - 1) :
        
        maxSumMFromLeft =0 if i - L < M - 1 else maxMEndAt[i - L]
        maxSumMFromRight = maxMStartFrom[i + 1] if i + 1 + M - 1 < len(A) else 0
        maxSum = max(
          maxSum, 
          currentSumL + max(maxSumMFromLeft, maxSumMFromRight)
          )
      
      
    
  
    return maxSum

vmaxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2)