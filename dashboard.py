from tkinter import *

from combined import EntrySelectionClass
from purchase import PurchaseClass  # Assuming PurchaseClass is defined in purchase module
from sales import SalesClass  # Import SalesClass from sales module
from view import ViewClass  # Import ViewClass from view module
from datetime import datetime

class ClassicHitachi:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Classic Hitachi Management System")

        # TITLE
        Label(self.root, text="Classic Hitachi Management System", font=("Eras Bold ITC", 40), bg="Tan", fg="white").place(x=0, y=0, relwidth=1, height=70)

        # TIME N DATE
        self.clock = Label(self.root, text="", font=("Times new roman", 15), bg="Tan",fg="black")
        self.clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()  # Call to update the clock immediately

        # MENU
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="burlywood4")
        LeftMenu.place(x=0, y=102, width=200, height=565)
        lbl_menu = Label(LeftMenu, text="MENU", font=("Times new roman", 35, "bold"), fg="black").pack(side=TOP, fill=X, padx=10, pady=20)

        # BUTTONS
        btn_purchase = Button(LeftMenu, text="PURCHASE", command=self.show_purchase, font=("Times new roman", 15), bg="white", fg="Black", bd=3, cursor="hand2")
        btn_purchase.pack(side=TOP, fill=X, padx=10, pady=25)

        btn_sales = Button(LeftMenu, text="SALES", command=self.show_sales, font=("Times new roman", 15), bg="white", fg="Black", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X, padx=10, pady=25)

        btn_view = Button(LeftMenu, text="VIEW", command=self.show_view, font=("Times new roman", 15), bg="white", fg="Black", bd=3, cursor="hand2")
        btn_view.pack(side=TOP, fill=X, padx=10, pady=25)

        btn_exit = Button(LeftMenu, text="DATA ENTRY",command=self.show_entry, font=("Times new roman", 15), bg="white", fg="Black", bd=3, cursor="hand2")
        btn_exit.pack(side=TOP, fill=X, padx=10, pady=25)

        # REPORTS
        #self.lbl_purchase = Label(self.root, text="TOTAL PURCHASE\n[0]", bd=5, relief=RIDGE, bg="cyan", fg="black", font=("Arial Narrow", 20, "bold"))
        #self.lbl_purchase.place(x=350, y=150, height=150, width=300)

        #self.lbl_sales = Label(self.root, text="TOTAL SALES\n[0]", bd=5, relief=RIDGE, bg="cyan", fg="black", font=("Arial Narrow", 20, "bold"))
        #self.lbl_sales.place(x=800, y=150, height=150, width=300)

        #self.lbl_closingStock = Label(self.root, text="CLOSING STOCK\n[0]", bd=5, relief=RIDGE, bg="cyan", fg="black", font=("Arial Narrow", 20, "bold"))
        # self.lbl_closingStock.place(x=350, y=350, height=150, width=300)

    def update_clock(self):
        now = datetime.now()  # Get current date and time
        current_time = now.strftime("Date: %d-%m-%Y \t\t Time: %H:%M:%S")  # Format the time
        self.clock.config(text=current_time)  # Update the label text
        self.clock.after(1000, self.update_clock)  # Schedule to call this method again after 1 second

    def show_purchase(self):
        self.clear_main_content()
        self.purchase_content = PurchaseClass(self.root, self.return_to_dashboard)

    def show_sales(self):
        self.clear_main_content()
        self.sales_content = SalesClass(self.root, self.return_to_dashboard)

    def show_view(self):
        self.clear_main_content()
        self.view_content = ViewClass(self.root, self.return_to_dashboard)

    def show_entry(self):
        self.clear_main_content()
        self.entry_content = EntrySelectionClass(self.root, self.return_to_dashboard)


    def clear_main_content(self):
        for widget in self.root.winfo_children():
            if widget != self.clock:  # Exclude the clock label
                widget.destroy()

    def return_to_dashboard(self):
        self.clear_main_content()
        self.__init__(self.root)  # Reinitialize the dashboard

def main():
    root = Tk()
    obj = ClassicHitachi(root)
    root.mainloop()

if __name__ == "__main__":
    main()
