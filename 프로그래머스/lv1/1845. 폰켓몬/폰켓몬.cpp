#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int n = nums.size() / 2;
    
    vector<int> v;
    
    for (const int num: nums) {
        if (find(v.begin(), v.end(), num) == v.end()) {
            v.push_back(num);
        }
        
        if (v.size() >= n) {
            return n;
        }
    }
    
    return v.size();
}