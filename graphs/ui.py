# SPDX-License-Identifier: GPL-3.0-or-later
"""Some UI utilities."""
import contextlib
from gettext import gettext as _, pgettext as C_

from gi.repository import GLib, Graphs, Gtk

from graphs import file_import, file_io, misc, utilities
from graphs.item_box import ItemBox


def on_items_change(
    data,
    _ignored,
    application: Graphs.Application,
) -> None:
    """Handle UI representation of items."""
    item_list = application.get_window().get_item_list()
    while item_list.get_last_child() is not None:
        item_list.remove(item_list.get_last_child())

    for index, item in enumerate(data):
        itembox = ItemBox(application, item, index)
        item_list.append(itembox)
        row = item_list.get_row_at_index(index)
        row.add_controller(itembox.get_drag_source())
        row.add_controller(itembox.get_drop_target())
        row.add_controller(itembox.get_click_gesture())
    data.add_view_history_state()


def add_data_dialog(application: Graphs.Application) -> None:
    """Show add data dialog."""

    def on_response(dialog, response):
        with contextlib.suppress(GLib.GError):
            file_import.import_from_files(
                application,
                dialog.open_multiple_finish(response),
            )

    dialog = Gtk.FileDialog()
    dialog.set_filters(
        utilities.create_file_filters((
            (
                C_("file-filter", "Supported files"),
                ["xy", "dat", "txt", "csv", "xrdml", "xry", "graphs"],
            ),
            (C_("file-filter", "ASCII files"), ["xy", "dat", "txt", "csv"]),
            (C_("file-filter", "PANalytical XRDML"), ["xrdml"]),
            (C_("file-filter", "Leybold xry"), ["xry"]),
            misc.GRAPHS_PROJECT_FILE_FILTER_TEMPLATE,
        )),
    )
    dialog.open_multiple(application.get_window(), None, on_response)


def export_data_dialog(application: Graphs.Application) -> None:
    """Show export data dialog."""
    data = application.get_data()
    window = application.get_window()
    if data.props.empty:
        window.add_toast_string(_("No data to export"))
        return
    multiple = len(data) > 1

    def on_response(dialog, response):
        with contextlib.suppress(GLib.GError):
            if multiple:
                directory = dialog.select_folder_finish(response)
                for item in data:
                    file = directory.get_child_for_display_name(
                        f"{item.get_name()}.txt",
                    )
                    file_io.save_item(file, item)
            else:
                file = dialog.save_finish(response)
                file_io.save_item(file, data[0])
            window.add_toast_string_with_file(
                _("Exported Data"),
                file,
            )

    dialog = Gtk.FileDialog()
    if multiple:
        dialog.select_folder(window, None, on_response)
    else:
        filename = f"{data[0].get_name()}.txt"
        dialog.set_initial_name(filename)
        dialog.set_filters(
            utilities.create_file_filters(
                ((C_("file-filter", "Text Files"), ["txt"]), ),
            ),
        )
        dialog.save(window, None, on_response)


def validate_entry(entry: Gtk.Editable) -> float:
    """Validate an entry for having a parsable bool value."""
    value = utilities.string_to_float(entry.get_text())
    is_valid = value is not None
    if is_valid:
        entry.remove_css_class("error")
    else:
        entry.add_css_class("error")
    return is_valid, value
