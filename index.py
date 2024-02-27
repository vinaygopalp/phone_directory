from tkinter import *  
import mysql.connector as mysql1
base = Tk()  

base.geometry("550x550")  
base.title('Registration form')  
base.config(bg="lightblue")
lbl_0 = Label(base, text="Phone Book", width=20,font=("bold",20),bg="blue") 
lbl_0.place(x=90,y=60)  
lbl_1 =Label(base, text= "Full Name", width=20,font=("bold",10))  
lbl_1.place(x=80,y=130)   
Name = Entry(base)  
Name.place(x=240,y=130)  

lbl_2 = Label(base, text="Email", width=14,font=("bold",14))  
lbl_2.place(x=68,y=180)  

email = Entry(base)  
email.place(x=240,y=180) 

lbl_3 = Label(base, text="Phone Number", width=14,font=("bold",14))  
lbl_3.place(x=68,y=230)  
Phone = Entry(base, width=30)  
Phone.place(x=240,y=220)
dic={}
def Objects():
    
    name = Name.get()
    dic["name"]=name
    phone=Phone.get()
    dic['phone']=phone
    Email=email.get()
    dic['email']=Email
    print(Email)
    sql_connector()
def sql_connector():
                mycon2=mysql1.connect(host="localhost",user="root",passwd="vinay",database="phone_book")
                cursor=mycon2.cursor()
                ST = "INSERT INTO contact (name, email, cell) VALUES ('{0}', '{1}', '{2}')".format(dic['name'], dic['email'], dic['phone'])

                cursor.execute(ST)
                mycon2.commit()
                mycon2.close()               
                # msg=QMessageBox()
                # msg.setText("submited")
                # X=msg.exec_()    
Button(base, text='Submit' , width=20, bg="black",fg='white',command=Objects).place(x=180,y=380)  
 
base.mainloop()  