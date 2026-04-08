class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, count, biggest, res = 0, {}, 0, 0

        for right in range(len(s)):
            letter = s[right]
            count[letter] = 1 + count.get(letter, 0)
            biggest = max(biggest, count[letter])
            
            while (right - left + 1) - biggest > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
            


