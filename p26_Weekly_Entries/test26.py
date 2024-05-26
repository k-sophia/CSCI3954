"""
Test driver for Program 26
"""

import pandas as pd
import numpy as np
import seaborn as sns
import p26

# test tripTime
'''
Expected output:

                pickup              dropoff  ...  pickup_borough  dropoff_borough
0  2019-03-23 20:21:09  2019-03-23 20:27:24  ...       Manhattan        Manhattan
1  2019-03-04 16:11:55  2019-03-04 16:19:00  ...       Manhattan        Manhattan
2  2019-03-27 17:53:01  2019-03-27 18:00:25  ...       Manhattan        Manhattan
3  2019-03-10 01:23:59  2019-03-10 01:49:51  ...       Manhattan        Manhattan
4  2019-03-30 13:27:42  2019-03-30 13:37:14  ...       Manhattan        Manhattan
5  2019-03-11 10:37:23  2019-03-11 10:47:31  ...       Manhattan        Manhattan
6  2019-03-26 21:07:31  2019-03-26 21:17:29  ...       Manhattan        Manhattan
7  2019-03-22 12:47:13  2019-03-22 12:58:17  ...       Manhattan        Manhattan
8  2019-03-23 11:48:50  2019-03-23 12:06:14  ...       Manhattan        Manhattan
9  2019-03-08 16:18:37  2019-03-08 16:26:57  ...       Manhattan        Manhattan

[10 rows x 14 columns]
                pickup              dropoff  ...  dropoff_borough        tripTime
0  2019-03-23 20:21:09  2019-03-23 20:27:24  ...        Manhattan 0 days 00:06:15
1  2019-03-04 16:11:55  2019-03-04 16:19:00  ...        Manhattan 0 days 00:07:05
2  2019-03-27 17:53:01  2019-03-27 18:00:25  ...        Manhattan 0 days 00:07:24
3  2019-03-10 01:23:59  2019-03-10 01:49:51  ...        Manhattan 0 days 00:25:52
4  2019-03-30 13:27:42  2019-03-30 13:37:14  ...        Manhattan 0 days 00:09:32
5  2019-03-11 10:37:23  2019-03-11 10:47:31  ...        Manhattan 0 days 00:10:08
6  2019-03-26 21:07:31  2019-03-26 21:17:29  ...        Manhattan 0 days 00:09:58
7  2019-03-22 12:47:13  2019-03-22 12:58:17  ...        Manhattan 0 days 00:11:04
8  2019-03-23 11:48:50  2019-03-23 12:06:14  ...        Manhattan 0 days 00:17:24
9  2019-03-08 16:18:37  2019-03-08 16:26:57  ...        Manhattan 0 days 00:08:20

[10 rows x 15 columns]
'''
taxi = sns.load_dataset('taxis')
print(taxi.iloc[0:10])  #Print first 10 lines:
taxi['tripTime'] = taxi.apply(lambda x: p26.tripTime(x['pickup'], x['dropoff']), axis=1)
print(taxi.iloc[0:10])


# test weekdays
'''
Expected output

  pickup              dropoff  ...  pickup_borough  dropoff_borough
1   2019-03-04 16:11:55  2019-03-04 16:19:00  ...       Manhattan        Manhattan
2   2019-03-27 17:53:01  2019-03-27 18:00:25  ...       Manhattan        Manhattan
5   2019-03-11 10:37:23  2019-03-11 10:47:31  ...       Manhattan        Manhattan
6   2019-03-26 21:07:31  2019-03-26 21:17:29  ...       Manhattan        Manhattan
7   2019-03-22 12:47:13  2019-03-22 12:58:17  ...       Manhattan        Manhattan
9   2019-03-08 16:18:37  2019-03-08 16:26:57  ...       Manhattan        Manhattan
11  2019-03-20 19:39:42  2019-03-20 19:45:36  ...       Manhattan        Manhattan
12  2019-03-18 21:27:14  2019-03-18 21:34:16  ...       Manhattan        Manhattan
13  2019-03-19 07:55:25  2019-03-19 08:09:17  ...       Manhattan        Manhattan
14  2019-03-27 12:13:34  2019-03-27 12:25:48  ...       Manhattan        Manhattan

[10 rows x 14 columns]
'''
taxi = sns.load_dataset('taxis')
weekdays = p26.weekdays(taxi,'pickup')
print(weekdays.iloc[0:10])