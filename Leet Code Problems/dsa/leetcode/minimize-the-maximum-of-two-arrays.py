class Solution:
    def minimizeSet(self, div1: int, div2: int, cnt1: int, cnt2: int) -> int:
        min_possible_max = cnt1 + cnt2
        max_possible_max = 2 ** 31

        while min_possible_max <= max_possible_max:
            mid = min_possible_max + (max_possible_max - min_possible_max) // 2

            common_multiples = mid // ((div1 * div2) // self.gcd(div1, div2))
            
            div1_multiples = mid // div1 - common_multiples
            div2_multiples = mid // div2 - common_multiples
            
            not_multiple = mid - (mid // div1 + mid // div2 - common_multiples)
           
            e_demand1 = max(0, cnt1 - div2_multiples)
            e_demand2 = max(0, cnt2 - div1_multiples)
            
            if e_demand1 + e_demand2 <= not_multiple:
                max_possible_max = mid - 1

            else:
                min_possible_max = mid + 1

        return min_possible_max

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
