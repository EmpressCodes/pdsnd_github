import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    user_input=input("Enter the city you'd like to view:")
    user_input.lower() #ensures case insensitivity
    while (user_input not in ('chicago','new york city','washington')):
        print("Invalid input or incorrect spelling. Please check if your input is either \'chicago', \'new york city' or \'washington' ")
        print("-------Restarting the program-------- \n\n")
        main()
    city=user_input;

    # get user input for month (all, january, february, ... , june)
    user_input=input("Enter the specific month you'd like to filter by or type '\ALL' to view all months:")
    user_input.lower() #ensures case insensitivity
    while (user_input not in ('all','january','february', 'march', 'april', 'may','june')):
        print("Invalid input and incorrect spelling. Please check your input.")
        print("-------Restarting the program-------- \n\n")
        main()
    month=user_input;


    # get user input for day of week (all, monday, tuesday, ... sunday)
    user_input=input("Enter the specific day you'd like to filter by or type '\ALL' to view all days:")
    user_input.lower() #ensures case insensitivity
    while (user_input not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday')):
        print("Invalid input or incorrect spelling. Please check if your input.")
        print("-------Restarting the program-------- \n\n")
        main()
    week_day=user_input;
    print('-'*40)
    return city,month,week_day

def load_data(city,month,week_day):
    """
    Loads data for the specified city,month and week_day
    """
    file_load=CITY_DATA[city]
    df=pd.read_csv(file_load)
    df=df.dropna(axis = 0)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if week_day != 'all':
         df = df[df['day_of_week'] == week_day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month here
    df['month'] = df['Start Time'].dt.month_name()
    common_month = df['month'].mode()[0]
    print("\n The most common_month is:",common_month )


    # display the most common day of week

    df['day'] = df['Start Time'].dt.day_name()
    common_day = df['day'].mode()[0]
    print("\n The most common_day is:",common_day )


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\n The most popular_hour is:",popular_hour )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\n The most common start station is:",df['Start Station'].mode()[0])


    # display most commonly used end station
    print("\nThe most common end station is:",df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip

    print("\n The most frequent combination of start station and end station trip is\n:", df.groupby(['Start Station','End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n \n Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: ",df["Trip Duration"].sum())



    # display mean travel time
    print("\n The total average time is: ",df["Trip Duration"].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\n\ncounts of user types\n",user_types)



    # Display counts of gender
    if city=='washington':
        print("\n\nGender count not available for Washington city\n\n")
    else:
        gender = df['Gender'].value_counts()
        print("\n Counts of gender:",gender)

    print('-'*40)

    # Display earliest, most recent, and most common year of birth
    if city=='washington':
        print("\n\nYear of birth stats not available for Washington city")
    else:
        print("\n\nEarliest year of birth is:", df['Birth Year'].min())

        print("\n\nMost recent year of birth is:", df['Birth Year'].max())

        print("\n\nThe most common year of birth is:", df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ Displays raw data upon user request"""

    print("\n would you like to see the first 5 lines of raw data from the collected samples?\n")
    answer=input("Type Y/Yes or N/No:")
    answer.lower()
    if (answer=='no' or answer=='n'):
        return
    elif (answer=='yes' or answer=='y'):
        print(df.head())
        counter=5
        while True:
            print("\n\n would you like to see more lines of raw data?\n")
            answer_2=input("Type Y/Yes or N/No:")
            answer_2.lower()
            if (answer_2=='yes' or answer_2=='y'):
                print(df.iloc[counter:counter+5])
                counter=counter+5


            else:
                return







def main():
    while True:
        city,month,week_day= get_city()
        df = load_data(city,month,week_day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
