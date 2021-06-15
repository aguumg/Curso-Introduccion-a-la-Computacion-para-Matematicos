#include <iostream>
#include <string>
using namespace std;

int main(int argc, char* argv[]){
cout << "\t" << "Millas " << "\t\t" <<"Kilometros" << "\n";
int mill=0;
int km=0;
while (mill<=100){
	cout << "\t" << mill << " \t\t " << km << "\n";
	mill=mill+10;
	km=mill*1.61;
	}
cout << "\n" << "\t" << "Kilometros " << "\t" <<"Millas" << "\n";
mill=0;
km=0;
while (km<=100){
	cout << "\t" << km << " \t\t " << mill << "\n";
	km=km+10;
	mill=km/1.61;
	}
return 0;
}
