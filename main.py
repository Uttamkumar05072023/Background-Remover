from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image
from rembg import remove

# Functioning Part
def upload_btn():
    global filename,original_img,resize_img
    filepath = filedialog.askopenfilename(title="Select Image File",filetypes=[("jpg","*.jpg"),("png","*.png"),("jpeg","*.jpeg")])
    if filepath:
        fullfilename = filepath.split("/")[-1]
        filename = fullfilename.split(".")[0]
        original_img = Image.open(filepath)
        resize_img = original_img.resize((472, 472))
        img = ImageTk.PhotoImage(resize_img)
        upload.configure(image=img)
        upload.image = img
    
def removebg_btn():
    global original_img_nobg,remobg
    try:
        original_img_nobg = remove(original_img)
        resize_img_nobg = remove(resize_img)
    except:
        messagebox.showerror("Error", "Upload Image First")
    else:
        img = ImageTk.PhotoImage(resize_img_nobg)
        download.configure(image=img)
        download.image = img
        remobg = True

def download_btn():
    try:
        if remobg:
            filepath = filedialog.asksaveasfilename(initialfile=filename, defaultextension=".png", filetypes=[("png","*.png")], title="Save Image")
    except:
        messagebox.showerror("Error", "Remove Background First")
    else:
        original_img_nobg.save(filepath)
        messagebox.showinfo("Success", "Image Downloaded Successfully")

def reset_btn():
    upload.configure(image=uploadImage)
    download.configure(image=downloadImage)
    
def exit_btn():
    root.destroy()

# GUI Part
root = Tk()
root.title("Background Remover")
root.geometry("1200x670")
root.resizable(0, 0)
root.iconbitmap("remove_ico.ico")
root.config(bg="grey")

# ================ MAIN LABLE ================
Label(root,text="Background Remover", font="arial 30 bold", bg="lightblue", fg="black").pack(side=TOP, fill=X,ipady=10)

# ================ IMAGE FRAME ================
imageFrame = Frame(root,bg="grey",height=520)

uploadFrame = Frame(imageFrame,height=480,width=480,highlightthickness=2,highlightbackground="black")
uploadImage = PhotoImage(file="upload.png")
upload = Label(uploadFrame, image=uploadImage)
upload.place(x=0,y=0)
uploadFrame.place(x=80,y=20)

downloadFrame = Frame(imageFrame,height=480,width=480,highlightthickness=2,highlightbackground="black")
downloadImage = PhotoImage(file="download.png")
download = Label(downloadFrame, image=downloadImage)
download.place(x=0,y=0)
downloadFrame.place(x=640,y=20)

imageFrame.pack(side=TOP, fill=X)

# ================ BUTTON FRAME ================
buttonFrame = LabelFrame(root,bg="lightgreen",height=77)

uploadimg = PhotoImage(file="uplobtn.png")
Button(buttonFrame,image=uploadimg,compound=LEFT, text="Upload Image",font="arial 18 bold", bg="lightblue", fg="black",width=220,command=upload_btn).place(x=35,y=10)

removeimg = PhotoImage(file="remove.png")
Button(buttonFrame,image=removeimg,compound=LEFT, text="Remove Background",font="arial 18 bold", bg="lightblue", fg="black",width=300,command=removebg_btn).place(x=285,y=10)

downloadimg = PhotoImage(file="downbtn.png")
Button(buttonFrame,image=downloadimg,compound=LEFT, text="Download Image",font="arial 18 bold", bg="lightblue", fg="black",width=250,command=download_btn).place(x=615,y=10)

resetimg = PhotoImage(file="reset.png")
Button(buttonFrame,image=resetimg,compound=LEFT, text="Reset",font="arial 18 bold", bg="lightblue", fg="black",width=130,command=reset_btn).place(x=895,y=10)

exitimg = PhotoImage(file="exit.png")
Button(buttonFrame,image=exitimg,compound=LEFT, text="Exit",font="arial 18 bold", bg="lightblue", fg="black",width=110,command=exit_btn).place(x=1055,y=10)

buttonFrame.pack(side=TOP, fill=X)

root.mainloop()