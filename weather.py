import matplotlib.pyplot as plt

time_of_day = ['06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
               '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '00:00', '01:00', '02:00', '03:00',
               '04:00', '05:00']

temperature = [6, 6, 5, 5, 5, 6, 6, 6, 6, 6, 5, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# print(len(temperature))
# print(len(time_of_day))
# plt.plot(temperature)
# plt.xlabel('Time Of Day')
# plt.ylabel('Temperature (C)')
# plt.xticks(time_of_day)
# plt.show()




# fig = plt.figure()
# ax = fig.add_subplot(111)
# y = temperature
# xt = time_of_day
# ax.plot(y)
# ax.set_xticklabels(xt)
# plt.show()

# import datetime
# import random
# import matplotlib.pyplot as plt
#
# print(datetime.datetime.now().date())
#
# # make up some data
# x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
# y = [i+random.gauss(0,1) for i,_ in enumerate(x)]
#
# # plot
# plt.plot(x,y)
# # beautify the x-labels
# plt.gcf().autofmt_xdate()
#
# plt.show()






import matplotlib.pyplot as plt

def create_bar_chart(data, labels):

    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each
    #  Bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

if __name__ == '__main__':
    # Number of steps I walked during the past week
    steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
    # Corresponding days
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    create_bar_chart(steps, labels)
