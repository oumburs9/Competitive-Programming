class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenDict = defaultdict(int) # tokenId -> currentTime + timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenDict[tokenId] =  currentTime + self.timeToLive 
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if currentTime < self.tokenDict[tokenId]:
            self.tokenDict[tokenId] = self.timeToLive + currentTime 
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        tokensToDelete = []
        count = 0

        for token in self.tokenDict:
            if self.tokenDict[token] > currentTime:
                count += 1
            else:
                tokensToDelete.append(token)
        # cleaning if expired
        for token in tokensToDelete:
            del self.tokenDict[token]

        return count
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)