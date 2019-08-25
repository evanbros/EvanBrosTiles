from gi.repository import Gtk

class Handler:
    def __init__(self, builder, main_window):
        self.builder = builder
        self.main_window = main_window

    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def onNew(self, *args):
        print("new")

    def loadTileset(self, *args):
        dialog = Gtk.FileChooserDialog(
            parent=self.main_window,
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
            self.file_chooser_open( dialog.get_filename() )

        dialog.destroy()

    def file_chooser_open(self, a):
        print(a)

    def addLayer(self, *args):
        print("add")
