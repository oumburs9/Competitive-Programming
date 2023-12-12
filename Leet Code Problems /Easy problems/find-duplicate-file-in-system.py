class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for path in paths:
            arr = path.split(' ')
            directory = arr[0]

            for i in range(1,len(arr)):
                # fileName(content)
                fileName = arr[i][:arr[i].index('(')]
                content = arr[i][arr[i].index('('): len(arr[i])-1]

                dir = directory + '/' + fileName

                store[content].append(dir)
            
        return [ dir for dir in store.values() if len(dir) > 1]

