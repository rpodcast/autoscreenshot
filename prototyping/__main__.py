def main():
    """Run the autoscreenshot tool"""
    # Standard library imports
    import os
    import platform
    import pwd
    import sys
    import time
    import logging
    from datetime import timedelta, datetime

    # autoscreenshot imports
    from mss import mss
    import mss.tools
    from autoscreenshot import getscreenshot, screenshotloop
    from timeloop import Timeloop

    # utility functions
    def get_username():
        return pwd.getpwuid( os.getuid() )[ 0 ]

    def py_minor():
        return sys.version_info[1]


    def platform_is_osx():
        return sys.platform == "darwin"


    def platform_is_win():
        return sys.platform == "win32"


    def platform_is_linux():
        return sys.platform.startswith("linux")

    def use_x_display():
        if platform_is_win():
            return False
        if platform_is_osx():
            return False
        DISPLAY = os.environ.get("DISPLAY")
        XDG_SESSION_TYPE = os.environ.get("XDG_SESSION_TYPE")
        # Xwayland can not be used for screenshot
        return DISPLAY and XDG_SESSION_TYPE != "wayland"

    def using_multiple_displays():
        with mss.mss() as mss_instance:
            #print(mss_instance.monitors)
            return len(mss_instance.monitors) > 2

    # check if running under linux
    if platform_is_linux():
        # if in a tty session (i.e. not in an actual graphical desktop), exit script
        if os.environ.get("XDG_SESSION_TYPE") == "tty":
            print("screenshots cannot be taken in a terminal (tty) session!  Please run inside a graphical session")
            sys.exit()
        else:
            if use_x_display():
                print("Running under X11: Proceeding as normal")
            else:
                print("Sorry, running under Wayland needs more work")
                sys.exit()

    args = create_parser().parse_args()

    # check if an output directory was specified
    if not os.path.isdir(args.output_dir):
        image_dir=os.getcwd()
    else:
        image_dir=os.path.normpath(args.output_dir)

    # take one screenshot per monitor for dry run if requested
    if args.dryrun:
        print("Creating one screenshot for each monitor detected")
        with mss.mss() as mss_instance:
            # get all monitors
            mon_range = range(1, len(mss_instance.monitors)-1)
            for monitor_id in mon_range:
                getscreenshot(mss_instance, image_type = "jpg", image_dir=image_dir, monitor_id=monitor_id)

        sys.exit()
    else:
        monitor_id = args.monitor
        quality = args.quality
        lowres_interval = args.lowinterval
        highres_interval = args.highinterval
        print("Creating automatic screenshots. To stop process, terminate the command with ctrl+c")
        screenshotloop(image_dir=image_dir, monitor_id=monitor_id, highres_interval=highres_interval, lowres_interval=lowres_interval, quality=quality)

    