from gi.repository import Gtk
from resources.widgets.LoadTilesetWidget import LoadTilesetWidget

class Handler:
    def __init__(self, builder):
        self.builder = builder
        self.loadTilesetWidget = LoadTilesetWidget(builder)

    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def onNew(self, *args):
        print("new")

    def loadTilesetDialog(self, *args):
        self.loadTilesetWidget.widget.show()

    def addLayer(self, *args):
        print("add")
