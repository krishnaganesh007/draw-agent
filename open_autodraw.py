import subprocess
import time
import pyautogui


def is_autodraw_open():
    applescript = '''
    tell application "Google Chrome"
        set window_list to every window
        repeat with the_window in window_list
            set tab_list to every tab of the_window
            repeat with the_tab in tab_list
                set the_url to the_tab's URL
                if the_url starts with "https://www.autodraw.com" then
                    return true
                end if
            end repeat
        end repeat
        return false
    end tell
    '''
    result = subprocess.run(
        ['osascript', '-e', applescript],
        capture_output=True,
        text=True
    )
    return "true" in result.stdout



def switch_to_autodraw_tab():
    applescript = '''
    tell application "Google Chrome"
        repeat with the_window in every window
            set tab_index to 0
            repeat with the_tab in every tab of the_window
                set tab_index to tab_index + 1
                if (the_tab's URL starts with "https://www.autodraw.com") then
                    set active tab index of the_window to tab_index
                    set index of the_window to 1
                    activate
                    return
                end if
            end repeat
        end repeat
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript])



def ensure_autodraw_and_draw_rectangle(x1, y1, x2, y2, draw_button_x, draw_button_y):
    """
    Ensure AutoDraw is open (or open it), then draw a rectangle.
    """
    if is_autodraw_open():
        print("AutoDraw tab is open, switching to it.")
        switch_to_autodraw_tab()
    else:
        print("AutoDraw not open, launching it.")
        subprocess.run(['open', '-a', 'Google Chrome', 'https://www.autodraw.com'])
        time.sleep(5)  # Wait for AutoDraw to load

    # Drawing rectangle:
    time.sleep(2)  # Make sure browser is ready
    pyautogui.click(draw_button_x, draw_button_y, duration=0.25)
    time.sleep(0.5)
    pyautogui.moveTo(x1, y1)
    time.sleep(0.4)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.moveTo(x2, y1, duration=0.3)
    pyautogui.moveTo(x2, y2, duration=0.3)
    pyautogui.moveTo(x1, y2, duration=0.3)
    pyautogui.moveTo(x1, y1, duration=0.3)
    pyautogui.moveTo(x2, y1, duration=0.3)
    pyautogui.mouseUp(button='left')
    
    print(f"Clicked Draw button at ({draw_button_x}, {draw_button_y}) and drew rectangle from ({x1}, {y1}) to ({x2}, {y2})")
    return f"Clicked Draw button at ({draw_button_x}, {draw_button_y}) and drew rectangle from ({x1}, {y1}) to ({x2}, {y2})"


def ensure_autodraw_and_write_text(x_text_tool, y_text_tool, x, y, text):
    """
    Ensure AutoDraw is open (or open it), then write text.
    """
    if is_autodraw_open():
        print("AutoDraw tab is open, switching to it.")
        switch_to_autodraw_tab()
    else:
        print("AutoDraw not open, launching it.")
        subprocess.run(['open', '-a', 'Google Chrome', 'https://www.autodraw.com'])
        time.sleep(5)  # Wait for AutoDraw to load

    # Writing text:
    time.sleep(1)
    pyautogui.click(x_text_tool, y_text_tool, duration=0.7)
    time.sleep(0.4)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write(text, interval=0.08)
    
    print(f'Typed "{text}" at ({x}, {y}) on AutoDraw.')
    return f'Typed "{text}" at ({x}, {y}) on AutoDraw.'



# ensure_autodraw_and_draw_rectangle(300, 700, 1000, 500, 45, 375) #342)
# ensure_autodraw_and_write_text(45, 450, 400, 600, "Hello, AutoDraw!")


def draw_rectangle(
    x1: int, y1: int, x2: int, y2: int,
    draw_button_x: int, draw_button_y: int
) -> dict:
    """
    Click the AutoDraw 'Draw' tool and draw a rectangle on the canvas.
    Returns both a JSON body and explicit content blocks.
    """
    try:
        if is_autodraw_open():
            print("AutoDraw tab is open, switching to it.")
            switch_to_autodraw_tab()
        else:
            print("AutoDraw not open, launching it.")
            subprocess.run(['open', '-a', 'Google Chrome', 'https://www.autodraw.com'])
            time.sleep(3)

        time.sleep(1.2)
        pyautogui.click(draw_button_x, draw_button_y, duration=0.25)
        time.sleep(0.5)

        pyautogui.moveTo(x1, y1)
        time.sleep(0.3)
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.moveTo(x2, y1, duration=0.8)
        pyautogui.moveTo(x2, y2, duration=0.5)
        pyautogui.moveTo(x1, y2, duration=0.5)
        pyautogui.moveTo(x1, y1, duration=0.9)
        pyautogui.moveTo(x2, y1, duration=0.3)
        pyautogui.mouseUp(button='left')

        msg = f"Drew rectangle from ({x1},{y1}) to ({x2},{y2}) after clicking Draw at ({draw_button_x},{draw_button_y})."

        return {
            "status": "success",
            "message": msg
        }
    except Exception as e:
        err = f"Error drawing rectangle: {e}"
        return err

draw_rectangle(300, 700, 1000, 500, 45, 375) #342)