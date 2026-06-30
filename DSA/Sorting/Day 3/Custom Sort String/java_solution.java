class Solution {
    public String customSortString(String order, String s) {

        // Frequency array for 26 lowercase letters
        int[] freq = new int[26];

        // Count frequencies
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }

        StringBuilder result = new StringBuilder();

        // Add characters according to custom order
        for (char ch : order.toCharArray()) {
            int idx = ch - 'a';
            while (freq[idx] > 0) {
                result.append(ch);
                freq[idx]--;
            }
        }

        // Add remaining characters
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                result.append((char) (i + 'a'));
                freq[i]--;
            }
        }

        return result.toString();
    }
}