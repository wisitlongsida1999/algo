Algo 

This problem isn't anymore. It's just find the relation betweem them follow these pattern.

List members   |   Output | 
1              |   1      | 
2              |   1      | 
3              |   2      | 
6              |   3      | 
10             |   4      | 
15             |   5      | 
21             |   6      | 


Then find out the math solution that match with above pattern.


Note : n = List members, k = Output

1 + 2 + ... + k <= n
k(k + 1) / 2 <= n
(k + 0.5)(k + 0.5) <= n * 2 + 0.25
k + 0.5 <= sqrt(n * 2 + 0.25)
k <= sqrt(n * 2 + 0.25) - 0.5

Time O(1)
Space O(1)