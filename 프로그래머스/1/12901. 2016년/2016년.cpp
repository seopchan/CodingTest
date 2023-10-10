#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(int a, int b) {
    vector<int> m = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30};
    vector<string> d = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
    int WEEK = 7;
    
    int date = b;
    for (int i=1; i<=a; i++) {
        date += m[i-1];
    }
    
    int day = date % 7;
    
    return d[day];
}