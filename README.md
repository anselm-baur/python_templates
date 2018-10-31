## Python Templates

Simple and nice plot and fit template for single data points.

![useful image](https://raw.githubusercontent.com/anselm-baur/python_templates/master/fig/plot.jpg)

### Required import packages
```python

import numpy as np
import matplotlib.pyplot as plt
```

### Insert data points
```python
x_data = np.array([39674,35656,32512,29436,27052,23805,21511,20335,18657,16621,15119,13358,12764,11604,10402,9646])
y_data = np.array(np.arange(0.14,0.22,0.005))
```
Process data points for analysis
```python
x_raw = x_data
y_raw = np.log(N*y_data**2)
y_err = delta
```


### Fit the data points
Define the fit function with fit parameters a, b, c, ...

```python
def func(x, a, b):
    return(a*x+b)
```

Fit the data points and get the error of the fit parameters.
```python
popt_1, pcov_1 = curve_fit(func, x_raw, y_raw,sigma=y_err)
a_1 = round(popt_1[0], 4)
b_1 = round(popt_1[1], 4)
perr_1 = np.sqrt(np.diag(pcov_1))
```

### Print the data points and the fit

Adjust plot range and the number of ticks.
```pyhton
x_scal = np.array([0.1,0.25])
y_scal = np.array([6.1,6.7])

# Number of ticks of each axes
x_num_major_tick = 5
y_num_major_tick = 6
```


### Save plot

Use image format *.eps for vector graphics
```python
fig.savefig('fig/plot.eps')
```
