from main import *

import tkinter


class OurApp(tk.Frame):
    def __init__(self, master=None,**options):
        tk.Frame.__init__(self, master,**options)
        self.pack()
        self.user_depth = tk.DoubleVar()
        self.master.title("A gui for Gumbel distribution")
        ww = 628  # width
        wh = 382  # height
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2
        # assign geometry
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))
        # assign space holders around widgets
        self.dx = 5
        self.dy = 5
        tk.Label(master, text=" choose the Extrapolation years")


        tk.Entry(self, bg="alice blue", width=20, textvariable=self.user_depth).grid(stick=tk.EW, row=0, column=1,
                                                                                     padx=5)
        self.eval_button = tk.Button(self, text="Estimate Discharge", bg="snow2", fg="dark violet",
                                     command=lambda: self.call_estimator())
        self.eval_button.grid(row=0, column=2, padx=5)
        self.button2 = tkinter.Button(self,text='hydrograph', command= lambda :self.plotting())
        self.button2.grid(row=5, column=2, padx=10)

    def call_estimator(self):
            try:
                year= float(self.user_depth.get())
            except tk.TclError:
                return showerror("ERROR", "Non-numeric value entered.")
            self.eval_button.config(fg="green4", bg="DarkSeaGreen1")
            showinfo("Result", "The estimated Discharge is: " + str(self.estimate_u(year)))

    def estimate_u(self,h):
            try:
                return flood_discharge_dict[h]
            except ValueError:
                showerror("ERROR: Bad values defined.")
                return None
            except TypeError:
                showerror("ERROR: Bad data types defined.")
                return None
    def plotting(self):
        t= data['Year']
        y= data['Discharge [CMS]']

        figure = plt.figure(figsize=(5, 4), dpi=100)
        figure.add_subplot(111).plot(t, y)
        chart = FigureCanvasTkAgg(figure,master=tkinter.Tk())
        chart.draw()
        chart.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    pass




if __name__ == '__main__':
    OurApp().mainloop()












