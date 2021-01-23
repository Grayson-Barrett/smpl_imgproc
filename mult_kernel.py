import cv2 as cv
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        global panelA, panelB, path

        # # Image Selection
        # btn that allows user to select and display the image
        self.btnSI = Button(root, text="select an image", command=self.select_image)
        self.btnSI.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

        # # Canny edge detection
        # btn that activates canny edge
        self.btnCE = Button(root, text="Edge detection", command=self.canny_scales)
        self.btnCE.pack(side="left", fill="both", expand="yes", padx="10", pady="10")

    def select_image(self):
        global panelA, path

        path = filedialog.askopenfilename()

        if len(path) > 0:
            # load the image from disk
            img = cv.imread(path)

            # convert image to RGB
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            # convert image to PIL format
            img = Image.fromarray(img)

            # convert images to ImageTK format
            img = ImageTk.PhotoImage(img)

            # if the panel are none, initialize them:
            if panelA is None:
                # the first panel will store out original images
                panelA = Label(image=img)
                panelA.image = img
                panelA.pack(side="left", padx=10, pady=10)

                # otherwise, update the image panels
            else:
                # update panels
                panelA.configure(image=img)
                panelA.image = img
        return 0

    def canny_scales(self):

        # set scale for min value
        self.minval = Scale(self, orient="horizontal",
                            from_=0, to=600)
        self.minval_label = Label(self, text="Max Val")
        self.minval.pack(side="bottom", fill="x")
        self.minval_label.pack(side="bottom")

        # set scale for max value
        self.maxval = Scale(self, orient="horizontal",
                            from_=0, to=600)
        self.maxval_label = Label(self, text="Min Val")
        self.maxval.pack(side="bottom", fill="x")
        self.maxval_label.pack(side="bottom")

        global panelB
        img = cv.imread(path)
        grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edged = cv.Canny(grey, self.minval.get(), self.maxval.get())

        # convert images to PIL format
        edged = Image.fromarray(edged)

        # convert images to ImageTK format
        edged = ImageTk.PhotoImage(edged)

        if panelB is None:
            # panelB will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)
        else:
            # update panels
            panelB.configure(image=edged)
            panelB.image = edged

        return 0


if __name__ == "__main__":
    root = Tk()
    panelA = None
    panelB = None
    Example(root).pack(fill="both", expand=True);
    root.mainloop()
