# Intro

`kicks` is more or less simple helper for setting up a workstation for development.

# Setup Windows Server 2022

As `Administrator` (but WITHOUT ELEVATION) in a `cmd.exe` commandline, run:

    curl -L -o pysetup.exe "https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe"

to get a LTS python and install it by running...

    pysetup.exe PrependPath=1 /passive

Python and PIP should be in your PATH after re-opening the commandline.

Now run

    pip install kicks

to install the actual script and then start

    pip -m kicks
