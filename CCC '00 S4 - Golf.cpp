//
//  CCC '00 S4 - Golf.cpp
//  link: https://dmoj.ca/problem/ccc00s4

#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

struct node{
    
    node(int getHere, int distance){
        this->getHere = getHere;
        this->distance = distance;
        total = getHere+distance;
    }
    
    int getHere;
    int distance;
    int total;
};

vector<node*> openNodes;
vector<int> clubs;

node* openNode(int id){
    //open id
    for (int i = 0; i < clubs.size(); i++) {
        if(openNodes[id]->distance-clubs[i]>=0){ // not out of range
            node*newNode = new node(openNodes[id]->getHere+1, openNodes[id]->distance-clubs[i]);
            openNodes.push_back(newNode);
            if(newNode->distance == 0){
                return newNode; // found the best path
            }
        }
        
    }
    
    delete openNodes[id];
    openNodes.erase(openNodes.begin()+id);
    
    if(openNodes.size()==0){
        return new node(-1,-1); // there are no more open nodes
    }
    
    int lowestCostNode = 0;
    
    for (int i = 1; i < openNodes.size(); i++) {
        if(openNodes[lowestCostNode]->total > openNodes[i]->total){
            // this may be wrong
            lowestCostNode = i;
        }
    }
    return openNode(lowestCostNode);
}

int main(){
    int amountOfClubs;
    int disFrom;
    cin>>disFrom>>amountOfClubs;
    
    
    for (int i = 0; i < amountOfClubs; i++) {
        int clubDis;
        cin>>clubDis;
        clubs.push_back(clubDis);
    }
    
    node*firstNode = new node(0, disFrom);
    openNodes.push_back(firstNode);
    
    node* finalID = openNode(0);
    
    if(finalID->getHere!=-1){
        
        cout<<"Roberta wins in "<<finalID->getHere<<" strokes."<<endl;
    }else{
        cout<<"Roberta acknowledges defeat."<<endl;
    }
}
