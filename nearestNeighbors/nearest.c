#include<stdio.h>
#include<math.h>

int main() {
    
    FILE* train = fopen("../TAdrop/train.txt", "r");
    double tr[800][229];
    int i, j, k;    

    for(i = 0; i < 800; ++i) {
        tr[i][228] = 0;
        for(j = 0; j < 228; ++j) {
            fscanf(train, "%lf", &tr[i][j]);    
            tr[i][228] += tr[i][j]*tr[i][j];
        }
    }
    fclose(train);

    FILE* test = fopen("../TAdrop/test.txt", "r");
    double te[200][229];

    for(i = 0; i < 200; ++i) {
        te[i][228] = 0;
        for(j = 0; j < 228; ++j) {
            fscanf(test, "%lf", &te[i][j]);
            te[i][228] += te[i][j]*te[i][j];
        }
    }
    fclose(test);
    
    int one = 0;            //test
    int two = 0;            //test

    int r_i = 0;            //record index
    double min_a = 0;       //minimum angle
    FILE* output = fopen("./test_out", "w"); 
    for(i = 0; i < 200; ++i){
        r_i = 0;
        min_a = 0;
        for (j = 0; j < 800; ++j) {
            double dot = 0;
            double cosa = 0;
            for (k = 0; k < 228; ++k) {
                dot += te[i][k]*tr[j][k];
            }
            cosa = (dot*dot) / (te[i][228]*tr[j][228]);
            if ((cosa-min_a) > 0) {
                r_i = j;
                min_a = cosa;
            }
        }
        
        if (r_i < 400) {
            fputs("1\n", output);
            one++;
        } else {
            fputs("2\n", output);
            two++;
        }
    }
    fclose(output);
    printf("1:%d, 2:%d\n", one ,two);
    return 0;
}
