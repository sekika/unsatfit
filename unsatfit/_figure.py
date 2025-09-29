import numpy as np


def set_scale(self):
    x1, y1 = self.swrc
    if self.log_x:
        self.min_x = self.min_x_log
        if hasattr(self, 'max_x'):
            self.max_x = max(self.max_x, max(x1) * 1.5)
        else:
            self.max_x = max(x1) * 1.5
    else:
        self.min_x = min(0, min(x1) * 0.85)
        try:
            self.max_x
        except AttributeError:
            self.max_x = max(x1) * 1.05
    self.min_y1 = 0
    if not hasattr(self, 'max_y1'):
        self.max_y1 = max(y1) * 1.15
    if not self.ht_only:
        x2, y2 = self.unsat
        if hasattr(self, 'min_y2'):
            self.min_y2 = min(self.min_y2, min(y2) * 0.2)
        else:
            self.min_y2 = min(y2) * 0.2
        self.max_y2 = max(y2) * self.max_y2_log


def add_curve(self):
    import math
    self.set_scale()
    color = self.color[self.line_num % len(self.color)]
    style = self.style[self.line_num % len(self.style)]
    if self.log_x:
        x = 2**np.linspace(math.log2(self.min_x),
                           math.log2(self.max_x), num=self.curve_smooth)
    else:
        x = np.linspace(self.min_x, self.max_x, num=self.curve_smooth)
    if self.ht_only:
        self.curves_ht.append({'data': (x, self.f_ht(
            self.fitted, x)), 'color': color, 'style': style, 'legend': self.line_legend})
    else:
        self.curves_ht.append({'data': (x, self.f_ht(self.p_ht(
            self.fitted), x)), 'color': color, 'style': style, 'legend': self.line_legend})
        self.curves_hk.append({'data': (x, self.f_hk(
            self.fitted, x)), 'color': color, 'style': style, 'legend': self.line_legend})
    self.line_num += 1


def clear_curves(self):
    self.curves_ht = []
    self.curves_hk = []
    self.line_num = 0


def h_0to1(self, data):
    if not self.fig_h_0to1:
        return data
    x, y = data
    x = np.where(x == 0, 1, x)
    return (x, y)


def plot(self, pore_segment=False):
    import matplotlib.pyplot as plt  # type: ignore
    import matplotlib.ticker as ticker  # type: ignore

    if self.data_only:
        self.set_scale()

    def draw_segment(ax, data, label):
        x, y = data
        macro_max = self.pore_minima[0]
        meso_max = self.pore_minima[1]
        mask = [x <= macro_max, (x > macro_max) & (
            x <= meso_max), x > meso_max]
        for i in range(3):
            ax.plot(
                x[mask[i]],
                y[mask[i]],
                color=self.pore_color[i],
                linestyle=self.pore_style[i],
                label=label[i],
                lw=2.3,
                zorder=4)
        ax.axvline(macro_max, color='k', ls='--', lw=1, alpha=0.5)
        ax.axvline(meso_max, color='k', ls='--', lw=1, alpha=0.5)

    # Set subplots
    if self.ht_only:
        fig, ax1 = plt.subplots(figsize=[self.fig_width, self.fig_height])
    else:
        fig, (ax1, ax2) = plt.subplots(2, figsize=[
            self.fig_width, self.fig_height_double])
    fig.subplots_adjust(
        top=1 - self.top_margin,
        bottom=self.bottom_margin,
        right=1 - self.right_margin,
        left=self.left_margin,
        hspace=self.hspace)

    if pore_segment:
        self.find_pore_extreme(self.fitted, epsilon=1e-6)
        if len(self.pore_minima) != 2:
            print(
                f'Pore segmentation failed; it has {len(self.pore_minima)} minima, not 2.')
            pore_segment = False

    # Draw plots, curves and legends
    ax1.plot(*self.h_0to1(self.swrc), color=self.color_marker, marker=self.marker,
             linestyle='', label=self.data_legend)
    if not self.data_only:
        if self.have_new_plot:
            self.add_curve()
        for curve in self.curves_ht:
            if pore_segment:
                draw_segment(
                    ax1, curve['data'], self.pore_label)
            else:
                ax1.plot(*curve['data'], color=curve['color'],
                         linestyle=curve['style'], label=curve['legend'])
        if not self.ht_only:
            ax2.plot(*self.h_0to1(self.unsat), color=self.color_marker,
                     marker=self.marker, linestyle='', label='_nolegend_')
            for curve in self.curves_hk:
                if pore_segment:
                    draw_segment(
                        ax2, curve['data'], ['_nolegend_'] * 3)
                else:
                    ax2.plot(*curve['data'], color=curve['color'],
                             linestyle=curve['style'], label='_nolegend_')
        if hasattr(self, 'fp'):
            leg = fig.legend(loc=self.legend_loc, prop=self.fp,
                             facecolor=self.legend_facecolor)
        else:
            leg = fig.legend(
                loc=self.legend_loc, fontsize=self.legend_fontsize, facecolor=self.legend_facecolor)
        leg.get_frame().set_alpha(self.legend_opacity)

    # Draw scale
    if self.log_x:
        ax1.set_xscale("log")
    ax1.axis([self.min_x, self.max_x, self.min_y1, self.max_y1])
    if not self.ht_only:
        ax1.xaxis.set_major_formatter(ticker.NullFormatter())
        ax2.axis([self.min_x, self.max_x, self.min_y2, self.max_y2])
        if self.log_x:
            ax2.loglog(base=10)
        else:
            ax2.set_yscale = ("log")
            ax2.xaxis.set_major_formatter(ticker.ScalarFormatter())

    # Draw labels
    if self.ht_only:
        ax1.set_xlabel(self.label_head)
    else:
        ax2.set_xlabel(self.label_head)
    ax1.set_ylabel(self.label_theta)
    if not self.ht_only:
        ax2.set_ylabel(self.label_k)

    # Show and/or save figure
    if self.save_fig:
        plt.savefig(self.filename)
    if self.show_fig:
        plt.show()
    plt.close()
