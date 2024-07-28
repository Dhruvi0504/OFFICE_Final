from tkinter import Tk, Label, Entry, Button, StringVar, Frame
import dashboard  # Ensure this imports your dashboard module correctly

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#f0f0f0")

        # Create a frame for better layout
        frame = Frame(self.root, bg="white", padx=20, pady=20)
        frame.pack(pady=50)

        # Static admin credentials
        self.director_username = "director"
        self.director_password = "director123"

        self.admin_username = "admin"
        self.admin_password = "admin123"

        # Username and Password variables
        self.username_var = StringVar()
        self.password_var = StringVar()

        # Login form
        Label(frame, text="Admin Login", font=("Helvetica", 20, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))

        Label(frame, text="Username", bg="white").grid(row=1, column=0, sticky="w")
        Entry(frame, textvariable=self.username_var, width=30).grid(row=1, column=1, padx=10, pady=5)

        Label(frame, text="Password", bg="white").grid(row=2, column=0, sticky="w")
        Entry(frame, textvariable=self.password_var, show='*', width=30).grid(row=2, column=1, padx=10, pady=5)

        Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=20)

    def login(self):
        if ((self.username_var.get() == self.director_username and self.password_var.get() == self.director_password) or (self.username_var.get() == self.admin_username and self.password_var.get() == self.admin_password)):
            self.root.destroy()  # Close the login window
            dashboard.main()  # Open the dashboard
        else:
            Label(self.root, text="Invalid credentials!", fg="red", bg="#f0f0f0").pack(pady=5)

def main():
    root = Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
