''' This module provides statistical information for a company information and data '''
from typing import Tuple
import math
import statistics

def company_profile():
    '''
    This function is used for defining company information
    '''
    company_name: str = "Pradhan Analytics Inc."
    count_active_projects: int = 1
    has_international_presence: bool = True
    services_offered_string: str = "IT Consultancy, Data Analysis, Machine Learning Consulting, Business Intelligence Solutions"
    satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0]

    return company_name, count_active_projects, has_international_presence, services_offered_string, satisfaction_scores

def company_statistics():
    '''
    This function is used for computing statistics on company information
    '''
    company_spec: Tuple =  company_profile()
    smallest= min(company_spec[4])
    largest= max(company_spec[4])
    total= sum(company_spec[4])
    count= len(company_spec[4])
    mean= statistics.mean(company_spec[4])
    mode= statistics.mode(company_spec[4])
    median= statistics.median(company_spec[4])
    standard_deviation=statistics.stdev(company_spec[4])
    return smallest, largest, total, count, mean, mode, median, standard_deviation

def main():
     '''
     This function is used to display all the company information and statistics
     '''
     company_spec: Tuple =  company_profile()
     company_stats: Tuple = company_statistics()
     active_projects_string: str = f"Active Projects: {company_spec[1]}"
     international_presence_string: str = f"International Presence: {company_spec[2]}"
     stats_string: str = f""" Descriptive Statistics for Our Satisfaction Scores:
     Smallest: {company_stats[0]}
     Largest: {company_stats[1]}
     Total: {company_stats[2]}
     Count: {company_stats[3]}
     Mean: {company_stats[4]}
     Mode: {company_stats[5]}
     Median: {company_stats[6]}
     Standard Deviation: {company_stats[7]}
     """
     byline: str = f"""
     {company_spec[0]}
     {active_projects_string}
     {international_presence_string}
     {stats_string}
     """
     print(byline)
if __name__ == '__main__':
    main()

