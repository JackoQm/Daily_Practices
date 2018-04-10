/*
 *	From: LeetCode - 598. Range Addition II (https://leetcode.com/problems/range-addition-ii/description/)
 *	Level: Easy
 *	Question: Given an m * n matrix M initialized with all 0's and several update operations.
			  Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
 			  You need to count and return the number of maximum integers in the matrix after performing all the operations.
 *	Status: AC
 *	Solution: Using set intersection(https://leetcode.com/problems/range-addition-ii/solution/)
*/

#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int begin, end;
        begin = m;
        end = n;
        for(int i = 0; i < ops.size(); ++i) {
            int b, e;
            b = ops[i][0], e = ops[i][1];
            if(b < begin)
                begin = b;
            if(e < end)
                end = e;
        }
        return begin*end;
    }
};

/*
Standard Answer:

public class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        for (int[] op: ops) {
            m = Math.min(m, op[0]);
            n = Math.min(n, op[1]);
        }
        return m * n;
    }
}
*/
