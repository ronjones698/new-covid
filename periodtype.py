from math import trunc
def days(data):
    impact = {}
    severeImpact = {}
    availablebeds = trunc(data['totalHospitalBeds']*0.35)
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    impact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    severeImpact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    impact['hospitalBedsByRequestedTime'] = availablebeds - impact['severeCasesByRequestedTime']
    severeImpact['hospitalBedsByRequestedTime'] = availablebeds - severeImpact['severeCasesByRequestedTime']
    impact['casesForICUByRequestedTime'] = trunc(0.05 * impact['infectionsByRequestedTime'])
    severeImpact['casesForICUByRequestedTime'] = trunc(0.05 * severeImpact['infectionsByRequestedTime'])

    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact
    }
    return result

def weeks(data):
    impact = {}
    severeImpact = {}
    availablebeds = trunc(data['totalHospitalBeds']*0.35)
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] *7 / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse']*7 / 3))
    impact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    severeImpact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    impact['hospitalBedsByRequestedTime'] = availablebeds - impact['severeCasesByRequestedTime']
    severeImpact['hospitalBedsByRequestedTime'] = availablebeds - severeImpact['severeCasesByRequestedTime']
    impact['casesForICUByRequestedTime'] = trunc(0.05 * impact['infectionsByRequestedTime'])
    severeImpact['casesForICUByRequestedTime'] = trunc(0.05 * severeImpact['infectionsByRequestedTime'])
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact
    }
    return result

def months(data):
    impact = {}
    severeImpact = {}
    availablebeds = trunc(data['totalHospitalBeds']*0.35)
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse']*30 / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse']*30/ 3))
    impact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    severeImpact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    impact['hospitalBedsByRequestedTime'] = availablebeds - impact['severeCasesByRequestedTime']
    severeImpact['hospitalBedsByRequestedTime'] = availablebeds - severeImpact['severeCasesByRequestedTime']
    impact['casesForICUByRequestedTime'] = trunc(0.05 * impact['infectionsByRequestedTime'])
    severeImpact['casesForICUByRequestedTime'] = trunc(0.05 * severeImpact['infectionsByRequestedTime'])
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact
    }
    return result