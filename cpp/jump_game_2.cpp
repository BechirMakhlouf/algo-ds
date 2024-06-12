#include <algorithm>
#include <bits/stdc++.h>
#include <unordered_map>

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
  int jump(vector<int> &nums) {
    int l = 0, r = 0;
    int ans = 0;
    while (r < nums.size() - 1) {
      int furthest = r;
      for (int i = l; i < r + 1; i++) {
        furthest = furthest > nums[i] + i ? furthest : nums[i] + i;
      }
      l = r + 1;
      r = furthest;
      ans++;
    }
    return ans;
  }
};
