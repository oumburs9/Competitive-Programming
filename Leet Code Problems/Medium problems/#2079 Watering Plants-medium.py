class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        cap = capacity
        steps = 1
        
        for i in range(len(plants)-1):
            cap -= plants[i]
            
            if cap < plants[i+1]:
                cap = capacity
                steps += 2*(i+1) + 1
            else:    
                steps +=1
            
        return steps

                
            
        