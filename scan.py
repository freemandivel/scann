import pygeoip

gip = pygeoip.GeoIP('GeoLiteCity.dat')

rec = gip.record_by_addr('64.233.161.99') #Put hir your IP
for key.val in rec.items():
	print "%s: %s" %(key,val)

