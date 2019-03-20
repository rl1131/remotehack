from pdm2time import *


remote = RemoteData()
remote.addparam('repeat_count', 10)
remote.addparam('inter_packet_gap_us', 10000)

# Winter stuff

d = pdm2time('Winter_Power_1.wav')
remote.addcmd('up1', 'Air Up Speed1', d)

d = pdm2time('Winter_Power_2.wav')
remote.addcmd('up2', 'Air Up Speed2', d)

d = pdm2time('Winter_Power_3.wav')
remote.addcmd('up3', 'Air Up Speed3', d)

d = pdm2time('Winter_Power_4.wav')
remote.addcmd('up4', 'Air Up Speed4', d)

d = pdm2time('Winter_Power_5.wav')
remote.addcmd('up5', 'Air Up Speed5', d)

d = pdm2time('Winter_Power_6.wav')
remote.addcmd('up6', 'Air Up Speed6', d)


# Summer stuff

d = pdm2time('Summer_Power_1.wav')
remote.addcmd('dn1', 'Air Down Speed1', d)

d = pdm2time('Summer_Power_2.wav')
remote.addcmd('dn2', 'Air Down Speed2', d)

d = pdm2time('Summer_Power_3.wav')
remote.addcmd('dn3', 'Air Down Speed3', d)

d = pdm2time('Summer_Power_4.wav')
remote.addcmd('dn4', 'Air Down Speed4', d)

d = pdm2time('Summer_Power_5.wav')
remote.addcmd('dn5', 'Air Down Speed5', d)

d = pdm2time('Summer_Power_6.wav')
remote.addcmd('dn6', 'Air Down Speed6', d)



d = pdm2time('Winter_Power_Nat.wav')
remote.addcmd('upnat', 'Natural Up Button', d)

d = pdm2time('Summer_Power_Nat.wav')
remote.addcmd('dnnat', 'Natural Down Button', d)

d = pdm2time('Summer_Power_0.wav')
remote.addcmd('dnpwrtgl', 'Toggle Power (Down)', d)

d = pdm2time('Winter_Power_0.wav')
remote.addcmd('uppwrtgl', 'Toggle Power (Up)', d)

d = pdm2time('Winter_Switch.wav')
remote.addcmd('toggleup', 'Air Up Switch', d)

d = pdm2time('Summer_Switch.wav')
remote.addcmd('toggledown', 'Air Down Switch', d)

d = pdm2time('Light.wav')
remote.addcmd('light', 'Light Toggle', d)

d = pdm2time('W2H.wav')
remote.addcmd('2h', '2 Hour Timer', d)

d = pdm2time('W4H.wav')
remote.addcmd('4h', '4 Hour Timer', d)

d = pdm2time('W8H.wav')
remote.addcmd('8h', '8 Hour Timer', d)

d = pdm2time('WHome.wav')
remote.addcmd('off', 'Fan Off', d)




remote.show()
