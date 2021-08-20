#PREONICPI - Raspberry Pi PICO
#Rpi pico keyboard keymap
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes


plr7kb = KMKKeyboard()
plr7kb.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
plr7kb.row_pins = (board.GP20, board.GP21, board.GP22, board.GP26, board.GP27)
plr7kb.diode_orientation = DiodeOrientation.COLUMNS
plr7kb.debug_enabled = False
layers_ext = Layers()
nokey = KC.NO

plr7kb.modules = [layers_ext]
plr7kb.debug_enabled = False


plr7kb.keymap = [
    [
    #Layer 0
    KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC, 
    KC.GRAVE, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.DEL, 
    KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, 
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.ENT, 
    KC.LCTL, KC.LGUI, KC.LALT, KC.RALT, KC.MO(1), KC.SPC, KC.SPC, KC.MO(1), KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, 
    ],
    
    [
    #Layer 1
    
    nokey, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, nokey,
    KC.CAPS, KC.F11,  KC.F12,  nokey, nokey, nokey, nokey, KC.MINUS, KC.EQUAL,  KC.LBRC, KC.RBRC, KC.BSLS,
    nokey, KC.VOLD, KC.MUTE, KC.VOLU, nokey, nokey, nokey, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
    nokey, KC.MPRV, KC.MPLY, KC.MNXT, nokey, nokey, nokey, nokey, nokey, nokey, nokey, nokey,
    nokey, nokey, nokey, nokey, KC.TRNS, nokey, nokey, KC.TRNS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
    ],
]

#Simple thing to enable LED on pi once this script is executed
import digitalio
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True
#At this point once the LED is enabled the keyboard should be usable

def usbfunc():
    if __name__ == '__main__':
        plr7kb.go(hid_type=HIDModes.USB) #Wired USB enable
        raise Exception('Something has caused an error.')
        
try:
    usbfunc()
except Exception as e:
    import supervisor
    print(e)
    led.value = False
    supervisor.reload()

supervisor.reload()
#last ditch effort to reset the MCU, if this is being ran then something really is wrong lol
