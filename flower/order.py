import yaml
from pathlib import Path
from collections import OrderedDict
from dataclasses import dataclass

@dataclass
class Frame:
    id : int
    video: str = None
    audio: str = None
    subtitles: str = None
    image: str = None

class Order:
    """
    Represents the sequence of frames to render in a project.

    Responsibilities:
    - Load and parse an order YAML file.
    - Validate frame data (basic checks for required keys).
    - Provide access to the sequence of frames.
    
    Attributes:
        order_file (Path): Path to the order YAML file.
        media (Path): Base path of the project directory.
        frames (list[dict]): List of frame dictionaries, each containing:
            - id: int, frame ID
            - video: Optional[str], video filename
            - audio: Optional[str], audio filename
            - subtitles: Optional[str], subtitles filename
            - image: Optional[str], image filename

    Methods:
        load_order(): Reads the YAML file and populates the frames list.
        iter_frames(): Yields each frame dictionary in order.
        __len__(): Returns the number of frames.
    """
    
    def __init__(self, order_file: Path, media: Path ) -> None:
        self.order_file : Path = order_file
        self.media : Path = media
        self.frames : list[Frame] = []
        self.generate_frames()
        
    def generate_frames(self):
        pass