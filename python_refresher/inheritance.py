"""practice class inheritance"""


class Device:
    """Device class"""
    def __init__(self, name: str, connected_by: str):
        """Construct class device"""
        self.name = name
        self.connected_by = connected_by
        self.connected: bool = True

    def __str__(self) -> str:
        """ return device name and how it is connected """
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        """ disconnect device """
        self.connected = False
        print("Disconnected.")


class Printer(Device):
    """Printer class child class of device"""
    def __init__(self, name: str, connected_by: str, capacity: int):
        """ constructor """
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages: int = capacity

    def __str__(self) -> str:
        """ str """
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages: int):
        """use the printer to print if enough page is available"""
        if not self.connected:
            print("Your printer is not connected")
        elif self.remaining_pages >= pages:
            print(f"Printing {pages} pages")
            self.remaining_pages -= pages
        else:
            print("Not enough pages to print")


home_printer = Printer("brother", "wifi", 3000)
home_printer.disconnect()
home_printer.print(3001)
print(home_printer)
