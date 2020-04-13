from math import trunc
from flask import g,Flask

def days(data):
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] / 3))
    impact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    severeImpact['severeCasesByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.15)
    availablebeds = trunc(data['totalHospitalBeds'] * 0.35)
    impact['hospitalBedsByRequestedTime'] = availablebeds - impact['severeCasesByRequestedTime']+1
    severeImpact['hospitalBedsByRequestedTime'] = availablebeds - severeImpact['severeCasesByRequestedTime']+1
    impact['casesForICUByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.05)
    severeImpact['casesForICUByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.05)
    impact['casesForVentilatorsByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.02)
    severeImpact['casesForVentilatorsByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.02)
    impact['dollarsInFlight'] = trunc(impact['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']/data['timeToElapse'])
    severeImpact['dollarsInFlight'] = trunc(severeImpact['infectionsByRequestedTime']*data['region']['avgDailyIncomeInUSD'] *data['region']['avgDailyIncomePopulation']/data['timeToElapse'])
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact
    }
    return result

def weeks(data):
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse'] *7 / 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse']*7/ 3))
    impact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    severeImpact['severeCasesByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.15)
    availablebeds = trunc(data['totalHospitalBeds'] * 0.35)
    impact['hospitalBedsByRequestedTime'] = availablebeds - impact['severeCasesByRequestedTime']+1
    severeImpact['hospitalBedsByRequestedTime'] = availablebeds - severeImpact['severeCasesByRequestedTime']+1    
    impact['casesForICUByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.05)
    severeImpact['casesForICUByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.05)
    impact['casesForVentilatorsByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.02)
    severeImpact['casesForVentilatorsByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.02)
    impact['dollarsInFlight'] = trunc(impact['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']/data['timeToElapse'])
    severeImpact['dollarsInFlight'] = trunc(severeImpact['infectionsByRequestedTime']*data['region']['avgDailyIncomeInUSD'] *data['region']['avgDailyIncomePopulation']/data['timeToElapse'])
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact
    }
    return result

def months(data):
    impact = {}
    severeImpact = {}
    impact['currentlyInfected'] = data['reportedCases'] * 10
    severeImpact['currentlyInfected'] = data['reportedCases'] * 50
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * pow(2, trunc(data['timeToElapse']*30/ 3))
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected'] * pow(2, trunc(data['timeToElapse']*30/ 3))
    impact['severeCasesByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.15)
    severeImpact['severeCasesByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.15) 
    availablebeds = trunc(data['totalHospitalBeds'] * 0.35)
    impact['hospitalBedsByRequestedTime'] = availablebeds - impact['severeCasesByRequestedTime']+1
    severeImpact['hospitalBedsByRequestedTime'] = availablebeds - severeImpact['severeCasesByRequestedTime'] + 1
    impact['casesForICUByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.05)
    severeImpact['casesForICUByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.05)
    impact['casesForVentilatorsByRequestedTime'] = trunc(impact['infectionsByRequestedTime'] * 0.02)
    severeImpact['casesForVentilatorsByRequestedTime'] = trunc(severeImpact['infectionsByRequestedTime'] * 0.02)
    impact['dollarsInFlight'] = trunc(impact['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']/data['timeToElapse'])
    severeImpact['dollarsInFlight'] = trunc(severeImpact['infectionsByRequestedTime']*data['region']['avgDailyIncomeInUSD'] *data['region']['avgDailyIncomePopulation']/data['timeToElapse'])
    result = {
        'data': data,
        'impact': impact,
        'severeImpact':severeImpact
    }
    return result