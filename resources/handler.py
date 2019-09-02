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

    def file_chooser_open(self, *args):
        dialog = Gtk.FileChooserDialog(
            parent=self.builder.get_object("loadtilemapdialog"),
            title="Select a file", 
            action=Gtk.FileChooserAction.OPEN, 
            buttons=(
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK
            ) 
        )
        
        response = dialog.run()
        
        if response == Gtk.ResponseType.OK:
            print( dialog.get_filename() )

        dialog.destroy()

    def addLayer(self, *args):
        print("add")
