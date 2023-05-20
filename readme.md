## Description

OVOS TTS plugin for [bark](https://github.com/suno-ai/bark)

This is very slow and needs a GPU to be remotely usable

## Install

`pip install ovos-tts-plugin-bark`

## Configuration

see voices in [bark speaker library V2](https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c)

```json
  "tts": {
    "module": "ovos-tts-plugin-bark",
    "ovos-tts-plugin-bark": {
      "use_cuda": true,
      "small_models": true,
      "voice": "v2/en_speaker_6"
    }
  }
```