from SC18IM700 import USBI2CCONV 
conv = USBI2CCONV(port='COM14')
#HS3001

# Pattern1 write_read
i2caddr=0x44
wdata = [0x00]
conv.i2c_write(i2caddr,wdata)
time.sleep(30/1000)
res=conv.i2c_write_read(0x44,wdata,4)

#Calc Humd
hmd=((res[0]&0x3F)<<8)+res[1]
hmdf=hmd/(pow(2,14)-1)*100.0
#Calc Temp
tmp=(res[2]<<8)+res[3]
tmp=tmp>>2
tmpf=tmp/(pow(2,14)-1)*165-40
print('TEMP: ' + '{:.2f}'.format(tmpf) + ' ℃')
print('HUMD: ' + '{:.2f}'.format(hmdf)+' ％')

# Pattern2 write & read
i2caddr=0x44 #7bit Addr (without R/W bit)
rdata = 4
wdata = [0x00]
conv.i2c_write(i2caddr,wdata)
time.sleep(30/1000)
res=conv.i2c_read(i2caddr,rdata)
#Calc Humd
hmd=((res[0]&0x3F)<<8)+res[1]
hmdf=hmd/(pow(2,14)-1)*100.0
#Calc Temp
tmp=(res[2]<<8)+res[3]
tmp=tmp>>2
tmpf=tmp/(pow(2,14)-1)*165-40
print('TEMP: ' + '{:.2f}'.format(tmpf) + ' ℃')
print('HUMD: ' + '{:.2f}'.format(hmdf)+' ％')
del conv