class Solution {
public:
    int characterReplacement(string s, int k) {

        int n = s.size();
        vector<int> f(256, 0);

        int low = 0, high = 0;
        int res = 0;
        int maxcnt = 0;

        for (high = 0; high < n; high++) {

            f[s[high]]++;

            maxcnt = max(maxcnt, f[s[high]]);

            int len = high - low + 1;
            int diff = len - maxcnt;

            while (diff > k) {
                f[s[low]]--;
                low++;

                len = high - low + 1;
                diff = len - maxcnt;
            }

            res = max(res, len);
        }

        return res;
    }
};