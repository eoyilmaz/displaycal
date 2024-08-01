![license](https://img.shields.io/badge/License-GPL%20v3-blue.svg)
![pyversion](https://img.shields.io/pypi/pyversions/DisplayCAL.svg)
![pypiversion](https://img.shields.io/pypi/v/DisplayCAL.svg)
![wheel](https://img.shields.io/pypi/wheel/DisplayCAL.svg)

DisplayCAL Python 3 Project
===========================

This project intended to modernize the DisplayCAL code including Python 3 support.

Florian Höch, the original developer, did an incredible job of creating and maintaining
DisplayCAL for all these years. But, it seems that, during the pandemic, very
understandably, he lost his passion to the project. Now, it is time for us, the
DisplayCAL community, to contribute back to this great tool.

This project is based on the ``HEAD`` of the Sourceforge version, which had 5 extra
commits that Florian has created after the ``3.8.9.3`` release on 14 Jan 2020.

Status Update (6 June 2024)
---------------------------

Windows version is now working!

DisplayCAL is in [PyPI](https://pypi.org/project/DisplayCAL/) now (yay!).

Here is a screenshots showing the tool working with Python 3.10:

![image](https://user-images.githubusercontent.com/1786804/169152229-e06ff549-55fe-4149-8742-405446e6b01f.png)

Currently, DisplayCAL is working with Python 3.8 to 3.11 and wxPython 4.1.1 to 4.2.1.

Here is a list of things that is working:

- The UI and general functionality.
- Calibration + Characterization (Profiling).
- Installing the created ICC profile both locally and system-wide (requires root
  permissions).
- Profile Info window is now fully working (on some systems we still have an issue
  related to default values [#67](https://github.com/eoyilmaz/displaycal-py3/issues/67)).
- Measurement report creation.
- Creating, displaying and uploading Colorimeter Corrections.
- Measuring and reporting display uniformity.
- Creating charts with Test Chart Editor and creating diagnostic 3d data.
- Creating 3D LUTs.
- Creating synthetic ICC profiles.
- and a lot of other stuff are working properly.

What is not working
-------------------

- Everything should be working now. But, incase you encounter any bugs please create
  [issues](https://github.com/eoyilmaz/displaycal-py3/issues).

How to install (Linux and MacOS)
--------------------------------

Currently, there is no ``RPM``, ``DEB``, ``APP`` or ``MSI`` packages. These are coming
soon.

To test the code you can either run it directly from the source or install it as a
``sdist`` package.  To do this: 

Prerequisites:

* Assorted C/C++ builder tools
* dbus
* glib 2.0 or glibc
* gtk-3
* libXxf86vm
* pkg-config
* python3-devel

Please install these from your package manager. 

```shell
# Brew on MacOS
brew install glib gtk+3 python@3.10

# Debian installs
apt-get install build-essential dbus libglib2.0-dev pkg-config libgtk-3-dev libxxf86vm-dev

# Fedora core installs
dnf install gcc glibc-devel dbus pkgconf gtk3-devel libXxf86vm-devel python3-devel
```

> [!NOTE]
> Note, if your system's default python is outside the supported range you will need to
> install a supported version and its related devel package. 

Then pull the source:

```shell
git clone https://github.com/eoyilmaz/displaycal-py3
cd ./displaycal-py3/
```

At this stage you may want to switch to the ``develop`` branch to test some new features
or possibly fixed issues over the ``main`` branch.

```shell
git checkout develop
```

Then you can build and install DisplayCAL using:

```shell
make build
make install
```
The build step assumes your system has a `python3` binary available that is
within the correct range. If your system `python3` is not supported and you
installed a new one, you can try passing it to the build command:

```shell
$ python3 --version
# Python 3.12.2
$ make build # this will fail
$ python3.11 --version
# Python 3.11.8
$ make SYSTEM_PYTHON=python3.11 build # should work
```

If this errors out for you, you can follow the
[Manual Setup](https://github.com/eoyilmaz/displaycal-py3#manually-setup)
section below.

Otherwise, this should install DisplayCAL. To run the UI:

```shell
make launch
```

How To Install (Windows)
-----------------------

Windows version is now working properly. The catch is that you need to use Python 3.9,
3.10 or 3.11 and use the system Python, so no Virtual Environments. Here is the
installation procedure:

1- Download and install one of Python 3.9, 3.10 or 3.11. Unfortunatelly Python 3.12 is
   not currently working:

   Here is some download links that are now hidden in Python's home page:
   - [python-3.9.13-amd64.exe](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)
   - [python-3.10.11-amd64.exe](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
   - Python 3.11 can be downloaded directly from [Python.org](https://www.python.org/downloads/windows/).
   - Python 3.12 is not supported currently.

   Some of the libraries that DisplayCAL depends on are not working or supported with
   Python 3.12. So, stick with Python 3.9, 3.10 or 3.11 until we find a solution.

   Also don't forget to select "Add Python 3.xx to PATH" in the installer.

   ![image](screenshots/Python_3.9_Installation_Windows.jpg)

2- Download and install Visual Studio Build Tools:

   Download from https://visualstudio.microsoft.com/visual-cpp-build-tools/

   Select "Desktop development with C++" only:

   ![image](screenshots/Visual_Studio_Build_Tools.jpg)

3- Install DisplayCAL through PyPI:

   After both Python and Visual Studio Build Tools are installed run the following in
   the command prompt:

   ```shell
   pip install displaycal
   ```

4- Run DisplayCAL:

   ```shell
   python -m DisplayCAL
   ```

> [!WARNING]
> Under Windows use the system Python installation instead of a virtual environment as
> Wexpect module cannot read ArgyllCMS command outputs from inside a virtual
> environment.

> [!WARNING]
> Under Windows don't run DisplayCAL inside the IDE (Vscode, Pycharm etc.) terminal as
> most of the IDE's are creating virtual terminals and it is not possible to capture the
> command outputs with Wexpect.

Manual Setup (Linux & MacOS)
----------------------------

If the `makefile` workflow doesn't work for you, you can setup the virtual environment
manually. Ensure the python binary you're using is supported:

```shell
python -m venv .venv # python3.11 -m venv .venv if system python is not a supported version
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m build
pip install dist/DisplayCAL-3.9.*.whl
```

This should install DisplayCAL. To run the UI:

```shell
displaycal
```

Manual Setup (Windows)
----------------------

Under Windwos the `makefile` workflow will not work, using a virtual environment is also
breaking Wexpect module, so you need to use your system Python installation. Currently
under Windows, DisplayCAL will run with Python 3.9, 3.10 and 3.11, but Python 3.12 is
not supported. To install DisplayCAL manually under Windows follow these steps:

1- Download and install one of Python 3.9, 3.10 or 3.11. Unfortunatelly Python 3.12 is
   not currently working:

   Here is some download links that are now hidden in Python's home page:
   - [python-3.9.13-amd64.exe](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)
   - [python-3.10.11-amd64.exe](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
   - Python 3.11 can be downloaded directly from [Python.org](https://www.python.org/downloads/windows/).
   - Python 3.12 is not supported currently.

   Some of the libraries that DisplayCAL depends on are not working or supported with
   Python 3.12. So, stick with Python 3.9, 3.10 or 3.11 until we find a solution.

   Also don't forget to select "Add Python 3.xx to PATH" in the installer.

   ![image](screenshots/Python_3.9_Installation_Windows.jpg)

2- Download and install Visual Studio Build Tools:

   Download from https://visualstudio.microsoft.com/visual-cpp-build-tools/

   Select "Desktop development with C++" only:

   ![image](screenshots/Visual_Studio_Build_Tools.jpg)

3- Download and install Git:

   https://www.git-scm.com/download/win

   When installer asks, the default settings are okay.

4- Clone DisplayCAL repository, build and install it:

   Open up a command prompt and run the following:

   ```shell
   cd %HOME%
   git clone https://github.com/eoyilmaz/displaycal-py3.git
   cd displaycal-py3
   ```

   Then we suggest switching to the `develop` branch as we would have fixes introduced
   to that branch the earliest. To do that run:

   ```shell
   git checkout develop
   ```

   If you want to switch to some other branches to test the code you can replace
   `develop` in the previous command with the branch name:

   ```shell
   git checkout 367-compiled-sucessfully-in-w10-py311-but-createprocess-fails-call-to-dispread-to-measure
   ```

   Let's install the requirements, build displaycal and install it:

   ```shell
   pip install -r requirements.txt -r requirements-dev.txt
   python -m build
   pip install dist/DisplayCAL-3.9.*.whl
   ```

5- Run DisplayCAL:

   ```shell
   python -m DisplayCAL
   ```

6- To rebuild and install it again:

   First remove the old installation:

   ```shell
   pip uninstall displaycal
   ```

   Build and install it again:

   ```shell
   python -m build
   pip install dist/DisplayCAL-3.9.*.whl
   ```

Road Map
--------

Here are some ideas on where to focus the future development effort:

- ~~Add DisplayCAL to PyPI 
  ([#83](https://github.com/eoyilmaz/displaycal-py3/issues/83)).~~ (Done!
  [Display PyPI Page](https://pypi.org/project/DisplayCAL/))
- ~~Replace the ``DisplayCAL.ordereddict.OrderedDict`` with the pure Python ``dict``
  which is ordered after Python 3.6.~~ (Done!)
- ~~Make the code fully compliant with PEP8 with the modification of hard wrapping the
  code at 88 characters instead of 80 characters. This also means a lot of class and
  method/function names will be changed.~~ Thanks to ``black`` and some ``flake8`` this
  is mostly done.
- Remove the ``RealDisplaySizeMM`` C-Extension which is just for creating a 100 x 100 mm
  dialog and getting ``EDID`` information. It should be possible to cover all the same
  functionality of this extension and stay purely in Python. It is super hard to debug
  and super hard to maintain.
- Try to move the UI to Qt. This is a big ticket. The motivation behind this is that it
  is a better library and more developer understands it and the current DisplayCAL
  developers have more experience with it.
- Create unit tests with ``Pytest`` and reach to ~100% code coverage. The ``3.8.9.3``
  version of DisplayCAL is around 120k lines of Python code (other languages are not
  included) and there are no tests (or the repository this project has adapted didn't
  contain any tests). This is a nightmare and super hard to maintain. This is an ongoing
  work, with the latest commits we have around 200 tests (which is super low, should be
  thousands) and the code coverage is around 26% (again this is super low, should be
  over 99%).
- Replace the ``wexpect.py`` with the latest release of ``Wexpect``. There is no comment
  in the code on why we have a ``wexpect.py`` instead of using the PyPI version of
  ``Wexpect``.
- Replace ``os.path`` related code with ``pathlib.Path`` class.
- Organize the module structure, move UI related stuff in to ``ui`` module etc., move
  data files into their own folders.
- Use [importlib_resources](https://importlib-resources.readthedocs.io/en/latest/using.html)
  module for reading data files.
- Update the ``Remaining time`` calculation during profiling to estimate the time by
  also considering the luminance of the remaining patches to have a better estimation.
  Because, patches with higher luminance values are measured quickly than patches with
  lower luminance values.

Issues related to these ideas have been created. If you have a feature request, you can
create more issues or share your comment on the already created issues or create merge
requests that are fixing little or big things.

Because there are very little automated tests, **the code need to be tested 
constantly**. Please help us with that.

Have fun!
