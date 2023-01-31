<?xml version='1.0' encoding='utf-8'?>
<interface>
  <requires lib="gtk" version="4.0" />
  <requires lib="Adw" version="1.2" />
  <template class="GraphsWindow" parent="AdwApplicationWindow">
    <property name="default-width">1024</property>
    <property name="default-height">768</property>
    <property name="title">Graphs</property>
    <child>
      <object class="GtkBox">
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkHeaderBar" id="header_bar">
            <child>
              <object class="GtkBox">
                <child>
                  <object class="AdwSplitButton">
                    <property name="icon-name">list-add-symbolic</property>
                    <property name="menu-model">add_data_menu</property>
                    <property name="tooltip-text" translatable="yes">Add new data</property>
                    <property name="action-name">app.add_data</property>
                  </object>
                </child>
                <child>
                  <object class="GtkSeparator">
                    <property name="width-request">10</property>
                    <property name="css-classes">spacer</property>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="undo_button">
                    <property name="action-name">app.undo</property>
                    <property name="focusable">1</property>
                    <property name="receives_default">1</property>
                    <property name="tooltip-text" translatable="yes">Undo</property>
                    <property name="icon-name">edit-undo-symbolic</property>
                  </object>
                </child>
                <child>
                  <object class="GtkButton" id="redo_button">
                    <property name="action-name">app.redo</property>
                    <property name="focusable">1</property>
                    <property name="receives_default">1</property>
                    <property name="tooltip-text" translatable="yes">Redo</property>
                    <property name="icon-name">edit-redo-symbolic</property>
                  </object>
                </child>
                <child>
                  <object class="GtkSeparator">
                    <property name="width-request">10</property>
                    <property name="css-classes">spacer</property>
                  </object>
                </child>
              </object>
            </child>"
            <child type="end">
              <object class="GtkBox">
                <property name="spacing">5</property>
                <child>
                  <object class="GtkMenuButton" id="view_menu_button">
                    <property name="always-show-arrow">true</property>
                    <property name="menu-model">view_menu</property>
                    <property name="icon-name">view-reveal-symbolic</property>
                  </object>
                </child>
                <child>
                  <object class="GtkSeparator">
                    <property name="width-request">5</property>
                    <property name="css-classes">spacer</property>
                  </object>
                </child>
                <child>
                  <object class="GtkMenuButton">
                    <property name="tooltip-text" translatable="yes">Open Application Menu</property>
                    <property name="icon-name">open-menu-symbolic</property>
                    <property name="menu-model">primary_menu</property>
                  </object>
                </child>
              </object>
            </child>
          </object>
        </child>
        <child>
          <object class="AdwFlap" id="sidebar_flap">
            <property name="reveal-flap">True</property>
            <property name="fold-duration">1</property>
            <property name="fold-policy">ADW_FLAP_FOLD_POLICY_NEVER</property>
            <child type="flap">
              <object class="GtkBox" id="selection_box">"
                <property name="orientation">vertical</property>
                <property name="width-request">335</property>
                <property name="hexpand">false</property>
                <child>
                  <object class="GtkScrolledWindow" id="equation_scroll">
                    <property name="height-request">250</property>
                    <property name="focusable">1</property>
                    <property name="hscrollbar_policy">never</property>
                    <property name="child">
                      <object class="GtkViewport">
                        <property name="child">
                          <object class="GtkListBox" id="list_box">
                            <property name="margin-bottom">5</property>
                            <property name="margin-top">5</property>
                            <property name="margin-start">5</property>
                            <property name="margin-end">5</property>
                            <property name="selection-mode">none</property>
                            <style>
                              <class name="boxed-list" />
                            </style>
                          </object>
                        </property>
                      </object>
                    </property>
                  </object>
                </child>
                <child>
                  <object class="GtkBox">
                    <property name="spacing">10</property>
                    <property name="margin-top">5</property>
                    <property name="margin-bottom">5</property>
                    <property name="margin-start">10</property>
                    <property name="margin-end">10</property>
                    <child>
                      <object class="GtkToggleButton" id="pan_button">
                        <property name="icon-name">move-tool-symbolic</property>
                        <property name="tooltip-text" translatable="yes">Left button to pan, right button to zoom. Hold control to to keep aspect ratio fixed</property>
                        <property name="action-name">app.pan</property>
                        <property name="hexpand">true</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkToggleButton" id="zoom_button">
                        <property name="icon-name">loupe-symbolic</property>
                        <property name="tooltip-text" translatable="yes">Zoom to rectangle</property>
                        <property name="action-name">app.zoom</property>
                        <property name="hexpand">true</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkToggleButton" id="select_data_button">
                        <property name="icon-name">edit-select-all-symbolic</property>
                        <property name="tooltip-text" translatable="yes">Select a span of data</property>
                        <property name="action-name">app.select_data_toggle</property>
                        <property name="hexpand">true</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkToggleButton" id="cut_data_button">
                        <property name="icon-name">edit-cut-symbolic</property>
                        <property name="tooltip-text" translatable="yes">Cut the selected span</property>
                        <property name="action-name">app.cut_data</property>
                        <property name="hexpand">true</property>
                      </object>
                    </child>
                  </object>
                </child>
                <child>
                  <object class="GtkScrolledWindow">
                    <property name="focusable">1</property>
                    <property name="hscrollbar_policy">never</property>
                    <property name="child">
                      <object class="GtkViewport">
                        <property name="child">
                          <object class="GtkBox">
                            <property name="vexpand">True</property>
                            <property name="orientation">vertical</property>
                            <child>
                              <object class="AdwPreferencesGroup">
                                <property name="margin-bottom">5</property>
                                <property name="margin-top">5</property>
                                <property name="margin-start">5</property>
                                <property name="margin-end">5</property>
                                <child>
                                  <object class="AdwExpanderRow">
                                    <property name="title">Adjust Data</property>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="activatable-widget">normalize_button</property>
                                        <property name="subtitle">Normalize data</property>
                                        <child>
                                          <object class="GtkButton" id="normalize_button">
                                            <property name="label">Normalize</property>
                                            <property name="action-name">app.normalize_data</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Shift all data vertically with respect to each other</property>
                                        <property name="activatable-widget">shift_vertically_button</property>
                                        <child>
                                          <object class="GtkButton" id="shift_vertically_button">
                                            <property name="label">Shift</property>
                                            <property name="action-name">app.shift_vertically</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Smoothen the data</property>
                                        <property name="activatable-widget">smooth_button</property>
                                        <child>
                                          <object class="GtkButton" id="smooth_button">
                                            <property name="label">Smoothen</property>
                                            <property name="action-name">app.smooth</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Center the data</property>
                                        <property name="activatable-widget">center_data_button</property>
                                        <child>
                                          <object class="GtkButton" id="center_data_button">
                                            <property name="label">Center</property>
                                            <property name="action-name">app.center_data</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                  </object>
                                </child>
                                <child>
                                  <object class="AdwExpanderRow">
                                    <property name="title">Translate and Multiply</property>
                                    <child>
                                      <object class="AdwEntryRow" id="translate_x_entry">
                                        <property name="title">Translate x-Axis</property>
                                        <property name="max-width-chars">6</property>
                                        <child>
                                          <object class="GtkButton" id="translate_x_button">
                                            <property name="label">Translate</property>
                                            <property name="action-name">app.translate_x</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwEntryRow" id="translate_y_entry">
                                        <property name="title">Translate y-Axis</property>
                                        <property name="max-width-chars">6</property>
                                        <child>
                                          <object class="GtkButton" id="translate_y_button">
                                            <property name="label">Translate</property>
                                            <property name="action-name">app.translate_y</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwEntryRow" id="multiply_x_entry">
                                        <property name="title">Multiply X</property>
                                        <property name="max-width-chars">6</property>
                                        <child>
                                          <object class="GtkButton" id="multiply_x_button">
                                            <property name="label">Multiply</property>
                                            <property name="action-name">app.multiply_x</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwEntryRow" id="multiply_y_entry">
                                        <property name="title">Multiply Y</property>
                                        <property name="max-width-chars">6</property>
                                        <child>
                                          <object class="GtkButton" id="multiply_y_button">
                                            <property name="label">Multiply</property>
                                            <property name="action-name">app.multiply_y</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                  </object>
                                </child>
                                <child>
                                  <object class="AdwExpanderRow">
                                    <property name="title">Manipulate Data</property>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Get the derivative of the data</property>
                                        <property name="activatable-widget">derivative_button</property>
                                        <child>
                                          <object class="GtkButton" id="derivative_button">
                                            <property name="label">Get</property>
                                            <property name="action-name">app.get_derivative</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Get the indefinite integral of the data</property>
                                        <property name="activatable-widget">integral_button</property>
                                        <child>
                                          <object class="GtkButton" id="integral_button">
                                            <property name="label">Get</property>
                                            <property name="action-name">app.get_integral</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Get the Fast Fourier Transform of the data</property>
                                        <property name="activatable-widget">fourier_button</property>
                                        <child>
                                          <object class="GtkButton" id="fourier_button">
                                            <property name="label">Get</property>
                                            <property name="action-name">app.get_fourier</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Get the Inverse Fast Fourier Transform of the data</property>
                                        <property name="activatable-widget">inverse_fourier_button</property>
                                        <child>
                                          <object class="GtkButton" id="inverse_fourier_button">
                                            <property name="label">Get</property>
                                            <property name="action-name">app.get_inverse_fourier</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                    <child>
                                      <object class="AdwActionRow">
                                        <property name="subtitle">Perform custom transformations on the data</property>
                                        <property name="activatable-widget">transform_data_button</property>
                                        <child>
                                          <object class="GtkButton" id="transform_data_button">
                                            <property name="label">Transform</property>
                                            <property name="action-name">app.transform_data</property>
                                            <property name="margin-bottom">5</property>
                                            <property name="margin-top">5</property>
                                          </object>
                                        </child>
                                      </object>
                                    </child>
                                  </object>
                                </child>
                              </object>
                            </child>
                          </object>
                        </property>
                      </object>
                    </property>
                  </object>
                </child>
              </object>
            </child>
            <child type="separator">
              <object class="GtkSeparator">
                <property name="orientation">vertical</property>
              </object>
            </child>
            <child type="content">
              <object class="AdwFlap" id="toolbar_flap">
                <property name="fold-policy">ADW_FLAP_FOLD_POLICY_NEVER</property>
                <property name="flap-position">GTK_PACK_END</property>
                <property name="orientation">vertical</property>
                <child type="content">
                  <object class="AdwToastOverlay" id="toast_overlay">
                    <property name="margin-top">5</property>
                    <property name="margin-bottom">5</property>
                    <property name="margin-start">5</property>
                    <property name="margin-end">5</property>
                  </object>
                </child>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </template>
  <menu id="add_data_menu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Add Data from File</attribute>
        <attribute name="action">app.add_data</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Add Data from File (Advanced)</attribute>
        <attribute name="action">app.add_data_advanced</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Add Data from Equation</attribute>
        <attribute name="action">app.add_equation</attribute>
      </item>
    </section>
  </menu>
  <menu id="view_menu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Toggle Sidebar</attribute>
        <attribute name="action">app.toggle_sidebar</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Toggle Toolbar</attribute>
        <attribute name="action">app.toggle_toolbar</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Restore View</attribute>
        <attribute name="action">app.restore_view</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Go Back</attribute>
        <attribute name="action">app.view_back</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Go Forward</attribute>
        <attribute name="action">app.view_forward</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Logarithmic X Scale</attribute>
        <attribute name="action">app.change_xscale</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Logarithmic Y Scale</attribute>
        <attribute name="action">app.change_yscale</attribute>
      </item>
    </section>
  </menu>
  <menu id="primary_menu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Save as text</attribute>
        <attribute name="action">app.save_data</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Export</attribute>
        <attribute name="action">app.export_data</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Plot Settings</attribute>
        <attribute name="action">app.plot_settings</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Preferences</attribute>
        <attribute name="action">app.preferences</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_Keyboard Shortcuts</attribute>
        <attribute name="action">win.show-help-overlay</attribute>
      </item>
      <item>
        <attribute name="label" translatable="yes">_About Graphs</attribute>
        <attribute name="action">app.about</attribute>
      </item>
    </section>
  </menu>
</interface>
