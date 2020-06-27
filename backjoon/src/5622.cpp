/*
 * 5622.cpp
 *
 *  Created on: 2020. 6. 28.
 *      Author: minjae
 */

#include <iostream>

using namespace std;

int main(){
//	char a = 'D';
//	cout << ((int)a-59)/3 ;

	for(char a = 'A'; a <= 'Z'; a++){
		cout << a;
		cout << ((int)a - 59)/3 << endl;
	}
}


