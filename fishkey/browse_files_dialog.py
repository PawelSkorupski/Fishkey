from PyQt5 import QtWidgets
import os


def browseFiles(window) -> str:
    """
    Method showing File Input Dialog with only .csv files
    and directories. If correct file is selected, method
    returns file path.
    """
    fileLocation, ok = QtWidgets.QFileDialog.getOpenFileName(
        parent=window,
        caption="Wybierz plik z fiszkami",
        directory=os.getcwd(),
        filter="Plik z fiszkami (*.csv)",
    )
    if ok != "":
        return fileLocation
    return None
