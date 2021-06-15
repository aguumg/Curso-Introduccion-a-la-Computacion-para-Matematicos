#include <iostream>
#include <string>
using namespace std;

bool esPrimo(int n){
int contador=2;
while (contador<n){		//Recorro todos los numeros menores que n y me fijo si alguno lo divide.
	if(n%i==0){
	return false;
	}
	contador=contador+1;
}
return true;
}

int cantidadPrimosMenoresOIguales(int n){
int i=2;
int j=0;
while (i<=n){			//Recorro todos los numeros menores o iguales que n, me fijo cuales son primos (usando la funcion anterior) y por cada primo sumo 1 en el contador.
	if(esPrimo(i)==true){
		j=j+1;
	}
	i=i+1;
}
return j;
}

int cantidadDivisoresPrimos(int n){
int i=2;
int j=0;
while(i<=n){
	if(esPrimo(i)==true){
		if(n%i==0){
			j=j+1;
		}
	}
	i=i+1;
}
return j;
}

int iesimoDivisorPrimo(int n, int i){ // -1 si n no tiene i divisores primos.
int j=2;
int k=0;
string a;
if(i<=cantidadDivisoresPrimos(n)){
	while(j<=n){			// Recorro todos los numeros menores o iguales que n y guardo en un string (c/u en la posicion k-esima) los primos divisores.
		if(esPrimo(j)==true){
			if(n%j==0){
				a[k]=j;
				k=k+1;
				}
			}
		j=j+1;
	}
return a[i-1]; // i-1 porque el string empieza en la poscion 0.
}
return -1;
}

int potencia(int x, int y){	//Defino la funcion auxiliar "potencia" que devuelve x^y. La voy a usar para definir potenciaIesimoDivisorPrimo.
int n=1;
while (y!=0){
	n=n*x;
	y=y-1;
	}
return n;
}

int potenciaIesimoDivisorPrimo(int n, int i){ // -1 si n no tiene i divs primos.
int j=1;
if(i<=cantidadDivisoresPrimos(n)){
	while(n%potencia(iesimoDivisorPrimo(n, i),j)==0){
		j=j+1;
	}
	return j-1;
	}
return -1;
}

int main(int argc, char* argv[]){
	/*Lo primero que hay que hacer es comparar el primer argumento ingresado con cada una de las funciones que tenemos*/

if (argv[1]=="esPrimo"){
	int n=atoi(argv[2]);
	if (esPrimo(n)==true){
		cout << "si" << "\n";
	}else {
		cout << "no" << "\n";
	}
}

if (argv[1]=="cantidadPrimosMenoresOIguales"){
	int n=atoi(argv[2]);
	cout << cantidadPrimosMenoresOIguales(n) << "\n";
}

if (argv[1]=="cantidadDivisoresPrimos"){
	int n=atoi(argv[2]);
	cout << cantidadDivisoresPrimos(n) << "\n";
}

if (argv[1]=="iesimoDivisorPrimo"){
	int n=atoi(argv[2]);
	int i=atoi(argv[3]);
	if(i<=cantidadDivisoresPrimos(n)){
	cout << iesimoDivisorPrimo(n,i) << "\n";
}else{
	cout << n << " no tiene " << i << " divisores primos" << "\n";
}
}

if (argv[1]=="potenciaIesimoDivisorPrimo"){
	int n=atoi(argv[2]);
	int i=atoi(argv[3]);
	if(i<=cantidadDivisoresPrimos(n)){
	cout << potenciaIesimoDivisorPrimo(n,i) << "\n";
}else{
	cout << n << " no tiene " << i << " divisores primos" << "\n";
}
}
return 0;
}
