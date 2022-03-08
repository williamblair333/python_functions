import sys
import subprocess
import pkg_resources

def pkg_check(required):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', '-r', *missing], stdout=subprocess.DEVNULL)
