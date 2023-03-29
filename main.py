import pyqrcode

from pyqrcode import QRCode

s="https://www.youtube.com/watch?v=fNzpcB7ODxQ&t=33821s"

url=pyqrcode.create(s)

url.svg("Link.svg",scale=8)