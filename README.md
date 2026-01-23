# video-editing-flow-with-ffmpeg
My personal video editing flow with ffmpeg / python

Since my videos don't require that much editing to begin with, and since my objectives are simple I decided to automate it with ffmpeg. It should look into the media directory in the CWD, and uses the assets to generate videos. The media directory structure is like this:

```bash
.
├── main.py
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