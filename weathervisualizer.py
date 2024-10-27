import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox


class WeatherVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Weather Data Visualizer")

        # Create menu bar
        self.create_menu()

        # Input labels and entries for each day
        self.labels = []
        self.entries = []
        for i in range(7):
            label = tk.Label(master, text=f"Day {i+1} Temperature (°C):")
            label.pack()
            entry = tk.Entry(master)
            entry.pack()
            self.labels.append(label)
            self.entries.append(entry)

        # Button to calculate average and plot data
        self.calc_button = tk.Button(master, text="Calculate Average & Plot", command=self.calculate_and_plot)
        self.calc_button.pack()

        # Label for displaying average temperature
        self.average_label = tk.Label(master, text="")
        self.average_label.pack()

        # Matplotlib figure
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas.get_tk_widget().pack()

    def create_menu(self):
        # Menu bar setup
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Clear Data", command=self.clear_data)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def calculate_and_plot(self):
        try:
            # Get temperature data from entries
            temperatures = np.array([float(entry.get()) for entry in self.entries])
            average_temp = np.mean(temperatures)

            # Update average temperature label
            self.average_label.config(text=f"Average Temperature: {average_temp:.2f} °C")

            # Clear the previous plot
            self.ax.clear()
            self.ax.plot(range(1, 8), temperatures, marker='o', linestyle='-', color='blue')
            self.ax.set_xticks(range(1, 8))
            self.ax.set_xticklabels([f"Day {i+1}" for i in range(7)])
            self.ax.set_title("Weekly Temperature Data")
            self.ax.set_xlabel("Days")
            self.ax.set_ylabel("Temperature (°C)")
            self.ax.grid()

            # Draw the updated plot
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid temperature values.")

    def clear_data(self):
        """Clear all entry fields and reset the plot."""
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.average_label.config(text="")
        self.ax.clear()
        self.canvas.draw()

    def show_about(self):
        """Display an 'About' message."""
        messagebox.showinfo("About", "Weather Data Visualizer\nCreated with Python and Tkinter")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherVisualizer(root)
    root.mainloop()
