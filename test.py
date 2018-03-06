import json
import plotly.plotly as py
import plotly.graph_objs as go

'''
with open('therealumdscrape.json') as json_data:
    d = json.load(json_data)
'''
json_data = json.load(open('therealumdscrape.json'))



'''Generate the graph '''
giga_partners = [1]
giga_partners[0] = 'Leidos'

i = 0
mega_partners = [len(d[2])]
for s in d[2]:
  mega_partners[i] = s
  i += 1

j = 0
kilo_partners = [len(d[3])]
for s in d[3]:
  mega_partners[j] = s
  j += 1 




headerColor = 'red'
rowEvenColor = 'white'
rowOddColor = 'lightgrey'

trace0 = go.Table(
  type = 'table',
  header = dict(
    values = [['<b>University of Maryland</b>'],
                  ['<b>Giga</b>'],
                  ['<b>Mega</b>'],
                  ['<b>Kilo</b>']],
                  
    line = dict(color = '#506784'),
    fill = dict(color = headerColor),
    align = ['left','center'],
    font = dict(color = 'white', size = 12)
  ),
  cells = dict(

    values = [
      [['Types of Partners', ' ', ' ', ' ', '<b>TOTAL</b>']],
      [giga_partners],
      [mega_partners],
      [kilo_partners],
      [1, len(mega_partners), len(kilo_partners)]],

    line = dict(color = '#506784'),
    fill = dict(color = [[rowOddColor,rowEvenColor,rowOddColor,
                               rowEvenColor,rowOddColor]]),
    align = ['left', 'center'],
    font = dict(color = '#506784', size = 11)
    ))

data = [trace0]

py.iplot(data, filename = "alternating row colors")