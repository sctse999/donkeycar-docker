MM1_STEERING_MID = 1550
MM1_MAX_FORWARD = 1620  # Max is 2000
MM1_MAX_REVERSE = 1350
MM1_STOPPED_PWM = 1500
MM1_SHOW_STEERING_VALUE = False
MM1_SERIAL_PORT = '/dev/ttyS0'

THROTTLE_FORWARD_PWM = 395
THROTTLE_STOPPED_PWM = 370  # pwm value for no movement
THROTTLE_REVERSE_PWM = 320  # pwm value for max reverse throttle

# SERVO_ESC|DC_STEER_THROTTLE|DC_TWO_WHEEL|DC_TWO_WHEEL_L298N|SERVO_HBRIDGE_PWM|PIGPIO_PWM|MM1|MOCK
DRIVE_TRAIN_TYPE = "PIGPIO_PWM"

JOYSTICK_MAX_THROTTLE = 1.0
JOYSTICK_THROTTLE_DIR = -1.0

CONTROLLER_TYPE = 'mock'  # (ps3|ps4)
DRIVE_LOOP_HZ = 20

if (CONTROLLER_TYPE == 'F710'):
    JOYSTICK_DEADZONE = 0.1

USE_JOYSTICK_AS_DEFAULT = False

AUTO_CREATE_NEW_TUB = True
MAX_EPOCHS = 30
TRAIN_FILTER = lambda x: x.underlying["user/throttle"] >= 0

USE_SSD1306_128_32 = False  # Enable the SSD_1306 OLED Display


DONKEY_GYM = True
DONKEY_SIM_PATH = "remote" #"/home/tkramer/projects/sdsandbox/sdsim/build/DonkeySimLinux/donkey_sim.x86_64" when racing on virtual-race-league use "remote", or user "remote" when you want to start the sim manually first.
DONKEY_GYM_ENV_NAME = "donkey-generated-roads-v0" # ("donkey-generated-track-v0"|"donkey-generated-roads-v0"|"donkey-warehouse-v0"|"donkey-avc-sparkfun-v0")
GYM_CONF = { "body_style" : "donkey", "body_rgb" : (128, 128, 128), "car_name" : "car", "font_size" : 100} # body style(donkey|bare|car01) body rgb 0-255
GYM_CONF["racer_name"] = "Your Name"
GYM_CONF["country"] = "Hong Kong"
GYM_CONF["bio"] = "I race robots."

SIM_HOST = "host.docker.internal"   


CAMERA_VFLIP = True
CAMERA_HFLIP = True

STEERING_LEFT_PWM = 260
STEERING_RIGHT_PWM = 490
STEERING_PWM_INVERTED = False   #If PWM needs to be inverted

