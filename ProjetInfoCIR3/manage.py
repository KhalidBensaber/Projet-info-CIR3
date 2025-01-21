#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

def install_dependencies():
    try:
        # Check and install dependencies using the Python script
        print("Checking and installing dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', '-r', 'requirements.txt'])
        print("All dependencies are installed.")
    except subprocess.CalledProcessError as e:
        print("Failed to install dependencies. Error:", e)
        sys.exit(1)

def main():
    
    # Check and install dependencies before starting the server
    if os.path.exists("requirements.txt"):
        install_dependencies()
    
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetInfoCIR3.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
