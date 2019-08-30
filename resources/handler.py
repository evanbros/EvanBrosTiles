from gi.repository import Gtk

class Handler:
    def __init__(self, builder):
        self.builder = builder

    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def onNew(self, *args):
        print("new")

    def loadTilesetDialog(self, *args):
        widget = self.builder.get_object("loadtilemapdialog")
        load_button = self.builder.get_object("loadtileset")
        cancel_button = self.builder.get_object("canceltileset")

        load_button.connect( "clicked", self.loadTileset )
        cancel_button.connect( "clicked", self.cancelTileset, widget )

        widget.show()

    def loadTileset(self, *args):
        print('oooi')

    def cancelTileset(self, button, widget):
        widget.hide()

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
