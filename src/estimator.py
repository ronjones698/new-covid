from periodtype import days,weeks,months

def estimator(data):
  ptype = data['periodType']
  if (ptype == 'days'):
    results = days(data)
  elif (ptype == 'weeks'):
    results = weeks(data)
  else:
    results = months(data) 
  return results
