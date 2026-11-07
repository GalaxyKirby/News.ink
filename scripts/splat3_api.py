# File contains all code responsible for handling and returning API requests
from enum import Enum
import time
import requests
import json

# Enums
class Mode(Enum):
    TURF_WAR = 1
    SPLAT_ZONES = 2
    TOWER_CONTROL = 3
    RAINMAKER = 4
    CLAM_BLITZ = 5

class MatchType(Enum):
    REGULAR = 1
    OPEN = 2
    SERIES = 3
    X_BATTLE = 4

    SPLATFEST = 5
    TRI_COLOR = 6

# Classes
class Map():
    def __init__(self, name: str, image_url: str):
        self.image_url = image_url
        self.name = name

class Rotation():
    def __init__(self):
        self.name: str
        self.mode: str
        self.map1: Map
        self.map2: Map

        self.start_time: str
        self.end_time: str

# Functions
def fetch_schedule_data():
    res = requests.get('https://splatoon3.ink/data/schedules.json')
    
    try:
        if res.text != "":
            return json.loads(res.text)
        else:
            return None
    except:
        return None


def parse_scedule_data(data: json, index: int, type: MatchType):
    if data == None:
        raise ValueError("JSON recieved from schedule endpoint was NULL.")

    return_roto: Rotation = Rotation()

    is_splatfest: bool = False
    
    try:
        if not is_splatfest:
            if type == MatchType.SPLATFEST or type == MatchType.TRI_COLOR:
                raise ValueError("Searching for Splatfest battles, but there isn't a Splatfest happening!")

            # Setup
            rotationNode = None
            setting_node_name = None
            rotation_name = ""

            match type:
                case MatchType.REGULAR:
                    rotationNode = data["data"]["regularSchedules"]["nodes"][index]
                    setting_node_name = "regularMatchSetting"
                    
                    rotation_name = "Regular Battle"

                case MatchType.OPEN | MatchType.SERIES:
                    rotationNode = data["data"]["bankaraSchedules"]["nodes"][index]
                    setting_node_name = "bankaraMatchSettings"

                    if type == MatchType.OPEN:
                        rotation_name = "Anarchy Open"
                    else:
                        rotation_name = "Anarchy Series"

                case MatchType.X_BATTLE:
                    rotationNode = data["data"]["xSchedules"]["nodes"][index]
                    setting_node_name = "xMatchSetting"

                    rotation_name = "X Battle"

            if rotationNode == None or setting_node_name == None:
                raise ValueError("Failed to get the rotation node from JSON.")
            
            # Return Data
            return_roto.start_time = rotationNode["startTime"] #TODO: Convert the times to a readable format based on region
            return_roto.end_time = rotationNode["endTime"]

            return_roto.name = rotation_name

            if type == MatchType.OPEN or type == MatchType.SERIES:
                index = 0

                if type == MatchType.OPEN:
                    index = 1

                return_roto.mode = rotationNode[setting_node_name][index]["vsRule"]["name"]

                map1 = rotationNode[setting_node_name][index]["vsStages"][0]
                map2 = rotationNode[setting_node_name][index]["vsStages"][1]

                print(map1)
                print(map2)

                return_roto.map1 = Map(map1["name"], map1["image"]["url"])
                return_roto.map2 = Map(map2["name"], map2["image"]["url"])

            else:
                return_roto.mode = rotationNode[setting_node_name]["vsRule"]["name"]

                map1 = rotationNode[setting_node_name]["vsStages"][0]
                map2 = rotationNode[setting_node_name]["vsStages"][1]

                print(map1)
                print(map2)

                return_roto.map1 = Map(map1["name"], map1["image"]["url"])
                return_roto.map2 = Map(map2["name"], map2["image"]["url"])
        
        else:
            pass #TODO: Add splatfest support

        return return_roto
    
    except Exception as e:
        raise ValueError("An error occured while parsing schedule data! | " + str(e))