#!/bin/sh
set -eu

# Change to this directory
cd "$(dirname "$0")"

# test
./format.sh
./test.sh

# Make package
echo "Making packages."
cd ..
python3 -m build

# Token required. Check ~/.pypirc
python3 -m pip install twine --upgrade

# Upload distribution archives only, excluding extracted directories.
set --
for distribution in dist/*.whl dist/*.tar.gz; do
    if [ -f "$distribution" ]; then
        set -- "$@" "$distribution"
    fi
done
if [ "$#" -eq 0 ]; then
    echo "No distribution archives found in dist/." >&2
    exit 1
fi
python3 -m twine upload --skip-existing "$@"

# Uninstall unsatfit
sudo /usr/bin/python3 -m pip uninstall unsatfit
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "sudo /usr/bin/python3 -m pip install unsatfit"
