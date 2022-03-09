#!/usr/bin/env python
'''
    Driver for USB I2C Converter with SC18IM700
    Crescent　2203　v1.0

'''
import serial
import time

I2C_BUS_START_CMD=b'S'
I2C_BUS_STOP_CMD=b'P'
REG_READ_CMD=b'R'
REG_WRITE_CMD=b'W'
GPIO_READ_CMD=b'I'
GPIO_WRITE_CMD=b'O'

class USBI2CCONV:

    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600,bytesize=8, parity='N', stopbits=1, timeout=0.5)
        if(self.ser.isOpen() == False):
            self.ser.open()
        print("Serial Port Connected")
        
    def __del__(self):
        if(self.ser.isOpen() == True):
            self.ser.close();
        print("Serial Port Closed")   
        
    def _i2c_write_addr(self, addr): 
        return (addr << 1) & 0xFE
    
    def _i2c_read_addr(self, addr): 
        return (addr << 1) | 0x01
       
    
    def _tx(self, data):
        self.ser.write(data)
        time.sleep(10/1000)
        #print("Wrote 0x{:X}".format(data))  
        
    def _rx(self, size=1):
        res = self.ser.read(size)
        #res = self.ser.read_all()
        #print("Read 0x{:X}".format(res))
        return res
    
    def reg_write(self, reg, data):
        wdata = REG_WRITE_CMD + bytes([reg]) + bytes([data]) + I2C_BUS_STOP_CMD
        self._tx(wdata)

    def reg_read(self, reg):
        wdata = REG_READ_CMD + bytes([reg]) + I2C_BUS_STOP_CMD
        self._tx(wdata)
        return self._rx(1)
    
    def timeout_enable(self):
        self.reg_write(0x09, 0x67)
    
    def i2c_write(self, i2c_addr, data):
        size = len(data)
        addr = self._i2c_write_addr(i2c_addr)
        wdata = I2C_BUS_START_CMD + bytes([addr, size]) + bytes(data) + I2C_BUS_STOP_CMD
        self._tx(wdata)
   
    def i2c_read(self, i2c_addr, num=1):
        addr = self._i2c_read_addr(i2c_addr)
        wdata = I2C_BUS_START_CMD + bytes([addr, num]) + I2C_BUS_STOP_CMD
        self._tx(wdata)
        return self._rx(num)
    
    def i2c_write_read(self, i2c_addr, write_data, read_num=1):
        wadd = self._i2c_write_addr(i2c_addr)
        raddr= self._i2c_read_addr(i2c_addr)
        size = len(write_data)
        wdata = I2C_BUS_START_CMD + bytes([wadd]) + bytes([size]) + bytes(write_data) 
        self._tx(wdata)
        time.sleep(10/1000)
        wdata = I2C_BUS_START_CMD + bytes([raddr, read_num]) + I2C_BUS_STOP_CMD
        self._tx(wdata)
        time.sleep(10/1000)
        return self._rx(read_num)
    
	    
    def io_read(self):
        return self.reg_read(0x04)
    
    def io_write(self, data):
        return self.reg_write(0x04, data)
    
    def io_conf_set(self, conf):
        self.reg_write(0x02, conf[0])
        self.reg_write(0x03, conf[1])
	
    def i2c_device_search(self):
		self.timeout_enable()
        devlist=[]
        print('*I2C Device Search Start*')
        for addr in range(0x00, 0x7F, 0x02):
            res=self.i2c_read(addr,1)
            if res!=b'':
                print('Device Found: 0x' + '{:X}'.format(addr) + ' (7bit Address)')
                devlist.append(addr)
                #time.sleep(10/1000)
        print('*I2C Device Search End*')
        return devlist
    
