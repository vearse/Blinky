
import re
from googletrans import Translator
import pyttsx3
from moviepy.editor import *
from pydub import AudioSegment

def trimmiffy(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'http\S+','\n\n',  text)
    return text

def translate_text(thread, lang):
    print('Translating Text')
    text = '\n\n \n\n'.join(thread)  
    text = trimmiffy(text) 

    if(lang):
        translator = Translator()
        translated_text = translator.translate(text, dest=lang)
        text = translated_text.text
        # print(translated_text)

    return text
        
def generateAudio(id, text, speaker, lang):
    engine = pyttsx3.init()
    # engine = pyttsx3.init("espeak")
    voices = engine.getProperty('voices')      
    engine.setProperty("rate", 165)
    print(speaker, lang)

    if(lang == 'en'):
        for voice in voices :
            if(voice.languages[0][:2]  == 'en') :
                selectEnglishSpeaker(engine,speaker, voice)
    else:
        for voice in voices:
            if(voice.languages[0][:2]  == lang) :
                return engine.setProperty('voice', voice.id)
       

    audio_file= './app/assets/audio/'+ str(id) + '.wav'
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return audio_file
    
def selectEnglishSpeaker(engine, speaker, voice):
    if(str(speaker).lower() == 'zara' and voice.name == 'Karen') :
        return engine.setProperty('voice', voice.id)
    if(str(speaker).lower() == 'daniel' and voice.name == 'Daniel') :
        return engine.setProperty('voice', voice.id )
    
    if(str(speaker).lower() == 'mia' and voice.name == 'Moira') :
        return engine.setProperty('voice', voice.id)
    if(str(speaker).lower() == 'alex' and voice.name == 'Alex') :
        return engine.setProperty('voice', voice.id )

    if(str(speaker).lower() == 'tessa' and voice.name == 'Tessa') :
        return engine.setProperty('voice', voice.id)
    if(str(speaker).lower() == 'sophia' and voice.name == 'Samantha') :
        return engine.setProperty('voice', voice.id )

def giftSpeaking(id, text, language):
    # # tts = gTTS(text=text,  lang=language, slow=False) 
    # audio_file= './app/assets/audio/'+ str(id) + '.mp3'
    # tts.save(audio_file)
    # return audio_file
    return
 
def generateNewAudiogram(id):
    video_file= VideoFileClip('./app/assets/media/'+str(id)+'.mp4').resize(height=100)
    image_file=  VideoFileClip('./app/assets/media/'+str(id)+'.gif')
    audio_file= AudioFileClip('./app/assets/audio/'+str(id)+'.wav')
    videograph = './app/assets/play/'+str(id)+'.mp4'

    concat_clip = CompositeVideoClip([image_file, video_file.set_position(("center","bottom")) ])
    # .set_position((0.0,0.85), relative=True) ]).margin(top=1)
    # concat_clip = concatenate_videoclips([image_file, video_file], method="compose")
    concat_clip = concat_clip.set_audio(audio_file) 
    concat_clip.write_videofile(videograph, fps=24,codec='libx264', audio_codec='aac',  temp_audiofile='temp-audio.m4a', remove_temp=True)
    return videograph