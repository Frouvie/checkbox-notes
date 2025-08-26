import json
from pathlib import Path
from typing import Dict
from dataclasses import dataclass, field

@dataclass
class TaskModel():
    name: str = ""
    status: bool = False


@dataclass
class ListModel():
    name: str = ""
    tasks: Dict[int, TaskModel] = field(default_factory=dict)


@dataclass
class DataScheme():
    lists: Dict[int, ListModel] = field(default_factory=dict)


class DataModel():
    __file = Path("data.json")
    
    def __init__(self):
        self.__data = DataScheme()