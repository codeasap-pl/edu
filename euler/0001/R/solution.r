# run: Rscript solution.r

sum = 0;
for(i in 1:1000 - 1) {
    if(i %% 3 == 0 || i %% 5 == 0) {
        sum = sum + i;
    }
}

print(sum);
