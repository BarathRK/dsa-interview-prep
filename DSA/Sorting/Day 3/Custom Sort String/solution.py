class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Frequency array for 26 lowercase letters
        freq = [0] * 26

        # Count frequencies
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = []

        # Add characters according to custom order
        for ch in order:
            idx = ord(ch) - ord('a')
            while freq[idx] > 0:
                result.append(ch)
                freq[idx] -= 1

        # Add remaining characters
        for i in range(26):
            while freq[i] > 0:
                result.append(chr(i + ord('a')))
                freq[i] -= 1

        return "".join(result)