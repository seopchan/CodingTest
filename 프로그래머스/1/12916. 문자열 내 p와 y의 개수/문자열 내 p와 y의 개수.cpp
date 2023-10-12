#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int p=0, y=0;
    
    for (auto i: s) {
        if (i == 'p' || i == 'P')
            p++;
        if (i == 'y' || i == 'Y')
            y++;
    }

    return p == y;
}