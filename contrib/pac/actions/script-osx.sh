#!/bin/bash
set -ev

export PY37BINDIR=/Library/Frameworks/Python.framework/Versions/3.7/bin/
export PATH=$PATH:$PY37BINDIR
export CRYPTOGRAPHY_DONT_BUILD_RUST=1
echo osx build version is $DASH_ELECTRUM_VERSION


if [[ -n $GITHUB_REF ]]; then
    PIP_CMD="sudo python3 -m pip"
else
    python3 -m virtualenv env
    source env/bin/activate
    PIP_CMD="pip"
fi


if [[ -n $GITHUB_REF ]]; then
    git submodule init
    git submodule update

    echo "Building CalinsQRReader..."
    export MACOSX_DEPLOYMENT_TARGET=10.12
    d=contrib/CalinsQRReader
    pushd $d
    rm -fr build
    xcodebuild || fail "Could not build CalinsQRReader"
    popd
fi


$PIP_CMD install --no-dependencies -I \
    -r contrib/deterministic-build/requirements.txt
$PIP_CMD install --no-dependencies -I \
    -r contrib/deterministic-build/requirements-hw.txt
$PIP_CMD install --no-dependencies -I \
    -r contrib/deterministic-build/requirements-binaries-mac.txt
$PIP_CMD install --no-dependencies -I x11_hash>=1.4

$PIP_CMD install --no-dependencies -I \
    -r contrib/deterministic-build/requirements-build-mac.txt

pushd electrum_pac/
git clone https://github.com/zebra-lucky/electrum-dash-locale/ locale-repo
mv locale-repo/locale .
rm -rf locale-repo
find locale -name '*.po' -delete
find locale -name '*.pot' -delete
popd

cp contrib/osx/osx_actions.spec osx.spec
cp contrib/pac/pyi_runtimehook.py .
cp contrib/pac/pyi_tctl_runtimehook.py .

pyinstaller --clean \
    -y \
    --name electrum-pac-$DASH_ELECTRUM_VERSION.bin \
    osx.spec

sudo hdiutil create -fs HFS+ -volname "PacGlobal Electrum" \
    -srcfolder dist/PacGlobal\ Electrum.app \
    dist/Pac-Electrum-$DASH_ELECTRUM_VERSION-macosx.dmg
