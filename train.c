#include<stdio.h>

int main(){

    //FILE* tl = fopen("train_label.txt", "r");
    FILE* t = fopen("train.txt", "r");
    //FILE* foo = fopen("foo.txt", "w");
    int i, j, ac = 0, bc = 0;
    double m[800][229], a[228], b[228];

    for(i = 0 ; i < 800 ; i++){
        m[i][228] = 0;
        for(j = 0 ; j < 228 ; j++){
            fscanf(t, "%lf", &m[i][j]);
            m[i][228] += m[i][j];
        }
    }

    for(i = 0 ; i < 800 ; i++)
        for(j = 0 ; j < 228 ; j++)
            m[i][j] /= m[i][228];

    for(i = 0 ; i < 228 ; i++){
        a[i] = 0;
        for(j = 0 ; j < 400 ; j++)
            a[i] += m[j][i];
        a[i] /= 400;
    }
    
    for(i = 0 ; i < 228 ; i++){
        b[i] = 0;
        for(j = 400 ; j < 800 ; j++)
            b[i] += m[j][i];
        b[i] /= 400;
    }

    for(i = 0 ; i < 800 ; i++){
        double asum = 0, bsum = 0;
        for(j = 0 ; j < 228 ; j++){
            asum += (m[i][j] - a[j])*(m[i][j] - a[j]);
            bsum += (m[i][j] - b[j])*(m[i][j] - b[j]);
        }
        if(asum < bsum)
            ac++;
        else if(asum > bsum)
            bc++;
    }

    printf("%d %d\n", ac, bc);
    
    //fclose(foo);
    fclose(t);
    return 0;
}
