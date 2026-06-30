class Solution {
public:
    string customSortString(string order, string s) {

        // Frequency array for 26 lowercase letters
        vector<int> freq(26, 0);

        // Count frequencies
        for (char ch : s) {
            freq[ch - 'a']++;
        }

        string result;

        // Add characters according to custom order
        for (char ch : order) {
            int idx = ch - 'a';
            while (freq[idx] > 0) {
                result += ch;
                freq[idx]--;
            }
        }

        // Add remaining characters
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                result += (char)(i + 'a');
                freq[i]--;
            }
        }

        return result;
    }
};