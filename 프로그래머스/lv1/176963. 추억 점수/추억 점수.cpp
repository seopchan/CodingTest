#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    unordered_map<string, int> um;
    
    for (int i=0; i<name.size(); i++) {
        um.insert({name[i], yearning[i]});
    }
    
    vector<int> answer;
    for (int i=0; i<photo.size(); i++) {
        vector<string> pname = photo[i];
        int sum = 0;
        
        for (int j=0; j < pname.size(); j++) {
            if (um.find(pname[j]) != um.end()) {
                sum += um.at(pname[j]);        
            }
        }
        answer.push_back(sum);
    }
    
    return answer;
}