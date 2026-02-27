import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import get_connection   

#  MAIN WINDOW SETUP
root = tk.Tk()
root.title("Horse Racing Database System")
root.geometry("600x600")


#  LOGIN SCREEN
def open_admin_panel():
    login_frame.pack_forget()
    admin_panel()

def open_guest_panel():
    login_frame.pack_forget()
    guest_panel()

login_frame = tk.Frame(root)
login_frame.pack(pady=100)

tk.Label(login_frame, text="Welcome to Horse Racing Database", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(login_frame, text="Admin", width=20, command=open_admin_panel).pack(pady=5)
tk.Button(login_frame, text="Guest", width=20, command=open_guest_panel).pack(pady=5)


#  ADMIN PANEL
def admin_panel():
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Admin Panel", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Add Race and Results
    def add_race():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.callproc("add_new_race_with_results", (
                race_id.get(), race_name.get(), track_name.get(),
                race_date.get(), race_time.get(), horse_id.get(),
                result.get(), prize.get()
            ))
            conn.commit()
            messagebox.showinfo("Success", "Race added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn:
                conn.close()

    tk.Label(frame, text="Race ID:").grid(row=1, column=0)
    race_id = tk.Entry(frame); race_id.grid(row=1, column=1)
    tk.Label(frame, text="Race Name:").grid(row=2, column=0)
    race_name = tk.Entry(frame); race_name.grid(row=2, column=1)
    tk.Label(frame, text="Track Name:").grid(row=3, column=0)
    track_name = tk.Entry(frame); track_name.grid(row=3, column=1)
    tk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=4, column=0)
    race_date = tk.Entry(frame); race_date.grid(row=4, column=1)
    tk.Label(frame, text="Time (HH:MM):").grid(row=5, column=0)
    race_time = tk.Entry(frame); race_time.grid(row=5, column=1)
    tk.Label(frame, text="Horse ID:").grid(row=6, column=0)
    horse_id = tk.Entry(frame); horse_id.grid(row=6, column=1)
    tk.Label(frame, text="Result:").grid(row=7, column=0)
    result = tk.Entry(frame); result.grid(row=7, column=1)
    tk.Label(frame, text="Prize:").grid(row=8, column=0)
    prize = tk.Entry(frame); prize.grid(row=8, column=1)
    tk.Button(frame, text="Add Race", command=add_race, bg="#4CAF50", fg="white").grid(row=9, column=0, columnspan=2, pady=10)


    # Delete Owner and Related Info
    def delete_owner():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.callproc("delete_owner", (owner_id_del.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Owner and related info deleted!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn:
                conn.close()

    tk.Label(frame, text="Owner ID:").grid(row=10, column=0, pady=(20, 0))
    owner_id_del = tk.Entry(frame); owner_id_del.grid(row=10, column=1, pady=(20, 0))
    tk.Button(frame, text="Delete Owner", command=delete_owner, bg="#f44336", fg="white").grid(row=11, column=0, columnspan=2, pady=5)


    # Move Horse to Another Stable
    def move_horse():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.callproc("move_horse", (horse_id_move.get(), new_stable_id.get()))
            conn.commit()
            messagebox.showinfo("Success", "Horse moved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn:
                conn.close()

    tk.Label(frame, text="Horse ID:").grid(row=12, column=0, pady=(20, 0))
    horse_id_move = tk.Entry(frame); horse_id_move.grid(row=12, column=1, pady=(20, 0))
    tk.Label(frame, text="New Stable ID:").grid(row=13, column=0)
    new_stable_id = tk.Entry(frame); new_stable_id.grid(row=13, column=1)
    tk.Button(frame, text="Move Horse", command=move_horse, bg="#2196F3", fg="white").grid(row=14, column=0, columnspan=2, pady=5)


    # Approve New Trainer
    def approve_trainer():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.callproc("approve_new_trainer", (
                trainer_id.get(), trainer_lname.get(), trainer_fname.get(), trainer_stable_id.get()
            ))
            conn.commit()
            messagebox.showinfo("Success", "Trainer approved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn:
                conn.close()

    tk.Label(frame, text="Trainer ID:").grid(row=15, column=0, pady=(20, 0))
    trainer_id = tk.Entry(frame); trainer_id.grid(row=15, column=1, pady=(20, 0))
    tk.Label(frame, text="Last Name:").grid(row=16, column=0)
    trainer_lname = tk.Entry(frame); trainer_lname.grid(row=16, column=1)
    tk.Label(frame, text="First Name:").grid(row=17, column=0)
    trainer_fname = tk.Entry(frame); trainer_fname.grid(row=17, column=1)
    tk.Label(frame, text="Stable ID:").grid(row=18, column=0)
    trainer_stable_id = tk.Entry(frame); trainer_stable_id.grid(row=18, column=1)
    tk.Button(frame, text="Approve Trainer", command=approve_trainer, bg="#9C27B0", fg="white").grid(row=19, column=0, columnspan=2, pady=10)


#  GUEST PANEL
def guest_panel():
    # Clear window
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Title
    tk.Label(frame, text="Guest Panel", font=("Arial", 14, "bold")).pack(pady=10)

    # --- Input for owner's last name ---
    owner_input_frame = tk.Frame(frame)
    owner_input_frame.pack(pady=5)
    tk.Label(owner_input_frame, text="Enter Owner Last Name:").pack(side=tk.LEFT, padx=5)
    owner_lastname = tk.Entry(owner_input_frame, width=20)
    owner_lastname.pack(side=tk.LEFT, padx=5)

    # --- Output box ---
    output = tk.Text(frame, width=70, height=15)
    output.pack(pady=5)

    # --- Helper function to run a query ---
    def run_query(query):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            output.delete(1.0, tk.END)
            if not rows:
                output.insert(tk.END, "No results found.\n")
            else:
                for row in rows:
                    output.insert(tk.END, str(row) + "\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if conn:
                conn.close()

    # --- Search Horses by Owner ---
    def search_horses_by_owner():
        last_name = owner_lastname.get().strip()
        if not last_name:
            messagebox.showwarning("Input Required", "Please enter the owner's last name.")
            return
        query = f"SELECT * FROM horses_by_owner WHERE OwnerLastName = '{last_name}'"
        run_query(query)

    tk.Button(frame, text="Show Horses by Owner", width=25, bg="#607D8B", fg="white",
              command=search_horses_by_owner).pack(pady=3)

    # --- Other three buttons ---
    tk.Button(frame, text="Show Winning Trainers", width=25,
              command=lambda: run_query("SELECT * FROM winning_trainers")).pack(pady=3)

    tk.Button(frame, text="Show Trainer Winnings", width=25,
              command=lambda: run_query("SELECT * FROM trainer_total_winnings")).pack(pady=3)

    tk.Button(frame, text="Show Tracks Summary", width=25,
              command=lambda: run_query("SELECT * FROM track_stats")).pack(pady=3)

# start the app
root.mainloop()
