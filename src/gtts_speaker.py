#!/usr/bin/python2

# import the necessary packages
import rospy
import os
from gtts import gTTS
import pygame

from custom_msgs.msg import String_Int

class speaker_class():
    """ Class speaker_class.

    Is the class that gets the text that must be said.
    """

    def __init__(self):
        """Class constructor

        It is the constructor of the class. It does:
        - Subscribe itself to the topics
        """

        #Subscribe to ROS topics
        self.tts_sub = rospy.Subscriber("tts_text", String_Int, self.cb_tts)

        self.texto_tts = ' '

        print("[INFO] Ready to speak")

        self.define_parameters()

    def define_parameters(self):
        """Function to define Parameters

        In this functions the next parameters of the voice are set:
        - Choose language
        - Choose voice
        - Set pitch (default 50)
        - Set speed (default 175) --> Try 260
        - Emphasize capitals
        """
        self.language = 'es-us'

    def speaking(self):
        voice = gTTS(self.texto_tts,lang=self.language)
        voice.save("reproducir.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("reproducir.mp3")
        pygame.mixer.music.play()

    def run_loop(self):
        """ Infinite loop.

        It does nothing but wait until msgs are received.
        """
        while not rospy.is_shutdown():
            rospy.spin()

    def stoping_node(self):
        """ROS closing node

        Is the function called when ROS node is closed.
        This function closes all windows opened by opencv"""
        print("\n\nBye bye! :)\n\n")

    def cb_tts(self, data):
        print("Tipo: ")
        print (data.data_int)
        print("Text: ")
        print(data.data_string)
        self.texto_tts = data.data_string
        self.speaking()

if __name__=='__main__':
    """ Main void.

    Is the main void executed when started. It does:
    - Start the node
    - Create an object of the class
    - Run the node

    """
    try:
        rospy.init_node('speaker_node')       # Init ROS node

        speaker_tts = speaker_class()
        rospy.on_shutdown(speaker_tts.stoping_node)

        speaker_tts.run_loop()

    except rospy.ROSInterruptException:
        pass
