# This is selenium py2app OSX application with integrated chromedriver
## Requirements:
* python3-pip

## Build and run:
```bash
cd path/to/repo
make fullbuild
```
After this double click on resulted seleniumapp.app or type in terminal: open dist/seleniumapp.app

This command install python3 requirements, create py2app setup.py and build python3 application to osx app.

## Notes:
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
