#include <iostream>

int main(int argc, char *argv[]) {
    int a=5;
    int b=0;

    while(a>0){
        a-=b;
    }
    std::cout << "a = " << a << std::endl;    

    return 0;
}