from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder



class Screen1(Screen):
	pass
	
class Screen2(Screen):
	pass

class Screen3(Screen):
	pass
	
class Screen4(Screen):
	pass
	
class Screen5(Screen):
	pass
	
class Manager(ScreenManager):
	pass
	
	
class BMIApp(MDApp):
	def build(self):
	
		bldr = Builder.load_file("message.kv")
		return bldr

	def login(self, user, passw, auth):
		z="Invalid Credentials"
		a=user.text
		b=passw.text
		if ((a=="admin") and (b=="admin")):
			self.root.current="scr2"
		else:
			auth.text = str(z)

	def calc(self, height, weight, result):
		h = float(height.text)
		w = float(weight.text)

		bmi = (w/(h*h))
		result.text = "Your BMI is: "+str(bmi)

	 	
BMIApp().run()