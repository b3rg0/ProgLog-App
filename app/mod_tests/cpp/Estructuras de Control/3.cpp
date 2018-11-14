#include <iostream>

int main(int argc, char *argv[]) {
    int a = 10, b = 5;
    int c = 2 + 2;
    b= a + 2;
    
    if(a < 0){
    	std::cout << "c = " << c << std::endl;
    }
    else{
    	std::cout << "b = " << b << std::endl;	
    }
    	
    
    return 0;
}
