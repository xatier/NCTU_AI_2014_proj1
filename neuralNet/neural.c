#include<stdio.h>
#include<math.h>

int main(){

    FILE* train = fopen("train.txt", "r");
    double t[800][229], w[228];
    double label[2] = {0, 1};
    int i, j, k = 0;

    for(i = 0 ; i < 800 ; i++){
        t[i][228] = 0;
        for(j = 0 ; j < 228 ; j++){
            fscanf(train, "%lf", &t[i][j]);
            t[i][228] += t[i][j];
        }
    }

    for(i = 0 ; i < 800 ; i++)
        for(j = 0 ; j < 228 ; j++)
            t[i][j] /= t[i][228];

    //weight init
    for(j = 0 ; j < 228 ; j++)
        w[j] = 1.0;

    //learning
    for(i = 0 ; i < 800 ; i=(i+1)%800){
        double in = 0;
        for(j = 0 ; j < 228 ; j++)
            in -= t[i][j]*w[j];
        double g = 1/(1+exp(in));

        if(k < 800*800*10)//learing progress
            k++;
        else
            break;

        if(label[i/400] == 0 && g <= 0.5)
            continue;
        else if(label[i/400] == 1 && g > 0.5)
            continue;

        k -= 2;//not correct
        double Err = label[i/400] - g;
        for(j = 0 ; j < 228 ; j++)
            w[j] += 0.01*Err*g*(1-g)*t[i][j];//adjust weight

    }

    //run training data
    k = 0;
    for(i = 0 ; i < 800 ; i++){
        double in = 0;
        for(j = 0 ; j < 228 ; j++)
            in -= t[i][j]*w[j];
        double g = 1/(1+exp(in));

        if(label[i/400] == 0 && g <= 0.5)
            k++;
        else if(label[i/400] == 1 && g > 0.5)
            k++;
    }

    printf("%d correct\n", k);
    return 0;
}
