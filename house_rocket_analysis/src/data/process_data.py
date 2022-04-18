
def outliers_iqr(data, column, upper=1, lower=1, returns='limits'):
    """ Calculate the Upper and Lower Limit through the IQR method for find 'Outliers'
    Return the Upper and Lower Limit of the Sequence or Pandas Series
    : data: Sequence | Pandas Series
    : colunm: 'Columns Name'
    : upper: Percentage of the maximum limit to be considered outlier 
    : lower: Percentage of the minimun limit to be considered outlier 

    : returns: Value of the Upper Limit and Lower Limit, respectivily or the DataFrame without outliers"""
    
    import numpy as np


    # Find the 1st Quartitle and 3rd Quartitle with Numpy Percentitle method
    quartile_1, quartile_3 = np.percentile(data[column], [25, 75])

    # Calculate the Inter Quartitle (iqr)
    iqr = quartile_3 - quartile_1

    # Calculate the Lower and Upper limit
    lower_limit = (quartile_1 - (iqr * 1.5)) * lower
    upper_limit = (quartile_3 + (iqr * 1.5)) * upper

    # Create another DataFrame without outliers
    data_clean = data.loc[(data[column] <= upper_limit)
                          & (data[column] >= lower_limit)]

    # Print Lower and Upper Limit and the percentage of lines removed
    print('Lower Bound: {:,.2f} '.format(lower_limit))
    print('Upper Bound: {:,.2f}'.format(upper_limit))
    print('{} lines with outliers were identified, corresponding to {:.2f}% of the data set.'.format(
        (data.shape[0] - data_clean.shape[0]),
        ((data.shape[0] - data_clean.shape[0]) * 100) / data.shape[0]))

    # What returns
    if returns == 'limits':
        return upper_limit, lower_limit
    elif returns == 'dataframe':
        return data_clean
    else:
        return print("""Unexpected return value. 
Available values: 'limits','dataframe'.
Nothing has returned""")


def duplicated_rows(data):
    """
    Check if has duplicated rows in DataFrame
    """
    print('Duplicated rows')
    print()
    print('The dataset has {} rows duplicated'.format(data.duplicated().sum()))
    print('---------------------------------')

    return None


def missing_values(data):
    """
    Check if has missing values in dataset
    """
    print('Missing Values in each column')
    print()
    print(data.isnull().sum())
    print('---------------------------------')

    return None


def descriptive_statistics(data, column):
    descriptive_statistics_df = data[column].describe()

    print('Avarage Price: {:,.2f}'.format(descriptive_statistics_df.iloc[1]))
    print('Median Price: {:,.2f}'.format(descriptive_statistics_df.iloc[5]))
    print('Minimun Price: {:,.2f}'.format(descriptive_statistics_df.iloc[3]))
    print('Maximun Price: {:,.2f}'.format(descriptive_statistics_df.iloc[7]))
    print('The std Price: {:,.2f}'.format(descriptive_statistics_df.iloc[2]))

    return None


def create_season_column(data):
    """Create a new colunm named "Season", which contain the season based in the "Date" colunm"""
    import pandas as pd
    import numpy as np

    data['Month'] = pd.to_datetime(data['Date']).dt.strftime('%m')
    data['Month'] = data['Month'].astype(np.int64)


    data['Season'] = 'Winter'
    data.loc[(data['Month'] >= 3) & (data['Month'] < 6), 'Season'] = 'Spring'
    data.loc[(data['Month'] >= 6) & (data['Month'] < 9), 'Season'] = 'Summer'
    data.loc[(data['Month'] >= 9) & (data['Month'] < 12), 'Season'] = 'Fall'

    return None
