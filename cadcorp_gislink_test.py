import gislink
import logging
from pathlib import Path

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

            # Add SIS Ribbon controls
            btn = gislink.RibbonButton('Test Gislink')
            btn.help = 'Prints to the log'
            btn.description = 'Please print.'
            btn.min_selection = -1  # Disable button if no SWD is present
            btn.min_status = 1  # visible
            btn.enabled = True
            btn.default_command = True
            btn.click.add_handler(self.on_click_print)
            self.application.ribbon_group.add_control(btn)
        except Exception as e:
            self.log.fatal("Error initialising Gislink %s", e)

    def on_click_print(self, event):
        self.log.debug("You clicked me")


