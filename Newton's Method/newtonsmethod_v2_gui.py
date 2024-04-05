import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class NewtonsMethodApp:
    def __init__(self, master):
        self.master = master
        master.title("Newton's Method App")

        self.num_CTkLabel = customtkinter.CTkLabel(master, text="Enter a number:")
        self.num_CTkLabel.grid(row=0, column=0)

        self.num_CTkEntry = customtkinter.CTkEntry(master)
        self.num_CTkEntry.grid(row=0, column=1)

        self.guess_CTkLabel = customtkinter.CTkLabel(master, text="Enter initial guess:")
        self.guess_CTkLabel.grid(row=1, column=0)

        self.guess_CTkEntry = customtkinter.CTkEntry(master)
        self.guess_CTkEntry.grid(row=1, column=1)

        self.result_CTkTextbox = customtkinter.CTkTextbox(master, height=200, width=500)
        self.result_CTkTextbox.grid(row=2, columnspan=2)

        self.calculate_CTkButton = customtkinter.CTkButton(master, text="Calculate", command=self.calculate)
        self.calculate_CTkButton.grid(row=3, columnspan=2)

    def calculate(self):
        num = float(self.num_CTkEntry.get())
        initial_guess = float(self.guess_CTkEntry.get())
        self.root(num, initial_guess)

    def root(self, num, initial_guess):
        approximated = False
        iteration = 0

        if (initial_guess**2 - num == 0):
            initial_guess += 1
            self.result_CTkTextbox.insert(customtkinter.END, "Error: Results in zero, adding one to initial iteration.\n")

        x = initial_guess

        while not approximated:
            if (x == math.sqrt(num)):
                approximated = True
                self.result_CTkTextbox.insert(customtkinter.END, "********************************************************\n")
                self.result_CTkTextbox.insert(customtkinter.END, "Finished.\n")
            else:
                x = x - ((x**2 - num)/(2*x))
                iteration += 1
                percent_diff = (abs(x - math.sqrt(num)) / ((math.sqrt(num)+x)/2) * 100.0)
                self.result_CTkTextbox.insert(customtkinter.END, "********************************************************\n")
                self.result_CTkTextbox.insert(customtkinter.END, "Iteration #{} {}\n".format(iteration, x))
                self.result_CTkTextbox.insert(customtkinter.END, "Absolute Error:{} (Approx. {}%)\n".format((math.sqrt(num)-x), round(percent_diff, 2)))

def main():
    root = customtkinter.CTk()
    app = NewtonsMethodApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
