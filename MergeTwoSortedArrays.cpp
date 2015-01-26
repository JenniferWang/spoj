#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>

#define MAXLENGTH 10

using namespace std;

// If two sorted arrays are of the same size
int find_median(vector<int> &arr1, vector<int> &arr2){
  int l1 = 0, r1 = arr1.size() - 1, l2 = 0, r2 = arr2.size();
  while (r1 - l1 > 1){
    int m1 = (l1 + r1) / 2;
    int m2 = (l2 + r2) / 2;
    if (arr1[m1] == arr2[m2])
      return arr1[m1];
    if (arr1[m1] > arr2[m2]){
      r1 = m1 - 1;
      l2 = m2 + 1;
    }
    else{
      l1 = m1;
      r2 = m2;
    }
  }
  cout << "l1 is "<< l1 << " r1 is "<< r1<<endl;
  cout << "l2 is "<< l2 << " r2 is "<< r2<<endl;
  return ((max(arr1[l1], arr2[l2]) + min(arr1[r1], arr2[r2])) / 2);
}

// input format:
//  num_testcase 
//  size_of_array
//  a b c d ..... array1
//  a b c d ..... array2
int main(int argc, char* argv[]){
  int val;
  int num_tests;
  int array_size;
  vector <int> arr1;
  vector <int> arr2;
  cin >> num_tests;
  for (int i = 0; i < num_tests; i ++){
    cin >> array_size;
    for (int j = 0; j < array_size; j ++){
      cin >> val;
      arr1.push_back(val);
    }
    for (int j = 0; j < array_size; j ++){
      cin >> val;
      arr2.push_back(val);
    }
  }
  cout << find_median(arr1, arr2)<<endl;
  return 0;
}