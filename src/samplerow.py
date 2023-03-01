# SPDX-License-Identifier: GPL-3.0-or-later
from gi.repository import Gtk

from graphs import colorpicker, graphs, plotting_tools, ui, utilities
from graphs.plot_settings import PlotSettingsWindow


@Gtk.Template(resource_path="/se/sjoerd/Graphs/ui/sample_box.ui")
class SampleBox(Gtk.Box):
    __gtype_name__ = "SampleBox"
    sample_box = Gtk.Template.Child()
    sample_id_label = Gtk.Template.Child()
    check_button = Gtk.Template.Child()
    edit_button = Gtk.Template.Child()
    color_button = Gtk.Template.Child()
    delete_button = Gtk.Template.Child()

    def __init__(self, parent, key, color, label, selected=False):
        super().__init__()
        max_length = int(26)
        if len(label) > max_length:
            label = f"{label[:max_length]}..."
        if selected:
            self.check_button.set_active(True)
        self.sample_id_label.set_text(label)
        self.key = key
        self.parent = parent
        self.one_click_trigger = False
        self.time_first_click = 0
        self.gesture = Gtk.GestureClick()
        self.gesture.set_button(0)
        self.add_controller(self.gesture)
        self.edit_button.connect("clicked", self.edit)
        self.delete_button.connect("clicked", self.delete)
        self.color_picker = colorpicker.ColorPicker(color, key, parent,
                                                    self.color_button)
        self.check_button.connect("toggled", self.toggled)

    def delete(self, _):
        graphs.delete_item(self.parent, self.key, True)

    def toggled(self, _):
        plotting_tools.refresh_plot(self.parent, False)
        ui.enable_data_dependent_buttons(
            self.parent, utilities.get_selected_keys(self.parent))

    def edit(self, _):
        PlotSettingsWindow(self.parent, self.key)
