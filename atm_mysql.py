################## IMPORTED MODULES #################################
from tkinter import *
from tkinter import messagebox
import  tkinter.messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
from tkinter import ttk 
import os
from PIL import Image,ImageTk
import time
import random
import pyodbc
############################################################ BANKING SCREEN USING CLASS ############################################################

################## CURRENT BALANCE #################################


current_balance=0.00

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ################## INITIALIZING PAGES IN CONTAINER #################################
        for F in (StartPage, MenuPage, WithdrawPage,DepositPage,BalancePage,InfoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

################## START PAGE #################################
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('BANCO AMIGOS')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='abc.png'))

        heading=tk.Label(self,text='PayRealX',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#3d3d5c').pack()

        password_label=tk.Label(self,text=(f'BIENVENIDO {user_display_name} A BANCO AMIGOS'),font=('BatmanForeverAlternate',17),bg='#3d3d5c',fg='white').pack(pady=10)

        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='Enter',font=('orbitron',12),command=next_page,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Salir','Seguro que deseas salir?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='Quit',font=('orbitron',12),command=popup,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)


        dualtone_label=tk.Label(self, text='',font=('orbitron',13),fg='white',bg='#33334d',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response=messagebox.askyesno('Salir','Quieres usar otra cuenta?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Usar otra cuenta',font=('orbitron',12),command=popup2,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

        ################## BOTTOM FRAME #################################
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3).pack(fill='x',side='bottom')

        visa_photo= tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        mastercard_photo= tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        american_express_photo= tk.PhotoImage(file='american_express.png')
        american_express_label=tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image=american_express_photo

        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()


################## MENU PAGE #################################
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Main Menu',font=('orbitron',13),fg='white',bg='#3d3d5c')
        main_menu_label.pack(pady=5)
        slection_label=tk.Label(self,text='Selecciona una opci??n',font=('orbitron',13),fg='white',bg='#3d3d5c')
        slection_label.pack(fill='x',pady=5)

        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='RETIRO',font=('orbitron',13),command=withdraw,relief='raised',borderwidth=3,width=30,height=4)
        withdraw_button.grid(row=0,column=0,pady=7)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='DEPOSITO',font=('orbitron',13),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.grid(row=1,column=0,pady=5)
        def balance():
            controller.show_frame('BalancePage')

        balance_button=tk.Button(button_frame,text='SALDO',font=('orbitron',13),command=balance,relief='raised',borderwidth=3,width=30,height=4)
        balance_button.grid(row=0,column=1,pady=7,padx=794)

        def info():
            controller.show_frame('InfoPage')

        info_button=tk.Button(button_frame,text='INFO DE USUARIO',font=('orbitron',13),command=info,relief='raised',borderwidth=3,width=30,height=4)
        info_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')


        exit_button=tk.Button(button_frame,text='SALIR',font=('orbitron',13),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.grid(row=1,column=1,pady=5)

################## WITHDRAW PAGE #################################
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='ELIGE LA CANTIDAD A RETIRAR',font=('orbitron',13),fg='white',bg='#3d3d5c')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global current_balance
            if amount>current_balance:
                messagebox.showwarning('WARNING','SALDO INSUFICIENTE!')
                other_amount_entry.delete(0,END)
            else:

                current_balance -= amount
                messagebox.showinfo('RETIRO','EXITOSO!')
                other_amount_entry.delete(0,END)
                controller.shared_data['Balance'].set(current_balance)
                ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
                mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                mycursor=mydb.cursor()
                mycursor.execute("use Gangrena")
                mycursor.execute(f"update payrealbank set balance ={current_balance} where accid = {username1} ")
                mydb.commit()

                controller.show_frame('MenuPage')



        twenty_button=tk.Button(button_frame,text='$20',font=('orbitron',12),command=lambda:withdraw(20),relief='raised',borderwidth=3,width=30,height=4)
        twenty_button.grid(row=0,column=0,pady=5)

        fourty_button=tk.Button(button_frame,text='$40',font=('orbitron',12),command=lambda:withdraw(40),relief='raised',borderwidth=3,width=30,height=4)
        fourty_button.grid(row=1,column=0,pady=5)

        sixty_button=tk.Button(button_frame,text='$60',font=('orbitron',12),command=lambda:withdraw(60),relief='raised',borderwidth=3,width=30,height=4)
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button=tk.Button(button_frame,text='$80',font=('orbitron',12),command=lambda:withdraw(80),relief='raised',borderwidth=3,width=30,height=4)
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button=tk.Button(button_frame,text='$100',font=('orbitron',12),command=lambda:withdraw(100),relief='raised',borderwidth=3,width=30,height=4)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=794)

        two_hundred_button=tk.Button(button_frame,text='$200',font=('orbitron',12),command=lambda:withdraw(200),relief='raised',borderwidth=3,width=30,height=4)
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button=tk.Button(button_frame,text='$300',font=('orbitron',12),command=lambda:withdraw(300),relief='raised',borderwidth=3,width=30,height=4)
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('orbitron',12),textvariable=cash,width=28,justify='right')
        other_amount_entry.grid(row=3,column=1,pady=4,ipady=30)

        other_amount_heading=tk.Button(button_frame,text='OTRA CANTIDAD',font=('orbitron',13),borderwidth=0,relief='sunken',activeforeground='white',activebackground='#33334d',bg='#33334d',fg='white')
        other_amount_heading.grid(row=4,column=1)

        def other_amount(_):
            global current_balance
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('ATENCI??N','SALDO INSUFICIENTE!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('ANTENCI??N','INGRESA UNA CANTIDAD CORRECTA!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('RETIRO','EXITOSO!')
                    controller.show_frame('MenuPage')
                    ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update payrealbank set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('orbitron',13),relief=RIDGE,borderwidth=3,width=23,height=4)
        exit_button.grid(row=4,column=0)
################## DEPOSIT PAGE #################################
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Cajero Banco Amigos',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#3d3d5c').pack()

        enter_amount_label=tk.Label(self,text='INGRESA LA CANTIDAD A DEPOSITAR',font=('orbitron',13),bg='#3d3d5c',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('orbitron',12),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('Alerta','Ingresa una cantidad correcta!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    messagebox.showinfo('DEPOSITO','Deposito exitoso!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('MenuPage')
                    cash.set('')
                    ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
                    mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                    mycursor=mydb.cursor()
                    mycursor.execute("use Gangrena")
                    mycursor.execute(f"update payrealbank set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')


        enter_button=tk.Button(self,text='Enter',font=('orbitron',13),command=deposit_cash,relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#33334d')
        two_tone_label.pack(fill='both',expand=True)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(self,text='REGRESAR AL MENU',font=('orbitron',13),command=exit,relief='raised',borderwidth=3,width=23,height=3)
        exit_button.pack(pady=10)
        

################## BALANCE PAGE #################################
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='Cajero Banco Amigos',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, text='Balance', font=('orbitron',13),fg='white', bg='#3d3d5c', anchor='w')
        balance_label.pack()

        upperframe=tk.Frame(self,bg='#33334d')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('orbitron',16),fg='white', bg='#33334d', anchor='w')
        balance_label.pack(pady=7)

        button_frame=tk.Label(self,bg='#33334d')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Salir',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=5)

    def on_balance_changed(self, *args):
        self.balance_var.set('Saldo Actual: $'+str(self.controller.shared_data['Balance'].get()))

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading=tk.Label(self,text='CAJERO BANCO AMIGOS',font=('orbitron',45,'bold'),foreground='white',background='#3d3d5c')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Informacion personal',font=('orbitron',13),fg='white',bg='#3d3d5c')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#33334d')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both')

        ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
        mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
        mycursor=mydb.cursor()
        ##mycursor.execute("create database if not exists payrealx")
        mycursor.execute("use Gangrena")
        mycursor.execute(f"select pw from usuario where accit = {username1} ")
        pass_code=mycursor.fetchone()
        pass_code_read=''
        for i in pass_code:
            pass_code_read+=i

        name_info = tk.Label(upperframe, text=f'NOMBRE : {user_display_name}', font=('orbitron',16),fg='white', bg='#33334d')
        name_info.pack(pady=5)

        apep_info = tk.Label(upperframe, text=f'APELLIDO PATERNO : {apep_display_name}', font=('orbitron',16),fg='white', bg='#33334d')
        apep_info.pack(pady=5)

        apem_info = tk.Label(upperframe, text=f'APELLIDO MATERNO : {apem_display_name}', font=('orbitron',16),fg='white', bg='#33334d')
        apem_info.pack(pady=5)

        telf_info = tk.Label(upperframe, text=f'NUMERO DE TELEFONO : {telf_display_name}', font=('orbitron',16),fg='white', bg='#33334d')
        telf_info.pack(pady=5)

        accid_info = tk.Label(upperframe, text=f'NUMERO DE CUENTA : {username1}', font=('orbitron',16),fg='white', bg='#33334d')
        accid_info.pack(pady=5)

        pin_info = tk.Label(upperframe, text=f'PIN : {pass_code_read}', font=('orbitron',16),fg='white', bg='#33334d')
        pin_info.pack(pady=5)

       

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Menu',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)


################## CLASS  DEFINE FUNCTION #################################
def abcd():

        app = SampleApp()
        app.mainloop()


############################################################ REGISTER/LOGIN ############################################################


def password_not_recognised():
  messagebox.showwarning('Atenci??n',('Contrase??a invalida!'))

################## ABOUT SCREEN #################################
def about():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("About")
  screen3.geometry("380x90+750+230")
  screen3.configure(bg='lightblue')
  screen3.iconphoto(False,tk.PhotoImage(file='abc.png'))
  

################## WARNING_SCREEN #################################
def user_not_found():
  messagebox.showwarning('Alerta',('Usuario no encontrado !'))

################## REGISTER USER SCREEN #################################
def register_user():
  global username_info
  username_info = str(rand)
  password_info = password.get()
  name_info     = name.get()
  telf_info     = telf.get()
  apellidoP_info= apellidoP.get()
  apellidoM_info= apellidoM.get()
  Correo_info   = Correo.get()
  poss_info     = option_var.get()
  

  ################## MYSQL DATABASE ##################
  global mycursor
  ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
  mycursor=mydb.cursor()
  ##mycursor.execute("create database if not exists payrealx")
  mycursor.execute("use Gangrena")
  mydb.commit()

  mycursor.execute('select accit from usuario')
  values=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])
  if username_info in b:
    messagebox.showwarning('Alerta',('El usuario ya existe!'))

    password_entry.delete(0,END)
    name_entry.delete(0,END)
    apellM_entry.delete(0,END)
    apellP_entry.delete(0, END)
    correo_entry.delete(0, END)
    tel_entry.delete(0, END)


  elif name_info=='' :
        messagebox.showwarning('WARNING',('Ingresa un nombre!'))
        password_entry.delete(0,END)
  elif password_info=='' :
        messagebox.showwarning('WARNING',('Ingresa una contrase??a!'))
  elif telf_info=='' :
        messagebox.showwarning('WARNING',('Ingresa un telefono!'))
        password_entry.delete(0,END)
  elif apellidoP_info=='' :
        messagebox.showwarning('WARNING',('Ingresa apellido paterno!'))
  elif apellidoM_info=='' :
        messagebox.showwarning('WARNING',('Ingresa apellido materno!'))
        password_entry.delete(0,END)
  elif Correo_info=='' :
        messagebox.showwarning('WARNING',('Ingresa un correo!'))
  else:
        balance_inti='0.00'
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        apellM_entry.delete(0,END)
        apellP_entry.delete(0, END)
        correo_entry.delete(0, END)
        tel_entry.delete(0, END)        
        screen1.destroy()
        mycursor.execute("insert into usuario values('"+name_info+"', '"+apellidoP_info+"', '"+apellidoM_info+"', '"+telf_info+"', '"+Correo_info+"', '"+password_info+"', '"+poss_info+"', '"+balance_inti+"','"+username_info+"')")
        mydb.commit()
        messagebox.showinfo('Registro',('Exitoso!'))


################## LOGIN VERIFY SCREEN #################################
def login_verify():
  global current_balance
  global username1
  global name_display
  global user_display_name
  global apep_display_name
  global apem_display_name
  global telf_display_name
  global password1
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
  mycursor=mydb.cursor()
  #mycursor.execute("create database if not exists payrealx")
  mycursor.execute("use Gangrena")
  mycursor.execute("select accit from usuario")
  values=mycursor.fetchall()
  user_acc=[]
  for i in values:
    user_acc.append(i[0])

  if username1.isalpha():
        messagebox.showwarning('Atenci??n',('Ingrese un numero de cuenta valido!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)

  if str(username1)=='':
        messagebox.showwarning('Atenci??n',('Ingrese un numero de usuario!'))
        password_entry1.delete(0,END)
  elif str(username1).isspace():
        messagebox.showwarning('Antenci??n',('Ingrese un numero de usuario!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)
  elif username1.isalnum():
      if username1.isdigit():

          if int(username1) in user_acc:

              mycursor.execute(f"SELECT pw FROM usuario WHERE accit={username1}")
              values=mycursor.fetchall()
              mydb.commit()
              user_pass=[]
              for i in values:
                  user_pass.append(i[0])

              user_pass_1=int(user_pass[0])

              if password1=='':
                  messagebox.showwarning('Alerta',('Ingrese una contrase??a!'))
                  username_entry1.delete(0, END)
                  password_entry1.delete(0,END)
              elif password1 == str(user_pass_1) :
                  mycursor.execute(f"select nombre from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  user_name=[]
                  for i in values:
                    user_name.append(i[0])
                  user_display_name=str(user_name[0])

                  mycursor.execute(f"select apellido_pa from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  apep_name=[]
                  for i in values:
                    apep_name.append(i[0])
                  apep_display_name=str(apep_name[0])

                  mycursor.execute(f"select apellido_ma from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  apem_name=[]
                  for i in values:
                    apem_name.append(i[0])
                  apem_display_name=str(apem_name[0])

                  mycursor.execute(f"select telefono from usuario where accit={username1}")
                  values=mycursor.fetchall()
                  telf_name=[]
                  for i in values:
                    telf_name.append(i[0])
                  telf_display_name=str(telf_name[0])
                  #login_sucess()
                  ##mydb=mysql.connector.connect(host="localhost",user="root",password=enter your mysql password)
                  mydb=pyodbc.connect(driver='{SQL Server}', server='10.10.58.33', database='Gangrena', trusted_Connection='yes')
                  mycursor=mydb.cursor()
                  #mycursor.execute("create database if not exists payrealx")
                  mycursor.execute("use Gangrena")

                  mycursor.execute(f'select balance from usuario where accit={username1}')
                  values=mycursor.fetchall()
                  user_balance=[]
                  for i in values:
                    user_balance.append(i[0])
                  user_balance_1=float(user_balance[0])
                  current_balance=user_balance_1

                  screen2.destroy()
                  screen.destroy()
                  abcd()
              elif password1!= str(user_pass_1):
                  password_not_recognised()
          else:
              user_not_found()
      else:
          user_not_found()

  else:
        user_not_found()

################## REGISTER DISPLAY SCREEN #################################
def register():
  global screen1
  global password_entry
  global username_entry
  global tel_entry
  global apellP_entry
  global apellM_entry
  global correo_entry
  global rand
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("380x580+750+230")
  screen1.configure(bg='lightblue')
  screen1.iconphoto(False,tk.PhotoImage(file='abc.png'))

  photo = PhotoImage(file="login_person.png")
  img = photo.zoom(3)
  img = photo.subsample(2)
  label = Label(screen1,image=img,bg='lightblue')
  label.image = img

  label.pack(pady=2)

  global username
  global password
  global name
  global telf
  global apellidoM
  global apellidoP
  global Correo
  global option_var

  global username_entry1
  global password_entry1
  global name_entry

  username = StringVar()
  password = StringVar()
  name     = StringVar()
  telf     = StringVar()
  apellidoP = StringVar()
  apellidoM = StringVar()
  Correo = StringVar()
  option_var = StringVar()


  Label(screen1, text = "Ingresa tus datos",bg='lightblue',font = ("orbitron", 10)).pack()

  Label(screen1, text = "",bg='lightblue').pack()

  Label(screen1, text = "Nombre",font = ("orbitron", 10),bg='lightblue').pack()
  name_entry = Entry(screen1,font = ("orbitron",10), textvariable = name)
  name_entry.pack()

  Label(screen1, text = "Tu numero de cuenta es:",font = ("orbitron", 10),bg='lightblue').pack()
  rand=random.randint(1,100000)
  username=Label(screen1, text = rand,font = ("orbitron", 11),bg='lightblue').pack()
  #username_entry = Entry(screen1, textvariable = username)
  #username_entry.pack()

  Label(screen1, text = "Telefono",font = ("orbitron", 10),bg='lightblue').pack()
  tel_entry =  Entry(screen1,font = ("orbitron",10), textvariable = telf)
  tel_entry.config(fg='black')
  tel_entry.pack()

  Label(screen1, text = "Apellido Paterno",font = ("orbitron", 10),bg='lightblue').pack()
  apellP_entry =  Entry(screen1,font = ("orbitron",10), textvariable = apellidoP)
  apellP_entry.config(fg='black')
  apellP_entry.pack()

  Label(screen1, text = "Apellido Materno",font = ("orbitron", 10),bg='lightblue').pack()
  apellM_entry =  Entry(screen1,font = ("orbitron",10), textvariable = apellidoM)
  apellM_entry.config(fg='black')
  apellM_entry.pack()

  Label(screen1, text = "Correo",font = ("orbitron", 10),bg='lightblue').pack()
  correo_entry =  Entry(screen1,font = ("orbitron",10), textvariable = Correo)
  correo_entry.config(fg='black')
  correo_entry.pack()


  Label(screen1, text = "Contrase??a",font = ("orbitron", 10),bg='lightblue').pack()
  password_entry =  Entry(screen1,font = ("orbitron",10), textvariable = password)
  password_entry.config(fg='black',show='???')
  password_entry.pack()

  languages = (1, 2, 3 )

  label = Label(screen1,  text='Seleciona tu Posici??n', font= ("orbitron", 10), bg='lightblue').pack()

    # option menu
  option_menu = ttk.OptionMenu(
        screen1, 
        option_var,
        languages[0],
        *languages).pack()

  Label(screen1, text = "",bg='lightblue').pack()

  img1 = PhotoImage(file="register_final.png")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen1,command = register_user,image=photoimage1,bg='lightblue',activebackground='lightblue',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

################## LOGIN DISPLAY SCREEN #################################
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("380x470+750+230")
  screen2.configure(bg='lightblue')
  screen2.iconphoto(False,tk.PhotoImage(file='abc.png'))

  photo = PhotoImage(file="login_person.png")
  label = Label(screen2,image=photo,bg='lightblue')
  label.image = photo
  label.pack(pady=5)

  Label(screen2, text = "Por favor ingresa tus datos para iniciar sesi??n",bg='lightblue',font = ("orbitron", 10)).pack()
  Label(screen2, text = "",bg='lightblue').pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()


  global username_entry1
  global password_entry1

  Label(screen2, text = "Numero de cuenta",bg='lightblue',font = ("orbitron", 10)).pack()
  username_entry1 = Entry(screen2,font = ("orbitron",10) ,textvariable = username_verify)
  username_entry1.pack()

  Label(screen2, text = "",bg='lightblue').pack()
  Label(screen2, text = "PIN",bg='lightblue',font = ("orbitron", 10)).pack()
  password_entry1 = Entry(screen2,font = ("orbitron",10), textvariable = password_verify)
  password_entry1.config(fg='black',show='???')
  password_entry1.pack()

  img1 = PhotoImage(file="login_final.png")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen2,command = login_verify,image=photoimage1,bg='lightblue',activebackground='lightblue',relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

################## REGISTER/LOGIN SCREEN #################################
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("530x530+450+120")
  screen.title("BANCO AMIGOS")
  screen.configure(bg='lightblue')
  screen.iconphoto(False,tk.PhotoImage(file="abc.png"))


  Label(text = "BANCO AMIGOS",fg='white', bg = "grey", width = "300", height = "2", font = ("orbitron", 15,'bold')).pack()
  Label(text = "",bg='lightblue').pack()

  img = ImageTk.PhotoImage(Image.open("pr_logo.png"))
  panel = Label(screen, image = img,bg='lightblue')
  panel.pack()

  photo1 = PhotoImage(file="login_final.png")
  photoimage1 = photo1.subsample(2, 2)
  Button(command = login,bg='lightblue',activebackground='lightblue',relief=FLAT,image = photoimage1).pack(pady=5)

  Label(text = "",bg='lightblue',).pack()

  photo2 = PhotoImage(file="register_final.png")
  photoimage2 = photo2.subsample(2, 2)
  Button(command = register,bg='lightblue',activebackground='lightblue',relief=FLAT,image = photoimage2).pack(pady=5)

  Label(text = "",bg='lightblue').pack()

  ##photo3 = PhotoImage(file="about_final.png")
  ##photoimage3 = photo3.subsample(2, 2)
  ##Button(command = about,bg='lightblue',activebackground='lightblue',relief=FLAT,image = photoimage3).pack(pady=5)

  screen.mainloop()

main_screen()
