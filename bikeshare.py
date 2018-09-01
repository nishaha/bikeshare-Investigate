import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        city = input('Would you like to see data for chicago, new york city or washington?').lower()
        if city in ('chicago', 'new york city', 'washington'):
            print(city)
            break
        else:
            print('Please enter a correct value')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter tha data for january, february, march, april, may, june?').lower()
        if month in months:
            print(month)
            break
        else:
            print('Please enter a correct value')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose one day:monday,tuesday, wednesday, thursday, friday, saturday, sunday, all?').lower()
        if day in weekdays:
            print(day)
            break
        else:
            print('Please enter a correct value')
    
    
    print('-'*40)
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
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df =df[df['day_of_week'] == day.title()] 
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # df['Start Time'] =pd.to_datetime(df['Start Time'])
    # df['month'] =df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start month:', popular_month)

    # TO DO: display the most common day of week
   
    # df['week'] =df['Start Time'].dt.week
    popular_week = df['day_of_week'].mode()[0]
    print('Most Frequent Start week:', popular_week)

    # TO DO: display the most common start hour
   
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('most commonly used_start_station:',start_station)

    # TO DO: display most commonly used end station
    end_station =df['End Station'].mode()[0]
    print('most commonly used end station:',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_trip'] = df['Start Station'] + df['End Station']
    most_station_trip =df['frequent_trip'].mode()[0]
    print('most station trip:',most_station_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time =df['Trip Duration'].mean()
    print('mean travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('max of user types:',user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('counts of gender:',gender)
    except:
        print('There is no such column')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        # gender = df['Gender'].value_counts()                    
        # print('counts of gender:', gender)  
        a_birth_year = df['Birth Year'].sort_values(inplace=False,ascending=True)
        b_birth_year = df['Birth Year'].sort_values(inplace=False,ascending=False)
        most_common_birthyear=df['Birth Year'].mode()[0]
    except:
        print('There is no such column')
    else:
        print('earliest year of birth:',a_birth_year.iloc[0])
        print('most recent of birth:',b_birth_year.iloc[0])
        print('most_common_birthyear:',most_common_birthyear)
     

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
