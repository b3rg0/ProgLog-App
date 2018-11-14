#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 10/4;
    int d=c+2;
    switch(a){
        case 4: 
            std::cout << "c = " << 1 << std::endl;    
         break;

        case 10:
            std::cout << "c = " << 2 << std::endl;    
         break;

        case 5:
            std::cout << "c = " << 3 << std::endl;    
         break;

    }
    return 0;
}