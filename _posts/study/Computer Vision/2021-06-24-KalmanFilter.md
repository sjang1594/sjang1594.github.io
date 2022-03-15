---
title: Kalman Filter / Extended Kalman Filter
layout: post
category: study
tags: [c++, slam, computer vision]
---

Tracking is important in self-driving cars, this technique is crucial for estimating the state of a system. This is very similar to the probabilistic localization method(Monte Carlo localization). However, the difference in Kalman Filter estimates a continuous states whereas in Monte Carlo localization, it is forced to chop the world in the discrete places. As a result, the Kalman Filter happens to give us a uni-model distribution, whereas the Monte Carlo was fine with multi-model distributions. Both of these techniques are applicable to robot localization and tracking other vehicles.

### Definition of Kalman Filter

A Kalman filter gives us a mathematical way to infer velocity from only a set of measured locations. `The Kalman filter is used to estimate the state of a system when the measurement is noisy

### Kalman Filter - Common Types

* KF - linear
* EKF - nonlinear
* UKF(unscented Kalman filter) - highly nonlinear

### The Basis of the Kalman Filter

The basis of the Kalman Filter is the Gaussian Distribution.

```c++
#include <iostream>
#include <math.h>
using namespace std;
double calculateGaussian(double mu, double sigma2, double x){
 double prob = 1.0 / sqrt(2.0 * M_PI * sigma2) * exp(-.5 * pow((x-mu), 2.0) / sigma2);
    return prob;
}
int main(){
    cout << calculateGaussian(10.0, 4.0, 8.0) << endl;
 return 0;
}
```

The representation of Gaussian distribution gives

1. Predicted Motion
2. Sensor Measurement
3. Estimated State of Robot

### Measurement Updates

The prior belief + Measurement Updates will provide the posterior (with mean and the variance), which is also called new states. The two Gaussians will provide us with more information together than either Gaussian offered alone. As a result, the new state estimate is more confident than our prior belief and our measurement. This means that it has a higher peak(mean) and is narrower(variance).

```c++
#include <iostream>
#include <math.h>
#include <tuple>
using namespace std;
double new_mean, new_var;
tuple<double, double> measurement_update(double mean1, double var1, double mean2, double var2)
{
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2);
    new_var = 1 / (1 / var1 + 1 / var2); 
    return make_tuple(new_mean, new_var);
}
int main()
{
    tie(new_mean, new_var) = measurement_update(10, 8, 13, 2);
    printf("[%f, %f]", new_mean, new_var);
    return 0;
}
```

### State Prediction

The state prediction is the estimation that takes place after an inevitably uncertain motion. Since the measurement update and state prediction are an iterative cycle, it makes sense for us to continue where we left off. After taking into account the measurement, the posterior distribution can be calculated. However, since we've moved onto the state prediction step in the common filter cycle, this Gaussian is now referred to a s the prior belief.

Now robot's executes the command, "Move forward 7.5 meters". Calculating the new estimate is as easy as adding the mean of the motion to the mean of the prior, and similarly, adding the two variances together to produce the posterior estimates.

```c++
#include <iostream>
#include <math.h>
#include <tuple>
using namespace std;
double new_mean, new_var;
tuple<double, double> state_prediction(double mean1, double var1, double mean2, double var2)
{
    new_mean = mean1 + mean2;
    new_var =  var1 + var2;
    return make_tuple(new_mean, new_var);
}
int main()
{
    tie(new_mean, new_var) = state_prediction(10, 4, 12, 4);
    printf("[%f, %f]", new_mean, new_var);
    return 0;
}
```

### Implementation - 1D Kalman Filter

```c++
#include <iostream>
#include <math.h>
#include <tuple>
using namespace std;
double new_mean, new_var;
tuple<double, double> measurement_update(double mean1, double var1, double mean2, double var2)
{
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2);
    new_var = 1 / (1 / var1 + 1 / var2);
    return make_tuple(new_mean, new_var);
}
tuple<double, double> state_prediction(double mean1, double var1, double mean2, double var2)
{
    new_mean = mean1 + mean2;
    new_var = var1 + var2;
    return make_tuple(new_mean, new_var);
}
int main()
{
    //Measurements and measurement variance
    double measurements[5] = { 5, 6, 7, 9, 10 };
    double measurement_sig = 4;
    
    //Motions and motion variance
    double motion[5] = { 1, 1, 2, 1, 1 };
    double motion_sig = 2;
    
    //Initial state
    double mu = 0;
    double sig = 1000;
    for(int i = 0; i < sizeof(measurements) / sizeof(measurements[0]); i ++){
        tie(mu, sig) = measurement_update(mu, sig, measurements[i], measurement_sig);
        printf("update:  [%f, %f]\n", mu, sig);
        
        tie(mu, sig) = state_prediction(mu, sig, motion[i], motion_sig);
             printf("predict: [%f, %f]\n", mu, sig);
    }
    return 0;
}
```

### Advantage of Kalman Filter

How can the Kalman filter help us make better sense of our robot's current state?

* The Kalman filter can very quickly develop a surprisingly accurate estimate of the true value of the variable being measured. (e.g. robot's location in one dimensional world)
* Unlike other algorithms that require a lot of data to make an estimate, the Kalman filter is able to do so after just a few sensor measurements. It does so by using an initial guess and by taking into account the expected uncertainty of a sensor or movement.
* Let's say that my robot is using GPS data to identify its location. Today's GPS measurements are only accurate to a few meters. Sensor fusion uses the Kalman filter to calculate a more accurate estimate using data from multiple sensors.
