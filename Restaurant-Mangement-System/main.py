import tkinter as tk
from tkinter import TOP, GROOVE, BOTTOM, RAISED, LEFT, Y, X, messagebox, RIGHT, ttk
from datetime import datetime
import mysql.connector


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Customer, Payment, ViewCustomers, Orders):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=10)
        button_frame.pack(side=LEFT, fill=Y)

        # Title
        f1 = tk.Frame(self, bg="grey", relief=GROOVE, borderwidth=10)
        f1.pack(side=TOP, fill=X)

        # Items
        center_frame = tk.Frame(self, bg='white', relief=GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=TOP, anchor="n", fill=X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=TOP, fill=X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=7)
        down_nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        row_labels = [
            ["Tea\n₹20", "Coffee\n₹20", "Pastry\n₹30"],
            ["Pizza\n₹50", "Burger\n₹40", "Pasta\n₹30"],
            ["Wrap\n₹30", "Macrons\n₹30", "Soup\n₹25"]
        ]
        table = []
        for row in range(3):
            row_label = []
            for col in range(3):
                label = row_labels[row][col]
                item_button = tk.Button(center_frame, text=label, font=('FixedSys', 30, 'bold'), relief=RAISED)
                item_button.grid(row=row, column=col, sticky="nsew", padx=20, pady=30)
                row_labels.append(item_button)
            table.append(row_labels)


class Customer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=7)
        down_nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        # Labels and Entry fields for customer information
        tk.Label(center_frame, text="Customer ID:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=0, column=0,
                                                                                                    padx=10, pady=5)
        tk.Label(center_frame, text="Customer Name:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=1, column=0,
                                                                                                      padx=10, pady=5)
        tk.Label(center_frame, text="Phone:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=2, column=0, padx=10,
                                                                                              pady=5)
        tk.Label(center_frame, text="Address:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=3, column=0,
                                                                                                padx=10, pady=5)

        self.customer_id_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.customer_name_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.phone_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.address_entry = tk.Entry(center_frame, width=20, borderwidth=7)

        self.customer_id_entry.grid(row=0, column=1, padx=10, pady=15)
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=15)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=15)
        self.address_entry.grid(row=3, column=1, padx=10, pady=15)

        save_button = tk.Button(center_frame, text="Submit Data", font=('FixedSys', 20, 'bold'),
                                command=self.save_customer)
        save_button.grid(row=4, columnspan=2, padx=10, pady=15)

    def save_customer(self):
        customer_id = self.customer_id_entry.get()
        customer_name = self.customer_name_entry.get()
        phone = self.phone_entry.get()
        customer_address = self.address_entry.get()

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()

            insert_query = "INSERT INTO customers (customer_id, customer_name, phone, customer_address) VALUES (%s, %s, %s, %s)"
            values = (customer_id, customer_name, phone, customer_address)

            cursor.execute(insert_query, values)
            conn.commit()

            cursor.close()
            conn.close()

            print("Customer information saved successfully!")

            self.customer_id_entry.delete(0, tk.END)
            self.customer_name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)

            tk.messagebox.showinfo("showinfo", "Inserted Successfully!")

        except Exception as e:
            print(f"Error: {e}")
            tk.messagebox.showerror("showerror", "Error!")


class Payment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=7)
        down_nav_frame.pack(side=BOTTOM, fill=X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)
        # Fields For Payment

        # Create and place labels and entry fields for Order ID, Payment ID, and Payment Amount in a grid
        self.payment_id_label = tk.Label(center_frame, text="Payment ID:", bg='white', font=('FixedSys', 20, 'bold'))
        self.payment_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.payment_id_entry = tk.Entry(center_frame, borderwidth=7)
        self.payment_id_entry.grid(row=0, column=1, padx=10, pady=15)

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT Order_ID FROM Orders")
            order_ids = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
        except Exception as e:
            print("Error occurred while fetching order IDs:", e)

        self.order_id_var = tk.StringVar()
        self.order_id_var.set(order_ids[0])

        self.order_id_label = tk.Label(center_frame, text="Order ID:", font=('FixedSys', 12))
        self.order_id_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.order_id_dropdown = tk.OptionMenu(center_frame, self.order_id_var, *order_ids)
        self.order_id_dropdown.config(width=10)
        self.order_id_dropdown.grid(row=1, column=1, padx=10, pady=5)

        def fetch_order_ids():
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()
                cursor.execute("SELECT Order_ID FROM Orders")
                order_ids = [row[0] for row in cursor.fetchall()]
                cursor.close()
                conn.close()

                # Update the dropdown options
                self.order_id_var.set(order_ids[0])
                menu = self.order_id_dropdown['menu']
                menu.delete(0, 'end')
                for id in order_ids:
                    menu.add_command(label=id, command=lambda value=id: self.order_id_var.set(value))

            except Exception as e:
                print("Error occurred while fetching customer IDs:", e)

        # Add a Fetch button
        fetch_button = tk.Button(center_frame, text="Fetch Customer IDs", font=('FixedSys', 12),
                                 command=fetch_order_ids)
        fetch_button.grid(row=1, column=2, padx=10, pady=5)

        self.payment_amount_label = tk.Label(center_frame, text="Payment Amount:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_amount_label.grid(row=2, column=0, padx=10, pady=5)

        self.payment_amount_entry = tk.Label(center_frame, text="", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # label and radio buttons for Payment Method in a grid
        self.payment_method_label = tk.Label(center_frame, text="Payment Method:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_method_label.grid(row=3, column=0, padx=10, pady=5)

        # variable to hold the selected payment method
        self.payment_method_var = tk.StringVar()

        card_radio = tk.Radiobutton(center_frame, text="Card", variable=self.payment_method_var, value="Card",
                                    bg='white', font=('FixedSys', 20, 'bold'))
        cash_radio = tk.Radiobutton(center_frame, text="Cash", variable=self.payment_method_var, value="Cash",
                                    bg='white', font=('FixedSys', 20, 'bold'))

        card_radio.grid(row=3, column=1, padx=10, pady=5)
        cash_radio.grid(row=4, column=1, padx=10, pady=5)

        # Create a payment button to process the payment
        self.payment_button = tk.Button(center_frame, text="Process Payment", bg='white', font=('FixedSys', 20, 'bold'),
                                        command=self.process_payment)
        self.payment_button.grid(row=5, columnspan=2, padx=10, pady=15)

    def show_confirmation_popup(self):
        tk.messagebox.showinfo("Confirmation", "Payment processed successfully!")

    def update_payment_amount(self, event):
        selected_order_id = self.order_id_var.get()

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )

            cursor = conn.cursor()

            cursor.execute("SELECT total_price FROM Orders WHERE Order_ID = %s", (selected_order_id,))
            total_amount = cursor.fetchone()[0]

            # Update the payment_amount label to include total price
            self.payment_amount_entry.config(text=f"Payment Amount: ₹{total_amount}")

        except Exception as e:
            print("Error occurred! ", e)
            tk.messagebox.showerror("showerror", "No such Order ID Exists")

    def process_payment(self):
        payment_id = self.payment_id_entry.get()
        order_id = self.order_id_var.get()
        payment_method = self.payment_method_var.get()

        # Insert payment data into the database
        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )

            cursor = conn.cursor()

            cursor.execute("SELECT total_price FROM Orders WHERE Order_ID = %s", (order_id,))
            total_amount = cursor.fetchone()[0]

            # Update the payment_amount label to include total price
            self.payment_amount_entry.config(text=f"Payment Amount: ₹{total_amount}")

            insert_query = "INSERT INTO payments (payment_id, order_id, payment_amount, payment_method) VALUES (%s, %s, %s, %s)"
            data = (payment_id, order_id, total_amount, payment_method)

            cursor.execute(insert_query, data)
            conn.commit()

            self.payment_id_entry.delete(0, tk.END)
            self.payment_method_var.set("")
            print("Successfully Added!")
            self.after(3000, self.show_confirmation_popup)

        except Exception as e:
            print("Error occurred! ", e)
            tk.messagebox.showerror("showerror", "No such Order ID Exists")

class ViewCustomers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="⚙️Settings", font=('FixedSys', 10, 'bold'), width=10, height=2,
                           relief=tk.GROOVE, borderwidth=5)
        setting.pack(side=tk.BOTTOM, padx=15, pady=80)

        b1 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b1.pack(side=tk.BOTTOM, padx=15, pady=20)

        b2 = tk.Button(button_frame, text="Customer", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b2.pack(side=tk.BOTTOM, padx=15, pady=20)

        b3 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=7)
        down_nav_frame.pack(side=BOTTOM, fill=X)

        # Create a Treeview widget
        tree = ttk.Treeview(center_frame, columns=(
            "Customer_ID", "Order_ID", "Order_date", "Total_Price", "Customer_Name", "Phone", "Customer_Address"),
                            show="headings")

        # Define column headings
        tree.heading("Customer_ID", text="Customer ID")
        tree.heading("Order_ID", text="Order ID")
        tree.heading("Order_date", text="Order Date")
        tree.heading("Total_Price", text="Total Price")
        tree.heading("Customer_Name", text="Customer Name")
        tree.heading("Phone", text="Phone")
        tree.heading("Customer_Address", text="Customer Address")

        tree.pack(expand=True, fill=tk.BOTH)

        # Define column widths
        tree.column("Customer_ID", width=80)
        tree.column("Order_ID", width=80)
        tree.column("Order_date", width=100)
        tree.column("Total_Price", width=80)
        tree.column("Customer_Name", width=120)
        tree.column("Phone", width=100)
        tree.column("Customer_Address", width=150)

        def fetch_data():
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT customers.Customer_ID,orders.Order_ID,orders.Order_date,orders.total_price,customers.Customer_Name,customers.Phone,customers.Customer_Address FROM orders INNER JOIN customers ON orders.Customer_ID = customers.Customer_ID")

                rows = cursor.fetchall()

                cursor.close()
                conn.close()

                return rows

            except Exception as e:
                print("Error!")

        def update_treeview():
            data = fetch_data()
            tree.delete(*tree.get_children())  # Clear existing data

            for row in data:
                tree.insert("", "end", values=row)

        fetch_button = tk.Button(down_nav_frame, text="Fetch", relief=tk.GROOVE, font=('FixedSys', 10, 'bold'),
                                 width=20, height=2, borderwidth=2, command=update_treeview)
        fetch_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        def delete_record():
            selected_item = tree.selection()
            if selected_item:
                row_data = tree.item(selected_item, "values")

                try:
                    conn = mysql.connector.connect(
                        user='root',
                        password='1234',
                        host='localhost',
                        database='ai_restaurant',
                        auth_plugin='mysql_native_password'
                    )
                    cursor = conn.cursor()

                    # Assuming Customer_ID and Order_ID uniquely identify the record
                    customer_id = row_data[0]
                    order_id = row_data[1]

                    # Delete from orders table
                    cursor.execute("DELETE FROM orders WHERE Customer_ID = %s AND Order_ID = %s",
                                   (customer_id, order_id))

                    # Delete from customers table
                    cursor.execute("DELETE FROM customers WHERE Customer_ID = %s", (customer_id,))

                    conn.commit()

                    cursor.close()
                    conn.close()

                    update_treeview()

                except Exception as e:
                    print("Error!")
                    print(f"{e}")

        delete_button = tk.Button(down_nav_frame, text="Delete", relief=tk.GROOVE, font=('FixedSys', 10, 'bold'),
                                  width=20, height=2, borderwidth=2, command=delete_record)
        delete_button.pack(side=tk.BOTTOM, padx=15, pady=10)


class Orders(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        item_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        price = [20,20,30,50,30,30,30,25]
        quantity_entries = []

        item_names = ["Tea-₹20", "Coffee-₹20", "Pastry-₹30","Pizza-₹50", "Burger-₹40", "Pasta-₹30", "Wrap-₹30", "Macrons-₹30", "Soup-₹25"]

        # List to store entry fields for quantities
        for i, item_names in enumerate(item_names):
            item_label = tk.Label(center_frame, text=f"{item_names}", font=('FixedSys', 12))
            item_label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
            item_labels.append(item_label)

            quantity_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            quantity_entries.append(quantity_entry)

        self.order_id_label = tk.Label(center_frame, text="Order ID:", font=('FixedSys', 12))
        self.order_id_label.grid(row=10, column=0, padx=10, pady=5, sticky='w')
        self.order_id_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=10)
        self.order_id_entry.grid(row=10, column=1, padx=10, pady=5)

        '''self.customer_id_label = tk.Label(center_frame, text="Customer ID:", font=('FixedSys', 12))
        self.customer_id_label.grid(row=11, column=0, padx=10, pady=5, sticky='w')
        self.customer_id_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=10)
        self.customer_id_entry.grid(row=11, column=1, padx=10, pady=5)'''

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT Customer_ID FROM Customers")
            customer_ids = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
        except Exception as e:
            print("Error occurred while fetching customer IDs:", e)

        self.customer_id_var = tk.StringVar()
        self.customer_id_var.set(customer_ids[0])

        self.customer_id_label = tk.Label(center_frame, text="Customer ID:", font=('FixedSys', 12))
        self.customer_id_label.grid(row=11, column=0, padx=10, pady=5, sticky='w')

        self.customer_id_dropdown = tk.OptionMenu(center_frame, self.customer_id_var, *customer_ids)
        self.customer_id_dropdown.config(width=10)
        self.customer_id_dropdown.grid(row=11, column=1, padx=10, pady=5)

        def fetch_customer_ids():
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()
                cursor.execute("SELECT Customer_ID FROM Customers")
                customer_ids = [row[0] for row in cursor.fetchall()]
                cursor.close()
                conn.close()

                # Update the dropdown options
                self.customer_id_var.set(customer_ids[0])
                menu = self.customer_id_dropdown['menu']
                menu.delete(0, 'end')
                for id in customer_ids:
                    menu.add_command(label=id, command=lambda value=id: self.customer_id_var.set(value))

            except Exception as e:
                print("Error occurred while fetching customer IDs:", e)

        # Add a Fetch button
        fetch_button = tk.Button(center_frame, text="Fetch Customer IDs", font=('FixedSys', 12),
                                 command=fetch_customer_ids)
        fetch_button.grid(row=11, column=2, padx=10, pady=5)

        self.order_date_label = tk.Label(center_frame, text="Order Date:", font=('FixedSys', 12))
        self.order_date_label.grid(row=12, column=0, padx=10, pady=5, sticky='w')

        order_date_value = tk.Label(center_frame, text="", font=('FixedSys', 12))
        order_date_value.grid(row=12, column=1, padx=10, pady=5)

        self.total_price_label = tk.Label(center_frame, text="Total Price:", font=('FixedSys', 12))
        self.total_price_label.grid(row=13, column=0, padx=10, pady=5, sticky='w')

        total_price_value = tk.Label(center_frame, text="", font=('FixedSys', 12))
        total_price_value.grid(row=13, column=1, padx=10, pady=5)

        # Step 6: Calculate Total Price
        def calculate_total_price():
            total_price = 0
            for i in range(9):
                quantity_str = quantity_entries[i].get()
                if quantity_str and quantity_str.isdigit():
                    quantity = int(quantity_str)
                    total_price += quantity * price[i]

            total_price_value.config(text=f"Total Price: ₹{total_price}")
            order_date_value.config(text=f"Today: {datetime.now()}")

        # Step 7: Save Order to Database
        def save_order_to_database():
            order_id = int(self.order_id_entry.get())
            customer_id = int(self.customer_id_var.get())
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_price_str = total_price_value.cget("text")[13:]
            total_price = float(total_price_str.replace('₹', ''))

            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()

                insert_query = "INSERT INTO Orders(order_id,customer_id,order_date,total_price) VALUES (%s, %s, %s, %s)"
                data = (order_id, customer_id, order_date, total_price)

                cursor.execute(insert_query, data)
                conn.commit()

            except Exception as e:
                print("Error occurred! ", e)
                tk.messagebox.showerror("showerror", "No such Customer ID Exists")

        def submit_order():
            calculate_total_price()
            save_order_to_database()
            tk.messagebox.showinfo("showinfo", "Inserted Successfully!")

        submit_button = tk.Button(center_frame, text="Submit Order", font=('FixedSys', 12), command=submit_order)
        submit_button.grid(row=14, column=0, columnspan=2, pady=10)

# Create an instance of TkinterApp and run the application
app = TkinterApp()
app.mainloop()import tkinter as tk
from tkinter import TOP, GROOVE, BOTTOM, RAISED, LEFT, Y, X, messagebox, RIGHT, ttk
from datetime import datetime
import mysql.connector


class TkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Customer, Payment, ViewCustomers, Orders):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=10)
        button_frame.pack(side=LEFT, fill=Y)

        # Title
        f1 = tk.Frame(self, bg="grey", relief=GROOVE, borderwidth=10)
        f1.pack(side=TOP, fill=X)

        # Items
        center_frame = tk.Frame(self, bg='white', relief=GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=TOP, anchor="n", fill=X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=TOP, fill=X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=7)
        down_nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        row_labels = [
            ["Tea\n₹20", "Coffee\n₹20", "Pastry\n₹30"],
            ["Pizza\n₹50", "Burger\n₹40", "Pasta\n₹30"],
            ["Wrap\n₹30", "Macrons\n₹30", "Soup\n₹25"]
        ]
        table = []
        for row in range(3):
            row_label = []
            for col in range(3):
                label = row_labels[row][col]
                item_button = tk.Button(center_frame, text=label, font=('FixedSys', 30, 'bold'), relief=RAISED)
                item_button.grid(row=row, column=col, sticky="nsew", padx=20, pady=30)
                row_labels.append(item_button)
            table.append(row_labels)


class Customer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=7)
        down_nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        # Labels and Entry fields for customer information
        tk.Label(center_frame, text="Customer ID:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=0, column=0,
                                                                                                    padx=10, pady=5)
        tk.Label(center_frame, text="Customer Name:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=1, column=0,
                                                                                                      padx=10, pady=5)
        tk.Label(center_frame, text="Phone:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=2, column=0, padx=10,
                                                                                              pady=5)
        tk.Label(center_frame, text="Address:", bg='white', font=('FixedSys', 20, 'bold')).grid(row=3, column=0,
                                                                                                padx=10, pady=5)

        self.customer_id_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.customer_name_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.phone_entry = tk.Entry(center_frame, width=20, borderwidth=7)
        self.address_entry = tk.Entry(center_frame, width=20, borderwidth=7)

        self.customer_id_entry.grid(row=0, column=1, padx=10, pady=15)
        self.customer_name_entry.grid(row=1, column=1, padx=10, pady=15)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=15)
        self.address_entry.grid(row=3, column=1, padx=10, pady=15)

        save_button = tk.Button(center_frame, text="Submit Data", font=('FixedSys', 20, 'bold'),
                                command=self.save_customer)
        save_button.grid(row=4, columnspan=2, padx=10, pady=15)

    def save_customer(self):
        customer_id = self.customer_id_entry.get()
        customer_name = self.customer_name_entry.get()
        phone = self.phone_entry.get()
        customer_address = self.address_entry.get()

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()

            insert_query = "INSERT INTO customers (customer_id, customer_name, phone, customer_address) VALUES (%s, %s, %s, %s)"
            values = (customer_id, customer_name, phone, customer_address)

            cursor.execute(insert_query, values)
            conn.commit()

            cursor.close()
            conn.close()

            print("Customer information saved successfully!")

            self.customer_id_entry.delete(0, tk.END)
            self.customer_name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)

            tk.messagebox.showinfo("showinfo", "Inserted Successfully!")

        except Exception as e:
            print(f"Error: {e}")
            tk.messagebox.showerror("showerror", "Error!")


class Payment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=7)
        down_nav_frame.pack(side=BOTTOM, fill=X)

        view_button = tk.Button(down_nav_frame, text="View Customers", font=('FixedSys', 10, 'bold'),
                                command=lambda: controller.show_frame(ViewCustomers), width=20, height=2,
                                relief=tk.GROOVE, borderwidth=5)
        view_button.pack(side=tk.BOTTOM, padx=15, pady=10)
        # Fields For Payment

        # Create and place labels and entry fields for Order ID, Payment ID, and Payment Amount in a grid
        self.payment_id_label = tk.Label(center_frame, text="Payment ID:", bg='white', font=('FixedSys', 20, 'bold'))
        self.payment_id_label.grid(row=0, column=0, padx=10, pady=5)

        self.payment_id_entry = tk.Entry(center_frame, borderwidth=7)
        self.payment_id_entry.grid(row=0, column=1, padx=10, pady=15)

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT Order_ID FROM Orders")
            order_ids = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
        except Exception as e:
            print("Error occurred while fetching order IDs:", e)

        self.order_id_var = tk.StringVar()
        self.order_id_var.set(order_ids[0])

        self.order_id_label = tk.Label(center_frame, text="Order ID:", font=('FixedSys', 12))
        self.order_id_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        self.order_id_dropdown = tk.OptionMenu(center_frame, self.order_id_var, *order_ids)
        self.order_id_dropdown.config(width=10)
        self.order_id_dropdown.grid(row=1, column=1, padx=10, pady=5)

        def fetch_order_ids():
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()
                cursor.execute("SELECT Order_ID FROM Orders")
                order_ids = [row[0] for row in cursor.fetchall()]
                cursor.close()
                conn.close()

                # Update the dropdown options
                self.order_id_var.set(order_ids[0])
                menu = self.order_id_dropdown['menu']
                menu.delete(0, 'end')
                for id in order_ids:
                    menu.add_command(label=id, command=lambda value=id: self.order_id_var.set(value))

            except Exception as e:
                print("Error occurred while fetching customer IDs:", e)

        # Add a Fetch button
        fetch_button = tk.Button(center_frame, text="Fetch Customer IDs", font=('FixedSys', 12),
                                 command=fetch_order_ids)
        fetch_button.grid(row=1, column=2, padx=10, pady=5)

        self.payment_amount_label = tk.Label(center_frame, text="Payment Amount:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_amount_label.grid(row=2, column=0, padx=10, pady=5)

        self.payment_amount_entry = tk.Label(center_frame, text="", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_amount_entry.grid(row=2, column=1, padx=10, pady=5)

        # label and radio buttons for Payment Method in a grid
        self.payment_method_label = tk.Label(center_frame, text="Payment Method:", bg='white',
                                             font=('FixedSys', 20, 'bold'))
        self.payment_method_label.grid(row=3, column=0, padx=10, pady=5)

        # variable to hold the selected payment method
        self.payment_method_var = tk.StringVar()

        card_radio = tk.Radiobutton(center_frame, text="Card", variable=self.payment_method_var, value="Card",
                                    bg='white', font=('FixedSys', 20, 'bold'))
        cash_radio = tk.Radiobutton(center_frame, text="Cash", variable=self.payment_method_var, value="Cash",
                                    bg='white', font=('FixedSys', 20, 'bold'))

        card_radio.grid(row=3, column=1, padx=10, pady=5)
        cash_radio.grid(row=4, column=1, padx=10, pady=5)

        # Create a payment button to process the payment
        self.payment_button = tk.Button(center_frame, text="Process Payment", bg='white', font=('FixedSys', 20, 'bold'),
                                        command=self.process_payment)
        self.payment_button.grid(row=5, columnspan=2, padx=10, pady=15)

    def show_confirmation_popup(self):
        tk.messagebox.showinfo("Confirmation", "Payment processed successfully!")

    def update_payment_amount(self, event):
        selected_order_id = self.order_id_var.get()

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )

            cursor = conn.cursor()

            cursor.execute("SELECT total_price FROM Orders WHERE Order_ID = %s", (selected_order_id,))
            total_amount = cursor.fetchone()[0]

            # Update the payment_amount label to include total price
            self.payment_amount_entry.config(text=f"Payment Amount: ₹{total_amount}")

        except Exception as e:
            print("Error occurred! ", e)
            tk.messagebox.showerror("showerror", "No such Order ID Exists")

    def process_payment(self):
        payment_id = self.payment_id_entry.get()
        order_id = self.order_id_var.get()
        payment_method = self.payment_method_var.get()

        # Insert payment data into the database
        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )

            cursor = conn.cursor()

            cursor.execute("SELECT total_price FROM Orders WHERE Order_ID = %s", (order_id,))
            total_amount = cursor.fetchone()[0]

            # Update the payment_amount label to include total price
            self.payment_amount_entry.config(text=f"Payment Amount: ₹{total_amount}")

            insert_query = "INSERT INTO payments (payment_id, order_id, payment_amount, payment_method) VALUES (%s, %s, %s, %s)"
            data = (payment_id, order_id, total_amount, payment_method)

            cursor.execute(insert_query, data)
            conn.commit()

            self.payment_id_entry.delete(0, tk.END)
            self.payment_method_var.set("")
            print("Successfully Added!")
            self.after(3000, self.show_confirmation_popup)

        except Exception as e:
            print("Error occurred! ", e)
            tk.messagebox.showerror("showerror", "No such Order ID Exists")

class ViewCustomers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="⚙️Settings", font=('FixedSys', 10, 'bold'), width=10, height=2,
                           relief=tk.GROOVE, borderwidth=5)
        setting.pack(side=tk.BOTTOM, padx=15, pady=80)

        b1 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b1.pack(side=tk.BOTTOM, padx=15, pady=20)

        b2 = tk.Button(button_frame, text="Customer", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b2.pack(side=tk.BOTTOM, padx=15, pady=20)

        b3 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b3.pack(side=tk.BOTTOM, padx=15, pady=20)

        b4 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=tk.GROOVE, borderwidth=5)
        b4.pack(side=tk.BOTTOM, padx=15, pady=20)

        down_nav_frame = tk.Frame(self, bg='grey', relief=GROOVE, borderwidth=7)
        down_nav_frame.pack(side=BOTTOM, fill=X)

        # Create a Treeview widget
        tree = ttk.Treeview(center_frame, columns=(
            "Customer_ID", "Order_ID", "Order_date", "Total_Price", "Customer_Name", "Phone", "Customer_Address"),
                            show="headings")

        # Define column headings
        tree.heading("Customer_ID", text="Customer ID")
        tree.heading("Order_ID", text="Order ID")
        tree.heading("Order_date", text="Order Date")
        tree.heading("Total_Price", text="Total Price")
        tree.heading("Customer_Name", text="Customer Name")
        tree.heading("Phone", text="Phone")
        tree.heading("Customer_Address", text="Customer Address")

        tree.pack(expand=True, fill=tk.BOTH)

        # Define column widths
        tree.column("Customer_ID", width=80)
        tree.column("Order_ID", width=80)
        tree.column("Order_date", width=100)
        tree.column("Total_Price", width=80)
        tree.column("Customer_Name", width=120)
        tree.column("Phone", width=100)
        tree.column("Customer_Address", width=150)

        def fetch_data():
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT customers.Customer_ID,orders.Order_ID,orders.Order_date,orders.total_price,customers.Customer_Name,customers.Phone,customers.Customer_Address FROM orders INNER JOIN customers ON orders.Customer_ID = customers.Customer_ID")

                rows = cursor.fetchall()

                cursor.close()
                conn.close()

                return rows

            except Exception as e:
                print("Error!")

        def update_treeview():
            data = fetch_data()
            tree.delete(*tree.get_children())  # Clear existing data

            for row in data:
                tree.insert("", "end", values=row)

        fetch_button = tk.Button(down_nav_frame, text="Fetch", relief=tk.GROOVE, font=('FixedSys', 10, 'bold'),
                                 width=20, height=2, borderwidth=2, command=update_treeview)
        fetch_button.pack(side=tk.BOTTOM, padx=15, pady=10)

        def delete_record():
            selected_item = tree.selection()
            if selected_item:
                row_data = tree.item(selected_item, "values")

                try:
                    conn = mysql.connector.connect(
                        user='root',
                        password='1234',
                        host='localhost',
                        database='ai_restaurant',
                        auth_plugin='mysql_native_password'
                    )
                    cursor = conn.cursor()

                    # Assuming Customer_ID and Order_ID uniquely identify the record
                    customer_id = row_data[0]
                    order_id = row_data[1]

                    # Delete from orders table
                    cursor.execute("DELETE FROM orders WHERE Customer_ID = %s AND Order_ID = %s",
                                   (customer_id, order_id))

                    # Delete from customers table
                    cursor.execute("DELETE FROM customers WHERE Customer_ID = %s", (customer_id,))

                    conn.commit()

                    cursor.close()
                    conn.close()

                    update_treeview()

                except Exception as e:
                    print("Error!")
                    print(f"{e}")

        delete_button = tk.Button(down_nav_frame, text="Delete", relief=tk.GROOVE, font=('FixedSys', 10, 'bold'),
                                  width=20, height=2, borderwidth=2, command=delete_record)
        delete_button.pack(side=tk.BOTTOM, padx=15, pady=10)


class Orders(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_frame = tk.Frame(self, bg='grey', relief=tk.GROOVE, borderwidth=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        f1 = tk.Frame(self, bg="grey", relief=tk.GROOVE, borderwidth=10)
        f1.pack(side=tk.TOP, fill=tk.X)

        center_frame = tk.Frame(self, bg='white', relief=tk.GROOVE, borderwidth=5, width=1000, height=1000)
        center_frame.pack(padx=30, pady=30)

        lbl1 = tk.Label(f1, text="AI RESTAURANT", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), pady=10)
        lbl1.pack(side=tk.TOP, anchor="n", fill=tk.X)

        lbl2 = tk.Label(button_frame, text="🔎Menu", bg='grey', fg='white', font=('FixedSys', 20, 'bold'), padx=10)
        lbl2.pack(side=tk.TOP, fill=tk.X)

        setting = tk.Label(button_frame, text="AI", font=('FixedSys', 20, 'bold'), width=10, height=2,
                           relief=GROOVE, borderwidth=5)
        setting.pack(side=BOTTOM, padx=15, pady=80)
        b1 = tk.Button(button_frame, text="Payment", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Payment), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b1.pack(side=BOTTOM, padx=15, pady=20)
        b2 = tk.Button(button_frame, text="Orders", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Orders), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b2.pack(side=BOTTOM, padx=15, pady=20)
        b3 = tk.Button(button_frame, text="Customers", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(Customer), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b3.pack(side=BOTTOM, padx=15, pady=20)
        b4 = tk.Button(button_frame, text="Items", font=('FixedSys', 10, 'bold'),
                       command=lambda: controller.show_frame(StartPage), width=10, height=2,
                       relief=GROOVE, borderwidth=5)
        b4.pack(side=BOTTOM, padx=15, pady=20)

        item_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        price = [20,20,30,50,30,30,30,25]
        quantity_entries = []

        item_names = ["Tea-₹20", "Coffee-₹20", "Pastry-₹30","Pizza-₹50", "Burger-₹40", "Pasta-₹30", "Wrap-₹30", "Macrons-₹30", "Soup-₹25"]

        # List to store entry fields for quantities
        for i, item_names in enumerate(item_names):
            item_label = tk.Label(center_frame, text=f"{item_names}", font=('FixedSys', 12))
            item_label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
            item_labels.append(item_label)

            quantity_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            quantity_entries.append(quantity_entry)

        self.order_id_label = tk.Label(center_frame, text="Order ID:", font=('FixedSys', 12))
        self.order_id_label.grid(row=10, column=0, padx=10, pady=5, sticky='w')
        self.order_id_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=10)
        self.order_id_entry.grid(row=10, column=1, padx=10, pady=5)

        '''self.customer_id_label = tk.Label(center_frame, text="Customer ID:", font=('FixedSys', 12))
        self.customer_id_label.grid(row=11, column=0, padx=10, pady=5, sticky='w')
        self.customer_id_entry = tk.Entry(center_frame, font=('FixedSys', 12), width=10)
        self.customer_id_entry.grid(row=11, column=1, padx=10, pady=5)'''

        try:
            conn = mysql.connector.connect(
                user='root',
                password='1234',
                host='localhost',
                database='ai_restaurant',
                auth_plugin='mysql_native_password'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT Customer_ID FROM Customers")
            customer_ids = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
        except Exception as e:
            print("Error occurred while fetching customer IDs:", e)

        self.customer_id_var = tk.StringVar()
        self.customer_id_var.set(customer_ids[0])

        self.customer_id_label = tk.Label(center_frame, text="Customer ID:", font=('FixedSys', 12))
        self.customer_id_label.grid(row=11, column=0, padx=10, pady=5, sticky='w')

        self.customer_id_dropdown = tk.OptionMenu(center_frame, self.customer_id_var, *customer_ids)
        self.customer_id_dropdown.config(width=10)
        self.customer_id_dropdown.grid(row=11, column=1, padx=10, pady=5)

        def fetch_customer_ids():
            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()
                cursor.execute("SELECT Customer_ID FROM Customers")
                customer_ids = [row[0] for row in cursor.fetchall()]
                cursor.close()
                conn.close()

                # Update the dropdown options
                self.customer_id_var.set(customer_ids[0])
                menu = self.customer_id_dropdown['menu']
                menu.delete(0, 'end')
                for id in customer_ids:
                    menu.add_command(label=id, command=lambda value=id: self.customer_id_var.set(value))

            except Exception as e:
                print("Error occurred while fetching customer IDs:", e)

        # Add a Fetch button
        fetch_button = tk.Button(center_frame, text="Fetch Customer IDs", font=('FixedSys', 12),
                                 command=fetch_customer_ids)
        fetch_button.grid(row=11, column=2, padx=10, pady=5)

        self.order_date_label = tk.Label(center_frame, text="Order Date:", font=('FixedSys', 12))
        self.order_date_label.grid(row=12, column=0, padx=10, pady=5, sticky='w')

        order_date_value = tk.Label(center_frame, text="", font=('FixedSys', 12))
        order_date_value.grid(row=12, column=1, padx=10, pady=5)

        self.total_price_label = tk.Label(center_frame, text="Total Price:", font=('FixedSys', 12))
        self.total_price_label.grid(row=13, column=0, padx=10, pady=5, sticky='w')

        total_price_value = tk.Label(center_frame, text="", font=('FixedSys', 12))
        total_price_value.grid(row=13, column=1, padx=10, pady=5)

        # Step 6: Calculate Total Price
        def calculate_total_price():
            total_price = 0
            for i in range(9):
                quantity_str = quantity_entries[i].get()
                if quantity_str and quantity_str.isdigit():
                    quantity = int(quantity_str)
                    total_price += quantity * price[i]

            total_price_value.config(text=f"Total Price: ₹{total_price}")
            order_date_value.config(text=f"Today: {datetime.now()}")

        # Step 7: Save Order to Database
        def save_order_to_database():
            order_id = int(self.order_id_entry.get())
            customer_id = int(self.customer_id_var.get())
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_price_str = total_price_value.cget("text")[13:]
            total_price = float(total_price_str.replace('₹', ''))

            try:
                conn = mysql.connector.connect(
                    user='root',
                    password='1234',
                    host='localhost',
                    database='ai_restaurant',
                    auth_plugin='mysql_native_password'
                )
                cursor = conn.cursor()

                insert_query = "INSERT INTO Orders(order_id,customer_id,order_date,total_price) VALUES (%s, %s, %s, %s)"
                data = (order_id, customer_id, order_date, total_price)

                cursor.execute(insert_query, data)
                conn.commit()

            except Exception as e:
                print("Error occurred! ", e)
                tk.messagebox.showerror("showerror", "No such Customer ID Exists")

        def submit_order():
            calculate_total_price()
            save_order_to_database()
            tk.messagebox.showinfo("showinfo", "Inserted Successfully!")

        submit_button = tk.Button(center_frame, text="Submit Order", font=('FixedSys', 12), command=submit_order)
        submit_button.grid(row=14, column=0, columnspan=2, pady=10)

# Create an instance of TkinterApp and run the application
app = TkinterApp()
app.mainloop()