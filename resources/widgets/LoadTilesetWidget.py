class LoadTilesetWidget:
    def __init__(self, builder):
        self.widget = builder.get_object("loadtilemapdialog")
        load_button = builder.get_object("loadtileset")
        cancel_button = builder.get_object("canceltileset")

        self.widget.connect("delete-event", self.deleteEvent)
        load_button.connect("clicked", self.loadTileset)
        cancel_button.connect("clicked", self.cancelTileset)

    def deleteEvent(self, *args):
        self.cancelTileset()
        return True

    def loadTileset(self, *args):
        print('oooi')

    def cancelTileset(self, *args):
        self.widget.hide()
