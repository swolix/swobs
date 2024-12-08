#!/usr/bin/env python3
import logging
import random

from bitarray import bitarray

import swobs

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    drv = swobs.drivers.FT2232H("ftdi://ftdi:2232:251633009FEC/1")
    drv.test()
