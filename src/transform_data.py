# SPDX-License-Identifier: GPL-3.0-or-later
from gi.repository import Adw, Gtk

from graphs import item_operations, plotting_tools, utilities
from graphs.misc import InteractionMode

from numpy import *


def on_accept(_widget, self, window):
    input_x = str(window.transform_x_entry.get_text())
    input_y = str(window.transform_y_entry.get_text())
    selected_keys = utilities.get_selected_keys(self)
    if self.interaction_mode == InteractionMode.SELECT:
        _selection, start_stop = item_operations.select_data(self)

    for key in selected_keys:
        if f'{key}_selected' in self.datadict:
            start_index, stop_index = start_stop[key][0], start_stop[key][1]
            xdata_in = self.datadict[key].xdata[start_index:stop_index]
            ydata_in = self.datadict[key].ydata[start_index:stop_index]
            try:
                xdata_out, ydata_out = operation(xdata_in, input_x, input_y)
            except Exception as exception:
                exception_type = exception.__class__.__name__
                win = self.main_window
                win.toast_overlay.add_toast(Adw.Toast(title=f'{exception_type}: Unable to do transformation, make sure the syntax is correct'))
                return
            self.datadict[key].xdata[start_index:stop_index] = xdata_out
            self.datadict[key].ydata[start_index:stop_index] = ydata_out
        if self.interaction_mode != InteractionMode.SELECT:
            xdata_in = self.datadict[key].xdata
            ydata_in = self.datadict[key].ydata
            try:
                xdata_out, ydata_out = operation(key, xdata_in, ydata_in, input_x, input_y)
            except Exception as exception:
                exception_type = exception.__class__.__name__
                win = self.main_window
                win.toast_overlay.add_toast(Adw.Toast(title=f'{exception_type}: Unable to do transformation, make sure the syntax is correct'))
                return
            self.datadict[key].xdata = xdata_out
            self.datadict[key].ydata = ydata_out
        self.datadict[key].xdata, self.datadict[key].ydata = item_operations.sort_data(self.datadict[key].xdata, self.datadict[key].ydata)
    item_operations.delete_selected_data(self)
    item_operations.add_to_clipboard(self)
    plotting_tools.refresh_plot(self)
    window.destroy()


def operation(xdata, input_x, input_y):
    x_array = []
    y_array = []
    operations = []
    for xy_operation in [input_x, input_y]:
        xy_operation = xy_operation.replace('Y_range', 'y_range')
        xy_operation = xy_operation.replace('X_range', 'x_range')
        xy_operation = xy_operation.replace('Y', 'ydata[index]')
        xy_operation = xy_operation.replace('X', 'xdata[index]')
        xy_operation = xy_operation.replace('y_range', 'Y_range')
        xy_operation = xy_operation.replace('x_range', 'X_range')
        xy_operation = xy_operation.replace('^', '**')
        operations.append(xy_operation)
    x_operation, y_operation = operations[0], operations[1]
    for _index in enumerate(xdata):
        x_array.append(eval(x_operation))
        y_array.append(eval(y_operation))
    return x_array, y_array


@Gtk.Template(resource_path='/se/sjoerd/Graphs/ui/transform_window.ui')
class TransformWindow(Adw.Window):
    __gtype_name__ = 'TransformWindow'
    transform_x_entry = Gtk.Template.Child()
    transform_y_entry = Gtk.Template.Child()
    transform_confirm_button = Gtk.Template.Child()

    def __init__(self, parent):
        super().__init__()
        style_context = self.transform_confirm_button.get_style_context()
        style_context.add_class('suggested-action')

        self.transform_x_entry.set_text('X')
        self.transform_y_entry.set_text('Y')
        self.transform_confirm_button.connect('clicked', on_accept, parent, self)
        self.set_transient_for(parent.main_window)
        self.set_modal(True)
