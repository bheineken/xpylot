################################################################################
#   FILE    :   /world/Aircraft.py
#   DESC    :   Describes an aircraft object
################################################################################

class Aircraft:
    def __init__(self,
                 ident,
                 manufacturer,
                 type,
                 mlength,
                 mwingspan,
                 mheight,
                 oew,
                 mtow,
                 payload,
                 mfuel,
                 mspeed,
                 mrange,
                 mceiling,
                 pax,
                 home):
        self.ident = ident
        self.manufacturer = manufacturer
        self.type = type
        self. mlength = mlength
        self.mwingspan = mwingspan
        self.mheight = mheight
        self.oew = oew
        self.mtow = mtow
        self.payload = payload
        self.mfuel = mfuel
        self.mspeed = mspeed
        self.mrange = mrange
        self.mceiling = mceiling
        self.pax = pax
        self.home = home
    pass