#execute thankdrop calcs
#this will be used in a lottery for 1 and only nft,
#objective is to say thanks in including us in the contest from march
#organized by sunshine validation
#
#main airdropped accounts were (and are now) HUAHUA
#
#validators huahua: windpowerstake, sunshine, ecostake, carbonzero
#threshold huahua: 10000 huahua
#
#other networks included (but only windpowerstake in this case), just to avoid leaving them behind
#
#
#JUNO
#threshold juno 1
#validators windpowerstake
#
#CERBERUS
#threshold cerberus 10000
#
#EVMOS
#
#hand-picking all reasonable non-dust delegations
#validators windpowerstake
#addresses
#
#NOMIC
#we're working on it

import thankdrop01

print("HUAHUA")
print("WINDPOWERSTAKE")
thankdrop01.thankyou('windpowerstake_huahua_deles.json',10000)
print("SUNSHINE")
thankdrop01.thankyou('sunshine_huahua_deles.json',10000)
print("ECOSTAKE")
thankdrop01.thankyou('ecostake_huahua_deles.json',10000)
print("CARBONZERO")
thankdrop01.thankyou('carbonzero_huahua_deles.json',10000)


print("JUNO")
print("WINDPOWERSTAKE")
thankdrop01.thankyou('windpowerstake_juno_deles.json',1)

print("CERBERUS")
print("WINDPOWERSTAKE")
thankdrop01.thankyou('windpowerstake_cerberus_deles.json',190000)
