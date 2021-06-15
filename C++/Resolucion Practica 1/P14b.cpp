#include <iostream>
#include <string>
#include <array>
using namespace std;
/*int potencia(int x, int y){
int n=1;
while (y!=0){
	n=n*x;
	y=y-1;
	}
return n;
}
int largo_array(int x){
int i=1;
while (potencia(15,i)<=x){
	i = i+1;
	}
return i;
}
*/

int main(int argc, char* argv[]){
int x=10;
int i=0;
string aux={'A', 'B', 'C', 'D', 'E', 'F'};
string a;
while (x>=15){
	if(x%15<10){
		a[i]=x%15;
		}
		else{
			a[i]=aux[x%15-10];
			}
	i=i+1;
	x=x/15;
	}
if(x<10){
	a[i]=x;
	}
	else{
		a[i]=aux[x-10];
		};
i=0;
while (i<=a.size()){
	cout << a[i];
	i=i+1;
	}
cout << "\n";		/*ERROR: para 10<=x<=15 devuelve cualquier cosa*/
return 0;
}
