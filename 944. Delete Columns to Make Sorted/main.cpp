#include <string>
#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int count_col = 0;
        for (int i = 0; i < strs[0].size(); i++) {
            char prev = strs[0][i];
            char curr ;
            for (int j = 1; j < strs.size(); j++) {
                curr = strs[j][i];
                if (prev > curr) {
                    count_col++;
                    break;
                } else {
                    prev = curr;
                }
            }
        }
        return count_col;
    }
};



int main() {

Solution inst_tst;

vector<string> strs = {"cba","daf","ghi"};

int res = inst_tst.minDeletionSize(strs);

cout<<res;

return 0;

}