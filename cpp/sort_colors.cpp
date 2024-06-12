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
//
class Solution {
public:
  void sortColors(vector<int> &nums) {
    int c0 = 0, c1 = 0, c2 = 0;
    for (int c : nums) {
      if (c == 0) {
        c0++;
      } else if (c == 1) {
        c1++;
      } else {
        c2++;
      }
    }
    for (int i = 0; i < nums.size(); i++) {
      if (c0) {
        nums[i] = 0;
        c0--;
      }
      else if (c1) {
        nums[i] = 1;
        c1--;
      } else {
        nums[i] = 2;
      }
    }
  }
};
