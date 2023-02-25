#include <iostream>
#include <vector>


using namespace std;

class Solution {
public:
    int maxProfit(vector<int> p) {
        vector<int> mx = {p[0], 0};
        vector<int> mn = {p[0], 0};
        int dt = 0;

        for (int i = 1; i < p.size(); i++) {
            int j = p[i];
            if (j < mn[0]) {
                mn[0] = j;
                mn[1] = i;
            }
            if (j > mn[0] && i > mn[1]) {
                mx[0] = j;
                mx[1] = i;
            }
            if (mx[0] - mn[0] > dt && mx[1] > mn[1]) {
                dt = mx[0] - mn[0];
            }
        }
        return dt;
    }
};



int main()
{

    Solution inst;

    cout<<inst.maxProfit({1,2,3});
    

    return 0;
}

