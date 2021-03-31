from typing import Any, Callable, List, Tuple, TypeVar
from ctypes import c_void_p

_T = TypeVar("_T")
HWND = c_void_p

cadcorp_version: str
"""Global property to specify version of Cadcorp GisLink add-in program."""

cadcorp_vendor: str
"""Global property to specify vendor name of Cadcorp GisLink add-in program."""


class Application(object):
    def add_trigger(self, event: str, handler: Callable) -> None:
        """Registers a trigger handler for named command event.

        event
            Name of command event to register to fires the trigger.
        handler
            Callable object or function executed as the trigger handler.
        """
        pass

    def remove_trigger(self, event: str, handler: Callable) -> None:
        """Removes a trigger handler registered for named command event.

        event
            Name of command event registered to fire the trigger.
        handler
            Callable object or function registered to be executed as
            the trigger handler.
        """
        pass

    def takeover_desktop(self) -> Product:  # noqa: F821
        """Obtains access to SIS Desktop"""
        pass

    @property
    def context_menu(self) -> ContextMenu:  # noqa: F821
        """Returns SIS context menu"""
        pass

    @property
    def product_type(self) -> int:
        """Returns SIS product type"""
        pass

    @property
    def ribbon_group(self) -> RibbonGroup:  # noqa: F821
        """Returns SIS ribbon group"""
        pass


class ClickEvent(object):
    def add_handler(self, handler: Callable) -> None:
        """Registers a handler for click event.

        handler
            Callable object or function
        """
        pass

    def remove_handler(self, handler: Callable) -> None:
        """Removes a handler registered for click event.

        handler
            Callable object or function
        """
        pass


class ClickArguments(object):
    @property
    def desktop(self) -> Desktop:  # noqa: F821
        """Returns SIS Desktop product"""
        pass

    @property
    def window(self) -> HWND:
        """Returns SIS window handle"""
        pass

    @property
    def tag(self) -> str:
        """Returns SIS handler tag"""
        pass


class TriggerArguments(ClickArguments):
    @property
    def trigger(self) -> str:
        """Returns name of registered trigger"""
        pass


class Menu(object):
    @property
    def context_menu(self) -> ContextMenu:  # noqa: F821
        """Get context menu"""
        pass

    @property
    def items(self) -> MenuItemCollection:  # noqa: F821
        """Checks if this is top-level menu"""
        pass

    @property
    def is_parent(self) -> bool:
        """Get menu items"""
        pass


class ContextMenu(Menu):
    def __init__(self, text: str = None) -> None: ...

    @property
    def application(self) -> Application:
        """Application object"""
        pass


class MenuItem(object):
    def __init__(self, text: str = None) -> None: ...

    def on_click(self, args: ClickArguments) -> None:
        """Click event handler"""
        pass

    @property
    def checked(self) -> bool:
        """Show a tick against the menu item."""
        pass

    @checked.setter
    def checked(self, value: bool) -> None:
        """Show a tick against the menu item."""
        pass

    @property
    def class_name(self) -> str:
        """The class or group name this command is to be associated with.
        If set to 'Item' or '' then the command will be available for all
        item classes.
        """
        pass

    @class_name.setter
    def class_name(self, value: str) -> None:
        """The class or group name this command is to be associated with.
        If set to 'Item' or '' then the command will be available for all
        item classes.
        """
        pass

    @property
    def click(self) -> ClickEvent:
        """Click event handler"""
        pass

    @property
    def enabled(self) -> bool:
        """Tells whether the Ribbon menu item is shown enabled or disabled."""
        pass

    @enabled.setter
    def enabled(self, value: bool) -> None:
        """Tells whether the Ribbon menu item is shown enabled or disabled."""
        pass

    @property
    def filter(self) -> str:
        """Name of filter which all selected items must pass for the command
        to be available.
        """
        pass

    @filter.setter
    def filter(self, value: str) -> None:
        """Name of filter which all selected items must pass for the command
        to be available.
        """
        pass

    @property
    def help(self) -> str:
        """Help text"""
        pass

    @help.setter
    def help(self, value: str) -> None:
        """Help text"""
        pass

    @property
    def image(self) -> str:
        """Name or path of the icon to use for the menu item."""
        pass

    @image.setter
    def image(self, value: str) -> None:
        """Name or path of the icon to use for the menu item."""
        pass

    @property
    def index(self) -> int:
        """Returns index of item if it belongs to menu, otherwise -1"""
        pass

    @property
    def locus(self) -> str:
        """Name of spatial filter which all selected items must pass
        for the command to be available.
        """
        pass

    @locus.setter
    def locus(self, value: str) -> None:
        """Name of spatial filter which all selected items must pass
        for the command to be available.
        """
        pass

    @property
    def max_selection(self) -> int:
        """The maximum number of Items which may be selected to make this
        command valid."""
        pass

    @max_selection.setter
    def max_selection(self, value: int) -> None:
        """The maximum number of Items which may be selected to make this
        command valid."""
        pass

    @property
    def min_selection(self) -> int:
        """The minimum number of Items which must be selected to make this
        command valid."""
        pass

    @min_selection.setter
    def min_selection(self, value: int) -> None:
        """The minimum number of Items which must be selected to make this
        command valid."""
        pass

    @property
    def min_status(self) -> int:
        """The minimum status of the item, i.e. SIS_HITTABLE."""
        pass

    @min_status.setter
    def min_status(self, value: int) -> None:
        """The minimum status of the item, i.e. SIS_HITTABLE."""
        pass

    @property
    def parent(self) -> Menu:
        """Parent menu"""
        pass

    @property
    def text(self) -> str:
        """Label text"""
        pass

    @text.setter
    def text(self, value: str) -> None:
        """Label text"""
        pass


class MenuItemCollection(List):
    def append(self, menu_item: MenuItem) -> None:
        """Add menu item to the Ribbon menu.

        menu_item
            MenuItem object to add to the menu.
        """
        pass

    def insert(self, index: int, menu_item: MenuItem) -> None:
        """Insert control to Ribbon control collection.

        index
            Position at which to insert the item.
        menu_item
            MenuItem object to insert to the menu.
        """
        pass


class Program(object):
    def __init__(self, name: str) -> None: ...

    @property
    def application(self) -> Application:
        """Application object"""
        pass

    @property
    def name(self) -> str:
        """Program name"""
        pass


class Product(object):
    def __enter__(self: _T) -> _T:
        """Enter the runtime context related to Product object"""
        pass

    def __exit__(self) -> None:
        """Exit the runtime context related to Product object"""
        pass

    def do(self, class_name: str, *args: Any, type_suffixes: Tuple[str]) -> int:  # noqa: E501
        """Executes SIS product routine.

        class_name
            Name of GisLink class
            Values for the GisLink class arguments in order of the
            corresponding type suffixes.
        type_suffixes
            Tuple with suffixes of the GisLink class arguments types:
            '$' string, '&' integer, '#' float, '@' any object.
        """
        pass

    def evaluate(self, class_name: str, *args: Any, type_suffixes: Tuple[str]) -> int:  # noqa: E501
        """Executes SIS product function.

        class_name
            Name of GisLink class
            Values for the GisLink class arguments in order of the
            corresponding type suffixes.
        type_suffixes
            Tuple with suffixes of the GisLink class arguments types:
            '$' string, '&' integer, '#' float, '@' any object.
        """
        pass

    def release(self) -> None:
        """Releases SIS product."""
        pass

    def GetPos(self) -> List[float, float, float]:
        """Gets a position from the user and returns whether a position
        has been snapped"""
        pass

    def GetPosEx(self) -> List[int, float, float, float]:
        """Gets a position from the user and returns whether a position
        has been snapped"""
        pass


class RibbonControl(object):
    @property
    def parent_control(self) -> RibbonControl:  # noqa: F821
        """Returns parent of the control"""
        pass

    @property
    def ribbon_group(self) -> RibbonGroup:  # noqa: F821
        """Returns SIS ribbon group of the control"""
        pass

    @property
    def tag(self) -> str:
        """Tag of the Ribbon control"""
        pass

    @tag.setter
    def tag(self, value: str) -> None:
        """Tag of the Ribbon control"""
        pass

    @property
    def visible(self) -> bool:
        """Visibility of the Ribbon control"""
        pass

    @visible.setter
    def visible(self) -> None:
        """Visibility of the Ribbon control"""
        pass


class RibbonControlCollection(List):
    def append(self, control: RibbonControl) -> None:
        """Add control to Ribbon controls collection.

        control
            Control object to add to the collection.
        """
        pass

    def insert(self, index: int, control: RibbonControl) -> None:
        """Insert control to Ribbon control collection.

        index
            Position at which to insert the control.
        control
            Control object to insert to the collection.
        """
        pass


class RibbonButton(RibbonControl):
    def __init__(self, name: str = None, description: str = None, help: str = None) -> None: ...  # noqa: E501

    def on_click(self, args: ClickArguments) -> None:
        """Click event handler"""
        pass

    @property
    def always_large_image(self) -> bool:
        """Enables or disables transition to collapsed state displaying
        small images."""
        pass

    @always_large_image.setter
    def always_large_image(self, value: bool) -> None:
        """Enables or disables transition to collapsed state displaying
        small images."""
        pass

    @property
    def class_name(self) -> str:
        """The class or group name this command is to be associated with.
        If set to 'Item' or '' then the command will be available for
        all item classes.
        """
        pass

    @class_name.setter
    def class_name(self, value: str) -> None:
        """The class or group name this command is to be associated with.
        If set to 'Item' or '' then the command will be available for
        all item classes.
        """
        pass

    @property
    def click(self) -> ClickEvent:
        """Click event handler"""
        pass

    @property
    def default_command(self) -> bool:
        """Boolean that tells the button that it can execute its
        default command.
        """
        pass

    @default_command.setter
    def default_command(self, value: bool) -> None:
        """Boolean that tells the button that it can execute its
        default command.
        """
        pass

    @property
    def description(self) -> str:
        """Description text"""
        pass

    @description.setter
    def description(self, value: str) -> None:
        """Description text"""
        pass

    @property
    def enabled(self) -> bool:
        """Tells whether the Ribbon button is shown enabled or disabled."""
        pass

    @enabled.setter
    def enabled(self, value: bool) -> None:
        """Tells whether the Ribbon button is shown enabled or disabled."""
        pass

    @property
    def filter(self) -> str:
        """Name of filter which all selected items must pass for the command
        to be available.
        """
        pass

    @filter.setter
    def filter(self, value: str) -> None:
        """Name of filter which all selected items must pass for the command
        to be available.
        """
        pass

    @property
    def help(self) -> str:
        """Help text"""
        pass

    @help.setter
    def help(self, value: str) -> None:
        """Help text"""
        pass

    @property
    def icon(self) -> str:
        """Name or path of the icon to use for the Ribbon button."""
        pass

    @icon.setter
    def icon(self, value: str) -> None:
        """Name or path of the icon to use for the Ribbon button."""
        pass

    @property
    def id(self) -> int:
        """Identifier for the Ribbon checkbox (unsigned integer)."""
        pass

    @id.setter
    def id(self, value: int) -> None:
        """Identifier for the Ribbon button (unsigned integer)."""
        pass

    @property
    def large_image(self) -> bool:
        """Identifier for the Ribbon button (unsigned integer)."""
        pass

    @large_image.setter
    def large_image(self, value: bool) -> None:
        """Name of the large image."""
        pass

    @property
    def locus(self) -> str:
        """Name of spatial filter which all selected items must pass
        for the command to be available."""
        pass

    @locus.setter
    def locus(self, value: str) -> None:
        """Name of spatial filter which all selected items must pass
        for the command to be available."""
        pass

    @property
    def max_selection(self) -> int:
        """The maximum number of Items which may be selected to make
        this command valid."""
        pass

    @max_selection.setter
    def max_selection(self, value: int) -> None:
        """The maximum number of Items which may be selected to make
        this command valid."""
        pass

    @property
    def min_selection(self) -> int:
        """The minimum number of Items which must be selected to make
        this command valid."""
        pass

    @min_selection.setter
    def min_selection(self, value: int) -> None:
        """The minimum number of Items which must be selected to make
        this command valid."""
        pass

    @property
    def min_status(self) -> int:
        """The minimum status of the item, i.e. SIS_HITTABLE."""
        pass

    @min_status.setter
    def min_status(self, value: int) -> None:
        """The minimum status of the item, i.e. SIS_HITTABLE."""
        pass

    @property
    def selected(self) -> bool:
        """Sets the button to a Selected or Highlighted state"""
        pass

    @selected.setter
    def selected(self, value: bool) -> None:
        """Sets the button to a Selected or Highlighted state"""
        pass

    @property
    def subitems(self) -> List[RibbonControl]:
        """Items of popup menu assigned to the Ribbon button"""
        pass

    @property
    def shortcutkeys(self) -> str:
        """Shortcut keys"""
        pass

    @shortcutkeys.setter
    def shortcutkeys(self, value: str) -> None:
        """Shortcut keys"""
        pass

    @property
    def shortcutmenukeys(self) -> str:
        """Shortcut keys"""
        pass

    @shortcutmenukeys.setter
    def shortcutmenukeys(self, value: str) -> None:
        """Shortcut keys"""
        pass

    @property
    def text(self) -> str:
        """Label text"""
        pass

    @text.setter
    def text(self, value: str) -> None:
        """Label text"""
        pass


class RibbonCheckBox(RibbonControl):
    def __init__(self, name: str = None, description: str = None, help: str = None) -> None: ...  # noqa: E501

    def on_click(self, args: ClickArguments) -> None:
        """Click event handler"""
        pass

    @property
    def checked(self) -> bool:
        """Tells whether the Ribbon checkbox is shown checked or unchecked."""
        pass

    @checked.setter
    def checked(self, value: bool) -> None:
        """Tells whether the Ribbon checkbox is shown checked or unchecked."""
        pass

    @property
    def class_name(self) -> str:
        """The class or group name this command is to be associated with.
        If set to 'Item' or '' then the command will be available for all
        item classes.
        """
        pass

    @class_name.setter
    def class_name(self, value: str) -> None:
        """The class or group name this command is to be associated with.
        If set to 'Item' or '' then the command will be available for all
        item classes.
        """
        pass

    @property
    def click(self) -> ClickEvent:
        """Click event handler"""
        pass

    @property
    def description(self) -> str:
        """Description text"""
        pass

    @description.setter
    def description(self, value: str) -> None:
        """Description text"""
        pass

    @property
    def enabled(self) -> bool:
        """Tells whether the Ribbon checkbox is shown enabled or disabled."""
        pass

    @enabled.setter
    def enabled(self, value: bool) -> None:
        """Tells whether the Ribbon checkbox is shown enabled or disabled."""
        pass

    @property
    def filter(self) -> str:
        """Name of filter which all selected items must pass for the command
        to be available."""
        pass

    @filter.setter
    def filter(self, value: str) -> None:
        """Name of filter which all selected items must pass for the command
        to be available."""
        pass

    @property
    def help(self) -> str:
        """Help text"""
        pass

    @help.setter
    def help(self, value: str) -> None:
        """Help text"""
        pass

    @property
    def id(self) -> int:
        """Identifier for the Ribbon checkbox (unsigned integer)."""
        pass

    @id.setter
    def id(self, value: int) -> None:
        """Identifier for the Ribbon checkbox (unsigned integer)."""
        pass

    @property
    def locus(self) -> str:
        """Name of spatial filter which all selected items must pass for
        the command to be available."""
        pass

    @locus.setter
    def locus(self, value: str) -> None:
        """Name of spatial filter which all selected items must pass for
        the command to be available."""
        pass

    @property
    def max_selection(self) -> int:
        """The maximum number of Items which may be selected to make this
        command valid."""
        pass

    @max_selection.setter
    def max_selection(self, value: int) -> None:
        """The maximum number of Items which may be selected to make this
        command valid."""
        pass

    @property
    def min_selection(self) -> int:
        """The minimum number of Items which must be selected to make this
        command valid."""
        pass

    @min_selection.setter
    def min_selection(self, value: int) -> None:
        """The minimum number of Items which must be selected to make this
        command valid."""
        pass

    @property
    def min_status(self) -> int:
        """The minimum status of the item, i.e. SIS_HITTABLE."""
        pass

    @min_status.setter
    def min_status(self, value: int) -> None:
        """The minimum status of the item, i.e. SIS_HITTABLE."""
        pass

    @property
    def shortcutkeys(self) -> str:
        """Shortcut keys"""
        pass

    @shortcutkeys.setter
    def shortcutkeys(self, value: str) -> None:
        """Shortcut keys"""
        pass

    @property
    def text(self) -> str:
        """Label text"""
        pass

    @text.setter
    def text(self, value: str) -> None:
        """Label text"""
        pass


class RibbonLabel(RibbonControl):
    def __init__(self, name: str = None, description: str = None, help: str = None) -> None: ...  # noqa: E501

    @property
    def description(self) -> str:
        """Description text"""
        pass

    @description.setter
    def description(self, value: str) -> None:
        """Description text"""
        pass

    @property
    def help(self) -> str:
        """Help text"""
        pass

    @help.setter
    def help(self, value: str) -> None:
        """Help text"""
        pass

    @property
    def text(self) -> str:
        """Label text"""
        pass

    @text.setter
    def text(self, value: str) -> None:
        """Label text"""
        pass


class RibbonLaunchButton(RibbonControl):
    def __init__(self, description: str = None, help: str = None) -> None: ...  # noqa: E501

    def on_click(self, args: ClickArguments) -> None:
        """Click event handler"""
        pass

    @property
    def click(self) -> ClickEvent:
        """Click event handler"""
        pass

    @property
    def description(self) -> str:
        """Description text"""
        pass

    @description.setter
    def description(self, value: str) -> None:
        """Description text"""
        pass

    @property
    def enabled(self) -> bool:
        """Tells whether the Ribbon button is shown enabled or disabled."""
        pass

    @enabled.setter
    def enabled(self, value: bool) -> None:
        """Tells whether the Ribbon button is shown enabled or disabled."""
        pass

    @property
    def help(self) -> str:
        """Help text"""
        pass

    @help.setter
    def help(self, value: str) -> None:
        """Help text"""
        pass

    @property
    def id(self) -> int:
        """Identifier for the Ribbon checkbox (unsigned integer)."""
        pass

    @id.setter
    def id(self, value: int) -> None:
        """Identifier for the Ribbon checkbox (unsigned integer)."""
        pass

    @property
    def shortcutkeys(self) -> str:
        """Shortcut keys"""
        pass

    @shortcutkeys.setter
    def shortcutkeys(self, value: str) -> None:
        """Shortcut keys"""
        pass


class RibbonSeparator(RibbonControl):
    pass


class RibbonGroup(object):
    def add_control(self, control: RibbonControl) -> None:
        """Add control to program Ribbon group in SIS.

        control
            Control object to add to the Ribbon group.
        """
        pass

    @property
    def application(self) -> Application:
        """Application object"""
        pass

    @property
    def center_columns_vertically(self) -> bool:
        """Vertical alignment of Ribbon group elements."""
        pass

    @center_columns_vertically.setter
    def center_columns_vertically(self, value: bool) -> None:
        """Vertical alignment of Ribbon group elements."""
        pass

    @property
    def icon(self) -> str:
        """Name or path of the icon to use for the Ribbon group."""
        pass

    @icon.setter
    def icon(self, value: str) -> None:
        """Name or path of the icon to use for the Ribbon group."""
        pass

    @property
    def launch_button(self) -> str:
        """Launch button object."""
        pass

    @launch_button.setter
    def launch_button(self, value: RibbonLaunchButton) -> None:  # noqa: E501, F821
        """Launch button object."""
        pass

    @property
    def text(self) -> str:
        """Label text"""
        pass

    @text.setter
    def text(self, value: str) -> None:
        """Label text"""
        pass


class Desktop(Product):
    def AddToList(self, list: str) -> int:
        """
        Adds the current open item to a Named List. If the Named List does not
        exist, it will be created

        Parameters:
            list: str
                The Named List to which to add the current open item
        """
        pass

    def BeginDatasetTransaction(self, nDataset: int) -> int:
        """
        Begin a transaction on a spatial database dataset opened with a
        dynamic connection type

        Parameters:
            nDataset: int
                The serial number of the dataset for which a transaction is
                to be started
        """
        pass

    def BezierTo(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, x3: float, y3: float, z3: float) -> int:  # noqa: E501
        """
        Draws a Bezier curve from the current drawing position.  The curve is
        appended to the current LineString item sequence, started by the last
        MoveTo, and extended using BulgeTo, LineTo, or this method

        Parameters:
            x1: float
                The x position of the first Bezier control point
            y1: float
                The y position of the first Bezier control point
            z1: float
                The z position of the first Bezier control point
            x2: float
                The x position of the second Bezier control point
            y2: float
                The y position of the second Bezier control point
            z2: float
                The z position of the second Bezier control point
            x3: float
                The x position of the end point of the Bezier curve
            y3: float
                The y position of the end point of the Bezier curve
            z3: float
                The z position of the end point of the Bezier curve
        """
        pass

    def BulgeTo(self, angle: float, x: float, y: float) -> int:
        """
        Draws an arc from the current drawing position, through an angle, to
        an end point.The arc is appended to the current LineString sequence,
        started by the last MoveTo, and extended using BezierTo, LineTo, or
        this method

        Parameters:
            angle: float
                The arc angle in radians
            x: float
                The x coordinate of the end point
            y: float
                The y coordinate of the end point
        """
        pass

    def ChangeFeatureFilter(self, filter: str, fcode: int, flag: int) -> int:
        """
        Include or exclude a feature code from a named Feature Filter

        Parameters:
            filter: str
                The named Feature Filter to edit, previously created using
                CreateFeatureFilter
            fcode: int
                The feature code whose information is to be changed, from 0 to
                65535. Use 0 to specify all feature codes in the Feature
                Filter
            flag: int

        """
        pass

    def ChangeLocusTestMode(self, locus: str, geomTest: int, geomMode: int) -> int:  # noqa: E501
        """
        Modifies the testing mode of a named Locus

        Parameters:
            locus: str
                The named Locus whose test mode is to be modified
            geomTest: int
                The geometry test to use
            geomMode: int
                The geometry mode to use
        """
        pass

    def ChangePrjUnits(self, crsOut: str, crsIn: str, mode: int, dSize: float) -> int:  # noqa: E501
        """
        Copies a named Transverse Mercator CRS changing the units as a new
        named CRS in a Named Object Library, replacing any existing CRS with
        the same name

        Parameters:
            crsOut: str
                The named CRS to create, or replace
            crsIn: str
                The named CRS to copy
            mode: int
                The units of dSize. This parameter must be set to 0, which
                means that dSize is specified in metres
            dSize: float
                The size of one CRS unit
        """
        pass

    def ChangeValueListFilter(self, filter: str, flag: int, listval: str) -> int:  # noqa: E501
        """
        Include or exclude a list of values from a Value-list Filter

        Parameters:
            filter: str
                The named Value-list Filter to change, previously created
                using CreateValueListFilter
            flag: int

            listval: str
                A space-, comma-, tab- or newline-separated list of values to
                add or remove
        """
        pass

    def CleanLines(self, list: str, tolerance: float, options: int) -> int:
        """
        Cleans up LineString Items, removing repeated vertices etc

        Parameters:
            list: str
                The Named List containing the LineString Items to be cleaned.
                On completion, the named list will contain all the remaining
                LineString items
            tolerance: float
                The tolerance to use. LineString segments whose length is less
                than the tolerance value will be removed. Specify 0.0 to
                prevent deleting vertices which are close together
            options: int

        """
        pass

    def CloseCursor(self, cursor: str) -> int:
        """
        Closes a named cursor

        Parameters:
            cursor: str
                The cursor to close
        """
        pass

    def CloseDataset(self, filename: str) -> int:
        """
        Close a dataset

        Parameters:
            filename: str
                The dataset to close
        """
        pass

    def CloseIndexDatasetTile(self, nDataset: int, tilename: str) -> int:
        """
        Closes a named dataset tile within an index dataset

        Parameters:
            nDataset: int
                The serial number of the index dataset. The serial number can
                be obtained from the Dataset property of an overlay, or from
                the GetDataset, GetDatasetContainer or FindExternalDataset
                methods
            tilename: str
                The tile to close
        """
        pass

    def CloseItem(self) -> int:
        """
        Closes the current open item, stopping it being current
        """
        pass

    def CombineFilter(self, filterOutput: str, filter1: str, filter2: str, mode: int) -> int:  # noqa: E501
        """
        Creates a named Compound Filter in a Named Object Library by combining
        two named Filter objects using a Boolean operation, replacing any
        existing Filter with the same name

        Parameters:
            filterOutput: str
                The named Filter to create, or replace (see Remarks)
            filter1: str
                The first Filter to combine, or an empty string (see Remarks)
            filter2: str
                The second Filter to combine, or an empty string (see
                Remarks)
            mode: int
                The Boolean operation to use
        """
        pass

    def CombineLists(self, listOutput: str, list1: str, list2: str, mode: int) -> int:  # noqa: E501
        """
        Combines two Named Lists using a Boolean operation, returning the
        answer in a third Named List

        Parameters:
            listOutput: str
                The Named List resulting from the Boolean operation
            list1: str
                The first Named List to combine
            list2: str
                The second Named List to combine
            mode: int
                The Boolean operation to use
        """
        pass

    def CombineLocus(self, locusOutput: str, locus1: str, locus2: str, mode: int) -> int:  # noqa: E501
        """
        Creates a named Locus in a Named Object Library by combining two named
        Locus objects using a Boolean operation, replacing any existing Locus
        with the same name

        Parameters:
            locusOutput: str
                The named Locus to create, or replace (see Remarks)
            locus1: str
                The first Locus to combine, or an empty string (see Remarks)
            locus2: str
                The second Locus to combine, or an empty string (see Remarks)
            mode: int
                The Boolean operation to use
        """
        pass

    def CommitDatasetTransaction(self, nDataset: int) -> int:
        """
        Ends a transaction, committing to the database the changes made inside
        the transaction

        Parameters:
            nDataset: int
                The serial number of the dataset for which the transaction is
                to be committed. The serial number can be obtained from the
                Dataset property of an overlay, or from the GetDataset,
                GetDatasetContainer or FindExternalDataset methods
        """
        pass

    def CompactDataset(self, nDataset: int) -> int:
        """
        Discards all undo actions and defragments the memory used by an
        internal dataset

        Parameters:
            nDataset: int
                The serial number of the dataset to be compacted. The serial
                number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
        """
        pass

    def ComposeEx(self, name: str) -> int:
        """
        Composes the current window, in preparation for using
        PlacePrintTemplate or CreatePhoto on another window

        Parameters:
            name: str
                The name of the composition
        """
        pass

    def Compose(self) -> int:
        """
        Composes the current window, in preparation for using
        PlacePrintTemplate or CreatePhoto on another window
        """
        pass

    def ConnectGps(self, port: str, baudrate: int, databits: int, parity: int, stopbits: int, flags: int) -> int:  # noqa: E501
        """
        Establishes a connection with the GPS device attached to the computer.
        Cadcorp SIS starts reading the input immediately

        Parameters:
            port: str
                The name of the port on which the GPS device is attached.
                Should be "COMx", where x is in the range 1 to 255 inclusive
            baudrate: int
                The baudrate (bits/second) at which Cadcorp SIS will
                communicate with the GPS device
            databits: int
                The databit setting to be used in the communication with this
                GPS device
            parity: int
                The parity setting to be used in the communication with this
                GPS device.The possible settings are
            stopbits: int
                The number of stop bits to be used in the communication with
                this GPS device.The possible settings are
            flags: int
                Flags setting the NMEA options for receiving data from the GPS
                device. There are three NMEA sentences of interest
        """
        pass

    def CopyFeatureCode(self, fcodeTo: int, fcodeFrom: int, ftable: str) -> int:  # noqa: E501
        """
        Copies an existing feature code into the currently loaded Feature
        Table. Use LoadFeatureTable to load a Feature Table for editing

        Parameters:
            fcodeTo: int
                The feature code to be added, from 1 to 65535
            fcodeFrom: int
                The feature code to be copied, from 1 to 65535
            ftable: str
                The Feature Table from which to copy the feature code. Use ""
                to copy a feature code in the currently loaded Feature Table
        """
        pass

    def CopyListItems(self, list: str) -> int:
        """
        Copies the Items in a Named List to the default overlay

        Parameters:
            list: str
                The Named List whose Items are to be copied
        """
        pass

    def CopyNolObject(self, fromPos: int, toPos: int, aclass: str, name: str) -> int:  # noqa: E501
        """
        Copies a named object between Named Object Libraries (NOLs)

        Parameters:
            fromPos: int
                The position in the list of NOLs of the NOL containing the
                named object to be copied
            toPos: int
                The destination position in the list of NOLs of the NOL of the
                named object to be copied
            aclass: str
                The class of named object to be copied. See Named Object
                Library Classes for valid classes
            name: str
                The named object to copy
        """
        pass

    def CopyThemeComponent(self, componentTo: int, componentFrom: int, theme: str) -> int:  # noqa: E501
        """
        Copies an existing Theme component into the currently loaded Theme.
        Use LoadTheme to load a Theme for editing

        Parameters:
            componentTo: int
                The component to copy into
            componentFrom: int
                The component to copy from
            theme: str
                The Theme from which to copy the component. Use "" to copy a
                component in the currently loaded Theme
        """
        pass

    def CreateAreaFromLines(self, list: str, bDelete: int, createOption: int) -> int:  # noqa: E501
        """
        Creates one or more Polygon item(s) from the LineString item(s) in a
        Named List, using the creation option, optionally deleting the
        LineString item(s) after creating the Polygon item(s)

        Parameters:
            list: str
                The Named List containing the LineString items to be used in
                the Polygon item creation. If the method succeeds, the named
                list will contain the Polygon items created
            bDelete: int

            createOption: int

        """
        pass

    def CreateAspectGrid(self, list: str, resolution: float) -> int:
        """
        Creates an 'Aspect' Grid from the currently open TIN as angles
        measured from North

        Parameters:
            list: str
                The named list containing only TIN items for which the Aspect
                Grid will be created
            resolution: float
                The resolution or cell size at which the grid will be created
        """
        pass

    def CreateAssembly(self, list: str, x: float, y: float, z: float, shape: str, a: float, s: float) -> int:  # noqa: E501
        """
        Creates an Assembly item from the items in a Named List

        Parameters:
            list: str
                The Named List containing the Items to be added to the
                Assembly
            x: float
                The x position of the Assembly
            y: float
                The y position of the Assembly
            z: float
                The z position of the Assembly
            shape: str
                The shape of the Assembly
            a: float
                The angle, in radians, of the Assembly
            s: float
                The scale of the Assembly
        """
        pass

    def CreateBackdropOverlay(self, pos: int, backdrop: str) -> int:
        """
        Creates a new overlay which uses a named Item as a backdrop

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            backdrop: str
                The named Item to use as a backdrop
        """
        pass

    def CreateBarTheme(self, nBlocks: int) -> int:
        """
        Creates a new Bar Charts Theme. After editing the Theme properties,
        use StoreTheme to save the Theme in a Named Object Library

        Parameters:
            nBlocks: int
                The number of blocks in the Bar Charts Theme, in the range 1
                to 256
        """
        pass

    def CreateBds(self, filename: str) -> int:
        """
        Creates an empty Cadcorp Base Dataset (BDS) file. This call will fail
        if the BDS file already exists

        Parameters:
            filename: str
                The name of the new BDS file. The new dataset is created in
                the current attached directory, unless a full path name is
                given. The new dataset can be added to the current SIS
                Workspace Definition (SWD) using InsertDataset
        """
        pass

    def CreateBitmap(self, filename: str, x1: float, y1: float, x2: float, y2: float, bLinked: int, bStretch: int) -> int:  # noqa: E501
        """
        Creates a Bitmap item

        Parameters:
            filename: str
                The name of the bitmap to be opened
            x1: float
                The extents within which the Bitmap item will be placed
            y1: float
                The extents within which the Bitmap item will be placed
            x2: float
                The extents within which the Bitmap item will be placed
            y2: float
                The extents within which the Bitmap item will be placed
            bLinked: int

            bStretch: int

        """
        pass

    def CreateBitmapFromImage(self, w: int, h: int) -> int:
        """

        Parameters:
            w: int

            h: int

        """
        pass

    def CreateBlock(self, list: str, blk: str, x: float, y: float, z: float) -> int:  # noqa: E501
        """
        Creates a named Block in a Named Object Library from the Items in a
        Named List, replacing any existing Block with the same name

        Parameters:
            list: str
                The Named List containing the Items to be inserted into the
                Block
            blk: str
                The named Block to create, or replace
            x: float
                The origin of the Block
            y: float
                The origin of the Block
            z: float
                The origin of the Block
        """
        pass

    def CreateBoolean(self, list: str, boolop: int) -> int:
        """
        Creates a new Item by combining existing Items.This method can combine
        most types of Item. The type of Item created is dependent on the
        type(s) of the Items being combined.If a Group is open, then graphics
        are added to the Group, otherwise a new Item is created

        Parameters:
            list: str
                The Named List containing the Items to be combined
            boolop: int

        """
        pass

    def CreateBoundary(self) -> int:
        """
        Creates an Item from the boundary of the current open Item
        """
        pass

    def CreateBoxLabel(self, x1: float, y1: float, z1: float, h: float, text: str, x2: float, y2: float, z2: float) -> int:  # noqa: E501
        """
        Creates a Label item, which has a line pointing to a labelled
        location. Label text is similar to box text, as it is created in real
        world units, and when printed maintains its actual proportions to the
        surrounding graphics. This method respects the axes angle setting.
        This means that the x, y and z values are interpreted within the aces
        and all new items created will align to the axes angle

        Parameters:
            x1: float
                The x position of the alignment point of the Label item
            y1: float
                The y position of the alignment point of the Label item
            z1: float
                The z position of the alignment point of the Label item
            h: float
                The height in metres of the Label item
            text: str
                The text of the Label item
            x2: float
                The x position to draw the label pointer line to
            y2: float
                The y position to draw the label pointer line to
            z2: float
                The z position to draw the label pointer line to
        """
        pass

    def CreateBoxText(self, x: float, y: float, z: float, h: float, text: str) -> int:  # noqa: E501
        """
        Creates a BoxText item in real world units

        Parameters:
            x: float
                The x position of the alignment point of the BoxText item
            y: float
                The y position of the alignment point of the BoxText item
            z: float
                The z position of the alignment point of the BoxText item
            h: float
                The height in metres of the BoxText item
            text: str
                The text of the BoxText item
        """
        pass

    def CreateBufferFromItems(self, list: str, radius: float, resolution: float) -> int:  # noqa: E501
        """
        Creates a Polygon or QZone item surrounding the Items in a Named List

        Parameters:
            list: str
                The Named List containing the Items around which the Polygon
                or QZone will be created
            radius: float
                The buffer radius around each Item in list$
            resolution: float
                The resolution of the QZone. Use 0.0 for a smooth Polygon
                item, or a positive number for a QZone item
        """
        pass

    def CreateBufferLocusFromItems(self, list: str, bDelete: int, locus: str, radius: float, resolution: float) -> int:  # noqa: E501
        """
        Creates a named buffer Locus in Named Object Library surrounding Items
        in a Named List, replacing any existing Locus with the same name

        Parameters:
            list: str
                The Named List containing the items around which the Locus
                will be created
            bDelete: int

            locus: str
                The named Locus to create, or replace
            radius: float
                The buffer radius around each Item in the Named List
            resolution: float
                The resolution of the Locus. Use 0.0 for a smooth Polygon
                locus, or a positive number for a QZone locus
        """
        pass

    def CreateCircle(self, x: float, y: float, z: float, r: float) -> int:
        """
        Creates a circular Polygon item

        Parameters:
            x: float
                The x coordinate of the centre of the circle
            y: float
                The y coordinate of the centre of the circle
            z: float
                The z coordinate of the centre of the circle
            r: float
                The radius of the circle in metres
        """
        pass

    def CreateCircleLocus(self, locus: str, x: float, y: float, radius: float) -> int:  # noqa: E501
        """
        Creates a named circular Locus in a Named Object Library, replacing
        any existing Locus with the same name

        Parameters:
            locus: str
                The named Locus to create, or replace
            x: float
                The x coordinate centre of the circle Locus
            y: float
                The y coordinate centre of the circle Locus
            radius: float
                The radius of the circle Locus
        """
        pass

    def CreateClassTreeFilter(self, filter: str, formula: str) -> int:
        """
        Creates a named Class Filter in a Named Object Library, replacing any
        existing Filter with the same name

        Parameters:
            filter: str
                The named Filter to create or replace
            formula: str
                A class tree formula of the form "-Class +SubClass1 -SubClass2
                +SubClass3", eg "-Item +Line +Area" will match only LineString
                and Polygon Items, and their sub-classes
        """
        pass

    def CreateColumn(self, nDataset: int, nColumn: int) -> int:
        """

        Parameters:
            nDataset: int

            nColumn: int

        """
        pass

    def CreateColumnIndex(self, nDataset: int, column: str) -> int:
        """

        Parameters:
            nDataset: int

            column: str

        """
        pass

    def CreateCombinedFilter(self, filter: str) -> int:
        """
        Creates a named Combined Class/Property filter in a Named Object
        Library, replacing any existing Filter with the same name

        Parameters:
            filter: str
                The named Filter to create, or replace
        """
        pass

    def CreateComposition(self, name: str) -> int:
        """
        Creates a named composition based on the current open Photo item

        Parameters:
            name: str
                The name of the composition to be created
        """
        pass

    def CreateContourTheme(self, hMajor: float, hMinor: float) -> int:
        """
        Creates a new Contour Theme. After editing the Theme properties, use
        StoreTheme to save the Theme in a  Named Object Library

        Parameters:
            hMajor: float
                The height of the major contour
            hMinor: float
                The height of the minor contour
        """
        pass

    def CreateConvexHull(self) -> int:
        """
        Creates the smallest possible Item with convex geometry which contains
        the current open Item
        """
        pass

    def CreateDataSourceOverlay(self, pos: int, clsDataSource: str, parameters: str) -> int:  # noqa: E501
        """
        Inserts a dataset into the current SIS Workspace Definition (SWD),
        which will fetch data from non-file data source

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays, the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            clsDataSource: str
                The classname of the data source to use
            parameters: str
                Comma-separated optional parameters to configure the data
                source
        """
        pass

    def CreateDbBlobOverlay(self, pos: int, crs: str, rs: str, fmt: int, nfBlob: int, nfId: int, nfVer: int, nfSr: int, nfSlMin: int, nfSlMax: int, span: float) -> int:  # noqa: E501
        """
        Creates an overlay which views Blobs stored in a database

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            crs: str
                The named CRS of the stored Item Blobs
            rs: str
                A named recordset previously created using DefineRecordset
            fmt: int
                The format of the Item Blob strings
            nfBlob: int
                The index in the recordset columns argument of the Item Blob
                string column. This column must exist
            nfId: int
                The index in the recordset columns argument of the Item id
                column. A value of -1 will make Cadcorp SIS generate the Item
                id-s automatically
            nfVer: int
                The index in the recordset columns argument of the Item
                version column. A value of -1 indicates that no version
                information is being supplied
            nfSr: int
                The index in the recordset columns argument of the Item
                spatial reference column. A value of -1 indicates that no
                spatial reference is being supplied
            nfSlMin: int
                This parameter is currently ignored, please use -1 for future
                compatibility
            nfSlMax: int
                This parameter is currently ignored, please use -1 for future
                compatibility
            span: float
                The span used in the spatial reference (see
                GetSpatialReference)
        """
        pass

    def CreateDbOverlay(self, pos: int, unused: int, bTransact: int, connect: str, tableItem: str, crs: str, fmt: int, span: float) -> int:  # noqa: E501
        """
        Creates an overlay which stores editable Blobs in a database

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            unused: int

            bTransact: int

            connect: str
                The connect argument enables SIS to connect to the database
                containing the data to be mapped. The methods you can use to
                connect to a database are
            tableItem: str
                The name of the table containing Item information, ie Blob,
                spatial reference, etc. Many different tables may be used for
                different datasets within a single database
            crs: str
                The named CRS of the stored Item Blobs
            fmt: int
                The format of the Item Blob strings
            span: float
                The span used in the spatial reference (see
                GetSpatialReference)
        """
        pass

    def CreateDbPointOverlay(self, pos: int, crs: str, rs: str, aclass: str, nfX: int, nfY: int, nfId: int, nfSr: int, nfZ: int, nfUnused: int, span: float) -> int:  # noqa: E501
        """
        Creates an overlay which views Point data stored in a database

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            crs: str
                The named CRS of the stored Point coordinates
            rs: str
                A named recordset previously created using DefineRecordset
            aclass: str
                The class of Item to create
            nfX: int
                The index in the recordset columns argument of the x
                coordinate column. This column must exist
            nfY: int
                The index in the recordset columns argument of the y
                coordinate column. This column must exist
            nfId: int
                The index in the recordset columns argument of the Item id
                column. A value of -1 will make SIS generate the Item id-s
                automatically
            nfSr: int
                The index in the recordset columns argument of the Item
                spatial reference column. A value of -1 indicates that no
                spatial reference is being supplied
            nfZ: int
                The index in the recordset columns argument of the z
                coordinate column. A value of -1 indicates that points are 2D,
                and the Z values will be set to zero
            nfUnused: int
                This parameter is currently ignored, please use -1 for future
                compatibility
            span: float
                The span used in the spatial reference (see
                GetSpatialReference)
        """
        pass

    def CreateDbTableOverlay(self, pos: int, rs: str, nfId: int) -> int:
        """

        Parameters:
            pos: int

            rs: str

            nfId: int

        """
        pass

    def CreateDisplacement(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> int:  # noqa: E501
        """
        Creates a Displacement item, prior to doing a rubber sheet operation

        Parameters:
            x1: float
                The x position to displace from
            y1: float
                The y position to displace from
            z1: float
                The z position to displace from
            x2: float
                The x position to displace to
            y2: float
                The y position to displace to
            z2: float
                The z position to displace to
        """
        pass

    def CreateDotTheme(self, formula: str) -> int:
        """
        Creates a new Dot Density Theme. After editing the Theme properties,
        use StoreTheme to save the Theme in a Named Object Library

        Parameters:
            formula: str
                The formula to use for calculating dot densities. See Property
                Formula Syntax for details
        """
        pass

    def CreateDoubleBoolean(self, list1: str, boolop1: int, list2: str, boolop2: int, boolop3: int) -> int:  # noqa: E501
        """
        Executes a combination of Boolean operations

        Parameters:
            list1: str
                The Named List for the first Boolean operation
            boolop1: int
                The Boolean operator for the first Boolean operation
            list2: str
                The Named List for the second Boolean operation
            boolop2: int
                The Boolean operator for the second Boolean operation
            boolop3: int
                The Boolean operator for the third Boolean operation, which
                operates on the two Items resulting from the first two Boolean
                operations
        """
        pass

    def CreateDrapeBitmap(self, name: str) -> int:
        """
        Creates a named Bitmap item from the current view, which is suitable
        for draping in the 3D Window. This will be saved into the current
        Named Object Library

        Parameters:
            name: str
                The name of the Bitmap item to be created
        """
        pass

    def CreateEllipse(self, x1: float, y1: float, x2: float, y2: float) -> int:
        """
        Creates an elliptical Polygon item. This API method respects the axes
        angle setting. This means that the x, y and z values are interpreted
        within the axes and all new items created will align to the axes
        angle

        Parameters:
            x1: float
                The first x extent of the ellipse
            y1: float
                The first y extent of the ellipse
            x2: float
                The second x extent of the ellipse
            y2: float
                The second y extent of the ellipse
        """
        pass

    def CreateExtrudeTheme(self, formula: str) -> int:
        """
        Creates a new Extrude 2D items in 3D views Theme. After editing the
        Theme properties, use StoreTheme to save the Theme in a Named Object
        Library

        Parameters:
            formula: str
                The formula to use when evaluating the extrusion height. See
                Property Formula Syntax for details
        """
        pass

    def CreateExtrusion(self, height: float) -> int:
        """
        Creates a Surface item by extruding current open Polygon or LineString
        items

        Parameters:
            height: float
                The height to which to extrude the current open Polygon or
                LineString item (in metres)
        """
        pass

    def CreateFeatureFilter(self, filter: str, ftable: str) -> int:
        """
        Creates a named Feature Filter in a Named Object Library, based on a
        named Feature Table, replacing any existing Filter with the same name

        Parameters:
            filter: str
                The named Filter to create, or replace
            ftable: str
                The named Feature Table on which to base the Feature Filter
        """
        pass

    def CreateFilteredOverlay(self, oldPos: int, newPos: int, filter: str, locus: str) -> int:  # noqa: E501
        """
        Create a phased overlay with specified filters and loci applied

        Parameters:
            oldPos: int
                The position in the overlays list of the overlay to be
                scanned
            newPos: int
                The position of the new overlay in the overlays list
            filter: str
                Optionally, specify a named filter which items must pass to be
                included in the scan.Use an empty string to omit the filter
            locus: str
                Optionally, specify a named locus which items must fall within
                to be included in the scan.Use an empty string to omit the
                locus
        """
        pass

    def CreateFlowTheme(self) -> int:
        """
        Creates a new Flow Theme. After editing the Theme properties, use
        StoreTheme to save the Theme in a Named Object Library
        """
        pass

    def CreateFormulaGrid(self, formula: str) -> int:
        """
        Creates a Grid item by combining named Grid Items using a formula

        Parameters:
            formula: str
                The formulae involving Grid Items which have previously been
                saved in a Named Object Library. For example, if Grid Items
                have been saved under the names "g1" and "g2", then a new Grid
                item can be created by using the formula "g1 + g2"
        """
        pass

    def CreateGeodeticBuffer(self, list: str, datum: str, distance: float, nPoints: int) -> int:  # noqa: E501
        """
        Creates a 'geodetic' buffer around items in a named list

        Parameters:
            list: str
                The named list to be scanned
            datum: str
                The named datum to be used, eg WGS 84
            distance: float
                The size of the buffer
            nPoints: int
                The number of points to be used when creating the buffer (see
                Remarks)
        """
        pass

    def CreateGradientGrid(self, list: str, resolution: float) -> int:
        """
        Creates a 'slope' Grid from the currently open TIN as gradients
        between 0 and a value greater than 100%. 100% equals a slope of 45
        degrees. Slopes greater than 45 degrees will have a value larger than
        100%. In theory the gradient becomes infinite as the slope nears 90
        degrees. In practice the maximum value in SIS is 3276.7%

        Parameters:
            list: str
                The named list containing only TIN items for which the
                Gradient Grid will be created
            resolution: float
                The resolution or cell size at which the grid will be created
        """
        pass

    def CreateGraduatedTheme(self, formula: str) -> int:
        """
        Creates a new Graduated Theme. After editing the Theme properties, use
        StoreTheme to save the Theme in a Named Object Library

        Parameters:
            formula: str
                The formula to use when evaluating the symbol height, which
                must evaluate to a number. See Property Formula Syntax for
                details
        """
        pass

    def CreateGraticule(self, x1: float, y1: float, x2: float, y2: float) -> int:  # noqa: E501
        """
        Creates a Graticule item using the current open Photo item

        Parameters:
            x1: float
                The first x rectangular extent of the Graticule. This will
                typically be the extents of the associated Photo item
            y1: float
                The first y rectangular extent of the Graticule
            x2: float
                The second x rectangular extent of the Graticule
            y2: float
                The second y rectangular extent of the Graticule
        """
        pass

    def CreateGreatCircleLine(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, distance: float, datum: str) -> int:  # noqa: E501
        """
        Creates a great circle line

        Parameters:
            x1: float
                The x coordinate of the start point of the line
            y1: float
                The y coordinate of the start point of the line
            z1: float
                The z coordinate of the start point of the line
            x2: float
                The x coordinate of the end point of the line
            y2: float
                The y coordinate of the end point of the line
            z2: float
                The z coordinate of the end point of the line
            distance: float
                The length of individual segments along the line
            datum: str
                The named datum to be used, eg WGS84
        """
        pass

    def CreateGridFromQZone(self) -> int:
        """
        Creates a Grid item from current open QZone item
        """
        pass

    def CreateGroup(self, groupType: str) -> int:
        """
        Creates an empty Group item using a previously registered group class.
        All graphics created after calling this function but prior to calling
        CloseItem, PlaceGroup, Release or UpdateItem will be part of this
        group

        Parameters:
            groupType: str
                The type, or class, of group to create
        """
        pass

    def CreateGroupFromItems(self, list: str, bDelete: int, groupType: str) -> int:  # noqa: E501
        """
        Creates a Group item from the items in a Named List, optionally
        deleting the items in the Named List.The current axes will be used as
        the origin

        Parameters:
            list: str
                The Named List containing the items to be grouped
            bDelete: int

            groupType: str
                The type, or class, of group to create; the group class having
                been registered using RegisterGroupType
        """
        pass

    def CreateHotSpotGrid(self, list: str, formula: str, kernel: int, type: int, unit2: int, coincident: int, bandwidth: float, ox: float, oy: float, oz: float, cx: float, cy: float, flags: int) -> int:  # noqa: E501
        """
        Creates a Grid item from the hook points of the items in a named list
        using a kernel density estimation algorithm

        Parameters:
            list: str

            formula: str

            kernel: int

            type: int

            unit2: int

            coincident: int

            bandwidth: float

            ox: float

            oy: float

            oz: float

            cx: float

            cy: float

            flags: int

        """
        pass

    def CreateIdb(self, filename: str, schema: str) -> int:
        """

        Parameters:
            filename: str

            schema: str

        """
        pass

    def CreateIndexCoverage(self, list: str, tilename: str, namer: str, x1: float, y1: float, x2: float, y2: float) -> int:  # noqa: E501
        """
        Creates tile items covering extents, using one of the standard Index
        Dataset Naming Conventions

        Parameters:
            list: str
                The Named List in which to store any items created
            tilename: str
                The path name of one of the tiles being indexed
            namer: str
                The tile naming convention to use. This parameter is only
                needed if the tilename is not sufficient for SIS to
                unambiguously determine the tile's naming convention. See
                Index Dataset Naming Conventions for the available options
            x1: float
                The first x coordinate of the extent of the coverage
            y1: float
                The first y coordinate of the extent of the coverage
            x2: float
                The second x coordinate of the extent of the coverage
            y2: float
                The second y coordinate of the extent of the coverage
        """
        pass

    def CreateIndexOverlay(self, pos: int, tilename: str, namer: str, flags: int) -> int:  # noqa: E501
        """
        Creates an Index Dataset overlay, optionally creating outlines and
        labels for each tile found

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            tilename: str
                The path name of one of the tiles being indexed
            namer: str
                The tile naming convention to use. This parameter is only
                needed if the tilename is not sufficient for Cadcorp SIS to
                unambiguously determine the tile's naming convention. See
                Index Dataset Naming Conventions for the available options
            flags: int

        """
        pass

    def CreateIndividualTheme(self, formula: str, nValues: int) -> int:
        """
        Creates a new Individual Values Theme. After editing the Theme
        properties, use StoreTheme to save the Theme in a Named Object
        Library

        Parameters:
            formula: str
                The formula to use for matching values. See Property Formula
                Syntax for details
            nValues: int
                The number of individual values in the Theme, in the range 1
                to 16383
        """
        pass

    def CreateIndividualThemeFromFeatureTable(self, ftable: str, codes: str) -> int:  # noqa: E501
        """
        Create a new Individual Values theme from a feature table. After
        editing the theme properties, use StoreTheme to save the theme in a
        named object library

        Parameters:
            ftable: str
                The feature table from which the codes will be copied
            codes: str
                A space-separated string containing the feature codes to be
                created in the theme
        """
        pass

    def CreateInsert(self, x: float, y: float, z: float, blk: str, a: float, s: float) -> int:  # noqa: E501
        """
        Creates an Insert item using a named Block object

        Parameters:
            x: float
                The x position of the Insert item
            y: float
                The y position of the Insert item
            z: float
                The z position of the Insert item
            blk: str
                The Block object to which the Insert item refers
            a: float
                The angle of the Insert item in radians
            s: float
                The scale of the Insert item
        """
        pass

    def CreateInternalOverlay(self, overlay: str, pos: int) -> int:
        """
        Creates an internal overlay

        Parameters:
            overlay: str
                The name of the internal overlay
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
        """
        pass

    def CreateIsoRoute(self, x: float, y: float, z: float, r: float, isoVal: float, formula: str, filter: str, locusNoGo: str) -> int:  # noqa: E501
        """
        Create a MultiLineString Item (or a LineString Item) covering all
        connected places which can be reached from a position, within a given
        cost. When the cost is related to time, this query is often called an
        Isochrone

        Parameters:
            x: float
                The x position to start from
            y: float
                The y position to start from
            z: float
                The z position to start from
            r: float
                The maximum distance from the start point to linear geometry.
                The topological algorithm will spread out from the closest
                Item found. The distance from the point to the closest Item is
                not included in the cost calculation. Ideally, the start point
                should be on an item
            isoVal: float
                The maximum cost to incur during route finding
            formula: str
                The formula, or simple property, to use in the route finding
                calculation as the "cost" of a Link item. For example, using
                the simple property Length will find the shortest route, and
                using the formula "_length#/Speed#", provided each Link has a
                user-defined Speed# property, will find the quickest route.
                Any formula may be used, although if a string formula is used
                it must be a string representation of a numeric value. See
                Property Formula Syntax for details
            filter: str
                Optionally specifies a named Filter which all Items must pass
                to be considered as part of a route
            locusNoGo: str
                Optionally specifies a named Locus through which no route may
                pass
        """
        pass

    def CreateItem(self, blob: str, crs: str, fmt: int) -> int:
        """
        Creates an Item from a Blob string. If a Group is open, then graphics
        are added to the Group, otherwise a new Item is created

        Parameters:
            blob: str
                The stored Item Blob string
            crs: str
                The named CRS of the stored Item Blob
            fmt: int
                The format of the stored item Blob
        """
        pass

    def CreateItemFromLocus(self, locus: str) -> int:
        """
        Creates an Item from a named Locus. If a Group is open, then graphics
        are added to the Group, otherwise a new Item is created

        Parameters:
            locus: str
                The named Locus to use
        """
        pass

    def CreateKeyMap(self, x1: float, y1: float, x2: float, y2: float, list: str, backdrop: str, view: str) -> int:  # noqa: E501
        """
        Creates a Key Map item

        Parameters:
            x1: float
                The x coordinate of the first rectangular extent of the Key
                Map
            y1: float
                The y coordinate of the first rectangular extent of the Key
                Map
            x2: float
                The x coordinate of the second rectangular extent of the Key
                Map
            y2: float
                The y coordinate of the second rectangular extent of the Key
                Map
            list: str
                The Named List containing the Photo Items to be associated
                with the Key Map
            backdrop: str
                The named Item to draw as a backdrop in the Key Map
            view: str
                The named View to draw in the Key Map. If the Key Map does not
                have a named View, then it will draw the backdrop around the
                extents of all of the associated Photo Items
        """
        pass

    def CreateLabelTheme(self, formula: str) -> int:
        """
        Creates a new Labels Theme. After editing the Theme properties, use
        StoreTheme to save the Theme in a Named Object Library

        Parameters:
            formula: str
                The formula to use when labelling themed Items. See Property
                Formula Syntax for details
        """
        pass

    def CreateLayerFilter(self, filter: str, layers: str) -> int:
        """
        Creates a named filter in a Named Object Library, replacing any
        existing Filter with the same name

        Parameters:
            filter: str
                The named Filter to create, or replace
            layers: str
                A space-separated list of layer names, each preceded by + or -
                to indicate the inclusion or exclusion of the layer
        """
        pass

    def CreateLineText(self, text: str) -> int:
        """
        Creates a LineText item using the current open LineString item. If a
        Group is open, then graphics are added to the Group, otherwise a new
        Item is created

        Parameters:
            text: str
                The text of the LineText item
        """
        pass

    def CreateLinkFilter(self, filter: str, idlist: str) -> int:
        """
        Creates an empty List of Item IDs filter in a Named Object Library,
        replacing any existing Filter with the same name

        Parameters:
            filter: str
                The named Filter to create, or replace
            idlist: str
                A space-separated list of item id numbers to include in the
                link List of item IDs
        """
        pass

    def CreateListFromOverlay(self, pos: int, list: str) -> int:
        """
        Creates a Named List of all of the items on an overlay

        Parameters:
            pos: int
                The position in the overlays list of the overlay from which to
                fill the Named List
            list: str
                The Named List to fill with overlay Items
        """
        pass

    def CreateLocusFromItem(self, locus: str, geomTest: int, geomMode: int) -> int:  # noqa: E501
        """
        Creates a named Locus in a Named Object Library from the current open
        Item, replacing any existing Locus with the same name

        Parameters:
            locus: str
                The named Locus to create, or replace
            geomTest: int
                The geometry test to use. See Geometry Tests for details
            geomMode: int
                The geometry mode to use. See Geometry Tests for details
        """
        pass

    def CreateMarkdown(self, x1: float, y1: float, x2: float, y2: float, markdown: str) -> int:  # noqa: E501
        """

        Parameters:
            x1: float

            y1: float

            x2: float

            y2: float

            markdown: str

        """
        pass

    def CreateNorthPoint(self, x: float, y: float, z: float, shape: str, s: float) -> int:  # noqa: E501
        """
        Creates a North Point item using the current open Photo item. If a
        Group is open, then graphics are added to the Group, otherwise a new
        Item is created

        Parameters:
            x: float
                The x coordinate position of the North Point
            y: float
                The y coordinate position of the North Point
            z: float
                The z coordinate position of the North Point
            shape: str
                The Symbol of the North Point
            s: float
                The scale of the North Point
        """
        pass

    def CreateOpenGisSqlOverlay(self, pos: int, connect: str, ftable: str, gtable: str) -> int:  # noqa: E501
        """
        Creates an overlay using an Open Geospatial Consortium (OGC)
        conformant database. The overlay uses the Cadcorp OGC SQL92 Database
        dataset

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            connect: str
                The connect argument enables SIS to connect to the database
                containing the data to be mapped. The methods you can use to
                connect to a database are
            ftable: str
                The OGC feature table. Note This is not the same as a SIS
                Feature Table
            gtable: str

        """
        pass

    def CreatePhaseOverlay(self, oldPos: int, newPos: int) -> int:
        """
        Creates a new phase of an existing overlay

        Parameters:
            oldPos: int
                The position in the overlays list of the overlay being phased
            newPos: int
                The position in the overlays list at which to insert the new
                phase overlay. If this argument specifies a position in the
                existing overlays then the new overlay will not replace the
                existing overlay at the given position, but will shuffle any
                other overlays down the list
        """
        pass

    def CreatePhoto(self, x1: float, y1: float, x2: float, y2: float) -> int:
        """
        Creates a Photo item in the current window, filling it with the
        previously composed window

        Parameters:
            x1: float
                The x coordinate of the first rectangular extent of the Photo
                item
            y1: float
                The y coordinate of the first rectangular extent of the Photo
                item
            x2: float
                The x coordinate of the second rectangular extent of the Photo
                item
            y2: float
                The y coordinate of the second rectangular extent of the Photo
                item
        """
        pass

    def CreatePieTheme(self, nSlices: int) -> int:
        """
        Creates a new Pie Charts Theme. After editing the Theme properties,
        use StoreTheme to save the Theme in a Named Object Library

        Parameters:
            nSlices: int
                The number of slices in the Pie Charts, in the range 1 to 256
        """
        pass

    def CreatePoint(self, x: float, y: float, z: float, shape: str, a: float, s: float) -> int:  # noqa: E501
        """
        Creates a Point item. If a Group is open, then graphics are added to
        the Group, otherwise a new Item is created

        Parameters:
            x: float
                The x coordinate of the Point
            y: float
                The y coordinate of the Point
            z: float
                The z coordinate of the Point
            shape: str
                The Symbol of the Point
            a: float
                The angle of the Point in radians
            s: float
                The scale of the Point
        """
        pass

    def CreateProcessOverlay(self, oldPos: int, newPos: int, process: str) -> int:  # noqa: E501
        """

        Parameters:
            oldPos: int

            newPos: int

            process: str

        """
        pass

    def CreatePropertyFilter(self, filter: str, formula: str) -> int:
        """
        Creates a named Property Filter in a Named Object Library, replacing
        any existing Filter with the same name

        Parameters:
            filter: str
                The named Filter to create, or replace
            formula: str
                The property formula, eg "_closed&=0". See Property Formula
                Syntax for details
        """
        pass

    def CreateQZoneFromGrid(self, v1: float, v2: float) -> int:
        """
        Creates a QZone item from the cells in the current Grid item which are
        between two values. If a Group is open, then graphics are added to the
        Group, otherwise a new Item is created

        Parameters:
            v1: float
                The beginning of the range of values. Grid cells in this range
                will be included in the resulting QZone item
            v2: float
                The end of the range of values. Grid cells in this range will
                be included in the resulting QZone item
        """
        pass

    def CreateQueryOverlay(self, sql: str, pos: int) -> int:
        """

        Parameters:
            sql: str

            pos: int

        """
        pass

    def CreateRangeTheme(self, formula: str, nRanges: int) -> int:
        """
        Creates a new Ranges Theme. After editing the Theme properties, use
        StoreTheme to save the Theme in a Named Object Library

        Parameters:
            formula: str
                The formula to use for matching values, which must evaluate to
                a number. See Property Formula Syntax for details
            nRanges: int
                The number of ranges in the Theme, in the range 2 to 15
        """
        pass

    def CreateRectLocus(self, locus: str, x1: float, y1: float, x2: float, y2: float) -> int:  # noqa: E501
        """
        Creates a rectangular named Locus in a Named Object Library, replacing
        any existing Locus with the same name

        Parameters:
            locus: str
                The named Locus to create, or replace
            x1: float
                The first x coordinate of the rectangular extent of the Locus
            y1: float
                The first y coordinate of the rectangular extent of the Locus
            x2: float
                The second x coordinate of the rectangular extent of the
                Locus
            y2: float
                The second y coordinate of the rectangular extent of the
                Locus
        """
        pass

    def CreateRectangle(self, x1: float, y1: float, x2: float, y2: float) -> int:  # noqa: E501
        """
        Creates a rectangular Polygon item. If a Group is open, then graphics
        are added to the Group, otherwise a new Item is created

        Parameters:
            x1: float
                The first x coordinate of the rectangular extent of the
                Polygon item
            y1: float
                The first y coordinate of the rectangular extent of the
                Polygon item
            x2: float
                The second x coordinate of the rectangular extent of the
                Polygon item
            y2: float
                The second y coordinate of the rectangular extent of the
                Polygon item
        """
        pass

    def CreateReliefTheme(self, colset: str) -> int:
        """
        Creates a new Relief Theme. After editing the Theme properties, use
        StoreTheme to save the Theme in a Named Object Library

        Parameters:
            colset: str
                The Colour-set on which to base the Relief Theme
        """
        pass

    def CreateRubberSheet(self, list: str) -> int:
        """
        Creates a Rubber Sheet item from the Displacement Items in a Named
        List. If a Group is open, then graphics are added to the Group,
        otherwise a new Item is created

        Parameters:
            list: str
                The Named List which must contain three or more Displacement
                Items
        """
        pass

    def CreateScaleBar(self, x: float, y: float, z: float, shape: str, a: float) -> int:  # noqa: E501
        """
        Creates a Scale Bar item using the current open Photo item. If a Group
        is open, then graphics are added to the Group, otherwise a new Item is
        created

        Parameters:
            x: float
                The first x coordinate of the rectangular extent of the Scale
                Bar
            y: float
                The first y coordinate of the rectangular extent of the Scale
                Bar
            z: float
                The first z coordinate of the rectangular extent of the Scale
                Bar
            shape: str
                The Symbol of the Scale Bar
            a: float
                The angle of the Scale Bar in radians
        """
        pass

    def CreateScatterGrid(self, list: str, formula: str, mode: int, ox: float, oy: float, oz: float, cx: float, cy: float) -> int:  # noqa: E501
        """
        Creates a Grid item from the origins of the Items in a Named List. If
        a Group is open, then graphics are added to the Group, otherwise a new
        Item is created

        Parameters:
            list: str
                A Named List which contains the Items from which to make a
                scatter Grid. The origin of each Item is used to seed a value
                in the Grid item. The Items will typically be Point Items, but
                any Item class may be used. The Items are not edited by this
                operation, and therefore can be from a read-only dataset
            formula: str
                A formula which is evaluated for each item in the Named List.
                This parameter is ignored for the SIS_SCATTER_GRID_COUNT mode.
                See Property Formula Syntax for details
            mode: int
                The method used to calculate each Grid cell value
            ox: float
                The x coordinate of the origin of the Grid item. This is not
                the bottom-left-hand corner of the Grid, but is a position
                around which the grid will position itself. Use (0.0,0.0,0.0)
                to make a Grid aligned to the current axes
            oy: float
                The y coordinate of the origin of the Grid item. This is not
                the bottom-left-hand corner of the Grid, but is a position
                around which the grid will position itself. Use (0.0,0.0,0.0)
                to make a Grid aligned to the current axes
            oz: float
                The z coordinate of the origin of the Grid item. This is not
                the bottom-left-hand corner of the Grid, but is a position
                around which the grid will position itself. Use (0.0,0.0,0.0)
                to make a Grid aligned to the current axes
            cx: float
                The x size of each Grid cell in metres.The maximum size of the
                Grid item is 1000 by 1000 cells. The created Grid will always
                cover the Items in the Named List, so if a very small cell
                size is specified, this routine can fail
            cy: float
                The y size of each Grid cell in metres
        """
        pass

    def CreateSlopeGrid(self, list: str, resolution: float) -> int:
        """
        Creates a 'Slope' Grid from the TIN's in a named list

        Parameters:
            list: str
                The named list containing only TIN items for which the Slope
                Grid will be created
            resolution: float
                The resolution or cell size at which the grid will be created
        """
        pass

    def CreateSurface(self) -> int:
        """
        Creates a Surface item from the current open Polygon item. If a Group
        is open, then graphics are added to the Group, otherwise a new Item is
        created
        """
        pass

    def CreateTable(self, x1: float, y1: float, x2: float, y2: float, pos: int, nRows: int) -> int:  # noqa: E501
        """

        Parameters:
            x1: float

            y1: float

            x2: float

            y2: float

            pos: int

            nRows: int

        """
        pass

    def CreateText(self, x: float, y: float, z: float, text: str) -> int:
        """
        Creates a Text item. If a Group is open, then graphics are added to
        the Group, otherwise a new Item is created

        Parameters:
            x: float
                The x coordinate position of the alignment point of the Text
                item
            y: float
                The y coordinate position of the alignment point of the Text
                item
            z: float
                The z coordinate position of the alignment point of the Text
                item
            text: str
                The text of the Text item
        """
        pass

    def CreateThiessen(self, listOutput: str, list: str, bClipToCurItem: int) -> int:  # noqa: E501
        """
        Creates Thiessen Polygon Items from the origins of the Items in a
        Named List. If a Group is open, then graphics are added to the Group,
        otherwise a new Item is created

        Parameters:
            listOutput: str
                The Named List which will contain the Thiessen Polygon Items
            list: str
                A Named List containing the Items whose origins will be used
                to create the Thiessen Polygon Items
            bClipToCurItem: int

        """
        pass

    def CreateTin(self, list: str) -> int:
        """
        Create a Triangular Irregular Network (TIN) or MultiPolygon from items
        in a named list. A TIN is a special type of surface item. If a Group
        is open, then graphics are added to the Group, otherwise a new Item is
        created

        Parameters:
            list: str
                A Named List containing items which will be used to create the
                TIN or MultiPolygon
        """
        pass

    def CreateTinEx(self, list: str, formula: str, aclass: str, nFaces: int) -> int:  # noqa: E501
        """
        Creates a Triangular Irregular Network (TIN) or MultiPolygon from
        items in a named list, using advanced creation properties. A TIN is a
        special type of surface item. If a Group is open, then graphics are
        added to the Group, otherwise a new Item is created

        Parameters:
            list: str
                A Named List containing items which will be used to create the
                TIN or MultiPolygon
            formula: str
                The formula to use to calculate the Z value of the positions
                being triangulated. Use "_oz#" for the Z height of the item
            aclass: str
                The Item class which this method will create. This may be
                "Area" for MultiPolygon items or "TinSurface" for a TIN
            nFaces: int
                The number of triangular faces per Tin or MultiPolygon making
                up the surface
        """
        pass

    def CreateTinFromGrid(self, tol: float) -> int:
        """
        Fits a TIN item over the current open Grid item

        Parameters:
            tol: float
                This is the height tolerance in metres. See Convert to TIN
        """
        pass

    def CreateTopoTheme(self) -> int:
        """
        Creates a new Topology Theme which displays a schematic layout of a
        topological network. After editing the Theme properties, use
        StoreTheme to save the Theme in a Named Object Library
        """
        pass

    def CreateValueListFilter(self, filter: str, propertyName: str) -> int:
        """
        Creates an empty named Value-list Filter in a Named Object Library,
        replacing any existing Filter with the same name

        Parameters:
            filter: str
                The name of the Filter to create, or replace
            propertyName: str
                The property whose values will be compared by the Value-list
                Filter
        """
        pass

    def CreateViewshed(self, list: str, x: float, y: float, z: float, r: float, bQZone: int) -> int:  # noqa: E501
        """
        Create a Viewshed on a grid in a named list

        Parameters:
            list: str
                The named list containing a grid item
            x: float
                The x coordinate of the eye position from which the grid is
                viewed to create the viewshed
            y: float
                The y coordinate of the eye position from which the grid is
                viewed to create the viewshed
            z: float
                The z coordinate of the eye position from which the grid is
                viewed to create the viewshed
            r: float
                The maximum distance from the eye position for which the
                viewshed will be calculated
            bQZone: int
                0 create the viewshed as a grid item1 create the viewshed as a
                QZone item
        """
        pass

    def DecomposeGeometry(self, list: str) -> int:
        """
        Break down items with complex geometry into separate items

        Parameters:
            list: str
                The named list storing items to be decomposed. On completion,
                the list will store only any newly separated items
        """
        pass

    def DecomposeGrid(self, list: str) -> int:
        """
        'Explodes' the current open Grid item into one Polygon item per Grid
        cell

        Parameters:
            list: str

        """
        pass

    def DefineNolDatum(self, datum: str, re: float, rp: float, dx: float, dy: float, dz: float, ex: float, ey: float, ez: float, m: float, pm: float) -> int:  # noqa: E501
        """
        Creates a named Geodetic Datum in a Named Object Library, using the
        standard seven Bursa-Wolf parameters to modify WGS84, replacing any
        existing Geodetic Datum with the same name

        Parameters:
            datum: str
                The named Geodetic Datum to create, or replace
            re: float
                The equatorial radius of the ellipsoid, specified in metres
            rp: float
                The polar radius of the ellipsoid, specified in metres
            dx: float
                The x shift to apply to the ellipsoid, specified in metres
            dy: float
                The y shift to apply to the ellipsoid, specified in metres
            dz: float
                The z shift to apply to the ellipsoid, specified in metres
            ex: float
                The rotational adjustment about the x axis, specified in
                minutes of arc
            ey: float
                The rotational adjustment about the y axis, specified in
                minutes of arc
            ez: float
                The rotational adjustment about the z axis, specified in
                minutes of arc
            m: float
                The correction scale factor, specified in parts per million.
                Use 0.0 for no scale correction
            pm: float
                The Prime Meridian, specified in radians. At present, this
                parameter is ignored, and must be specified as 0.0
        """
        pass

    def DefineNolItem(self, item: str) -> int:
        """
        Stores the current open Item in a Named Object Library as a named
        Item, replacing any existing Item with the same name

        Parameters:
            item: str
                The named Item to create, or replace
        """
        pass

    def DefineNolItemFromLocus(self, item: str, locus: str) -> int:
        """
        Stores a named Locus in a Named Object Library as a named Item,
        replacing any existing Item with the same name

        Parameters:
            item: str
                The named Item to create, or replace
            locus: str
                The named Locus to be stored
        """
        pass

    def DefineNolObject(self, aclass: str, aname: str, implicit: str) -> int:
        """
        Creates a named object in a Named Object Library from an implicit
        string, replacing any object with the same name. This method is used
        to create named Brush, Colour-set, Pen and CRS objects.Implicit
        strings can be queried from existing named objects using
        GetImplicitNolObject

        Parameters:
            aclass: str
                The class of named object to be created. Valid classes are
            aname: str
                The named object to create, or replace
            implicit: str
                The implicit string which defines the object. See Brush,
                Colour-set, Pen, CRS and Feature Table for descriptions
        """
        pass

    def DefineNolPrintTemplate(self, ptemplate: str) -> int:
        """
        Defines a named Print Template in a Named Object Library from the
        current window contents, replacing any existing Print Template with
        the same name

        Parameters:
            ptemplate: str
                The named APrintTemplate@ to create, or replace
        """
        pass

    def DefineNolPrj(self, crs: str, epsg: int) -> int:
        """
        Creates a named CRS from an EPSG code in a Named Object Library,
        replacing any existing CRS with the same name

        Parameters:
            crs: str
                The named CRS to create, or replace
            epsg: int
                The EPSG code associated with the CRS
        """
        pass

    def DefineNolPrjLatLon(self, crs: str, lat: float, lon: float, datum: str, bDeg: int) -> int:  # noqa: E501
        """
        Creates a named Latitude/Longitude CRS in a Named Object Library,
        replacing any existing CRS with the same name

        Parameters:
            crs: str
                The named CRS to create, or replace
            lat: float
                The CRS latitude origin, in degrees. See Remarks
            lon: float
                The CRS longitude origin, in degrees. See Remarks
            datum: str
                The named Geodetic Datum on which to base the CRS. This can be
                any named Geodetic Datum previously created, or loaded from a
                Named Object Library
            bDeg: int

        """
        pass

    def DefineNolPrjTm(self, crs: str, lat: float, lon: float, datum: str, f0: float, cx: float, cy: float, cz: float, tometre: float) -> int:  # noqa: E501
        """
        Defines a named Transverse Mercator CRS in a Named Object Library,
        replacing any existing CRS with the same name

        Parameters:
            crs: str
                The named CRS to create, or replace
            lat: float
                The CRS latitude origin, in degrees
            lon: float
                The CRS longitude origin, in degrees
            datum: str
                The named Geodetic Datum on which to base the CRS. This can be
                any named Geodetic Datum previously created using
                DefineNolDatum, or loaded from a Named Object Library
            f0: float
                The scale on Central Meridian
            cx: float
                The x coordinate position of the false origin
            cy: float
                The y coordinate position of the false origin
            cz: float
                The z coordinate position of the false origin
            tometre: float
                The conversion from CRS units to metres
        """
        pass

    def DefineNolShape(self, shape: str, list: str, x: float, y: float, z: float, s: float) -> int:  # noqa: E501
        """
        Defines a named Symbol in a Named Object Library, from the items in a
        Named List, replacing any existing Symbol with the same name

        Parameters:
            shape: str
                The named Symbol to create, or replace
            list: str
                The Named List containing the Items which make up the Symbol
            x: float
                The x coordinate of the origin of the Symbol
            y: float
                The y coordinate of the origin of the Symbol
            z: float
                The z coordinate of the origin of the Symbol
            s: float
                The scale of the Symbol
        """
        pass

    def DefineNolView(self, view: str) -> int:
        """
        Defines a named View in a Named Object Library, from the view in the
        current window, replacing any existing View with the same name

        Parameters:
            view: str
                The named View to create, or replace
        """
        pass

    def Delete(self, list: str) -> int:
        """
        Deletes all of the Items in a Named List

        Parameters:
            list: str
                A Named List containing the Items to be deleted
        """
        pass

    def DeleteComposition(self, name: str) -> int:
        """
        Deletes a named composition

        Parameters:
            name: str
                The name of the composition
        """
        pass

    def DeleteGeomPt(self, nGeom: int, nPt: int) -> int:
        """
        Deletes a vertex from the geometry of the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            nPt: int
                The index of the vertex, starting at 0
        """
        pass

    def DeleteItem(self) -> int:
        """
        Deletes the current open Item
        """
        pass

    def DeleteNolObject(self, nPos: int, aclass: str, name: str) -> int:
        """
        Deletes a named object from a Named Object Library (NOL)

        Parameters:
            nPos: int
                The position in the list of NOLs of the NOL containing the
                named object to be deleted
            aclass: str
                The class of named object to be deleted. See Named Object
                Library Classes for valid classes
            name: str
                The named object to delete
        """
        pass

    def DeleteObject(self, url: str) -> int:
        """

        Parameters:
            url: str

        """
        pass

    def DeleteRecordset(self, rs: str) -> int:
        """
        Deletes a named recordset

        Parameters:
            rs: str
                A named recordset to delete, previously created using
                DefineRecordset
        """
        pass

    def DescribeProperty(self, prop: str, desc: str) -> int:
        """
        Sets the description of a property. The description will be used by
        the Workspace Window PropertyView and the dialog displayed by the
        Edit/Properties... command for the remainder of the session

        Parameters:
            prop: str

            desc: str

        """
        pass

    def DisconnectGps(self) -> int:
        """
        Terminate the connection currently open to the GPS device attached to
        the computer
        """
        pass

    def DissolveItems(self, list: str, formula: str) -> int:
        """
        Merge items based on attribute values

        Parameters:
            list: str
                The named list storing items to be merged. On completion, the
                list will store the merged items
            formula: str
                The formula to use to control the merge
        """
        pass

    def DropColumn(self, nDataset: int, column: str) -> int:
        """

        Parameters:
            nDataset: int

            column: str

        """
        pass

    def DropColumnIndex(self, nDataset: int, column: str) -> int:
        """

        Parameters:
            nDataset: int

            column: str

        """
        pass

    def EmptyGroup(self) -> int:
        """
        Empties the current open Group item, deleting all Items within the
        Group
        """
        pass

    def EmptyList(self, list: str) -> int:
        """
        Empties all of the Items from a Named List, and deletes the Named
        List

        Parameters:
            list: str
                The Named List to empty and delete
        """
        pass

    def EnableOverlayTheme(self, pos: int, nTheme: int, bEnable: int) -> int:
        """
        Enables or disables an overlay theme

        Parameters:
            pos: int
                The position of the overlay in the overlays list on which the
                theme is to be enabled
            nTheme: int
                The position of the theme in the overlay's theme list which is
                to be enabled. Theme indices run from zero to one less than
                the number of themes
            bEnable: int

        """
        pass

    def EnsureOpenWithin(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, s: float) -> int:  # noqa: E501
        """
        Forces datasets in the current window to open any items within the
        given extents, at the given scale

        Parameters:
            x1: float
                The first x coordinate of the cuboid within which all items
                will be opened
            y1: float
                The first y coordinate of the cuboid within which all items
                will be opened
            z1: float
                The first z coordinate of the cuboid within which all items
                will be opened
            x2: float
                The second x coordinate of the cuboid within which all items
                will be opened
            y2: float
                The second y coordinate of the cuboid within which all items
                will be opened
            z2: float
                The second z coordinate of the cuboid within which all items
                will be opened
            s: float
                The scale at which to open items
        """
        pass

    def ExplodeOverlayTheme(self, pos: int, nTheme: int, s: float) -> int:
        """
        Explodes an overlay Theme into a new overlay

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose Theme
                is to be exploded
            nTheme: int
                The index of the Theme, starting at 0. Use the Number of
                themes property to find out the number of Theme objects in an
                overlay
            s: float
                The scale at which to explode the overlay Theme graphics. Use
                the Display scale property to explode the graphics at the
                current screen scale
        """
        pass

    def ExportFeatureTable(self, ftable: str, filename: str) -> int:
        """
        Exports a named Feature Table to a comma-separated file

        Parameters:
            ftable: str
                The named Feature Table to export
            filename: str
                The name of the exported file
        """
        pass

    def FacetGeometry(self, list: str, tolerance: float) -> int:
        """
        Replaces curved geometry segments with shorter straight segments

        Parameters:
            list: str
                The Named List containing the Items to be facetted
            tolerance: float
                The maximum distance allowed between the original curve and
                the new facet. The smaller the number used, the greater the
                number of segments
        """
        pass

    def FillGeometry(self) -> int:
        """
        Fills the space that is enclosed by the geometry of the current open
        Item. For example, you could use this to convert a closed LineString
        into a Polygon item
        """
        pass

    def FillPhotoFromComposition(self, name: str) -> int:
        """
        Refills the current open Photo item from a named composition

        Parameters:
            name: str
                The name of the composition used to fill the current open
                Photo item
        """
        pass

    def FillSwdFromComposition(self, name: str) -> int:
        """
        Refills the current swd from a named composition

        Parameters:
            name: str
                The name of the composition used to fill the current swd
        """
        pass

    def GeneraliseDP(self, list: str, tolerance: float) -> int:
        """
        Generalises geometry using the Douglas-Peucker algorithm

        Parameters:
            list: str
                The named list containing the items to generalise
            tolerance: float
                The tolerance to use in the generalisation algorithm
        """
        pass

    def GetAxesPrj(self, crs: str) -> int:
        """
        Gets a copy of the current axes CRS, placing it in a Named Object
        Library, replacing any existing CRS with the same name

        Parameters:
            crs: str
                The named CRS to create, or replace.The CRS will either be
                cartesian or spherical, use GetAxesType to find out which
        """
        pass

    def GetDatasetPrj(self, nDataset: int, crs: str) -> int:
        """
        Gets a copy of a dataset CRS, placing it in a Named Object Library,
        replacing any existing CRS with the same name

        Parameters:
            nDataset: int
                The serial number of the dataset whose CRS is required. The
                serial number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
            crs: str
                The named CRS to create, or replace
        """
        pass

    def GetOverlayFilter(self, pos: int, filter: str) -> int:
        """
        Gets a copy of an overlay drawing Filter, placing it in a Named Object
        Library, replacing any existing Filter with the same name

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose drawing
                Filter is to be copied
            filter: str
                The named Filter to create, or replace
        """
        pass

    def GetOverlayLocus(self, pos: int, locus: str) -> int:
        """
        Gets a copy of an overlay drawing Locus, placing it in a Named Object
        Library, replacing any existing Locus with the same name

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose drawing
                Locus is to be copied
            locus: str
                The named Locus to create, or replace
        """
        pass

    def GetOverlaySchema(self, pos: int, schema: str) -> int:
        """
        Gets a copy of an overlay Schema, placing it in a Named Object
        Library, replacing any existing Schema with the same name

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose Schema
                is to be copied
            schema: str
                The named Schema to create, or replace
        """
        pass

    def GetOverlayTheme(self, pos: int, theme: str, nTheme: int) -> int:
        """
        Gets a copy of an overlay Theme, placing it in a Named Object Library,
        replacing any existing Theme with the same name

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose Theme
                is to be copied
            theme: str
                The named Theme to create, or replace
            nTheme: int
                The index of the Theme, starting at 0. Use the Number of
                themes property to find out the number of Theme objects in an
                overlay
        """
        pass

    def GetViewPrj(self, projection: str) -> int:
        """
        Gets a copy of the view projection, placing it in a Named Object
        Library, replacing any existing object with the same name

        Parameters:
            projection: str
                The named object to create, or replace
        """
        pass

    def ImportDataSourceOverlay(self, pos: int, clsDataSource: str, parameters: str) -> int:  # noqa: E501
        """
        Imports a dataset into the current Swd, that will fetch data from
        non-file data source

        Parameters:
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays, the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
            clsDataSource: str
                The class name of the data source to use
            parameters: str
                Comma-separated optional parameters used to configure the data
                source
        """
        pass

    def ImportDataset(self, dataset: str, pos: int) -> int:
        """
        Imports a dataset into the current Swd. This method creates an
        internal overlay which contains copies of all of the items in the
        given dataset

        Parameters:
            dataset: str
                The filename of the dataset to import.If the dataset class can
                handle parameters, then you can append parameters after the
                filename using a question mark. For example, the dataset name
                could be "c
            pos: int
                The position in the overlays list at which to insert the
                overlay. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
        """
        pass

    def ImportFeatureTable(self, ftable: str, filename: str) -> int:
        """
        Imports a named Feature Table from a comma-separated file, placing it
        in a Named Object Library, replacing any existing Feature Table with
        the same name

        Parameters:
            ftable: str
                The named Feature Table to create, or replace
            filename: str
                The name of the file from which to create the Feature Table
        """
        pass

    def InsertDataset(self, dataset: str, pos: int) -> int:
        """
        Inserts a dataset into the current SIS Workspace Definition (SWD)

        Parameters:
            dataset: str
                If the dataset class can handle parameters, then you can
                append parameters after the filename using a question mark.
                For example, the dataset name could be "c
            pos: int
                The position in the overlays list at which to insert the
                dataset. If this argument specifies a position in the existing
                overlays then the new overlay will not replace the existing
                overlay at the given position, but will shuffle any other
                overlays down the list
        """
        pass

    def InsertFeatureCode(self, fcode: int) -> int:
        """
        Inserts a new feature code into the currently loaded Feature Table.
        Use LoadFeatureTable to load a Feature Table for editing

        Parameters:
            fcode: int
                The feature code to be inserted, from 1 to 65535
        """
        pass

    def InsertGeomPt(self, nGeom: int, arclen: float, x: float, y: float, z: float) -> int:  # noqa: E501
        """
        Inserts a new vertex into geometry from the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
            arclen: float
                The length along the geometry component to insert the new
                vertex
            x: float
                The x coordinate position of the new vertex
            y: float
                The y coordinate position of the new vertex
            z: float
                The z coordinate position of the new vertex
        """
        pass

    def InsertOverlayTheme(self, pos: int, theme: str, nTheme: int) -> int:
        """
        Inserts a copy of a named Theme into an overlay in the current window

        Parameters:
            pos: int
                The position of the overlay in the overlays list to which the
                Theme is to be added
            theme: str
                The named Theme to add. This can be any named Theme previously
                created, or loaded from a Named Object Library
            nTheme: int
                The position in the list of Themes on the overlay at which to
                insert the Theme. If this argument specifies a position in the
                existing Themes then the new Theme will not replace the
                existing Theme at the given position, but will shuffle any
                other Theme objects down the list
        """
        pass

    def InsertSchemaColumn(self, formula: str, nColumn: int) -> int:
        """
        Inserts a new column into the currently loaded Schema. Use LoadSchema
        to load a Schema for editing

        Parameters:
            formula: str
                The formula of the new column. See Property Formula Syntax for
                details
            nColumn: int
                The position in the columns list at which to insert the new
                column. If this argument specifies a position in the existing
                columns then the new column will not replace the existing
                column at the given position, but will shuffle any other
                columns down the list
        """
        pass

    def IsoRoute(self, list: str, x: float, y: float, z: float, r: float, isoVal: float, formula: str, filter: str, locusNoGo: str) -> int:  # noqa: E501
        """
        Find Link and Node Items which can be reached from a position, within
        a given cost. When the cost is related to time, this query is often
        called an Isochrone

        Parameters:
            list: str
                A Named List of Link and Node Items which can be got to. Any
                Link item whose mid-point can be reached will be put in the
                Named List
            x: float
                The x coordinate of the position to start from
            y: float
                The y coordinate of the position to start from
            z: float
                The z coordinate of the position to start from
            r: float
                The maximum distance from the start point to a Link item. The
                topological algorithm will spread out from the closest Link
                found. The distance from the point to the closest Link is not
                included in the cost calculation. Ideally, the start point
                should be on a Link item
            isoVal: float
                The maximum cost to incur during route finding
            formula: str
                The formula, or simple property, to use in the route finding
                calculation as the "cost" of a Link item. For example, using
                the simple property Length will find all Link and Node Items
                within a fixed distance from the point. See Property Formula
                Syntax for details
            filter: str
                Optionally specifies a named Filter which all Link Items must
                pass to be considered as part of a route
            locusNoGo: str
                Optionally specifies a named Locus through which no route may
                pass
        """
        pass

    def JoinLines(self, list: str, tolerance: float) -> int:
        """
        Joins LineString items within a tolerance

        Parameters:
            list: str
                The Named List containing the LineString items to be joined
            tolerance: float
                The tolerance in current units within which to consider joins
        """
        pass

    def LineTo(self, x: float, y: float, z: float) -> int:
        """
        Draws a line from the current drawing position

        Parameters:
            x: float
                The x coordinate of the new LineString position
            y: float
                The y coordinate of the new LineString position
            z: float
                The z coordinate of the new LineString position
        """
        pass

    def LoadFeatureTable(self, ftable: str) -> int:
        """
        Loads a named Feature Table for editing

        Parameters:
            ftable: str
                The named Feature Table to load for editing. Use "" to create
                a new, empty Feature Table
        """
        pass

    def LoadSchema(self, schema: str) -> int:
        """
        Loads a named Schema for editing

        Parameters:
            schema: str
                The named Schema to load for editing. Use "" to create a new,
                empty Schema
        """
        pass

    def LoadTheme(self, theme: str) -> int:
        """
        Loads a named Theme for editing

        Parameters:
            theme: str
                The named Theme to load for editing
        """
        pass

    def LocusIntersect(self, locusOut: str, locus1: str, locus2: str) -> int:
        """
        Creates a named Locus in a Named Object Library, by intersecting two
        existing Locus objects, replacing any existing Locus with the same
        name

        Parameters:
            locusOut: str
                The named Locus to create, or replace
            locus1: str
                The first Locus object to intersect
            locus2: str
                The second Locus object to intersect
        """
        pass

    def MoveAxes(self, x: float, y: float, z: float) -> int:
        """
        Sets the position of the Cartesian axes

        Parameters:
            x: float
                The x coordinate of the new position of the axes origin. This
                position is relative to the current axes origin
            y: float
                The y coordinate of the new position of the axes origin. This
                position is relative to the current axes origin
            z: float
                The z coordinate of the new position of the axes origin. This
                position is relative to the current axes origin
        """
        pass

    def MoveCursorToBegin(self, cursor: str) -> int:
        """
        Moves the current row to be at the start of the named cursor

        Parameters:
            cursor: str
                The named cursor in which the current row is to be moved to
                the beginning
        """
        pass

    def MoveCursorToEnd(self, cursor: str) -> int:
        """
        Moves the current row to be at the end of the named cursor

        Parameters:
            cursor: str
                The named cursor in which the current row is to be moved to
                the end
        """
        pass

    def MoveList(self, list: str, x: float, y: float, z: float, a: float, s: float) -> int:  # noqa: E501
        """
        Moves, rotates, and scales editable Items in a Named List

        Parameters:
            list: str
                The Named List containing the Items to be moved, rotated and
                scaled
            x: float
                The distances to move in the x direction. Note that these
                values are relative, ie the items will be moved by these
                values from their current positions
            y: float
                The distances to move in the y direction. Note that these
                values are relative, ie the items will be moved by these
                values from their current positions
            z: float
                The distances to move in the z direction. Note that these
                values are relative, ie the items will be moved by these
                values from their current positions
            a: float
                The rotation, in radians, to apply
            s: float
                The scaling to apply
        """
        pass

    def MoveTo(self, x: float, y: float, z: float) -> int:
        """
        Sets the current drawing position

        Parameters:
            x: float
                The x coordinate of the new drawing position
            y: float
                The y coordinate of the new drawing position
            z: float
                The z coordinate of the new drawing position
        """
        pass

    def NolClose(self, nPos: int, bSave: int) -> int:
        """
        Closes a Named Object Library (NOL) file, optionally saving any
        changes.Non-file NOLs, eg "(temporary)", cannot be removed from the
        list of currently loaded NOLs. Calling this method with an editable
        non-file NOL will empty it of all objects instead. Calling this method
        with a read-only non-file NOL will have no effect

        Parameters:
            nPos: int
                The position in the list of NOLs of the NOL to be closed
            bSave: int

        """
        pass

    def NolCompact(self, nPos: int) -> int:
        """
        Discards all old Named Object Library (NOL) objects and defragments
        memory used by the NOL

        Parameters:
            nPos: int
                The position in the list of NOLs of the NOL to be compacted
        """
        pass

    def NolCreate(self, filename: str) -> int:
        """
        Creates an empty Named Object Library (NOL) file. This call will fail
        if the NOL file already exists

        Parameters:
            filename: str
                The name of the new NOL file. The new NOL is created in the
                current attached directory, unless a full path name is given.
                The new NOL can be added using NolInsert
        """
        pass

    def NolInsert(self, filename: str, nPos: int, bReadOnly: int) -> int:
        """
        Inserts a Named Object Library (NOL) file

        Parameters:
            filename: str
                The NOL file to insert
            nPos: int
                The position in the list of NOLs at which to insert the new
                NOL
            bReadOnly: int

        """
        pass

    def NolOwn(self, nPos: int, bOwn: int) -> int:
        """
        Sets the ownership of a Named Object Library (NOL)

        Parameters:
            nPos: int
                The position in the list of NOLs of the NOL whose ownership is
                to be changed
            bOwn: int

        """
        pass

    def NolSave(self, nPos: int) -> int:
        """
        Saves a Named Object Library (NOL) file

        Parameters:
            nPos: int
                The position in the list of NOLs of the NOL to be saved
        """
        pass

    def OpenClosestItem(self, x: float, y: float, z: float, r: float, stat: str, filter: str) -> int:  # noqa: E501
        """
        Opens the item closest to a 3D position, within a specified search
        radius, making it the current open Item

        Parameters:
            x: float
                The x coordinate of the position to search from
            y: float
                The y coordinate of the position to search from
            z: float
                The z coordinate of the position to search from
            r: float
                The search radius, in XY units
            stat: str
                The status of Items to be included in the search
            filter: str
                Optionally specifies a named Filter which Items must pass to
                be included in the search
        """
        pass

    def OpenCursorDatasetItem(self, nDataset: int, bookmark: Any) -> int:
        """
        Opens the Item in the named cursor dataset with the given serial
        number, making it the current open Item

        Parameters:
            nDataset: int
                The serial number of the cursor dataset
            bookmark: object
                Any item in a cursor-based dataset will have this property,
                which lets you go back to the underlying data store and find
                the row
        """
        pass

    def OpenCursorItem(self, cursor: str) -> int:
        """
        Opens the item referred to by the current row in the specified cursor

        Parameters:
            cursor: str
                The named cursor from which the item corresponding to the
                current row is to be opened
        """
        pass

    def OpenDatasetItem(self, dataset: str, id: int) -> int:
        """
        Opens the Item in the named dataset with the given ID number, making
        it the current open Item. If the dataset is not open, Cadcorp SIS will
        open it and attempt to own it

        Parameters:
            dataset: str
                The filename of the dataset whose Item is to be opened
            id: int
                The ID number of the Item to be opened
        """
        pass

    def OpenExistingDatasetItem(self, nDataset: int, id: int) -> int:
        """
        Opens an Item from an existing dataset with the given ID number,
        making it the current open Item

        Parameters:
            nDataset: int
                The serial number of the dataset whose Item is to be opened.
                The number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
            id: int
                The ID number of the Item to be opened
        """
        pass

    def OpenFormulaItem(self, nDataset: int, formula: str) -> int:
        """
        Opens an Item within a dataset which matches a formula, making it the
        current open Item

        Parameters:
            nDataset: int
                The serial number of the dataset whose Item is to be opened.
                The number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
            formula: str
                The formula to check dataset Items against. See Property
                Formula Syntax for details
        """
        pass

    def OpenItem(self, id: int) -> int:
        """
        Opens the Item in the current dataset with the given id number, making
        it the current open Item

        Parameters:
            id: int
                The ID number of the Item to be opened
        """
        pass

    def OpenList(self, list: str, n: int) -> int:
        """
        Opens an Item from a Named List, making it the current open Item

        Parameters:
            list: str
                The Named List containing the Item to be opened
            n: int
                The index of the Item in the Named List
        """
        pass

    def OpenListCursor(self, cursor: str, list: str, fields: str) -> int:
        """
        Opens a new cursor containing specified fields for all items in a
        named list

        Parameters:
            cursor: str
                The named cursor to be created with the specified fields for
                all items in an overlay. Any existing cursor with this name
                will be overwritten
            list: str
                The named list containing items from which properties will be
                read to fill the cursor
            fields: str
                The list of fields to be included in the cursor. Field names
                should be as they appear in the formula box within SIS and
                should be TAB-separated
        """
        pass

    def OpenOverlayCursor(self, cursor: str, pos: int, fields: str, bForwardOnly: int) -> int:  # noqa: E501
        """
        Opens a new cursor containing specified fields for all items in an
        overlay

        Parameters:
            cursor: str
                The named cursor to be created with the specified fields for
                all items in an overlay. Any existing cursor with this name
                will be overwritten
            pos: int
                The position in the overlays list of the overlay from which to
                fill the cursor
            fields: str
                The list of fields to be included in the cursor. Field names
                should be as they appear in the formula box within SIS and
                should be TAB-separated
            bForwardOnly: int
                True  you can pass forward only through the records (a
                Forward-Only cursor is slightly more efficient)False  you can
                navigate forwards and backwards through the records at will
        """
        pass

    def OpenOverlayItem(self, pos: int, id: int) -> int:
        """
        Opens the Item on an overlay with the given ID number, making it the
        current open Item

        Parameters:
            pos: int
                The position in the overlays list of the overlay containing
                the Item to be opened
            id: int
                The ID number of the Item to be opened
        """
        pass

    def OpenSortedCursor(self, cursor: str, sourceCursor: str, nField: int, bAscending: int) -> int:  # noqa: E501
        """
        Opens a new sorted cursor from an existing named cursor

        Parameters:
            cursor: str
                The cursor created from sourceCursor
            sourceCursor: str
                The name of the cursor being interrogated
            nField: int
                The index number of the field being interrogated
            bAscending: int

        """
        pass

    def OwnDataset(self, dataset: str, bOwn: int) -> int:
        """
        Sets the ownership of a dataset

        Parameters:
            dataset: str
                The filename of the dataset whose ownership is to be changed
            bOwn: int

        """
        pass

    def PauseGpsReplay(self) -> int:
        """
        Pause the replay of the GPS log file currently being replayed
        """
        pass

    def PhotoGrid(self) -> int:
        """
        Sets the default grid on the current open Photo item
        """
        pass

    def PlaceGroup(self, x: float, y: float, z: float) -> int:
        """
        Places the current open Group item, at a given position, leaving it
        open

        Parameters:
            x: float
                The x coordinate position at which to place the new Group
                item
            y: float
                The y coordinate position at which to place the new Group
                item
            z: float
                The z coordinate position at which to place the new Group
                item
        """
        pass

    def PlacePrintTemplate(self, ptemplate: str, a: float, s: float) -> int:
        """
        Places a Print Template in the current SIS Workspace Definition (SWD),
        filling it with the previously composed window created by the Compose
        method.

        Parameters:
            ptemplate: str
                The name of a Print Template object stored in a previously
                loaded Named Object Library
            a: float
                The angle, in radians, of the placed Print Template
            s: float
                The scale of the placed Print Template
        """
        pass

    def Process(self, cursor: str, process: str) -> int:
        """

        Parameters:
            cursor: str

            process: str

        """
        pass

    def ProcessItem(self, process: str) -> int:
        """

        Parameters:
            process: str

        """
        pass

    def RecallNolItem(self, item: str) -> int:
        """
        Create an Item from an Item stored in a Named Object Library

        Parameters:
            item: str
                The named Item to recall
        """
        pass

    def RecallNolView(self, view: str) -> int:
        """
        Recalls a named View from a Named Object Library

        Parameters:
            view: str
                The named View to recall
        """
        pass

    def RefreshDataset(self, nDataset: int) -> int:
        """
        Makes sure that a dataset is up-to-date

        Parameters:
            nDataset: int
                The serial number of the dataset to refresh. The serial number
                can be obtained from the Dataset property of an overlay, or
                from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
        """
        pass

    def RefreshOverlayJoinTable(self, pos: int) -> int:
        """
        Refreshes the joined overlay and table view

        Parameters:
            pos: int
                The position of the overlay in the overlays list to be
                refreshed
        """
        pass

    def RegisterGroupType(self, clsName: str) -> int:
        """
        Registers a sub-class of a Group, which the users cannot directly
        modify. The registered group sub-class is used by CreateGroup

        Parameters:
            clsName: str
                The class of the group to register
        """
        pass

    def RemoveAtt(self, mnem: str) -> int:
        """
        Removes an attribute from the current open Item. This method is
        similar to the RemoveProperty method, but can only operate on Items

        Parameters:
            mnem: str
                The name of the user-defined attribute to be removed
        """
        pass

    def RemoveFeatureCode(self, fcode: int) -> int:
        """
        Removes an existing feature code from the currently loaded Feature
        Table. Use LoadFeatureTable to load a Feature Table for editing

        Parameters:
            fcode: int
                The feature code to remove, from 1 to 65535
        """
        pass

    def RemoveFromList(self, list: str) -> int:
        """
        Removes the current open Item from a Named List

        Parameters:
            list: str
                The Named List containing the Item to be removed
        """
        pass

    def RemoveListAtt(self, list: str, mnem: str) -> int:
        """
        Removes an attribute from all of the items in a named list

        Parameters:
            list: str
                The named list to query
            mnem: str
                The name of the attribute to remove
        """
        pass

    def RemoveOverlay(self, pos: int) -> int:
        """
        Remove an overlay from the current SIS Workspace Definition (SWD),
        deleting it if it is an internal overlay. If the dataset has been
        modified, all edits since the last save will be lost

        Parameters:
            pos: int
                The position in the overlays list of the overlay to be
                removed
        """
        pass

    def RemoveOverlayTheme(self, pos: int, nTheme: int) -> int:
        """
        Removes a Theme from an overlay in the current SIS Workspace
        Definition (SWD)

        Parameters:
            pos: int
                The position of the overlay in the overlays list from which
                the Theme is to be removed
            nTheme: int
                The index of the Theme, starting at 0. Use the Number of
                themes property to find out the number of Theme objects in an
                overlay
        """
        pass

    def RemoveProperty(self, objectType: int, nObject: int, propertyName: str) -> int:  # noqa: E501
        """
        Removes a property from an object. This method is similar to the
        RemoveAtt method, but can operate on all object types

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The property to remove. Only user defined attributes can be
                removed in this way
        """
        pass

    def RemoveSchemaColumn(self, nColumn: int) -> int:
        """
        Removes an existing column from the currently loaded Schema

        Parameters:
            nColumn: int
                The Schema column to remove
        """
        pass

    def ReorderOverlay(self, oldPos: int, newPos: int) -> int:
        """
        Changes the order of overlays

        Parameters:
            oldPos: int
                The position in the list of overlays of the overlay to be
                reordered
            newPos: int
                The position in the overlays list at which to re-insert the
                overlay. If this argument specifies a position in the existing
                overlays then the reordered overlay will not replace the
                existing overlay at the given position, but will shuffle any
                other overlays down the list
        """
        pass

    def ReplayGpsLog(self, filename: str, replayrate: int, flags: int) -> int:
        """
        Start or resume the replay a GPS log file

        Parameters:
            filename: str
                The name of the GPS log file to replay, or blank to resume
                after a pause
            replayrate: int
                The rate, in milliseconds, to replay the GPS log file, or zero
                to resume after a pause
            flags: int
                Flags setting the NMEA options for receiving data from the GPS
                device.There are three NMEA sentences of interest
        """
        pass

    def RollbackDatasetTransaction(self, nDataset: int) -> int:
        """
        End a transaction by rolling-back (discarding) all changes made since
        the transaction began

        Parameters:
            nDataset: int
                The serial number of the dataset for which the transaction is
                to be rolled-back
        """
        pass

    def RubberSheetRaster(self) -> int:
        """
        Applies the current Rubber Sheet Transformation to the currently open
        Bitmap item
        """
        pass

    def RubberSheetVector(self, list: str) -> int:
        """
        Transforms the items in a named list with the current Rubber Sheet

        Parameters:
            list: str
                The named list containing the items to be transformed
        """
        pass

    def SaveBitmap(self, filename: str, typeBitmap: int) -> int:
        """
        Saves the current open Bitmap item to a file

        Parameters:
            filename: str
                The named of the saved file
            typeBitmap: int
                The bitmap format to use
        """
        pass

    def SaveDataset(self, dataset: str) -> int:
        """
        Saves a dataset if it has been modified

        Parameters:
            dataset: str
                The name of the dataset to save
        """
        pass

    def SetAxesAngle(self, a: float) -> int:
        """
        Rotates the axes to an angle

        Parameters:
            a: float
                The axes rotation angle, in degrees. This value is absolute
        """
        pass

    def SetAxesNormal(self) -> int:
        """
        Resets the axes to the origin and orientation of the underlying CRS
        """
        pass

    def SetAxesPrj(self, crs: str) -> int:
        """
        Sets the current axes CRS

        Parameters:
            crs: str
                The named CRS to use. This can be any named CRS previously
                created using DefineNolPrjLatLon or DefineNolPrjTm, or loaded
                from a Named Object Library
        """
        pass

    def SetCombinedFilterClause(self, filter: str, aclass: str, flag: int, clause: str) -> int:  # noqa: E501
        """
        Adds a clause to a named Combined Class/Property filter

        Parameters:
            filter: str
                The named Combined Class/Property filter to edit, previously
                created using CreateCombinedFilter
            aclass: str
                The Item class which this clause will affect
            flag: int

            clause: str
                The property clause, eg "_closed&=-1"
        """
        pass

    def SetCoordUnits(self, ndim: int, units: int, places: int) -> int:
        """
        Changes the preferred angle, linear, area or volume units used in the
        user interface

        Parameters:
            ndim: int

            units: int
                The units to use. Valid values are
            places: int
                The number of decimal places to display, in the range 0 to 15
        """
        pass

    def SetDatasetPrj(self, nDataset: int, crs: str) -> int:
        """
        Sets a dataset CRS

        Parameters:
            nDataset: int
                The serial number of the dataset whose CRS is to be set. The
                serial number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
            crs: str
                The named CRS to use
        """
        pass

    def SetFlt(self, objectType: int, nObject: int, propertyName: str, value: float) -> int:  # noqa: E501
        """
        Sets the value of a floating point property

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property. All floating point properties end in
                '#'
            value: float
                The new floating point value of the property
        """
        pass

    def SetGazetteerView(self, clsGazetteer: str, parameters: str) -> int:
        """
        Finds and zooms to a location using a Plug-in Gazetteer

        Parameters:
            clsGazetteer: str
                The name of the Plug-in Gazetteer
            parameters: str
                The parameters for the search
        """
        pass

    def SetGeomPt(self, nGeom: int, nPt: int, x: float, y: float, z: float) -> int:  # noqa: E501
        """
        Sets the position of a vertex in the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
            nPt: int
                The index of the vertex, starting at 0. Use GetGeomNumPt to
                get the number of vertices in a geometry component
            x: float
                The x coordinate of the new position of the given vertex
            y: float
                The y coordinate of the new position of the given vertex
            z: float
                The z coordinate of the new position of the given vertex
        """
        pass

    def SetGeomSegBulge(self, nGeom: int, nSeg: int, bulge: float) -> int:
        """
        Sets the bulge value of a segment in the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
            nSeg: int
                The index of the segment within the current open Item. The
                indices run from 1 to GetGeomNumSeg - 1, eg a LineString item
                with two points has one segment, index 1
            bulge: float
                The new bulge value of the given segment. The bulge factor is
                the tangent of one quarter of the swept angle. A bulge factor
                of 0.0 implies a straight segment
        """
        pass

    def SetGridItemValue(self, x: float, y: float, z: float, v: float) -> int:
        """
        Sets the value in a cell of the current open Grid item. Grid cell
        values can be queried using GetGridItemValue

        Parameters:
            x: float
                The x coordinate position at which to set the Grid item value
            y: float
                The y coordinate position at which to set the Grid item value
            z: float
                The z coordinate position at which to set the Grid item value
            v: float
                The new value for the Grid cell
        """
        pass

    def SetInt(self, objectType: int, nObject: int, propertyName: str, value: int) -> int:  # noqa: E501
        """
        Sets the value of an integer property

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property. All integer properties end in '&'
            value: int
                The new integer value of the property
        """
        pass

    def SetListFlt(self, list: str, propertyName: str, value: float) -> int:
        """
        Sets the value of a floating point property on the Items in a Named
        List

        Parameters:
            list: str
                The Named List containing the Items whose property is to be
                set
            propertyName: str
                The name of the property. All floating point properties end in
                '#'
            value: float
                The new floating point value of the property
        """
        pass

    def SetListFormula(self, list: str, propertyName: str, formula: str) -> int:  # noqa: E501
        """
        Sets the value of a property on items is a Named List, using the
        result of a formula

        Parameters:
            list: str
                The Named List containing the items whose property is to be
                set
            propertyName: str
                The name of the property or attribute to set
            formula: str
                The formula to evaluate and apply the result as the named
                property
        """
        pass

    def SetListInt(self, list: str, propertyName: str, value: int) -> int:
        """
        Set the value of an integer property on the Items in a Named List

        Parameters:
            list: str
                The Named List containing the Items whose property is to be
                set
            propertyName: str
                The name of the property. All integer properties end in '&'
            value: int
                The new integer value of the property
        """
        pass

    def SetListProperty(self, list: str, propertyName: str, value: Any) -> int:
        """
        Set the value of a property on the items in a named list

        Parameters:
            list: str
                The named list containing the items whose property is to be
                set
            propertyName: str
                The name of the property
            value: object
                The value of the property
        """
        pass

    def SetListStr(self, list: str, propertyName: str, value: str) -> int:
        """
        Set the value of a floating point property on the Items in a Named
        List

        Parameters:
            list: str
                The Named List containing the Items whose property is to be
                set
            propertyName: str
                The name of the property. All string properties end in '$'
            value: str
                The new string value of the property
        """
        pass

    def SetOverlayDataset(self, pos: int, nDataset: int) -> int:
        """
        Sets the Dataset of an overlay in the current swd

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose dataset
                is to be set
            nDataset: int
                The serial number of the dataset to be used. The number can be
                obtained from the Dataset property of an overlay, or from the
                GetDataset, GetDatasetContainer or FindExternalDataset
                methods
        """
        pass

    def SetOverlayFilter(self, pos: int, filter: str) -> int:
        """
        Applies a copy of a named Filter to an overlay in the current SIS
        Workspace Definition (SWD)

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose drawing
                Filter is to be set
            filter: str
                The named Filter to copy. This can be any previously created
                named Filter, or a Filter loaded from a Named Object Library,
                or "" to unset the overlay drawing Filter
        """
        pass

    def SetOverlayJoinTable(self, pos: int, rs: str, formula: str, tablecolumn: str, bOneToMany: int) -> int:  # noqa: E501
        """
        Sets a join between an overlay and a table

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose Tables
                are to be joined
            rs: str
                A named recordset previously created using DefineRecordset
            formula: str
                The formula to join from
            tablecolumn: str
                The table column to join to
            bOneToMany: int
                If one column in a table is to relate to many columns in
                another table
        """
        pass

    def SetOverlayLocus(self, pos: int, locus: str) -> int:
        """
        Applies a copy of a named Locus to an overlay in the current SIS
        Workspace Definition (SWD)

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose drawing
                Locus is to be set
            locus: str
                The named Locus to copy. This can be any named Locus
                previously created, or loaded from a Named Object Library, or
                "" to unset the overlay drawing Locus
        """
        pass

    def SetOverlaySchema(self, pos: int, schema: str) -> int:
        """
        Applies a copy of a named Schema to an overlay in the current SIS
        Workspace Definition (SWD)

        Parameters:
            pos: int
                The position of the overlay in the overlays list whose Schema
                is to be set
            schema: str
                The named Schema to copy. This can be any named Schema
                previously created, or loaded from a Named Object Library, or
                "" to unset the overlay Schema
        """
        pass

    def SetPhotoWorldCentre(self, x: float, y: float, z: float) -> int:
        """
        Sets the centre of the view within the current open Photo item

        Parameters:
            x: float
                The x coordinate of the new centre of the Photo view, in Photo
                world coordinates
            y: float
                The y coordinate of the new centre of the Photo view, in Photo
                world coordinates
            z: float
                The z coordinate of the new centre of the Photo view, in Photo
                world coordinates
        """
        pass

    def SetProfileStr(self, propertyName: str, value: str) -> int:
        """
        Sets the value of a string profile property

        Parameters:
            propertyName: str
                The name of the property. All string properties end in '$'.
                The special properties "_properties$" and "_properties_edit$"
                are used to get lists of available properties for querying and
                editing respectively
            value: str
                The value of the property
        """
        pass

    def SetProperty(self, objectType: int, nObject: int, propertyName: str, value: Any) -> int:  # noqa: E501
        """
        Sets the value of a property. Note: Not available if using
        Cadcorp.SIS.GisLink.dll

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property
            value: object
                The value of the property
        """
        pass

    def SetRubberTransform(self, method: int) -> int:
        """
        Sets the current Rubber Sheet Transformation from the currently open
        Rubber Sheet item. This method must be used before transforming Raster
        or Vector data

        Parameters:
            method: int
                The displacement method to use
        """
        pass

    def SetStr(self, objectType: int, nObject: int, propertyName: str, value: str) -> int:  # noqa: E501
        """
        Sets the value of a string property

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property. All string properties end in '$'
            value: str
                The new string value of the property
        """
        pass

    def SetUnits(self, units: str, places: int) -> int:
        """
        Sets the preferred units used in the user interface

        Parameters:
            units: str
                A string describing the units
            places: int
                The number of decimal places
        """
        pass

    def SetViewExtent(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> int:  # noqa: E501
        """
        Sets the visible extents of the current Map Window

        Parameters:
            x1: float
                The new first x coordinate of the rectangular extents of the
                view
            y1: float
                The new first y coordinate of the rectangular extents of the
                view
            z1: float
                The new first z coordinate of the rectangular extents of the
                view
            x2: float
                The new second x coordinate of the rectangular extents of the
                view
            y2: float
                The new second y coordinate of the rectangular extents of the
                view
            z2: float
                The new second z coordinate of the rectangular extents of the
                view
        """
        pass

    def SetViewPrj(self, projection: str) -> int:
        """
        Sets the viewing projection of the current Map Window

        Parameters:
            projection: str
                The named CRS to use
        """
        pass

    def SimplifyGeom(self) -> int:
        """
        Simplifies the geometry of the current open Item.The meaning of Simple
        geometry is that defined by the Open Geospatial Consortium (OGC)
        consortium
        """
        pass

    def SliceGeometry(self, list: str) -> int:
        """
        Slice through LineString and Polygon items, cutting them into pieces

        Parameters:
            list: str
                The named list storing LineString and Polygon items which are
                to be sliced. On completion, the list will store only any
                LineStrings and Polygons created by the slice
        """
        pass

    def SnipGeometry(self, list: str, bInside: int) -> int:
        """
        Snips away portions of the Items inside or outside the current Item

        Parameters:
            list: str
                The Named List containing the Items to be snipped
            bInside: int

        """
        pass

    def SnipTin(self, list: str) -> int:
        """
        To snip out the part of current open TIN that does not overlap the
        given Polygon

        Parameters:
            list: str
                The Named List containing the snipping polgons. These must be
                two-dimensional and be completely inside the TIN
        """
        pass

    def StartGpsLog(self, filename: str) -> int:
        """
        Start logging the data being read from the currently connected GPS
        device or log file being replayed

        Parameters:
            filename: str
                The name of the text file to receive the log
        """
        pass

    def StopGpsLog(self) -> int:
        """
        Stop the logging of GPS data
        """
        pass

    def StopGpsReplay(self) -> int:
        """
        Stop replaying the GPS log file currently being replayed
        """
        pass

    def StoreAsArea(self) -> int:
        """
        Stores the previous MoveTo / LineTo operations as a Polygon item
        """
        pass

    def StoreAsLine(self) -> int:
        """
        Stores the previous MoveTo / LineTo operations as a LineString
        item.This method is an alternative to using MoveTo to store the
        previous MoveTo/LineTo operations
        """
        pass

    def StoreFeatureTable(self, ftable: str) -> int:
        """
        Stores the currently open Feature Table in a Named Object Library,
        replacing any existing Feature Table with the same name

        Parameters:
            ftable: str
                The name of the Feature Table to create, or replace
        """
        pass

    def StoreSchema(self, schema: str) -> int:
        """
        Stores the currently open Schema in a Named Object Library, replacing
        any existing Schema with the same name

        Parameters:
            schema: str
                The name of the Schema to create, or replace
        """
        pass

    def StoreTheme(self, theme: str) -> int:
        """
        Stores the currently open Theme in a Named Object Library, replacing
        any existing Theme with the same name

        Parameters:
            theme: str
                The name of the Theme to create, or replace
        """
        pass

    def SubdivideTin(self, nIterations: int) -> int:
        """
        Subdivides the current open TIN item's faces using smooth
        interpolation

        Parameters:
            nIterations: int
                The number of times the interpolation procedure is to be
                carried out
        """
        pass

    def TopoClean(self, list: str, tolerance: float, options: int) -> int:
        """
        Cleans up topological Link Items

        Parameters:
            list: str
                The Named List containing the Link Items to be cleaned
            tolerance: float
                The tolerance to use. Link Items whose length is less than
                this value will be removed. If SIS_CLEAN_TOPO_FIX_UNDER_OVER
                is specified then Link Items with a dangling end will be
                joined to another Link item within this distance
            options: int

        """
        pass

    def TopoCombineNamedSeeds(self, seedOutput: str, seed1: str, seed2: str, boolop: int) -> int:  # noqa: E501
        """
        Creates a Named Seed object by using a Boolean operation on an
        existing Named Seed Object

        Parameters:
            seedOutput: str
                The new Named Seed object, which will be a TopoPolygon item
            seed1: str
                The Named Seed object, which must be a TopoPolygon Item in the
                same dataset, to combine
            seed2: str
                The Named Seed object, which must be a TopoPolygon Item in the
                same dataset, to combine
            boolop: int

        """
        pass

    def TopoConvertToArea(self, bDeleteUnusedLinks: int) -> int:
        """
        Converts the current open TopoPolygon item into a Polygon item

        Parameters:
            bDeleteUnusedLinks: int

        """
        pass

    def TopoConvertToChain(self, category: str) -> int:
        """
        Converts the current open LineString item into a topological
        TopoLineString item. This method will insert Node Items at the start
        and end of the TopoLineString item, and at any intersections with
        existing Link Items

        Parameters:
            category: str
                The category of the new TopoLineString item
        """
        pass

    def TopoConvertToLine(self, bDeleteUnusedLinks: int) -> int:
        """
        Converts the current open TopoLineString item into a LineString item

        Parameters:
            bDeleteUnusedLinks: int

        """
        pass

    def TopoConvertToPolygon(self, category: str) -> int:
        """
        Converts the current open Polygon or MultiPolygon item into a
        topological TopoPolygon item

        Parameters:
            category: str
                The category of the new TopoPolygon item
        """
        pass

    def TopoCreateArea(self) -> int:
        """
        Creates a Polygon item from the current open TopoPolygon item, which
        may be read-only
        """
        pass

    def TopoCreateBoolean(self, seed: str, list: str, boolop: int) -> int:
        """
        Creates a Named Seed object by doing a fast Boolean operation with
        existing TopoPolygon Items

        Parameters:
            seed: str
                The new Named Seed object, which will be a TopoPolygon item
            list: str
                A Named List containing the TopoPolygon Items, which must all
                be in the same dataset, to combine
            boolop: int

        """
        pass

    def TopoCreateChain(self, seed: str, category: str) -> int:
        """
        Creates a TopoLineString item from a Named Seed object

        Parameters:
            seed: str
                The Named Seed object from which the TopoLineString item will
                be created
            category: str
                The category of the new TopoLineString item
        """
        pass

    def TopoCreateEmptyNamedSeed(self, seed: str, nDataset: int) -> int:
        """
        Creates a new, empty transient Named Seed object

        Parameters:
            seed: str
                The name of the new Named Seed object
            nDataset: int
                The serial number of the topological dataset. The serial
                number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, FindExternalDataset or
                TopoGetNamedSeedDataset methods
        """
        pass

    def TopoCreateLine(self) -> int:
        """
        Create a LineString item from the current open TopoLineString item,
        which may be read-only
        """
        pass

    def TopoCreateLink(self) -> int:
        """
        Creates a topological Link item, copying the geometry from the current
        LineString item
        """
        pass

    def TopoCreateNamedSeed(self, seed: str) -> int:
        """
        Creates a transient Named Seed object from the current TopoPolygon or
        TopoLineString item

        Parameters:
            seed: str
                The name of the new Named Seed object
        """
        pass

    def TopoCreateNode(self, x: float, y: float, z: float) -> int:
        """
        Creates a Node item, merging it in to any existing topology

        Parameters:
            x: float
                The x coordinate of the position at which to create the new
                Node item
            y: float
                The y coordinate of the position at which to create the new
                Node item
            z: float
                The z coordinate of the position at which to create the new
                Node item
        """
        pass

    def TopoCreatePoint(self, idNode: int, nDataset: int) -> int:
        """
        Creates a Point item, merging it in to any exisiting topology

        Parameters:
            idNode: int
                The id of the node to create
            nDataset: int
                The serial number of the dataset to be scanned. The number can
                be obtained from the Dataset property of an overlay, or from
                the GetDataset, GetDatasetContainer or FindExternalDataset
                methods
        """
        pass

    def TopoCreatePolygon(self, seed: str, category: str) -> int:
        """
        Creates a TopoPolygon item from a Named Seed object

        Parameters:
            seed: str
                The Named Seed object from which the TopoPolygon item will be
                created
            category: str
                The category of the new TopoPolygon item
        """
        pass

    def TopoDeleteLink(self) -> int:
        """
        Deletes the current open Link item
        """
        pass

    def TopoDeleteNamedSeed(self, seed: str) -> int:
        """
        Deletes a transient Named Seed object

        Parameters:
            seed: str
                The Named Seed object to delete
        """
        pass

    def TopoDeleteNode(self) -> int:
        """
        Deletes or simplifies the current open Node item
        """
        pass

    def TopoDeletePoint(self, bSimplifyNode: int) -> int:
        """
        Deletes or simplifies the current open Point item

        Parameters:
            bSimplifyNode: int

        """
        pass

    def TopoDeleteSeed(self, bDeleteUnusedLinks: int) -> int:
        """
        Deletes the current open topological TopoLineString or TopoPolygon
        item

        Parameters:
            bDeleteUnusedLinks: int

        """
        pass

    def TopoGrowNamedSeed(self, seed: str, bStart: int, idLink: int) -> int:
        """
        Adds a Link ID into a Named Seed object

        Parameters:
            seed: str
                The Named Seed object to which the Link item will be added
            bStart: int

            idLink: int
                The ID of the Link item to be added
        """
        pass

    def TopoMoveNode(self, x: float, y: float, z: float) -> int:
        """
        Moves the current open Node item, dragging any connected Link Items

        Parameters:
            x: float
                The x coordinate of the new position of the Node item
            y: float
                The y coordinate of the new position of the Node item
            z: float
                The z coordinate of the new position of the Node item
        """
        pass

    def TopoPolygonsFromLinks(self, list: str) -> int:
        """
        Create topological polygons from the topological links held a named
        list

        Parameters:
            list: str
                The named list of topological links. On completion the list
                will hold the newly created polygons
        """
        pass

    def TopoReverseSeed(self) -> int:
        """
        Reverses the direction of the current open TopoLineString or
        TopoPolygon item
        """
        pass

    def TopoSetChainSeedPt(self, x: float, y: float, z: float) -> int:
        """
        Set or move the seed point of the current

        Parameters:
            x: float
                The x coordinate of the new position of the seed point
            y: float
                The y coordinate of the new position of the seed point
            z: float
                The z coordinate of the new position of the seed point
        """
        pass

    def TopoSetLinkPt(self, nPt: int, x: float, y: float, z: float) -> int:
        """
        Sets the position of a vertex in the current open Link item

        Parameters:
            nPt: int
                The index of the vertex, starting at 0. Use GetGeomPt to get
                the number of vertices in the current Link item
            x: float
                The x coordinate of the new position of the given vertex
            y: float
                The y coordinate of the new position of the given vertex
            z: float
                The z coordinate of the new position of the given vertex
        """
        pass

    def TopoSetPolygonSeedPt(self, x: float, y: float, z: float) -> int:
        """
        Set or move the seed point of the current open topological polygon

        Parameters:
            x: float
                The x coordinate of the new position of the seed point
            y: float
                The y coordinate of the new position of the seed point
            z: float
                The z coordinate of the new position of the seed point
        """
        pass

    def TraceGeom(self, nGeom: int, arclenStart: float, arclenEnd: float, offset: float, bAllowSelfIntersections: int) -> int:  # noqa: E501
        """
        Creates a LineString item by tracing geometry from the current open
        Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
            arclenStart: float
                The length along the geometry component from which to start
                the trace
            arclenEnd: float
                The length along the geometry component at which to end the
                trace
            offset: float
                The offset from the geometry component at which to create the
                LineString item
            bAllowSelfIntersections: int

        """
        pass

    def UpdateCursorItem(self, cursor: str) -> int:
        """
        Updates data held in the specified cursor to reflect any relevant
        changes in the open item

        Parameters:
            cursor: str
                The named cursor to update
        """
        pass

    def UpdateItem(self) -> int:
        """
        Updates the current open Item, leaving it current
        """
        pass

    def UpdateObject(self, url: str, contenttype: str, content: Any) -> int:
        """

        Parameters:
            url: str

            contenttype: str

            content: object

        """
        pass

    def ZoomExtent(self) -> int:
        """
        Zooms the view to the extents of all of the Items in all of the
        visible, hittable and editable overlays
        """
        pass

    def ZoomView(self, f: float) -> int:
        """
        Zooms the current window by a scale factor

        Parameters:
            f: float
                The zooming factor, eg 2.0 to zoom out, or 0.5 to zoom in
        """
        pass

    def CreateItemB(self, blob: Any, crs: str, fmt: int) -> int:
        """
        Creates an Item from Blob data. If a Group is open, then graphics are
        added to the Group, otherwise a new Item is created

        Parameters:
            blob: object
                The stored Item Blob data, stored in an array of bytes, or in
                a stream
            crs: str
                The named CRS of the stored Item Blob
            fmt: int
                The format of the stored item Blob
        """
        pass

    def ActivateWnd(self, number: int) -> int:
        """
        Activates a window by its number, ie make the window the currently
        active child window, and its SIS Workspace Definition (SWD) the
        current SWD

        Parameters:
            number: int
                The number of the window to
        """
        pass

    def GisExit(self, savecode: int) -> int:
        """
        Exit the SIS session, using the given savecode

        Parameters:
            savecode: int

        """
        pass

    def ProjectClose(self, savecode: int) -> int:
        """
        Save and close the current project files

        Parameters:
            savecode: int

        """
        pass

    def ProjectOpen(self, folder: str, savecode: int) -> int:
        """
        Opens a project folder, after saving the existing open project files

        Parameters:
            folder: str
                The project folder to open
            savecode: int

        """
        pass

    def SwdClose(self, savecode: int) -> int:
        """
        Close all of the windows of the current SIS Workspace Definition
        (SWD), using the chosen savecode

        Parameters:
            savecode: int

        """
        pass

    def SwdNew(self) -> int:
        """
        Creates a new, empty SIS Workspace Definition (SWD)
        """
        pass

    def SwdNewWindow(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> int:  # noqa: E501
        """
        Creates a new window based on the current SIS Workspace Definition
        (SWD), with the given view

        Parameters:
            x1: float
                The first x
            y1: float
                The first y
            z1: float
                The first z
            x2: float
                The second x
            y2: float
                The second y
            z2: float
                The second z
        """
        pass

    def SwdNewWindow3D(self, xEye: float, yEye: float, zEye: float, xLook: float, yLook: float, zLook: float) -> int:  # noqa: E501
        """
        Creates a new 3D window based on the current SIS Workspace Definition
        (SWD)

        Parameters:
            xEye: float
                The x
            yEye: float
                The y
            zEye: float
                The z
            xLook: float
                The x
            yLook: float
                The y
            zLook: float
                The z
        """
        pass

    def SwdNewWindowTable(self) -> int:
        """
        Creates a new table window based on the current SIS Workspace
        Definition (SWD)
        """
        pass

    def SwdOpen(self, filename: str, unused: int) -> int:
        """
        Open an existing SIS Workspace Definition (SWD) file, optionally
        making it read-only

        Parameters:
            filename: str
                The full pathname of the SIS Workspace Definition (SWD)
            unused: int

        """
        pass

    def SwdSave(self) -> int:
        """
        Saves the current Swd
        """
        pass

    def SwdSaveAs(self, filename: str) -> int:
        """
        Saves the current SIS Workspace Definition (SWD) with a different
        name. The original file is not renamed but kept on disk

        Parameters:
            filename: str
                The new name for the SIS Workspace Definition (SWD)
        """
        pass

    def UpdateWorkspaceWindow(self) -> int:
        """
        Updates the current SIS Workspace Definition (SWD) in the workspace
        window, eg after changing the status of an overlay
        """
        pass

    def AllowCommands(self, flag: int, listcom: str) -> int:
        """
        Add or remove commands from the menu. To find the ACom equivalent for
        a menu command, turn on the ProgramView tab in the workspace window,
        select the command, and the ACom equivalent will be displayed in the
        window

        Parameters:
            flag: int

            listcom: str
                A list of commands separated by space, comma, tab, or newline
                characters
        """
        pass

    def CallCommand(self, comname: str) -> int:
        """
        Calls a non-interactive, or one-shot command (a command that does not
        require user intervention with the mouse) in the current SIS Workspace
        Definition (SWD)

        Parameters:
            comname: str
                The command to call
        """
        pass

    def Copy(self, list: str, bDelete: int) -> int:
        """
        Copies the Items in a Named List to the clipboard, optionally deleting
        the existing Items, ie Cut instead of Copy

        Parameters:
            list: str
                The Named List whose Items are to be copied
            bDelete: int
                Returns
        """
        pass

    def CreateListFromSelection(self, list: str) -> int:
        """
        Creates a Named List of the currently selected Items

        Parameters:
            list: str
                The Named List to fill with the currently selected Items
        """
        pass

    def DeselectAll(self) -> int:
        """
        Clears the current selection list
        """
        pass

    def DigitiserSnap(self, x: float, y: float, z: float, nButton: int) -> int:
        """
        Send a digitised position into the current command

        Parameters:
            x: float
                The x coordinate of the digitised position
            y: float
                The y coordinate of the digitised position
            z: float
                The z coordinate of the digitised position
            nButton: int
                The number of the digitiser button pressed. This argument is
                currently ignored
        """
        pass

    def DoCommand(self, comname: str) -> int:
        """
        Executes a command

        Parameters:
            comname: str
                The command to execute
        """
        pass

    def DrapeBitmap(self, name: str) -> int:
        """
        Drapes a Bitmap item, stored in a Named Object Library, in the 3D
        Window

        Parameters:
            name: str
                The name of the Bitmap item
        """
        pass

    def DrawList(self, drawcode: int, list: str, pen: str, brush: str, shape: str, font: str) -> int:  # noqa: E501
        """
        Draws Items in a Named List with overridden styles. This only changes
        the display until the next time it is redrawn

        Parameters:
            drawcode: int

            list: str
                The Named List containing the Items to be drawn
            pen: str
                The Pen with which to draw the items
            brush: str
                The Brush with which to fill the items
            shape: str
                The Symbol with which to draw the items
            font: str
                The Font with which to draw the items
        """
        pass

    def ExplodeShape(self, list: str) -> int:
        """
        Converts Point items with shapes into editable items

        Parameters:
            list: str
                The name of the list to explode
        """
        pass

    def Export(self, clsExport: str, filename: str, parameters: str) -> int:
        """
        Exports data using a Plug-in Exporter

        Parameters:
            clsExport: str
                The Plug-in Exporter class to use
            filename: str
                The name of the exported file
            parameters: str
                Optional parameters used to configure the Plug-in Exporter.
                There must be no spaces in parameters
        """
        pass

    def ExportBds(self, filename: str, precision: int) -> int:
        """
        Exports the current view to a Cadcorp Base Dataset (BDS) file

        Parameters:
            filename: str
                The name of the exported file
            precision: int
                The precision of the Items in the exported file.Valid values
                are
        """
        pass

    def ExportBmp(self, filename: str, bMono: int, w: int, h: int) -> int:
        """
        Exports the current view to a Windows Bitmap (BMP) file

        Parameters:
            filename: str
                The name of the exported file
            bMono: int

            w: int
                The width of the bitmap in pixels
            h: int
                The height of the bitmap in pixels
        """
        pass

    def ExportCursorDataset(self, filename: str, pos: int) -> int:
        """
        Exports an overlay to a cursor-based dataset, eg Cacorp Feature
        Database (FDB)

        Parameters:
            filename: str
                The name of the exported file
            pos: int
                The position of the overlay in the overlays list which is to
                be exported
        """
        pass

    def ExportEcw(self, filename: str, w: int, h: int, compression: int) -> int:  # noqa: E501
        """
        Exports the current view to an Earth Resource Mapping Enhanced
        Compression Wavelet (ECW) file

        Parameters:
            filename: str
                The name of the exported file
            w: int
                The width of the ECW image, in pixels
            h: int
                The height of the ECW image, in pixels
            compression: int
                The target compression ratio
        """
        pass

    def ExportGif(self, filename: str, w: int, h: int) -> int:
        """
        Exports the current view to a GIF file

        Parameters:
            filename: str
                The name of the exported file
            w: int
                The width of the GIF image, in pixels
            h: int
                The height of the GIF image, in pixels
        """
        pass

    def ExportJpeg(self, filename: str, w: int, h: int) -> int:
        """
        Exports the current view to a JPEG file

        Parameters:
            filename: str
                The name of the exported file
            w: int
                The width of the bitmap, in pixels
            h: int
                The height of the bitmap, in pixels
        """
        pass

    def ExportList(self, list: str, clsExport: str, filename: str, parameters: str) -> int:  # noqa: E501
        """
        Exports data from a named list using an add-in exporter

        Parameters:
            list: str
                The name of the list containing the items to export
            clsExport: str
                The class of the exported file
            filename: str
                The name of the exported file
            parameters: str
                The parameters of the exported file
        """
        pass

    def ExportPdf(self, filename: str, paperFormat: str, parameters: str) -> int:  # noqa: E501
        """
        Exports the current view to an Adobe PDF file

        Parameters:
            filename: str
                The name of the exported file
            paperFormat: str
                A string describing the paper size, format, resolution and so
                on. See Notes below
            parameters: str
                A comma-separated key-value pair collection. Possible keys
                are
        """
        pass

    def ExportPng(self, filename: str, w: int, h: int) -> int:
        """
        Exports the current view to a Portable Network Graphics (PNG) file

        Parameters:
            filename: str
                The name of the exported file
            w: int
                The width of the bitmap, in pixels
            h: int
                The height of the bitmap, in pixels
        """
        pass

    def ExportRaster(self, clsExport: str, filename: str, parameters: str) -> int:  # noqa: E501
        """
        Exports raster data using a Plug-in Exporter

        Parameters:
            clsExport: str
                The Plug-in Exporter class to use for Export to
            filename: str
                The name of the exported file
            parameters: str
                Optional parameters used to configure the Plug-in Exporter.
                There must be no spaces in Parameters
        """
        pass

    def ExportTiff(self, filename: str, w: int, h: int, tiffType: int, bNormalised: int) -> int:  # noqa: E501
        """
        Exports the current view to a TIFF file

        Parameters:
            filename: str
                The name of the exported file
            w: int
                The width of the TIFF image, in pixels
            h: int
                The height of the TIFF image, in pixels
            tiffType: int
                The compression type to use
            bNormalised: int

        """
        pass

    def ExportVrml(self, filename: str) -> int:
        """
        Exports the current view to a VRML file

        Parameters:
            filename: str
                The name of the exported file
        """
        pass

    def ExportWmf(self, filename: str) -> int:
        """
        Export the current view to a Windows Metafile (WMF) file

        Parameters:
            filename: str
                The name of the exported file
        """
        pass

    def Message(self, message: str) -> int:
        """
        Shows a message in the message panel of the main frame window

        Parameters:
            message: str
                The message to display
        """
        pass

    def OpenSel(self, nsel: int) -> int:
        """
        Opens an Item in the current selection list, making it the current
        open Item

        Parameters:
            nsel: int
                The index of the Item in the selection list
        """
        pass

    def Paste(self) -> int:
        """
        Pastes the contents of the Windows clipboard into the current
        overlay.N.B
        """
        pass

    def PasteFrom(self, filename: str, bLinked: int) -> int:
        """
        Pastes a file into the current SIS Workspace Definition (SWD)

        Parameters:
            filename: str
                The filename to paste
            bLinked: int

        """
        pass

    def Prompt(self, prompt: str) -> int:
        """
        Set the prompt to be displayed in the prompt panel of the main frame
        window when GetPos or GetPosEx is used

        Parameters:
            prompt: str
                The prompt to display
        """
        pass

    def Publish(self, clsPublish: str, filename: str, parameters: str) -> int:
        """

        Parameters:
            clsPublish: str

            filename: str

            parameters: str

        """
        pass

    def Redraw(self, redrawcode: int) -> int:
        """
        Redraws a window, or windows

        Parameters:
            redrawcode: int

        """
        pass

    def RedrawExtent(self, redrawcode: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> int:  # noqa: E501
        """
        Redraws a window, or windows

        Parameters:
            redrawcode: int

            x1: float
                The first x coordinate of the cuboid extent to be redrawn
            y1: float
                The first y coordinate of the cuboid extent to be redrawn
            z1: float
                The first z coordinate of the cuboid extent to be redrawn
            x2: float
                The second x coordinate of the cuboid extent to be redrawn
            y2: float
                The second y coordinate of the cuboid extent to be redrawn
            z2: float
                The second z coordinate of the cuboid extent to be redrawn
        """
        pass

    def ScrollView(self, dx: int, dy: int) -> int:
        """
        Scrolls the current window by a number of pixels

        Parameters:
            dx: int
                The number of pixels to scroll horizontally
            dy: int
                The number of pixels to scroll vertically
        """
        pass

    def SelectAll(self) -> int:
        """
        Selects all hittable and editable Items
        """
        pass

    def SelectItem(self) -> int:
        """
        Toggles the selection status of the current open Item, ie add it to
        the selection list if it is not selected, and remove it from the
        selection list if it is selected
        """
        pass

    def SelectList(self, list: str) -> int:
        """
        Toggles the selection status of Items in a Named List, ie add an Item
        to the selection list if it is not selected, and remove it from the
        selection list if it is selected

        Parameters:
            list: str
                The Named List containing the Items to have their selection
                status toggled
        """
        pass

    def SendPrint(self, driver: str, device: str, outputName: str, forceColour: int, fStretch: float) -> int:  # noqa: E501
        """
        Prints the current window

        Parameters:
            driver: str
                The printer driver
            device: str
                The printer device name
            outputName: str
                The printer output port
            forceColour: int

            fStretch: float
                The scaling factor to apply to the print in order to make it
                fit onto the printer paper
        """
        pass

    def Set3DView(self, bSetView0: int, xEye: float, yEye: float, zEye: float, xLook: float, yLook: float, zLook: float) -> int:  # noqa: E501
        """
        Sets the eye and look position in a 3D Window

        Parameters:
            bSetView0: int

            xEye: float
                The x coordinate of the eye position
            yEye: float
                The y coordinate of the eye position
            zEye: float
                The z coordinate of the eye position
            xLook: float
                The x coordinate of the look position
            yLook: float
                The y coordinate of the look position
            zLook: float
                The z coordinate of the look position
        """
        pass

    def SetAxesGrid(self, x: float, y: float, bShowGrid: int, bShowPoints: int, bAllowSnaps: int) -> int:  # noqa: E501
        """
        Shows/hides a grid of points or lines with optional snapping

        Parameters:
            x: float
                The x axis grid spacing
            y: float
                The y axis grid spacing
            bShowGrid: int

            bShowPoints: int

            bAllowSnaps: int

        """
        pass

    def SetDefaultPrj(self, crs: str) -> int:
        """
        Sets the default viewing projection and axes CRS

        Parameters:
            crs: str
                The named CRS to use
        """
        pass

    def SetViewHome(self, view: str) -> int:
        """
        Set the "home" view of the Map Window

        Parameters:
            view: str
                The named view to set as the "home" view
        """
        pass

    def ShowNolObjectDialog(self, nPos: int, aclass: str, name: str, bReadonly: int) -> int:  # noqa: E501
        """
        Shows the edit dialog for an object in a Named Object Library (NOL)

        Parameters:
            nPos: int
                The position in the list of NOLs of the NOL containing the
                named object to show the edit dialog
            aclass: str
                The destination position in the list of NOLs of the NOL of the
                named object for which the edit dialog is to be displayed. See
                Named Object Library Classes for valid classes
            name: str
                The named object to display the edit dialog
            bReadonly: int

        """
        pass

    def Snap(self, x: float, y: float, z: float) -> int:
        """
        Supplies a position to the current callback command

        Parameters:
            x: float
                The x coordinate of the position
            y: float
                The y coordinate of the position
            z: float
                The z coordinate of the position
        """
        pass

    def SwitchCommand(self, comname: str) -> int:
        """
        Queues a command which requires mouse input (a callback command) for
        the current window and return immediately. The command will be started
        in the current window when Release has been called, after which its
        progress may be monitored using triggers

        Parameters:
            comname: str

        """
        pass

    def CreateObject(self, url: str, contenttype: str, content: Any) -> int:
        """
        Parameters:
            url: str

            contenttype: str

            content: object

        """
        pass

    def DefineRecordset(self, rs: str, connect: str, tables: str, columns: str, aliases: str, sqlwhere: str) -> int:  # noqa: E501
        """
        Defines a named recordset, for use with databases, replacing any
        existing recordset with the same name

        Parameters:
            rs: str
                The named recordset to create, or replace
            connect: str
                The connect argument enables SIS to connect to the database
                containing the data to be mapped. The methods you can use to
                connect to a database are
            tables: str
                A comma-delimited list of tables which contain the columns
                referred to in the columns argument
            columns: str
                A comma-delimited list of columns which contain the data which
                will be available when the named recordset is used
            aliases: str
                A comma-delimited list of aliases for the columns referred to
                in the columns argument
            sqlwhere: str
                An optional SQL WHERE expression, eg "(Table.StatusColumn =
                'Pending' Or Table.StatusColumn = 'Agreed')". This expression
                should be wholly self-contained, using brackets if they are
                supported in the database, because under some circumstances,
                eg if a Spatial Reference is being used, SIS automatically
                generates a WHERE clause, with this expression appended using
                "And".Note
        """
        pass

    def DescribeObject(self, url: str) -> int:
        """

        Parameters:
            url: str

        """
        pass

    def Evaluate(self, objectType: int, nObject: int, formula: str) -> int:
        """
        Evaluates a formula

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            formula: str
                The formula to evaluate. See Property Formula Syntax for
                details
        """
        pass

    def EvaluateFlt(self, objectType: int, nObject: int, formula: str) -> int:
        """
        Evaluates a formula which has a floating point result

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            formula: str
                The formula to evaluate. See Property Formula Syntax for
                details
        """
        pass

    def EvaluateInt(self, objectType: int, nObject: int, formula: str) -> int:
        """
        Evaluates a formula which has an integer result

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            formula: str
                The formula to evaluate. See Property Formula Syntax for
                details
        """
        pass

    def EvaluateStr(self, objectType: int, nObject: int, formula: str) -> int:
        """
        Evaluates a formula which has a string result

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            formula: str
                The formula to evaluate. See Property Formula Syntax for
                details
        """
        pass

    def Execute(self, sql: str) -> int:
        """

        Parameters:
            sql: str

        """
        pass

    def FindDatasetOverlay(self, nDataset: int, pos: int, bForwards: int) -> int:  # noqa: E501
        """
        Finds an overlay which contains the given dataset

        Parameters:
            nDataset: int
                The serial number of the dataset to be matched. The serial
                number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
            pos: int
                The position in the list of overlays from which to calculate
                the search start (see bForwards, below). If set to -1 then the
                entire list is searched in the order specified by bForwards
            bForwards: int

        """
        pass

    def FindExternalDataset(self, dataset: str) -> int:
        """
        Gets the serial number of a dataset which is already open

        Parameters:
            dataset: str
                The name of the dataset to find
        """
        pass

    def GetAxesAngle(self) -> int:
        """
        Gets the angle of the current axes
        """
        pass

    def GetAxesFromLatLonHgt(self, lat: float, lon: float, hgt: float, datum: str) -> int:  # noqa: E501
        """
        Gets the current axes (x,y,z) position from latitude, longitude and
        height above sea-level

        Parameters:
            lat: float
                The latitude of the required position in degrees
            lon: float
                The longitude of the required position in degrees
            hgt: float
                The height of the required position in metres
            datum: str
                The named Geodetic Datum for the lat and lon input arguments.
                This can be any named Geodetic Datum previously created using
                DefineNolDatum, or loaded from a Named Object Library
        """
        pass

    def GetAxesType(self) -> int:
        """
        Find out whether the current axes are cartesian or spherical
        """
        pass

    def GetBlob(self, crs: str, fmt: int, precision: int) -> int:
        """
        Gets a Blob string of the current open Item, within a CRS

        Parameters:
            crs: str
                The named CRS of the returned Blob string
            fmt: int
                The format of the stored item Blob
            precision: int
                For the GeoJSON and OGC WKT formats, this value is interpreted
                as the number of decimal places to print for each coordinate,
                in the range 1-15 inclusive (0 will print the default number
                of decimal places). For other formats, this value is ignored
        """
        pass

    def GetBlobExtent(self, blob: str, crs: str, fmt: int) -> int:
        """
        Gets the extents of a Blob string, within a CRS

        Parameters:
            blob: str
                The stored Item Blob string
            crs: str
                The named CRS of the stored Item Blob
            fmt: int
                The format of the stored Item Blob
        """
        pass

    def GetClassTreeFilterValues(self, filter: str) -> int:
        """
        Get the complete list of class and subclass values for a named class
        tree filter

        Parameters:
            filter: str
                The named class tree filter to interrogate
        """
        pass

    def GetClosestPt(self, x: float, y: float, r: float) -> int:
        """
        Calculate the position on the current open item closest to the
        specified position

        Parameters:
            x: float
                The x coordinate from which the search is made
            y: float
                The y coordinate from which the search is made
            r: float
                The radius within which the closest point must lie
        """
        pass

    def GetClosestVertex(self, x: float, y: float, r: float) -> int:
        """
        Get the vertex on the current open item closest to the specified
        position

        Parameters:
            x: float
                The x coordinate from which the search is made
            y: float
                The y coordinate from which the search is made
            r: float
                The radius within which the closest vertex must lie
        """
        pass

    def GetCoordExtent(self, coordClass: str, coord: str) -> int:
        """
        Gets the extents corresponding to a coordinate format string

        Parameters:
            coordClass: str
                The coordinate format class to use in interpreting the coord
                argument
            coord: str
                The coordinate string, in the format specified by the
                coordClass argument, to be interpreted
        """
        pass

    def GetCoordString(self, coordClass: str, x: float, y: float, z: float) -> int:  # noqa: E501
        """
        Gets the string representation of a position

        Parameters:
            coordClass: str
                The coordinate format class to use in interpreting the x, y, z
                coordinates
            x: float
                The x coordinate position to be converted into the format
                specified by the coordClass argument
            y: float
                The y coordinate position to be converted into the format
                specified by the coordClass argument
            z: float
                The z coordinate position to be converted into the format
                specified by the coordClass argument
        """
        pass

    def GetCoordUnits(self, ndim: int) -> int:
        """
        Gets the preferred angle, linear, area or volume units used in the
        user interface

        Parameters:
            ndim: int

        """
        pass

    def GetCursorFieldDescription(self, cursor: str, nField: int) -> int:
        """
        Get the description of the specified field from a specified cursor

        Parameters:
            cursor: str
                The name of the cursor to be interrogated
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0.Use nField = -1 to get all of the column
                descriptions
        """
        pass

    def GetCursorFieldFlt(self, cursor: str, nField: int) -> int:
        """
        Get the value of a floating point field in the specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
        """
        pass

    def GetCursorFieldFormula(self, cursor: str, nField: int) -> int:
        """
        Get the formula of the specified field in the specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
        """
        pass

    def GetCursorFieldInt(self, cursor: str, nField: int) -> int:
        """
        Get the value of an integer field in the specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
        """
        pass

    def GetCursorFieldStatistics(self, cursor: str, nField: int) -> int:
        """
        Get the statistics for a numeric field in the specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
        """
        pass

    def GetCursorFieldStr(self, cursor: str, nField: int) -> int:
        """
        Get the value of a string field in the specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
        """
        pass

    def GetCursorFieldValue(self, cursor: str, nField: int) -> int:
        """
        Get the value of the field of the specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
        """
        pass

    def GetCursorFieldValues(self, cursor: str, separator: str, nullValue: str) -> int:  # noqa: E501
        """
        Get the values of all fields in the current row of the specified
        cursor

        Parameters:
            cursor: str
                The name of the cursor to query
            separator: str
                The character string to be placed as a separator between the
                fields' values returned
            nullValue: str
                The value to be written to the returned string for any field
                which is null, ie contains no value
        """
        pass

    def GetCursorValues(self, cursor: str, nField: int, nDelta: int, separator: str, nullValue: str) -> int:  # noqa: E501
        """
        Get the values for a single field for a number of rows in the
        specified cursor

        Parameters:
            cursor: str
                The name of the cursor we are interrogating
            nField: int
                The index number of the field we are interrogating, the index
                starts at 0
            nDelta: int
                The number of rows, relative to the current row, for which
                values are to be returned. Enter 0 to include all rows from
                the current row to the end of the cursor
            separator: str
                The character string to be placed as a separator between the
                fields' values returned
            nullValue: str
                The value to be written to the returned string for any field
                which is null, ie contains no value
        """
        pass

    def GetDataset(self) -> int:
        """
        Gets the serial number of the dataset of the current open Item
        """
        pass

    def GetDatasetContainer(self, nDataset: int, nContainer: int) -> int:
        """
        Gets the serial number of the dataset which contains the specified
        dataset (eg in an Index Dataset)

        Parameters:
            nDataset: int
                The serial number of the dataset whose container is required.
                The serial number can be obtained from the Dataset property of
                an overlay, or from the GetDataset or FindExternalDataset
                methods
            nContainer: int
                The index of the container dataset in the datasets list of
                containers (eg if a tile is included in more than one Index
                Dataset, then nContainer% can have the value between 1 and the
                number of datasets)
        """
        pass

    def GetDatasetExtent(self, nDataset: int) -> int:
        """
        Gets the extents of all of the Items in a dataset

        Parameters:
            nDataset: int
                The serial number of the dataset whose extents are required.
                The serial number can be obtained from the Dataset property of
                an overlay, or from the GetDataset, GetDatasetContainer or
                FindExternalDataset methods
        """
        pass

    def GetExtent(self) -> int:
        """
        Gets the extents of the current open Item
        """
        pass

    def GetFeatureFilterBranches(self, filter: str, fcode: int) -> int:
        """
        Gets the feature codes branching from a parent feature code in a named
        Feature Filter

        Parameters:
            filter: str
                The named Feature Filter to query
            fcode: int
                The feature code whose children are to be queried, from 0 to
                65535. Use 0 to query the top-level feature codes
        """
        pass

    def GetFeatureFilterCodes(self, filter: str) -> int:
        """
        Get the complete list of feature code values for a named feature
        filter

        Parameters:
            filter: str
                The named feature filter to interrogate
        """
        pass

    def GetFeatureFilterTable(self, filter: str) -> int:
        """
        Get the name of the feature table on which the named feature filter is
        based

        Parameters:
            filter: str
                The named feature filter to interrogate
        """
        pass

    def GetFeatureTableBranches(self, fcode: int, bCascade: int) -> int:
        """
        Gets the feature codes branching from a parent feature code in the
        currently loaded Feature Table. Use LoadFeatureTable to load a Feature
        Table for editing

        Parameters:
            fcode: int
                The feature code whose children are to be queried, from 0 to
                65535. Use 0 to query the top-level feature codes
            bCascade: int

        """
        pass

    def GetFilterClass(self, filter: str) -> int:
        """
        Get the class type of a named filter

        Parameters:
            filter: str
                The named filter to interrogate
        """
        pass

    def GetFlt(self, objectType: int, nObject: int, propertyName: str) -> int:
        """
        Gets the value of a floating point property on the given object type

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property. All floating point properties end in
                '#'
        """
        pass

    def GetGeomAngleFromLength(self, nGeom: int, arclen: float) -> int:
        """
        Gets the tangent angle at a specified length along the geometry of the
        current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            arclen: float
                The length along the geometry component
        """
        pass

    def GetGeomDim(self, nGeom: int) -> int:
        """
        Gets the dimension of the geometry from the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
        """
        pass

    def GetGeomIntersections(self, nGeom: int, list: str) -> int:
        """
        Get the positions of intersections of items with the geometry of the
        current open item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            list: str
                The named list containing the items to be checked against the
                geometry component for intersection
        """
        pass

    def GetGeomLength(self, nGeom: int) -> int:
        """
        Gets the length of the geometry from the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
        """
        pass

    def GetGeomLengthUpto(self, nGeom: int, arclenStart: float, x: float, y: float, z: float) -> int:  # noqa: E501
        """
        Gets the length along the geometry of the current open Item up to a
        position

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            arclenStart: float
                The length along the geometry component from which to start
                the measurement. Use -1.0 to measure from the start of the
                geometry
            x: float
                The x coordinate position along the geometry component to
                measure up to
            y: float
                The y coordinate position along the geometry component to
                measure up to
            z: float
                The z coordinate position along the geometry component to
                measure up to
        """
        pass

    def GetGeomNumPt(self, nGeom: int) -> int:
        """
        Gets the number of vertices in the geometry of the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
        """
        pass

    def GetGeomNumSeg(self, nGeom: int) -> int:
        """
        Gets the number of segments in the geometry of the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
        """
        pass

    def GetGeomPosFromLength(self, nGeom: int, arclen: float) -> int:
        """
        Gets the position a specified length along the geometry of the current
        open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
            arclen: float
                The length along the geometry component
        """
        pass

    def GetGeomPt(self, nGeom: int, nPt: int) -> int:
        """
        Gets the position of a vertex from the geometry of the current open
        Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            nPt: int
                The index of the vertex, starting at 0
        """
        pass

    def GetGeomSegAxis(self, nGeom: int, nSeg: int) -> int:
        """
        Gets the axis of a bulged segment within the geometry of the current
        open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            nSeg: int
                The index of the segment within the geometry component
        """
        pass

    def GetGeomSegBulge(self, nGeom: int, nSeg: int) -> int:
        """
        Gets the bulge of a segment within the geometry in the current open
        Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            nSeg: int
                The index of the segment within the geometry component
        """
        pass

    def GetGeomSegShape(self, nGeom: int, nSeg: int) -> int:
        """
        Gets the shape of a segment within the geometry of the current open
        Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            nSeg: int
                The index of the segment within the geometry component
        """
        pass

    def GetGeomSelfIntersection(self, nGeom: int, arclenStart: float) -> int:
        """
        Gets the position of self-intersection of the geometry of the current
        open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0
            arclenStart: float
                The length along the geometry component from which to start
                the search. Use -1.0 to search from the start of the geometry
        """
        pass

    def GetGeomTgtFromLength(self, nGeom: int, arclen: float) -> int:
        """
        Gets the tangent vector at a specified length along the geometry of
        the current open Item

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
            arclen: float
                The length along the geometry of the current open Item
        """
        pass

    def GetGpsPosition(self) -> int:
        """
        Read a position from the currently attached GPS device or GPS log file
        being replayed
        """
        pass

    def GetGridItemValue(self, x: float, y: float, z: float) -> int:
        """
        Gets the value of the cell in the current open Grid item at a
        position. Grid cell values can be set using SetGridItemValue

        Parameters:
            x: float
                The x coordinate position at which to query the Grid item
                value
            y: float
                The y coordinate position at which to query the Grid item
                value
            z: float
                The z coordinate position at which to query the Grid item
                value
        """
        pass

    def GetHook(self) -> int:
        """
        Gets the origin of the current open Item. The origin is also known as
        the hook point
        """
        pass

    def GetImplicitNolObject(self, aclass: str, aname: str) -> int:
        """
        Gets the implicit equivalent of an object in a Named Object
        Library.The implicit string can be used in DefineNolObject to create a
        new named object

        Parameters:
            aclass: str
                The class of named object to be queried. Valid classes are
            aname: str
                The named object whose equivalent implicit string is to be
                queried
        """
        pass

    def GetInt(self, objectType: int, nObject: int, propertyName: str) -> int:
        """
        Gets the value of an integer property on the given object type

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property. All integer properties end in '&'
        """
        pass

    def GetLatLonHgtFromAxes(self, x: float, y: float, z: float, datum: str) -> int:  # noqa: E501
        """
        Gets the latitude, longitude and height above sea-level of an (x,y,z)
        position

        Parameters:
            x: float
                The x coordinate position within the current axes
            y: float
                The y coordinate position within the current axes
            z: float
                The z coordinate position within the current axes
            datum: str
                The named Geodetic Datum to use. This can be any named
                Geodetic Datum previously created using DefineNolDatum, or
                loaded from a Named Object Library
        """
        pass

    def GetLayerFilterValues(self, filter: str) -> int:
        """
        Get the list of layer values specified in a named layer filter

        Parameters:
            filter: str
                The named layer filter to interrogate
        """
        pass

    def GetLinkFilterIds(self, filter: str) -> int:
        """
        Get the list of item IDs specified in a named link filter

        Parameters:
            filter: str
                The named layer filter to interrogate
        """
        pass

    def GetListDetails(self, list: str) -> int:
        """
        Get the dataset serial numbers and item IDs for items in a named list

        Parameters:
            list: str
                The named list whose details are required
        """
        pass

    def GetListExtent(self, list: str) -> int:
        """
        Gets the extents of all of the items in a Named List

        Parameters:
            list: str
                The Named List containing the items whose extents are
                required
        """
        pass

    def GetListItemFlt(self, list: str, n: int, propertyName: str) -> int:
        """
        Gets the value of a floating point property on an item in a Named
        List

        Parameters:
            list: str
                The Named List to query
            n: int
                The index of the item in the Named List
            propertyName: str
                The name of the property. All floating point properties end in
                '#'
        """
        pass

    def GetListItemInt(self, list: str, n: int, propertyName: str) -> int:
        """
        Gets the value of a integer property on an item in a Named List

        Parameters:
            list: str
                The Named List to query
            n: int
                The index of the item in the Named List
            propertyName: str
                The name of the property. All integer properties end in '&'
        """
        pass

    def GetListItemProperty(self, list: str, n: int, propertyName: str) -> int:
        """
        Gets the value of a property on an item in a Named List

        Parameters:
            list: str
                The Named List to query
            n: int
                The index of the item in the Named List
            propertyName: str
                The name of the property
        """
        pass

    def GetListItemStr(self, list: str, n: int, propertyName: str) -> int:
        """
        Gets the value of a string property on an item in a Named List

        Parameters:
            list: str
                The Named List to query
            n: int
                The index of the item in the Named List
            propertyName: str
                The name of the property. All string properties end in '$'
        """
        pass

    def GetListSize(self, list: str) -> int:
        """
        Gets the number of items in a Named List

        Parameters:
            list: str
                The Named List to query
        """
        pass

    def GetNumCursorFields(self, cursor: str) -> int:
        """
        Get the number of fields in the specified cursor

        Parameters:
            cursor: str
                The named cursor to query
        """
        pass

    def GetNumGeom(self) -> int:
        """
        Gets the number of geometry pieces in the current open Item
        """
        pass

    def GetNumNol(self) -> int:
        """
        Gets the number of Named Object Libraries (NOLs) in use
        """
        pass

    def GetOverlayThemeLegend(self, pos: int, nTheme: int, crs: str, fmt: int, precision: int) -> int:  # noqa: E501
        """
        Gets an overlay Theme legend as a Blob string within a CRS

        Parameters:
            pos: int
                The position in the overlays list of the overlay whose Theme
                legend is required
            nTheme: int
                The index of the Theme, starting at 0. Use the Number of
                themes property to find out the number of Theme objects in an
                overlay
            crs: str
                The named CRS of the returned Blob string
            fmt: int

            precision: int
                This parameter is ignored and will always return 64-bit
                precision
        """
        pass

    def GetPhotoWorldPos(self, paperX: float, paperY: float) -> int:
        """
        Gets the world position from a paper position within the current open
        Photo item

        Parameters:
            paperX: float
                The x coordinate of the paper position to convert to a world
                position
            paperY: float
                The y coordinate of the paper position to convert to a world
                position
        """
        pass

    def GetPrjCode(self, crs: str) -> int:
        """
        Gets the EPSG code of a named CRS

        Parameters:
            crs: str
                The named CRS from which to retrieve the EPSG code
        """
        pass

    def GetPrjScaleAtCentre(self, crs: str) -> int:
        """
        Gets the scale at the centre of a named CRS

        Parameters:
            crs: str
                The CRS to query
        """
        pass

    def GetProfileStr(self, propertyName: str, defaultValue: str) -> int:
        """
        Gets the value of a string profile property

        Parameters:
            propertyName: str
                The name of the property. All string properties end in '$'.
                The special properties "_properties$" and "_properties_edit$"
                are used to get lists of available properties for querying and
                editing respectively
            defaultValue: str

        """
        pass

    def GetProperty(self, objectType: int, nObject: int, propertyName: str) -> int:  # noqa: E501
        """
        Gets a property

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property
        """
        pass

    def GetPropertyDescription(self, prop: str) -> int:
        """
        Gets the description of a property

        Parameters:
            prop: str
                The property whose description is required
        """
        pass

    def GetPropertyFilterFormula(self, filter: str) -> int:
        """
        Get the formula specified in a named property filter

        Parameters:
            filter: str
                The named property filter to interrogate
        """
        pass

    def GetShapeExtent(self, shape: str) -> int:
        """
        Gets the extents of a named shape

        Parameters:
            shape: str
                The shape whose extents are required
        """
        pass

    def GetSpatialReference(self, crs: str, span: float) -> int:
        """
        Gets the spatial reference for the current open Item within a spanned
        cube in a CRS

        Parameters:
            crs: str
                The named CRS used in the calculation of the spatial
                reference
            span: float
                The span of the cube used in the calculation of the spatial
                reference
        """
        pass

    def GetSpatialReferenceFromExtent(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, crs: str, span: float) -> int:  # noqa: E501
        """
        Gets the spatial reference for an extents within a spanned cube in a
        CRS

        Parameters:
            x1: float
                The first x coordinate of the cuboid extent to be queried
            y1: float
                The first y coordinate of the cuboid extent to be queried
            z1: float
                The first z coordinate of the cuboid extent to be queried
            x2: float
                The second x coordinate of the cuboid extent to be queried
            y2: float
                The second y coordinate of the cuboid extent to be queried
            z2: float
                The second z coordinate of the cuboid extent to be queried
            crs: str
                The named CRS used in the calculation of the spatial
                reference
            span: float
                The span of the cube used in the calculation of the spatial
                reference
        """
        pass

    def GetStr(self, objectType: int, nObject: int, propertyName: str) -> int:
        """
        Gets the value of a string property

        Parameters:
            objectType: int

            nObject: int
                The index of the object type
            propertyName: str
                The name of the property. All string properties end in '$'.
                The special properties "_properties$" and "_properties_edit$"
                are used to get lists of available properties for querying and
                editing respectively
        """
        pass

    def GetValueListFilterProperty(self, filter: str) -> int:
        """
        Get the property specified in a named value-list filter

        Parameters:
            filter: str
                The named value-list filter to interrogate
        """
        pass

    def GetValueListFilterValues(self, filter: str) -> int:
        """
        Get the list of values specified in a named value-list class

        Parameters:
            filter: str
                The named value-list filter to interrogate
        """
        pass

    def GetViewExtent(self) -> int:
        """
        Gets the visible extents of the current Map Window
        """
        pass

    def IsColumnIndexed(self, nDataset: int, column: str) -> int:
        """

        Parameters:
            nDataset: int

            column: str

        """
        pass

    def IsGeomClockwise(self, nGeom: int) -> int:
        """
        Tests if the geometry of the current open item is clockwise

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
        """
        pass

    def IsGeomClosed(self, nGeom: int) -> int:
        """
        Tests if the geometry of the current open item is closed

        Parameters:
            nGeom: int
                The index of the geometry component, starting at 0. Use
                GetNumGeom to get the number of geometry components in an
                Item
        """
        pass

    def IsOverlayThemeEnabled(self, pos: int, nTheme: int) -> int:
        """
        Checks whether an Overlay theme is currently enabled or disabled

        Parameters:
            pos: int
                The position of the overlay in the overlays list on which the
                theme is to be Queried
            nTheme: int
                The position of the theme in the overlay's theme list which is
                to be queried. Theme indices run from zero to one less than
                the number of themes
        """
        pass

    def MeasureAzimuth(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, datum: str) -> int:  # noqa: E501
        """
        Measures the azimuth between two positions

        Parameters:
            x1: float
                The x coordinate of the start point of the measurement
            y1: float
                The y coordinate of the start point of the measurement
            z1: float

            x2: float
                The x coordinate of the end point of the measurement
            y2: float
                The y coordinate of the end point of the measurement
            z2: float
                The z coordinate of the end point of the measurement
            datum: str
                The Geodetic Datum to do the measuring within
        """
        pass

    def MeasureGreatCircle(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, datum: str) -> int:  # noqa: E501
        """
        Measures the Great Circle distance between two positions

        Parameters:
            x1: float
                The x coordinate of the start point of the measurement
            y1: float
                The y coordinate of the start point of the measurement
            z1: float
                The z coordinate of the start point of the measurement
            x2: float
                The x coordinate of the end point of the measurement
            y2: float
                The y coordinate of the end point of the measurement
            z2: float
                The z coordinate of the end point of the measurement
            datum: str
                The Geodetic Datum to do the measuring within
        """
        pass

    def MeasureRoute(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, formula: str, filter: str, locusNoGo: str, bCreateLine: int) -> int:  # noqa: E501
        """
        Measures the best route between two positions

        Parameters:
            x1: float
                The x coordinate of the start point of the route
            y1: float
                The y coordinate of the start point of the route
            z1: float
                The z coordinate of the start point of the route
            x2: float
                The x coordinate of the end point of the route
            y2: float
                The y coordinate of the end point of the route
            z2: float
                The z coordinate of the end point of the route
            formula: str

            filter: str
                Optionally specifies a named Filter which all items must pass
                to be considered as part of the route
            locusNoGo: str
                Optionally specifies a named Locus through which the route
                cannot pass
            bCreateLine: int

        """
        pass

    def MetreFromStr(self, s: str) -> int:
        """
        Gets a metre dimension from a string, regardless of the units used in
        the string

        Parameters:
            s: str
                The string representation of the dimension
        """
        pass

    def MoveCursor(self, cursor: str, nDelta: int) -> int:
        """
        Move the current row to a new position by moving it forward or
        backward by a specific number of rows. Can be used to loop through the
        rows in a cursor

        Parameters:
            cursor: str
                The named cursor in which the current row is to be moved
            nDelta: int
                The number of lines by which to move the current row. A
                positive number moves the current position forward; a negative
                number moves the current position backward (providing the
                cursor was not opened as forward-only)
        """
        pass

    def MultiRoute(self, list: str, nStart: int, maxNum: int, maxVal: float, rSnap: float, formula: str, filter: str, locusNoGo: str) -> int:  # noqa: E501
        """
        Measures routes between Items in a Named List

        Parameters:
            list: str
                The items to find routes between. The origin of each Item in
                the Named List is used as a potential target location
            nStart: int
                The index within list of the place to start from. The route
                finder will find lots of routes which all start from the
                nStart item
            maxNum: int
                The maximum number of targets to find
            maxVal: float
                The maximum route value to search within
            rSnap: float
                The maximum distance from the start point to a Link item. The
                topological algorithm will spread out from the closest Link
                found. The distance from the point to the closest Link is not
                included in the cost calculation. Ideally, the start point
                should be on a Link item
            formula: str
                The formula, or simple property, to use in the route finding
                calculation as the "cost" of a Link item. For example, using
                the simple property Length will find the shortest route, and
                using the formula "_length#/Speed#", provided each Link has a
                user-defined Speed# property, will find the quickest route.
                Any formula may be used, although if a string formula is used
                it must be a string representation of a numeric value. See
                Property Formula Syntax for details
            filter: str
                Optionally specifies a named Filter which all Link Items must
                pass to be considered as part of the route
            locusNoGo: str
                Optionally specifies a named Locus through which the route
                cannot pass
        """
        pass

    def NolCatalog(self, aclass: str, bCurOnly: int) -> int:
        """
        Lists all of the objects of a given class in all of the Named Object
        Libraries (NOLs)

        Parameters:
            aclass: str
                The class of named object to list
            bCurOnly: int

        """
        pass

    def ReadObject(self, url: str) -> int:
        """

        Parameters:
            url: str

        """
        pass

    def Scan(self, list: str, stat: str, filter: str, locus: str) -> int:
        """
        Scans for items, storing any found in a Named List

        Parameters:
            list: str
                The Named List in which to store any Items found
            stat: str
                The status of Items to be included in the scan
            filter: str
                Optionally specifies a named Filter which items must pass to
                be included in the scan
            locus: str
                Optionally specifies a named Locus which items must pass to be
                included in the scan. Use an empty string to omit the locus
        """
        pass

    def ScanDataset(self, list: str, nDataset: int, filter: str, locus: str) -> int:  # noqa: E501
        """
        Scans a dataset for Items, storing any found in a Named List

        Parameters:
            list: str
                The Named List in which to store any Items found
            nDataset: int
                The serial number of the dataset to be scanned. The number can
                be obtained from the Dataset property of an overlay, or from
                the GetDataset, GetDatasetContainer or FindExternalDataset
                methods
            filter: str
                Optionally specifies a named Filter which Items must pass to
                be included in the scan
            locus: str
                Optionally specifies a named Locus which Items must pass to be
                included in the scan
        """
        pass

    def ScanGeometry(self, list: str, geomTest: int, geomMode: int, filter: str, locus: str) -> int:  # noqa: E501
        """
        Finds Items which satisfy a condition with the current open Item

        Parameters:
            list: str
                The Named List in which to store any items found
            geomTest: int
                The geometry test to use. See Geometry Tests for details
            geomMode: int
                The geometry mode to use. See Geometry Tests for details
            filter: str
                Optionally specifies a named Filter which items must pass to
                be included in the scan
            locus: str
                Optionally specifies a named Locus which items must pass to be
                included in the scan
        """
        pass

    def ScanList(self, listOut: str, listIn: str, filter: str, locus: str) -> int:  # noqa: E501
        """
        Scans a Named List for Items matching a named Filter and/or named
        Locus

        Parameters:
            listOut: str
                The Named List in which to store any Items found
            listIn: str
                The Named List to be scanned
            filter: str
                Optionally specifies a named Filter which Items must pass to
                be included in the scan
            locus: str
                Optionally specifies a named Locus which Items must pass to be
                included in the scan
        """
        pass

    def ScanOverlay(self, list: str, pos: int, filter: str, locus: str) -> int:
        """
        Scans an overlay for Items, storing any found in a Named List

        Parameters:
            list: str
                The Named List in which to store any Items found
            pos: int
                The position in the overlays list of the overlay to be
                scanned
            filter: str
                Optionally specifies a named Filter which Items must pass to
                be included in the scan. The Filter specified, if any, will be
                used in addition to any overlay drawing Filter
            locus: str
                Optionally specifies a named Locus which Items must pass to be
                included in the scan. The Locus specified, if any, will be
                used in addition to any overlay drawing Locus
        """
        pass

    def ScanPointContainers(self, list: str, x: float, y: float, z: float, filter: str, locus: str) -> int:  # noqa: E501
        """
        Finds Items which intersect a point.This will find for example, Point
        items which are co-incident with the given point, LineString items
        which cross the given point, and Polygon items which contain the given
        point

        Parameters:
            list: str
                The Named List in which to store any Items found
            x: float
                The x coordinate position at which to scan
            y: float
                The y coordinate position at which to scan
            z: float
                The z coordinate position at which to scan
            filter: str
                Optionally specifies a named Filter which Items must pass to
                be included in the scan
            locus: str
                Optionally specifies a named Locus which Items must pass to be
                included in the scan
        """
        pass

    def Snap2D(self, x: float, y: float, r: float, bEditOnly: int, codes: str, filter: str, locus: str) -> int:  # noqa: E501
        """
        Simulates a 2D snap, making snapped item current, and returning the
        snapped position

        Parameters:
            x: float
                The x coordinate of the position from which to snap. Item
                geometries with any Z values will be considered
            y: float
                The y coordinate of the position from which to snap. Item
                geometries with any Z values will be considered
            r: float
                The approximate radius to search within
            bEditOnly: int
                Should SIS only consider editable items?
            codes: str
                The types of geometry you wish to snap to. You can supply a
                single letter, or a list of letters. SIS will find the closest
                matching geometry. Some snap-codes take priority over others.
                For example, if you specify "LV" and a vertex is only slightly
                further away than a line, then SIS will snap to the vertex
            filter: str
                Optionally specifies a named Filter which Items must pass to
                be considered for snapping
            locus: str
                Optionally specifies a named Locus which Items must pass to be
                considered for snapping
        """
        pass

    def SplitCombinedFilter(self, filter: str, filter1: str, filter2: str) -> int:  # noqa: E501
        """
        Recreate the two filters that were combined to make the named combined
        filter

        Parameters:
            filter: str
                The named combined filter to interrogate
            filter1: str
                A named filter to create or replace; this will contain the
                contents of one of the two filters combined to create the
                combined filter being interrogated
            filter2: str
                A named filter to create or replace; this will contain the
                contents of the other of the two filters combined to create
                the combined filter being interrogated
        """
        pass

    def StrFromMetre(self, metre: float, ndim: int, showunits: int) -> int:
        """
        Formats a metre dimension as a string, in a chosen format

        Parameters:
            metre: float
                The metre dimension to be formatted
            ndim: int

            showunits: int

        """
        pass

    def TopoEdgeFill(self, seed: str, bForwards: int, filter: str) -> int:
        """
        Creates a Named Seed object by following the current open Link item to
        make a closed loop

        Parameters:
            seed: str
                The new Named Seed object, which will be a TopoPolygon item
            bForwards: int

            filter: str
                Optionally specifies a named Filter which all Link Items must
                pass to be considered as part of the TopoPolygon
        """
        pass

    def TopoFindRoute(self, seed: str, idNode1: int, idNode2: int, nDataset: int, formula: str, filter: str, locusNoGo: str) -> int:  # noqa: E501
        """
        Creates a Named Seed object by route-finding between two Node Items
        within a dataset

        Parameters:
            seed: str
                The name of the new Named Seed object
            idNode1: int
                The start Node of the route
            idNode2: int
                The end Node of the route
            nDataset: int
                The serial number of the topological dataset. The serial
                number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, FindExternalDataset or
                TopoGetNamedSeedDataset methods
            formula: str

            filter: str
                Optionally specifies a named Filter which all Link Items must
                pass to be considered as part of the route
            locusNoGo: str
                Optionally specifies a named Locus through which the route
                cannot pass
        """
        pass

    def TopoFloodFill(self, seed: str, x: float, y: float, z: float, nDataset: int, filter: str) -> int:  # noqa: E501
        """
        Creates a Named Seed object by flood-filling Link Items within a
        dataset

        Parameters:
            seed: str
                The name of the new Named Seed object
            x: float
                The x coordinate of the position from which to flood-fill
            y: float
                The y coordinate of the position from which to flood-fill
            z: float
                The z coordinate of the position from which to flood-fill
            nDataset: int
                The serial number of the topological dataset. The serial
                number can be obtained from the Dataset property of an
                overlay, or from the GetDataset, FindExternalDataset or
                TopoGetNamedSeedDataset methods
            filter: str
                Optionally specifies a named Filter which all Link Items must
                pass to be considered as part of the flood-fill
        """
        pass

    def TopoGetLinkNode(self, bStart: int) -> int:
        """
        Gets the ID of a Node item from the current open Link item

        Parameters:
            bStart: int

        """
        pass

    def TopoGetLinkNumSeed(self) -> int:
        """
        Gets the number of TopoPolygon and TopoLineString Items attached to
        the current open Link item
        """
        pass

    def TopoGetLinkSeed(self, n: int) -> int:
        """
        Gets the signed ID of a TopoPolygon or TopoLineString item from the
        current open Link item

        Parameters:
            n: int
                The index of the TopoPolygon or TopoLineString item in the
                list of TopoPolygon and TopoLineString Items attached to the
                current Link item, starting at 0. Use TopoGetLinkNumSeed to
                find out the number of TopoPolygon and TopoLineString Items
                attached to a Link item
        """
        pass

    def TopoGetNamedSeedDataset(self, seed: str) -> int:
        """
        Gets the dataset with which a Named Seed object is compatible

        Parameters:
            seed: str
                The Named Seed object whose dataset is required
        """
        pass

    def TopoGetNamedSeedLoopLink(self, seed: str, nLoop: int, n: int) -> int:
        """
        Gets the ID of a Link item from a Named Seed object

        Parameters:
            seed: str
                The Named Seed object to be queried
            nLoop: int
                The index in the list of loops in the Named Seed object of the
                loop to be queried, starting at 0. Use TopoGetNamedSeedNumLoop
                to find out the number of loops in a Named Seed object
            n: int
                The index in the loop of the Link item to be queried, starting
                at 0. Use TopoGetNamedSeedLoopSize to find out the number of
                Link Items referred to by a loop in a Named Seed object
        """
        pass

    def TopoGetNamedSeedLoopSize(self, seed: str, nLoop: int) -> int:
        """
        Gets the number of Link Items referred to by a loop in a Named Seed
        object

        Parameters:
            seed: str
                The Named Seed object to be queried
            nLoop: int
                The index in the list of loops in the Named Seed object of the
                loop to be queried, starting at 0. Use TopoGetNamedSeedNumLoop
                to find out the number of loops in a Named Seed object
        """
        pass

    def TopoGetNamedSeedNumLoop(self, seed: str) -> int:
        """
        Gets the number of loops in a Named Seed object

        Parameters:
            seed: str
                The Named Seed object to be queried
        """
        pass

    def TopoGetNodeLink(self, n: int) -> int:
        """
        Gets the signed ID of a Link item from the current open Node item

        Parameters:
            n: int
                The index in the list of Link Items attached to the current
                Node item of the Link item to be queried, starting at 0
        """
        pass

    def TopoGetNodeNumLink(self) -> int:
        """
        Gets the number of Link Items attached to the current open Node item
        """
        pass

    def TopoIsChain(self, seed: str) -> int:
        """
        Tests if a Named Seed object is a topological TopoLineString

        Parameters:
            seed: str
                The Named Seed object to test
        """
        pass

    def TopoIsPolygon(self, seed: str) -> int:
        """
        Tests if a Named Seed object is a topological TopoPolygon

        Parameters:
            seed: str
                The Named Seed object to test
        """
        pass

    def TopoShrinkNamedSeed(self, seed: str, bStart: int) -> int:
        """
        Removes a Link item from a Named Seed object

        Parameters:
            seed: str
                The Named Seed object from which to remove the Link item
            bStart: int

        """
        pass

    def GetBlobB(self, crs: str, fmt: int, precision: int) -> int:
        """
        Gets a Blob (as an array of bytes) of the current open Item, within a
        CRS

        Parameters:
            crs: str
                The named CRS of the returned Blob data
            fmt: int
                The format of the stored item Blob
            precision: int
                This parameter is ignored and will always return 64-bit
                precision
        """
        pass

    def GetNumSwd(self) -> int:
        """
        Get number of different SIS Workspace Definition (SWD) files open
        """
        pass

    def GetNumWnd(self) -> int:
        """
        """
        pass

    def CanDoCommand(self, comname: str) -> int:
        """
        Checks whether or not a command can be executed. The result depends on
        the type of the current window, and the selection within the current
        Swd. In the SIS Control, the current licence level is also checked

        Parameters:
            comname: str
                The command to check
        """
        pass

    def Get3DEye(self) -> int:
        """
        Gets the position of the Eye in a 3D Window
        """
        pass

    def Get3DLook(self) -> int:
        """
        Gets the position looked towards in a 3D Window
        """
        pass

    def GetDisplayExtent(self) -> int:
        """
        Gets the padded visible extents of the current window
        """
        pass

    def GetDrawExtent(self) -> int:
        """
        Returns the "draw" extents of the current open item, eg including the
        extents of a symbol on a point item
        """
        pass

    def GetNumSel(self) -> int:
        """
        Gets the number of items selected in the current Swd
        """
        pass

    def GetNumSelEx(self) -> int:
        """
        Gets the number of items selected in the current Swd
        """
        pass

    def ShowUI(self, ui: str, parameters: str) -> int:
        """
        Shows UI, eg a dialog or Wizard, for a specific task

        Parameters:
            ui: str

            parameters: str

        """
        pass
