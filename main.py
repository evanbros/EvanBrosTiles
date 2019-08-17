import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
	def onDestroy(self, *args):
		Gtk.main_quit()

	def onNew(self, *args):
		print("Novo?")

builder = Gtk.Builder()
builder.add_from_file("window.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainwindow")
window.show_all()

Gtk.main()