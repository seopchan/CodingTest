#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    int h = s.size() / 2;
    if (s.size() % 2) {
        string ans = s.substr(h, 1);
        return ans;
    } else {
        string ans = s.substr(h-1, 2);
        return ans;
    }

}