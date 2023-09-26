################################################################################
#   FILE    :   /world/Airport.py
#   DESC    :   Describes an airport object
################################################################################

class Airport:
    def __init__(self,
                 icao,
                 iata,
                 type,
                 name,
                 latitude,
                 longitude,
                 elevation,
                 continent,
                 country,
                 region,
                 municipality,
                 services,
                 gps,
                 local):
        self.icao = icao
        self.iata = iata
        self.type = type
        self.name = name
        self.latitude = latitude,
        self.longitude = longitude
        self.elevation = elevation
        self.continent = continent
        self.country = country
        self.region = region
        self.municipality = municipality
        self.services = services
        self.gps = gps
        self.local = local
    pass

