import yfinance as yf
import datetime as datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk #To integrated plots to tkinter
from matplotlib.widgets import RadioButtons
import numpy as np
from tkinter import *
#import os
#import pandas as pd
#from openpyxl.workbook import Workbook



ticks = ["TTRAK.IS", "ERSU.IS", "DOAS.IS", "AKSA.IS", "CEMTS.IS", "EREGL.IS", "PETKM.IS", "AEFES.IS", "ASELS.IS", "INDES.IS"]

start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

window = Tk()
window.title("Stocks")
window.geometry("800x600")


fig, ax = plt.subplots(figsize=(12,8))


# All stocks in a different variable
TTRAK_data = yf.download("TTRAK.IS", start=start_date, end=end_date)['Adj Close']
ERSU_data = yf.download("ERSU.IS", start=start_date, end=end_date)['Adj Close']
DOAS_data = yf.download("DOAS.IS", start=start_date, end=end_date)['Adj Close']
AKSA_data = yf.download("AKSA.IS", start=start_date, end=end_date)['Adj Close']
CEMTS_data = yf.download("CEMTS.IS", start=start_date, end=end_date)['Adj Close']
EREGL_data = yf.download("EREGL.IS", start=start_date, end=end_date)['Adj Close']
PETKM_data = yf.download("PETKM.IS", start=start_date, end=end_date)['Adj Close']
AEFES_data = yf.download("AEFES.IS", start=start_date, end=end_date)['Adj Close']
ASELS_data = yf.download("ASELS.IS", start=start_date, end=end_date)['Adj Close']
INDES_data = yf.download("INDES.IS", start=start_date, end=end_date)['Adj Close']


#All stocks in one plot
def graph_all():
    ax.clear() # Clear the graph every time the function called 
    plt.plot(TTRAK_data.index, TTRAK_data, label="TTRAK.IS", drawstyle='steps',color='b')
    plt.plot(ERSU_data.index, ERSU_data, label="ERSU.IS", drawstyle='steps',color='orange')
    plt.plot(DOAS_data.index, DOAS_data, label="DOAS.IS", drawstyle='steps',color='g')
    plt.plot(AKSA_data.index, AKSA_data, label="AKSA.IS", drawstyle='steps',color='r')
    plt.plot(CEMTS_data.index, CEMTS_data, label="CEMTS.IS", drawstyle='steps',color='k')
    plt.plot(EREGL_data.index, EREGL_data, label="EREGL.IS", drawstyle='steps',color='purple')
    plt.plot(PETKM_data.index, PETKM_data, label="PETKM.IS", drawstyle='steps',color='pink')
    plt.plot(AEFES_data.index, AEFES_data, label="AEFES.IS", drawstyle='steps',color='brown')
    plt.plot(ASELS_data.index, ASELS_data, label="ASELS.IS", drawstyle='steps',color='gray')
    plt.plot(INDES_data.index, INDES_data, label="INDES.IS", drawstyle='steps',color='y')
    plt.legend(loc='upper left')
    canvas.draw() 


def choose_stock(stock):
    ax.clear()
    data = yf.download(stock,start=start_date,end=end_date)['Adj Close']
    plt.plot(data.index, data, label=stock, drawstyle='steps')
    canvas.draw()


def on_stock_selected(event):
    selected_stock_value = selected_stock.get()
    choose_stock(selected_stock_value)
    

def stock_median():
    selected_stock_value = selected_stock.get()  
    ax.clear()
    data = yf.download(selected_stock_value, start=start_date, end=end_date)['Adj Close']
    median = np.median(data)
    plt.plot(data.index, data, label=selected_stock_value, drawstyle='steps', color='b')
    ax.axhline(median, color='r', linestyle='--', label=f"Median: {median}")
    plt.legend(loc='upper left')
    canvas.draw()
    
    
def stock_mean():
    selected_stock_value = selected_stock.get()  
    ax.clear()
    data = yf.download(selected_stock_value, start=start_date, end=end_date)['Adj Close']
    mean = np.mean(data)
    plt.plot(data.index, data, label=selected_stock_value, drawstyle='steps', color='b')
    ax.axhline(mean, color='r', linestyle='--', label=f"Mean: {mean}")
    plt.legend(loc='upper left')
    canvas.draw()



def graph_week(week):
    start_date = datetime.date(2022, 1, 3) + datetime.timedelta(weeks= week - 1)
    end_date = start_date + datetime.timedelta(days=5)
    selected_stock_value = selected_stock.get()
    
    ax.clear()
    data = yf.download(selected_stock_value,start=start_date,end=end_date)['Adj Close']
    plt.plot(data.index, data, label=selected_stock_value, drawstyle='steps')
    plt.legend(loc='upper left')
    canvas.draw()
    
def get_week_data():
    week = int(week_entry.get()) 
    graph_week(week)

def comprasion():
    pass

frame = Frame(window)
label = Label(text="Stocks")
label.pack()


canvas = FigureCanvasTkAgg(fig,master=window)
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas,frame,pack_toolbar=False) # Call matplotlib default toolbar ery
toolbar.update()
toolbar.pack(anchor="w",fill=X)

#label
week_label = Label(frame, text="Week :")
week_label.pack()
week_entry = Entry(frame)
week_entry.pack()


#Buttons
graph_all_button = Button(frame,text = "Graph",command= graph_all).pack()


selected_stock = StringVar()
menu = OptionMenu(frame, selected_stock, *ticks)
menu.pack(anchor='w', side=RIGHT)
menu.bind("<Configure>", on_stock_selected) 
median_button = Button(frame, text="Median", command=stock_median)
median_button.pack(side=LEFT)

mean_button = Button(frame, text="Mean", command=stock_mean)
mean_button.pack(side=LEFT)

week_button = Button(frame,text="Week",command=get_week_data)
week_button.pack(side=LEFT)


frame.pack()
window.mainloop()








# To download as excel
#close_df = pd.DataFrame()
#for tick in ticks:
#    data = yf.download(tick,start=startD,end=endD)
#    close_df[tick] = data['Close']
    
#output_folder = r"c:\New folder"
#output_file = os.path.join(output_folder,'stock.xlsx')
#close_df.to_excel(output_file)






""" Old Code

labels = "TTRAK.IS", "ERSU.IS", "DOAS.IS", "AKSA.IS", "CEMTS.IS", "EREGL.IS", "PETKM.IS", "AEFES.IS", "ASELS.IS", "INDES.IS"

plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')

plt.title('Stock Prices for All Tickers')

def choose(labelName):
    stocks = {
        "TTRAK.IS" : TTRAK_data, 
        "ERSU.IS" : ERSU_data, 
        "DOAS.IS" : DOAS_data, 
        "AKSA.IS" : AKSA_data, 
        "CEMTS.IS" : CEMTS_data, 
        "EREGL.IS" : EREGL_data, 
        "PETKM.IS" : PETKM_data, 
        "AEFES.IS" : AEFES_data, 
        "ASELS.IS" : ASELS_data, 
        "INDES.IS" : INDES_data
    }
    data = stocks[labelName]
  
# RadioButtons
ax_radio = plt.axes([0.05,0.4,0.10,0.5])
radio_buttons = RadioButtons(ax_radio, labels)
plt.subplots_adjust(left=0.25)

plt.legend(loc='upper left')  # Stocks color and name
radio_buttons.on_clicked(choose)
plt.show()
"""