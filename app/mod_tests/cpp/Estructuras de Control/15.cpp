#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/4;
    int d=c+3;
    switch(d){
        case 6: 
            std::cout << "c = " << 1 << std::endl;    
         break;

        case 13:
            std::cout << "c = " << 2 << std::endl;    
         break;

        case 5:
            std::cout << "c = " << 3 << std::endl;    
         break;

    }
    return 0;
}