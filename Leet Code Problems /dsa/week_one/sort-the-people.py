class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine names and heights into a list of tuples
        people = list(zip(names, heights))

        people.sort(key=lambda x: x[1], reverse=True)

        return [name for name, _ in people]

        
