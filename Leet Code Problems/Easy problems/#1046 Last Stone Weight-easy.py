class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = list(map(neg, stones))  # negate values to simulate max heap behavior
        heapify(hq)  # convert the list into a min heap

        while len(hq) > 1 and hq[0] != 0:
            heappush(hq, heappop(hq) - heappop(hq))  # Smash the two smallest elements

        return -heappop(hq)  # return the last remaining stone's weight

        

  
    
