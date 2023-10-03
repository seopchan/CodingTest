#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    unordered_map<string, int> pla;
    for (int i = 0; i < players.size(); i++) {
        pla[players[i]] = i;
    }
    
    for (const string& call: callings) {
        if (pla.find(call) != pla.end()) {
            int n = pla[call];
            
            if (n > 0) {
                string tmp = players[n-1];
                players[n-1] = players[n];
                players[n] = tmp;
                
                pla[players[n]] = n;
                pla[players[n-1]] = n-1;
            }
        }
    }
    
    return players;
}