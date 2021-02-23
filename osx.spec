# -*- mode: python -*-
import os
import os.path
import sys
from PyInstaller.utils.hooks import (collect_data_files, collect_submodules,
                                     collect_dynamic_libs)


for i, x in enumerate(sys.argv):
    if x == '--name':
        cmdline_name = sys.argv[i+1]
        break
else:
    raise Exception('no name')

PY36BINDIR = os.environ.get('PY36BINDIR')
GITHUB_REF = os.environ.get('GITHUB_REF')
DASH_ELECTRUM_VERSION = os.environ.get('DASH_ELECTRUM_VERSION')
ICONS_FILE = 'electrum_pac/gui/icons/electrum-pac.icns'

hiddenimports = []
hiddenimports += collect_submodules('pkg_resources')  # workaround for https://github.com/pypa/setuptools/issues/1963
hiddenimports += collect_submodules('trezorlib')
hiddenimports += collect_submodules('safetlib')
hiddenimports += collect_submodules('btchip')
hiddenimports += collect_submodules('keepkeylib')
hiddenimports += collect_submodules('websocket')

# safetlib imports PyQt5.Qt.  We use a local updated copy of pinmatrix.py until they
# release a new version that includes https://github.com/archos-safe-t/python-safet/commit/b1eab3dba4c04fdfc1fcf17b66662c28c5f2380e
hiddenimports.remove('safetlib.qt.pinmatrix')

hiddenimports += [
    'electrum_pac',
    'electrum_pac.base_crash_reporter',
    'electrum_pac.base_wizard',
    'electrum_pac.plot',
    'electrum_pac.qrscanner',
    'electrum_pac.websockets',
    'electrum_pac.gui.qt',
    'PyQt5.sip',
    'PyQt5.QtPrintSupport',  # needed by Revealer

    'electrum_pac.plugins',

    'electrum_pac.plugins.hw_wallet.qt',

    'electrum_pac.plugins.audio_modem.qt',
    'electrum_pac.plugins.cosigner_pool.qt',
    'electrum_pac.plugins.digitalbitbox.qt',
    'electrum_pac.plugins.email_requests.qt',
    'electrum_pac.plugins.keepkey.qt',
    'electrum_pac.plugins.revealer.qt',
    'electrum_pac.plugins.labels.qt',
    'electrum_pac.plugins.trezor.qt',
    'electrum_pac.plugins.safe_t.client',
    'electrum_pac.plugins.safe_t.qt',
    'electrum_pac.plugins.ledger.qt',
    'electrum_pac.plugins.virtualkeyboard.qt',
]

datas = [
    ('electrum_pac/checkpoints*.*', 'electrum_pac'),
    ('electrum_pac/*.json', 'electrum_pac'),
    ('electrum_pac/locale', 'electrum_pac/locale'),
    ('electrum_pac/wordlist', 'electrum_pac/wordlist'),
    ('electrum_pac/gui/icons', 'electrum_pac/gui/icons'),
]

datas += collect_data_files('trezorlib')
datas += collect_data_files('safetlib')
datas += collect_data_files('btchip')
datas += collect_data_files('keepkeylib')

# Add the QR Scanner helper app
if GITHUB_REF:
    QRREADER_ZPATH = 'contrib/CalinsQRReader/build/Release/CalinsQRReader.app'
    QRREADER_PATH = './contrib/CalinsQRReader/build/Release/CalinsQRReader.app'
    datas += [(QRREADER_ZPATH, QRREADER_PATH)]

# Add libusb so Trezor and Safe-T mini will work
binaries = []
binaries += [('libusb-1.0.dylib', '.')]
binaries += [('libsecp256k1.0.dylib', '.')]
binaries += [('libgmp.10.dylib', '.')]  # need by libsecp256k1.0.dylib

# Workaround for "Retro Look":
binaries += [b for b in collect_dynamic_libs('PyQt5') if 'macstyle' in b[0]]

# https://github.com/pyinstaller/pyinstaller/wiki/Recipe-remove-tkinter-tcl
sys.modules['FixTk'] = None
excludes = ['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter']
excludes += [
    'PyQt5.QtBluetooth',
    'PyQt5.QtCLucene',
    'PyQt5.QtDBus',
    'PyQt5.Qt5CLucene',
    'PyQt5.QtDesigner',
    'PyQt5.QtDesignerComponents',
    'PyQt5.QtHelp',
    'PyQt5.QtLocation',
    'PyQt5.QtMultimedia',
    'PyQt5.QtMultimediaQuick_p',
    'PyQt5.QtMultimediaWidgets',
    'PyQt5.QtNetwork',
    'PyQt5.QtNetworkAuth',
    'PyQt5.QtNfc',
    'PyQt5.QtOpenGL',
    'PyQt5.QtPositioning',
    'PyQt5.QtQml',
    'PyQt5.QtQuick',
    'PyQt5.QtQuickParticles',
    'PyQt5.QtQuickWidgets',
    'PyQt5.QtSensors',
    'PyQt5.QtSerialPort',
    'PyQt5.QtSql',
    'PyQt5.Qt5Sql',
    'PyQt5.Qt5Svg',
    'PyQt5.QtTest',
    'PyQt5.QtWebChannel',
    'PyQt5.QtWebEngine',
    'PyQt5.QtWebEngineCore',
    'PyQt5.QtWebEngineWidgets',
    'PyQt5.QtWebKit',
    'PyQt5.QtWebKitWidgets',
    'PyQt5.QtWebSockets',
    'PyQt5.QtXml',
    'PyQt5.QtXmlPatterns',
    'PyQt5.QtWebProcess',
    'PyQt5.QtWinExtras',
]

a = Analysis(['electrum-pac'],
             hiddenimports=hiddenimports,
             datas=datas,
             binaries=binaries,
             excludes=excludes,
             runtime_hooks=['pyi_runtimehook.py'])

# http://stackoverflow.com/questions/19055089/
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

# Strip out parts of Qt that we never use. Reduces binary size by tens of MBs. see #4815
qt_bins2remove=('qtweb', 'qt3d', 'qtgame', 'qtdesigner', 'qtquick', 'qtlocation', 'qttest', 'qtxml')
print("Removing Qt binaries:", *qt_bins2remove)
for x in a.binaries.copy():
    for r in qt_bins2remove:
        if x[0].lower().startswith(r):
            a.binaries.remove(x)
            print('----> Removed x =', x)

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          debug=False,
          strip=False,
          upx=False,
          console=False,
          icon='electrum_pac/gui/icons/electrum-pac.ico',
          name=os.path.join('electrum-pac', cmdline_name))

coll = COLLECT(exe,
               a.binaries,
               a.datas,
               strip=False,
               upx=False,
               name=os.path.join('dist', 'electrum-pac'))

app = BUNDLE(coll,
             info_plist={
                'NSHighResolutionCapable': True,
                'NSSupportsAutomaticGraphicsSwitching': True,
                'CFBundleURLTypes': [
                    {'CFBundleURLName': 'dash', 'CFBundleURLSchemes': ['dash']}
                ],
             },
             name=os.path.join('dist', 'PacGlobal Electrum.app'),
             appname="PacGlobal Electrum",
	         icon=ICONS_FILE,
             version=DASH_ELECTRUM_VERSION)
