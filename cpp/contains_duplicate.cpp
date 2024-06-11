
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

void solve() {
  int n;
  cin >> n;
  string s, t;
  cin >> t >> s;
  sort(s.begin(), s.end());
  sort(t.begin(), t.end());
  reverse(s.begin(), s.end());
  reverse(t.begin(), t.end());
  string ss = s;
  string tt = t;
  // min theni yekel ala rasou  <=
  int ans = 0;
  while (!s.empty()) {
    while (!s.empty() && s.back() < t.back()) {
      ans++;
      s.pop_back();
    }
    if (!s.empty()) {
      s.pop_back();
    }
    t.pop_back();
  }
  cout << ans << endl;
  ans = 0;
  while (!ss.empty()) {
    while (!ss.empty() && ss.back() <= tt.back()) {
      ss.pop_back();
    }
    if (!ss.empty()) {
      ans++;
      ss.pop_back();
    }
    tt.pop_back();
  }
  cout << ans << endl;
}

int main() {
  // freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
  FAST;
  int p = 1;
  int t = 1;
  // cin >> t;
  while (t--) {
    // cout << "Case #"<<p++<< ": ";
    solve();
  }
}

/* stuff you should look for
 * int overflow, array bounds
 * special cases (n=1?)
 * do smth instead of nothing and stay organized
 * WRITE STUFF DOWN
 * DON'T GET STUCK ON ONE APPROACH
 * think backwards
 */
