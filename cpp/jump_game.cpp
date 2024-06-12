#include <algorithm>
#include <bits/stdc++.h>

#define FAST ios::sync_with_stdio(0), cin.tie(0) //, cout.tie(0)
#define ll long long
#define ld long double
#define endl "\n"

using namespace std;

// const int MOD = 1e9+7  ;
const int MOD = 998244353;
const int N = 2e5 + 5;
const ll INF = 1e18 + 1;
const ll MIN = -1e18;
const ll prime = 2;
// const ll prime2 = 101 ;

class Solution {
public:
  bool canJump(vector<int> &nums) {
    int x = nums.size() - 1;
    bool res = false;
    int i = x-1;
    while (i >= 0) {
      if (i + nums[i] >= nums.size() - 1) {
        x = i;
      }
      i--;
    }
    return x == 0;
  }
};
