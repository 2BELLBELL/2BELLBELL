/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;

const int INF = 1'000'000'000;
int dp[10001][101];

int solve(int n, int m) {
    if(dp[n][m] != INF) return dp[n][m];
    
    if(n < m) {
        dp[n][m] = solve(m, n);
        return dp[n][m];
    }
    if(n%m == 0) {
        dp[n][m] = n/m;
        return dp[n][m];
    }
    if(n > 3*m) {
        dp[n][m] = solve(n-m, m)+1;
        return dp[n][m];
    }
    
    for(int i = 1; i < n; i++) {
        dp[n][m] = min(dp[n][m], solve(i, m)+solve(n-i, m));
    }
    for(int j = 1; j < m; j++) {
        dp[n][m] = min(dp[n][m], solve(n, j)+solve(n, m-j));
    }
    
    return dp[n][m];
}

int main()
{
    int n, m; cin >> n >> m;
    
    for(int i = 0; i <= 10001; i++) {
        fill(dp[i], dp[i]+101, INF);
    }
    
    cout << solve(n, m);

    return 0;
}