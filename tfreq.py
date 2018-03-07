from SX127x.LoRa import *
from SX127x.board_config import BOARD
BOARD.setup()
lora = LoRa()
lora.set_mode(MODE.STDBY)
lora.set_freq(433.0)       # Set the frequency to 433 MHz
print 'freq = %s' % lora.get_freq()
BOARD.teardown()
