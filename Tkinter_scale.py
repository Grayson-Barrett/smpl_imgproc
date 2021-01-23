import cv2 as cv
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # set scale for min value
        self.minval = Scale(self, orient="horizontal",
                           from_=0, to=600,
                           command=self.change_val)
        self.minval_label = Label(self, text="Max Val")
        self.minval.pack(side="bottom", fill="x")
        self.minval_label.pack(side="bottom")

        # set scale for max value
        self.maxval = Scale(self, orient="horizontal",
                            from_=0, to=600,
                            command=self.change_val)
        self.maxval_label = Label(self, text="Min Val")
        self.maxval.pack(side="bottom", fill="x")
        self.maxval_label.pack(side="bottom")

        self.btn = Button(root,text="select an image",command=self.select_image)
        self.btn.pack(side="bottom",fill="both",expand="yes",padx="10",pady="10")

    def select_image(self):
        global panelA, panelB, path

        path = filedialog.askopenfilename()

        if len(path) > 0:
            # load the image from disk
            img = cv.imread(path)
            grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            edged = cv.Canny(grey,self.minval.get(),self.maxval.get())

            # Convert img to RGB
            img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

            # convert images to PIL format
            img = Image.fromarray(img)
            edged = Image.fromarray(edged)

            # convert images to ImageTK format
            img = ImageTk.PhotoImage(img)
            edged = ImageTk.PhotoImage(edged)

            #if the panel are none, initialize them:
            if panelA is None or panelB is None:
                # the first panel will store out original images
                panelA = Label(image=img)
                panelA.image = img
                panelA.pack(side="left", padx=10,pady=10)

                # while th second panel will store the edge map
                panelB = Label(image=edged)
                panelB.image = edged
                panelB.pack(side="right", padx=10,pady=10)

                # otherwise, update the image panels
            else:
                # update panels
                panelA.configure(image=img)
                panelB.configure(image=edged)
                panelA.image = img
                panelB.image = edged

        return 0

    def change_val(self,value):
        if panelB is None:
            pass
        else:

            img = cv.imread(path)
            grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            edged = cv.Canny(img,self.minval.get(),self.maxval.get())

            edged = Image.fromarray(edged)
            edged = ImageTk.PhotoImage(edged)
            panelB.configure(image=edged)
            panelB.image = edged
        return 0


if __name__ == "__main__":
    root = Tk()
    panelA = None
    panelB = None
    Example(root).pack(fill="both", expand=True);
    root.mainloop()