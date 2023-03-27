### Hexlet tests and linter status:
[![Actions Status](https://github.com/EzerTigger/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/EzerTigger/python-project-50/actions)
![Action Status](https://github.com/EzerTigger/python-project-50/actions/workflows/my_workflow.yml/badge.svg)
<a href="https://codeclimate.com/github/EzerTigger/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/caa0b76920f59f6618d1/maintainability" /></a>
<a href="https://codeclimate.com/github/EzerTigger/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/caa0b76920f59f6618d1/test_coverage" /></a>
##### The Console utility generates a diff between two files (json, yaml) and outputs it in different forms depending on the selected formatter.
#### Getting started
***
Clone the current repository via command:
>git clone https://github.com/EzerTigger/python-project-50.git 

#### Requirements
***
- Python = "^3.9"
- Poetry = "^1.2.2"

Check your pip version with the following command:
>python -m pip --version

Make sure that pip is always up to update. If not, use the following:
>python -m pip install --upgrade pip

#### Makefile
***
Using the Makefile you can generate all the needed packages for your virtual env.

To install poetry packages:
~~~
make install
~~~ 
To build your packages inside your project:
~~~
make build
~~~
It will let us execute the publish command knowing exactly what is going into the build:
~~~
make publish
~~~
Installs the build package from our OS, so we can start using simple shell commands:
~~~
make package-install
~~~


#### Usage:
~~~
gendiff
~~~
[![asciicast](https://asciinema.org/a/fuge8NWzl7CdkGimeaTrSm6U4.svg)](https://asciinema.org/a/fuge8NWzl7CdkGimeaTrSm6U4)
~~~
gendiff -f plain
~~~
[![asciicast](https://asciinema.org/a/570620.svg)](https://asciinema.org/a/570620)
~~~
gendiff -f json
~~~
[![asciicast](https://asciinema.org/a/570625.svg)](https://asciinema.org/a/570625)