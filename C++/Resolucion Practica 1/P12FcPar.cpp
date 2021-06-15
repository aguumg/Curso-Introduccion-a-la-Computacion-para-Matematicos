#include <iostream>
#include <string>
using namespace std;

/* Creo las funciones que devuelven hasta la fila i-esima de la conversion*/

void milltokm_fila(int i){
cout << "\t" << "Millas " << "\t\t" <<"Kilometros" << "\n";
int mill=0;
int km=0;
while (mill<=10*(i-1)){
	cout << "\t" << mill << " \t\t " << km << "\n";
	mill=mill+10;
	km=mill*1.61;
	}
}
void kmtomill_fila(int i){
cout << "\n" << "\t" << "Kilometros " << "\t" <<"Millas" << "\n";
int mill=0;
int km=0;
while (km<=10*(i-1)){
	cout << "\t" << km << " \t\t " << mill << "\n";
	km=km+10;
	mill=km/1.61;
	}
}

/*El programa recibe 2 parámetros i,j, con:
	i=numero de fila de milltokm
	j=numero de fila de kmtomill	*/

int main(int argc, char* argv[]){
milltokm_fila(atoi(argv[1]));
kmtomill_fila(atoi(argv[2]));
return 0;
}
