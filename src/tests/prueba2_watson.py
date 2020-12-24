from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('BjHfv8ct-Rypjy23mYp8q1pF74kHBEEwa0JBkP4tR2ne')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/d383fac8-02d5-4896-b8d0-373e50273e1c')

with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Ikki bebe',
            voice='es-ES_LauraVoice',
            accept='audio/wav'
        ).get_result().content)
