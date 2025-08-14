#region VEXcode Generated Robot Configuration
from vex import *
import math


# Brain should be defined by default
brain = Brain()

# Wait for rotation sensor to fully initialize
wait(30, MSEC)


# ---------------------------------------------------------------------------- #
#                              MAIN PROGRAM FILE                               #
# ---------------------------------------------------------------------------- #


# Motor Definitions
Left_Back = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)      
Left_Middle = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
Left_Front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)

Right_Back = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
Right_Middle = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
Right_Front = Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)

elevation = DigitalOut(brain.three_wire_port.a)

#Intakes
Intake_one = Motor(Ports.PORT10,GearSetting.RATIO_18_1, True)
Intake_two_1 = Motor(Ports.PORT4,GearSetting.RATIO_18_1, False)
Intake_two_2 = Motor(Ports.PORT6,GearSetting.RATIO_18_1, False)

# Controller and Inertial
controller_1 = Controller(PRIMARY)
inertial_15 = Inertial(Ports.PORT20)
rotational_sensor = Rotation(Ports.PORT5)

# Motor Groups

AllDriveMotors = MotorGroup(Left_Front, Left_Middle, Left_Back, Right_Front, Right_Middle, Right_Back)
FrontMotors = MotorGroup(Left_Front, Right_Front)
BackMotors = MotorGroup(Left_Back, Right_Back)
RightMotors = MotorGroup(Right_Front, Right_Middle, Right_Back)
LeftMotors = MotorGroup(Left_Front, Left_Middle, Left_Back)
Intake = MotorGroup(Intake_one,Intake_two_1, Intake_two_2)


# PID Turn Function Using Inertial Sensor

x = False

def toggle_piston():
   global x
   elevation.set(x) 
   x = not x 

   
def inertial_turn(target_heading):
    actual_heading = inertial_15.heading()
    error = target_heading - actual_heading
    Kp = 0.46
    Ki = 0.005
    Kd = 0.25
    tolerance = 1.5
    integral = 0
    previous_error = error

    while abs(error) > tolerance:
        actual_heading = inertial_15.heading(DEGREES)

        # Normalize error to -180° to 180°
        error = target_heading - actual_heading
        if error > 180:
            error -= 360
        elif error < -180:
            error += 360

        # PID calculations
        integral += error
        integral = max(min(integral, 100), -100)  
        derivative = error - previous_error
        motor_speed = Kp * error + Ki * integral + Kd * derivative

        # Set motor speeds (turn in opposite directions)
        RightMotors.spin(FORWARD, -motor_speed, PERCENT)
        LeftMotors.spin(FORWARD, motor_speed, PERCENT)

        # Display debugging info
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Error: %.2f" % error)
        brain.screen.set_cursor(2, 1)
        brain.screen.print("Heading: %.2f" % actual_heading)
        brain.screen.set_cursor(3, 1)
        brain.screen.print("Motor Speed: %.2f" % motor_speed)

        wait(200, MSEC)
        previous_error = error

    RightMotors.stop()
    LeftMotors.stop()
    brain.screen.clear_screen()
    brain.screen.set_cursor(1,1)
    brain.screen.print("Done")

controller_1.buttonL1.pressed(toggle_piston)

# User Control Code (Tank Drive or Arcade Drive)
def user_control():
    while True:
        # Read joystick axes
        raw_forward = controller_1.axis3.position()  # Forward/backward
        raw_turn = controller_1.axis4.position()     # Left/right

        # Normalize to [-1, 1]
        forward = raw_forward / 100.0
        turn = raw_turn / 100.0

        # Apply quadratic scaling
        forward *= abs(forward)
        turn *= abs(turn)

        # Calculate speeds
        left_speed = (forward + turn) * 100
        right_speed = (forward - turn) * 100

        # Set motor speeds
        LeftMotors.set_velocity(left_speed/2, PERCENT)
        RightMotors.set_velocity(right_speed/2, PERCENT)

        LeftMotors.spin(FORWARD)
        RightMotors.spin(FORWARD)

        
        Intake.set_velocity(100,PERCENT)

        if controller_1.buttonR1.pressing():
          Intake.spin(REVERSE)
        elif controller_1.buttonR2.pressing():
          Intake.spin(FORWARD)
        else:
          Intake.stop()
        

        




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

'''
class odometry:
    def __init__(self, rotation_sensor: Rotation, wheel_diameter: float):
        self.rotation_sensor = rotation_sensor
        self.radius = wheel_diameter / 2 
        self.reset()

    def reset(self):
        self.rotation_sensor.reset_position()
        self.prev_degrees = 0
        self.position_mm = 0

    def update(self):
        current_degrees = self.rotation_sensor.position()
        
        delta_degrees = current_degrees - self.prev_degrees
        
 
        delta_radians = math.radians(delta_degrees)
        
        delta_mm = delta_radians * self.radius
        
        self.position_mm += delta_mm
        
        self.prev_degrees = current_degrees

    def get_position_mm(self):
        return self.position_mm
    


odom = odometry(rotational_sensor, wheel_diameter = 50.8)


def odom_test():
    while True:
        odom.update()
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        brain.screen.print("Position (mm): {:.2f}", odom.get_position_mm())
        wait(100, MSEC)




global_x = 0.0
global_y = 0.0
global_theta = 0.0



previous_horizontal_motor_encoder = 0.0
previous_verticle_motor_encoder = 0.0
previous_theta_angle = 0.0

verticle_motor_encoder = Rotation(Ports.PORT16)
horizontal_motor_encoder = Rotation(Ports.PORT10)
inertial_encoder = Inertial(Ports.PORT18)

def Odometry():

    global global_x, global_y, global_theta
    global previous_horizontal_motor_encoder,previous_verticle_motor_encoder,previous_theta_angle
    #getting current headings
    current_horizontal_motor_encoder = verticle_motor_encoder.position(RotationUnits.DEG)
    current_verticle_motor_encoder = horizontal_motor_encoder.position(RotationUnits.DEG)
    current_inertial_encoder = inertial_encoder.heading()

    #diameter
    horizontal_wheel_diameter = 2
    verticle_wheel_diameter = 2

    circumfrence = horizontal_wheel_diameter * math.pi

    #radius
    horizontal_wheel_radius = horizontal_wheel_diameter / 2.0
    verticle_wheel_radius = verticle_wheel_diameter / 2.0

    #n-variable
    ticks_per_encoder = 360

    #change in Sv and Sh
    delta_horizontal_encoder = current_horizontal_motor_encoder - previous_horizontal_motor_encoder
    delta_verticle_encoder = current_verticle_motor_encoder - previous_verticle_motor_encoder

    #change in theta
    delta_theta = current_inertial_encoder - previous_theta_angle

    #STEP THREE
    delta_horizontal_distance = (delta_horizontal_encoder / ticks_per_encoder) * (circumfrence)
    delta_verticle_distance = (delta_verticle_encoder / ticks_per_encoder) * (circumfrence)

    #STEP FOUR
    theta_avg = current_inertial_encoder + (delta_theta / 2.0)

    #local 
    delta_local_x = delta_horizontal_distance
    delta_local_y = delta_verticle_distance

    delta_global_x = (delta_local_x * math.cos(theta_avg)) - (delta_local_y * math.sin(theta_avg))
    delta_global_y = (delta_local_x * math.sin(theta_avg)) + (delta_local_y * math.cos(theta_avg))

    global_x += delta_global_x
    global_y += delta_global_y
    global_theta += delta_theta

    #STEP SIX
    previous_horizontal_motor_encoder = current_horizontal_motor_encoder
    previous_verticle_motor_encoder = current_verticle_motor_encoder
    previous_theta_angle = current_inertial_encoder

    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("X: {:.2f} in".format(global_x))
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Y: {:.2f} in".format(global_y))
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Theta: {:.2f} deg".format(math.degrees(global_theta)))

def Odometry_Runner():
    global previous_horizontal_motor_encoder, previous_verticle_motor_encoder, previous_theta_angle
    previous_verticle_motor_encoder = verticle_motor_encoder.position(RotationUnits.DEG)
    previous_horizontal_motor_encoder = horizontal_motor_encoder.position(RotationUnits.DEG)
    previous_theta_angle = inertial_encoder.heading(RotationUnits.DEG)

    while True:
        Odometry()
        wait(50, MSEC) 

'''



'''
def pre_auton():
    inertial_15.calibrate()
    while inertial_15.is_calibrating():
            wait(300, MSEC)

def autonomous():
    inertial_turn(90)
    wait(30, MSEC)
    inertial_turn(180)
    
# Start user control
pre_auton()
autonomous()
'''
user_control()
