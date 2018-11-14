#include <iostream>
int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/4;
    int d=a+c;

    switch(a){
        case 12: 
            std::cout << "d = " << 10 << std::endl;    
         break;

        case 13:
            std::cout << "d = " << 11 << std::endl;    
         break;

        default:
            std::cout << "d = " << 12 << std::endl;    
         break;
    }
    return 0;
}