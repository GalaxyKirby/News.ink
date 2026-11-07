import splat3_api

from PySide6 import QtCore, QtWidgets, QtGui
import json

# Main Display
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        pass

#Testing out methods for now
data = splat3_api.fetch_schedule_data()

turf_war_roto = splat3_api.parse_scedule_data(data, 0, splat3_api.MatchType.REGULAR)

print(turf_war_roto.start_time + " " + turf_war_roto.map1.name)