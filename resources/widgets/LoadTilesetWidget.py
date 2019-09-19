import array
from PIL import Image
from gi.repository import Gtk, GdkPixbuf
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
                self.insertImagesInGrid(image)
                self.widget.hide()

        except AttributeError as error:
            self.ErrorDialog.defineMessageError("You must select an image to load!")
            self.ErrorDialog.dialog.show()
            print(repr(error))
        except IndexError as error:
            self.ErrorDialog.defineMessageError("The size of tile exced the image size!")
            self.ErrorDialog.dialog.show()
            print(repr(error))
        except OSError as error:
            self.ErrorDialog.defineMessageError("This is not a valid image file!")
            self.ErrorDialog.dialog.show()
            print(repr(error))
    
    def cutImage(self, image):
        width = image.size[0]
        height = image.size[1]
        tile_width = self.width_input.get_value_as_int()
        tile_height = self.height_input.get_value_as_int()
        rows = int(width / tile_height)
        cols = int(height / tile_width)
        image_list = []
        
        colinit = 0
        colend = tile_width
        rowinit = 0
        rowend = tile_height
        
        for col in range(cols):
            for row in range(rows):
                outfile = "/var/tmp/evanbrostiles/"+str(row)+"-"+str(col)+".png"
                box = (rowinit, colinit, rowend, colend)
                rowinit += tile_height
                rowend += tile_height
                
                region = image.crop(box)

                region_colors = region.getcolors()
                
                if len(region_colors) == 1:
                    region_pixel_colors = region.getcolors()[0][1]
                    has_colors = False

                    for color in range(len(region_pixel_colors)):
                        if region_pixel_colors[color] > 0:
                            has_colors = True
                    
                    if has_colors:
                        image_list.append(str(row)+"-"+str(col)+".png")
                        region.save(outfile, "PNG")
                        
                else:
                    image_list.append(str(row)+"-"+str(col)+".png")
                    region.save(outfile, "PNG")
            
            colinit += tile_width
            colend += tile_width
                
        
        return image_list
    
    def insertImagesInGrid(self, image):
        image_list = self.cutImage(image)
        view = self.builder.get_object("tilesetview")
        
        # CLEAN CHILDREN FROM ELEMENT
        children = view.get_children()
        if children:
            for child_number in range( len(children) ):
                view.remove( children[child_number] )
        
        grid = Gtk.Grid()
        
        list_length = len(image_list)
        number_row = 0
        
        for number_tile in range(list_length):
            button = Gtk.Button()
            image = Gtk.Image()
            
            image.set_from_file("/var/tmp/evanbrostiles/"+image_list[number_tile])

            button.add(image)
            
            grid.attach( button, ( (number_tile + 1) % 4 )-1, number_row, 1, 1 )
            

            if not(number_tile % 4) :
                number_row += 1;
        
        view.add(grid)
        grid.show_all()