__author__ = 'Chase'

'''                           ------GENERATE DATA 1: University of Maryland-----                                    '''

my_data = {"giga": ["Leidos "], "headings": ["Giga Partners", "Mega Partners", "Kilo Partners"], "mega": ["Bloomberg ",
            "Booz Allen Hamilton ", "Capital One ", "Fannie Mae ", "Lockheed Martin ", "ValidaTek "],
           "kilo": ["Accenture  ", "Adobe ", "AINS ", "Appian ", "AQR ", "Cipher Tech Solutions ", "Dante  ",
            "Easy Dynamics ", "Facebook ", "Geico ", "Goldman Sachs ", "Google ", "MicroStrategy ", "NSA ", "Oculus  ",
            "OPIS ", "SIG ", "SuprTEK ", "The Aerospace Corporation  "],
            "pricing": ["$10,000 for most companies", "$15,000 - Palantir", "$5,000 scholarship and a 20,000 dollar donation",
                        "$5,000 - x2 companies","3 honorary (Google, Microsoft, AFCEA)"
                        ]}

global giga_partners
global mega_partners
global kilo_partners
global pricing

giga_partners = my_data.get('giga')
mega_partners = my_data.get('mega')
kilo_partners = my_data.get('kilo')
pricing = my_data.get("pricing")

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
                          "\nVoya Foundation", "\nXerox Corporation, USA"],
                "comp_events": ["CSE Winter Light Show", "LeaderShape Institute", "Catalyst by LeaderShape", "CSE Expo", 
                                "CSE Week", "Summer Camps: Discover STEM, Girls Solve It!, and Eureka!", 
                                "CSE Women in Science and Engineering (WISE) Initiative", "CSE President 2019 Emerging Scholars (PES) Program", 
                                "CSE Student Organization Grant Funding", "Summer Computing Academy", "Girls Who Code", 
                                "Engineers Without Borders, University of Minnesota (EWB-UMN)", "SWEekend", "Competitive Project Teams", 
                                "Platinum Partners: $50,000 per year", "Gold Partners: $25,000 per year", "Silver Partners: $10,000 per year", 
                                "Bronze Event/Organization Sponsor: $2,000 per event"], 
                "bronze_comp_plans": ["Companies may select to sponsor particular events, K-12 outreach programs or student organizations and competition teams with a $2,000 contribution. Bronze sponsors will receive logo placement on all promotional materials for the event they select, and will be recognized at the event as a bronze sponsor."], 
                "silver_comp_plans": ["All Bronze Benefits","Sponsorship recognition at up to three events, competitions, or student organizations of their choosing, which includes:", "Opportunity for special interaction with student leaders (see event list for specific opportunities)"], 
                "platn_comp_plans": ["All Bronze, Silver, and Gold Benefits","Logo placement on all promotional materials", "Sponsor recognition in social media", "Recognition as Platinum Partner at the event", "Opportunity for special interaction with student leaders (see event list for specifics of opportunities)"], 
                "gold_comp_plans": ["All Bronze and Silver Benefits","Logo placement on all promotional materials", "Sponsor recognition in social media", "Recognition as Gold Partner at the event"]
                          }

global minn_sponsors
global minn_events
global minn_bronze
global minn_silver
global minn_gold
global minn_platinum
global minn_total

minn_sponsors = minn_of_u.get('headings')
minn_events = minn_of_u.get('comp_events')
minn_bronze = minn_of_u.get('bronze_comp_plans')
minn_silver = minn_of_u.get('silver_comp_plans')
minn_gold = minn_of_u.get('gold_comp_plans')
minn_platinum = minn_of_u.get('platn_comp_plans')


minn_clean_sponsors = [x.replace('\n', '') for x in minn_sponsors]
minn_sponsors = minn_clean_sponsors

minn_tier1 = 0
minn_tier2 = len(minn_sponsors)
minn_tier3 = 0

minn_total =  minn_tier2 

'''                              ------GENERATE DATA 3: University of Illinois-----                                 '''

ill_of_u = {"comps": ["Apple logo", "C3 logo", "otech logo", "Cirrius logo", "Citadel logo", "Climatel logo",
                      "John deere logo", "Facebook logo", "Google logo", "Groupon logo", "GW logo", "IBM logo",
                      "IMC  logo", "Intel logo", "Jump trading logo", "LGS  logo", "MS logo", "Northern Trust logo",
                      "Northrup logo", "NVIDIA logo", "Optiver logo", "State Farm logo", "Texas Inst logo",
                      "Union Pacific logo", "viasat logo", "vmware  logo", "yahoo  logo"],

            "start_ups": ["http://www.1787fp.co", "http://www.500miles.io", "http://www.aplus.com", 
                          "https://www.affirm.com/", "http://www.ag-informatics.com/", "http://www.alightinc.com/",
                            "http://www.apropose.com/", "http://www.atlas5d.com/", "http://www.benecure.com/", 
                            "http://www.blandertechnologies.com/", "https://www.bloc.io/", "http://www.breakfreesolutions.com/about-us/", 
                            "http://cast21.com/", "http://www.civisanalytics.com/apply", "http://www.getclassroomiq.com/", "https://databricks.com", 
                            "http://www.draftpedia.com/", "http://enodoscore.com/", "http://www.granular.ag/", "http://www.highstriderun.com/", 
                            "http://www.hirebrite.com/", "https://www.hoopr.com/", "http://www.impactenterprises.org/", "http://www.inventure.org/", 
                            "http://www.kincha.me/", "http://www.letslinc.com/", "http://www.life-foundry.com/", "http://www.magikstra.com/", 
                            "https://www.maana.io/", "http://www.nextcapital.com/", "http://www.nomwell.co/", "http://novoed.com/", "http://www.novumind.com/", 
                            "http://www.omnivu.net/", "http://runoranj.com/", "http://www.peerwell.co/", "http://www.qeexo.com/", 
                            "http://www.quicketsolutions.com/", "http://www.qumulo.com/#/qumulo_logo", "http://www.reflektion.com/", 
                            "http://www.therentnest.com/", "http://www.retentionscience.com/careers/", "http://tapfwd.com", "http://www.thetekmill.com/", 
                            "http://thinkb1g.com/", "http://tubularlabs.com/", "http://tusimple.ai/", "http://www.varsahealth.com", "https://www.veriflow.net/", 
                            "http://victoryparade.com/", "http://www.virool.com/", "http://www.virtusensetech.com/", "http://www.whamcitylights.com/", 
                            "https://www.wish.com/", "http://www.workspot.com/", "http://www.zesthealth.com"],
            "benefits": ["One-stop-shopping to connect with CS and ECE students.", "A dedicated account manager to help you develop a custom strategy to maximize your sponsorship. ",
                         "Participation in two Corporate Connection After Hours events (fall and spring) ", "Engineering Career Services (ECS) benefits, which includes posting of jobs and internships,database access, and one table at the spring or fall ECS career fair. ", 
                         "The ability to target specific students for inclusion in your recruiting events.", "One \"Corporate Day\" per year or the equivalent in activities and services", 
                         "First consideration for involvement in and sponsorship of student events, activities, scholarships, and projects.", 
                         "Priority consideration for established lectures including Intro to CS, ECE Explorations, and the ECE Colloquium.", "Facilitated access to student groups and organizations.", 
                         "Priority in room and facility scheduling for additional recruitment events.", "No-fee info sessions and tech talks in the ECE Building and Siebel.", 
                         "Publication of company information and announcements in targeted email blasts sent to students.", "The opportunity to include information in weekly electronic newsletters directed at students, faculty, and staff of both departments.", 
                         "Acknowledgment of sponsorship status on The Corporate Connection page via logo, company profile, and link to career page", "A visual presence in select CS and ECE communications tools.", 
                         "Assistance in organizing campus visits.", "Opportunities to further increase student awareness of your company through tech talks and classroom appearances." ], 
            "details": ["All sponsorships support program activities, educational and outreach activities, student projects, student organizations, scholarships, and other investments to strengthen the infrastructure of the CS and ECE Departments.", 
                        "The annual sponsorship contribution is $20,000, and the sponsorship year runs from the beginning of August to end of the following July. Companies already investing in CS and/or ECE may qualify for a reduced sponsorship contribution. Startups and small businesses may also qualify. ",
                        "Your contribution will be receipted by the University of Illinois Foundation. Your receipt will reflect the fair market value of goods and services received in exchange for your sponsorship.", 
                        "The Corporate Connection is a joint program of the Department of Computer Science and Department of Electrical and Computer Engineering at the University of Illinois"]
 
                      }

global ill_sponsors
global ill_startups
global ill_sponsorplan
global ill_moredets
global ill_tier1
global ill_tier2
global ill_tier3
global ill_total

ill_sponsors = ill_of_u.get('comps')
ill_oldstartups = ill_of_u.get('start_ups')
ill_newstartups = [x.replace("http://",'') for x in ill_oldstartups]
ill_holder = [x.replace("https://",'') for x in ill_newstartups]
ill_startups = [x.replace("www.",'') for x in ill_holder]
ill_new_set = [x.replace(' logo', '') for x in ill_sponsors]
ill_sponsors = ill_new_set
ill_sponsorplan = ill_of_u.get('details')
ill_moredets = ill_of_u.get('benefits')


ill_tier1 = len(ill_startups)
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



purdue_plan_descrips = {"advisor_level": ["Benefits include all of the items listed above plus the following:", 
                                          "Interview space in Lawson or Haas as available", 
                                          "Class project opportunity in CS 307/407", 
                                          "Invitation to attend fall CPP meeting in advisory capacity", 
                                          "Class presentation in CS 391 (signup on first-come, first served basis,", 
                                          "Company day (including use of video wall) and tech talk in ", 
                                          " (no company days during February Industry Days)", 
                                          "Reception/lunch with top students following fall CPP meeting"], 
                        "friend_level": ["Attendance at fall career fair and choice of ", " other recruitment activity, ", 
                                          " a company day (including use of video wall) and tech talk", 
                                          " a class presentation in CS 391 (signup on first-come, first-served basis, so Friends may participate if space is available)", 
                                          "Direct contact with CS department", "Opportunity to participate in other recruiting activities such as February Industry Days, Purdue's For Me admission presentations, and Bridge Program", 
                                          "Publicity in CS department (bulletin boards, website, video wall)", "Advertising of partner-sponsored events (company days, etc.)", "Posting of positions in weekly email to students", 
                                          "Salary/placement data", "Assistance in developing strategy to attract candidates", "Link on CS website to corporate web page", "Opportunity to work with/support student organizations as desired", "Opportunity to support CS department with merit-based scholarships", "Invitation to spring awards banquet"], 
                        "details": ["The Corporate Partners Program (CPP) is designed to foster close communication and promote mutually beneficial relationships between select corporations and the Department of Computer Science. This cooperation provides members with increased visibility and communication, interaction with students who may become future employees who are experts in relevant technical fields, and executive involvement. Partnerships provide the Department of Computer Science diversification of funding sources and access to modern instrumentation, as well as professional resources in tune to marketplace needs. It is a true partnership, where both sides benefit.", "Each corporate member is asked to appoint a working contact person. Membership thus ensures a personal communication link and offers individualized service to member companies. Advisor level members are eligible for representation at the fall Corporate Partners meeting. The annual meeting held each fall provides opportunities to participate in curriculum development and networking with students, faculty, and corporate peers."]}


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

global purdue_advisor_plans
global purdue_friend_plans
global purdue_details

purdue_advisor_plans = purdue_plan_descrips.get('advisor_level')
purdue_friend_plans = purdue_plan_descrips.get('friend_level')
purdue_details = purdue_plan_descrips.get('details')


'''                                         ------GENERATE DATA 5: Wisc-Madison-----                                       '''
wisc_mad_data = {"Bronze_5000_Annualy": ["One free career fair (limit 1 table)", "Preferred choice of on-campus interview and career fair dates", 
                "Welcoming message on social media outlets of the Corporate Partners Program with link to employers website or careers site", 
                "Logo/link displayed on Engineering Career Services website and on Corporate Partners Program page on College of Engineering website", 
                "Logo displayed on available poster/electronic screen displays throughout College of Engineering", 
                "Opportunity to organize mock interview or information sessions", "Branding recognition at all career fairs", 
                "Email blast to targeted students relating to employers job postings, special event or info session", 
                "Invitation to participate in the Diversity Spring Welcome event", "Invitation to participate in the Industry Showcase during Innovation Days",
                 "Advance interview schedule sign up prior to career fairs", "Assistance in executing student recruiting events", 
                 "Sponsor of Engineering Career Services Job Search Guide when published", "Employer name and logo on all career fair materials distributed to students"],
              "Gold_25000_Annualy": ["Multiple info sessions & tech talks throughout the year", "Execute employer meet & greet in desired academic department", 
                  "Opportunity to display organization video/promo (30 seconds max) on video boards throughout engineering accompanied with social media postings to engineering pages", 
                  "Article in Perspective magazine highlighting UW-Madison engineering alumni within the organization and the organizations connection to the college"], 
              "Silver_10000_Annualy": ["Two free career fairs (Limit 2 tables)", "Host a corporate day on the College of Engineering campus", 
                  "Support in executing engagement strategy with student organizations and departments, including revenue sharing to streamline campus efforts", 
                  "Opportunity to have a corporate executive speak to students within a department"],
              "Gold_Partners": ["Epic", "Georgia-Pacific", "Hydrite Chemical Co."],
              "Silver_Partners": ["Boston Scientific", "CAT", "Ford", "Greenheck", "Micron", "Oshkosh", "Plexus", "Spectrum Brands", "Sub Zero Wolf", "X-ES, Extreme Engineering Solutions"],
              "Bronze_Partners": ["Abbvie", "Capital One", "Dell", "Ecolab", "G&E, Gas and Electric", "GKN Sinter Metals", "Target"]}


global wisc_mad_gold
global wisc_mad_silver
global wisc_mad_bronze
global wisc_tier1
global wisc_tier2
global wisc_tier3
global wisc_total

global wisc_gold_partners
global wisc_silver_partners
global wisc_bronze_partners

wisc_gold_partners = wisc_mad_data.get('Gold_Partners')
wisc_silver_partners = wisc_mad_data.get('Silver_Partners')
wisc_bronze_partners = wisc_mad_data.get('Bronze_Partners')




wisc_mad_bronze = wisc_mad_data.get('Bronze_5000_Annualy')
wisc_mad_silver = wisc_mad_data.get('Silver_10000_Annualy')
wisc_mad_gold = wisc_mad_data.get('Gold_25000_Annualy')

wisc_tier1 = len(wisc_gold_partners)
wisc_tier2 = len(wisc_silver_partners)
wisc_tier3 = len(wisc_bronze_partners)
wisc_total = wisc_tier1 + wisc_tier2 + wisc_tier3

'''                                         ------GENERATE DATA 6: University of Washington-----                                       '''


wash_data = {"Univ_Benefits": ["The advantages to the University are also substantial. We can learn about current problems in industry. Students become acquainted with industrial needs. The co-op program and summer internships in local and national industry provide students with a complementary element to their education. The result of the interaction is greater excellence in both the research and teaching missions of the school.",], 
            "General_Benefits": ["The program offers many benefits to business and industry. There is the opportunity to influence computing research and education and to participate in long-range technical assessments of problems and directions in the field. Contacts with prospective employees can be established easily; affiliates have early access to student resumes and student and faculty publications. Special seminars and short courses can be arranged. Faculty members are available for informal technical discussions and more formal presentations."], 
            "Benefits": ["attendance at an annual Industry Affiliates Program meeting that features research overviews by faculty, in-depth research presentations and demonstrations by students on current work, working sessions on common technical areas with both faculty and students, and opportunities to interview prospective employees;", "seminars by faculty members at the affiliate company's site (upon request);", "access to online resumes submitted by graduating students at all degree levels, as well as ability to post open positions on CSE's jobs board;", 
                         "announcement of interesting seminars and presentations;", "contact with technical and administrative representatives of other affiliate companies; and", "many opportunities for informal meetings.","Research overviews by faculty and updates on recent developments and research results within the department.", "Small focused sessions organized by research areas where students, faculty, and affiliates can interact in a workshop setting and discuss research areas in depth.", "Demonstrations of software and hardware systems developed by our research projects.", 
                         "One-on-one meetings with individual faculty and students to create and/or continue collaborations.", "Discussion of the educational mission of the department and the continuous changes and improvements made to the curriculum", "Interaction with other affiliate members.", "Opportunities to interview and discuss employment opportunities with our undergraduate and graduate students for both permanent and co-op/internship positions."],
            "Details": ["$250 for individual entrepreneurs or startups with 10 or fewer employees", "$500/year for startups and companies of fewer than 50 employees", "$2,500/year for those with between 50 and 150 employees", "$5,000/year for those with between 150 and 1000 employees", "$10,000/year for larger companies"], 
            "Companies": ["3Tier Environmental Forecast Group", "8VC", "Adaptiva", "Adobe", "Affirm", "Allen Institute for Artificial Intelligence", "airbnb", "Allen Institute", "Allen Institute for Artificial Intelligence", "Amazon", "Amperity", "Andreessen Horowitz", "AppDynamics", "Apple", "Aqua Alert", "Arista Networks", "Axon", "Bizible", "BloomReach", "Blue Origin", "Bonanza", "Bungie", "Chief Architect Software", "Cisco Systems, Inc.", "Classify & Process Inc.", "Clean Power Research", "Clustrix", "Coding Dojo", "Conenza", "Convoy Inc.", "Coupang", "Cozi", "Cray", "Curalate", "Daimler (Mercedes-Benz)", "Deja vu Security", "Dell EMC", "Delphix", "Disney", "DocuSign", "Doosan GridTech", "Edutech Lab, Inc.", "Entrupy Inc.", "Ericsson", "Expeditors", "Extrahop Networks", "F5 Networks", "Facebook", "GE Digital", "GoDaddy", "Google", "Hive Battery", "Hoists Direct", "Huawei", "Hulu", "Icebrg, LLC", "Igneous Systems", "Ignition Partners", "Impinj", "Indeed", "Intel", "Karat", "Kernel Labs", "Kloa", "Lawrence Livermore National Lab", "Lightspeed Venture Partners", "Los Alamos National Laboratory", "Luum", "Madrona Venture Group", "Marchex", "MemSQL", "Meraki", "Mesosphere", "MicaSense", "Microsoft", "mohCare", "NVIDIA", "Noonum", "Nordstrom", "Nutanix", "Nuvoton", "OfferUp", "OpenMarket", "Pacific Northwest National Laboratory", "Palantir Technologies", "PayScale", "Perkins Coie, LLP", "Pixar", "Qualtrics", "Quantcast", "Qumulo", "RareCyte", "RealNetworks", "RealSelf", "Redfin Corporation", "Remitly", "RetailMeNot", "resin.io", "Riot Games", "Sage Bionetworks", "Salesforce.com", "Samsung", "Sandia National Labs", "shopkick", "Sift Science", "Simply Measured", "Socrata", "Splunk", "Starbucks", "StuffMapper", "Tableau Software", "Tellwise", "Tencent", "Tibco", "TUNE", "twitter", "Two Sigma", "UW CoMotion", "Uber", "Unity Technologies", "unravel", "Voyager Capital", "Vulcan", "Washington Research Foundation", "WTIA", "Whitepages", "Workday", "XKL LLC", "Zillow"]}

global wash_comp
global wash_univ_ben
global wash_general_ben
global wash_benefits
global wash_details
global wash_tier1
global wash_tier2
global wash_tier3
global wash_total

wash_comp = wash_data.get('Companies')
wash_univ_ben = wash_data.get('Univ_Benefits')
wash_general_ben = wash_data.get('General_Benefits')
wash_benefits = wash_data.get('Benefits')
wash_details = wash_data.get('Details')

wash_tier1 = 0
wash_tier2 = 0
wash_tier3 = 0
wash_total = len(wash_comp)


global carn_comps
global carn_ben
global carn_details
global carn_tier1
global carn_tier2
global carn_tier3
global carn_total

carn_data={"Comps": ["Oculus", "Microsoft", "Catepillar", "Boeing", "Amazon", "Department of Defense", 
                     "IBM", "NASA", "Google"],
          "Partnership_Ops": ["Fund an Endowed Chair or Fellowship", "Participate in Sponsored Research", 
                              "Sponsor an Event", "Fund a Scholarship","Sponsor a research opportunity", 
                              "Endow a faculty chair", "Join an affiliate center", "License a new technology", 
                              "Create a fellowship or scholarship", "Support a student organization", "Sponsor a capstone project", 
                              "Donate to a lecture series or fund", "Learn about recruitment opportunities","Name a professorship",
                              "Provide a capital gift", "Name a lab or learning space", "Donate equipment or software ", "Name a college or deanship"],
          "Details": [" OurCS has a tradition of working closely  with industry and research groups to both understand critical gender issues in professional  settings, as well as exploring job opportunities for women researchers  in computing related domains.",
                      " The School of Computer Science at Carnegie Mellon University  welcomes sponsors to join us in supporting OurCS for women  undergraduates in the United States and around the world. ", 
                      " Exclusive  sponsorship gives a single company or computing related domain full brand exposure for a single  offering of OurCS. This includes high-profile recognition on the OurCS  web site, and inclusion in CMU-based media articles, press releases and  all event-related announcements. Additionally, sponsors are asked to  recommend potential speakers and mentors for OurCS events.", 
                      " Co-sponsorships provide similar identity opportunities, only shared among two or more co-sponsors and providing around $25,000 each.", " We welcome gifts at any level from secondary sponsors and will provide online visibility and recognition for their contributions! ", 
                      " The two primary value propositions for sponsors are taking a  high-profile leadership position in the global effort to recognize and  encourage women in computer science; and two, direct connection to a  pool of top talent in the field, including access to student resumes (with their permission). For companies and research groups with strong STEM  priorities, this is an opportunity to have a measurable, long-term  impact on the field." ]}


carn_comp = carn_data.get("Comps")
carn_details = carn_data.get("Details")
carn_ben = carn_data.get("Partnership_Ops")
carn_tier1 = 0
carn_tier2 = 0
carn_tier3 = 0
carn_total = len(carn_comp)








