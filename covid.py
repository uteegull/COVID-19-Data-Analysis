from tkinter import *

import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


#graph customisation
def reformat_large_tick_values(tick_val, pos):
    """
    Turns large tick values (in the billions, millions and thousands) such as 4500 into 4.5K and also appropriately turns 4000 into 4K (no zero after the decimal).
    """
    if tick_val >= 1000000000:
        val = round(tick_val / 1000000000, 1)
        new_tick_format = '{:}B'.format(val)
    elif tick_val >= 1000000:
        val = round(tick_val / 1000000, 1)
        new_tick_format = '{:}M'.format(val)
    elif tick_val >= 1000:
        val = round(tick_val / 1000, 1)
        new_tick_format = '{:}K'.format(val)
    elif tick_val < 1000:
        new_tick_format = round(tick_val, 1)
    else:
        new_tick_format = tick_val

    # make new_tick_format into a string value
    new_tick_format = str(new_tick_format)

    # code below will keep 4.5M as is but change values such as 4.0M to 4M since that zero after the decimal isn't needed
    index_of_decimal = new_tick_format.find(".")

    if index_of_decimal != -1:
        value_after_decimal = new_tick_format[index_of_decimal + 1]
        if value_after_decimal == "0":
            # remove the 0 after the decimal point since it's not needed
            new_tick_format = new_tick_format[0:index_of_decimal] + new_tick_format[index_of_decimal + 2:]

    return new_tick_format

# data analysis for world
def world_analysis():
    corona_data = pd.read_csv("corona-data.csv", engine='python')
    x = sum(corona_data['Confirmed'])
    y = sum(corona_data['Deaths'])
    z = sum(corona_data['Recovered'])
    figure1 = Figure(figsize=(4, 3), dpi=100)
    subplot1 = figure1.add_subplot(111)
    labels1 = 'Confirmed', 'Deaths', 'Recovered'
    piesizes = [x, y, z]
    plt.pie(piesizes, labels=labels1, autopct='%.1f%%')
    plt.title('World wide cases analysis for COVID-19')
    print(plt.show())
    pie1 = FigureCanvasTkAgg(figure1, win)
    pie1.get_tk_widget().pack()


# data analysis state wise
def data_analysis():
    corona_data = pd.read_csv("corona-data.csv", engine='python')
    #print(corona_data.shape)
    # country analysis
    corona_data_country = pd.DataFrame(corona_data.groupby(by='Country/Region').sum())
    if 'SNo' in corona_data_country:
        corona_data_country = corona_data_country.drop('SNo', axis=1)
    corona_data_country['country'] = corona_data_country.index
    #print('Total no. of confirmed cases over these days', sum(corona_data['Confirmed']))
    #print('Total no. of deaths over these days', sum(corona_data['Deaths']))
    #print('Total no. of recovered cases over these days', sum(corona_data['Recovered']))
    sorted_country_data = corona_data_country.sort_values(['Confirmed', 'Deaths', 'Recovered'],
                                                          ascending=[False, False, False])
    #print(sorted_country_data)
    state_name_get=state_name.get()
    US_data = sorted_country_data[sorted_country_data['country'] == state_name_get]
    #print(US_data)

    US_data_list = [US_data.columns.values.tolist()] + US_data.values.tolist()
    #print(US_data)
    # loop through data to display in tkinter
    print_rec = ''
    for record in US_data_list:
        print_rec += str(record) + "\n"
    query_label = Label(text=print_rec)
    query_label.grid(row=2, column=1, columnspan=2)
    # create charts
    x = US_data['Confirmed']
    y = US_data['Deaths']
    z = US_data['Recovered']
    piesizes = [float(x), float(y),float(z)]
    figure2 = Figure(figsize=(4, 3), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'Confirmed', 'Deaths', 'Recovered'
    plt.pie(piesizes,labels=labels2, startangle=90, autopct='%.1f%%')
    plt.title('Country wise analysis of COVID-19 Cases')
    print(plt.show())
    pie2 = FigureCanvasTkAgg(figure2, win)
    pie2.get_tk_widget().pack()

def top_10():
    corona_data = pd.read_csv("corona-data.csv", engine='python')
    corona_data_country = pd.DataFrame(corona_data.groupby(by='Country/Region').sum())
    if 'SNo' in corona_data_country:
        corona_data_country = corona_data_country.drop('SNo', axis=1)
    corona_data_country['country'] = corona_data_country.index
    df_top_confirmed = corona_data_country.sort_values(by=['Confirmed'], ascending=[False]).head(10)
    figure3 = plt.Figure(figsize=(4, 3), dpi=100)
    ax1 = figure3.add_subplot(111)

    df1 = df_top_confirmed[['Confirmed', 'Deaths', 'Recovered', 'country']].groupby('country').sum()
    df1.plot(kind='bar', legend=True)
    plt.xlabel('Countries')
    plt.ylabel('Population in Millions')
    plt.title('Top 10 countries affected by COVID-19')
    print(plt.show())
    bar1 = FigureCanvasTkAgg(figure3, win)
    bar1.get_tk_widget().pack()

def last_10():
    corona_data = pd.read_csv("corona-data.csv", engine='python')
    corona_data_country = pd.DataFrame(corona_data.groupby(by='Country/Region').sum())
    if 'SNo' in corona_data_country:
        corona_data_country = corona_data_country.drop('SNo', axis=1)
    corona_data_country['country'] = corona_data_country.index
    df_top_confirmed = corona_data_country.sort_values(by=['Confirmed'], ascending=[False]).tail(10)
    figure3 = plt.Figure(figsize=(4, 3), dpi=100)
    ax1 = figure3.add_subplot(111)

    df1 = df_top_confirmed[['Confirmed', 'Deaths', 'Recovered', 'country']].groupby('country').sum()
    ax = df1.plot(kind='barh', legend=True)
    ax = plt.gca()
    plt.xlabel('Countries')
    plt.ylabel('Rate ')
    plt.title('Countries Least affected by COVID-19')
    ax.xaxis.set_major_formatter(tick.FuncFormatter(reformat_large_tick_values));
    print(plt.show())
    bar1 = FigureCanvasTkAgg(figure3, win)
    bar1.get_tk_widget().pack()

def state_analysis():
    corona_data = pd.read_csv("corona-data.csv", engine='python')
    t1 = corona_data[['Province/State', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
    print(t1)
    state_name_get = state_name.get()
    t2 = t1[t1['Country/Region'] == state_name_get]
    print(t2)
    t3 = t2[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
    print(t3)
    t4 = pd.DataFrame(t3.groupby(by='Province/State').sum())
    print(t4)
    sorted_t4 = t4.sort_values(['Confirmed', 'Deaths', 'Recovered'], ascending=[False, False, False])
    print(sorted_t4)
    df_top_t4 = sorted_t4.sort_values(by=['Confirmed'], ascending=[False]).head(10)
    print(df_top_t4)
    y = df_top_t4['Confirmed'].tolist()
    x = list(df_top_t4.index.values)
    #print(y)
    y1 = [round(x) for x in y]
    #print(list)
    figure4 = plt.Figure(figsize=(4, 3), dpi=100)
    ax2 = figure4.add_subplot(111)

    ax = plt.barh(x, y1)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(tick.FuncFormatter(reformat_large_tick_values));
    print(plt.show())
    bar1 = FigureCanvasTkAgg(figure4, win)
    bar1.get_tk_widget().pack()


#start of tkinter
win= Tk()
win.title("Corona Data Analysis")
win.geometry("650x500")
#Text Labels
l1 = Label(win,text="Covid - 19 analysis")
l1.grid(row=2,column=10)
#Submit button for world wide analysis
submit_btn = Button(win,text="World wide Covid-19 cases",command=world_analysis)
submit_btn.grid(row=5,column=10)

#Text Box
state_name = StringVar()
state = Entry(win,textvariable=state_name,width=30)
state.grid(row=8,column=10)

#Text Box Labels
state_label = Label(win,text="Enter Country Name")
state_label.grid(row=8,column=9)

#submit for state wise analysis
submit_btn = Button(win,text="Covid-19 cases for this Country",command=data_analysis)
submit_btn.grid(row=10,column=10,padx=20)

#button for top 10 country analysis
submit_btn = Button(win,text="Most Affected Countries",command=top_10)
submit_btn.grid(row=13,column=10,padx=20)

#button for least affected country analysis
submit_btn = Button(win,text="Least Affected Countries",command=last_10)
submit_btn.grid(row=15,column=10,padx=20)

#button for state cases
submit_btn = Button(win,text="State wise analysis ",command=state_analysis)
submit_btn.grid(row=18,column=10,padx=20)



win.mainloop()


