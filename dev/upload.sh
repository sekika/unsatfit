#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`

# Check version
LATEST=`pip3 search unsatfit | grep ^unsatfit | awk '{print $2}' | sed -e 's/(//' | sed -e 's/)//'`
echo 'Latest version: '$LATEST
CURRENT=`grep ^version ../unsatfit/data/system.ini | sed -e 's/^.*=//' | sed -e 's/ //g'`
echo 'Development version: '$CURRENT
if [ $LATEST = $CURRENT ]; then
  echo 'Change version in ../unsatfit/data/system.ini to upload.'
  exit
fi

# Make package
echo "Making packages."
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel

# Upload
echo "Preparing PyPI password with passme"
# pip3 install passme
passme python
twine upload --skip-existing dist/*

# Uninstall unsatfit
sudo /usr/bin/python3 -m pip uninstall unsatfit
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "sudo /usr/bin/python3 -m pip install unsatfit"
