#!/bin/bash
set -ev

if [[ $ELECTRUM_MAINNET == "true" ]] && [[ -z $IS_RELEASE ]]; then
    # do not build mainnet apk if is not release
    exit 0
fi

cd build
if [[ -n $TRAVIS_TAG ]]; then
    BUILD_REPO_URL=https://github.com/bynicolas/electrum-pac.git
    git clone --branch $TRAVIS_TAG $BUILD_REPO_URL electrum-pac
else
    git clone .. electrum-pac
fi


pushd electrum-pac
./contrib/make_locale
find . -name '*.po' -delete
find . -name '*.pot' -delete
popd

# patch buildozer to support APK_VERSION_CODE env
VERCODE_PATCH_PATH=/home/buildozer/build/contrib/pac/travis
VERCODE_PATCH="$VERCODE_PATCH_PATH/read_apk_version_code.patch"

DOCKER_CMD="pushd /opt/buildozer"
DOCKER_CMD="$DOCKER_CMD && patch -p0 < $VERCODE_PATCH && popd"
DOCKER_CMD="$DOCKER_CMD && rm -rf packages"
DOCKER_CMD="$DOCKER_CMD && ./contrib/make_packages"
DOCKER_CMD="$DOCKER_CMD && rm -rf packages/bls_py"
DOCKER_CMD="$DOCKER_CMD && rm -rf packages/python_bls*"
DOCKER_CMD="$DOCKER_CMD && ./contrib/android/make_apk"

if [[ $ELECTRUM_MAINNET == "false" ]]; then
    DOCKER_CMD="$DOCKER_CMD release-testnet"
fi

sudo chown -R 1000 electrum-pac
docker run --rm \
    --env APP_ANDROID_ARCH=$APP_ANDROID_ARCH \
    --env APK_VERSION_CODE=$DASH_ELECTRUM_VERSION_CODE \
    -v $(pwd)/electrum-pac:/home/buildozer/build \
    -t zebralucky/electrum-pac-winebuild:Kivy40x bash -c \
    "$DOCKER_CMD"

FNAME_TAIL=release-unsigned.apk
if [[ $ELECTRUM_MAINNET == "false" ]]; then
  PATHNAME_START=electrum-pac/bin/electrum_pac/_Testnet
else
  PATHNAME_START=electrum-pac/bin/electrum_pac/
fi
