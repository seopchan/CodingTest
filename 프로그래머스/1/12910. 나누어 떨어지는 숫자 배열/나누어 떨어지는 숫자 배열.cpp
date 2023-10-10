#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> l;
    for (int i=0; i<arr.size(); i++) {
        if (arr[i] % divisor == 0) {
            l.push_back(arr[i]);
        }
    }
    
    if (l.size() == 0) {
        return {-1};
    }
    
    sort(l.begin(), l.end());
    
    return l;
}