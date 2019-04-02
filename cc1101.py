# Thanks for the original library go to Nahuel D. Sánchez 
# This is a modified version of his pycc1101 library 
# https://github.com/nahueldsanchez/pycc1101  
# (MIT License)
#
# Modified by Robert Lee for project specific needs.
# https://github.com/rl1131
# I did pear it down pretty significantly ;-) since
# the purpose is to only support OOK modulation
# for RF remote control emulation

import spidev
import time

class TICC1101_OOK(object):
    WRITE_SINGLE_BYTE = 0x00
    WRITE_BURST = 0x40
    READ_SINGLE_BYTE = 0x80
    READ_BURST = 0xC0

    # TI cc1101 Register Addresses
    IOCFG2 = 0x00  # GDO2 Output Pin Configuration
    IOCFG1 = 0x01  # GDO1 Output Pin Configuration
    IOCFG0 = 0x02  # GDO0 Output Pin Configuration
    FIFOTHR = 0x03  # RX FIFO and TX FIFO Thresholds
    SYNC1 = 0x04  # Sync Word, High Byte
    SYNC0 = 0x05  # Sync Word, Low Byte
    PKTLEN = 0x06  # Packet Length
    PKTCTRL1 = 0x07  # Packet Automation Control
    PKTCTRL0 = 0x08  # Packet Automation Control
    ADDR = 0x09  # Device Address
    CHANNR = 0x0A  # Channel Number
    FSCTRL1 = 0x0B  # Frequency Synthesizer Control
    FSCTRL0 = 0x0C  # Frequency Synthesizer Control
    FREQ2 = 0x0D  # Frequency Control Word, High Byte
    FREQ1 = 0x0E  # Frequency Control Word, Middle Byte
    FREQ0 = 0x0F  # Frequency Control Word, Low Byte
    MDMCFG4 = 0x10  # Modem Configuration
    MDMCFG3 = 0x11  # Modem Configuration
    MDMCFG2 = 0x12  # Modem Configuration
    MDMCFG1 = 0x13  # Modem Configuration
    MDMCFG0 = 0x14  # Modem Configuration
    DEVIATN = 0x15  # Modem Deviation Setting
    MCSM2 = 0x16  # Main Radio Control State Machine Configuration
    MCSM1 = 0x17  # Main Radio Control State Machine Configuration
    MCSM0 = 0x18  # Main Radio Control State Machine Configuration
    FOCCFG = 0x19  # Frequency Offset Compensation Configuration
    BSCFG = 0x1A  # Bit Synchronization Configuration
    AGCCTRL2 = 0x1B  # AGC Control
    AGCCTRL1 = 0x1C  # AGC Control
    AGCCTRL0 = 0x1D  # AGC Control
    WOREVT1 = 0x1E  # High Byte Event0 Timeout
    WOREVT0 = 0x1F  # Low Byte Event0 Timeout
    WORCTRL = 0x20  # Wake On Radio Control
    FREND1 = 0x21  # Front End RX Configuration
    FREND0 = 0x22  # Front End TX Configuration
    FSCAL3 = 0x23  # Frequency Synthesizer Calibration
    FSCAL2 = 0x24  # Frequency Synthesizer Calibration
    FSCAL1 = 0x25  # Frequency Synthesizer Calibration
    FSCAL0 = 0x26  # Frequency Synthesizer Calibration
    RCCTRL1 = 0x27  # RC Oscillator Configuration
    RCCTRL0 = 0x28  # RC Oscillator Configuration

    # Configuration Register Details - Registers that Loose Programming in SLEEP State

    FSTEST = 0x29  # Frequency Synthesizer Calibration Control
    PTEST = 0x2A  # Production Test
    AGCTEST = 0x2B  # AGC Test
    TEST2 = 0x2C  # Various Test Settings
    TEST1 = 0x2D  # Various Test Settings
    TEST0 = 0x2E  # Various Test Settings

    # Command Strobe Registers

    SRES = 0x30  # Reset chip
    SFSTXON = 0x31  # Enable and calibrate frequency synthesizer (if MCSM0.FS_AUTOCAL=1).
    # If in RX (with CCA): Go to a wait state where only the synthesizer
    # is running (for quick RX / TX turnaround).

    SXOFF = 0x32  # Turn off crystal oscillator.
    SCAL = 0x33  # Calibrate frequency synthesizer and turn it off.
    # SCAL can be strobed from IDLE mode without setting manual calibration mode.

    SRX = 0x34  # Enable RX. Perform calibration first if coming from IDLE and MCSM0.FS_AUTOCAL=1.
    STX = 0x35  # In IDLE state: Enable TX. Perform calibration first
    # if MCSM0.FS_AUTOCAL=1.
    # If in RX state and CCA is enabled: Only go to TX if channel is clear.

    SIDLE = 0x36  # Exit RX / TX, turn off frequency synthesizer and exit Wake-On-Radio mode if applicable.
    SWOR = 0x38  # Start automatic RX polling sequence (Wake-on-Radio)
    # as described in Section 19.5 if WORCTRL.RC_PD=0.

    SPWD = 0x39  # Enter power down mode when CSn goes high.
    SFRX = 0x3A  # Flush the RX FIFO buffer. Only issue SFRX in IDLE or RXFIFO_OVERFLOW states.
    SFTX = 0x3B  # Flush the TX FIFO buffer. Only issue SFTX in IDLE or TXFIFO_UNDERFLOW states.
    SWORRST = 0x3C  # Reset real time clock to Event1 value.
    SNOP = 0x3D  # No operation. May be used to get access to the chip status byte.

    PATABLE = 0x3E  # PATABLE
    TXFIFO = 0x3F  # TXFIFO
    RXFIFO = 0x3F  # RXFIFO

    # Status Register Details

    PARTNUM = 0xF0  # Chip ID
    VERSION = 0xF1  # Chip ID
    FREQEST = 0xF2  # Frequency Offset Estimate from Demodulator
    LQI = 0xF3  # Demodulator Estimate for Link Quality
    RSSI = 0xF4  # Received Signal Strength Indication
    MARCSTATE = 0xF5  # Main Radio Control State Machine State
    WORTIME1 = 0xF6  # High Byte of WOR Time
    WORTIME0 = 0xF7  # Low Byte of WOR Time
    PKTSTATUS = 0xF8  # Current GDOx Status and Packet Status
    VCO_VC_DAC = 0xF9  # Current Setting from PLL Calibration Module
    TXBYTES = 0xFA  # Underflow and Number of Bytes
    RXBYTES = 0xFB  # Overflow and Number of Bytes
    RCCTRL1_STATUS = 0xFC  # Last RC Oscillator Calibration Result
    RCCTRL0_STATUS = 0xFD  # Last RC Oscillator Calibration Result

    ST_IDLE = 0
    ST_RX   = 1
    ST_TX   = 2
    ST_FSTXON = 3
    ST_CALIBRATE = 4
    ST_SETTLING  = 5
    ST_RXFIFO_OVERFLOW = 6
    ST_TXFIFO_UNDERFLOW = 7
    
    # The device I am using has a 26MHz base clock.  If yours is different, change this.
    CLOCK_RATE_MHZ = 26.0
    
    ook_init_data = [   (IOCFG0,      0x2E),     # GDO0 Output Pin Configuration
                        (IOCFG1,      0x2E),     # GDO0 Output Pin Configuration
                        (IOCFG2,      0x2E),     # GDO0 Output Pin Configuration
                        (FIFOTHR,     0x47),     # RX FIFO and TX FIFO Thresholds
                        (PKTLEN,      0xFF),     # Packet Automation Control
                        (PKTCTRL1,    0x00),     # Packet Automation Control
                        (PKTCTRL0,    0x32),     # Packet Automation Control
                        (FSCTRL1,     0x06),     # Frequency Synthesizer Control
                        (FREQ2,       0x0C),     # Frequency Control Word, High Byte
                        (FREQ1,       0x1E),     # Frequency Control Word, Middle Byte
                        (FREQ0,       0x98),     # Frequency Control Word, Low Byte
                        (MDMCFG4,     0xDB),     # Modem Configuration
                        (MDMCFG3,     0xF8),     # Modem Configuration
                        (MDMCFG2,     0x33),     # Modem Configuration
                        (MDMCFG1,     0x22),     # Modem Configuration
                        (MDMCFG0,     0xF8),     # Modem Configuration
                        (DEVIATN,     0x15),     # Modem Deviation Setting
                        (MCSM1,       0x30),     # Main Radio Control State Machine Configuration
                        (MCSM0,       0x18),     # Main Radio Control State Machine Configuration
                        (FOCCFG,      0x14),     # Frequency Offset Compensation Configuration
                        (WORCTRL,     0xFB),     # Wake On Radio Control
                        (FREND0,      0x11),     # Front End TX Configuration
                        (FSCAL3,      0xE9),     # Frequency Synthesizer Calibration
                        (FSCAL2,      0x2A),     # Frequency Synthesizer Calibration
                        (FSCAL1,      0x00),     # Frequency Synthesizer Calibration
                        (FSCAL0,      0x1F),     # Frequency Synthesizer Calibration
                        (AGCCTRL2,    0x07),     #
                        (AGCCTRL1,    0x00),     #
                        (AGCCTRL0,    0x92),     #
                        (TEST2,       0x81),     # Various Test Settings
                        (TEST1,       0x35)      # Various Test Settings
    ]

    def __init__(self, bus=0, device=0, speed=500000):
        try:
            self._spi = spidev.SpiDev()
            self._spi.open(bus, device)
            self._spi.max_speed_hz = speed
            self.writeGroup(self.ook_init_data)
            # Set OOK on and off radio TX power (0 = None, 0xC2 = +10db)
            self.writeBurst(0x3E, [0x00, 0xC2])
        except Exception as e:
            print(e)

    def setCarrierFrequency(self, freq_mhz=433.0):
        freq = int( freq_mhz /  (self.CLOCK_RATE_MHZ / 65536) )
        self.writeSingleByte(self.FREQ2, (freq >> 16) & 0xFF)
        self.writeSingleByte(self.FREQ1, (freq >>  8) & 0xFF)
        self.writeSingleByte(self.FREQ0, (freq >>  0) & 0xFF)
        return freq

    def _usDelay(self, useconds):
        time.sleep(useconds / 1000000.0)

    def getRxStatus(self):
        b = self._spi.xfer([self.READ_SINGLE_BYTE])
        return ((b[0] & 0x70) >> 4), (b[0] & 0x0F)

    def getTxStatus(self):
        b = self._spi.xfer([self.WRITE_SINGLE_BYTE])
        return ((b[0] & 0x70) >> 4), (b[0] & 0x0F)

    def writeSingleByte(self, address, byte_data):
        return self._spi.xfer([self.WRITE_SINGLE_BYTE | address, byte_data])

    def readSingleByte(self, address):
        return self._spi.xfer([self.READ_SINGLE_BYTE | address, 0x00])[1]

    def writeBurst(self, address, data):
        data.insert(0, (self.WRITE_BURST | address))
        return self._spi.xfer(data)

    def writeGroup( self, group ):
        for a,v in group:
            self.writeSingleByte(a,v)

    def _strobe(self, address):
        return self._spi.xfer([address, 0x00])

    def selfTest(self):
        part_number = self.readSingleByte(self.PARTNUM)
        component_version = self.readSingleByte(self.VERSION)
        # These asserts are based on the documentation
        # Section 29.3 "Status Register Details"
        # On reset PARTNUM == 0x00
        # On reset VERSION == 0x14
        return (part_number == 0x00) and (component_version == 0x14)

    def sidle(self):
        self._strobe(self.SIDLE)
        while (self.readSingleByte(self.MARCSTATE) != 0x01):
            self._usDelay(100)
        self._strobe(self.SFTX)
        self._usDelay(100)

    def reset(self):
        return self._strobe(self.SRES)

    def setTXState(self):
        self._strobe(self.STX)
        self._usDelay(2)

    def setRXState(self):
        self._strobe(self.SRX)
        self._usDelay(2)
