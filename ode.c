//Solucion de ODEs
// Andrea Rozo

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

//Euler

float derivada (float x, float y);

int main ()
{
	float h = 0.2;
	int n_points = (1.0+h)/h;
	float *y;
	float *x;
	int i;
	float y_prima;
	y = malloc(n_points*sizeof(float));
	x = malloc(n_points*sizeof(float));
	
	if (!y && !x)
	{
		printf("Error al crear los vectores");
		exit(1);
	}
	
	y[0] = 0;
	for (i = 1;i < n_points;i++)
	{
		y_prima = derivada(x[i-1],y[i-1]);
		x[i] = x[i-1]+h;
		y[i] = y[i-1]+h*y_prima;
	}
}

float derivada (float x, float y)
{
	return (1.0 + pow(y,2));
}
