#include <iostream>

int main(int argc, char *argv[]) {
    int a [5];
    int v=7;
    
    for(int i=0;i<5;i++){        
    	a[i]=v-i;        
    	v--;
    }
    
    std::cout << "a[v] = " << a[v] <<std::endl;  
    
    return 0;
}