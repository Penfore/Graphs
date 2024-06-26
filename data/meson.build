# SPDX-License-Identifier: GPL-3.0-or-later
desktop_file_in = configure_file(
        input: application_id + '.desktop.in.in',
       output: application_id + '.desktop.in',
configuration: conf
)

desktop_file = i18n.merge_file(
        input: desktop_file_in,
       output: application_id + '.desktop',
         type: 'desktop',
       po_dir: '../po',
      install: true,
  install_dir: join_paths(datadir, 'applications')
)

desktop_file_validate = find_program('desktop-file-validate', required: false)
if desktop_file_validate.found()
  test(
    'Validate desktop file',
    desktop_file_validate,
    args: [
      desktop_file.full_path()
    ]
  )
endif

appstream_file_in = configure_file(
        input: application_id + '.appdata.xml.in.in',
       output: application_id + '.appdata.xml.in',
configuration: conf
)

appstream_file = i18n.merge_file(
        input: appstream_file_in,
       output: application_id + '.appdata.xml',
       po_dir: '../po',
      install: true,
  install_dir: join_paths(datadir, 'appdata')
)

# Validate Appdata
appstreamcli = find_program('appstreamcli', required: false)
if (appstreamcli.found())
  test(
    'Validate appstream file', appstreamcli,
    args: ['validate', '--no-net', '--explain', appstream_file.full_path()],
    workdir: meson.current_build_dir()
  )
endif

install_data(application_id + '.gschema.xml',
  install_dir: join_paths(datadir, 'glib-2.0/schemas'),
 install_mode: 'rwxrwxrwx'
)
gnome.compile_schemas(
  depend_files: [
    application_id + '.gschema.xml'
  ]
)

install_data(
    application_id + '.mime.xml',
    install_dir: get_option('datadir') / 'mime/packages',
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file',
       compile_schemas,
       args: ['--strict', '--dry-run', meson.current_source_dir()])
endif

blueprints_source = [
  'ui/add-equation.blp',
  'ui/add-style.blp',
  'ui/curve-fitting.blp',
  'ui/dialogs.blp',
  'ui/edit-item.blp',
  'ui/export-figure.blp',
  'ui/figure-settings-dialog.blp',
  'ui/figure-settings-page.blp',
  'ui/fitting-parameters.blp',
  'ui/import.blp',
  'ui/import-columns.blp',
  'ui/item-box.blp',
  'ui/shortcuts.blp',
  'ui/smoothen-settings.blp',
  'ui/style-color-box.blp',
  'ui/style-editor.blp',
  'ui/style-preview.blp',
  'ui/transform.blp',
  'ui/window.blp'
]

blueprints_ui = []
blueprints_vala = []
foreach b : blueprints_source
	blueprints_ui += b.replace('.blp', '.ui')
	blueprints_vala += b.replace('ui/', '') + '.vala'
endforeach

blueprints = custom_target('blueprints',
  input: blueprints_source,
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

blueprints_hack = custom_target('blueprints_hack',
	input: blueprints,
	output: blueprints_vala,
	command: [find_program('touch'), '@OUTPUT@'],
)

gresource_name = application_id + '.gresource.xml'
gresource_file = join_paths(meson.current_build_dir(), gresource_name)

gresource = custom_target('gresource',
  input: gresource_name,
  output: gresource_name,
  command: ['cp', '@INPUT@', '@OUTPUT@'],
  depends: blueprints,
)

gresource_bundle = gnome.compile_resources(
  application_id, gresource,
    dependencies: gresource,
gresource_bundle: true,
      source_dir: meson.current_build_dir(),
         install: true,
     install_dir: pkgdatadir,
          c_name: project_name,
)

devenv.set('GRAPHS_OVERRIDE_RESOURCES', gresource_bundle.full_path())

scalable_dir = join_paths('icons', 'hicolor', 'scalable', 'apps')
icon_name = ('@0@.svg').format(application_id)
if debug
  icon_name = ('@0@.Devel.svg').format(application_id)
endif
install_data(
  join_paths(scalable_dir, icon_name),
     rename: ('@0@.svg').format(application_id),
install_dir: join_paths(datadir, scalable_dir)
)

symbolic_dir = join_paths('icons', 'hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, ('@0@-symbolic.svg').format(application_id)),
  install_dir: join_paths(datadir, symbolic_dir)
)
