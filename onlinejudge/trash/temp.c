#include<bits/stdc++.h>
using namespace std;

bool checkPattern(string s) {
    string patterns[] = {"ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"};
    for (const string& pattern : patterns) {
        if (s == pattern) {
            return true;
        }
    }
    return false;
}

int main() {
    string S;
    cin >> S;
//  individual nahi ek arrray hi pass kar diya

    if (checkPattern(S)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
