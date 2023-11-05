#include <math.h>
#include <stdio.h>

double func_f(double x) {
  return cos(pow(1.7,(x+1)) - 2.7);
}

double func_g(double x) {
  return pow(2,x) + pow(x,2) - 2;
}

double func_a_ij(double i, double m) {
  double sum = 0.0;
  double j = 1.0;
  while(j <= m){
      sum += func_f(i) + func_g(j);
      j++;
  }
  return fabs(sum);
}

double func_n_a(double m, double n){
  m = fmin(m, n);
  double max_value = 0.0;

  for (double i = 0.0; i <= m; i++) {
    max_value = fmax(max_value, func_a_ij(i,m));
  }
  return max_value;
}
