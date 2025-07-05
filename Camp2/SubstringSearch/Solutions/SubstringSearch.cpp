
#include <iostream>
#include <string>

using namespace std;

int main() {
  string text, pattern;
  getline(cin, text);
  getline(cin, pattern);

  size_t found = text.find(pattern);
  if (found != string::npos) {
    cout << found << endl;
  } else {
    cout << -1 << endl;
  }

  return 0;
}