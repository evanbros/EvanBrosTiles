from PIL import Image
from gi.repository import Gtk
from resources.widgets.ErrorDialog import ErrorDialog

class LoadTilesetWidget:
    def __init__(self, builder):
        self.builder = builder
        self.ErrorDialog = ErrorDialog(builder)
        self.widget = builder.get_object("loadtilemapdialog")
        self.file_input = builder.get_object("tilesetfileinput")
        self.width_input = builder.get_object("tilesetwidthinput")
        self.height_input = builder.get_object("tilesetheightinput")

        load_button = builder.get_object("loadtileset")
        cancel_button = builder.get_object("canceltileset")

        self.widget.connect("delete-event", self.deleteEvent)
        load_button.connect("clicked", self.loadTileset)
        cancel_button.connect("clicked", self.cancelTileset)

    def deleteEvent(self, *args):
        self.widget.hide()
        return True
    
    def cancelTileset(self, *args):
        self.widget.hide()

    def loadTileset(self, *args):
        image_path = self.file_input.get_filename()
        
        try:
            with Image.open(image_path) as image:
                self.widget.hide()
        except AttributeError as error:
            self.ErrorDialog.defineMessageError("You must select an image to load!")
            self.ErrorDialog.dialog.show()
        except OSError as error:
            self.ErrorDialog.defineMessageError("This is not a valid image file!")
            self.ErrorDialog.dialog.show()