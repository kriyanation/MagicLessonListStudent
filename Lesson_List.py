import tkinter as tk
from tkinter import ttk
import data_capture


class MagicLessonList(tk.Frame):
    def __init__(self,parent,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        s = ttk.Style(self)
        s.configure('TScrollbar', background="gray16", foreground="snow")
        s.map('TScrollbar', background=[('active', '!disabled', 'gray16'), ('pressed', "snow")],
              foreground=[('pressed', "snow"), ('active', "gray16")])
        self.configure(background='gray25')
        self.l_canvas = tk.Canvas(self, background='gray25',highlightthickness=0)
        self.l_canvas.grid(row=0, column=0, columnspan=5)
        self.lesson_frame = tk.Frame(self.l_canvas, width=770,
                                    height=300,
                                    background='gray25')
        self.scrollbar = ttk.Scrollbar(self, style='TScrollbar')
        self.l_canvas.config(yscrollcommand=self.scrollbar.set)
        self.l_canvas.create_window((0, 0), window=self.lesson_frame, anchor='nw')
        self.lesson_frame.bind("<Configure>", self.l_function)
        self.scrollbar.config(command=self.l_canvas.yview)
        self.scrollbar.grid(row=0, column=5, sticky="nsew")
        self.lesson_view_label = ttk.Label(self, text="Lessons View",
                                      font=("Comic Sans", 14, 'bold'), background="gray16", foreground="snow")
        self.scroll_frame = ttk.Frame(self)
        self.headerlesson_id_label = ttk.Label(self.lesson_frame, text="ID", font=('TkDefaultFont', 16),
                                           background='gray25',
                                           foreground='snow')
        self.headerlessonlabel = ttk.Label(self.lesson_frame, text="Lesson Name", font=('TkDefaultFont', 16), background='gray25',
                                         foreground='snow')
        self.headerfactlabel = ttk.Label(self.lesson_frame, text="Lesson Terms", font=('TkDefaultFont', 16),
                                          background='gray25', foreground='snow')
        self.headerstepslabel = ttk.Label(self.lesson_frame, text="Lesson Skills", font=('TkDefaultFont', 16),
                                           background='gray25', foreground='snow')
        self.headersteps_numberlabel = ttk.Label(self.lesson_frame, text="Skill Steps", font=('TkDefaultFont', 16),
                                          background='gray25', foreground='snow')

        self.headerlesson_id_label.grid(row=0, column=0,padx=20, pady=10,sticky=tk.W)
        self.headerlessonlabel.grid(row=0, column=1 ,padx=20,pady=10,sticky=tk.W)
        self.headerfactlabel.grid(row=0, column=2,padx=20,pady=10,sticky=tk.W)
        self.headerstepslabel.grid(row=0, column=3, padx=20,pady=10,sticky=tk.W)
        self.headersteps_numberlabel.grid(row=0, column=4,padx=20, pady=10,sticky=tk.W)

        self.lesson_list = data_capture.get_Lessons()
        row_index=1
        for element in self.lesson_list:

            bgcolor = "gray25"
            self.dataidlabel = ttk.Label(self.lesson_frame, text=element[0], font=('TkDefaultFont', 12),
                                           foreground='aquamarine', wraplength=200, background=bgcolor)
            self.datanamelabel = ttk.Label(self.lesson_frame, text=element[1], font=('TkDefaultFont', 12),
                                           foreground='aquamarine', wraplength=200, background=bgcolor)
            self.datafactlabel = ttk.Label(self.lesson_frame, text=element[2]+'\n'+element[3]+'\n'+element[4], font=('TkDefaultFont', 12),
                                         foreground='aquamarine', wraplength=300, background=bgcolor)
            self.datasteplabel = ttk.Label(self.lesson_frame,
                                           text=element[5],
                                           font=('TkDefaultFont', 12),
                                           foreground='aquamarine', wraplength=200, background=bgcolor)
            self.datastepnumbers = ttk.Label(self.lesson_frame,
                                           text=str(element[6]),
                                           font=('TkDefaultFont', 12),
                                           foreground='aquamarine', wraplength=200, background=bgcolor)
            self.dataidlabel.grid(row=row_index,column=0,padx=20,sticky=tk.W)
            self.datanamelabel.grid(row=row_index, column=1,padx=20,sticky=tk.W)
            self.datafactlabel.grid(row=row_index, column=2,padx=20,sticky=tk.W)
            self.datasteplabel.grid(row=row_index, column=3,padx=20,sticky=tk.W)
            self.datastepnumbers.grid(row=row_index, column=4,padx=20,sticky=tk.W)
            row_index += 1

    def l_function(self,event):
       self.l_canvas.configure(scrollregion=self.l_canvas.bbox("all"),width=1080,height=720)



if __name__== "__main__":
    dashboard_app = tk.Tk()
    dashboard_app.configure(background="gray25")
    dashboard_app.title("Learning Room Lesson List")
    dashboard_app.geometry("1200x800")
    frame = MagicLessonList(dashboard_app)
    dashboard_app.rowconfigure(0,weight=1)
    dashboard_app.columnconfigure(0, weight=1)
    frame.grid(row=0,column=0)
    dashboard_app.mainloop()