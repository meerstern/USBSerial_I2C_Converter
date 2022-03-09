from SC18IM700 import USBI2CCONV 
conv = USBI2CCONV(port='COM14')
devlist = conv.i2c_device_search()
del conv