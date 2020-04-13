from math import trunc
def days(data):
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact,
    }
    return result

def weeks(data):
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact,
    }
    return result


def months(data):
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact,
    }
    return result