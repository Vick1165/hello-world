import requests

url = 'https://api.sumanjay.cf/covid/india'
r = requests.get(url).json()

# if r['success'] == 'true':
#     print('working fine')

delhi_confirm = r['data'] ['regional'][8]['confirmedCasesIndian']
delhi_recover = r['data'] ['regional'][8]['discharged']
delhi_death = r['data'] ['regional'][8]['deaths']


print(f"""In Delhi There are {delhi_confirm} number of 
covid cases  {delhi_recover} recoverd {delhi_death} deaths""")
