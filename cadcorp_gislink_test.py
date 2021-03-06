import gislink
import logging
from pathlib import Path
from cadcorp_gislink_form import ModalForm

cadcorp_version = '0.1'
cadcorp_vendor = 'West Yorkshire Police'

filename = Path(__file__)
logging.basicConfig(filename=filename.with_suffix(".log"), level=logging.DEBUG)
logging.debug("Logging Activated")

class Cadcorp_Gislink_Test(gislink.Program):
    def __init__(self):
        try:
            self.log = logging.getLogger(__name__)
            app_name = "Test GisLink App"
            super().__init__(name=app_name)

            # respond to every changed selection
            self.application.add_trigger(
                "SelectionChange", self.on_selection_changed)

        except Exception as e:
            self.log.fatal("Error initialising Gislink %s", e)

    def on_selection_changed(self, event):
        self.log.debug("Selection Changed:")
        try:
            self.log.debug("Let's open that form")
            # https://community.cadcorp.com/t/example-python-scripts-with-a-gui/1019/9
            # Takeover will prevent interactions with SIS desktop,
            # forcing modal mode
            with self.application.takeover_desktop() as desktop:
                form = ModalForm(self.name, desktop)
                form.show()  # will wait until the form is closed
            self.log.debug("Form is closed")

        except Exception as e:
            self.log.error("Error on Selection Change: %s", e)