## Python Templates

You can use the [editor on GitHub](https://github.com/anselm-baur/p1/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

![useful image](https://raw.githubusercontent.com/anselm-baur/python_templates/master/fig/plot.jpg)

### Required import packages
```python

import numpy as np
import matplotlib.pyplot as plt
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

Adjust plot range and the ticks.
```pyhton
x_scal = np.array([0.1,0.25])
y_scal = np.array([6.1,6.7])
```
```python
xmajor_ticks = np.arange(x_scal[0],x_scal[1]+0.01,(x_scal[1]-x_scal[0])/5)
xminor_ticks = np.arange(x_scal[0],x_scal[1],(x_scal[1]-x_scal[0])/50)

ymajor_ticks = np.arange(y_scal[0],y_scal[1]+0.001,(y_scal[1]-y_scal[0])/6)
yminor_ticks = np.arange(y_scal[0],y_scal[1],(y_scal[1]-y_scal[0])/60)
```
