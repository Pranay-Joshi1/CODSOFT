import tkinter as tk

class to_do_list():
    def __init__(self):
        self.root= tk.Tk()
        self.root.geometry("600x600")
        self.root.title("To-Do List")

        self.label1 = tk.Label(self.root, text = "Welcome to the To-Do List App",font=('Brother 1816',20))
        self.label1.pack(padx=10, pady=10)
        
        #Created a frame, the list goes to its left and scroll bar to the right
        self.frame1 =tk.Frame(self.root)
        self.frame1.pack(pady=10)
        self.list = tk.Listbox(self.frame1,font=("Intro Regular Alt", 20), bg="#FFFFFF", 
                                  bd=0, highlightthickness=0, selectbackground="#a6a6a6", 
                                  activestyle="none")
        self.list.pack(side="left",fill="both")
        self.scrollbar = tk.Scrollbar(self.frame1)
        self.scrollbar.pack(side="right",fill="both")
        self.list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list.yview)

        self.item = tk.Entry(self.root, font=('Segoe UI',12))
        self.item.pack(padx=10, pady=10)
        
        self.frame2= tk.Frame(self.root)
        self.frame2.columnconfigure(0,weight=1)
        self.frame2.columnconfigure(1,weight=1)
        
        self.addbtn = tk.Button(self.frame2, text="Add Item to List", font=('Intro Alt',12), command= self.add_item)
        self.clrbtn = tk.Button(self.frame2, text="Clear List", font=('Intro Alt',12), command= self.clear_list)
        self.delbtn = tk.Button(self.frame2, text="Delete Item", font=('Intro Alt',12), command= self.del_item)
        self.addbtn.grid(row=0, column=0,padx=5)
        self.clrbtn.grid(row=0, column=1,padx=5)
        self.delbtn.grid(row=0, column=2,padx=5)
        self.frame2.pack(padx=10, pady=10)
        
        self.root.mainloop()
         
    def add_item(self):
        self.list.insert(tk.END,self.item.get())
    
    def clear_list(self):
        self.list.delete(0,tk.END)
    
    def del_item(self):
        self.list.delete(tk.ANCHOR)
to_do_list()