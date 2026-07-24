from enum import IntEnum

class Industry(IntEnum):
    TECH = 0          # Technology
    FIN = 1           # Finance
    HEALTH = 2        # Healthcare
    ENERGY = 3        # Energy
    MFG = 4           # Manufacturing
    RETAIL = 5        # Retail
    CONS = 6          # Consumer Goods
    TELECOM = 7       # Telecommunications
    TRANS = 8         # Transportation
    REALEST = 9       # Real Estate
    CONSTR = 10       # Construction
    MINING = 11       # Mining & Metals
    AGRI = 12         # Agriculture
    FOOD = 13         # Food & Beverage
    MEDIA = 14        # Media & Entertainment
    UTIL = 15         # Utilities
    AERO = 16         # Aerospace & Defense
    AUTO = 17         # Automotive
    CHEM = 18         # Chemicals
    TOUR = 19         # Hospitality & Tourism

INDUSTRY_NAME = {
    Industry.TECH:"Technology",
    Industry.FIN:"Finance",
    Industry.HEALTH: "Healthcare",
    Industry.ENERGY: "Energy",
    Industry.MFG :"Manufacturing",
    Industry.RETAIL : "Retail",
    Industry.CONS : "Consumer Goods",
    Industry.TELECOM: "Telecommunications",
    Industry.TRANS: "Transportation",
    Industry.REALEST: "Real Estate",
    Industry.CONSTR: "Construction",
    Industry.MINING: "Mining & Metals",
    Industry.AGRI: "Agriculture",
    Industry.FOOD :"Food & Beverage",
    Industry.MEDIA: "Media & Entertainment",
    Industry.UTIL: "Utilities",
    Industry.AERO:"Aerospace & Defense",
    Industry.AUTO: "Automotive",
    Industry.CHEM: "Chemicals",
    Industry.TOUR:"Hospitality & Tourism"
}