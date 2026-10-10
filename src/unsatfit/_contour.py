def contour(self, x_name, y_name):
    """Contour of RMSE"""
    import numpy as np
    import matplotlib.pyplot as plt
    from .unsatfit import Fit

    # Set data and residual function
    param = self.model[self.model_name.replace('Modified ', '')]['param']
    if self.ht_only:
        data = self.swrc
        par = list(self.fitted)
        for c in self.const_ht:
            par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
        for i in sorted(self.model_k_only, reverse=True):
            param = param[:i] + param[i + 1:]
    else:
        data = self.unsat
        par = list(self.fitted)
        for c in self.const:
            par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    const = []
    for i in range(len(par)):
        const.append([i + 1, par[i]])
    xi = param.index(x_name)
    yi = param.index(y_name)
    x = par[xi]
    y = par[yi]
    for i in sorted((xi, yi), reverse=True):
        const = const[:i] + const[i + 1:]

    f = Fit()
    if 'Modified' in self.model_name:
        f.set_model(self.model_name.replace('Modified ', ''), const=const)
        f.modified_model(self.hs)
    else:
        f.set_model(self.model_name, const=const)
    if self.ht_only:
        residual = f.residual_ht
    else:
        residual = f.residual_log10_hk

    # Make grid of (X,Y)
    x_min, x_max = self.contour_range_x
    y_min, y_max = self.contour_range_y
    x_delta = (x_max - x_min) / self.contour_smooth
    y_delta = (y_max - y_min) / self.contour_smooth
    x_grid = np.arange(x * x_min, x * x_max, x * x_delta)
    y_grid = np.arange(y * y_min, y * y_max, y * y_delta)
    X, Y = np.meshgrid(x_grid, y_grid)

    # Calculate RMSE for (X,Y) as Z
    z = []
    for yi in y_grid:
        row = []
        for xi in x_grid:
            mse = np.average(residual((xi, yi), *data)**2)
            row.append(mse ** 0.5)
        z.append(row)
    Z = np.array(z)

    # Draw contour of (X,Y,Z)
    fig, ax = plt.subplots(figsize=[self.fig_width, self.fig_height])
    fig.subplots_adjust(top=1 - self.top_margin, bottom=self.bottom_margin,
                        right=1 - self.right_margin, left=self.left_margin)
    CS = ax.contour(X, Y, Z, self.contour_level, colors=self.contour_color)
    ax.set_xlabel(self.label(x_name))
    ax.set_ylabel(self.label(y_name))
    ax.clabel(CS, inline=True, fontsize=10)

    if self.contour_show_marker:
        ax.plot(x, y, color=self.contour_marker_color,
                marker='o', linestyle='')

    if self.save_fig:
        plt.savefig(self.filename)
    if self.show_fig:
        plt.show()


def label(self, name):
    label = '$' + name + '$'
    for i in [['qs', '\\theta_s'], ['qr', '\\theta_r'], ['hb', 'h_b'], ['hm2', 'h_{m2}'], [
            'hm', 'h_m'], ['Ks', 'K_s'], ['sigma', '\\sigma'], ['1', '_1'], ['2', '_2']]:
        label = label.replace(i[0], i[1])
    return label
