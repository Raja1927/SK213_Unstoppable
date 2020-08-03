import tkinter as tk
from tkinter import *
import cv2
import os
import numpy as np
from PIL import Image,ImageTk
import datetime
import time

#####Window is our Main frame of system
window = tk.Tk()
window.title("Access System")

window.geometry('790x520+0+0')
window.configure(background='black')
image=Image.open("image120.jpg")
photo1=ImageTk.PhotoImage(image)
label_1=Label(image=photo1)
label_1.pack()
un = tk.Label(window, text="Username", width=10, height=2, fg="black", bg="#2bd92b",
              font=('times', 10, ' bold '))
un.place(x=150, y=150)
pw = tk.Label(window, text="Password", width=10, height=2, fg="black", bg="#2bd92b",
              font=('times', 10, ' bold '))
pw.place(x=150, y=240)

un_entr1 = tk.Entry(window, width=20, bg="white", fg="red", font=('times', 23, ' bold '))
un_entr1.place(x=270, y=150)
pw_entr2 = tk.Entry(window, width=20, show="*", bg="white", fg="red", font=('times', 23, ' bold '))
pw_entr2.place(x=270, y=240)

####GUI for manually fill attendance
def manually_fill():
    global sb
    sb = tk.Tk()
    sb.iconbitmap('AMS.ico')
    sb.title("Enter Category...")
    sb.geometry('580x320')
    sb.configure(background='#261a24')

    def err_screen_for_subject():

        def ec_delete():
            ec.destroy()
        global ec
        ec = tk.Tk()
        ec.geometry('300x100')
        ec.iconbitmap('AMS.ico')
        ec.title('Warning!!')
        ec.configure(background='snow')
        Label(ec, text='Please enter category!', fg='red', bg='white', font=('times', 16, ' bold ')).pack()
        Button(ec, text='OK', command=ec_delete, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
               font=('times', 15, ' bold ')).place(x=90, y=50)

    def fill_attendance():
        ts = time.time()
        Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        ####Creatting csv of attendance
        ##Create table for Attendance
        global subb
        subb=SUB_ENTRY.get()
        DB_table_name = str(subb + "" + Date + "_Time" + Hour + "" + Minute + "" + Second)

        import pymysql.connections

        ###Connect to the database
        try:
            global cursor
            connection = pymysql.connect(host='localhost', user='root', password='raja', db='manually')
            cursor = connection.cursor()
        except Exception as e:
            print(e)

        sql = "CREATE TABLE " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT,
                         SUSPECT_ID varchar(100) NOT NULL,
                         NAME VARCHAR(50) NOT NULL,
                         PLACE VARCHAR(50) NOT NULL,
                         AGE VARCHAR(20) NOT NULL,
                         TYPE VARCHAR(20) NOT NULL,
                         DATE VARCHAR(20) NOT NULL,
                         TIME VARCHAR(20) NOT NULL,
                             PRIMARY KEY (ID)
                             );
                        """


        try:
            cursor.execute(sql)  ##for create a table
        except Exception as ex:
            print(ex)  #

        if subb=='':
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Tk()
            MFW.iconbitmap('AMS.ico')
            MFW.title("Manually filling of "+ str(subb))
            MFW.geometry('880x700')
            MFW.configure(background='#301a2b')

            def del_errsc2():
                errsc2.destroy()

            def err_screen1():
                global errsc2
                errsc2 = tk.Tk()
                errsc2.geometry('330x100')
                errsc2.iconbitmap('AMS.ico')
                errsc2.title('Warning!!')
                errsc2.configure(background='snow')
                Label(errsc2, text='Please enter Suspect details', fg='red', bg='white',
                      font=('times', 16, ' bold ')).pack()
                Button(errsc2, text='OK', command=del_errsc2, fg="black", bg="lawn green", width=9, height=1,
                       activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)

            def testVal(inStr, acttyp):
                if acttyp == '1':  # insert
                    if not inStr.isdigit():
                        return False
                return True

            ENR = tk.Label(MFW, text="Enter Suspect ID", width=15, height=2, fg="white", bg="#1b3c44",
                           font=('times', 15, ' bold '))
            ENR.place(x=30, y=60)

            STU_NAME = tk.Label(MFW, text="Enter Suspect name", width=15, height=2, fg="white", bg="#1b3c44",
                                font=('times', 15, ' bold '))
            STU_NAME.place(x=30, y=160)

            PLACE = tk.Label(MFW, text="Enter Place", width=15, height=2, fg="white", bg="#1b3c44",
                           font=('times', 15, ' bold '))
            PLACE.place(x=30, y=260)

            AGE = tk.Label(MFW, text="Enter Age", width=15, height=2, fg="white", bg="#1b3c44",
                           font=('times', 15, ' bold '))
            AGE.place(x=30, y=360)

            Type = tk.Label(MFW, text="Enter Criminal Type", width=15, height=2, fg="white", bg="#1b3c44",
                           font=('times', 15, ' bold '))
            Type.place(x=30, y=460)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(MFW, width=20,validate='key', bg="snow", fg="red", font=('times', 23, ' bold '))
            ENR_ENTRY['validatecommand'] = (ENR_ENTRY.register(testVal), '%P', '%d')
            ENR_ENTRY.place(x=290, y=65)

            global AGE_ENTRY
            AGE_ENTRY = tk.Entry(MFW, width=20, validate='key', bg="snow", fg="red", font=('times', 23, ' bold '))
            AGE_ENTRY['validatecommand'] = (ENR_ENTRY.register(testVal), '%P', '%d')
            AGE_ENTRY.place(x=290, y=365)

            PLACE_ENTRY = tk.Entry(MFW, width=20, bg="snow", fg="red", font=('times', 23, ' bold '))
            PLACE_ENTRY.place(x=290, y=265)

            TYPE_ENTRY = tk.Entry(MFW, width=20, bg="snow", fg="red", font=('times', 23, ' bold '))
            TYPE_ENTRY.place(x=290, y=465)

            def remove_enr():
                ENR_ENTRY.delete(first=0, last=22)

            STUDENT_ENTRY = tk.Entry(MFW, width=20, bg="snow", fg="red", font=('times', 23, ' bold '))
            STUDENT_ENTRY.place(x=290, y=165)

            def remove_student():
                STUDENT_ENTRY.delete(first=0, last=22)


            def remove_place():
                PLACE_ENTRY.delete(first=0, last=50)

            def remove_age():
                AGE_ENTRY.delete(first=0, last=22)

            def remove_type():
                TYPE_ENTRY.delete(first=0, last=22)

            ####get important variable
            def enter_data_DB():
                SUSPECT_ID = ENR_ENTRY.get()
                STUDENT = STUDENT_ENTRY.get()
                PLACE = PLACE_ENTRY.get()
                AGE = AGE_ENTRY.get()
                TYPE = TYPE_ENTRY.get()

                if SUSPECT_ID=='':
                    err_screen1()
                elif STUDENT=='':
                    err_screen1()
                elif PLACE=='':
                    err_screen1()
                elif AGE=='':
                    err_screen1()
                elif TYPE=='':
                    err_screen1()
                else:
                    time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    Hour, Minute, Second = time.split(":")
                    Insert_data = "INSERT INTO " + DB_table_name + " (ID,SUSPECT_ID,NAME,PLACE,AGE,TYPE,DATE,TIME) VALUES (0, %s, %s, %s, %s, %s, %s,%s)"
                    VALUES = [(str(SUSPECT_ID), str(STUDENT), str(PLACE), str(AGE), str(TYPE), str(Date), str(time))]
                    try:
                        cursor.executemany(Insert_data, VALUES)
                        connection.commit()
                    except Exception as e:
                        print(e)
                    ENR_ENTRY.delete(first=0, last=22)
                    STUDENT_ENTRY.delete(first=0, last=22)
                    PLACE_ENTRY.delete(first=0, last=50)
                    AGE_ENTRY.delete(first=0, last=22)
                    TYPE_ENTRY.delete(first=0, last=20)

            def create_csv():
                import csv
                cursor.execute("select * from " + DB_table_name + ";")
                csv_name='C:/Users/shubh/Desktop/Police_Functions/Details/Manually/'+DB_table_name+'.csv'
                with open(csv_name, "w") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                    csv_writer.writerows(cursor)
                    O="CSV created Successfully"
                    Notifi.configure(text=O, bg="Green", fg="white", width=33, font=('times', 19, 'bold'))
                    Notifi.place(x=140, y=610)
                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Attendance of " + subb)
                root.configure(background='snow')
                with open(csv_name, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(root, width=13, height=1, fg="black", font=('times', 13, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()

            Notifi = tk.Label(MFW, text="CSV created Successfully", bg="Green", fg="white", width=33,
                                height=2, font=('times', 19, 'bold'))


            c1ear_enroll = tk.Button(MFW, text="Clear", command=remove_enr, fg="black", bg="#9fbacd", width=10,
                                     height=1,
                                     activebackground="Red", font=('times', 15, ' bold '))
            c1ear_enroll.place(x=690, y=60)

            c1ear_student = tk.Button(MFW, text="Clear", command=remove_student, fg="black", bg="#9fbacd", width=10,
                                      height=1,
                                      activebackground="Red", font=('times', 15, ' bold '))
            c1ear_student.place(x=690, y=160)

            c1ear_place = tk.Button(MFW, text="Clear", command=remove_place, fg="black", bg="#9fbacd", width=10,
                                      height=1,
                                      activebackground="Red", font=('times', 15, ' bold '))
            c1ear_place.place(x=690, y=260)

            c1ear_age = tk.Button(MFW, text="Clear", command=remove_age, fg="black", bg="#9fbacd", width=10,
                                      height=1,
                                      activebackground="Red", font=('times', 15, ' bold '))
            c1ear_age.place(x=690, y=360)

            c1ear_type = tk.Button(MFW, text="Clear", command=remove_type, fg="black", bg="#9fbacd", width=10,
                                  height=1,
                                  activebackground="Red", font=('times', 15, ' bold '))
            c1ear_type.place(x=690, y=460)

            DATA_SUB = tk.Button(MFW, text="Enter Data",command=enter_data_DB, fg="black", bg="#b38097", width=20,
                                 height=2,
                                 activebackground="Red", font=('times', 15, ' bold '))
            DATA_SUB.place(x=140, y=530)

            MAKE_CSV = tk.Button(MFW, text="Convert to CSV",command=create_csv, fg="black", bg="#d4bacd", width=20,
                                 height=2,
                                 activebackground="Red", font=('times', 15, ' bold '))
            MAKE_CSV.place(x=540, y=530)

            MFW.mainloop()


    SUB = tk.Label(sb, text="Enter Crime", width=15, height=2, fg="white", bg="#3e546e", font=('times', 15, ' bold '))
    SUB.place(x=30, y=100)

    global SUB_ENTRY

    SUB_ENTRY = tk.Entry(sb, width=20, bg="snow", fg="red", font=('times', 23, ' bold '))
    SUB_ENTRY.place(x=250, y=105)

    fill_manual_attendance = tk.Button(sb, text="Fill Suspect Details",command=fill_attendance, fg="black", bg="#c9b59b", width=20, height=2,
                       activebackground="Red", font=('times', 15, ' bold '))
    fill_manual_attendance.place(x=250, y=160)
    sb.mainloop()

##For clear textbox
def clear():
    txt.delete(first=0, last=22)

def clear1():
    txt2.delete(first=0, last=22)
def del_sc1():
    sc1.destroy()
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry('300x100')
    sc1.iconbitmap('AMS.ico')
    sc1.title('Warning!!')
    sc1.configure(background='snow')
    Label(sc1,text='ID & Name required!!!',fg='red',bg='white',font=('times', 16, ' bold ')).pack()
    Button(sc1,text='OK',command=del_sc1,fg="black"  ,bg="lawn green"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)

##Error screen2
def del_sc2():
    sc2.destroy()
def err_screen1():
    global sc2
    sc2 = tk.Tk()
    sc2.geometry('300x100')
    sc2.iconbitmap('AMS.ico')
    sc2.title('Warning!!')
    sc2.configure(background='snow')
    Label(sc2,text='Please enter category!!!',fg='red',bg='white',font=('times', 16, ' bold ')).pack()
    Button(sc2,text='OK',command=del_sc2,fg="black"  ,bg="lawn green"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)

###for choose subject and fill attendance
def subjectchoose():
    def Fillattendances():
        sub=tx.get()
        now = time.time()  ###For calculate seconds of video
        future = now + 20
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                try:
                    recognizer.read("TrainingImageLabel\Trainner.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=20, y=250)

                harcascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.1, 10)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf <70):
                            print(conf)
                            global Subject
                            #global aa
                            global date
                            global timeStamp

                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            global tt
                            tt = str(Id) + '-' + aa
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)

                        else:
                            Id = 'Unknown'
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                    if time.time() > future:
                        break

                    cv2.imshow('Filling Details..', im)
                    key = cv2.waitKey(30) & 0xff
                    if key == 27:
                        break

                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Hour, Minute, Second = timeStamp.split(":")

                ##Create table for Attendance
                date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
                DB_Table_name = str( Subject + "" + date_for_DB + "_Time" + Hour + "" + Minute + "" + Second)
                import pymysql.connections

                ###Connect to the database
                try:
                    global cursor
                    connection = pymysql.connect(host='localhost', user='root', password='raja', db='Face_reco_fill')
                    cursor = connection.cursor()
                except Exception as e:
                    print(e)

                sql = "CREATE TABLE " + DB_Table_name + """
                (ID INT NOT NULL AUTO_INCREMENT,
                 SUSPECT_ID varchar(100) NOT NULL,
                 NAME VARCHAR(50) NOT NULL,
                 PLACE VARCHAR(50) NOT NULL,
                 AGE VARCHAR(20) NOT NULL,
                 TYPE VARCHAR(20) NOT NULL,
                 DATE VARCHAR(20) NOT NULL,
                 TIME VARCHAR(20) NOT NULL,
                     PRIMARY KEY (ID)
                     );
                """
                try:
                    cursor.execute(sql)  ##for create a table
                except Exception as ex:
                    print(ex)  #

                ####Now enter details in Database
                insert_data =  "INSERT INTO " + DB_Table_name + " (ID,SUSPECT_ID,NAME,PLACE,AGE,TYPE,DATE,TIME) VALUES (0, %s, %s, %s, %s, %s, %s,%s)"
                VALUES = [(str(Id), str(aa), str(Place), str(Age), str(Ctype), str(date), str(timeStamp))]
                try:
                    cursor.executemany(insert_data, VALUES)##For insert data into table
                    connection.commit()
                except Exception as ex:
                    print(ex)  #

                M = 'Suspect Entered Successfully'
                Notifica.configure(text=M, bg="Green", fg="white", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=20, y=250)

                import csv
                cursor.execute("select * from " + DB_Table_name + ";")
                with open('SuspectDetails\SuspectDetails.csv', 'a') as csvFile:
                    csv_writer = csv.writer(csvFile)
                    csv_writer.writerows(cursor)

                fileName = "Details/" + Subject + "" + date + "_Time" + Hour + "-" + Minute + "-" + Second + ".csv"

                import csv
                cursor.execute("select * from " + DB_Table_name + ";")
                with open(fileName, 'w') as csvv:
                    csv_writer = csv.writer(csvv)
                    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                    csv_writer.writerows(cursor)

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Details of " + Subject)
                root.configure(background='snow')
                cs = 'C:/Users/shubh/Desktop/Police_Functions/' + fileName
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()

    ###windo is frame for subject chooser
    windo = tk.Tk()
    windo.iconbitmap('AMS.ico')
    windo.title("Enter Category...")
    windo.geometry('580x320')
    windo.configure(background='#261a24')
    Notifica = tk.Label(windo, text="Suspect filled Successfully", bg="Green", fg="white", width=33,
                            height=2, font=('times', 15, 'bold'))

    sub = tk.Label(windo, text="Enter Crime", width=15, height=2, fg="white", bg="#3e546e", font=('times', 15, ' bold '))
    sub.place(x=30, y=100)

    tx = tk.Entry(windo, width=20, bg="snow", fg="red", font=('times', 23, ' bold '))
    tx.place(x=250, y=105)

    fill_a = tk.Button(windo, text="Check", fg="black",command=Fillattendances, bg="#c9b59b", width=20, height=2,
                       activebackground="Red", font=('times', 15, ' bold '))
    fill_a.place(x=250, y=160)
    windo.mainloop()


def Submit():
    global NN
    NN = en1.get()
    global rad
    rad = en4.get(1.0, "end")
    pathname = 'C:/Users/shubh/Desktop/Police_Functions/FIR'
    fname = os.path.join(pathname, NN +".txt")
    file = open(fname, "w")
    file.write(rad)
    file.close()
    en1.delete(first=0, last=22)
    en4.delete(1.0, END)

def Fill_FIR():
    global fi
    fi = tk.Tk()
    fi.iconbitmap('AMS.ico')
    fi.title("Report FIR")
    fi.geometry('1000x720')
    fi.configure(background='#54743b')

    global Lb2

    Lb1 = tk.Label(fi,text="Applicant Name", width=12, height=2, fg="white", bg="#426b98", font=('times', 15, ' bold '))
    Lb1.place(x=10,y=10)
    Lb4 = tk.Label(fi, text="Detial of Crime", width=50, height=2, fg="white", bg="#426b98", font=('times', 15, ' bold '))
    Lb4.place(x=200, y=65)

    global en1
    global en4


    en1 = tk.Entry(fi, width=35, bg="snow", fg="red", font=('times', 23, ' bold '))
    en1.place(x=200, y=10)
    en4 = tk.Text(fi, width= 60, height=15, bg="snow", fg="red", font=('times', 23, ' bold ') )
    en4.place(x=14, y=110)

    Sub = tk.Button(fi, text="Submit", fg="white", command=Submit, bg="#928443",width=20, height=1, font=('times', 15, ' bold '))
    Sub.place(x=400, y=670)
    fi.mainloop()


def admin_panel():
    email=un_entr1.get()
    passw=pw_entr2.get()

    if email == 'vivek':
        if passw == 'vivek123':
            window.destroy()

            win = tk.Tk()
            win.iconbitmap('AMS.ico')
            win.title("FRI-Face Recoginition System")
            win.geometry('1280x720+0+0')
            image = Image.open("image77.jpg")
            photo1 = ImageTk.PhotoImage(image)
            label_1 = Label(image=photo1)
            label_1.pack()

        else:
            valid = 'Incorrect ID or Password'
            l.configure(text=valid, bg="white", fg="black", width=20, font=('times', 19, 'bold'))
            l.place(x=280, y=380)

    else:
        valid = 'Incorrect ID or Password'
        l.configure(text=valid, bg="white", fg="black", width=20, font=('times', 19, 'bold'))
        l.place(x=280, y=380)

    def log_in():

        import csv
        import tkinter
        root = tkinter.Tk()
        root.title("Suspect Details")
        root.configure(background='snow')

        cs = 'C:/Users/shubh/Desktop/Police_Functions/SuspectDetails/SuspectDetails.csv'
        with open(cs, newline="") as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:
                    # i've added some styling
                    label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                          bg="white", text=row, relief=tkinter.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
    AP = tk.Button(win, text="Check Suspect Register", command=log_in, fg="black", bg="gray", width=20, height=1,
                   activebackground="Red", font=('times', 15, ' bold '))
    AP.place(x=750, y=650)
    #For takking images as data
    def take_img():
        l1 = txt.get()
        l2 = txt2.get()
        l3 = txt3.get()
        l4 = txt4.get()
        l5 = txt5.get()

        if l1 == '':
            err_screen()
        elif l2 == '':
            err_screen()
        elif l3 == '':
            err_screen()
        elif l4 == '':
            err_screen()
        elif l5=='':
            err_screen()
        else:
            try:
                cam = cv2.VideoCapture(0)
                detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                global Suspect_ID
                global aa
                global Age
                global Place
                global Ctype
                Suspect_ID = txt.get()
                aa = txt2.get()
                Age = txt4.get()
                Place = txt3.get()
                Ctype = txt5.get()

                sampleNum = 0
                while (True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.1, 10)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        # incrementing sample number
                        sampleNum = sampleNum + 1
                        # saving the captured face in the dataset folder
                        cv2.imwrite("TrainingImage/ " + aa + "." + Suspect_ID + '.' + str(sampleNum) + ".jpg",
                                    gray[y:y + h, x:x + w])
                        cv2.imshow('Frame', img)
                    # wait for 100 miliseconds
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    # break if the sample number is morethan 100
                    elif sampleNum > 70:
                        break
                cam.release()
                cv2.destroyAllWindows()
                ts = time.time()
                Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            except FileExistsError as F:
                f = 'Suspect Data already exists'
                Notification.configure(text=f, bg="Red", width=21)
                Notification.place(x=450, y=400)

    def remove_1():
        txt.delete(first=0, last=22)
    def remove_2():
        txt2.delete(first=0, last=22)
    def remove_3():
        txt3.delete(first=0, last=22)
    def remove_4():
        txt4.delete(first=0, last=22)
    def remove_5():
        txt5.delete(first=0, last=22)
    takeImg = tk.Button(win,text="Take Images", command=take_img, fg="black", bg="gray", width=20,
                        height=2, activebackground="Red", font=('times', 15, ' bold '))
    takeImg.place(x=130, y=550)
    lbl = tk.Label(win, text="Enter Suspect-id", width=20, height=2, fg="black", bg="gray",
                   font=('times', 15, ' bold '))
    lbl.place(x=200, y=120)
    lbl2 = tk.Label(win, text="Suspect Name", width=20, fg="black", bg="gray", height=2, font=('times', 15, ' bold '))
    lbl2.place(x=200, y=210)
    lbl3 = tk.Label(win, text="Enter Crime Place", width=20, fg="black", bg="gray", height=2, font=('times', 15, ' bold '))
    lbl3.place(x=200, y=300)
    lbl4 = tk.Label(win, text="Enter Age", width=20, fg="black", bg="gray", height=2, font=('times', 15, ' bold '))
    lbl4.place(x=200, y=390)
    lbl5 = tk.Label(win, text="Enter Criminal Type", width=20, fg="black", bg="gray", height=2, font=('times', 15, ' bold '))
    lbl5.place(x=200, y=480)
    message = tk.Label(win, text="Face-Recognition-Identification", bg="black", relief="flat", fg="#9c150b",
                       width=50,
                       height=3, font=('times', 30, 'bold '))
    message.place(x=70, y=-50)

    c1ear_1 = tk.Button(win, text="Clear", command=remove_1, fg="black", bg="gray", width=10,
                              height=1, font=('times', 15, ' bold '))
    c1ear_1.place(x=1000, y=120)
    c1ear_2 = tk.Button(win, text="Clear", command=remove_2, fg="black", bg="gray", width=10,
                        height=1, font=('times', 15, ' bold '))
    c1ear_2.place(x=1000, y=210)
    c1ear_3 = tk.Button(win, text="Clear", command=remove_3, fg="black", bg="gray", width=10,
                        height=1, font=('times', 15, ' bold '))
    c1ear_3.place(x=1000, y=300)
    c1ear_4 = tk.Button(win, text="Clear", command=remove_4, fg="black", bg="gray", width=10,
                        height=1, font=('times', 15, ' bold '))
    c1ear_4.place(x=1000, y=390)
    c1ear_4 = tk.Button(win, text="Clear", command=remove_5, fg="black", bg="gray", width=10,
                        height=1, font=('times', 15, ' bold '))
    c1ear_4.place(x=1000, y=480)

    def testVal(inStr, acttyp):
        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False
        return True

    txt = tk.Entry(win, validate="key", width=20, bg="snow", fg="black", font=('times', 25, ' bold '))
    txt['validatecommand'] = (txt.register(testVal), '%P', '%d')
    txt.place(x=550, y=120)
    txt2 = tk.Entry(win, width=20, bg="snow", fg="black", font=('times', 25, ' bold '))
    txt2.place(x=550, y=210)
    txt3 = tk.Entry(win, width=20, bg="snow", fg="black", font=('times', 25, ' bold '))
    txt3.place(x=550, y=300)
    txt4 = tk.Entry(win, validate="key", width=20, bg="snow", fg="black", font=('times', 25, ' bold '))
    txt4['validatecommand'] = (txt.register(testVal), '%P', '%d')
    txt4.place(x=550, y=390)
    txt5 = tk.Entry(win, width=20, bg="snow", fg="black", font=('times', 25, ' bold '))
    txt5.place(x=550, y=480)
    ###For train the model
    def trainimg():
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        global detector
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        try:
            global faces, Id
            faces, Id = getImagesAndLabels("TrainingImage")
        except Exception as e:
            l = 'please make "TrainingImage" folder & put Images'
            Notification.configure(text=l, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
            Notification.place(x=350, y=400)

        recognizer.train(faces, np.array(Id))
        try:
            recognizer.save("TrainingImageLabel\Trainner.yml")
        except Exception as e:
            q = 'Please make "TrainingImageLabel" folder'
            Notification.configure(text=q, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
            Notification.place(x=350, y=400)

        res = "Model Trained"  # +",".join(str(f) for f in Id)
        Notification.configure(text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=250, y=400)

    trainImg = tk.Button(win, text="Train Images", fg="black", command=trainimg, bg="gray", width=20,
                         height=2, activebackground="Red", font=('times', 15, ' bold '))
    trainImg.place(x=410, y=550)
    quitWindow = tk.Button(win, text="Manually Fill suspect", command=manually_fill, fg="black",
                           bg="gray", width=20, height=2, activebackground="blue", font=('times', 15, ' bold '))
    quitWindow.place(x=990, y=550)
    FA = tk.Button(win, text="face recoginition", fg="black", command=subjectchoose, bg="gray",
                   width=20, height=2, activebackground="Red", font=('times', 15, ' bold '))
    FA.place(x=690, y=550)
    FIR = tk.Button(win, text="Fill FIR", command=Fill_FIR, fg="black",
                           bg="gray", width=20, height=1, activebackground="blue", font=('times', 15, ' bold '))
    FIR.place(x=190, y=650)
    win.mainloop()
l = Label(window, bg="ivory", fg="darkgreen")

###For train the model
def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("TrainingImage")
    except Exception as e:
        l='please make "TrainingImage" folder & put Images'
        Notification.configure(text=l, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("TrainingImageLabel\Trainner.yml")
    except Exception as e:
        q='Please make "TrainingImageLabel" folder'
        Notification.configure(text=q, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    res = "Model Trained"  # +",".join(str(f) for f in Id)
    Notification.configure(text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
    Notification.place(x=250, y=400)

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = detector.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as Id of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.iconbitmap('AMS.ico')

def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)
image0=Image.open("image99.jpg")
photo2=ImageTk.PhotoImage(image0)

Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                      height=3, font=('times', 17, 'bold'))

AP = tk.Button(window, text="LogIn",command=admin_panel,fg="black"  ,bg="gray"  ,width=10 ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
AP.place(x=467, y=305)
img2=PhotoImage(file="image104.png")

window.mainloop()