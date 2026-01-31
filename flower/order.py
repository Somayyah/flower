import yaml
from pathlib import Path
from dataclasses import dataclass
import logging

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
        self.logger = logging.getLogger(__name__)
        self.order_file = self.load_yaml(order_file)
        self.frames: list[Frame] = []
        self.timeline = self.draft_timeline()
        self.load_frames()

    def load_yaml(self, order_file: Path) -> dict:
        """Load the YAML file and return its contents as a dictionary."""
        try:
            with order_file.open("r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            self.logger.error(f"Order file not found: {order_file}")
            raise

    def load_frames(self) -> None:
        """Parse order.yaml and populate self.frames."""
        for frame_entry in self.order_file.get('frames', []):
            frame = Frame(
                id=frame_entry.get('id'),
                video=frame_entry.get('video'),
                audio=frame_entry.get('audio'),
                subtitles=frame_entry.get('subtitles'),
                image=frame_entry.get('image')
            )
            self.logger.debug(f"Created frame: {frame}")
            self.frames.append(frame)
        self.logger.info(f"Loaded {len(self.frames)} frames from order file.")
    
    def draft_timeline(self):
        """Draft a timeline based on the loaded frames."""
        timeline = []
        for frame in self.frames:
            timeline.append({
                'video': frame.video,
                'audio': frame.audio,
                'subtitles': frame.subtitles,
                'image': frame.image
            })
        return timeline