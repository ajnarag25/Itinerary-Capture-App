from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
import cv2
import os
from KivyFile import KV
Window.size = (400, 600)

HOME_DIR = os.path.dirname(__file__)

Places = []
wa = []
wawa = []
wawawa = []
class MediaApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        screen = Screen()
        run = Builder.load_string(KV)
        screen.add_widget(run)
        return screen

    def add(self,text):
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
                wa.append(aa)
                print(Places)
                print(wa)
                print('waaaaaaaaaaaaaaaaaaaaa')
            else:
                for i in range(len(Places)):
                    print('wa')
                    if a == Places[i][0]:
                        print('wawa')
                        self.warning2 = MDDialog(text="It is already Exists!", size_hint=(0.7, 1),
                                                 buttons=[
                                                     MDFlatButton(
                                                         text="OK", on_release=self.close2
                                                     )])

                        self.warning2.open()
                        return
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
                print(Places)
                print(wa)

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
            print(qw)
            qe = len(Places)
            print(qe)
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
go.add_widget(MyApp(name="gomain"))
go.add_widget(CreateItinerary(name="iti"))
go.add_widget(ShowItinerary(name="show"))
go.add_widget(About(name="abt"))

MediaApp().run()


