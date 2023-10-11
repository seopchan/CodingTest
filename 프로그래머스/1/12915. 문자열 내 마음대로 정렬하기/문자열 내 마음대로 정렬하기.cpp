#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int N;

bool cmp(string a, string b) {
    return a[N] < b[N];
}

vector<string> solution(vector<string> strings, int n) {
    N = n;
    sort(strings.begin(), strings.end());
    stable_sort(strings.begin(), strings.end(), cmp);
    
    return strings;
}