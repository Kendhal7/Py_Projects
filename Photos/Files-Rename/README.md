# Files-Rename

## Description

Files Rename is a python script that allows to rename all the files of a specific folder using a template name.

## Usage

Command line :
```bash
$ python3 files-rename.py src_dir newname newtype
```
Attributs:
```bash
src_dir = Source directory
newname = Name template for the files
newtype = Extension for the files ('same' to keep the existing extension)
```
## Examples :

Rename all the files in Test folder by IMG_i.jpg with i the number of the element
```bash
$ python3 files-rename.py /Desktop/Test IMG_ jpg 
```

Rename all the files in Test folder by July_i.png with i the number of the element
```bash
$ python3 files-rename.py /Desktop/Test July_ png 
```

Rename all the files in Test folder by Test_i with the existing extension
```bash
$ python3 files-rename.py /Desktop/Test July_ same
```

## Author and acknowledgment
Kendhal ALTAY
with the help of [GeeksforGeeks](https://www.geeksforgeeks.org/rename-multiple-files-using-python/) website.

## Date
27/02/20

##  Github
[Kendhal_Github](https://github.com/Kendhal7/Py_Projects.git)