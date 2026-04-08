class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, count, largest = 0, {}, 0
        
        for right in range(len(s)):
            letter = s[right]
            count[letter] = count.get(letter, 0) + 1

            while count[letter] > 1:
                left_let = s[left]
                count[left_let] -= 1

                if count[left_let] == 0:
                    del count[left_let]

                left += 1

            largest = max(largest, right - left + 1)

        return largest
