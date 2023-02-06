#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`

# Make package
echo "Making packages."
cd ..
python3 -m build

# Upload
echo "Preparing PyPI password with passme"
# pip3 install passme
passme python
twine upload --skip-existing dist/*

# Uninstall unsatfit
sudo /usr/bin/python3 -m pip uninstall unsatfit
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "sudo /usr/bin/python3 -m pip install unsatfit"
