# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

from ovos_plugin_manager.templates.tts import TTS
from scipy.io.wavfile import write as write_wav


class BarkTTSPlugin(TTS):
    """Interface to Bark TTS."""
    lang2voices = {
        'ca': ['upc_ona-x-low', 'upc_pau-x-low'],
        'da': ['nst_talesyntese-medium'],
        'de': ['eva_k-x-low',
               'karlsson-low',
               'kerstin-low',
               'pavoque-low',
               'ramona-low',
               'thorsten-low'],
        'el-gr': ['rapunzelina-low'],
        'en-gb': ['alan-low', 'southern_english_female-low'],
        'en-us': ['amy-low',
                  'danny-low',
                  'kathleen-low',
                  'lessac-low',
                  'lessac-medium',
                  'libritts-high',
                  'ryan-high',
                  'ryan-low',
                  'ryan-medium',
                  'lessac'],
        'es': ['carlfm-x-low', 'mls_10246-low', 'mls_9972-low'],
        'fi': ['harri-low'],
        'fr': ['gilles-low', 'mls_1840-low', 'siwis-low', 'siwis-medium'],
        'it': ['riccardo_fasol-x-low'],
        'kk': ['iseke-x-low', 'issai-high', 'raya-x-low'],
        'ne': ['google-medium', 'google-x-low'],
        'nl': ['mls_5809-low',
               'mls_7432-low',
               'nathalie-x-low',
               'rdh-medium',
               'rdh-x-low'],
        'no': ['talesyntese-medium'],
        'pl': ['mls_6892-low'],
        'pt-br': ['edresson-low'],
        'uk': ['lada-x-low'],
        'vi': ['25hours-single-low', 'vos-x-low'],
        'zh-cn': ['huayan-x-low']}
    voice2url = {
        '25hours-single-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-vi-25hours-single-low.tar.gz',
        'alan-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-gb-alan-low.tar.gz',
        'amy-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-amy-low.tar.gz',
        'carlfm-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-es-carlfm-x-low.tar.gz',
        'danny-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-danny-low.tar.gz',
        'edresson-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-pt-br-edresson-low.tar.gz',
        'eva_k-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-de-eva_k-x-low.tar.gz',
        'gilles-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-fr-gilles-low.tar.gz',
        'google-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-ne-google-medium.tar.gz',
        'google-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-ne-google-x-low.tar.gz',
        'harri-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-fi-harri-low.tar.gz',
        'huayan-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-zh-cn-huayan-x-low.tar.gz',
        'iseke-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-kk-iseke-x-low.tar.gz',
        'issai-high': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-kk-issai-high.tar.gz',
        'karlsson-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-de-karlsson-low.tar.gz',
        'kathleen-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-kathleen-low.tar.gz',
        'kerstin-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-de-kerstin-low.tar.gz',
        'lada-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-uk-lada-x-low.tar.gz',
        'lessac': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us_lessac.tar.gz',
        'lessac-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-lessac-low.tar.gz',
        'lessac-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-lessac-medium.tar.gz',
        'libritts-high': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-libritts-high.tar.gz',
        'mls_10246-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-es-mls_10246-low.tar.gz',
        'mls_1840-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-fr-mls_1840-low.tar.gz',
        'mls_5809-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-nl-mls_5809-low.tar.gz',
        'mls_6892-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-pl-mls_6892-low.tar.gz',
        'mls_7432-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-nl-mls_7432-low.tar.gz',
        'mls_9972-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-es-mls_9972-low.tar.gz',
        'nathalie-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-nl-nathalie-x-low.tar.gz',
        'nst_talesyntese-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-da-nst_talesyntese-medium.tar.gz',
        'pavoque-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-de-pavoque-low.tar.gz',
        'ramona-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-de-ramona-low.tar.gz',
        'rapunzelina-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-el-gr-rapunzelina-low.tar.gz',
        'raya-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-kk-raya-x-low.tar.gz',
        'rdh-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-nl-rdh-medium.tar.gz',
        'rdh-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-nl-rdh-x-low.tar.gz',
        'riccardo_fasol-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-it-riccardo_fasol-x-low.tar.gz',
        'ryan-high': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-ryan-high.tar.gz',
        'ryan-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-ryan-low.tar.gz',
        'ryan-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-us-ryan-medium.tar.gz',
        'siwis-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-fr-siwis-low.tar.gz',
        'siwis-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-fr-siwis-medium.tar.gz',
        'southern_english_female-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-en-gb-southern_english_female-low.tar.gz',
        'talesyntese-medium': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-no-talesyntese-medium.tar.gz',
        'thorsten-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-de-thorsten-low.tar.gz',
        'upc_ona-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-ca-upc_ona-x-low.tar.gz',
        'upc_pau-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-ca-upc_pau-x-low.tar.gz',
        'vos-x-low': 'https://github.com/rhasspy/bark/releases/download/v0.0.2/voice-vi-vivos-x-low.tar.gz'
    }

    def __init__(self, lang="en-us", config=None):
        super(BarkTTSPlugin, self).__init__(lang, config)
        # needs to be done before import of bark
        if not self.config.get("use_cuda", False):
            os.environ["CUDA_VISIBLE_DEVICES"] = ""
        if self.config.get("small_models", True):
            os.environ["SUNO_USE_SMALL_MODELS"] = "1"

        from bark import SAMPLE_RATE
        from bark.generation import (
            generate_text_semantic,
            preload_models,
        )
        from bark.api import semantic_to_waveform

        # download and load all models
        preload_models()

        self.sample_rate = SAMPLE_RATE
        self.temperature = self.config.get("temperature", 0.6)
        self.min_eos_p = self.config.get("min_eos_p", 0.05)  # this controls how likely the generation is to end
        self.voice = self.config.get("voice", "v2/en_speaker_6")

        def generate_semantic_audio(sentence, speaker=self.voice,
                                    temperature=self.temperature, min_eos_p=self.min_eos_p,
                                    lang=self.lang):
            semantic_tokens = generate_text_semantic(
                sentence,
                history_prompt=speaker,
                temp=temperature,
                min_eos_p=min_eos_p,  # this controls how likely the generation is to end
            )

            audio_array = semantic_to_waveform(semantic_tokens, history_prompt=speaker, )
            return audio_array

        self.bark = generate_semantic_audio

    def get_tts(self, sentence, wav_file, lang=None, speaker=None):
        """Generate WAV and phonemes.

        Arguments:
            sentence (str): sentence to generate audio for
            wav_file (str): output file
            lang (str): optional lang override
            speaker (int): optional speaker override

        Returns:
            tuple ((str) file location, (str) generated phonemes)
        """
        lang = lang or self.lang
        audio_array = self.bark(sentence, lang=lang)
        write_wav("bark_generation.wav", self.sample_rate, audio_array)
        return wav_file, None

    def available_languages(self) -> set:
        return {"en", "zh", "fr", "de", "hi", "it", "ja", "ko", "pl", "pt", "ru", "es", "tr"}


_f = ["v2/en_speaker_9",
      "v2/pl_speaker_4", "v2/pl_speaker_6", "v2/pl_speaker_9",
      "v2/ru_speaker_5", "v2/ru_speaker_6", "v2/ru_speaker_9",
      "v2/es_speaker_8", "v2/es_speaker_9",
      "v2/tr_speaker_4", "v2/tr_speaker_5",
      "v2/it_speaker_2", "v2/it_speaker_7", "v2/it_speaker_9",
      "v2/de_speaker_3", "v2/de_speaker_8",
      "v2/ja_speaker_0", "v2/ja_speaker_1", "v2/ja_speaker_3", "v2/ja_speaker_4", "v2/ja_speaker_5",
      "v2/ja_speaker_7", "v2/ja_speaker_8", "v2/ja_speaker_9",
      "v2/fr_speaker_1", "v2/fr_speaker_3", "v2/fr_speaker_5",
      "v2/hi_speaker_1", "v2/hi_speaker_3", "v2/hi_speaker_4", "v2/hi_speaker_9",
      "v2/zh_speaker_4", "v2/zh_speaker_6", "v2/zh_speaker_7", "v2/zh_speaker_9"]

BarkTTSPluginConfig = {
    lang: [{v: {"voice": v,
                "gender": "female" if v in _f else "male",
                "offline": True}}
           for v in {f"v2/{lang}_speaker_{i}" for i in range(10)}]
    for lang in ["en", "zh", "fr", "de", "hi", "it", "ja", "ko", "pl", "pt", "ru", "es", "tr"]
}

if __name__ == "__main__":
    config = {"use_cuda": True,
              "small_models": True}

    print(BarkTTSPluginConfig["en"])
    config["voice"] = "v2/en_speaker_6"  # TODO
    e = BarkTTSPlugin(config=config)
    e.get_tts("hey mycroft", "hello.wav")
