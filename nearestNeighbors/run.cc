#include<cstdio>
#include<cmath>

int main (void) {

    FILE* train = std::fopen("../TAdrop/train.txt", "r");
    double tr[800][229];
    int i, j, k;

    for(i = 0; i < 800; ++i) {
        tr[i][228] = 0;
        for(j = 0; j < 228; ++j) {
            std::fscanf(train, "%lf", &tr[i][j]);
            tr[i][228] += tr[i][j]*tr[i][j];
        }
    }
    std::fclose(train);

    FILE* test = std::fopen("../TAdrop/train.txt", "r");
    double te[800][229];

    for(i = 0; i < 800; ++i) {
        te[i][228] = 0;
        for(j = 0; j < 228; ++j) {
            std::fscanf(test, "%lf", &te[i][j]);
            te[i][228] += te[i][j]*te[i][j];
        }
    }
    std::fclose(test);

    int one = 0;            //test
    int two = 0;            //test
    int one_ = 0;
    int two_ = 0;

    int r_i = 0;            //record index
    double min_a = 0;       //minimum angle
    FILE* output = stdout;
    for(i = 0; i < 800; ++i) {
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


        if (i < 400) {
            if (r_i < 400)
                one++;
            else
                one_++;
        }
        else {
            if (r_i < 400)
                two_++;
            else
                two++;
        }
    }
    //std::fclose(output);
    std::puts("= confusion matrix =");
    std::printf("1:%d, 2:%d\n", one ,two);
    std::printf("1x:%d, 2x:%d\n", one_ ,two_);
    std::puts("====================");
    return 0;
}
