# ZeroCut
An unconventional Tic-Tac-Toe game making it way more interesting and fun.

The game is developed using [libGDX](https://libgdx.badlogicgames.com/download.html) and python. libGDX is used for desktop (Windows /Linux /Mac) , Android and HTML. Currently iOS versions have not been implemented.


###Python Implementation
The game was first implemented using pygame library for python. The python implementation supports only desktops with pygame library installed. The python folder in root directory contains the python code for the game.The [v1.0](https://goo.gl94I1v7) of the game is available for download and was packaged as .exe using PyInstaller for Windows PC. Further development in python will not be done as porting to other platforms will be difficult


###Android
The code is under development. Android app can be built by selecting the android configuration in android studio (default configuration)


###Desktop(Win/Linux/Mac)
The code is under development. Desktop app can be built by creating a new configuration in android studio. Add new configuration as Application and give 
Main class : com.slateandpencil.zerocut.desktop.DesktopLauncher 
Change working directory to android/assets folder
Use classpath of module : desktop

Run using the new configuration to create desktop app.

To deploy to desktop, type 'gradlew desktop:dist' in the terminal opened in root directory of project. The `.jar` will be stored in `desktop/build/libs/`


###HTML
To compile the project as web app [GWT](http://www.gwtproject.org/download.html) is required. gwt 2.8.0 is used in this project. Download the zip and extract it. Copy the extracted folder to html/ and then you can compile your webapp.

To deploy type `gradlew html:dist` in the terminal opened in root directory of the project. The dist folder can be hosted in Apache, NGINX servers. Opening the `index.html` with browser lets you play the game inside the browser.
