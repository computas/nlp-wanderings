import azure.cognitiveservices.speech as speechsdk
import time

import sys
def speech_recognize_continuous_from_file():
    print(speechsdk.version)
    """performs continuous speech recognition with input from an audio file"""
    speech_key, service_region = sys.argv[1], "northeurope"
    
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.set_service_property(name='wordLevelConfidence', value='true', channel=speechsdk.ServicePropertyChannel.UriQueryParameter)
    speech_config.set_service_property(name='format', value='detailed', channel=speechsdk.ServicePropertyChannel.UriQueryParameter)
    #speech_config.endpoint_id = "b71c4815-62c8-4175-8f8e-856d30785395"
    
    audio_config = speechsdk.audio.AudioConfig(filename="politikk.wav")
 
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="nb-NO",audio_config=audio_config)
    #speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_config)

    done = False
 
    def stop_cb(evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
 
    all_results = []
    def handle_final_result(evt):
        #print(evt.result.properties)
        print(evt.result.text)
        all_results.append(evt.result.text)
    speech_recognizer.recognized.connect(handle_final_result)
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)
    print(all_results)
    myfile=open("rawtext.txt",'w')
    for t in all_results:
        myfile.write(t)

speech_recognize_continuous_from_file()
