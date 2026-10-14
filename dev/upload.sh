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
# Keep each build separate so old archives in dist/ are never uploaded.
mkdir -p dist
build_dir=$(mktemp -d dist/upload.XXXXXX)
python3 -m build --outdir "$build_dir"

# Token required. Check ~/.pypirc
python3 -m pip install twine --upgrade

# Upload distribution archives only, excluding extracted directories.
set --
for distribution in "$build_dir"/*.whl "$build_dir"/*.tar.gz; do
    if [ -f "$distribution" ]; then
        set -- "$@" "$distribution"
    fi
done
if [ "$#" -eq 0 ]; then
    echo "No distribution archives found in $build_dir/." >&2
    exit 1
fi
python3 -m twine check "$@"
python3 -m twine upload --verbose --skip-existing "$@"

# Uninstall unsatfit
/usr/bin/python3 -m pip uninstall unsatfit
echo "Upload completed. Installed version uninstalled. Wait for a while and run"
echo "sudo /usr/bin/python3 -m pip install unsatfit"
