import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class ImageViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        # Style
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Use the "clam" theme

        # Center the window on the screen
        self.center_window()

        # Menu Bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Image", command=self.load_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        # Toolbar
        toolbar = ttk.Frame(root)
        toolbar.pack(side=tk.TOP, pady=20)  # Increase vertical padding for centering

        open_button = ttk.Button(toolbar, text="Open", command=self.load_image, style="Toolbutton.TButton")
        open_button.grid(row=0, column=0, padx=5)

        exit_button = ttk.Button(toolbar, text="Exit", command=root.destroy, style="Toolbutton.TButton")
        exit_button.grid(row=0, column=1, padx=5)

        # Image Label
        self.image_label = ttk.Label(root)
        self.image_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def center_window(self):
        # Calculate the window position to center it on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 800  
        window_height = 600  

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set the window position
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def load_image(self):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            try:
                # Open and display the image using Pillow
                image = Image.open(file_path)

                # Maximize the window
                self.root.state('zoomed')

                # Update the label with the new image
                tk_image = ImageTk.PhotoImage(image)
                self.image_label.config(image=tk_image)
                self.image_label.image = tk_image

                # Update status bar
                self.status_var.set(f"Image loaded: {file_path}")
            except Exception as e:
                self.status_var.set(f"Error loading image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)

    # Configure button style for better visibility
    app.style.configure("Toolbutton.TButton", padding=5, relief="flat", background="#4CAF50", foreground="white")

    root.mainloop()
