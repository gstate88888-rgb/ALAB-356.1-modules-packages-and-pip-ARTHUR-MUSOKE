ALAB 356.1 - Modules, Packages, and PIP
Learner
Arthur Musoke

Overview
This lab demonstrates:

Using Python built-in modules

math
random
platform
Creating and importing custom modules and packages

Installing and using third-party packages with PIP

Files
builtin_usage.py
Uses built-in Python modules to:

Generate a random number
Calculate a square root
Display operating system information
Display Python version information
mypackage/utilities.py
Contains:

greet(name)
factorial(n)
use_utilities.py
Imports and uses functions from the custom package.

external_package.py
Demonstrates the use of the Colorama package installed using PIP.

Package Structure
ALAB-356.1-modules-packages-and-pip-ARTHUR-MUSOKE/

│
├── builtin_usage.py
├── use_utilities.py
├── external_package.py
│
└── mypackage/
    ├── __init__.py
    └── utilities.py
