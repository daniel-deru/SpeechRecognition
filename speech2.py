# install pyaudio, speechrecognition and pocketsphinx
# if anthing doesn't want to install, install pipwin and install the modules using pipwin

from pocketsphinx import LiveSpeech
# for phrase in LiveSpeech():
#     print(phrase)
#     if "t" in phrase:
#         break

speech = LiveSpeech(lm=False, keyphrase='a', kws_threshold=1e-20)
for phrase in speech:
    print(phrase.segments(detailed=True))