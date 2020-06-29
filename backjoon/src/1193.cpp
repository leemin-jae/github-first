/*
 * 1193.cpp
 *
 *  Created on: 2020. 6. 29.
 *      Author: minjae
 */

#include <iostream>

using namespace std;

//int main(){
//	int a;
//	cin >> a;
//	int tmp = 1;
//	int tmp2 = 3;
//	int i = 0;
//	while(!(tmp<=a && a<=tmp2)){
//		i++;
//		tmp = tmp + ((i-1)*4+3);
//		tmp2 = tmp2 +(i*4+3);
//	}
//	int pi = (tmp+tmp2)/2;
//	if(a < pi){
//		cout << (2*(i+1)-1) - (a-tmp) << "/" << 1+(a-tmp);
//	}
//	else{
//		cout << (2*(i+1)) - (tmp2-a) << "/" << 1+(tmp2-a);
//	}
//
//}

int main() {
	int X;
	cin>>X;

	int a = 0;
	int i = 1;
	for(; a<X; i++){
		a+=i;
	}
	i--;
	int numerator;
	int denominator;
	int t = a-X;
	if(i%2 == 1){
		numerator = 1+t;
		denominator = i-t;
	}
	else{
		numerator = i-t;
		denominator = 1+t;
	}

	cout<<numerator<<"/"<<denominator<<'\n';
}
