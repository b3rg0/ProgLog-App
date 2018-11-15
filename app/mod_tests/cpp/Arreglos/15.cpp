#include <iostream>

int main(int argc, char *argv[]) {
    int a [5],b[5];
    int v=3;
    std::cout << "a * b = [ ";
    for(int i=0;i<5;i++){        
    	a[i]=i+v;
    	b[i]=i-v;    
    	std::cout << a[i]*b[i] <<" ";
    }
    std::cout << "]";    
    
    return 0;
}