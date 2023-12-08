class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losers = Counter([ match[1]  for match in matches  ])
        
        one_time_losers = { k for k ,v in losers.items() if v == 1  }
        
        
        winners = { match[0]  for match in matches  if match[0] not in losers }

        return [sorted(list(winners)), sorted(one_time_losers)]

       

        









        