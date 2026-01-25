# Flower

My personal video editing flow with ffmpeg / python

Since my videos don't require that much editing to begin with, and since my objectives are simple I decided to automate it with ffmpeg. It should look into the media directory in the CWD, and uses the assets to generate videos. The media directory structure is like this:

```bash
.
├── media
│   ├── audio
│   │   └── 1.wav
│   ├── srts
│   │   └── 1.srt
│   └── video
│       ├── 1.mp4
│       └── 2
│           └── 2a.mp4
│           └── 2b.mp4
└── output.mp4 >> Final audio
```

and I want to concatinate all the media files in an order, if that makes sense. I'll figure it as I go.

## Assets order

Frame order is stored in order.yaml, for example:

```yaml
- id: 1
  video: 1.mp4
  audio: 1.wav
  subtitles: 1.srt
  image: null

- id: 2
  video: null
  audio: 2.wav
  subtitles: null
  image: 2.png
```

Frames have sequencial IDs, you can ommit adding assets if they don't exist and you can explicitly ommit them as below:

```yaml
- id: 1
  video: 1.mp4
  audio: 1.wav
  subtitles: 1.srt

- id: 2
  video: null
  audio: 2.wav
  subtitles: null
```

If Assets are ommitted it will be assumed based on the ID number, so below:

```yaml
- id: 1

- id: 2
```

Is same as:

```yaml
- id: 1
  video: 1.mp4
  audio: 1.wav
  subtitles: 1.srt
  image: 1.png

- id: 2
  video: null
  audio: 2.wav
  subtitles: 1.srt
  image: 2.png
```

## How to use

`flower` is a simple CLI to stitch together your videos, audio, images, and subtitles in the order you define in a YAML file.

### Basic Format

```bash
flower [OPTIONS]
```

**Example**

```bash
flower -i my_project -o order.yaml -w final_video.mp4
```

### Options

* `-i <PROJECT>` → **Initialize a new project folder**
  Creates a project structure like this inside `<PROJECT>`:

  ```
  ./my_project/
  ├── media/
  │   ├── audio/     # put audio files here
  │   ├── images/    # put image files here
  │   ├── srts/      # put subtitles here
  │   └── video/     # put video files here
  └── order.yaml     # YAML file defining your sequence
  ```

* `-o <ORDER_FILE>` → **Specify which order.yaml to use**

  * When used with `-i`, this becomes the name of the new order file.
  * Otherwise, it points to an existing order file for stitching.

* `-w <OUTPUT>` → **Specify the output video filename**
  Defaults to `output.mp4` if not provided.

---

### Minimal example

```bash
# Create a new project
flower -i my_project -o order.yaml

# Generate a video from an existing project and YAML
flower -o my_project/order.yaml -w final.mp4
```