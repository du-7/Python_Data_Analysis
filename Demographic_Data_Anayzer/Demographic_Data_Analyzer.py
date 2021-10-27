import pandas as pd
import numpy as np

def calculate_demografic_data(print_data = True):
    #read data from csv file
    path = 'C:\\Users\\RicardoC\\Desktop\\Python\\Data_Analysis\\adult_data.csv'
    df = pd.read_csv(path)
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    race_count  = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male']['age'].mean().round(decimals = 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df.loc[df['education'] == 'Bachelors']['education'].count()
    total_count = df['education'].count()
    percentage_bachelors = (100*bachelors_count/total_count).round(decimals = 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    higher_education = df.loc[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df.loc[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = (100* higher_education.loc[higher_education['salary'] == '>50K']['salary'].count() / higher_education['salary'].count()).round(decimals=1)
    lower_education_rich = (100 * lower_education.loc[lower_education['salary'] == '>50K']['salary'].count() / lower_education['salary'].count()).round(decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    rich_percentage = (100 * num_min_workers.loc[num_min_workers['salary'] == '>50K']['salary'].count() / num_min_workers['salary'].count()).round(decimals=1)

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    country_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    highest_earning_country = (100* country_rich_count / country_count).idxmax()
    highest_earning_country_percentage = (100* country_rich_count / country_count).max().round(decimals=1)

    # Identify the most popular occupation for those who earn >50K in India.
    people_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    ocuupation_percentage = people_india['occupation'].value_counts()

    top_IN_occupation = ocuupation_percentage.idxmax()


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        'highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demografic_data()
