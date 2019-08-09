import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(self):
			Gtk.Window.__init__(self, title="Hello World")

			label = Gtk.Label(label="Hello World", angle=50, halign=Gtk.Align.END)
			self.button = Gtk.Button()
			self.button.add(label)
			self.button.connect("clicked", self.on_button_clicked)
			self.button.connect("clicked", Gtk.main_quit)
			self.add(self.button)

	def on_button_clicked(self, widget):
			print("Hello World")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()