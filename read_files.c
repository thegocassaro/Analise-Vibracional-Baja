#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N_LINES 20000

int main(){

    FILE *f = fopen("data/ASSOALHO/1500-ASSOALHO.txt", "r");

    float* time = (float*)malloc(sizeof(float) * N_LINES);
    float* x = (float*)malloc(sizeof(float) * N_LINES);
    float* y = (float*)malloc(sizeof(float) * N_LINES);
    float* z = (float*)malloc(sizeof(float) * N_LINES);

    char* lixo;

    for(int i=0; i<3; i++){

        fscanf(f, "%f;", &time[i]);
        fscanf(f, "%[^=]", lixo);
        fscanf(f, "%f", &x[i]);
        fscanf(f, "%[^=]", lixo);
        fscanf(f, "%f", &y[i]);
        fscanf(f, "%[^=]", lixo);
        fscanf(f, "%f", &z[i]);

        printf("%f %f %f %f\n", time[i], x[i], y[i], z[i]);
    }
   
    fclose(f);

    free(time);
    free(x);
    free(y);
    free(z);

    return 0;
}