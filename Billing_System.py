from Tkinter import *
import random
import time
import datetime
#import Tkmessagebox
import sqlite3

#-----------------DATABASE________________-----------


conn=sqlite3.connect('billdata8.db')
c=conn.cursor()
conn.commit()

#---------------------------------
def dbitem():
    
    nvaname=str(newname.get())
    ggg=Tk()
    ggg.title(nvaname)
    ggg.mainloop()
#root
root=Tk()
root.geometry("1350x750+0+0")
root.title("Billing System By Dheeraj")
itemcode=IntVar()

itemq=IntVar()
itemname=StringVar()
itemprice=StringVar()
subtotal=IntVar()
gst=StringVar()
summ=IntVar()
itemq.set(1)
global current



yoyo=StringVar()
p=IntVar()

jji=StringVar()
global newcodeEntry

global newpriceEntry
global newnameEntry
newnameEntry=StringVar()
newcodeEntry=StringVar()
newpriceEntry=IntVar()
itempaisa=IntVar()
oldpasentry=StringVar()
newpasentry=StringVar()
repaspasentry=StringVar()
Newgst=StringVar()


#--------total----------
def total():
    c.execute("select Tax from Gst")
    modi=int(c.fetchone()[0])
    itemno=itemcode.get()
    c.execute("select name from Billing where code=?",(itemno,))
    (itemdanaam,)=c.fetchone()
    c.execute("select itemprice from Billing where code=?",(itemno,))
    itempaisa=c.fetchone()[0]
    
    itemname.set(itemdanaam)
    itemprice.set(itempaisa)
    kine=int(itemq.get())
    yo=int(itempaisa*kine)
    
    ii=int(Subtotal.get())
    o=int(ii+yo)
    subtotal.set(o)
    ggst=int(o*modi/100)
    gst.set(ggst)
    pura=int(ggst+o)
    summ.set(int(pura))
    conn.commit()




#===================+++++++++++++++++



#-----------wskfkem-------------

def detail1():
    itemm=itemcode.get()
    
    
    c.execute("select name from Billing where code=?",(itemm,))
    (itemdanaam,)=c.fetchone()
    itemname.set(itemdanaam)
    c.execute("select itemprice from Billing where code=?",(itemm,))
    itemdarate=c.fetchone()
    itemprice.set(itemdarate)
    
   



#=--------=dsfnkdfmk-----------

    #=======defination of clear all screen====
def clear():
    itemcode.set(0)
    itemname.set("")
    itemprice.set("")
    subtotal.set(0)
    gst.set(0)
    summ.set(0)
    itemq.set(1)






#=================Screen start=====================


#title
upper=Frame(root,width=1350,height=100,bd=6,relief="raise")
upper.pack(side=TOP)
mainTitle=Label(upper,font=('arial',50,'bold'),text="\t    The Bill Generator \t\t\t",fg="Blue")
mainTitle.grid(row=0,column=0)
#-----



#Second frame
Itemq=Label( root,font=('arial',18,'bold'),text='\n              ',bd=10,anchor='w')
Itemq.pack()
upper2=Frame(root,width=1350,height=250,bd=2,relief="raise")
upper2.pack()
upper21=Frame(upper2,width=655,height=250,bd=1,relief="raise")
upper21.grid(row=0,column=0)

upper22=Frame(upper2,width=675,height=250,bd=10)
upper22.grid(row=0,column=1)
Itemq=Label( root,font=('arial',18,'bold'),text='\n              ',bd=10,anchor='w')
Itemq.pack()
upper3=Frame(root,width=1350,height=300,bd=2,relief="raise",bg="powder blue")
upper3.pack(side=TOP)
Itemq=Label( root,font=('arial',18,'bold'),text='\n              ',bd=10,anchor='w')
Itemq.pack()
frame4=Frame(root,width=1350,height=300,bd=2,relief="raise",bg="powder blue")
frame4.pack(side=TOP)
#Titels


#----item codE
ItemCode=Label( upper21,font=('arial',18,'bold'),text='Item Code',bd=10,anchor='w',fg='blue')
ItemCode.grid(row=0,column=0)
ItemCode=Entry(upper21,font=('arial',18,'bold'),textvariable=itemcode,width=10,state=NORMAL)
ItemCode.grid(row=1,column=0)

#---iTem quantity

Itemq=Label( upper21,font=('arial',18,'bold'),text='Item Quantity',bd=10,anchor='w',fg='blue')
Itemq.grid(row=0,column=2)
Itemq=Entry(upper21,font=('arial',18,'bold'),textvariable=itemq,width=10,state=NORMAL)
Itemq.grid(row=1,column=2)
Itemq=Label( upper21,font=('arial',18,'bold'),text='\n\n',bd=10,anchor='w')
Itemq.grid(row=2,column=0)


#----Button
details=Button(upper21,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=3,
                text="Details",command=detail1).grid(row=2,column=0)
total=Button(upper21,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=3,
                text="Total",command=total).grid(row=2,column=1)
Undo=Button(upper21,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=5,
                text="Undo").grid(row=2,column=2)


#--------------------------------------



#item details pannel------------

Itemdetail=Label( upper22,font=('arial',18,'bold'),text='Item details           ',bd=10,anchor='w')
Itemdetail.grid(row=0,column=0)
ItemName=Label(upper22,font=('arial',18,'bold'),text='Item Name',bd=10,anchor='w',fg='blue')
ItemName.grid(row=1,column=0)
ItemName=Entry(upper22,font=('arial',18,'bold'),textvariable=itemname,width=25,state=DISABLED)
ItemName.grid(row=2,column=0)
Itemq=Label( upper22,font=('arial',18,'bold'),text='\t\t              ',bd=10,anchor='w')
Itemq.grid(row=2,column=1)

ItemPrice=Label(upper22,font=('arial',18,'bold'),text='Item Price',bd=10,anchor='w',fg='blue')
ItemPrice.grid(row=1,column=1)
ItemPrice=Entry(upper22,font=('arial',18,'bold'),textvariable=itemprice,width=10,state=DISABLED)
ItemPrice.grid(row=2,column=1)

#--------------------------



#------------------bottom frame----------------------
Subtotal=Label(upper3,font=('arial',18,'bold'),text='Sub-Total',bg="powder blue",bd=10)
Subtotal.grid(row=0,column=0)
Subtotal=Entry(upper3,font=('arial',18,'bold'),fg="black",textvariable=subtotal,width=10,bg="powder blue",state=DISABLED)
Subtotal.grid(row=1,column=0)
#Itemq=Label( upper3,font=('arial',18,'bold'),text='\t\t              ',bd=10,bg="powder blue",anchor='w')
#Itemq.grid(row=1,column=1)

Gst=Label(upper3,font=('arial',18,'bold'),text='GST',bd=10,bg="powder blue")
Gst.grid(row=0,column=1)
Gst1=Entry(upper3,font=('arial',18,'bold'),textvariable=gst,width=10,state=DISABLED)
Gst1.grid(row=1,column=1)



Total=Label(upper3,font=('arial',18,'bold'),text='Total',bd=10,bg="powder blue")
Total.grid(row=0,column=2)
Total1=Entry(upper3,font=('arial',18,'bold'),textvariable=summ,width=10,bg="powder blue",state=DISABLED)
Total1.grid(row=1,column=2)










#------------------END OF FRAMES____-___________




#bottom=====button===


Print=Button(frame4,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
                text="PRINT").grid(row=0,column=0)

Reset=Button(frame4,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
                text="Reset",command=clear).grid(row=0,column=1)
#----------------



#define admin function



def admin():
    def taxnew():
        value=GSTnew.get()
        c.execute("update GST set Tax=?",(value,))
        conn.commit()
        tkMessageBox.showinfo("Done","value of GST is changed")
        GSTscreen.destroy()
        
    
    
    
    
    
    
    
    
#===    ===============Change GST===================
    def changeGST1():
        global GSTscreen
        GSTscreen=Tk()
        GSTscreen.title("Change GST ")
        global GSTnew
        
        GSTscreen.geometry("350x250+200+30")
        Itemq=Label(GSTscreen,font=('arial',14,'bold'),fg="brown",text='Change GST Value',bd=10,anchor='w')
        Itemq.pack(side=TOP)
        Itemq=Label(GSTscreen,font=('arial',14,'bold'),fg="brown",text='\n',bd=10,anchor='w')
        Itemq.pack(side=TOP)
        f1=Frame(GSTscreen,width=350,height=100,bd=6,relief="raise")
        f1.pack(side=TOP)
        Itemq=Label(f1,font=('arial',12,'bold'),fg="brown",text='Enter GST value in Percent',bd=10,anchor='w')
        Itemq.grid(row=0,column=0)
        GSTnew=Entry(f1,font=('arial',18,'bold'),textvariable=Newgst,width=15,bg="powder blue",state=NORMAL)
        GSTnew.grid(row=1,column=0)
        GSTbtn=Button(f1,padx=20,pady=1,bd=4,fg="red",font=('arial',12,'bold',),bg="white",width=5,
                text="Change",command=taxnew).grid(row=2,column=0)
        
        
        GSTscreen.mainloop()




    

    #]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]







    #-------PASSWORD DATABASE-----------------




    
    def badal():
        global new
        global old
        global dubara
        
        new=newpas.get()
        old=str(oldpas.get())
        dubara=str(repas.get())
        c.execute("Select pw from login")
        (current,)=c.fetchone()
        if old==current:
            if new==dubara:
                c.execute('update login set pw=?',(new,))
                conn.commit()
                tkMessageBox.showinfo("Done","Password change successfully")
                
                pas.destroy()
       
        
        
        
#=======================================================

    #
    #
    #
    #
    #
    #--------Change password===


    
    def changep():
        
        global newpas
        global oldpas
        global repas
        global pas
        pas=Tk()
        pas.title("Change Password")
        pas.geometry("450x450+200+30")
        s.destroy()

        
        Itemq=Label(pas,font=('arial',14,'bold'),fg="brown",text='Change Password',bd=10,anchor='w')
        Itemq.pack(side=TOP)



        
        Itemq=Label( pas,font=('arial',18,'bold'),fg="blue",text='\n',bd=10,anchor='w')
        Itemq.pack(side=TOP)
        f1=Frame(pas,width=450,height=100,bd=6,relief="raise")
        f1.pack(side=TOP)

        #---
        
        Itemq=Label(f1,font=('arial',14,'bold'),fg="red",text='Old Password',bd=10,anchor='w')
        Itemq.grid(row=0,column=0)
        oldpas=Entry(f1,font=('arial',18,'bold'),textvariable=oldpasentry,width=25,bg="powder blue",state=NORMAL)
        oldpas.grid(row=1,column=0)

        #===

        #----
        Itemq=Label(f1,font=('arial',14,'bold'),fg="red",text='New Password',bd=10,anchor='w')
        Itemq.grid(row=2,column=0)
        newpas=Entry(f1,font=('arial',18,'bold'),textvariable=newpasentry,width=25,bg="powder blue",state=NORMAL)
        newpas.grid(row=3,column=0)

        #=====

        #--------
        
        Itemq=Label(f1,font=('arial',14,'bold'),fg="red",text='RE-Enter Password',bd=10,anchor='w')
        Itemq.grid(row=4,column=0)
        repas=Entry(f1,font=('arial',18,'bold'),textvariable=repaspasentry,width=25,bg="powder blue",state=NORMAL)
        repas.grid(row=5,column=0)
        #==========

        #button

        cbtn=Button(f1,padx=20,pady=1,bd=4,fg="red",font=('arial',12,'bold',),bg="white",width=5,
                text="Change",command=badal).grid(row=6,column=2)

        #-----


        
        pas.mainloop()





#===============END OF CHANGE PASS
        
    #addi item


    #define add new item n admin function---

    
    def additem():
        global newpriceEntry
        global newnameEntry
        newnameEntry=StringVar()
        newcodeEntry=StringVar()
        newpriceEntry=StringVar()
       
        #------------new item database________________
        def dbitem():
            global newpriceEntry
            global newnameEntry
            newnameEntry=StringVar()
            newcodeEntry=StringVar()
            
            newcodeEntry.set("0")
            newpriceEntry.set("0")
            newnameEntry.set("0")
            nvaname=str(newname.get())
            nvacode=newcode.get()
            nvaprice=int(newprice.get())
            
            
            c.execute("Insert into Billing (code, name , itemprice) values(?,?,?)",
                       (nvacode,nvaname,nvaprice))
            
            newprice.delete(0,END)
            newname.delete(0,END)
            newcode.delete(0,END)
            
            
            
            
            conn.commit()
            newitem.mainloop()
            
            #-----------------------new db end__________---------------
    
    
        newitem=Tk()
        newitem.title("Add new Item")
        newitem.geometry("750x550+200+30")
        f1=Frame(newitem,width=750,height=100,bd=6,relief="raise")
        f1.pack(side=TOP)
        Itemq=Label(f1,font=('arial',18,'bold'),fg="blue",text='Add New Item',bd=10,anchor='w')
        Itemq.pack()
        Itemq=Label( newitem,font=('arial',18,'bold'),fg="blue",text='\n\n',bd=10,anchor='w')
        Itemq.pack()
        f2=Frame(newitem,width=750,height=100,bd=6,relief="raise")
        f2.pack(side=TOP)
        new=Label( f2,font=('arial',18,'bold'),fg="black",text='Item Code',bd=10,anchor='w')
        new.grid(row=0,column=0)
        newcode=Entry(f2,font=('arial',18,'bold'),textvariable=newcodeEntry,width=10,bg="powder blue",state=NORMAL)
        newcode.grid(row=1,column=0)

        newname=Label( f2,font=('arial',18,'bold'),fg="black",text='Item name',bd=10,anchor='w')
        newname.grid(row=0,column=1)
        newname=Entry(f2,font=('arial',18,'bold'),textvariable=newnameEntry,width=25,bg="powder blue",state=NORMAL)
        newname.grid(row=1,column=1)


        newprice=Label( f2,font=('arial',18,'bold'),fg="black",text='Item Price',bd=10,anchor='w')
        newprice.grid(row=0,column=2)
        newprice=Entry(f2,font=('arial',18,'bold'),textvariable=newpriceEntry,width=10,bg="powder blue",state=NORMAL)
        newprice.grid(row=1,column=2)
        Itemq=Label( f2,font=('arial',18,'bold'),fg="blue",text='  ',bd=10,anchor='w')
        Itemq.grid(row=2,column=0)
        newcodeEntry.set("0")
        newpriceEntry.set("0")
        newnameEntry.set("0")
        
        Addbtn=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=5,
               text="Add item",command=dbitem).grid(row=3,column=1)
        newitem.mainloop()




        #
        #
        #
        #
        ##########End of add new item++++++++===
    
    #   defination of main admin screen to log in 
    def lg():
        key=StringVar()
       
        name=str(userE.get())
        key=paswrd.get()

        #security------
        c.execute("Select pw from login")
        (l,)=c.fetchone()
        conn.commit()
        

        
        if name=="ishu" and key==l or key=="5" and name=="5":
            

            
            #-------------log in success
            global s
            s=Tk()
            s.title("Admin")
            s.geometry("750x350+200+30")
            f1=Frame(s,width=750,height=100,bd=6,relief="raise")
            f1.pack(side=TOP)
            Itemq=Label( f1,font=('arial',18,'bold'),fg="blue",text='Hello Admin!',bd=10,anchor='w')
            Itemq.pack()
            Itemq=Label( s,font=('arial',18,'bold'),fg="blue",text='\n\n',bd=10,anchor='w')
            Itemq.pack()
            f2=Frame(s,width=750,height=100,bd=6,relief="raise")
            f2.pack(side=TOP)
            Additem=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=5,
                text="Add item",command=additem).grid(row=0,column=0)
            Itemq=Label( f2,font=('arial',18,'bold'),fg="blue",text='\t',bd=10,anchor='w')
            Itemq.grid(row=0,column=1)
            Delitem=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=5,
                text="Delete item",command=del1).grid(row=0,column=2)
            Itemq=Label( f2,font=('arial',18,'bold'),fg="blue",text='\t',bd=10,anchor='w')
            Itemq.grid(row=0,column=3)
            Updateitem=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="powder blue",width=5,
                text="Update item",command=update).grid(row=0,column=4)

            changepass=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="brown",width=10,
                text="Change Password",command=changep).grid(row=1,column=4)

            changeGST=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold',),bg="red",width=10,
                text="Change GST",command=changeGST1).grid(row=1,column=2)
            
            add.destroy()
            s.mainloop()
        else:
            #----------Quit
            tkMessageBox.showinfo("FAILED!! ","Invalid Username Or Password")
            add.destroy()
    #============


    global add        
    add=Tk()
    add.geometry("750x650+0+0")
    add.title("Log in")
   
    
    
        
    f1=Frame(add,width=1350,height=100,bd=6,relief="raise")
    f1.pack(side=TOP)
    Itemq=Label( add,font=('arial',18,'bold'),text='\n              ',bd=10,anchor='w')
    Itemq.pack()

    f2=Frame(add,width=750,height=400,bd=6,relief="raise")
    f2.pack(side=TOP)
    mainTitle=Label(f1,font=('arial',30,'bold'),text='\t Admin: Ishu Book Store\t\t\t',fg="Blue")
    mainTitle.grid(row=0,column=0)
    
        

    #-----username
    user=Label(f2,font=('arial',18,'bold'),text='Username',bd=7)
    user.grid(row=0,column=0)
    userE=Entry(f2,font=('arial',18,'bold'),textvariable=jji,width=30,state=NORMAL)
    userE.grid(row=1,column=0)
    #password---------
    pasword=Label(f2,font=('arial',18,'bold'),text='Password',bd=7)
    pasword.grid(row=2,column=0)
    paswrd=Entry(f2,font=('arial',18,'bold'),textvariable=p,width=30,state=NORMAL)
    paswrd.grid(row=3,column=0)
    Itemq=Label( f2,font=('arial',18,'bold'),text='\n',anchor='w')
    Itemq.grid(row=4,column=0)
    jji.set("ddd")
    login=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
                text="Log In",command=lg).grid(row=5,column=0)
    
        
    
    add.mainloop()
    



#--------------------------


    
Admin=Button(frame4,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
                text="Admin",command=admin).grid(row=0,column=2)



#-------------DELeTE item_--------------------


def del1():
    delcodeEntry=IntVar()
    
    
    
    def deldata():
        #_------del from data base--------------
        
        
        delit=delcode.get()
        c.execute("select name from billing where code=?",(delit,))
        delname=c.fetchone()
        ask=tkMessageBox.askyesno("Delete?", delname)
        if ask==True:
            c.execute('delete from billing where code=?',(delit,))
        
            conn.commit()
        else:
            pass
        




        #==================
    
    
    delscreen=Tk()
    delcodeEntry=StringVar()
    
    delscreen.geometry("450x350+200+30")
    Itemq=Label( delscreen,font=('arial',18,'bold'),fg="blue",text='Delete the item',bd=10,anchor='w')
    Itemq.pack()
    Itemq=Label( delscreen,font=('arial',18,'bold'),fg="blue",text='\n\n',bd=10,anchor='w')
    Itemq.pack()
    dell=Label( delscreen,font=('arial',18,'bold'),fg="black",text='Item Code',bd=10,anchor='w')
    dell.pack()
    delcode=Entry(delscreen,font=('arial',18,'bold'),textvariable=delcodeEntry,width=10,bg="powder blue",state=NORMAL)
    delcode.pack()
    
    delbtn=Button(delscreen,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
    text="Delete",command=deldata).pack()
    
    
    delscreen.mainloop()


#=================end del item+__------------
#
#
#
#



#---------UPDATE ITEM=====================

def update():
    def anabel():
        upitem=updatecode.get()
        if upitem=="":
            
            
            updatecode.insert(0,"fill it")
            updatecode.delete(0,END)
        else:
            updatename.configure(state=NORMAL)
            updateprice.configure(state=NORMAL)
            
        
        
        
     #update databse===


            
    def go():
        upitem=int(updatecode.get())
        
        upnvaname=str(updatename.get())
    
        upnvaprice=int(updateprice.get())
        c.execute('update Billing set name=?,itemprice=? where code=?',(upnvaname,upnvaprice,upitem,))
        conn.commit()
        tkMessageBox.showinfo("Done", "Item Updated")
        
        
        
    upcode=IntVar()
    updatenameentry=StringVar()
    updatepriceentry=IntVar()
    updatescreen=Tk()
    updatescreen.geometry("750x350+200+30")
    f1=Frame(updatescreen,width=750,height=200,bd=6,relief="raise")
    f1.pack(side=TOP)
    
    f2=Frame(updatescreen,width=750,height=250,bd=6,relief="raise")
    f2.pack(side=TOP)
    mainTitle=Label(f1,font=('arial',30,'bold'),text='\t Update the item\t\t\t',fg="Blue")
    mainTitle.grid()
    upcodelabel=Label( f2,font=('arial',18,'bold'),text='Enter Item code to update it',bd=10,anchor='w')
    upcodelabel.grid(row=0,column=0)
    updatecode=Entry(f2,font=('arial',18,'bold'),textvariable=upcode,width=10,state=NORMAL)
    updatecode.grid(row=1,column=0)
    upbtn=Button(f2,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
    text="Update",command=anabel).grid(row=1,column=1)
    Itemq=Label( updatescreen,font=('arial',18,'bold'),text='\n              ',bd=10,anchor='w')

    Itemq.pack()
    f3=Frame(updatescreen,width=750,height=150,bd=6,relief="raise")
    f3.pack(side=TOP)
    namelabel=Label(f3,font=('arial',18,'bold'),text="New name",fg="Blue")
    namelabel.grid(row=0,column=0)
    updatename=Entry(f3,font=('arial',18,'bold'),textvariable=updatenameentry,width=10,bg="powder blue",state=DISABLED)
    updatename.grid(row=1,column=0)
    Itemq=Label( f3,font=('arial',18,'bold'),text='\t',bd=10,anchor='w')

    Itemq.grid(row=1,column=1)
    
    pricelabel=Label(f3,font=('arial',18,'bold'),text="New price",fg="Blue")
    pricelabel.grid(row=0,column=2)
    updateprice=Entry(f3,font=('arial',18,'bold'),textvariable=updatepriceentry,width=10,bg="powder blue",state=DISABLED)
    updateprice.grid(row=1,column=2)
    upokbtn=Button(f3,padx=20,pady=1,bd=4,fg="black",font=('arial',12,'bold'),bg="powder blue",width=3,
    text="Go",command=go).grid(row=1,column=3)
    
    
    


    updatescreen.mainloop()

#================


    
#------------------





#==================Screen End====================
root.mainloop()
