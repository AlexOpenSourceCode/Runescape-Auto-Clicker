from rslib import *
from rs_binds import tab_bottom_right_offsets
import traceback
import time
import random

def generate_random_float(low_f, high_f):
    return random.uniform(low_f,high_f)

while True:
    try:
        active_window = get_active_window()
        active_window_name = get_window_name(active_window)


        if contains_any(active_window_name,['OSBuddy', 'RS', 'runescape', 'RuneScape', 'Konduit']):
            original_mouse_x, original_mouse_y = get_mouse_position()


            active_window_x, active_window_y  = get_window_position(active_window)
            active_window_width, active_window_height = get_window_size(active_window)

            def click_rs_item(item_name):

                rs_click_x = active_window_width + tab_bottom_right_offsets[item_name][0]
                rs_click_y = active_window_height + tab_bottom_right_offsets[item_name][1]


                active_window_x, active_window_y = get_window_position(active_window)
                screen_click_x = active_window_x + rs_click_x
                screen_click_y = active_window_y + rs_click_y
                click(screen_click_x, screen_click_y)


            def click_rs(x,y):

                rs_click_x = active_window_width + x
                rs_click_y = active_window_height + y


                active_window_x, active_window_y = get_window_position(active_window)
                screen_click_x = active_window_x + rs_click_x
                screen_click_y = active_window_y + rs_click_y
                click(screen_click_x, screen_click_y)



            base_point = (-50, -180)

            click(original_mouse_x, original_mouse_y)

            time.sleep(generate_random_float(0.3,.5))

    except:
        traceback.print_exc()