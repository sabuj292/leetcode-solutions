

#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1'000'000'007;
using ull = unsigned long long;

const int MAXC = 64;
long long PROD[MAXC + 1];
ull LEN[MAXC + 1];

inline long long mulmod(long long a, long long b){ return (a*b) % MOD; }

void precompute() {
    LEN[0] = LEN[1] = 0;
    for (int c = 2; c <= MAXC; ++c) LEN[c] = (1ULL << (c - 1)) - 1ULL;
    PROD[0] = PROD[1] = 1;
    PROD[2] = 2;
    for (int c = 3; c <= MAXC; ++c) {
        long long t = mulmod(PROD[c-1], PROD[c-1]);
        PROD[c] = mulmod(t, c);
    }
}

inline int ceil_log2(ull x) {
    int lg = 63 - __builtin_clzll(x);
    return ((x & (x - 1)) ? lg + 1 : lg);
}

long long drain_prefix_prod(long long C, ull L) {
    if (L == 0 || C <= 1) return 1;
    int cap = max(2, ceil_log2(L + 1) + 2);
    if (C > cap) C = cap;
    ull left_len = (C >= 2 ? ((1ULL << (C - 2)) - 1ULL) : 0ULL);
    if (L <= left_len) {
        return drain_prefix_prod(C - 1, L);
    } else if (L == left_len + 1) {
        return mulmod(PROD[C - 1], C % MOD);
    } else {
        ull rest = L - (left_len + 1);
        long long left_full = mulmod(PROD[C - 1], C % MOD);
        return mulmod(left_full, drain_prefix_prod(C - 1, rest));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int T; 
    cin >> T;
    while (T--) {
        int n; long long k;
        cin >> n >> k;
        vector<long long> a(n);
        for (auto &x : a) cin >> x;
        sort(a.begin(), a.end());

        ull non_one = (a[0] == 1 ? (k / 2) : ((k + 1) / 2));
        long long ans = 1;

        for (long long x : a) {
            if (x < 2) continue;
            if (non_one == 0) break;
            ans = mulmod(ans, x % MOD);
            --non_one;
            if (non_one == 0) break;
            long long C = x - 1;
            ull can_take;
            if (C <= 1) {
                can_take = 0;
            } else if (C >= MAXC) {
                can_take = non_one;
            } else {
                can_take = min<ull>(non_one, LEN[C]);
            }
            if (can_take) {
                ans = mulmod(ans, drain_prefix_prod(C, can_take));
                non_one -= can_take;
            }
        }

        cout << ans % MOD << "\n";
    }
    return 0;
}