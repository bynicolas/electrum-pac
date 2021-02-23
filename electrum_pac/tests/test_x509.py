import unittest

from electrum_pac.x509 import X509

from . import ElectrumTestCase


class TestX509(ElectrumTestCase):
    def test_generalizedtime(self):
        full = X509(b'0\x82\x05F0\x82\x03.\x02\t\x00\xfeV\xd6\xb5?\xb1j\xe40\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x000d1\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x130\x11\x06\x03U\x04\x08\x0c\nCalifornia1!0\x1f\x06\x03U\x04\n\x0c\x18Internet Widgits Pty Ltd1\x1d0\x1b\x06\x03U\x04\x03\x0c\x14testnet.qtornado.com0 \x17\r180206010225Z\x18\x0f21180113010225Z0d1\x0b0\t\x06\x03U\x04\x06\x13\x02US1\x130\x11\x06\x03U\x04\x08\x0c\nCalifornia1!0\x1f\x06\x03U\x04\n\x0c\x18Internet Widgits Pty Ltd1\x1d0\x1b\x06\x03U\x04\x03\x0c\x14testnet.qtornado.com0\x82\x02"0\r\x06\t*\x86H\x86\xf7\r\x01\x01\x01\x05\x00\x03\x82\x02\x0f\x000\x82\x02\n\x02\x82\x02\x01\x00\xc2B\xe0\xa8\xd9$M\xbc)Wx\x0cv\x00\xc0\xfa2Ew:\xce\xa7\xcb\xc8\r?\xea\xc5R(\xc7\xc3Y\xe7zq=\xcd\x8d\xe3\x86\x9ecSI\xc7\x84\xf2~\x91\xd4\x19\xc2;\x97\xe81e\xf2\xeb\xf1\xadw\xa3p\x88A*-\r\xb6Yt\x98R\xe8\x8a\xf9\xb5>"F\xac\x19%\xc8~\x1d\xac\x93A\xffk\xce\xdb\xfc9\x05\xa0\xad\xf9V\x0f0\xa2b\xd0@\xe4\xf1\xb1\xe8\xb1\x10[&\xa1\xff\x13\xcfQ\xb7\x805\xef\xe7tL\xe5|\x08W\x8c\xd72\x9d\'\xeb\x92)3N\x01M\x06\xa9\xdc\xe4\'\x13\x90x\xd8\x830\x97\xa8\xcc2d \xfa\x91\x04\xd0\x1b\xe7\xaa t\x87\xba]\xb5w\x05(\xba\x07\xc2X$~?L\xc5\x03\xb2\xdeQ\xf3\xf3\xdab\xd9\x92\xd9\x86^:\x93\xc9\x86~\xd1\x94\xd4\x80\x9c\xff0\xc6m\xf4\xf0\xd6\x18\x96l\x1d\x0c\xe8\x15 \x8c\x89\xcb\xa4*\xd9\xefg\x844\x81\xb3\xce\xa1\x8a|\xf9h\xc3\xe1!\xfeZ`\xb71\x97Kj\x0b"\xd3\x98T\r\xd9\xbb<r\x0c\xd5Q\xd0L\x02\xcb\x19\x19\xd6\xdf$\xcej\xa8l\xbd\x81\x803\x95\x0e\x907&\x81J\x88\xaf\xa23\xb4q\x96\x08\xa9]}\xb8Rs\x89{\x04\x88/\xc1m\x8c\xe8\\X\x95 \x1cj\xf2(t\xd7\xef\x10-r\xb6\x17L\xce_\x1bf\xc0c\x18\x83\x99\xdf\xd5\xad\x88\xcd \xae\x07 \xed\xb6\xfc[\x9a/f\x92\xce^\x9c\xd9\x064\xb4\xcc\x1d,d\x99\xee\x9a4\xbe\xde0\x92\x8f/keq\x94\x9frf1\xda\xadM_\x11C\x19\x01\xf0\xe0I\x84W\xf9\xaa\xd3\x12ex\x89"\xbfQ\x1f\xbdU\xa0\x92\xa3\x9d\xdb?\x86\x82\x0b\x1e\xe0\x8aSq\xce%\xea4\xfb\x82\x92\x0f\xcf\xaa\xe2\r\xedd\xba\xff\x85\xa2+\xb0x9\xba\'\xd3\xf5\xd6\xfa\xb43\x0b\xd4\xf4\xca\xa5\xb1\xe4[\xe7\xf7\xc3\xd3\xdd\x85)\xac5E\x17\xae\x03fCC(\x06\x1cU\xedM\x90r\xe87\x8d}\xf1i\xfdO\x83\x05\x83\x83y\xd9f,\xe1\xba\xf0\\y\x8d\x08`\xb1\x02\x03\x01\x00\x010\r\x06\t*\x86H\x86\xf7\r\x01\x01\x0b\x05\x00\x03\x82\x02\x01\x00,.\x12jC3\x9fdF\x15\x16\xea*1\x0b[\xfa-\xcf\x80\x17\xf0\xfa\xf4\x96C\xff\xf9\xe9\xa2N\xda\xf1&6\x9ecV~\xea[\x07\xc1R\x03\x95\xd4\x84B\xe2r\x92\xad<mp\xf1\xcb\xb3\x8b\xbf \x08\x12\x1e6\xe3\xad\xbd1\x81\xbe\xaex\x002\xb6\xf9\xa0\xf6\xb7E^"\r\xa0w\x08\x14\xe7\x84\x03q2\x9c\xac\xce>\xc6\x0b\x81\x81k\x0e\xd01\x16\x91\xe4A\x8c\x1a\xe9W\xd4=<\xd4m_\xd4m\xa4H\x14\xc0\xae\x12\xab\x808\xf1\xf9_\xbb\xfb\xd0U\x0e\\\xd3.?\xa36\xe1hstU"\x17P\xcb>\x83\x9c\xaa\x9b\xb7\xe5\xb4\xb5W\xdc\xc1\xee\x91K\x12\xc2\xe1U\xaf\xf7I`\x83\x91\x0c\xc0\xcb\x15\x13!V\xa9\xc1\xca\x1b\x80\xff\xd8\x1f\xd8_+\x83\xcd\xcb%\xd6\xb7\xdc\x8a2\xa8Q\x1f\xbb.\xdf\x05\xb7hD\xab\xea\xe9\xfb.\xdd\x93\xd1\xf0\xb8r\xb9t.\xab\xf6]\xac\xc9U9\x87\x9e\xe36 \x87\xe7eo\x98\xac\xf4\x87\x8e\xf4\xa86\xd3\xcapy\xee\xa0]\xdbA\xb9\x00\xe9_R\xc8\xf7\xca\x13\xc6\xb1Z|c\xe8v\xa24\xac?k\xf1\xc4\x97\x18\x07\xbaU\xc9\xf5? \x95\x8f\x11\xa7\xc9\x8eY\x9c\xdfnx?\x88\xba\x90\xef\x94WU\xb5\xcf\x0b"\xe8\xfe\xa6.\x0cr-\xaf3\x8a\xe6v\xf9\xb91\x87\x91\xc6\xb1\xe9\xb9UP\xf5\x14\xb7\x99\x80\xc0\xc5}\x9a~\x7f\x06\x1e\xb8\x05\xd5\xa2LXO\\73i\x82\xcd\xc6#\xb7\xa4q\xd7\xd4y\xb1d\xaf\xa8\t\x9e1K\xd94\xaf7\x08\x8c);\xd2\xed\x91\xc6\xed\x83\x90\r\xef\x85\xf0\xfeJi\x02;\xf0\x0b\x03\xe7\xc1\x84\xd45\xaeP\xc2Lp\x1akb\xcaP\xe9\xfc\xc1\xc8VPQu\x85\x92l\x12\xb99{\x91\xd0\xa6d\n\xde\xf85\x93e\xfa\\\xf9cKx8\x84"s\xb8\xe52~\x97\x05\xc3\xf6\x1c\xca\x0b\xda\x8b\x90\xfeu5,\x94,\x99\xf9\x9a\xf3T\x8dAZ\xc7\xe9\x95-\x98\xf2\xbaL\x89\xc0?\xba1\xb5\\t|RY_\xc6\xabr\xe8')
        full.check_date()
