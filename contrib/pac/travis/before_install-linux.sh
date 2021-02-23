#!/bin/bash
set -ev

docker pull zebralucky/electrum-pac-winebuild:Linux40x

docker pull zebralucky/electrum-pac-winebuild:AppImage40x

docker pull zebralucky/electrum-pac-winebuild:Wine40x
