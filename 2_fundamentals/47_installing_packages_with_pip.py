# Installing Packages with pip
# In a terminal:
#   pip install requests            install
#   pip install -U requests         upgrade
#   pip install requests==2.31.0    specific version
#   pip uninstall requests          remove
#   pip show requests               details
#   pip list                        installed packages
# (Use pip3 / python -m pip if 'pip' points to an old Python.)

try:
    import requests
    print("requests is installed, version", requests.__version__)
except ImportError:
    print("requests is not installed - run: pip install requests")
