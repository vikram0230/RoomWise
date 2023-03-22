import math
import numpy as np
import pandas as pd
from datetime import timedelta
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureExtractor(TransformerMixin):
    def  __init__(self):
        print('Feature Extractor initiated...')

    def fit(self,X,y=None):
        print('Fitting data...')
        return self        

    def transform(self, X, y=None, add_time_series=True):
        print('Extracting data...')
        X_ = X.copy()

        X_['arrival_date'] = pd.to_datetime(X_['arrival_date'], format='%Y-%m-%d')
        X_['arrival_year'] = X_['arrival_date'].dt.year
        X_['arrival_month'] = X_['arrival_date'].dt.month
        X_['arrival_day_of_month'] = X_['arrival_date'].dt.day
        X_['arrival_day_of_week'] = X_['arrival_date'].dt.day_of_week + 1
        X_['arrival_week_number'] = X_['arrival_date'].dt.isocalendar().week

        X_['booking_date'] = pd.to_datetime(X_['booking_date'], format='%Y-%m-%d')
        X_['booking_year'] = X_['booking_date'].dt.year
        X_['booking_month'] = X_['booking_date'].dt.month
        X_['booking_day_of_month'] = X_['booking_date'].dt.day
        X_['booking_day_of_week'] = X_['booking_date'].dt.day_of_week + 1
        X_['booking_week_number'] = X_['booking_date'].dt.isocalendar().week

        X_['departure_date'] = pd.to_datetime(X_['departure_date'], format='%Y-%m-%d')

        X_[['stays_in_week_nights','stays_in_weekend_nights']] = X_.apply(lambda x: self.__find_week_day(x['arrival_day_of_week'],x['arrival_date'],x['departure_date']), axis=1, result_type='expand')
        X_['distribution_channel'] = X_.apply(lambda x: self.__set_distribution_channel(x['market_segment']), axis=1)
        X_['is_repeated_guest'] = 0
        X_['previous_cancellations'] = 0
        X_['previous_bookings_not_canceled'] = 0
        X_['booking_changes'] = 0
        X_['deposit_type'] = 'No Deposit'
        X_['agent'] = 0
        X_['company'] = 0
        X_['days_in_waiting_list'] = 0
        X_['customer_type'] = 'Transient'
        X_['children'] = X_['children'].apply(int)

        X_['is_family'] = X_.apply(lambda x: self.__family(x['children'] + x['babies']), axis=1)

        timeseries_labels = ['arrival_month','arrival_week_number','arrival_day_of_month','arrival_day_of_week',
                'booking_month', 'booking_week_number', 'booking_day_of_month', 'booking_day_of_week']

        if add_time_series:
            for label in timeseries_labels:
                X_[label + "_norm"] = 2 * math.pi * X_[label] / X_[label].max()
                X_["cos_" + label] = np.cos(X_[label + "_norm"])
                X_["sin_" + label] = np.sin(X_[label + "_norm"])

                X_.drop(labels=[label + '_norm', label], axis=1, inplace=True)

        X_.drop(labels=['arrival_date','arrival_year','booking_date','booking_year','departure_date'],axis=1,inplace=True)

        print('Extraction Done')
        self.__view_data_specs(X_)
        return X_

    # def __null_handler(self,X):
    #     X.agent.fillna(0, inplace=True)
    #     X.company.fillna(0, inplace=True)
    #     X.children.fillna(0, inplace=True)
    #     X.country.fillna('PRT', inplace=True)
    #     X.loc[X[X['market_segment'] == 'Undefined'].index, 'market_segment'] = 'Online TA'
    #     X.loc[X[X['distribution_channel'] == 'Undefined'].index, 'distribution_channel'] = 'TA/TO'
    #     return X

    def __set_distribution_channel(self,market_segment):
        if market_segment in ['Online TA','Offline TA/TO','Groups']:
            distribution_channel = 'TA/TO'
        elif market_segment in ['Corporate','Complementary','Aviation']:
            distribution_channel = 'Corporate'
        else:
            distribution_channel = 'Direct'
        return distribution_channel

    def __find_week_day(self,arrival_day_of_week,arrival_date,departure_date):
        stay_duration = (departure_date - arrival_date).days
        days = [] # Weekday: True; Weekend: False
        for i in range(stay_duration-1):
            day = arrival_day_of_week
            days.append(day < 5)
            day = day + 1
            if day > 6:
                day = 0
            
        week_nights = days.count(True)
        weekend_nights = days.count(False)
        return [week_nights, weekend_nights]

    def __family(self,value):
        if value > 0:
            return 1
        else:
            return 0

    def __view_data_specs(self,data):
        print(data.columns)
        print(data.shape)
        print(data.info())

# feature_extractor = FeatureExtractor()
# transformed_data = feature_extractor.fit_transform(train_data_filtered)
# transformed_data.info()