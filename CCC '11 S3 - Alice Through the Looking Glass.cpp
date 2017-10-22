/**
 complete
 
#include <iostream>
using namespace std;
//link: https://dmoj.ca/problem/ccc11s3
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
    bool crystal[enterAmount];
    
    for (uint i = 0; i < enterAmount; i++) {
        cin>>m>>x>>y; // 2 4 4
        uint highestY = 0;
        for (int im = m; im > 0; im--) {
            uint oneTile = power(5, im-1); // check how big one tile is
            
            // check where x would be if it only the bigest tiles (divided into five)
            uint xPos = x/oneTile;
            highestY+=multipliers[xPos] * oneTile; // change tallest point
            if(multipliers[xPos] == 0){
                im=0; // if this section no longer goes up, end the loop
            }
            x = x%oneTile; // x gets everthing outside of the current tile removed
            
        }
        
        if(y<highestY){
            crystal[i] = true;
        }else{
            crystal[i] = false;
        }
        
    }
    
    for (uint i = 0; i < enterAmount; i++) {
        if(crystal[i]){
            cout<<"crystal\n";
        }else{
            cout<<"empty\n";
        }
    }
    return 0;
}
 **/
