import pandas as pd
import tkinter as tk

def fetch_details():
    ev = entry.get()
    df['Customer ID'] = df['Customer ID'].astype(str)
    s = df[df['Customer ID'] == ev]

    ci = s['Customer ID'].iloc[0]
    up = s['Unit Price'].iloc[0]
    di = s['Discount'].iloc[0]
    sc = s['Shipping Cost'].iloc[0]
    qo = s['Quantity ordered new'].iloc[0]
    cn = s['Customer Name'].iloc[0]
    pn = s['Product Name'].iloc[0]
   

    label2.config(text=f"customer ID: {ci}")
    label3.config(text=f"Unit price: {up}")
    label4.config(text=f"Discound: {di}")
    label5.config(text=f"Shipping Cost: {sc}")
    label6.config(text=f"Quandity: {qo}")
    label7.config(text=f"Customer Name: {cn}")
    label8.config(text=f"Product: {pn}")



window =tk.Tk()
df = pd.read_excel("C://Users//Administrator//Downloads//SuperStoreUS-2015.xlsx")

label =tk.Label(window,text="Customer id: ")
entry =tk.Entry(window)
button =tk.Button(window,text="Click here",command=fetch_details)
label2 =tk.Label(window,text="Customer ID")
label3 =tk.Label(window,text="Unit Price")
label4 =tk.Label(window,text="Discount")
label5 =tk.Label(window,text="Shipping Cost")
label6 =tk.Label(window,text="Quandity")
label7 =tk.Label(window,text="Customer Name")
label8 =tk.Label(window,text="Product")





label.pack()
entry.pack()
button.pack()
label2.pack(side=tk.TOP)
label3.pack(side=tk.TOP)
label4.pack(side=tk.TOP)
label5.pack(side=tk.TOP)
label6.pack(side=tk.TOP)
label7.pack(side=tk.TOP)
label8.pack(side=tk.TOP)
window.mainloop()
