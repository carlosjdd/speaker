#!/usr/bin/python3

#If bad interpreter error comes out, run "dos2unix file_name" to decode it

# import the necessary packages
import rospy

# import the necessary msgs. Example with msg type String_Int_Arrays:
from custom_msgs.msg import String_Int_Arrays
from custom_msgs.msg import String_Int

class tiempo_real():
    """ Class tiempo_real.

    Esta clase sirve para hacer que cubo tenga expresiones, mueva la boca y hable en tiempo real.
    """

    def __init__(self):
        """Class constructor

        It is the constructor of the class. It does:
        """

        #Subscribe to ROS topics
        self.name_subscriber = rospy.Subscriber("topic_sub", String_Int_Arrays, self.callback)

        #Define the ROS publishers
        self.tts_pub = rospy.Publisher("tts_text", String_Int, queue_size=0) # Para hacer que Qbo hable

        #Define object as msg type
        self.tts_msg = String_Int()
        self.tts_msg.data_int = 0
        self.tts_msg.data_string = ' '

        self.type_msg = String_Int_Arrays()
        self.type_msg.data_int = [0,0,0]
        self.type_msg.data_string = [""]

        print("[INFO] Node started: " + rospy.get_name())


    def run_loop(self):
        """ Infinite loop.

        When ROS is closed, it exits.
        """
        while not rospy.is_shutdown():
            #functions to repeat until the node is closed
            terminal_input = input()
            
            # if(input == '1')

            self.tts_msg.data_string = terminal_input
            self.tts_pub.publish(self.tts_msg)

            rospy.spin()

    def stopping_node(self):
        """ROS closing node

        Is the function called when ROS node is closed."""
        print("\n[" + rospy.get_name() + "] Bye bye! :)\n")

    def callback(self, data):
        """ROS callback

        This void is executed when a message is received"""

        #Example to publish msg
        self.name_publisher.publish(self.type_msg)


if __name__=='__main__':
    """ Main void.

    Is the main void executed when started. It does:
    - Start the node
    - Create an object of the class
    - Run the node

    """
    try:
        rospy.init_node('ROSnode_name')       # Init ROS node

        class_object = tiempo_real()
        rospy.on_shutdown(class_object.stopping_node)   #When ROS is closed, this void is executed

        class_object.run_loop()

    except rospy.ROSInterruptException:
        pass
