import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class BoundingBoxGUI:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.root = tk.Tk()
        self.root.title("Bounding Box GUI")
        self.canvas = tk.Canvas(self.root, width=self.image.width, height=self.image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

        self.top_left_x = None
        self.top_left_y = None
        self.bottom_right_x = None
        self.bottom_right_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_button_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.root.mainloop()

    def on_button_press(self, event):
        self.top_left_x = event.x
        self.top_left_y = event.y

    def on_button_drag(self, event):
        self.canvas.delete("bbox")  # Clear previous bounding box
        self.bottom_right_x = event.x
        self.bottom_right_y = event.y
        self.canvas.create_rectangle(
            self.top_left_x, self.top_left_y,
            self.bottom_right_x, self.bottom_right_y,
            outline="red", width=2, tags="bbox"
        )

    def on_button_release(self, event):
        self.save_cropped_image()

    def save_cropped_image(self):
        if self.top_left_x is not None and self.top_left_y is not None and \
           self.bottom_right_x is not None and self.bottom_right_y is not None:
            bbox = (self.top_left_x, self.top_left_y, self.bottom_right_x, self.bottom_right_y)
            cropped_image = self.image.crop(bbox)
            cropped_image.save("cropped_image.jpg")
            print("Cropped image saved as 'cropped_image.jpg'.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    # Ask user to enter the path of the image file
    image_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if image_path:
        gui = BoundingBoxGUI(image_path)
    else:
        print("No image selected.")