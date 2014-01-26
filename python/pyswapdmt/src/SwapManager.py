#########################################################################
#
# SwapManager
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
__date__ ="$Aug 21, 2011 4:30:47 PM$"
#########################################################################

from swap.SwapInterface import SwapInterface
from swap.protocol.SwapDefs import SwapState, SwapFunction
from swap.SwapException import SwapException

class SwapManager(SwapInterface):
    """
    SWAP Management Class
    """
    def get_message_type(self, packet):
        """
        Return string defining the type of message

        @param packet: SWAP packet

        @return string
        """
        if packet.function == SwapFunction.COMMAND:
            msgtype = "C"
        elif packet.function == SwapFunction.QUERY:
            msgtype = "Q"
        elif packet.function == SwapFunction.STATUS:
            msgtype = "S"
        else:
            msgtype = "?"

        return msgtype

    def swapPacketReceived(self, packet):
        """
        New SWAP packet received

        @param packet: SWAP packet received
        """
        if self._sniff:
            msgtype = self.get_message_type(packet)
            rssi = "{0:02X}".format(packet.rssi)
            lqi = "{0:02X}".format(packet.lqi)

            print "<-" + msgtype + "-- " + "(" + rssi + lqi + ")" + packet.toString()

    def swapPacketSent(self, packet):
        """
        SWAP packet transmitted

        @param packet: SWAP packet transmitted
        """
        if self._sniff:
            msgtype = self.get_message_type(packet)
            rssi = "{0:02X}".format(packet.rssi)
            lqi = "{0:02X}".format(packet.lqi)

            print "--" + msgtype + "-> " + "(" + rssi + lqi + ")" + packet.toString()

    def newMoteDetected(self, mote):
        """
        New mote detected by SWAP server
        
        'mote'  Mote detected
        """
        if self._printSWAP == True:
            print "New mote with address " + str(mote.address) + " : " + mote.definition.product + \
            " (by " + mote.definition.manufacturer + ")"


    def newEndpointDetected(self, endpoint):
        """
        New endpoint detected by SWAP server
        
        'endpoint'  Endpoint detected
        """
        if self._printSWAP == True:
            print "New endpoint with Reg ID = " + str(endpoint.getRegId()) + " : " + endpoint.name


    def moteStateChanged(self, mote):
        """
        Mote state changed
        
        'mote'  Mote having changed
        """
        if self._printSWAP == True:
            print "Mote with address " + str(mote.address) + " switched to \"" + \
            SwapState.toString(mote.state) + "\""
        # SYNC mode entered?
        if mote.state == SwapState.SYNC:
            self._addrInSyncMode = mote.address


    def moteAddressChanged(self, mote):
        """
        Mote address changed
        
        'mote'  Mote having changed
        """
        if self._printSWAP == True:
            print "Mote changed address to " + str(mote.address)


    def endpointValueChanged(self, endpoint):
        """
        Endpoint value changed
        
        'endpoint' Endpoint object
        """
        if self._printSWAP == True:
            print endpoint.name + " in address " + str(endpoint.getRegAddress()) + " changed to " + endpoint.getValueInAscii()
            
            
    def paramValueChanged(self, param):
        """
        Config parameter value changed
        
        'param' Config parameter object
        """
        if self._printSWAP == True:
            print param.name + " in address " + str(param.getRegAddress()) + " changed to " + param.getValueInAscii()


    def getAddressInSync(self):
        """
        Return the address of the mote currently in SYNC mode
        """
        return self._addrInSyncMode


    def resetAddressInSync(self):
        """
        Reset _addrInSyncMode variable
        """
        self._addrInSyncMode = None


    def __init__(self, settings=None, sniff=False, monitor=False):
        """
        Class constructor
        
        'monitor'  Print out network events or not
        """
        # Superclass call
        SwapInterface.__init__(self, settings)
        # Print SWAP activity
        self._printSWAP = monitor
        self._sniff = sniff
        # Mote address in SYNC mode
        self._addrInSyncMode = None
