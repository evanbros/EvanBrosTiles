class ErrorDialog:
    def __init__(self, builder):
        self.builder = builder
        self.dialog = self.builder.get_object("errordialog")
        self.close_button = self.builder.get_object("errorclose")
        self.message_dialog = self.builder.get_object("errorlabel")

        self.dialog.connect("delete-event", self.deleteEvent)
        self.close_button.connect("clicked", self.closeError)

    def closeError(self, *args):
        self.dialog.hide()

    def deleteEvent(self, *args):
        self.dialog.hide()
        return True

    def defineMessageError(self, message_error):
        self.message_dialog.set_text(message_error)
