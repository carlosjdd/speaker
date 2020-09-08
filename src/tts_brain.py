#!/usr/bin/python3

# import the necessary packages
import rospy
import rospkg

from custom_msgs.msg import String_Int_Arrays
from custom_msgs.msg import String_Int

import csv

class brain():
    """ Class brain.

    Is the class that gets the information of the people in the image
    """

    def __init__(self):
        """Class constructor

        It is the constructor of the class. It does:
        - Subscribe itself to the topics
        """

        #Subscribe to ROS topics
        self.tts_sub = rospy.Subscriber("tts_info", String_Int_Arrays, self.cb_info)

        #Define the ROS publishers
        self.tts_pub = rospy.Publisher("tts_text", String_Int, queue_size=0)

        #Define object as msg type
        self.tts_msg = String_Int()
        self.tts_msg.data_int = 0
        self.tts_msg.data_string = ' '

        #Set phrases Paths
        rospack = rospkg.RosPack()
        pkg_name = "speaker"			# Name of the ROS package. Is used to take the path of the package
        self.path_greetings = rospack.get_path(pkg_name) + "/data/database1_greetings.csv"
        self.path_wait_detection = rospack.get_path(pkg_name) + "/data/database2_wait_recognition.csv"
        self.path_noone = rospack.get_path(pkg_name) + "/data/database3_noone.csv"
        self.path_only_unknown = rospack.get_path(pkg_name) + "/data/database4_only_unknown.csv"
        self.path_one_known = rospack.get_path(pkg_name) + "/data/database5_one_known.csv"
        self.path_many_known = rospack.get_path(pkg_name) + "/data/database6_many_known.csv"
        self.path_one_unknown = rospack.get_path(pkg_name) + "/data/database7_one_unknown.csv"
        self.path_many_unknown = rospack.get_path(pkg_name) + "/data/database8_many_unknown.csv"

        print("[INFO] Ready to receive info")

        self.open_data()

    def open_data(self):

        self.phrases = [[],[],[],[],[],[],[],[],[]]     #Start the list with 9 arrays, as much as databases needed

        with open(self.path_greetings) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[0].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_wait_detection) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[1].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_noone) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[2].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_only_unknown) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[3].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_one_known) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[4].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_many_known) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[5].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_one_unknown) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[6].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_many_unknown) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[7].append(row[0])					            # Save the path of every SVG file into the array
                self.phrases[8].append(row[1])

        print(self.phrases)
        print(len(self.phrases[0]))

    def decission_maker(self, type, text):
        if type[0] == 0:
            self.tts_msg.data_string = text[0]
        elif type[0] == 1:
            pass


    def run_loop(self):
        """ Infinite loop.

        It does nothing but wait until msgs are received.
        """
        while not rospy.is_shutdown():
            pass

    def stoping_node(self):
        """ROS closing node

        Is the function called when ROS node is closed.
        This function closes all windows opened by opencv"""
        print("\n\nBye bye! :)\n\n")

    def cb_info(self, data):
        print("numeros enteros: ")
        print (data.data_int)
        print("strings: ")
        print(data.data_string)
        self.decission_maker(data.data_int, data.data_string)

if __name__=='__main__':
    """ Main void.

    Is the main void executed when started. It does:
    - Start the node
    - Create an object of the class
    - Run the node

    """
    try:
        rospy.init_node('tts_brain')       # Init ROS node

        text_formation = brain()
        rospy.on_shutdown(text_formation.stoping_node)

        text_formation.run_loop()

    except rospy.ROSInterruptException:
        pass
