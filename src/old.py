#region VEXcode Generated Robot Configuration
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Left_Back = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
Left_Middle = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
Left_Front = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
Right_Back = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
Right_Middle = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)
Right_Front = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
Intake = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
inertial_11 = Inertial(Ports.PORT11)
digital_out_c = DigitalOut(brain.three_wire_port.c)
digital_out_a = DigitalOut(brain.three_wire_port.a)
digital_out_b = DigitalOut(brain.three_wire_port.b)





def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
#region VEXcode Generated Robot Configuration
from vex import *


# Brain should be defined by default
brain=Brain()






# ------------------------------------------
#
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode V5 Python Project
#
# ------------------------------------------




# Robot configuration code
Left_Back = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Left_Middle = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
Left_Front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Right_Back = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
Right_Middle = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
Right_Front = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)
Intake = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
digital_out_a = DigitalOut(brain.three_wire_port.a)
digital_out_b = DigitalOut(brain.three_wire_port.b)
inertial_15 = Inertial(Ports.PORT16)
# vex-vision-config:begin
vision_6__BLUERING = Signature(1, -4395, -3623, -4009,6963, 7791, 7377,1.6, 0)
vision_6__REDRING = Signature(2, 9021, 10837, 9929,-1605, -861, -1233,5, 0)
vision_6 = Vision(Ports.PORT6, 50, vision_6__BLUERING, vision_6__REDRING)
# vex-vision-config:end






# ------------------------------------------
#
#   Project:      3400Z V5 Robot
#   Author:       Arav Jain, Arsh Jaiswal, Sripath Badhika, & Alex Reyes
#   Created:      10/15/2024
#   Description:  The top team's robot code!
#
# ------------------------------------------




# Robot configuration code
Left_Back = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
Left_Middle = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
Left_Front = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
Right_Back = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False) #
Right_Middle = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False) #
Right_Front = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False) #
Intake = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
Left_Lady = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
Right_Lady = Motor(Ports.PORT17, GearSetting.RATIO_18_1, False)


controller_1 = Controller(PRIMARY)
inertial_11 = Inertial(Ports.PORT11)




# ------------------------------------------
#
#   Project:      3400Z V5 Robot
#   Author:       Arav Jain & Sripath Badhika
#   Created:      10/15/2024
#   Description:  The code for the top team's robot!
#
# ------------------------------------------






# Define motor groups using built-in MotorGroup class
AllDriveMotors = MotorGroup(Left_Front, Left_Middle, Left_Back, Right_Front, Right_Middle, Right_Back)
FrontMotors = MotorGroup(Left_Front, Right_Front)
BackMotors = MotorGroup(Left_Back, Right_Back)
RightMotors = MotorGroup(Right_Front, Right_Middle, Right_Back)
LeftMotors = MotorGroup(Left_Front, Left_Middle, Left_Back)
Lady_brown = MotorGroup(Left_Lady, Right_Lady)










# Initialize the inertial sensor on Port 15
inertial_15 = Inertial(Ports.PORT16)


'''
def check():
   # Calibrate the inertial sensor
   inertial_15.calibrate()
  
   # Wait until calibration completes
   while inertial_15.is_calibrating():
       wait(100, MSEC)  # Wait for 100 milliseconds before checking again


   # Display a message indicating calibration is complete
   brain.screen.clear_screen()
   brain.screen.print("Calibrated! Now rotating...")


   while True:
       # Get the current heading from the inertial sensor
       actual_heading = inertial_15.heading()


       # Update the screen with the current heading
       brain.screen.clear_screen()  # Clear the screen to avoid clutter
       brain.screen.set_cursor(1, 1)  # Set cursor to the top-left
       brain.screen.print("Heading: {:.2f}".format(actual_heading))  # Display the heading


       # Short delay before updating the screen again
       wait(100, MSEC)  # Adjust delay for smooth updates
'''


inertial_15 = Inertial(Ports.PORT16)


def inertial_turn(target_heading):
   actual_heading = inertial_15.heading()
   error = target_heading - actual_heading
   Kp = 0.6
   Ki = 0.01
   Kd = 0.2
   tolerance = 2
   integral = 0.001
   previous_error = 0.0
   if target_heading == 181:
        tolerance = 0.3
   while abs(error) > tolerance:
       actual_heading = inertial_15.heading(DEGREES)



       # Normalize error to -180° to 180°


       error = target_heading - actual_heading
       if error > 180:
           error -= 360
       elif error < -180:
           error += 360


       # Prevent integral windup (only accumulate small errors)
       if abs(error) < 20:
           integral += error
       else:
           integral = 0  # Reset integral for large errors


       # Derivative term (change in error)
       derivative = error - previous_error
       

       # PID Control Output
       motor_speed = Kp * error + Ki * integral + Kd * derivative



       # Scale motor speed for precision


       # Set motor speeds
       RightMotors.spin(FORWARD, -motor_speed, PERCENT)
       LeftMotors.spin(FORWARD, motor_speed, PERCENT)


       previous_error = error  # Update previous error
       wait(50, MSEC)  # Faster response time


   # Stop motors after the turn
   RightMotors.stop()
   LeftMotors.stop()




check_blue = Event()
check_red = Event()
run_task = True
ring_color = None


def has_blue():
   global ring_color
   brain.screen.clear_row(1)
   brain.screen.set_cursor(1,1)
   vex_vision = vision_6.take_snapshot(vision_6__BLUERING)
   if vex_vision and len(vex_vision) > 0:
       brain.screen.print("Blue Object")
       ring_color = "Blue"
       wait(400,MSEC)
   else:
       brain.screen.print("No Object found")
       ring_color = None






def has_red():
   global ring_color
   brain.screen.clear_row(1)
   brain.screen.set_cursor(1,1)
   vex_vision = vision_6.take_snapshot(vision_6__REDRING)
   if vex_vision and len(vex_vision) > 0:
       brain.screen.print("Red Object")
       ring_color = "Red"
       wait(400, MSEC)
   else:
       brain.screen.print("No Object found")
       ring_color = None


def calling_1():
   global run_task
   while run_task:
       has_blue() 
       if ring_color != "Blue": 
           has_red()
       wait(100, MSEC)
  






front_clamp = DigitalOut(brain.three_wire_port.a)  # Replace 'a' with your actual port
doinker = DigitalOut(brain.three_wire_port.b)  # Replace 'b' with your actual port
doinker_ext = DigitalOut(brain.three_wire_port.c)  # Replace 'b' with your actual port




# Initialize the global variable for piston state
x = False  # False = Retracted, True = Extended
y = False
l = False


def toggle_piston():
   global x
   front_clamp.set(x) 
   x = not x 


def toggle_piston_2():
  global y
  doinker.set(y)
  y = not y


def toggle_piston_3():
  global l
  doinker_ext.set(l)
  l = not l




def pid_test():
   inertial_turn(90)


def turnleft(deg):
   AllDriveMotors.set_velocity(35, PERCENT)
   LeftMotors.spin_for(REVERSE, 1.24*(19/9)*deg, DEGREES, wait=False)
   RightMotors.spin_for(FORWARD, 1.24*(19/9)*deg, DEGREES, wait=False)
   wait(1,SECONDS)


def turnright(deg):
   AllDriveMotors.set_velocity(35, PERCENT)
   LeftMotors.spin_for(FORWARD, 1.24*(19/9)*deg, DEGREES, wait=False)
   RightMotors.spin_for(REVERSE, 1.24*(19/9)*deg, DEGREES, wait=False)
   wait(1, SECONDS)






def deceleration(alpha, direction, dist):
   AllDriveMotors.set_position(0,DEGREES)
   AllDriveMotors.spin(direction)


   while AllDriveMotors.position(DEGREES) < dist and alpha > 0.1:
       alpha = alpha*0.9
       AllDriveMotors.set_velocity(alpha, PERCENT)
       wait(0.1, SECONDS)
      
   AllDriveMotors.stop()


def loading_pos():
   Lady_brown.set_velocity(100,PERCENT)
   Lady_brown.spin_for(REVERSE,35, DEGREES)
   Lady_brown.set_stopping(HOLD)


def scoring_pos():
   Lady_brown.set_velocity(10,PERCENT)
   Lady_brown.spin_for(REVERSE, 150, DEGREES)
   Lady_brown.set_stopping(HOLD)
   wait(1,SECONDS)


def reset_pos():
   Lady_brown.spin(FORWARD)
   wait(1, SECONDS)
   Lady_brown.stop()














def drive_straight(speed, duration):
   initial_heading = inertial_15.heading(DEGREES)  # Store the starting heading
   Kp = 0.8  # Proportional constant for correction


   timer = 0
   while timer < duration:
       current_heading = inertial_15.heading(DEGREES)
      
       # Calculate the error (deviation from initial heading)
       error = current_heading - initial_heading


       # Normalize error to -180° to 180° range
       if error > 180:
           error -= 360
       elif error < -180:
           error += 360


       # Apply correction (reduce motor speed on one side)
       correction = Kp * error


       # Adjust motor speeds
       left_speed = speed - correction
       right_speed = speed + correction


       # Set motor speeds
       LeftMotors.spin(FORWARD, left_speed, PERCENT)
       RightMotors.spin(FORWARD, right_speed, PERCENT)


       # Debugging information
       brain.screen.clear_screen()
       brain.screen.set_cursor(1, 1)
       brain.screen.print("Heading: %.2f" % current_heading)
       brain.screen.set_cursor(2, 1)
       brain.screen.print("Error: %.2f" % error)
       brain.screen.set_cursor(3, 1)
       brain.screen.print("Correction: %.2f" % correction)


       wait(50, MSEC)  # Small delay for control loop
       timer += 50


   # Stop the motors after reaching the target duration
   LeftMotors.stop()
   RightMotors.stop()


def drive_reverse(speed, duration):
   initial_heading = inertial_15.heading(DEGREES)  # Store the starting heading
   Kp = 0.8  # Proportional constant for correction


   timer = 0
   while timer < duration:
       current_heading = inertial_15.heading(DEGREES)

       if speed == 50 and duration == 2500:
           if timer == 2500 * 0.85:
               front_clamp.set(False)


       # Calculate the error (deviation from initial heading)
       error = current_heading - initial_heading


       # Normalize error to -180° to 180° range
       if error > 180:
           error -= 360
       elif error < -180:
           error += 360


       # Apply correction (reduce motor speed on one side)
       correction = Kp * error


       # Adjust motor speeds
       left_speed = speed + correction
       right_speed = speed - correction


       # Set motor speeds
       LeftMotors.spin(REVERSE, left_speed, PERCENT)
       RightMotors.spin(REVERSE, right_speed, PERCENT)


       # Debugging information
       brain.screen.clear_screen()
       brain.screen.set_cursor(1, 1)
       brain.screen.print("Heading: %.2f" % current_heading)
       brain.screen.set_cursor(2, 1)
       brain.screen.print("Error: %.2f" % error)
       brain.screen.set_cursor(3, 1)
       brain.screen.print("Correction: %.2f" % correction)


       wait(50, MSEC)  # Small delay for control loop
       timer += 50


   # Stop the motors after reaching the target duration
   LeftMotors.stop()
   RightMotors.stop()


def pid_arc(target_heading, base_speed = 50):
   actual_heading = inertial_15.heading()
   error = target_heading - actual_heading
   Kp = 0.6
   Ki = 0.01
   Kd = 0.2
   tolerance = 2
   integral = 0.001
   previous_error = 0.0


   while abs(error) > tolerance:


       integral += error
       derivative = error - previous_error


       # Normalize error to -180° to 180°
       error = target_heading - actual_heading
       if error > 180:
           error -= 360
       elif error < -180:
           error += 360


       # Prevent integral windup (only accumulate small errors)
       if abs(error) < 20:
           integral += error
       else:
           integral = 0  # Reset integral for large errors


       derivative = error - previous_error


      
       motor_speed = Kp * error + Ki * integral + Kd * derivative




       left_speed = base_speed + motor_speed
       right_speed = base_speed - motor_speed


       # Set motor speeds
       LeftMotors.spin(FORWARD, left_speed, PERCENT)
       RightMotors.spin(FORWARD, right_speed, PERCENT)


       previous_error = error
       wait(20, MSEC)  # Small delay to prevent CPU overload


   # Stop motors when target is reached
   LeftMotors.stop()
   RightMotors.stop()


def drive_with_clamp(speed, duration):
    initial_heading = inertial_15.heading(DEGREES)  
    Kp = 0.8  

    timer = 0
    while timer < duration:
        current_heading = inertial_15.heading(DEGREES)
        error = current_heading - initial_heading

        if error > 180:
            error -= 360
        elif error < -180:
            error += 360

        correction = Kp * error

        left_speed = speed - correction
        right_speed = speed + correction

        LeftMotors.spin(REVERSE, left_speed, PERCENT)
        RightMotors.spin(REVERSE, right_speed, PERCENT)

        # Activate the clamp after half the distance
        if timer == duration*0.15:
            front_clamp.set(False)

        wait(50, MSEC)  
        timer += 50

    LeftMotors.stop()
    RightMotors.stop()

  


    '''
   inertial_turn(-145) # set heading to -165; add 30 to all degrees when running actual
   drive_reverse(40, 1000)
   wait(0.25, SECONDS)
   front_clamp.set(False)
   drive_reverse(15, 3000)
   inertial_turn(-35)
   doinker.set(True)
   drive_straight(40,200)
   inertial_turn(-90)
   drive_straight(40,400)
   inertial_turn(-200)
   '''


def redRightMatchAuton():
    drive_reverse(40, 500)
    inertial_turn(-40)
    front_clamp.set(True)
    drive_straight(40, 1000)
    front_clamp.set(False)
    Intake.set_velocity(100, PERCENT)
    Intake.spin(REVERSE)
    inertial_turn(92)
    drive_straight(40, 1200)



def left_side():

    Intake.set_velocity(100, PERCENT)
    front_clamp.set(True)
    drive_reverse(50,900)
    wait(.5, SECONDS)
    front_clamp.set(False)
    wait(.5, SECONDS)
    Intake.spin(REVERSE)
    inertial_turn(56)
    drive_straight(40, 650)
    wait(3, SECONDS)
    Intake.stop()
    '''
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

    # Continuously display the heading
    while True:
        heading = inertial_15.heading(DEGREES)  # Get heading in degrees
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Heading: {:.2f}°".format(heading))  # Display heading
        wait(100, MSEC)  # Update every 100ms
    '''


def right_blue():
    
    Intake.set_velocity(100, PERCENT)
    front_clamp.set(True)
    drive_reverse(50,1000)
    wait(.5, SECONDS)
    front_clamp.set(False)
    wait(.5, SECONDS)
    Intake.spin(REVERSE)
    inertial_turn(-60)
    drive_straight(40, 700)
    '''
    inertial_turn(-140)
    wait(0.5, SECONDS)
    drive_straight(20,1130)
    wait(1, SECONDS)
    drive_reverse(20,300)
    inertial_turn(-118.5)
    drive_straight(20, 510)
    wait(1, SECONDS)
    drive_reverse(50, 200)
    '''

    

    '''
   Intake.set_velocity(100, PERCENT)
   front_clamp.set(True)
   drive_reverse(50,1000)
   wait(0.5, SECONDS)
   front_clamp.set(False)
   wait(1,SECONDS)
   Intake.spin(REVERSE)
   inertial_turn(45)
   drive_straight(60, 1000)
   inertial_turn(170)
   drive_straight(30, 1200)
   drive_reverse(30, 200)
   wait(1, SECONDS)
   inertial_turn(130)
   drive_straight(30, 500)
   wait(1, SECONDS)
   drive_reverse(40, 500)
   '''




    # Continuously display the heading

def new_auton():
    Intake.set_velocity(100, PERCENT)
    drive_reverse(60, 800)
    inertial_turn(-30)
    front_clamp.set(True)
    drive_reverse(50, 400)
    wait(1,SECONDS)
    front_clamp.set(False)
    Intake.spin(REVERSE)
    inertial_turn(90)
    drive_straight(70, 700)
    inertial_turn(0)
    Intake.stop()






'''
competition = Competition(user_control, left_side)

'''

def macro_1():
    Intake.set_velocity(80, PERCENT)
    Intake.spin(REVERSE)
    wait(0.5, SECONDS)
    Intake.stop()
    Intake.set_velocity(100, PERCENT)
    front_clamp.set(True)
    #---------------------------------


    #Driving towards the Mobile Goal and Clamp
    drive_straight(40, 480)
    inertial_turn(-90)
    drive_reverse(30, 1200)
    front_clamp.set(False)
    wait(500, MSEC)
    drive_straight(40, 930)
    #----------------------------------


    #Turn towards First and Second Ring and Pickup
    inertial_turn(45)
    Intake.spin(REVERSE)
    drive_straight(70, 1695)
    wait(500, MSEC)
    inertial_turn(7)
    wait(300, MSEC)
    drive_straight(100, 500)


    #-----------------------------------------------


    #Pickup 3 ring first try in a row
    inertial_turn(182.5)
    wait(.15,SECONDS)
    drive_straight(60, 1500)

  
#Intake R1
#outake R2
'''
def lady_brown_hold():
   Lady_brown.set_velocity(100, PERCENT)
   Lady_brown.spin_for(REVERSE, 200, DEGREES)
   Lady_brown.stop()
'''
# Bind Button to Function


#controller_1.buttonL2.pressed(lady_brown_hold)
controller_1.buttonL1.pressed(toggle_piston)
controller_1.buttonY.pressed(toggle_piston_2)
controller_1.buttonUp.pressed(toggle_piston_3)
controller_1.buttonDown.pressed(macro_1)



def user_control():
  #solenoid_state = False  # Initial state of the solenoid
  global calling
  calling = True
#    task_1 = Thread(calling_1)
  global ring_color
  lady_phase = 0


  while True:
      Lady_brown.set_velocity(20, PERCENT)
   #    if controller_1.buttonX.pressing() and (lady_angle < lady_max):
   #        Lady_brown.spin_for(FORWARD,1,DEGREES)
   #        lady_angle += 1
   #    elif controller_1.buttonA.pressing():
   #        Lady_brown.spin(REVERSE)
   #    else:
   #        Lady_brown.stop()
      if controller_1.buttonDown.pressing():
          macro_1()
    
     
      if controller_1.buttonX.pressing():
          lady_phase += 1
          if lady_phase == 1:
              Lady_brown.set_stopping(HOLD)
              Lady_brown.spin_for(REVERSE,28,DEGREES)
          if lady_phase == 2:
              Lady_brown.set_stopping(HOLD)
              Lady_brown.spin_for(REVERSE,145,DEGREES)
          if lady_phase == 3:
              Lady_brown.spin(FORWARD)
              wait(1,SECONDS)
              Lady_brown.stop()
              lady_phase = 0
          wait(0.5,SECONDS)
         
      if controller_1.buttonRight.pressing():
          Lady_brown.spin_for(REVERSE,15,DEGREES)
      if controller_1.buttonLeft.pressing():
          Lady_brown.spin_for(FORWARD,5,DEGREES)

      # Get the joystick values from the left joystick
      raw_forward = controller_1.axis3.position()  # Forward/backward movement (left joystick up/down)
      raw_turn = controller_1.axis4.position()
      raw_turn_axis_1 = controller_1.axis1.position()
    
         # Turning left/right (left joystick left/right)


      # Define pneumatic solenoid
      # Apply quadratic scaling for smoother control
      # Normalize joystick values to range [-1, 1]
      forward = raw_forward / 100.0
      turn = raw_turn / 100.0
      turn_axis_1 = raw_turn_axis_1 / 100.0




      # Quadratic scaling to adjust sensitivity
      forward = (forward * abs(forward)) * 0.7 # Quadratic scaling for forward
      turn = (turn * abs(turn)) * 0.4
      turn_axis_1 = (turn_axis_1 * abs(turn_axis_1)) * 0.15


      # Scale back to motor speed range [-100, 100]
      left_speed = (forward + turn + turn_axis_1) * 100
      right_speed = (forward - turn - turn_axis_1) * 100


      # Set the speed for each motor group
      LeftMotors.set_velocity(left_speed, PERCENT)
      RightMotors.set_velocity(right_speed, PERCENT)
      


      Intake.set_velocity(150, PERCENT)
      # Spin the motors accordingly
   
      LeftMotors.spin(FORWARD)
      RightMotors.spin(FORWARD)


      if controller_1.buttonX.pressing():
          calling = False
         
      if ring_color == "Blue":
          Intake.set_velocity(55,PERCENT)
      else:
          Intake.set_velocity(200, PERCENT)  # Default velocity


      # Control intake motor
      if controller_1.buttonR1.pressing():
          Intake.spin(FORWARD)


      elif controller_1.buttonR2.pressing():
          Intake.spin(REVERSE)
      else:
          Intake.stop()


      # Add a short delay to prevent wasted resources
      wait(20, MSEC)


def pre_autonomous():
   inertial_15.calibrate()
   while inertial_15.is_calibrating():
       wait(400, MSEC)  # Wait until calibration completes


def skills_auto():

   #Scoring alliance stake
   Intake.set_velocity(80, PERCENT)
   Intake.spin(REVERSE)
   wait(0.5, SECONDS)
   Intake.stop()
   Intake.set_velocity(100, PERCENT)
   front_clamp.set(True)
   #---------------------------------


   #Driving towards the Mobile Goal and Clamp
   drive_straight(40, 480)
   inertial_turn(-90)
   drive_reverse(30, 1200)
   front_clamp.set(False)
   wait(500, MSEC)
   drive_straight(40, 910)
   #----------------------------------


   #Turn towards First and Second Ring and Pickup
   inertial_turn(45)
   Intake.spin(REVERSE)
   drive_straight(70, 1720)
   wait(500, MSEC)
   inertial_turn(7)
   wait(300, MSEC)
   drive_straight(100, 500)


   #-----------------------------------------------


   #Pickup 3 ring first try in a row
   '''
   inertial_turn(90)
   wait(0.5, SECONDS)
   inertial_turn(178)
   '''
   inertial_turn(181)
   wait(.5,SECONDS)
   drive_straight(60, 1500)
   wait(.5,SECONDS)
   drive_straight(20, 3700)
   wait(.1,SECONDS)
  
   #---------------------------------------------------


   #Drive Backwards and Pickup Last Ring and Score it
   drive_reverse(30, 500)
   inertial_turn(71)
   drive_straight(40, 470)
   drive_reverse(30,540)
   inertial_turn(-30)
   drive_reverse(40, 690)
   front_clamp.set(True)
   wait(.01,SECONDS)
   Intake.spin(FORWARD)
   wait(0.25, SECONDS)
   drive_straight(50,310)
   Intake.stop()
   #------------------------------------------------------


   #Head Towards the Second Mobile Goal and Clamp
   inertial_turn(90)
   Intake.set_velocity(100,PERCENT)
   Intake.spin(REVERSE)
   front_clamp.set(True)
   drive_reverse(50, 2500)
   front_clamp.set(False)
   drive_straight(70, 750)


   #Turn to face the first ring on second side
   inertial_turn(-45)
   drive_straight(70,1620)
   #-------------------------------------------


   #Pickup second Ring and score
   inertial_turn(0)
   drive_straight(50, 1000)
   #-----------------------------


   #Pickup 3-rings in a row
   inertial_turn(90)
   wait(0.5,SECONDS)
   inertial_turn(181)
   drive_straight(60, 1430)
   wait(.05, SECONDS)
   drive_straight(16, 4100)
   wait(.25,SECONDS)
 #  drive_straight(16, 700)
  # wait(1,SECONDS)
   #-----------------------------
  
   #Drive backwards to pickup last ring and score it
   drive_reverse(30, 650)
   inertial_turn(-90)
   drive_straight(40, 500)
   drive_reverse(30,550)
   inertial_turn(40)
   drive_reverse(40, 580)
   front_clamp.set(True)
   Intake.spin(REVERSE)
   wait(0.5, SECONDS)
   Intake.stop()
   drive_straight(50,420)


   #-----------------------------------------------------
   #Going to the third mobile goal
   Intake.spin(REVERSE)
   inertial_turn(0) # set heading to -30
   drive_straight(100,1000)
   inertial_turn(45)
   drive_straight(60,900)
   front_clamp.set(True)
   Intake.stop()
   inertial_turn(180)
   drive_reverse(100,700)
   front_clamp.set(False)
   inertial_turn(97)
   drive_reverse(100, 2000)
   front_clamp.set(True)
   drive_straight(100, 700)
   Intake.spin(FORWARD)
   inertial_turn(90)
   drive_straight(100, 3000)
   Intake.stop()


pre_autonomous()
#competition = Competition(user_control, left_side) #Game Left Red
#competition = Competition(user_control, right_blue) # Game right blue


competition = Competition(user_control, new_auton) # skills

#skills_auto()
