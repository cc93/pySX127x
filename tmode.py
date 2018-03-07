from SX127x.LoRa import *
from SX127x.board_config import BOARD
BOARD.setup()
lora = LoRa()
lora.set_mode(MODE.STDBY)
from time import sleep
sleep(2)
print 'mode is',hex(lora.get_mode())
BOARD.teardown()

