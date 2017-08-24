# This is tkinter and selenium py2app OSX application example
## Requirements:
* python3
* python3-pip

## Build and run:
```bash
cd path/to/repo
make requirements
make buildapp
```
After this double click on resulted seleniumapp.app or type in terminal: open dist/seleniumapp.app

This command install python3 requirements, create py2app setup.py and build python3 application to osx app.

## Notes:
* if you build this from virtualenv, you need change PythonExecutable value to /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 in dist/seleniumapp.app/Contents/Info.plist file.
* if you regenerate setup.py file, you will need add "chromedriver" to DATA_FILES list manualy

## Other command:
```bash
make clean
```
remove build and dist folders from repository folders

```bash
make makesetup
```
create py2app setup.py file

```bash
make buildapp
```
build python3 application to osx app

```
make requirements
```
install python3 requirements over pip3
