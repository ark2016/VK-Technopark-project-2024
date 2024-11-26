#include <iostream>
using namespace std;

class Example {
public:
    void greet() {
        cout << "Hello, World!" << endl;
    }
};

int main() {
    Example ex;
    ex.greet();
    return 0;
}
