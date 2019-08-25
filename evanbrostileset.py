import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from resources.handler import Handler

builder = Gtk.Builder()
builder.add_from_file("template/window.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainwindow")
window.maximize()
window.show_all()

Gtk.main()