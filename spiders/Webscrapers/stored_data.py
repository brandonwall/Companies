__author__ = 'Chase'

'''                           ------GENERATE DATA 1: University of Maryland-----                                    '''

my_data = {"giga": ["Leidos "], "headings": ["Giga Partners", "Mega Partners", "Kilo Partners"], "mega": ["Bloomberg ",
            "Booz Allen Hamilton ", "Capital One ", "Fannie Mae ", "Lockheed Martin ", "ValidaTek "],
           "kilo": ["Accenture  ", "Adobe ", "AINS ", "Appian ", "AQR ", "Cipher Tech Solutions ", "Dante  ",
            "Easy Dynamics ", "Facebook ", "Geico ", "Goldman Sachs ", "Google ", "MicroStrategy ", "NSA ", "Oculus  ",
            "OPIS ", "SIG ", "SuprTEK ", "The Aerospace Corporation  "]}

global giga_partners
global mega_partners
global kilo_partners

giga_partners = my_data.get('giga')
mega_partners = my_data.get('mega')
kilo_partners = my_data.get('kilo')

global umd_g
global umd_m
global umd_k
global umd_total

umd_g = len(giga_partners)
umd_m = len(mega_partners)
umd_k = len(kilo_partners)
umd_total = umd_g + umd_k + umd_m

'''                           ------GENERATE DATA 2: University of Minnesota-----                                   '''

minn_of_u = {"headings": ["3M", "\nAltium, Inc.", "\nAmerican Chemical Society", "\nApplied Research Associates, Inc.",
                          "\nAsahi Kasei Corporation", "\nAshland, Inc.", "\nBASF Corporation",
                          "\nBecton Dickinson and Company", "\nBest Buy Foundation", "\nBoston Scientific Corporation",
                          "\nCabot Corporation", "\nChinese Academy of Sciences", "\nCisco Systems, Inc.",
                          "\nCummins Business Services", "\nDai Nippon Printing Company, Ltd.", "\nDLMC Foundation",
                          "\nE I DuPont De Nemours & Company", "\nEastman Chemical Company", "\nEcolab, Inc.",
                          "\nEmerson Process Management", "\nEvonik Corporation", "\nExxonMobil Corporation",
                          "\nFacebook", "\nFrank J. & Eleanor A. Maslowski Charitable Trust", "\nGalil Medical, Inc.",
                          "\nGE Foundation", "\nGeneral Mills, Inc.", "\nGoogle, Inc.",
                          "\nGordon and Betty Moore Foundation", "\nGraco Foundation", "\nH B Fuller Company",
                          "\nHenkel Corporation", "\nHoneywell Aerospace", "\nHorton Holding, Inc.",
                          "\nHuawei Technologies", "\nIBM International Foundation", "\nInfineum USA, LP",
                          "\nIngersoll-Rand Company", "\nIntel Corporation", "\nInterplastic Corporation",
                          "\nKanomax FMT, Inc.", "\nKimberly-Clark Corporation",
                          "\nLam Research Foundation/Silicon Valley Community Foundation", "\nLonza",
                          "\nMakkah Techno Valley Company", "\nMathers Hydraulics", "\nMeadWestvaco",
                          "\nMedtronic, Inc.", "\nMicrosoft Corporation", "\nMocon Inc.",
                          "\nNational Center for Women & Information Technology", "\nNiron Magnetics, Inc.",
                          "\nNitto Denko Corporation", "\nPhillips 66 Company",
                          "\nPrecast/Prestressed Concrete Institute", "\nProcter & Gamble Company", "\nPTC Corporation",
                          "\nRTP Company", "\nSabic Innovative Plastics US, LLC", "\nSaminco, Inc.", "\nSappi, Ltd.",
                          "\nSeagate Technology", "\nShimakusu, Ltd.", "\nSilicon Valley Community Foundation",
                          "\nSt Jude Medical, Inc.", "\nStarkey Hearing Technologies, Inc.", "\nSupervalu, Inc.",
                          "\nTarget Corporation", "\nThe Bergquist Company", "\nThe Dow Chemical Company",
                          "\nThe McKnight Foundation", "\nThe Valspar Foundation", "\nToray Industries, Inc.",
                          "\nTotal American Services, Inc.", "\nValspar Corporation", "\nVeritas Technologies, LLC",
                          "\nVoya Foundation", "\nXerox Corporation, USA"]}

global minn_sponsors
global minn_tier1
global minn_tier2
global minn_tier3
global minn_total

minn_sponsors = minn_of_u.get('headings')
minn_clean_sponsors = [x.replace('\n', '') for x in minn_sponsors]
minn_sponsors = minn_clean_sponsors

minn_tier1 = 0
minn_tier2 = len(minn_sponsors)
minn_tier3 = 0

minn_total = minn_tier3 + minn_tier2 + minn_tier1

'''                              ------GENERATE DATA 3: University of Illinois-----                                 '''

ill_of_u = {"comps": ["Apple logo", "C3 logo", "otech logo", "Cirrius logo", "Citadel logo", "Climatel logo",
                      "John deere logo", "Facebook logo", "Google logo", "Groupon logo", "GW logo", "IBM logo",
                      "IMC  logo", "Intel logo", "Jump trading logo", "LGS  logo", "MS logo", "Northern Trust logo",
                      "Northrup logo", "NVIDIA logo", "Optiver logo", "State Farm logo", "Texas Inst logo",
                      "Union Pacific logo", "viasat logo", "vmware  logo", "yahoo  logo"]}

global ill_sponsors
global ill_tier1
global ill_tier2
global ill_tier3
global ill_total

ill_sponsors = ill_of_u.get('comps')
ill_new_set = [x.replace(' logo', '') for x in ill_sponsors]
ill_sponsors = ill_new_set

ill_tier1 = 0
ill_tier2 = len(ill_sponsors)
ill_tier3 = 0

ill_total = ill_tier3 + ill_tier2 + ill_tier1


'''                                         ------GENERATE DATA 4: Purdue-----                                       '''

purdue_data = {"table": ["Advisor Level:", "Friend Level:"], "friend": ["Amazon", "AT&T",
                "Blue Horseshoe Solutions, Inc.", "Cerner Corporation", "Chicago Trading Company", "Cisco", "CME Group",
                "Dell EMC", "Delphi\u00a0Technologies", "Discover", "DMI", "Equifax", "ExxonMobil", "Facebook",
                "FactSet Research Systems, Inc.", "General Electric", "Google", "Informatica", "Intel Corporation",
                "Land O'Lakes", "Liberty Mutual", "Lutron Electronics", "Mercury Defense Systems, Inc.",
                "Milliman\u00a0- PRM Analytics", "National Security Agency", "Nielsen", "Oath: A Verizon Company",
                "Polaris", "Raytheon Company", "Rockwell Collins", "Salesforce", "Sandia National Laboratories",
                "State Farm", "TechPoint", "The Climate Corporation", "Union Pacific", "US Foods", "USAA", "Yelp, Inc."],
                "advisor": ["Bloomberg", "The Boeing Company", "Capital One", "Eli Lilly", "Harris Corporation", "IBM",
                "Microsoft", "MISO", "Northrop Grumman", "Qualcomm, Inc.", "West Monroe Partners, LLC"]}


global purdue_friends
global purdue_advisors
global purdue_tier1
global purdue_tier2
global purdue_tier3
global purdue_total

purdue_friends = purdue_data.get('friend')
purdue_advisors = purdue_data.get('advisor')
purdue_tier1 = len(purdue_advisors)
purdue_tier2 = len(purdue_friends)
purdue_tier3 = 0

purdue_total = purdue_tier3 + purdue_tier2 + purdue_tier1

