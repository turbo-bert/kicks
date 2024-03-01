import requests
import time
import os
import rich
import subprocess
from rich.pretty import pprint as PP
from rich.console import Console
from rich.table import Table

# written by robert degen
# 2015-2024

CONSOLE = Console()

home = os.getenv("USERPROFILE")

OP="_kicks"
OD=os.makedirs(OP, exist_ok=True)

t = Table()
t.add_column("#")
t.add_column("File")
t.add_row("u", "update kicks")
t.add_row("ud", "update dcx")
t.add_row("b", "create wrappers (.bat) in '\%USERPROFILE\%/AppData/Local/Microsoft/WindowsApps'")
t.add_row("1", "firefox windows 64")
t.add_row("2", "chrome windows 64")
t.add_row("3", "docker windows")
t.add_row("4", "process explorer")
t.add_row("5", "vc_redist")
t.add_row("6", "virtualbox")
t.add_row("7", "grml small iso")
t.add_row("8", "fpc win64")
t.add_row("9", "sublime")
t.add_row("10", "emacs")
t.add_row("11", "cygwin")

CONSOLE.print(t)

x = CONSOLE.input('# ')

if x == "u":
    while True:
        kicks_online = requests.get('https://pypi.org/pypi/kicks/json').json()["info"]["version"]
        lines = subprocess.check_output("pip freeze", shell=True, universal_newlines=True).strip().replace("\r", "").split("\n")
        kicks_local = [x for x in lines if x.find('kicks==') >= 0]
        CONSOLE.print("Latest ONLINE Version of kicks is %s" % kicks_online)
        CONSOLE.print("Local Version is %s" % str(kicks_local))
        update_loop_confirm = CONSOLE.input('u for UNINSTALL | i for INSTALL | q for QUIT | EMPTY for RE-CHECK # ')
        if update_loop_confirm == "u":
            uninstall_command = "pip uninstall -y kicks"
            subprocess.call(uninstall_command, shell=True)
        if update_loop_confirm == "i":
            install_command = 'pip install "kicks==%s"' % kicks_online
            update_loop_confirm = CONSOLE.input("run '%s' ? # " % install_command)
            subprocess.call(install_command, shell=True)
        if update_loop_confirm == "q":
            break

if x == "ud":
    while True:
        dcx_online = requests.get('https://pypi.org/pypi/dcx/json').json()["info"]["version"]
        lines = subprocess.check_output("pip freeze", shell=True, universal_newlines=True).strip().replace("\r", "").split("\n")
        dcx_local = [x for x in lines if x.find('dcx==') >= 0]
        CONSOLE.print("Latest ONLINE Version of dcx is %s" % dcx_online)
        CONSOLE.print("Local Version is %s" % str(dcx_local))
        update_loop_confirm = CONSOLE.input('u for UNINSTALL | i for INSTALL | q for QUIT | EMPTY for RE-CHECK # ')
        if update_loop_confirm == "u":
            uninstall_command = "pip uninstall -y dcx"
            subprocess.call(uninstall_command, shell=True)
        if update_loop_confirm == "i":
            install_command = 'pip install "dcx==%s"' % dcx_online
            update_loop_confirm = CONSOLE.input("run '%s' ? # " % install_command)
            subprocess.call(install_command, shell=True)
        if update_loop_confirm == "q":
            break


if x == "b":
    bindir = os.path.join(home, 'AppData', 'Local', 'Microsoft', 'WindowsApps')
    
    #dcx / python: daisy chain xpath
    with open(os.path.join(bindir, 'dcx.bat'), 'w') as f:
        f.write('python -m dcx %%*')

    #dcxc / python: daisy chain xpath CHROME
    with open(os.path.join(bindir, 'dcxc.bat'), 'w') as f:
        f.write('python -m dcx --local-chrome %%*')

    #dcxe / python: daisy chain xpath EDGE
    with open(os.path.join(bindir, 'dcxe.bat'), 'w') as f:
        f.write('python -m dcx --local-edge %%*')

    #kicks / python: kickstarter for windows64
    with open(os.path.join(bindir, 'dcx.bat'), 'w') as f:
        f.write('python -m kicks')

    #e / emacs
    with open(os.path.join(bindir, 'ee.bat'), 'w') as f:
        f.write('%s -nw %%*' % (os.path.join(home, '_kicks', 'e', 'bin', 'emacs')))

    #e / sublime
    with open(os.path.join(bindir, 'e.bat'), 'w') as f:
        f.write('%s %%*' % (os.path.join(home, '_kicks', 'sub', 'sublime_text')))

    #cw / cygwin mintty
    with open(os.path.join(bindir, 'cw.bat'), 'w') as f:
        f.write('%s %%*' % (os.path.join('C:\\', 'Cygwin64', 'bin', 'mintty.exe')))

    #lbu / lazarus build
    with open(os.path.join(bindir, 'lbu.bat'), 'w') as f:
        f.write('%s %%*' % (os.path.join('C:\\', 'lazarus', 'lazbuild.exe')))

    #ff / firefox
    with open(os.path.join(bindir, 'ff.bat'), 'w') as f:
        f.write('"%s" %%*' % (os.path.join('C:\\', 'Program Files', 'Mozilla Firefox', 'firefox.exe')))

    #pe / process explorer
    with open(os.path.join(bindir, 'pe.bat'), 'w') as f:
        f.write('"%s" %%*' % (os.path.join(home, '_kicks', 'pe', 'procexp.exe')))

if x == "1":
    outfile = os.path.join(OP, "firefox-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "2":
    outfile = os.path.join(OP, "chrome.zip")
    outzipdir = os.path.join(OP, "chrome")
    cmd = 'curl -C - -L -o "%s" "https://dl.google.com/chrome/install/GoogleChromeEnterpriseBundle64.zip"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call("""powershell -Command Expand-Archive -Path '%s' -DestinationPath '%s'""" % (outfile, outzipdir), shell=True)
        subprocess.call("""%s""" % os.path.join(outzipdir, "Installers", "GoogleChromeStandaloneEnterprise64.msi"), shell=True)
        #subprocess.call("""explorer %s""" % (outzipdir), shell=True)

if x == "3":
    outfile = os.path.join(OP, "docker-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://desktop.docker.com/win/main/amd64/Docker%%20Desktop%%20Installer.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "4":
    #https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer
    outfile = os.path.join(OP, "pe.zip")
    outzipdir = os.path.join(OP, "pe")
    cmd = 'curl -C - -L -o "%s" "https://download.sysinternals.com/files/ProcessExplorer.zip"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call("""powershell -Command Expand-Archive -Path '%s' -DestinationPath '%s'""" % (outfile, outzipdir), shell=True)
        subprocess.call("""explorer %s""" % (outzipdir), shell=True)

if x == "5":
    outfile = os.path.join(OP, "vc_redist.exe")
    cmd = 'curl -C - -L -o "%s" "https://aka.ms/vs/17/release/vc_redist.x64.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "6":
    #https://www.virtualbox.org/wiki/Downloads
    outfile = os.path.join(OP, "vbox-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://download.virtualbox.org/virtualbox/7.0.14/VirtualBox-7.0.14-161095-Win.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "7":
    #https://download.grml.org/grml64-small_2024.02.iso
    outfile = os.path.join(OP, "grml.iso")
    cmd = 'curl -C - -L -o "%s" "https://download.grml.org/grml64-small_2024.02.iso"' % outfile
    subprocess.call(cmd, shell=True)
    subprocess.call("""explorer %s""" % (OP), shell=True)

if x == "8":
    #https://sourceforge.net/projects/lazarus/files/
    outfile = os.path.join(OP, "laz-setup.exe")
    cmd = 'curl -C - -L -o "%s" "https://deac-riga.dl.sourceforge.net/project/lazarus/Lazarus%%20Windows%%2064%%20bits/Lazarus%%203.2/lazarus-3.2-fpc-3.2.2-win64.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)

if x == "9":
    outfile = os.path.join(OP, "sub.zip")
    outzipdir = os.path.join(OP, "sub")
    cmd = 'curl -C - -L -o "%s" "https://download.sublimetext.com/sublime_text_build_4169_x64.zip"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call("""powershell -Command Expand-Archive -Path '%s' -DestinationPath '%s'""" % (outfile, outzipdir), shell=True)
        subprocess.call("""explorer %s""" % (outzipdir), shell=True)

if x == "10":
    outfile = os.path.join(OP, "e.zip")
    outzipdir = os.path.join(OP, "e")
    cmd = 'curl -C - -L -o "%s" "http://ftp.gnu.org/gnu/emacs/windows/emacs-29/emacs-29.2_1.zip"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call("""powershell -Command Expand-Archive -Path '%s' -DestinationPath '%s'""" % (outfile, outzipdir), shell=True)
        subprocess.call("""explorer %s""" % (outzipdir), shell=True)

if x == "11":
    outfile = os.path.join(OP, "cygwinsetup.exe")
    cmd = 'curl -C - -L -o "%s" "https://www.cygwin.com/setup-x86_64.exe"' % outfile
    subprocess.call(cmd, shell=True)
    run_confirm = CONSOLE.input('run it? type "run" to execute or anything else to exit # ')
    if run_confirm == "run":
        subprocess.call(outfile, shell=True)
