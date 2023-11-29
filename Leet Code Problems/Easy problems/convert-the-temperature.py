class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        kel = celsius + 273.15
        fahrenheit = 1.8*celsius + 32
        
        return [kel,fahrenheit]
        