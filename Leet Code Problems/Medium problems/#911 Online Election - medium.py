from bisect import bisect_right
from typing import List


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = self._compute_leaders(persons)

    def _compute_leaders(self, persons: List[int]) -> List[int]:
        vote_count = {}  
        leaders = []   
        leader = None    
        max_votes = 0   
        
        for person in persons:
            vote_count[person] = vote_count.get(person, 0) + 1
            if vote_count[person] >= max_votes:
                leader = person
                max_votes = vote_count[person]
            leaders.append(leader)
        
        return leaders

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t)  
        return self.leaders[idx - 1]  

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)