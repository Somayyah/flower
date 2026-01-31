import yaml
from pathlib import Path
from dataclasses import dataclass, field
import logging

@dataclass
class Frame:
    video: str = None
    audio: str = None
    subtitles: str = None
    image: str = None

@dataclass
class timelineEntry:
    clip: list = None
    transition: str = None

@dataclass
class Clip:
    name: str
    frames: list[int]
    
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
        self.logger = logging.getLogger(__name__)
        self.order_file = self.load_yaml(order_file)
        self.frames: list[Frame] = self.load_frames()
        self.timeline = self.draft_timeline()

    def load_yaml(self, order_file: Path) -> dict:
        """Load the YAML file and return its contents as a dictionary."""
        try:
            with order_file.open("r") as f:
                order = yaml.safe_load(f)
                self.logger.debug(f"Loaded order file: {order_file}")
                self.logger.debug(f"Order contents: {order}")
                return order
        except FileNotFoundError:
            self.logger.error(f"Order file not found: {order_file}")
            raise

    def load_frames(self) -> None:
        """Parse order.yaml and populate self.frames."""
        frames = []
        for frame_entry in self.order_file['frames'].items():
            self.logger.debug(f"Parsing frame entry: {frame_entry}")
            frame = Frame(
                video=frame_entry.get('video'),
                audio=frame_entry.get('audio'),
                subtitles=frame_entry.get('subtitles'),
                image=frame_entry.get('image')
            )
            frames[int(frame_entry[0])] = frame
            self.logger.debug(f"Created frame: {frame}")
        self.logger.info(f"Loaded {len(frames)} frames from order file.")
        return frames
    
    def draft_timeline(self):
        """Draft a timeline based on the loaded frames."""
        if 'timeline' not in self.order_file:
            return []
        timeline = []
        for entry in self.order_file['timeline']:
            timeline.append(entry)
        self.logger.info(f"Drafted timeline with {len(timeline)} entries.")
        self.logger.debug(f"Timeline contents: {timeline}")
        return timeline