import yfinance as yf
import datetime as datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #To integrated plots to tkinter
from matplotlib.widgets import RadioButtons
import numpy as np
from tkinter import *
#import os
#import pandas as pd
#from openpyxl.workbook import Workbook
# All stocks for different actions


ticks = ["TTRAK.IS", "ERSU.IS", "DOAS.IS", "AKSA.IS", "CEMTS.IS", "EREGL.IS", "PETKM.IS", "AEFES.IS", "ASELS.IS", "INDES.IS"]

start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

window = Tk()
window.title("Stocks")
window.geometry("600x400")


fig, ax = plt.subplots()


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

def graph():
#All stocks in one plot
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


frame = Frame(window)
label = Label(text="Stocks")
label.pack()


canvas = FigureCanvasTkAgg(fig,master=window)
canvas.get_tk_widget().pack()

button = Button(frame,text = "Graph",command= graph).pack()

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