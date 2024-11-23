import tkinter as tk
from tkinter import messagebox, ttk
import pymysql.cursors
def get_connection_localDB():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Dravidaishu!7305',
        db='nextgen_project',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


def save_data(Name, Place, Degree, Gender, Years_of_Experience, Additional_Experience):
    try:
        connection = get_connection_localDB()

        with connection.cursor() as cursor:
            sql = "Insert into nextgenproject (Name, Place, Degree, Gender, Years_of_Experience, Additional_Experience) values (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (Name, Place, Degree, Gender, Years_of_Experience, Additional_Experience))

        connection.commit()
        messagebox.showinfo("Success", "Data saved successfully!")


        show_saved_information(Name, Place, Degree, Gender, Years_of_Experience, Additional_Experience)

    except pymysql.Error as e:
        print(f"Error saving data: {e}")
        messagebox.showerror("Error", "Failed to save data to database.")



def show_saved_information(Name, place, Degree, Gender, Years_of_Experience, Additional_experience):
    info_window = tk.Toplevel()
    info_window.title("Saved Information")

    info_frame = ttk.Frame(info_window, padding="20")
    info_frame.pack()

    tk.Label(info_frame, text="Name:").grid(row=0, column=0, sticky="w")
    tk.Label(info_frame, text=Name).grid(row=0, column=1, sticky="w")

    tk.Label(info_frame, text="Place:").grid(row=1, column=0, sticky="w")
    tk.Label(info_frame, text=Place).grid(row=1, column=1, sticky="w")

    tk.Label(info_frame, text="Degree:").grid(row=2, column=0, sticky="w")
    tk.Label(info_frame, text=Degree).grid(row=2, column=1, sticky="w")

    tk.Label(info_frame, text="Gender:").grid(row=3, column=0, sticky="w")
    tk.Label(info_frame, text=Gender).grid(row=3, column=1, sticky="w")

    tk.Label(info_frame, text="Years_of_Experience:").grid(row=4, column=0, sticky="w")
    tk.Label(info_frame, text=Years_of_Experience).grid(row=4, column=1, sticky="w")

    tk.Label(info_frame, text="Additional_Experience:").grid(row=5, column=0, sticky="w")
    tk.Label(info_frame, text=Additional_Experience).grid(row=5, column=1, sticky="w")


def open_about_me_page():
    about_me_window = tk.Toplevel()
    about_me_window.title("nextgen_project")

    scroll_frame = ttk.Frame(about_me_window)
    scroll_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


    scroll_bar = ttk.Scrollbar(scroll_frame, orient=tk.VERTICAL)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)


    canvas = tk.Canvas(scroll_frame, yscrollcommand=scroll_bar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    scroll_bar.config(command=canvas.yview)


    content_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)


    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>", on_configure)

    menu_bar = tk.Menu(about_me_window)
    about_me_window.config(menu=menu_bar)


    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Save", command=lambda: save_data(entry_Name.get(), var_Place.get(),
                                                                  get_selected_Degree(var_Degree),
                                                                  var_Gender.get(),
                                                                  experience_spinbox.get(),
                                                                  entry_experience.get("1.0", tk.END)))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=about_me_window.destroy)


    label_name = tk.Label(content_frame, text="Name:")
    label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    entry_name = tk.Entry(content_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)


    label_place = tk.Label(content_frame, text="Place:")
    label_place.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

    var_place = tk.StringVar()
    var_place.set("")

    places = ["ECR", "Avadi", "poonamalle", "porur", "broadway"]
    for i, place in enumerate(places):
        radio_place = tk.Radiobutton(content_frame, text=place, variable=var_place, value=place)
        radio_place.grid(row=1, column=i + 1, padx=10, pady=5, sticky=tk.W)


    label_degree = tk.Label(content_frame, text="Degrees:")
    label_degree.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

    degrees = ["SSLC", "HSC", "Master's", "Phd", "BE.CS", "BTECH.IT", "BTECH.AIDS", "BTECH.AIML", "Bsc,Artificial_intelligence", "Bba", "B.Com"]
    var_degrees = []
    for i, degree in enumerate(degrees):
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(content_frame, text=degree, variable=var)
        checkbutton.grid(row=2, column=i + 1, padx=10, pady=5, sticky=tk.W)
        var_degrees.append((degree, var))


    label_gender = tk.Label(content_frame, text="Gender:")
    label_gender.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

    var_gender = tk.StringVar()
    radio_male = tk.Radiobutton(content_frame, text="Male", variable=var_gender, value="Male")
    radio_male.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
    radio_female = tk.Radiobutton(content_frame, text="Female", variable=var_gender, value="Female")
    radio_female.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)


    label_experience = tk.Label(content_frame, text="Years of Experience:")
    label_experience.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

    experience_spinbox = tk.Spinbox(content_frame, from_=0, to=50)
    experience_spinbox.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)


    label_additional = tk.Label(content_frame, text="Additional Experience:")
    label_additional.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

    entry_experience = tk.Text(content_frame, height=5, width=30)
    entry_experience.grid(row=5, column=1, padx=10, pady=5, columnspan=3, sticky=tk.W)



    save_button = tk.Button(content_frame, text="Save", command=lambda: save_data(
        entry_name.get(),
        var_place.get(),
        get_selected_degrees(var_degrees),
        var_gender.get(),
        experience_spinbox.get(),
        entry_experience.get("1.0", tk.END)
    ))
    save_button.grid(row=6, column=0, pady=10)


def get_selected_degrees(degrees_list):
    selected_degrees = []
    for degree, var in degrees_list:
        if var.get() == 1:
            selected_degrees.append(degree)
    return ', '.join(selected_degrees)


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admindravid" and password == "dravidaishu!7305":
        print(f"Login Successful! Username: {username}, Password: {password}")
        root.withdraw()  # Hide login window
        open_about_me_page()  # Open the About Me page
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")



root = tk.Tk()
root.title("Login Page")


tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)


tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)


login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
