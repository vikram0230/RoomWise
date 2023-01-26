import pandas as pd
from datetime import timedelta
import math
import numpy as np

class Preprocessor:
    def load_model(filename):
        pickle_in = open(filename,"rb")
        model = pickle.load(pickle_in)
        return model

    def preprocess(self,X,y=None):
        print('Extracting data...')
        X_ = X.copy()
        X_.rename(columns={'arrival_date_year':'arrival_year', 'arrival_date_month':'arrival_month', 'arrival_date_day_of_month':'arrival_day_of_month', 'arrival_date_week_number':'arrival_week_number'}, inplace=True)
        X_['arrival_month'] = X_.apply(lambda x: self.__get_month_index(x['arrival_month']), axis=1)
        
        X_ = self.__null_handler(X_)

        X_['children'] = X_['children'].apply(int)
        X_['agent'] = X_['agent'].apply(int)
        X_['company'] = X_['company'].apply(int)
        
        X_['arrival_date'] = X_.apply(lambda x: self.__get_date(x['arrival_year'], x['arrival_month'], x['arrival_day_of_month']), axis=1)
        X_['arrival_date'] = pd.to_datetime(X_['arrival_date'], format='%Y-%m-%d')
        X_['arrival_day_of_week'] = X_['arrival_date'].dt.day_of_week

        X_['booking_date'] = X_.apply(lambda x: x['arrival_date'] - timedelta(days=x['lead_time']), axis=1)
        X_['booking_year'] = X_['booking_date'].dt.year
        X_['booking_month'] = X_['booking_date'].dt.month
        X_['booking_day_of_month'] = X_['booking_date'].dt.day
        X_['booking_day_of_week'] = X_['booking_date'].dt.day_of_week
        X_['booking_week_number'] = X_['booking_date'].dt.isocalendar().week

        X_['arrival_day_of_week'] = X_['arrival_date'].dt.dayofweek

        X_['is_family'] = X_.apply(lambda x: self.__family(x['children'] + x['babies']), axis=1)

        timeseries_labels = ['arrival_month','arrival_week_number','arrival_day_of_month','arrival_day_of_week',
                'booking_month', 'booking_week_number', 'booking_day_of_month', 'booking_day_of_week']

        if add_time_series:
            for label in timeseries_labels:
                X_[label + "_norm"] = 2 * math.pi * X_[label] / X_[label].max()
                X_["cos_" + label] = np.cos(X_[label + "_norm"])
                X_["sin_" + label] = np.sin(X_[label + "_norm"])

                X_.drop(labels=[label + '_norm', label], axis=1, inplace=True)

        X_.drop(labels=['arrival_date','arrival_year','booking_date'],axis=1,inplace=True)

        return X_

    def __null_handler(self,X):
        X.agent.fillna(0, inplace=True)
        X.company.fillna(0, inplace=True)
        X.children.fillna(0, inplace=True)
        X.country.fillna('PRT', inplace=True)
        X.loc[X[X['market_segment'] == 'Undefined'].index, 'market_segment'] = 'Online TA'
        X.loc[X[X['distribution_channel'] == 'Undefined'].index, 'distribution_channel'] = 'TA/TO'
        return X

    def __get_month_index(self,month):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return months.index(month)+1

    def __get_date(self,year,month,day):
        return str(year) + '-' + str(month) + '-' + str(day)

    def __family(self,value):
        if value > 0:
            return 1
        else:
            return 0