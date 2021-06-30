# ann formulas

### notations
$$z^{(L)} = b^{(L)} +\sum_{n=0}^{x} w_{x}^{(L)} a_{x}^{(L-1)}$$
$$a^{(L)} = \sigma(z^{(L)})$$
$$C = (a^{(L_f)} - Y)^2$$

### nodges
$$\frac{\partial C}{\partial b^{(L)}} = \frac{\partial z^{(L)}}{\partial b^{(L)}} \frac{\partial a^{(L)}}{\partial z^{(L)}} \frac{\partial C}{\partial a^{(L)}}$$
$$\frac{\partial C}{\partial a^{(L)}} = 2(a^{(L)} - y)$$
$$\frac{\partial a^{(L)}}{z^{(L)}} = \sigma\prime(z^{(L)})$$
$$\frac{\partial z^{(L)}}{\partial w^{(L)}} = a^{(L-1)}$$
$$\frac{\partial C}{\partial b^{(L)}} = 2(a^{(L)} - y) \times\sigma\prime(z^{(L)})\times a^{(L-1)}$$