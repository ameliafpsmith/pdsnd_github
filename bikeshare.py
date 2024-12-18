import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Function Definitions
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Which city would you like to explore - Chicago, New York City, or Washington? ").lower().strip()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please enter 'Chicago', 'New York City', or 'Washington'.")
    
    while True:
        month = input("Which month - January, February, March, April, May, June, or 'all' to apply no filter? ").lower().strip()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid month. Please enter one of the following: January, February, March, April, May, June, or 'all'.")
    
    while True:
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or 'all' to apply no filter? ").lower().strip()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid day. Please enter one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or 'all'.")
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].mode()[0].title()
    print(f"Most Common Month: {most_common_month}")
    most_common_day = df['day_of_week'].mode()[0].title()
    print(f"Most Common Day: {most_common_day}")
    most_common_hour = df['hour'].mode()[0]
    print(f"Most Common Hour: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
