from gi.repository import Gtk, Adw
import copy
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.backends.backend_gtk4agg import (
    FigureCanvasGTK4Agg as FigureCanvas)
from matplotlib.backends.backend_gtk4 import (
    NavigationToolbar2GTK4 as NavigationToolbar)
from . import datman
from matplotlib.widgets import SpanSelector
from cycler import cycler
import matplotlib.font_manager

def define_highlight(self, span=None):
    self.highlight = SpanSelector(
        self.canvas.figure.axes[0],
        on_select,
        "horizontal",
        useblit=True,
        props=dict(alpha=0.3, facecolor = "tab:blue", linewidth = 0),
        handle_props=dict(linewidth=0),
        interactive=True,
        drag_from_anywhere=True)
    if span is not None:
        self.highlight.extents = span
    self.highlight.set_visible(True)
    self.highlight.set_active(True)

def on_select(self, xmin):
    pass

def hide_highlight(self):
    win = self.props.active_window
    button = win.select_data_button
    self.highlight.set_visible(False)
    self.highlight.set_active(False)
    button.set_active(False)

def toggle_highlight(shortcut, _, self):
    win = self.props.active_window
    button = win.select_data_button
    if self.highlight == None:
        define_highlight(self)
    if button.get_active():
        hide_highlight(self)
    else:
        button.set_active(True)
        self.highlight.set_visible(True)
        self.highlight.set_active(True)
    self.canvas.draw()


def plot_figure(self, canvas, X, Y, filename="", xlim=None, linewidth = 2, title="", scale="log",marker=None, linestyle="solid",
                     revert = False, color = None, marker_size = 10):
    fig = canvas.ax
    linewidth = linewidth
    line = fig.plot(X, Y, linewidth = linewidth ,label=filename, linestyle=linestyle, marker=marker, color = color, markersize=marker_size)
    if self.preferences.config["plot_legend"]:
        fig.legend()
    return line

def set_canvas_limits(self, canvas, limits = {"xmin":None, "xmax":None, "ymin":None, "ymax":None}):
    graph_limits = find_limits(self)
    for key, item in limits.items():
        if item is not None:
            graph_limits[key] = item

    span = (graph_limits["xmax"] - graph_limits["xmin"])
    if self.canvas.ax.get_xscale() == "linear":
        graph_limits["xmin"] -= 0.015*span
        graph_limits["xmax"] += 0.015*span
    if self.canvas.ax.get_yscale() == "linear":
        graph_limits["ymin"] *=  0.000
        graph_limits["ymax"] *=  1.05
    else:
        graph_limits["ymin"] *= 0.5
        graph_limits["ymax"] *= 2
    canvas.ax.set_xlim(graph_limits["xmin"], graph_limits["xmax"])
    canvas.ax.set_ylim(graph_limits["ymin"], graph_limits["ymax"])

def find_limits(self):
    xmin_all = None
    xmax_all = None
    ymin_all = None
    ymax_all = None
    for key, item in self.datadict.items():
        if item is not None and len(item.xdata) > 0:
            nonzero_ydata = list(filter(lambda x: (x != 0), item.ydata))
            xmin_item = min(item.xdata)
            xmax_item = max(item.xdata)
            ymin_item = min(nonzero_ydata)
            ymax_item = max(item.ydata)

            if xmin_all == None:
                xmin_all = xmin_item
            if xmax_all == None:
                xmax_all = xmax_item
            if ymin_all == None:
                ymin_all = ymin_item
            if ymax_all == None:
                ymax_all = ymax_item

            if xmin_item < xmin_all:
                xmin_all = xmin_item
            if xmax_item > xmax_all:
                xmax_all = xmax_item
            if (ymin_item < ymin_all):
                ymin_all = ymin_item
            if ymax_item > ymax_all:
                ymax_all = ymax_item
    return {"xmin":xmin_all, "xmax":xmax_all, "ymin":ymin_all, "ymax":ymax_all}


def reload_plot(self, from_dictionary = True):
    datman.clear_layout(self)
    datman.load_empty(self)
    define_highlight(self)
    hide_highlight(self)
    datman.open_selection(self, None, from_dictionary)
    if len(self.datadict) > 0:
        set_canvas_limits(self, self.canvas)


def refresh_plot(self, from_dictionary = True, set_limits = True):
    for line in self.canvas.ax.lines:
        line.remove()
    datman.open_selection(self, None, from_dictionary)
    if set_limits and len(self.datadict) > 0:
        set_canvas_limits(self, self.canvas)
    self.canvas.draw()

def get_next_color(self):
    color_list = self.canvas.color_cycle
    used_colors = []
    item_rows = copy.copy(self.item_rows)
    color_length = len(color_list)
    if len(item_rows) >= color_length:
        item_rows_list = list(item_rows.items())
        item_rows_list = item_rows_list[-color_length+1:]
        item_rows = dict(item_rows_list)
    for key, item in item_rows.items():
        used_colors.append(item.color_picker.color)
    for color in color_list:
        if color not in used_colors:
            return color

def load_fonts(self):
    font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    for font in font_list:
        try:
            matplotlib.font_manager.fontManager.addfont(font)
        except:
            print(f"Could not load {font}")
    print("Done loading fonts")


class PlotWidget(FigureCanvas):
    def __init__(self, parent=None, xlabel="", ylabel="", yscale = "log", title="", scale="linear", style = "seaborn-whitegrid"):
        self.figure = Figure()
        self.figure.set_tight_layout(True)
        self.canvas = FigureCanvas(self.figure)
        self.set_style(parent)
        self.ax = self.figure.add_subplot(111)
        xscale = parent.preferences.config["plot_X_scale"]
        yscale = parent.preferences.config["plot_Y_scale"]
        title = parent.preferences.config["plot_title"]
        self.set_ax_properties(parent, title, xlabel, ylabel, xscale, yscale)
        self.set_save_properties(parent)
        self.set_color_cycle(parent)
        super(PlotWidget, self).__init__(self.figure)

    def set_save_properties(self, parent):
        plt.rcParams["savefig.format"] = parent.preferences.config["savefig_filetype"]
        if parent.preferences.config["savefig_transparent"]:
            plt.rcParams["savefig.transparent"] = True

    def set_ax_properties(self, parent, title = "", xlabel = "", ylabel = "", xscale="linear", yscale = "log"):
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel, fontweight = parent.preferences.config["plot_font_weight"])
        self.ax.set_ylabel(ylabel, fontweight = parent.preferences.config["plot_font_weight"])
        self.ax.set_title(title)
        self.ax.tick_params(direction=parent.preferences.config["plot_tick_direction"], length=parent.preferences.config["plot_major_tick_length"], width=parent.preferences.config["plot_major_tick_width"])
        self.ax.tick_params(direction=parent.preferences.config["plot_tick_direction"], length=parent.preferences.config["plot_minor_tick_length"], width=parent.preferences.config["plot_minor_tick_width"], which="minor")
        self.ax.set_yscale(yscale)
        self.ax.set_xscale(xscale)
        self.ax.tick_params(axis='x',which='minor',bottom=True, top=True)
        self.ax.tick_params(axis='y',which='minor',left=True, right=True)
        self.ax.minorticks_on()
        self.ax.tick_params(bottom=parent.preferences.config["plot_tick_bottom"], top=parent.preferences.config["plot_tick_top"],
                                left=parent.preferences.config["plot_tick_left"], right=parent.preferences.config["plot_tick_right"])



    def set_style(self, parent):
        plt.rcParams.update(plt.rcParamsDefault)
        if Adw.StyleManager.get_default().get_dark():
            self.figure.patch.set_facecolor("#242424")
            params = {"ytick.color" : "w",
            "xtick.color" : "w",
            "axes.labelcolor" : "w",
            "font.family": "sans-serif",
            "font.weight": parent.preferences.config["plot_font_weight"],
            "font.sans-serif": parent.preferences.config["plot_font_family"],
            "font.size": parent.preferences.config["plot_font_size"],
            "font.style": parent.preferences.config["plot_font_style"],
            "mathtext.default": "regular"
            }
            plt.style.use(parent.preferences.config["plot_style_dark"])
        else:
            self.figure.patch.set_facecolor("#fafafa")
            params = {"ytick.color" : "black",
            "xtick.color" : "black",
            "axes.labelcolor" : "black",
            "font.family": "sans-serif",
            "font.weight": parent.preferences.config["plot_font_weight"],
            "font.sans-serif": parent.preferences.config["plot_font_family"],
            "font.size": parent.preferences.config["plot_font_size"],
            "font.style": parent.preferences.config["plot_font_style"],
            "mathtext.default": "regular"
            }

            plt.style.use(parent.preferences.config["plot_style_light"])
        plt.rcParams.update(params)

    def set_color_cycle(self, parent):
        cmap = parent.preferences.config["plot_color_cycle"]
        reverse_dark = parent.preferences.config["plot_invert_color_cycle_dark"]
        if Adw.StyleManager.get_default().get_dark() and reverse_dark:
            cmap += "_r"
        color_cycle = cycler(color=plt.get_cmap(cmap).colors)
        self.color_cycle = color_cycle.by_key()['color']


