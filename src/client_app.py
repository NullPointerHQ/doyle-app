# =============================================
#         'To-Do List' Client App 
# =============================================
import flet as ft
import time as time
from pathlib import Path

# - App Mascot and Name GUI Elements
def title_card():
    # - Settings for Mascot's Head and Name
    title_card = ft.Container(
        content= ft.Column(
            controls = [
                # -  Image Settings
                ft.Image(
                        src = "/mascot.png",# - TODO: Come up with some app mascot
                        width = 120,
                        height = 120,
                        fit = ft.BoxFit.CONTAIN,
                        ),
                        # - Title Settings
                        ft.Text(value = "Placeholder", size = 35, italic = True),
                    ],
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
        margin = ft.Margin(left=0,top=20, right=0, bottom= 400), # - Adjusts the placement of the card (Remember: Controls are inverted)
        )
    # - Compiled
    cover = ft.Column(controls = [title_card], horizontal_alignment = ft.CrossAxisAlignment.CENTER)
    return cover

def loading():
    # - Settings for Mascot's Head and Name
    loading_text = ft.Container(
        # - Text Settings
        content = ft.Text(value = "Pulling up your list...", size = 35, italic = True),
        opacity = 0,
        animate_opacity = ft.Animation(duration = 800, curve = ft.AnimationCurve.EASE_IN_OUT),
        )

    # - Loading Wheel Settings        
    hamster_wheel = ft.Container(content = ft.ProgressRing(width=28, height=28, stroke_width= 3, color= ft.Colors.CYAN), 
        opacity = 0,
        animate_opacity = ft.Animation(duration = 800, curve = ft.AnimationCurve.EASE_IN_OUT),
    )

    # - Combining The text and hamster wheel into one box
    loading_card = ft.Container(content=ft.Column(controls=[loading_text, hamster_wheel], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
    margin = ft.Margin(left=0,top=20, right=0, bottom= 20), # - Adjusts the placement of the card (Remember: Controls are inverted)
    )  
    return loading_card, loading_text, hamster_wheel

# - Main App Operation 
def main(page: ft.Page):

    # - Universal Configs
    page.title = "App"
    # - App screen dimensions and configs
    page.window.width = 390
    page.window.height = 800
    page.window.resizable = False 
    page.window.maximizable = False

    # - Universal Aesthetics
    page.theme_mode = ft.ThemeMode.DARK # - Forces Dark Mode which is generally preferred
    page.bgcolor = "#22262b" # - Background color, Current: SLATE
    page.theme = ft.Theme(color_scheme_seed = ft.Colors.CYAN) # - Core Color for Doyle

    # - Forcing UI Elements to default to the center
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.padding = 0
    
    page.add(title_card()) # - Bringing in the title card elements

    
    # - Updating GUI for DB Initialization
    init_card, init_text, init_hamster_wheel = loading() # - Setting up Loading Screen Objects
    page.add(init_card) # - Foundation for Load Screen Anims
    time.sleep(0.3) 

    # - Text Fade In
    init_text.opacity = 1 
    page.update()
    time.sleep(0.8)

    # - Wheel Fade In and Simmed Loading
    init_hamster_wheel.opacity = 1
    page.update()
    time.sleep(3.0)

    #page.clean() # - Clears the screen

# - Running the app, please keep at bottom
assets_path = Path(__file__).resolve().parent.parent / "assets" # - Helps Flet find the path to the assets folder
ft.app(target=main, assets_dir=str(assets_path)) # - Runs the app