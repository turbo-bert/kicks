# Intro

`kicks` is more or less simple helper for setting up a windows workstation for development. It is written in python and hosted on pypi. So using this it's always A) Installing a python intepreter B) Installing the pypi package.

You could also just use https://github.com/turbo-bert/kicks/blob/main/src/kicks/__main__.py as your source of inspiration and manually do your tasks.

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

Take a look at main option `b` to make your life easier when working with `cmd.exe`.

# Troubleshooting

## No Administrator Privileges Needed

Don't elevate your `cmd.exe` via UAC. All tasks can be done (and should be) as normal Administrator.

## User

Works only with user `Administrator`.

# Financial Support Appreciated

Feel free to use https://www.paypal.com/donate/?hosted_button_id=4EZE2QKKG29JE
