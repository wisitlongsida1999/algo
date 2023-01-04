#include <unordered_map>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> freq;
        for (int task : tasks) {
            freq[task]++;
        }

        int result = 0;
        for (auto& [task, count] : freq) {
            if (count == 1) {
                return -1;
            }
            result += (count + 2) / 3;
        }

        return result;
    }
};