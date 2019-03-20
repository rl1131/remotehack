"""OOK/PDM Remote control specifications file
   Each data structure in this file represents the set of commands
   which a given remote control supports.
   
   Each structure is a dictionary of MODEs.  Most remotes have only
   one mode, 'global'.  The 'global' mode encompasses all of the 
   BUTTONs that only have 1 function.  If a button has more than
   one function then each of those functions can be grouped into
   a respective MODE.  For instance, my ceiling fan remote has a 
   'Winter' mode and a 'Summer' mode.
   
   Each MODE is, in turn, a dictionary of COMMANDs.  The key for
   each COMMAND is a short, unique, name that is used to specify
   the command when the virtual button is pressed.
   
   Each COMMAND is, again, a dictionary.  Each COMMAND has two 
   dictionary entries (keys), 'name', 'symbols'.
   
   The 'name' is a string that is displayed when a human readable
   name for the command is displayed.
   
   The 'symbols' entry is a list of two-tuples that represent the 
   pulses the radio must send out to execute the given command.
   Each pair represents an on time and an off time for the radio
   transmitter.  The times are given in microseconds.
"""

harbor_breeze_6_speed_dc_remote_0 = {
     'parms': {'inter_packet_gap_us': 10000, 'repeat_count': 10},
     'symbols': {'2h': ((443, 785), (423, 784), (423, 783), (425, 784), (423, 790), (417, 783),
                        (424, 784), (423, 784), (438, 784), (423, 785), (422, 784), (423, 784),
                        (424, 785), (422, 784), (423, 785), (422, 785), (437, 784), (425, 407),
                        (798, 407), (797, 784), (425, 407), (798, 406), (800, 407), (796, 784),
                        (414, 0)),
                 '4h': ((435, 794), (413, 791), (417, 791), (417, 792), (416, 790), (417, 793),
                        (415, 791), (416, 790), (432, 789), (418, 790), (418, 791), (417, 792),
                        (415, 790), (418, 792), (416, 790), (418, 790), (433, 414), (790, 793),
                        (417, 412), (791, 792), (418, 414), (791, 414), (792, 416), (788, 792),
                        (405, 0)),
                 '8h': ((431, 798), (409, 798), (410, 798), (410, 796), (412, 797), (410, 798),
                        (410, 797), (411, 799), (422, 797), (411, 796), (412, 796), (412, 797),
                        (410, 799), (409, 797), (411, 798), (409, 798), (424, 797), (411, 797),
                        (412, 421), (783, 798), (411, 419), (787, 420), (785, 425), (779, 799),
                        (399, 0)),
                 'dn1': ((430, 798), (409, 798), (410, 802), (406, 798), (410, 798), (410, 800),
                         (408, 799), (409, 799), (423, 800), (408, 797), (410, 798), (410, 799),
                         (409, 798), (410, 800), (408, 800), (408, 802), (420, 798), (412, 419),
                         (787, 421), (784, 420), (786, 427), (777, 798), (412, 420), (784, 800),
                         (398, 0)),
                 'dn2': ((430, 798), (410, 797), (411, 797), (411, 796), (412, 797), (410, 798),
                         (410, 798), (410, 797), (424, 798), (410, 798), (410, 797), (411, 797),
                         (411, 800), (408, 797), (410, 798), (410, 797), (427, 419), (785, 796),
                         (413, 418), (788, 418), (788, 419), (785, 798), (411, 419), (785, 797),
                         (401, 0)),
                 'dn3': ((441, 785), (423, 785), (422, 788), (420, 786), (421, 788), (420, 786),
                         (421, 787), (421, 785), (436, 788), (420, 787), (420, 785), (423, 785),
                         (422, 786), (422, 784), (423, 786), (421, 787), (435, 788), (420, 785),
                         (424, 406), (800, 406), (799, 408), (796, 785), (424, 406), (798, 784),
                         (414, 0)),
                 'dn4': ((447, 780), (428, 782), (425, 780), (428, 781), (427, 781), (426, 785),
                         (423, 780), (427, 781), (441, 780), (427, 782), (426, 782), (426, 782),
                         (425, 782), (426, 784), (424, 782), (426, 782), (442, 404), (801, 406),
                         (798, 781), (428, 404), (802, 403), (801, 781), (429, 404), (799, 782),
                         (416, 0)),
                 'dn5': ((442, 785), (423, 785), (422, 786), (422, 784), (424, 785), (422, 784),
                         (424, 785), (422, 785), (437, 785), (423, 784), (423, 788), (420, 787),
                         (420, 785), (423, 785), (423, 785), (422, 783), (439, 784), (426, 409),
                         (794, 784), (426, 407), (798, 407), (797, 784), (426, 406), (797, 785),
                         (413, 0)),
                 'dn6': ((440, 789), (419, 791), (416, 790), (418, 787), (420, 787), (421, 788),
                         (420, 789), (418, 789), (433, 786), (421, 787), (421, 786), (421, 787),
                         (421, 786), (422, 787), (420, 787), (421, 786), (437, 408), (796, 790),
                         (418, 789), (421, 410), (795, 410), (794, 786), (423, 409), (795, 787),
                         (411, 0)),
                 'dnnat': ((439, 789), (418, 788), (420, 789), (418, 788), (420, 787), (420, 789),
                           (419, 787), (420, 786), (435, 788), (420, 789), (418, 788), (420, 787),
                           (421, 787), (420, 787), (421, 786), (421, 788), (433, 788), (420, 788),
                           (419, 789), (421, 410), (795, 409), (794, 788), (422, 412), (791, 789),
                           (409, 0)),
                 'dnpwrtgl': ((439, 790), (418, 790), (418, 790), (418, 791), (417, 790), (418, 790),
                              (417, 793), (415, 789), (433, 789), (419, 789), (418, 790), (418, 790),
                              (418, 790), (418, 789), (419, 790), (418, 789), (434, 412), (794, 414),
                              (792, 412), (794, 413), (793, 412), (792, 792), (418, 412), (792, 791),
                              (406, 0)),
                 'light': ((436, 791), (417, 791), (417, 791), (416, 789), (419, 788), (419, 788),
                           (420, 788), (419, 788), (434, 788), (419, 789), (419, 788), (419, 789),
                           (419, 791), (416, 791), (417, 790), (418, 790), (431, 790), (420, 409),
                           (796, 410), (794, 789), (421, 411), (793, 789), (420, 412), (792, 788),
                           (410, 0)),
                 'off': ((428, 798), (410, 798), (409, 799), (409, 800), (407, 798), (409, 798),
                         (410, 798), (409, 800), (421, 798), (410, 798), (409, 797), (411, 797),
                         (411, 797), (410, 799), (408, 799), (409, 798), (423, 799), (409, 798),
                         (410, 798), (409, 799), (410, 421), (785, 421), (784, 421), (783, 799),
                         (398, 0)),
                 'toggledown': ((434, 791), (416, 792), (416, 794), (414, 788), (419, 791), (417, 790),
                                (418, 790), (417, 789), (433, 790), (417, 792), (416, 790), (418, 793),
                                (414, 791), (417, 792), (416, 790), (417, 792), (432, 412), (793, 414),
                                (792, 414), (789, 791), (419, 414), (790, 789), (420, 414), (790, 793),
                                (405, 0)),
                 'toggleup': ((438, 789), (418, 791), (417, 791), (416, 792), (416, 790), (417, 792),
                              (415, 791), (417, 790), (431, 791), (417, 790), (417, 791), (417, 790),
                              (418, 792), (415, 792), (416, 791), (416, 793), (431, 414), (791, 414),
                              (792, 411), (792, 791), (417, 790), (417, 790), (420, 413), (791, 790),
                              (407, 0)),
                 'up1': ((436, 792), (415, 792), (415, 792), (416, 790), (417, 791), (416, 791),
                         (417, 791), (416, 792), (429, 794), (414, 791), (416, 792), (415, 791),
                         (417, 792), (415, 791), (417, 791), (415, 792), (430, 791), (418, 415),
                         (790, 414), (792, 413), (790, 790), (418, 791), (418, 414), (789, 791),
                         (407, 0)),
                 'up2': ((432, 796), (411, 796), (411, 797), (411, 801), (406, 801), (407, 797),
                         (410, 801), (407, 798), (423, 798), (410, 796), (411, 798), (409, 797),
                         (411, 797), (410, 797), (411, 799), (409, 799), (422, 798), (411, 422),
                         (784, 421), (784, 421), (782, 800), (408, 797), (412, 419), (784, 797),
                         (401, 0)),
                 'up3': ((433, 796), (411, 796), (412, 796), (412, 796), (412, 796), (411, 797),
                         (411, 797), (411, 796), (425, 798), (410, 797), (411, 796), (412, 795),
                         (412, 797), (411, 797), (411, 797), (410, 796), (426, 796), (412, 795),
                         (414, 420), (786, 417), (787, 796), (411, 796), (414, 420), (784, 800),
                         (397, 0)),
                 'up4': ((431, 796), (411, 797), (411, 797), (410, 796), (412, 796), (411, 795),
                         (412, 797), (410, 797), (424, 797), (411, 796), (411, 797), (410, 796),
                         (411, 796), (411, 797), (411, 798), (409, 797), (426, 421), (784, 419),
                         (784, 796), (413, 419), (784, 800), (408, 796), (413, 419), (784, 796),
                         (401, 0)),
                 'up5': ((432, 796), (411, 797), (411, 797), (411, 798), (409, 797), (411, 799),
                         (409, 799), (408, 797), (424, 799), (409, 797), (411, 798), (409, 797),
                         (411, 797), (410, 797), (411, 797), (410, 797), (425, 797), (412, 419),
                         (785, 798), (411, 420), (783, 798), (410, 797), (412, 419), (785, 796),
                         (401, 0)),
                 'up6': ((426, 799), (408, 802), (406, 800), (407, 798), (410, 799), (408, 801),
                         (407, 801), (406, 800), (421, 802), (406, 800), (408, 801), (406, 800),
                         (408, 800), (407, 799), (409, 799), (409, 800), (423, 422), (781, 801),
                         (407, 799), (411, 420), (783, 800), (408, 800), (410, 423), (780, 801),
                         (397, 0)),
                 'upnat': ((428, 799), (409, 798), (409, 799), (408, 804), (403, 799), (409, 798),
                           (410, 800), (407, 798), (424, 799), (408, 799), (409, 797), (410, 800),
                           (408, 799), (408, 799), (408, 800), (408, 797), (424, 799), (409, 799),
                           (408, 800), (410, 421), (782, 798), (410, 798), (411, 420), (783, 799),
                           (399, 0)),
                 'uppwrtgl': ((429, 797), (411, 795), (413, 796), (411, 797), (411, 796), (412, 797),
                              (410, 799), (409, 795), (426, 798), (410, 797), (411, 795), (412, 797),
                              (411, 798), (409, 798), (410, 797), (410, 799), (425, 418), (787, 420),
                              (786, 418), (787, 422), (782, 797), (410, 796), (414, 417), (787, 796),
                              (401, 0))}}



