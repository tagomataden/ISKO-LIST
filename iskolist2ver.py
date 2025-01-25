import tkinter as tk
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    show_all_todos()

def show_all_todos():
    for widget in content_area.winfo_children():
        widget.destroy()

    header_label = tk.Label(
        content_area, text="All To-Dos", font=("Arial", 20, "bold"), bg="#E5E5E5"
    )
    header_label.pack(pady=10, anchor="w", padx=20)

    for task in tasks[:]:
        if not task["completed"]:
            task_frame = tk.Frame(content_area, bg="#FFFFFF", relief="flat", bd=1)
            task_frame.pack(fill="x", padx=20, pady=5)

            task_check = tk.Checkbutton(
                task_frame,
                bg="#FFFFFF",
                relief="flat",
                command=lambda t=task: complete_task(t),
            )
            task_check.pack(side="left", padx=10, pady=10)

            task_details = tk.Frame(task_frame, bg="#FFFFFF")
            task_details.pack(side="left", fill="x", expand=True, padx=10)

            task_title = tk.Label(
                task_details,
                text=task["name"],
                font=("Arial", 14, "bold"),
                bg="#FFFFFF",
                anchor="w",
            )
            task_title.pack(fill="x")

            truncated_description = (
                (task["description"][:50] + "...") if len(task["description"]) > 50 else task["description"]
            )
            task_description = tk.Label(
                task_details,
                text=truncated_description,
                font=("Arial", 10),
                fg="#777777",
                bg="#FFFFFF",
                anchor="w",
            )
            task_description.pack(fill="x")

            task_title.bind("<Button-1>", lambda e, t=task: show_task_details(t))

            delete_button = tk.Button(
                task_frame,
                text="Delete",
                bg="#A83232",
                fg="white",
                font=("Arial", 10),
                command=lambda t=task: delete_task(t),
            )
            delete_button.pack(side="right", padx=10, pady=10)

def show_completed_tasks():
    for widget in content_area.winfo_children():
        widget.destroy()

    header_label = tk.Label(
        content_area, text="Completed Tasks", font=("Arial", 20, "bold"), bg="#E5E5E5"
    )
    header_label.pack(pady=10, anchor="w", padx=20)

    for task in tasks[:]:
        if task["completed"]:
            task_frame = tk.Frame(content_area, bg="#FFFFFF", relief="flat", bd=1)
            task_frame.pack(fill="x", padx=20, pady=5)

            task_details = tk.Frame(task_frame, bg="#FFFFFF")
            task_details.pack(fill="x", padx=10, pady=10)

            task_title = tk.Label(
                task_details,
                text=task["name"],
                font=("Arial", 14, "bold"),
                bg="#FFFFFF",
                anchor="w",
            )
            task_title.pack(fill="x")

            task_description = tk.Label(
                task_details,
                text=task["description"],
                font=("Arial", 10),
                fg="#777777",
                bg="#FFFFFF",
                anchor="w",
            )
            task_description.pack(fill="x")

            delete_button = tk.Button(
                task_frame,
                text="Delete",
                bg="#A83232",
                fg="white",
                font=("Arial", 10),
                command=lambda t=task: delete_completed_task(t),
            )
            delete_button.pack(side="right", padx=10, pady=10)

def delete_completed_task(task):
    tasks.remove(task)  # Remove the task from the list
    show_completed_tasks()  # Refresh the Completed Tasks view

def complete_task(task):
    task["completed"] = True
    show_all_todos()
def show_task_details(task):
    details_popup = tk.Toplevel(app)
    details_popup.title("Task Details")
    details_popup.geometry("400x300")
    details_popup.configure(bg="#FFFFFF")
    center_popup(details_popup, 400, 300)
    tk.Label(
        details_popup, text="Task Name:", font=("Arial", 12, "bold"), bg="#FFFFFF"
    ).pack(anchor="w", padx=10, pady=(10, 0))
    name_entry = tk.Entry(details_popup, font=("Arial", 12), bg="#F5F5F5")
    name_entry.insert(0, task["name"])
    name_entry.pack(fill="x", padx=10, pady=(0, 10))
    tk.Label(
        details_popup, text="Task Description:", font=("Arial", 12, "bold"), bg="#FFFFFF"
    ).pack(anchor="w", padx=10, pady=(10, 0))
    desc_text = tk.Text(details_popup, font=("Arial", 12), bg="#F5F5F5", height=8)
    desc_text.insert("1.0", task["description"])
    desc_text.pack(fill="both", padx=10, pady=(0, 10), expand=True)
    button_frame = tk.Frame(details_popup, bg="#FFFFFF")
    button_frame.pack(fill="x", pady=(10, 0))
    save_button = tk.Button(
        button_frame,
        text="Save",
        bg="#A83232",
        fg="white",
        font=("Arial", 12),
        command=lambda: save_task_details(task, name_entry.get(), desc_text.get("1.0", "end").strip(), details_popup),
    )
    save_button.pack(side="right", padx=(0, 10))
    cancel_button = tk.Button(
        button_frame,
        text="Cancel",
        bg="#FFFFFF",
        fg="black",
        font=("Arial", 12),
        command=details_popup.destroy,
    )
    cancel_button.pack(side="right", padx=(0, 10))
def save_task_details(task, new_name, new_description, popup):
    task["name"] = new_name
    task["description"] = new_description
    popup.destroy()
    show_all_todos()
def add_task_popup():
    popup = tk.Toplevel(app)
    popup.title("New Task")
    popup.geometry("400x250")
    popup.configure(bg="#FFFFFF")
    center_popup(popup, 400, 250)
    tk.Label(
        popup, text="Task Name:", font=("Arial", 12, "bold"), bg="#FFFFFF"
    ).pack(anchor="w", padx=10, pady=(10, 0))
    task_name_entry = tk.Entry(popup, font=("Arial", 12), bg="#F5F5F5")
    task_name_entry.pack(fill="x", padx=10, pady=(0, 10))
    tk.Label(
        popup, text="Task Description:", font=("Arial", 12, "bold"), bg="#FFFFFF"
    ).pack(anchor="w", padx=10, pady=(10, 0))
    task_desc_entry = tk.Text(popup, font=("Arial", 12), bg="#F5F5F5", height=4)
    task_desc_entry.pack(fill="x", padx=10, pady=(0, 10))
    button_frame = tk.Frame(popup, bg="#FFFFFF")
    button_frame.pack(fill="x", pady=(10, 0))
    create_button = tk.Button(
        button_frame,
        text="Create",
        bg="#A83232",
        fg="white",
        font=("Arial", 12),
        command=lambda: create_task(task_name_entry.get(), task_desc_entry.get("1.0", "end").strip(), popup),
    )
    create_button.pack(side="right", padx=(0, 10))
    cancel_button = tk.Button(
        button_frame,
        text="Cancel",
        bg="#FFFFFF",
        fg="black",
        font=("Arial", 12),
        command=popup.destroy,
    )
    cancel_button.pack(side="right", padx=(0, 10))

def logout_app():
    app.destroy()
    import Login

def create_task(name, description, popup):
    if name.strip():
        tasks.append({"name": name.strip(), "description": description.strip(), "completed": False})
        popup.destroy()
        show_all_todos()
def center_popup(popup, width, height):
    app.update_idletasks()
    x = app.winfo_x() + (app.winfo_width() // 2) - (width // 2)
    y = app.winfo_y() + (app.winfo_height() // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")
def open_settings_popup():
    settings_popup = tk.Toplevel(app)
    settings_popup.title("Settings")
    settings_popup.geometry("600x400")
    settings_popup.configure(bg="#F5F5F5")
    center_popup(settings_popup, 600, 400)
    sidebar = tk.Frame(settings_popup, width=150, bg="#F5F5F5", relief="flat")
    sidebar.pack(side="left", fill="y")
    main_content = tk.Frame(settings_popup, bg="#FFFFFF", relief="flat")
    main_content.pack(side="right", fill="both", expand=True)
    def switch_content(option):
        for widget in main_content.winfo_children():
            widget.destroy()
        if option == "Profile":
            load_profile_content(main_content)
            highlight_button(profile_btn)
        elif option == "Security":
            load_security_content(main_content)
            highlight_button(security_btn)
        elif option == "Notifications":
            load_notifications_content(main_content)
            highlight_button(notifications_btn)
    def highlight_button(active_button):
        for btn in [profile_btn, security_btn, notifications_btn]:
            btn.configure(bg="#FFFFFF", fg="black")
        active_button.configure(bg="#A83232", fg="white")
    profile_btn = tk.Button(
        sidebar,
        text="Profile",
        bg="#A83232",  # Highlighted initially
        fg="white",
        font=("Arial", 12),
        relief="flat",
        anchor="w",
        command=lambda: switch_content("Profile"),
    )
    profile_btn.pack(fill="x", pady=10, padx=10)
    security_btn = tk.Button(
        sidebar,
        text="Security Settings",
        bg="#FFFFFF",
        fg="black",
        font=("Arial", 12),
        relief="flat",
        anchor="w",
        command=lambda: switch_content("Security"),
    )
    security_btn.pack(fill="x", pady=10, padx=10)
    notifications_btn = tk.Button(
        sidebar,
        text="Notification Settings",
        bg="#FFFFFF",
        fg="black",
        font=("Arial", 12),
        relief="flat",
        anchor="w",
        command=lambda: switch_content("Notifications"),
    )
    notifications_btn.pack(fill="x", pady=10, padx=10)
    load_profile_content(main_content)
def load_profile_content(frame):
    tk.Label(frame, text="Profile", font=("Arial", 16, "bold"), bg="#FFFFFF").pack(pady=10)
def load_security_content(frame):
    tk.Label(frame, text="Security Settings", font=("Arial", 16, "bold"), bg="#FFFFFF").pack(pady=10)
def load_notifications_content(frame):
    tk.Label(frame, text="Notification Settings", font=("Arial", 16, "bold"), bg="#FFFFFF").pack(pady=10)
app = tk.Tk()
app.title("Isko-list")
app.geometry("800x600")
app.configure(bg="#E5E5E5")
icon = tk.PhotoImage(file="logo.png")
app.iconphoto(True, icon)
sidebar = tk.Frame(app, width=250, bg="#F5F5F5", relief="flat")
sidebar.pack(side="left", fill="y")
buttons = [
    {"text": "Add Task", "command": add_task_popup},
    {"text": "All Tasks", "command": show_all_todos},
    {"text": "Completed Tasks", "command": show_completed_tasks},
    {"text": "Settings", "command": open_settings_popup},
]
for button in buttons:
    btn = tk.Button(
        sidebar,
        text=button["text"],
        bg="#FFFFFF",
        fg="black",
        font=("Arial", 12),
        relief="flat",
        activebackground="#D3D3D3",
        activeforeground="black",
        command=button["command"],
    )
    btn.pack(fill="x", pady=15, padx=20)
logout_button = tk.Button(
    sidebar,
    text="Log out",
    bg="#A83232",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    command=logout_app,
)
logout_button.pack(side="bottom", fill="x", pady=30, padx=20)
content_area = tk.Frame(app, bg="#E5E5E5", relief="flat")
content_area.pack(side="right", fill="both", expand=True)
tasks = []
app.mainloop()