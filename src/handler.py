from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def onNew(self, *args):
        print("new")

    def loadTileset(self, fileChooser):
        response = fileChooser.run()

    def addLayer(self, *args):
        print("add")