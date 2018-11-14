#include <iostream>
int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/4;
    int d=c+2;
    switch(c){
        case 2: 
            std::cout << "d = " << 4 << std::endl;    
         break;

        case 5:
            std::cout << "d = " << 5 << std::endl;    
         break;

        default:
            std::cout << "d = " << 3 << std::endl;    
         break;
    }
    return 0;
}