import sys
import wave
import pprint


def pdm2time(file_name, window_size=10, quiet=True):

    """Very quick and dirty function to convert a fairly clean
       already demodulated OOK signal into on-off time pairs.
       The input is a .wav file (exported from say "Universal
       Radio Hacker").
       .wav file is expected to have 2 bytes per sample"""
       

    wfile = wave.open(file_name,'r')
    if not quiet:
        print("pdm2time working on {}".format(file_name))
        print("Samples per second:  ",wfile.getframerate())
        print("Sample count:  ",wfile.getnframes())
    data = wfile.readframes(wfile.getnframes())
    swidth = wfile.getsampwidth()
    wfile.close()

    if swidth != 2:
       print("ERROR:  Wave file must be 2 bytes per sample.  Did you export from Universal Radio Hacker?")
       return
    
    freq = wfile.getframerate()

    i = 0
    samples = []
    window = [0] * window_size
    widx = 0
    total = 0
    high = 0
    low = 0x10000
    while i < len(data) - 1:
        val = int(data[i]) + (int(data[i+1]) << 8)
        total = total + val
        window[widx] = val
        widx = widx + 1
        if widx >= window_size:
            widx = 0
        s = int(sum(window) / window_size)
        samples.append(s)
        if s > high:
            high = s
        if s < low:
            low = s
        i = i + 2

    avg = int((high - low) / 2) + low

    # Find the starting edge
    i = 0
    while samples[i] < avg:
        i = i + 1

    ptimes = []

    done = False
    while not done:
        i0 = i
        while samples[i] >= avg:
            i = i + 1
        i1 = i
        try:
            while samples[i] < avg:
                i = i + 1
            i2 = i
        except IndexError:
            i2 = i1
            done = True
        hi_time_us = int(((i1-i0) / freq) * 1000000)
        lo_time_us = int(((i2-i1) / freq) * 1000000)
        ptimes.append( (hi_time_us, lo_time_us) )

    return tuple(ptimes)

class RemoteData:

    def __init__(self):
        self.dstruct = dict()
        self.dstruct['parms'] = dict()
        self.dstruct['symbols'] = dict()
        self.pp = pprint.PrettyPrinter(width=100, compact=True)

    def addparam(self, pname, pvalue):
        self.dstruct['parms'][pname] = pvalue

    def addcmd(self, commandid, name, symbols):
        self.dstruct['symbols'][commandid] = symbols

    def show(self):
        self.pp.pprint(self.dstruct)

