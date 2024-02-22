## We have moved
The project source code is now hosted over on [GNOME Gitlab](https://gitlab.gnome.org/World/Graphs).

# Graphs
Plot and manipulate data with Graphs!

![image](https://gitlab.gnome.org/World/Graphs/-/raw/main/data/screenshots/sin_cos.png?ref_type=heads)


Graphs is a simple, yet powerful tool that allows you to plot and manipulate your data with ease. New data can be imported from a wide variety of filetypes, or generated by equation. All data can be manipulated using a variety of operations.
Apart from regular operations, Graphs also has support for curve fitting on the data, allowing you to effortlessly analyze trends within your datasets.
Graphs supports extensive customization options to change the style of the plots. You can add and edit stylesheets in detail, allowing you to quickly save and apply existing stylesheets on new data. 
Graphs is an excellent fit for both plotting and data manipulation. The plots created with Graphs can be saved in a variety of formats suitable for sharing and presenting to a wide audience, such as in a scientific publication or presentations.
It is also possible to save the plots as vector images, which can be easily edited in programs like Inkscape for further customization and refinement. Graphs is written with the GNOME environment in mind, but should be suitable for any other desktop environment as well.

The operations include:
  - Shifting data
  - Normalizing Data
  - Smoothening data
  - Centering Data
  - Cutting Data
  - Combining Data
  - Translating data
  - Derivative and indefinite integral
  - Fourier Transformations
  - Custom transformations
 
For feedback or general issues, please file an issue [at the GitLab issue tracker](https://gitlab.gnome.org/World/Graphs/-/issues).

## Install Graphs

### Stable
Since Graphs is developed using GNOME Builder, most testing will be done in a Flatpak environment, and the recommended installation method is therefore to install Graphs from Flathub. 
An official build is also available on the Snap store:

<p>
<a href="https://flathub.org/apps/details/se.sjoerd.Graphs"><img height="62" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-en.svg"/></a>&nbsp;&nbsp;
<a href="https://snapcraft.io/graphs"><img height="60" alt="Get it from the Snap Store" src="https://snapcraft.io/static/images/badges/en/snap-store-black.svg"/></a>
</p> 

### Beta
The latest testing version of Graphs is available in the Flathub beta channel. To install the beta, first the Flatpak remote needs to be configured:

```sh
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
```

Then, install the application:

```sh
flatpak install flathub-beta se.sjoerd.Graphs
```
To run the beta version by default, the following command can be used:

```sh
sudo flatpak make-current se.sjoerd.Graphs beta
```
Note that the `sudo` is neccesary here, as it sets the current branch on the system level. To install this on a per-user basis, the flag `--user` can be used in the  previous commands. 
To switch back to the stable version simply run the above command replacing `beta` with `stable`. A beta version is also available in the beta channel of the Snap Store.
We are always looking for feedback, so feel free to report any issues or suggestions on the GitLab [issue tracker](https://gitlab.gnome.org/World/Graphs/-/issues).



## How to build from source
This project is developed in [GNOME Builder](https://developer.gnome.org/documentation/introduction/builder.html). After cloning and opening the project, you can press run to verify you have all correct dependencies installed.
You might need to install meson, if it is not already available on your system.
When the project successfully ran, you can create a Flatpak-bundle on the buildchain menu, which you then can install on your system.

If you want to try the latest development, we urge you to try the Flathub beta branch instead of building yourself.

### Build without Flatpak
This project targets the GNOME Platform on Flathub. Manually building Graphs for any other platform is currently **not supported**.

If you want to build without Flatpak anyway these instructions might help:

build-time dependencies: `meson, blueprint-compiler, gettext`, `vala`, `gtk4-devel`, `libadwaita-devel`

runtime dependencies: `matplotlib, python3-matplotlib-gtk4, scipy, numpy, numexpr, sympy`

The actual package names might vary depending on your distribution, and depending on your distribution additional packages may be required.

building:
```
git clone https://gitlab.gnome.org/World/Graphs.git
cd Graphs
meson setup build
ninja -C build
ninja -C build/ install
```
Uninstall could then be done with the following:
```
ninja -C build/ uninstall
```

Please note, that this install might have issues that the Flatpak version does not.

## How to contribute
### Translations

Graphs is translated on the GNOME translation platform [Damned Lies](https://l10n.gnome.org/module/Graphs). 
If you wish to contribute by translating Graphs, you can join a language team. More information on that can be found on the [GNOME Translation Project Wiki](https://wiki.gnome.org/TranslationProject).

### Code 

If you wish to contribute to the code of Graphs, feel free to submit a [Merge Request](https://gitlab.gnome.org/World/Graphs/-/merge_requests). 
We are always happy for contributions, and new code is generally reviewed within a few days time.

### Feedback and bug reports

If you found an issue or have general feedback, please file an issue at the [issue tracker](https://gitlab.gnome.org/World/Graphs/-/issues).


## Code of Conduct
This project follows the [GNOME Code of Conduct](https://conduct.gnome.org/committee/).
