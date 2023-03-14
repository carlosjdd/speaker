#!/usr/bin/python2

# import the necessary packages
import rospy
import rospkg

import openai

from custom_msgs.msg import String_Int_Arrays
from custom_msgs.msg import String_Int

import csv
import random

class brain():
    """ Class brain.

    Is the class that gets the information of the people in the image
    """

    def __init__(self):
        """Class constructor

        It is the constructor of the class. It does:
        - Subscribe itself to the topics
        """
        openai.api_key = "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"

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
        self.path_greetings = rospack.get_path(pkg_name) + "/data/database01_greetings.csv"
        self.path_wait_detection = rospack.get_path(pkg_name) + "/data/database02_wait_recognition.csv"
        self.path_noone = rospack.get_path(pkg_name) + "/data/database03_noone.csv"
        self.path_only_unknown = rospack.get_path(pkg_name) + "/data/database04_only_unknown.csv"
        self.path_one_known = rospack.get_path(pkg_name) + "/data/database05_one_known.csv"
        self.path_many_known = rospack.get_path(pkg_name) + "/data/database06_many_known.csv"
        self.path_one_unknown = rospack.get_path(pkg_name) + "/data/database07_one_unknown.csv"
        self.path_many_unknown = rospack.get_path(pkg_name) + "/data/database08_many_unknown.csv"
        self.path_name = rospack.get_path(pkg_name) + "/data/database09_name.csv"
        self.path_blame = rospack.get_path(pkg_name) + "/data/database10_blame.csv"
        self.path_fr_hi = rospack.get_path(pkg_name) + "/data/database11_fragance_hello.csv"
        self.path_fr_look = rospack.get_path(pkg_name) + "/data/database12_fragance_look.csv"
        self.path_fr_no = rospack.get_path(pkg_name) + "/data/database13_fragance_no.csv"
        self.path_fr_yes = rospack.get_path(pkg_name) + "/data/database14_fragance_yes.csv"
        self.path_fr_also = rospack.get_path(pkg_name) + "/data/database15_fragance_also.csv"
        self.path_alexa = rospack.get_path(pkg_name) + "/data/database16_alexa.csv"
        self.path_qbo_hi = rospack.get_path(pkg_name) + "/data/database17_qbo_hi.csv"
        self.path_qbo_presentation = rospack.get_path(pkg_name) + "/data/database18_qbo_presentation.csv"
        self.path_qbo_answer = rospack.get_path(pkg_name) + "/data/database19_qbo_answer.csv"
        self.path_frases_celebres = rospack.get_path(pkg_name) + "/data/database20_frases_celebres.csv"
        self.path_frases_absurdas = rospack.get_path(pkg_name) + "/data/database21_frases_absurdas.csv"
        self.path_police = rospack.get_path(pkg_name) + "/data/database22_policia.csv"
        self.path_nothing = rospack.get_path(pkg_name) + "/data/database23_nothing_asked.csv"
        self.path_chistes = rospack.get_path(pkg_name) + "/data/database24_chistes.csv"
        self.path_curiosidades = rospack.get_path(pkg_name) + "/data/database25_curiosidades.csv"
        self.path_ofertas = rospack.get_path(pkg_name) + "/data/database26_ofertas.csv"
        self.path_cinco = rospack.get_path(pkg_name) + "/data/database27_cinco.csv"

        print("[INFO] Ready to receive info")

        self.open_data()


    def open_data(self):

        self.phrases = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]     #Start the list with as much arrays as databases needed

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
                self.phrases[2].append(row[0])					            # Save ]the path of every SVG file into the array

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

        with open(self.path_name) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[9].append(row[0])					            # Save the path of every SVG file into the array
                self.phrases[10].append(row[1])

        with open(self.path_blame) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[11].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_fr_hi) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                self.phrases[12].append(row[0])

        with open(self.path_fr_look) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                self.phrases[13].append(row[0])

        with open(self.path_fr_no) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                self.phrases[14].append(row[0])

        with open(self.path_fr_yes) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                self.phrases[15].append(row[0])

        with open(self.path_fr_also) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                self.phrases[16].append(row[0])

        with open(self.path_alexa) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[17].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_qbo_hi) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[18].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_qbo_presentation) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[19].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_qbo_answer) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[20].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_frases_celebres) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[21].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_frases_absurdas) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[22].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_police) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[23].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_nothing) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[24].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_chistes) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[25].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_curiosidades) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[26].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_ofertas) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[27].append(row[0])					            # Save the path of every SVG file into the array

        with open(self.path_cinco) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")	            # Read the csv file
            for row in csv_reader:								        # Go through every row in the csv file
                self.phrases[28].append(row[0])					            # Save the path of every SVG file into the array
                self.phrases[29].append(row[1])


    def decission_maker(self, type, text):

        # In case type is 0, it is send to speak the exactly same text that has been received
        if type[0] == 0:
            self.tts_msg.data_string = text[0]

        # In case type is 1 or 2, it is send to speak a phrase from the self.phrase[0] and self.phrase[1] respectively
        elif type[0] == 1 or type[0] == 2:
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]-1]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]-1][random.randint(0,len(self.phrases[type[0]-1])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]-1][type[1]-1]

        # In case type is 3, it is necessary to know if there is noone in front of the camera. If there is noone known, if there is someone known and if there is also someone unknown
        elif type[0] == 3:
            if text[0] == '' and type[2] <= 0:
                if type[1] <= 0 or type[1] > len(self.phrases[type[0]-1]):                                                                                       # If the type[1] is 0, or a wrong number, a random phrase is said.
                    self.tts_msg.data_string = self.phrases[type[0]-1][random.randint(0,len(self.phrases[type[0]-1])-1)]
                else:                                                                                                                                             #Otherwise, it is said the phrase indicated in the type[1]
                    self.tts_msg.data_string = self.phrases[type[0]-1][type[1]-1]
            elif text[0] != '':
                if len(text) == 1:
                    if type[1] <= 0 or type[1] > len(self.phrases[type[0]+1]):                                                                                    # If the type[1] is 0, or a wrong number, a random phrase is said.
                        self.tts_msg.data_string = self.phrases[type[0]+1][random.randint(0,len(self.phrases[type[0]+1])-1)] + text[0] + ', '
                    else:                                                                                                                                         #Otherwise, it is said the phrase indicated in the type[1]
                        self.tts_msg.data_string = self.phrases[type[0]+1][type[1]-1] + text[0] + ', '
                else:
                    if type[1] <= 0 or type[1] > len(self.phrases[type[0]+2]):                                                                                    # If the type[1] is 0, or a wrong number, a random phrase is said.
                        self.tts_msg.data_string = self.phrases[type[0]+2][random.randint(0,len(self.phrases[type[0]+2])-1)]
                    else:                                                                                                                                         #Otherwise, it is said the phrase indicated in the type[1]
                        self.tts_msg.data_string = self.phrases[type[0]+2][type[1]-1]
                    for i in text:
                        self.tts_msg.data_string = self.tts_msg.data_string + i + ', '
            else:
                if type[1] <= 0 or type[1] > len(self.phrases[type[0]]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                    self.tts_msg.data_string = self.phrases[type[0]][random.randint(0,len(self.phrases[type[0]])-1)]
                else:                                                                                                                                             #Otherwise, it is said the phrase indicated in the type[1]
                    self.tts_msg.data_string = self.phrases[type[0]][type[1]-1]

            if type[2] == 1:
                if type[1] <= 0 or type[1] > len(self.phrases[type[0]+3]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                    self.tts_msg.data_string = self.tts_msg.data_string + self.phrases[type[0]+3][random.randint(0,len(self.phrases[type[0]+3])-1)]
                else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                    self.tts_msg.data_string = self.tts_msg.data_string + self.phrases[type[0]+3][type[1]-1]
            elif type[2] > 1:
                if type[1] <= 0 or type[1] > len(self.phrases[type[0]+4]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                    num_random = random.randint(0,len(self.phrases[type[0]+4])-1)
                    self.tts_msg.data_string = self.tts_msg.data_string + self.phrases[type[0]+4][num_random] + str(type[2]) + self.phrases[type[0]+5][num_random]
                else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                    self.tts_msg.data_string = self.tts_msg.data_string + self.phrases[type[0]+4][type[1]-1] + str(type[2]) + self.phrases[type[0]+5][type[1]-1]

        elif type[0] == 4:
            random_value = random.randint(0,len(self.phrases[type[0]+5])-1)
            full_text = ""
            for i in text:
                full_text += i
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+5]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+5][random_value] + full_text + " " + self.phrases[type[0]+6][random_value]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+5][type[1]-1]+ full_text + " " + self.phrases[type[0]+6][type[1]-1]

        elif type[0] >= 5 and type[0] <= 8:
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+6]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+6][random.randint(0,len(self.phrases[type[0]+6])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+6][type[1]-1]

        elif type[0] == 9 or type[0] == 10:
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+6]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+6][random.randint(0,len(self.phrases[type[0]+6])-1)] + str(type[2])
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+6][type[1]-1] + str(type [2])

        elif type[0] == 11:
            """
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+6]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+6][0]
                self.tts_pub.publish(self.tts_msg)
                self.tts_msg.data_string = self.phrases[type[0]+6][random.randint(1,len(self.phrases[type[0]+6])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+6][0]
                self.tts_pub.publish(self.tts_msg)
                self.tts_msg.data_string = self.phrases[type[0]+6][type[1]-1] """

            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+6]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+6][0] + ", " + self.phrases[type[0]+6][random.randint(1,len(self.phrases[type[0]+6])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+6][0] + ", " + self.phrases[type[0]+6][type[1]-1]

        elif type[0] == 12 or type[0] == 13:
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+6]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+6][random.randint(0,len(self.phrases[type[0]+6])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+6][type[1]-1]

        elif type[0] == 14:
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+6]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+6][random.randint(0,len(self.phrases[type[0]+6])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+6][type[1]-1]

        elif type[0] == 15:
            full_text = ""
            for i in text:
                full_text += i
            #Uncomment next lines to ask alexa:                                                                                                                                                       #Otherwise, it is said the phrase indicated in the type[1]
            #self.tts_msg.data_string = self.phrases[17][0] + ", " + full_text
            
            #Uncomment next lines to ask ChatGPT
            full_text = full_text + "en 20 palabras maximo"
            completion = openai.Completion.create(engine="text-davinci-003", prompt=full_text, max_tokens=2048)
            self.tts_msg.data_string = completion.choices[0].text

        elif type[0] >= 16 and type[0] <= 24:
            if type[1] <= 0 or type[1] > len(self.phrases[type[0]+5]):                                                                                          # If the type[1] is 0, or a wrong number, a random phrase is said.
                self.tts_msg.data_string = self.phrases[type[0]+5][random.randint(0,len(self.phrases[type[0]+5])-1)]
            else:                                                                                                                                               #Otherwise, it is said the phrase indicated in the type[1]
                self.tts_msg.data_string = self.phrases[type[0]+5][type[1]-1]

        print (self.tts_msg.data_string)
        self.tts_pub.publish(self.tts_msg)

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
