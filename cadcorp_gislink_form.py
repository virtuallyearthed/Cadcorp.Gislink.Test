import gislink
import logging
import tkinter

class ModalForm(tkinter.Tk):
    def __init__(self, name, sis):
        super().__init__()
        self.log = logging.getLogger(__name__)

        try:
            assert sis is not None
            self.log.debug("Form Opened")

            self.sis = sis  # GisLink Program object
            self.title(name)

            # SAFETY: Set handler for closing with X button in
            #         upper-right corner of window.
            #         Ensures parent process does not terminate
            #         along with Tkinter/Tcl interpreter.
            self.protocol('WM_DELETE_WINDOW', self.close)
            self.frame = tkinter.Frame(self)
        
            self.frame.grid(row=0, columnspan=2,
                            sticky=tkinter.W + tkinter.E + tkinter.N + tkinter.S)
            
            #Get Selected items
            sis.CreateListFromSelection("selected_items")
            details = sis.GetListDetails("selected_items").split(":")
            #List details contain the Dataset ID "colon" comma seperated list of object Ids "colon" repeat
            sis.EmptyList("selected_items")
            
            self.log.debug("List Details: %s", details)
            if not details or not details[0]:
                self.log.warn("No items selected")
                return
            
            current_form_row=1
            tkinter.Label(self.frame, text='Selected Items').grid(columnspan=2, row=current_form_row)
            current_form_row += current_form_row

            tkinter.Label(self.frame, text="Dataset ID", bd=10).grid(column=1, row=current_form_row)
            tkinter.Label(self.frame, text="Item ID", bd=10).grid(column=2, row=current_form_row)
            current_form_row += current_form_row

            for i in range(0, len(details), 2): #Loop through each dataset tuple
                item_ids=details[i + 1].split(",")
                tkinter.Label(self.frame, text=details[i], bd=10).grid(column=1, row=current_form_row,rowspan=len(item_ids))
                for x in item_ids:
                    tkinter.Label(self.frame, text=x, bd=10).grid(column=2, row=current_form_row)
                    current_form_row += current_form_row

        except Exception as e:
            self.log.fatal("Error creating form: %s", e, exc_info=1)

        

    def close(self):
        # Terminate Tkinter event loop
        self.quit()
        # Destroy all Tkinter widgets
        self.destroy()

    def show(self):
        # Move in front of all other windows on the display
        self.lift()
        # We MUST always enter the event loop to start accepting UI events
        self.mainloop()
        # Now SIS is becomes unresponsive until the UI window has been closed
