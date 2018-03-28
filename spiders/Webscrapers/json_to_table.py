#!/usr/bin/env python
import stored_data
import sys
import plotly as log
import plotly.plotly as py
import plotly.graph_objs as go
log.tools.set_credentials_file(username='chasew',api_key='5zQ8K1pJ7EkKiU21tLX0')

count_tables = sys.argv[1]
#print count_tables

''' bar graph '''
if count_tables == '0':
  trace0 = go.Bar(
      x=['U of MD', 'U of Minnesota', 'U of Illinois', 'Purdue', 'U of Wisconsin-Madison', 'U of Washington','Carnigie Mellon'],
      y=[stored_data.umd_g, stored_data.minn_tier1, stored_data.ill_tier1, stored_data.purdue_tier1, stored_data.wisc_tier1, stored_data.wash_tier1,stored_data.carn_tier1],
      name='Giga Partners (Tier 1)',
      marker=dict(
          color='rgb(244,66,80)', 
      )
  )

  trace1 = go.Bar(
      x=['U of MD', 'U of Minnesota', 'U of Illinois', 'Purdue', 'U of Wisconsin-Madison','U of Washington','Carnigie Mellon'],
      y=[stored_data.umd_m, stored_data.minn_tier2, stored_data.ill_tier2, stored_data.purdue_tier2, stored_data.wisc_tier2, stored_data.wash_tier2,stored_data.carn_tier2],
      name='Mega Partners (Tier 2)',
      marker=dict(
          color='rgb(66,152,244)',
      )

  )

  trace2 = go.Bar(
      x=['U of MD', 'U of Minnesota', 'U of Illinois', 'Purdue', 'U of Wisconsin-Madison','U of Washington','Carnigie Mellon'],
      y=[stored_data.umd_k, stored_data.minn_tier3, stored_data.ill_tier3, stored_data.purdue_tier3, stored_data.wisc_tier3, stored_data.wash_tier3,stored_data.carn_tier3],
      name='Kilo Partners (Tier 3)',
      marker=dict(
          color='rgb(113,66,244)',
      )
  )

  trace3 = go.Bar(
      x=['U of MD', 'U of Minnesota', 'U of Illinois', 'Purdue', 'U of Wisconsin-Madison','U of Washington',"Carnigie Mellon"],
      y=[stored_data.umd_total, stored_data.minn_total, stored_data.ill_total, stored_data.purdue_total, stored_data.wisc_total, stored_data.wash_total, stored_data.carn_total],
      name='Total',
      marker=dict(
          color='rgb(65, 244, 146)',
      )
  )


  data = [trace0, trace1, trace2, trace3]
  layout = go.Layout(

      barmode='group',
  )



  fig = go.Figure(data=data, layout=layout)
  py.plot(fig, filename='angled-text-bar')
elif count_tables == '1':

 '''                           ------GENERATE TABLE 1: University of Maryland------                                   '''

 umd_headerColor = 'rgb(255, 0, 0)'
 umd_rowEvenColor = 'rgb(255, 160, 131)'
 umd_rowOddColor = 'white'

 count = 1
 umd_highest = []
 umd_row_colors = []
 while (count < stored_data.umd_k):
     umd_highest.append(count)
     count += 1
     if count % 2 == 0:
         umd_row_colors.append(umd_rowEvenColor)
     else:
         umd_row_colors.append(umd_rowOddColor)


 trace0 = go.Table(
   type = 'table',
   header = dict(
     values = [['<b>University of Maryland:</b> Partner Level'],
                   ['<b>Tier 1: Giga</b>'],
                   ['<b>Tier 2: Mega</b>'],
                   ['<b>Tier 3: Kilo</b>'],
                   ['<b>Pricing Info</b>']],

     line = dict(color = 'black'),
     fill = dict(color = umd_headerColor),
     align = ['left','center'],
     font = dict(color = 'white', size = 12)
   ),
   cells = dict(
     values = [
       [umd_highest],
       [stored_data.giga_partners],
       [stored_data.mega_partners],
       [stored_data.kilo_partners],
       [stored_data.pricing]],
       
     line = dict(color = 'black'),
     fill = dict(color = [umd_row_colors]),
     align = ['left', 'center'],
     font = dict(color = 'black', size = 11)
     ))
 data = [trace0]

 py.plot(data, filename = "UMD data table")

elif count_tables == '2': 

  '''                           ------GENERATE TABLE 2: University of Minnesota-----                                   '''

  minn_headerColor = 'rgb(221, 8, 8)'
  minn_rowEvenColor = 'rgb(255, 216, 165)'
  minn_rowOddColor = 'white'

  count = 1
  minn_highest = []
  minn_row_colors = []
  while (count < stored_data.minn_tier2):
      minn_highest.append(count)
      count += 1
      if count % 2 == 0:
          minn_row_colors.append(minn_rowEvenColor)
      else:
          minn_row_colors.append(minn_rowOddColor)


  trace1 = go.Table(
    type = 'table',
    header = dict(
      values = [['<b>University of Minnesota:</b> Partner Level'],
                    ['<b>Sponsors</b>'],
                    ['<b>Potentional Sponsorship Oppurtunities </b>'],
                    ['<b>Bronze Plan ($2,000 per year)</b>'],
                    ['<b>Silver Plan ($10,000 per year)</b>'],
                    ['<b>Gold Plan ($25,000 per year)</b>'],
                    ['<b>Platinum Plan ($50,000 per year)</b>']],

      line = dict(color = '#506784'),
      fill = dict(color = minn_headerColor),
      align = ['left','center'],
      font = dict(color = 'white', size = 12)
    ),
    cells = dict(
      values = [
        [minn_highest],
        [stored_data.minn_sponsors],
        [stored_data.minn_events],
        [stored_data.minn_bronze],
        [stored_data.minn_silver],
        [stored_data.minn_gold],
        [stored_data.minn_platinum]],
        

      line = dict(color = 'rgb(17, 17, 17)'),
      fill = dict(color = [minn_row_colors]),
      align = ['left', 'center'],
      font = dict(color = 'rgb(17, 17, 17)', size = 11)
      ))

  data = [trace1]

  py.plot(data, filename = "Minnesota data table")



elif count_tables=='3':
  '''                           ------GENERATE TABLE 3: University of Illinois-----                                   '''

  ill_headerColor = 'rgb(0, 33, 224)'
  ill_rowEvenColor = 'rgb(164, 205, 255)'
  ill_rowOddColor = 'white'

  count = 1
  ill_highest = []
  ill_row_colors = []
  while count < stored_data.ill_tier1:
      ill_highest.append(count)
      count += 1
      if count % 2 == 0:
          ill_row_colors.append(ill_rowEvenColor)
      else:
          ill_row_colors.append(ill_rowOddColor)


  trace2 = go.Table(
    type = 'table',
    header = dict(
      values = [['<b>University of Illinois:</b> Partner Level'],
                    ['<b>Tier 1: Start Ups ($20,000 per year)</b>'],
                    ['<b>Tier 2: Sponsors ($20,000 per year)</b>'],
                    ['<b>Tier 3: Sponsorship Details</b>'],
                    ['<b>Tier 4: Sponsorship Advantages</b>']],

      line = dict(color = '#506784'),
      fill = dict(color = ill_headerColor),
      align = ['left','center'],
      font = dict(color = 'white', size = 12)
    ),
    cells = dict(
      values = [
        [ill_highest],
        [stored_data.ill_startups],
        [stored_data.ill_sponsors],
        [stored_data.ill_sponsorplan],
        [stored_data.ill_moredets]],

      line = dict(color = 'rgb(17, 17, 17)'),
      fill = dict(color = [ill_row_colors]),
      align = ['left', 'center'],
      font = dict(color = 'rgb(17, 17, 17)', size = 11)
      ))

  data = [trace2]

  py.plot(data, filename = "Illinois data table")

elif count_tables=='4':
  
  '''                                        ------GENERATE TABLE 4: Purdue-----                                      '''

  purdue_headerColor = 'rgb(219, 182, 63)'
  purdue_rowEvenColor = 'rgb(255, 225, 130)'
  purdue_rowOddColor = 'white'

  count = 1
  purdue_highest = []
  purdue_row_colors = []
  while count < stored_data.purdue_tier2:
      purdue_highest.append(count)
      count += 1
      if count % 2 == 0:
          purdue_row_colors.append(purdue_rowEvenColor)
      else:
          purdue_row_colors.append(purdue_rowOddColor)


  trace3 = go.Table(
    type = 'table',
    header = dict(
      values = [['<b>University of Purdue:</b> Partner Level'],
                ['<b>Tier 1: Advisor ($10,000 per year)</b>'],
                ['<b>Tier 2: Friend ($5,000 per year)</b>'],
                ['<b>Tier 3: </b>'],
                ['<b>Advisor Description:</b>'],
                ['<b>Friend Description:</b>'],
                ['<b>Additional Details:</b>']],

      line = dict(color = '#506784'),
      fill = dict(color = purdue_headerColor),
      align = ['left','center'],
      font = dict(color = 'white', size = 12)
    ),
    cells = dict(
      values = [
        [purdue_highest],
        [stored_data.purdue_advisors],
        [stored_data.purdue_friends],
        [['']],
        [stored_data.purdue_advisor_plans],
        [stored_data.purdue_friend_plans],
        [stored_data.purdue_details]],

      line = dict(color = 'rgb(17, 17, 17)'),
      fill = dict(color = [purdue_row_colors]),
      align = ['left', 'center'],
      font = dict(color = 'rgb(17, 17, 17)', size = 11)
      ))

  data = [trace3]

  py.plot(data, filename = "Purdue data table")

elif count_tables=='5':
  
  '''                                        ------GENERATE TABLE 5: Wisc Madison -----                                      '''

  wisc_headerColor = 'rgb(255, 96, 112)'
  wisc_rowEvenColor = 'white'
  wisc_rowOddColor = 'rgb(255, 221, 137)'

  count = 1
  wisc_highest = []
  wisc_row_colors = []
  while count < len(stored_data.wisc_mad_bronze):
      wisc_highest.append(count)
      count += 1
      if count % 2 == 0:
          wisc_row_colors.append(wisc_rowEvenColor)
      else:
          wisc_row_colors.append(wisc_rowOddColor)


  trace3 = go.Table(
    type = 'table',
    header = dict(
      values = [['<b>Wisconsin-Madison:</b> Partner Level'],
                ['<b>Tier 1: Gold ($25,000 Annualy)</b>'],
                ['<b>Tier 2: Silver ($10,000 Annualy)</b>'],
                ['<b>Tier 3: Bronze ($5,000 Annualy)</b>'],
                ['<b>Gold Description:</b>'],
                ['<b>Silver Description:</b>'],
                ['<b>Bronze Descritpion</b>']],

      line = dict(color = '#506784'),
      fill = dict(color = wisc_headerColor),
      align = ['left','center'],
      font = dict(color = 'white', size = 12)
    ),
    cells = dict(
      values = [
        [wisc_highest],
        [stored_data.wisc_gold_partners],
        [stored_data.wisc_silver_partners],
        [stored_data.wisc_bronze_partners],
        [stored_data.wisc_mad_gold],
        [stored_data.wisc_mad_silver],
        [stored_data.wisc_mad_bronze]],

      line = dict(color = 'rgb(17, 17, 17)'),
      fill = dict(color = [wisc_row_colors]),
      align = ['left', 'center'],
      font = dict(color = 'rgb(17, 17, 17)', size = 11)
      ))

  data = [trace3]

  py.plot(data, filename = "Wisconsin Madison data table")

elif count_tables=='6':
  
  '''                                        ------GENERATE TABLE 6: U of Washington-----                                      '''

  wash_headerColor = 'rgb(159, 43, 255)'
  wash_rowEvenColor = 'white'
  wash_rowOddColor = 'rgb(255, 249, 183)'

  count = 1
  wash_highest = []
  wash_row_colors = []
  while count < len(stored_data.wash_comp):
      wash_highest.append(count)
      count += 1
      if count % 2 == 0:
          wash_row_colors.append(wash_rowEvenColor)
      else:
          wash_row_colors.append(wash_rowOddColor)


  trace3 = go.Table(
    type = 'table',
    header = dict(
      values = [['<b>University of Washington:</b> Partner Level'],
                ['<b>Corporate Affiliate Partners</b>'],
                ['<b>Plan Details</b>'],
                ['<b>Company Benefits</b>'],
                ['<b>General Benefits</b>'],
                ['<b>University Benefits</b>']],

      line = dict(color = '#506784'),
      fill = dict(color = wash_headerColor),
      align = ['left','center'],
      font = dict(color = 'white', size = 12)
    ),
    cells = dict(
      values = [
        [wash_highest],
        [stored_data.wash_comp],
        [stored_data.wash_details],
        [stored_data.wash_benefits],
        [stored_data.wash_general_ben],
        [stored_data.wash_univ_ben]],

      line = dict(color = 'rgb(17, 17, 17)'),
      fill = dict(color = [wash_row_colors]),
      align = ['left', 'center'],
      font = dict(color = 'rgb(17, 17, 17)', size = 11)
      ))

  data = [trace3]

  py.plot(data, filename = "University of Washington data table")



elif count_tables == '7':

  '''                                        ------GENERATE TABLE 7: Carnigie Mellon U-----                                      '''

  carn_headerColor = 'rgb(196, 30, 58)'
  carn_rowEvenColor = 'white'
  carn_rowOddColor = 'rgb(128,128,128)'

  count = 1
  carn_highest = []
  carn_row_colors = []
  while count < len(stored_data.carn_ben):
      carn_highest.append(count)
      count += 1
      if count % 2 == 0:
          carn_row_colors.append(carn_rowEvenColor)
      else:
          carn_row_colors.append(carn_rowOddColor)


  trace3 = go.Table(
    type = 'table',
    header = dict(
      values = [['<b>Carnegie Mellon University:</b> Partner Level'],
                ['<b>Sponsors</b>'],
                ['<b>Company Oppurtunities</b>'],
                ['<b>Additional Details</b>']],

      line = dict(color = '#506784'),
      fill = dict(color = carn_headerColor),
      align = ['left','center'],
      font = dict(color = 'white', size = 12)
    ),
    cells = dict(
      values = [
        [carn_highest],
        [stored_data.carn_comp],
        [stored_data.carn_ben],
        [stored_data.carn_details]],

      line = dict(color = 'rgb(17, 17, 17)'),
      fill = dict(color = [carn_row_colors]),
      align = ['left', 'center'],
      font = dict(color = 'rgb(17, 17, 17)', size = 11)
      ))

  data = [trace3]

  py.plot(data, filename = "Carnigie Mellon University data table")
else: 
  print "Incorrect Number."
