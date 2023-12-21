def init_fig(self):
    """Set initial parameters for drawing figure"""
    self.show_fig = False  # Show figure by matplotlib.pyplot.show
    # Save figure as self.filename where output format is deduced from the
    # extension of the filename
    self.save_fig = False
    self.fig_h_0to1 = False  # Change data of h=0 to h=1 for logarithmic plot
    self.data_only = False  # Plot data only
    self.have_new_plot = True

    # Size of the figure in inch
    self.fig_width = 4.3
    self.fig_height = 3.2
    self.fig_height_double = 4.7
    self.top_margin = 0.05
    self.bottom_margin = 0.12
    self.left_margin = 0.17  # Space for label is needed
    self.right_margin = 0.05
    self.hspace = 0.07

    # Axis
    self.log_x = True  # Logarithmic x axis
    self.min_x_log = 1  # Minimum of x axis in logrithmic scale
    # self.max_x = 10**4
    # self.max_y1 = 0.5
    # self.min_y2 = 10**(-12)
    self.max_y2_log = 5  # Maximum of K axis / maximum of K value

    # Marker
    self.marker = 'o'  # Select from https://matplotlib.org/stable/api/markers_api.html
    # See https://matplotlib.org/stable/gallery/color/named_colors.html
    self.color_marker = 'black'

    # Curves
    # Order of colors and styles
    self.color = ('red', 'blue', 'green', 'magenta', 'cyan', 'black')
    # See
    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    self.style = ['dashed', 'dashdot', 'solid', 'dotted']
    self.curve_smooth = 200  # Numbers of calculation points in a curve
    self.line_num = 0
    self.curves_ht = []
    self.curves_hk = []

    # Label of axis
    self.label_head = 'Matric head'
    self.label_theta = 'Volumetric water content'
    self.label_k = 'Hydraulic conductivity'

    # Legend
    self.legend = True
    self.show_r2 = True
    self.legend_fontsize = 10
    self.legend_loc = 'center right'
    self.legend_facecolor = 'white'
    self.legend_opacity = 1  # 0 = transparent, 1 = opaque
    self.data_legend = 'Measured'
    self.line_legend = 'Fitted'

    # Contour
    self.contour_level = 8
    self.contour_color = None  # specified by cmap. specify a color as 'black'
    self.contour_show_marker = True
    self.contour_marker_color = 'red'
    self.contour_smooth = 50
    self.contour_range_x = 0.3, 1.5
    self.contour_range_y = 0.5, 1.5
