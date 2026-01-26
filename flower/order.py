import yaml
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class Frame:
    id : int
    video: str = None
    audio: str = None
    subtitles: str = None
    image: str = None

class Order:
    """
    Represents the frame order defined in order.yaml.

    Responsibilities:
    - Load and parse the order YAML file.
    - Convert frame entries into Frame objects.
    - Preserve declared order.

    Attributes:
        order_file (Path): Path to the order YAML file.
        frames (list[Frame]): Ordered list of Frame objects.
    """

    def __init__(self, order_file: Path) -> None:
        self.order_file = order_file
        self.frames: list[Frame] = []
        self.load_frames()

    def load_frames(self) -> None:
        """Parse order.yaml and populate self.frames."""
        pass
