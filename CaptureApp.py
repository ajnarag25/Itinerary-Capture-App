from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.properties import StringProperty
import cv2
import os
from KivyFile import KV
import mysql.connector
Window.size = (400, 600)

HOME_DIR = os.path.dirname(__file__)

Places = []
wa = []
wawa = []
wawawa = []
name = []
data = []

class MediaApp(MDApp):
    name = StringProperty()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        screen = Screen()
        run = Builder.load_string(KV)
        screen.add_widget(run)
        return screen

    def exit(self):
        self.dialog = MDDialog(text="Do you want to log-out now?", size_hint=(0.7, 1),
                               buttons=[
                                   MDFlatButton(
                                       text="Yes", on_release=self.eeexit
                                   ), MDFlatButton(
                                       text="No", on_release=self.close
                                   )])

        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()

    def eeexit(self, obj):
        exit()

    def get(self,text):
        self.root.ids.name = text
        names = self.root.ids.name
        if names == "":
            names = "USER"
            name.append(names)
        else:
            name.append(names)


    def add(self,text):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="narag", database="bikeitinerary")
        self.root.ids.place = text
        a = self.root.ids.place
        if a == "":
            self.warning1 = MDDialog(text="Please input the Necessary Information Needed!",size_hint=(0.7,1),
                                     buttons = [
                                         MDFlatButton(
                                             text="OK", on_release=self.close1
                                         )])

            self.warning1.open()

        else:
            if not Places:
                self.warning3 = MDDialog(text="Do Want To Take Selfie in this Place?", size_hint=(0.7, 1),
                                         buttons=[
                                             MDFlatButton(
                                                 text="Yes", on_release=self.opencam
                                             ), MDFlatButton (text="No", on_release=self.close3)
                                         ])

                self.warning3.open()
                aa = a + '.png'
                Places.append([a,aa])

                data.append(a)

                convert = ''.join(data)
                txt = ''.join(name)

                connection = self.conn.cursor()
                prompt = "insert into itinerarydata(names,places) values(%s, %s);"
                dat = (txt,convert)
                connection.execute(prompt, dat)
                self.conn.commit()

                print("Successfully Added!")
                wa.append(aa)

            else:
                for i in range(len(Places)):
                    if a == Places[i][0]:
                        self.warning2 = MDDialog(text="It is already Exists!", size_hint=(0.7, 1),
                                                 buttons=[
                                                     MDFlatButton(
                                                         text="OK", on_release=self.close2
                                                     )])

                        self.warning2.open()
                        return

                txt = ''.join(name)
                connection = self.conn.cursor()
                check = "SELECT * FROM itinerarydata where names=%s;"
                txtname = (txt,)
                connection.execute(check, txtname)
                get = connection.fetchall()
                chk = len(get)
                if chk > 0:
                    data.append(a)
                    convert = ','.join(map(str, data))
                    add = "update itinerarydata set places=%s where names=%s;"
                    dat1 = (convert, txt)
                    connection.execute(add, dat1)
                    self.conn.commit()
                    print("Successfully Added!")


                self.warning3 = MDDialog(text="Do Want To Take Selfie in this Place?", size_hint=(0.7, 1),
                                         buttons=[
                                             MDFlatButton(
                                                 text="Yes", on_release=self.opencam
                                             ), MDFlatButton(text="No", on_release=self.close3)
                                         ])

                self.warning3.open()
                aa = a + '.png'
                Places.append([a, aa])
                wa.append(aa)



    def close1(self,obj):
        self.warning1.dismiss()
    def close2(self,obj):
        self.warning2.dismiss()
    def close3(self,obj):
        self.warning3.dismiss()
    def opencam(self,obj):

        cv2.namedWindow("Camera")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            key = cv2.waitKey(20)
            cv2.imshow("Camera", frame)
            rval, frame = vc.read()
            if key & 0xFF == ord('s'):  # save on pressing 's'
                cv2.imwrite(wa[0], frame)
                wawawa.append(wa[0])
                wa.clear()
                print(wa)
                self.warning3.dismiss()
                print("Captured")
                break
            elif key == 27:  # exit on ESC
                self.warning3.dismiss()
                break
        cv2.destroyWindow("Camera")

class First(Screen):
    pass
class MyApp(Screen):
    pass
class CreateItinerary(Screen):
    pass

class ShowItinerary(Screen):
    def show(self):
        if not Places:
            self.warning1 = MDDialog(text="It is Empty", size_hint=(0.7, 1),
                                     buttons=[
                                         MDFlatButton(
                                             text="OK", on_release=self.close1
                                         )])
            self.warning1.open()
        else:
            qw = len(wawa)
            qe = len(Places)
            qr = qe - qw
            print(qr)
            if not wawa:
                for i in range(len(Places)):
                    wawa.append(Places[i][0])
                    self.ids.go.add_widget(
                OneLineListItem(text=Places[i][0],on_release=self.openImage
        ))
            elif len(wawa) == len(Places):
                self.warning2 = MDDialog(text="It is Already Updated!", size_hint=(0.7, 1),
                                         buttons=[
                                             MDFlatButton(
                                                 text="OK", on_release=self.close2
                                             )])
                self.warning2.open()
            else:
                for q in range(qw,len(Places)):
                    wawa.append(Places[q][0])
                    self.ids.go.add_widget(
                        OneLineListItem(text=Places[q][0],on_release=self.openImage
                                        ))

    def openImage(self,OneLineListItem):
        we = OneLineListItem.text
        if not wawawa:
            print('For Logic')
        else:
            for i in range(len(Places)):
                for x in range(len(wawawa)):
                    if we == Places[i][0]:
                        if Places[i][1] == wawawa[x]:
                            color_img = cv2.imread(wawawa[x])
                            cv2.imshow('Selfie', color_img)
                            cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            return
        self.warning5 = MDDialog(text="There's no picture inserted!", size_hint=(0.7, 1),
                                 buttons=[
                                     MDFlatButton(
                                         text="Okay", on_release=self.closewindow
                                     )
                                 ])

        self.warning5.open()


    def closewindow(self,obj):
        self.warning5.dismiss()
    def close1(self,obj):
        self.warning1.dismiss()
    def close2(self,obj):
        self.warning2.dismiss()



class About(Screen):
    pass

go = ScreenManager()
go.add_widget(First(name="firstpage"))
go.add_widget(MyApp(name="gomain"))
go.add_widget(CreateItinerary(name="iti"))
go.add_widget(ShowItinerary(name="show"))
go.add_widget(About(name="abt"))

MediaApp().run()


