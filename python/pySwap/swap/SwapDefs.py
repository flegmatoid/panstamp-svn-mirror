#########################################################################
#
# SwapDefs
#
# Copyright (c) 2011 Daniel Berenguer <dberenguer@usapiens.com>
#
# This file is part of the panStamp project.
#
# panStamp  is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# panStamp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with panLoader; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
# USA
#
#########################################################################
__author__="Daniel Berenguer"
__date__ ="$Aug 20, 2011 10:36:00 AM$"
#########################################################################

class SwapAddress:
    """ SWAP reserved addresses """
    # Broadcast address
    BROADCAST_ADDR = 0x00
    
class SwapFunction:
    """ SWAP function codes """
    INFO = 0x00
    QUERY = 0x01
    COMMAND = 0x02

class SwapRegId:
    """ Standard register ID's """
    ID_PRODUCT_CODE = 0
    ID_HW_VERSION = 1
    ID_FW_VERSION = 2
    ID_SYSTEM_STATE = 3
    ID_FREQ_CHANNEL = 4
    ID_SECU_OPTION = 5
    ID_SECU_PASSWD = 6
    ID_SECU_NONCE = 7
    ID_NETWORK_ID = 8
    ID_DEVICE_ADDR = 9

class SwapState:
    """ System states """
    RESTART = 0
    RUNNING = 1
    SYNC = 2
    STOP = 3

    @staticmethod
    def toString(state):
        """ Return string defining the system state """
        if state == SwapState.RESTART:
            return "System restarting"
        elif state == SwapState.RUNNING:
            return "System running"
        elif state == SwapState.SYNC:
            return "Synchronization mode"
        elif state == SwapState.STOP:
            return "System stopping"

class SwapType:
    """ Data types """
    BINARY = "bin"
    NUMBER = "num"
    STRING = "str"
    VIRTUAL = "vir"
    INPUT = "inp"
    OUTPUT = "out"