#include <iostream>
using namespace std;

uint power(uint num, int toPowOf){
    uint mult = num;
    if(toPowOf == 0){
        return 1;
    }else if (toPowOf == 1){
        return num;
    }
    for (int i = 1; i < toPowOf; i++) {
        num = num*mult;
    }
    return num;
}

int main(int argc, const char * argv[]) {
    
    int multipliers[5] = {0,1,2,1,0};
    uint enterAmount = 0; //
    uint m = 0;//1-13
    uint x = 0;
    uint y = 0;
    
    cin>>enterAmount;
    for (uint i = 0; i < enterAmount; i++) {
        cin>>m>>x>>y; // 2 4 4
        long long highestY = 0;
        for (uint im = 0; im < m; im++) {
            uint max = power(5, m-im-1);
            uint xPos = x/max;
            highestY+=multipliers[xPos] * max;
            x = x%max;
        }
        
        if(y<highestY){
            cout<<"crystal\n";
        }else{
            cout<<"empty\n";
        }
        
    }
    
    
    return 0;
}
