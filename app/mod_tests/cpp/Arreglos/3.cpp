#include <iostream>

int main(int argc, char *argv[]) {
    int a [5];
    int v=7;
    std::cout << "a = [ ";
    for(int i=0;i<5;i++){        
    	a[i]=v-i;    
    	std::cout << a[i] <<" ";
    }
    std::cout << "]";    
    
    return 0;
}