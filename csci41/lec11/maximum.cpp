#include <iostream>
#include <string>
#include <list>
using namespace std;

template <class T> // this line introduces a type variable
T maximum(T a, T b) {
  if (a > b) return a;
  else return b;
}

int main() {
  cout << maximum<int>(42, 43) << endl; 
  cout << maximum(3.14, 2.71) << endl; // C++ can infer that we want maximum<double> here
  cout << maximum<string>("abc", "bcd") << endl; 

  list<int> l = {1, 2, 3};
  list<int> l2 = {2, 3, 4};
  list<int> l3 = maximum(l, l2);
  for (int x : l3) {
    cout << x << " ";
  }
  cout << endl;

  return 0;
}
