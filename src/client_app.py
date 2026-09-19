# =============================================
#         'Doyle' Client App 
# =============================================
import flet as ft
import time as time

# - Startup Screen Flash
def startup():
    # - Settings for Doyle's Head
    mascot = ft.Container(
            shape = ft.BoxShape.CIRCLE,
            shadow = ft.BoxShadow(offset=ft.Offset(0,0), blur_radius = 20, spread_radius = 2, color = ft.Colors.CYAN), # -  The Glow!
            content = ft.Icon(icon=ft.Icons.PERSON, size= 80, color = ft.Colors.CYAN)
            )

    # - Title Settings
    name  = ft.Text(value = "Doyle", size = 35, italic = True)

    # - Compiled
    cover = ft.Column(controls = [mascot, name], horizontal_alignment = ft.CrossAxisAlignment.CENTER, spacing = 15)
    return cover

# - Main App Operation 
def main(page: ft.Page):

    # - Universal Configs
    page.title = "Doyle"
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
    page.add(startup()) # - Bringing in the Startup screen
    time.sleep(5) 
    #page.clean() # - Clears the screen

ft.app(target = main) # Runs the app KEEP AT BOTTOM