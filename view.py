from tkinter import *
from tkinter import messagebox, ttk
import openpyxl
import os
import TypeOfMachines
import subpart1_data

class ViewClass:
    def __init__(self, root, return_to_dashboard):
        self.root = root
        self.return_to_dashboard = return_to_dashboard
        self.inventory_data_file = "Inventory_Data.xlsx"  # File path for inventory data

        # Configure root window
        self.root.geometry("1200x700")  # Set the root window size
        self.root.title("View Page")  # Set the title of the root window

        # Frame to contain all widgets
        self.frame = Frame(self.root, bd=2, relief=RIDGE, bg="AntiqueWhite")
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # Frame covers entire root window

        Label(self.frame, text="VIEW PAGE", font=("Arial", 30, "bold"), bg="AntiqueWhite", fg="black").pack(pady=(50, 10))  # Added padding

        # Dropdowns for filters
        self.create_dropdowns()

        # Initialize dictionaries to store purchase and sales data
        self.purchase_data = {}
        self.sales_data = {}

        # Load data from files
        self.load_data()

        # Button to return to dashboard (bottom-right)
        btn_back = Button(self.frame, text="Back to Dashboard", command=self.return_to_dashboard, font=("Arial", 15),
                          bg="lightgray", fg="black", bd=3, cursor="hand2")
        btn_back.place(relx=1.0, rely=1.0, anchor=SE, x=-10, y=-10)

    def create_dropdowns(self):
        Label(self.frame, text="Type of Machine", font=("Arial", 14), bg="AntiqueWhite", fg="black").pack(pady=5)
        self.machine_type_var = StringVar()
        self.machine_type_dropdown = ttk.Combobox(self.frame, textvariable=self.machine_type_var)
        self.machine_type_dropdown['values'] = TypeOfMachines.type_of_machine_options
        self.machine_type_dropdown.pack(pady=5)

        Label(self.frame, text="SubPart 1", font=("Arial", 14), bg="AntiqueWhite", fg="black").pack(pady=5)
        self.subpart1_var = StringVar()
        self.subpart1_dropdown = ttk.Combobox(self.frame, textvariable=self.subpart1_var)
        self.subpart1_dropdown['values'] = subpart1_data.subpart1_options
        self.subpart1_dropdown.pack(pady=5)

        btn_filter = Button(self.frame, text="Filter", command=self.display_closing_stock_table, font=("Arial", 14),
                            bg="lightgray", fg="black", bd=3, cursor="hand2")
        btn_filter.pack(pady=20)

    def load_data(self):
        try:
            if os.path.isfile(self.inventory_data_file):
                wb = openpyxl.load_workbook(self.inventory_data_file)
                sheet = wb.active

                for row in sheet.iter_rows(min_row=2, values_only=True):
                    entry_type = row[0]  # Assuming Entry Type is in the first column (index 0)
                    machine_type = row[5]  # Assuming Type of Machine is in the sixth column (index 5)
                    subpart1 = row[6]  # Assuming SubPart 1 is in the seventh column (index 6)
                    quantity = float(row[9])  # Assuming Quantity is in the tenth column (index 9)

                    key = (machine_type, subpart1)
                    if entry_type == "Purchase":
                        if key in self.purchase_data:
                            self.purchase_data[key] += quantity
                        else:
                            self.purchase_data[key] = quantity
                    elif entry_type == "Sales":
                        if key in self.sales_data:
                            self.sales_data[key] += quantity
                        else:
                            self.sales_data[key] = quantity

            else:
                messagebox.showwarning("Warning", f"No inventory data found at {self.inventory_data_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def display_closing_stock_table(self):
        try:
            # Create or update Treeview with columns: "Type of Machine", "SubPart 1", "Remaining Quantity"
            if hasattr(self, 'tree'):
                self.tree.destroy()

            self.tree = ttk.Treeview(self.frame, columns=("type_of_machine", "subpart1", "remaining_quantity"), show="headings")
            self.tree.heading("type_of_machine", text="Type of Machine")
            self.tree.heading("subpart1", text="SubPart 1")
            self.tree.heading("remaining_quantity", text="Remaining Quantity")
            self.tree.pack(pady=20)

            selected_machine_type = self.machine_type_var.get()
            selected_subpart1 = self.subpart1_var.get()

            # Calculate remaining quantity for each combination of "Type of Machine" and "SubPart 1"
            for key in self.purchase_data.keys():
                machine_type, subpart1 = key
                if (selected_machine_type and machine_type != selected_machine_type) or \
                   (selected_subpart1 and subpart1 != selected_subpart1):
                    continue

                purchase_quantity = self.purchase_data.get(key, 0)
                sales_quantity = self.sales_data.get(key, 0)
                remaining_quantity = purchase_quantity - sales_quantity

                # Inserting data into the Treeview
                self.tree.insert("", "end", values=(machine_type, subpart1, remaining_quantity))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to display closing stock: {str(e)}")

    def return_to_dashboard(self):
        self.frame.destroy()
        self.return_to_dashboard()

# Test the view page independently
if __name__ == "__main__":
    root = Tk()

    def return_to_dashboard():
        root.destroy()  # Destroy the view window
        import dashboard  # Import your dashboard module
        dashboard.main()  # Call the main function or instantiate your dashboard class

    obj = ViewClass(root, return_to_dashboard)
    root.mainloop()
