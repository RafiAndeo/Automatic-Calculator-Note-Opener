
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="Python GUIs for Humans">
  <h2 align="center">psgtest</h2>
  <h2 align="center">Simple Python Testing</h2>
</p>

Run your Python programs using the interpreter version of your choice, and display the output in a GUI window.

![example](https://raw.githubusercontent.com/PySimpleGUI/psgtest/main/images_for_readme/psgtest_example.gif?token=ALAGMY7OEDZBCYVS7LEZP33BRUQGC)

## Installation

### Old-school Straight Pip

pip install psgtest

### pip via `python -m pip` the python recommended way

#### If `python` is your command

`python -m pip install psgtest`

#### If `python3` is your command

`python3 -m pip install psgtest`

## Usage

Once pip installed, you can launch psgtest by typing on the command line:  
`psgtest`

You can also create a Windows shortcut by following the instructions below.

## About

This is an example of another utility used in the development of PySimpleGUI that is being released for other PySimpleGUI users to use either as a standalone tool or as example code / design pattern to follow.

It can be challenging to manage multiple versions of Python and the need to test across multiple versions.  Virtual Environments are one approach that are often used.  psgtest does not use virtual environments.  Instead, it invokes the Python interpreter of your choice directly.

The advantage is that changing which version of Python that's used is changed in a single drop-down menu selection as shown in the example GIF above.  The session in the GIF shows launching the PySimpleGUI main test harness using multiple versions of Python by selecting the version from the drop-down at the top.

## Executing Multiple Programs

To run multiple programs, select the files to run from the list of files on the left portion of the window.  Then click the "Run" button.


## Editing Programs

You can also edit the programs selected by clicking the "Edit" button.  You will need to set up your editor using the PySimpleGUI global settings.  If you have pip installed a version of PySimpleGUI that's 4.53.0.14 or greater, then you can type `psgsettings` from the command line.  You can also change the settings by calling `sg.main()` (or typing from the command line `psgmain`).

## Specifying/Selecting Python Interpreter Locations

The Setup Window is where you enter the path to each version of Python that you want to test with.  The settings are stored in a file and thus will be saved from one run to another.

Selecting the version to use can be done in either the settings window or using the drop-down menu in the main window.

## Output

The stdout and stderr from each program you execute are  displayed in a tab with a name that matches your filename.  Each program you run will open a new tab.

In each tab you'll find 2 buttons that operate on the output shown in that tab.

Use the `Copy To Clipboard` button to copy the contents of the output to the clipboard.  

Use the `Clear` button to delete the output.

The `Close Tab` button closes the tab as does the right click menu item `Close`.  If you run the program again after closing the tab, the old contents of the tab are retained and shown when the tab is "re-opened".  (See the GIF above for an example)

## Make a Windows Shortcut

If you're running Windows, then you can use `psgshortcut` to make a shortcut to the .pyw file (if you download psgtest from GitHub) or the .py file (if you pip installed).  The icon for `psgtest` is in this repo and is also included when you pip install psgtest.  It's in the same folder as the gui.py file.  

You can find the location of psgtest after pip installing it by running psgtest, right clicking, and choosing "File Location".  You'll be shown where the `gui.py` file is located (the name of the psgtest program when pip installed).  It will usually be located in the `site-packages` folder in a folder named  `psgtest`.

Instructions on how to make shortcuts to pip installed PySimpleGUI programs can be found in [description for psgshortcut on PyPI](https://pypi.org/project/psgshortcut/).


## Release Notes



### 1.12.0

* Addition of a "custom release" of Python entry in setup
	* Enables using other "Python flavors" like pypy
	* One custom item is allowed

### 1.11.0
* Addition of a "run a single file" option so that you can quickly and easily test one program against many versions of Python

### 1.10.0

* Regression Test Feature - run large sets of tests.  Will keep tabs open that have failures and show an error popup

### 1.9.0

* Fix for exception when no settings are initially found.  Oy.... bad bug to have released reight away
* Will create a settings file with the currently running version of Python if one is not found
* Added minimum of 4.55.1 requirement for PySimpleGUI to the setup.py file

### 1.8.0

* Support for Python 3.4, 3.5, 3.11 added to settings 
* Set the settings filename to be `psgtest` instead of the default filename. This is needed because the file for these psg projects on PyPI are all name gui.py and thus will have all point to the same settings file if not explicitly set
* Only show configured interpreters in the Combo in main window     

## License

Licensed under an LGPL3 License

## Designed and Written By

Mike from PySimpleGUI.org

## Contributing

Like the PySimpleGUI project, this project is currently licensed under an open-source license, the project itself is structured like a proprietary product. Pull Requests are not accepted.

## Copyright

Copyright 2021 PySimpleGUI
