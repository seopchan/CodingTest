#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    int h, w;
    int mh = park.size();
    int mw = park[0].size();
    map<pair<int, int>, bool> isWalkable;
    
    for (int idx_h = 0; idx_h < mh; ++idx_h) {
        string p = park[idx_h];
        for (int idx_w = 0; idx_w < mw; ++idx_w) {
            char j = p[idx_w];
            if (j == 'S') {
                h = idx_h;    
                w = idx_w;
                isWalkable.insert({make_pair(idx_h, idx_w), true});
            } else if (j == 'X') {
                isWalkable.insert({make_pair(idx_h, idx_w), false});
            } else {
                isWalkable.insert({make_pair(idx_h, idx_w), true});
            }
        }
    }
    
    for (auto &r: routes) {
        char v = r[0];
        int move_val = r[2] - '0';
        
        int tmph = h;
        int tmpw = w;
        
        bool check = true;
        
        for (int i=0; i<move_val; i++) {
            switch(v) {
                case 'E':
                    tmpw++;
                    break;
                case 'S':
                    tmph++;
                    break;
                case 'N':
                    tmph--;
                    break;
                case 'W':
                    tmpw--;
                    break;
            }
            
            if (tmpw < mw && tmph < mh && 0 <= tmpw && 0 <= tmph) {
                try {
                    if (isWalkable.at(make_pair(tmph, tmpw))) {
                        continue;
                    } else {
                        check = false;
                        break;
                    }
                } catch (const std::out_of_range&) {
                    check = false;
                    break;
                }
            } else {
                check = false;
                break;
            }
        }
        
        if (check) {
            w = tmpw;
            h = tmph;
        }
    }
    
    vector<int> answer = {h, w};
    return answer;
}
