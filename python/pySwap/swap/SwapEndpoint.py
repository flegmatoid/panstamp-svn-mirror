#########################################################################
#
# SwapEndpoint
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

from swap.SwapDefs import SwapType
from swap.SwapValue import SwapValue
from swap.SwapParam import SwapParam

class SwapEndpoint(SwapParam):
    """
    SWAP endpoint class
    """

    def getRegAddress(self):
        """
        Return register address
        """
        return self.register.getAddress()

    def getRegId(self):
        """
        Return register id
        """
        return self.register.id

  
    def sendSwapCmd(self, value):
        """
        Send SWAP command for the current endpoint
        
        'value'     New endpoint value
        
        Return expected SWAP info response to be received from the mote
        """

        # Insert new endpoint value into the current register value
        lstValue = self.register.value
        lstValue[self.bytePos: self.bytePos + self.byteSize] = value.toList()

        # Convert to SWapValue
        newVal = SwapValue(lstValue)

        # Send SWAP command
        return self.register.sendSwapCmd(newVal)


    def sendSwapQuery(self):
        """
        Send SWAP query for the current endpoint
        """
        self.register.sendSwapQuery()

    
    def sendSwapInfo(self):
        """
        Send SWAP info packet about this endpoint
        """
        self.register.sendSwapInfo()
    
    def __init__(self, register=None, pType=SwapType.NUMBER, direction=SwapType.INPUT,
                description=None, position="0", size="1", default=None):
        """
        Class constructor

        'register'      Register containing this endpoint
        'type'          Type of SWAP endpoint (see SwapDefs.SwapType)
        'direction'     Input or output (see SwapDefs.SwapType)
        'description'   Short description about hte endpoint
        'position'      Position in bytes within the parent register
        'size'          Size in bytes
        'default'       Default value in string format
        """
        SwapParam.__init__(self, register, pType, direction, description, position, size, default)