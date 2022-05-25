import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import time

def epoch_to_date(epoch_date):
    my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_date)))
    return(my_time)
def date_to_epoch(h_date):
    time_format = '%d/%m/%Y %I:%M:%S %p'
    epoch_date = int(time.mktime(time.strptime(h_date,time_format)))
    return epoch_date
def spacing():
    print('*\n*\n*')

print('Welcome to get_graphs from Aranet data program!\n')
time.sleep(1)

#Variables
x_val = []
y_val = []
aranet_id_ls = []
epoch_ls = []
pollut_ls = [('Carbon dioxide(ppm)', 'ppm'), ('Relative humidity(%)', '%'), ('Atmospheric pressure(hPa)','hPa')]
usr_input = None
event_name = input("Please input the event or experiment name attached to the csv files you want to plot: \n")
while True:
    usr_input = input("Please input Aranet ID, input 'no' when done: ")
    if(usr_input == 'no'):
        break
    aranet_id_ls.append(usr_input)
spacing()
print("The following IDs' data will be plotted and saved: ", aranet_id_ls, '\n')

for id in aranet_id_ls:
    print("-Processing Data from Aranet ", id)
    try:
        df = pd.read_csv('/home/tony/aranet_python/aranet_csv/'+ id + '_' + event_name + '.csv')
    except:
        print('====== Error: CSV file was not found for Aranet ', id, ' ======')
        continue
    for date in df['Time(dd/mm/yyyy)']:
        epoch_ls.append(date_to_epoch(date))
    for epoch in epoch_ls:
            x_val.append(epoch_to_date(epoch))
    datenum = md.date2num(x_val)
    for pollut in pollut_ls:
        for pollutval in df[pollut[0]]:
            y_val.append(float(pollutval))
        plt.figure(figsize=(20,10)) #width, height
        plt.title('Aranet' + id + ': ' + pollut[0] + ' vs Time')
        plt.xlabel("fecha y hora")
        plt.ylabel(pollut[1])
        plt.xticks(rotation=25)
        plt.grid()
        ax = plt.gca()
        xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
        ax.xaxis.set_major_formatter(xfmt)
        plt.plot(datenum, y_val)
        try:
            plt.savefig('/home/tony/aranet_python/aranet_figures/'+ event_name + '_' + pollut[0] +'_Aranet_' + id + '.png', bbox_inches = 'tight')
        except:
            print('====== Error: Unable to save figure for Aranet ', id, ', Check path ======')
            print()
        time.sleep(1)
        plt.close()
        y_val.clear()
    x_val.clear()
    epoch_ls.clear()
print("\nThe figures where saved succesfully!!!")
print("Quitting...")
exit()
