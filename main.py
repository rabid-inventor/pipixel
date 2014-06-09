

import os, args
from time import sleep as delay
import spidev

try:

  while 1:
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz=(16000000)
    delay(10)
    print(spi.SpiDev_get_mode())
    
    
  
  
