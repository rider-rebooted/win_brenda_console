# win_brenda_console (beta) FIXED

*WARNING, THIS IS MY FIRST PYTHON PROJECT AND IT MAY HAVE SERIOUS ISSUES WHICH COULD COST YOU MONEY.*

29/12/2018\
version : 201812291155\
**UPDATE - Fixes errors which caused it to crash immediatly upon starting**\
Now pulls information from a file in my Dropbox instead of a non-exisiting file on my old website.

16/08/2016\
version : 201608162155\
**UPDATE - Empty frame and project buckets**\
Option to empty frame and project buckets from the 'Canceling and resetting your farm' menu.

09/01/2016\
**UPDATE - Better workflow in setup menu**\
Workq build and instance initialisation now takes place in the job review menu option.

04/01/2016\
**UPDATE - Frame format now selectable**\
Frame formats such as JPEG etc. can now be selected.

03/01/2016\
**UPDATE - Sub-frame rendering now an option**\
Choose "frame settings" in the "setting up your farm" menu. Also there is a "job summary" available too. Various other improvements.

Simple console for operating James Yonan's [Brenda](https://github.com/jamesyonan/brenda) for Blender on Windows without command lines. Brenda is an open source piece of software which lets you render Blender projects with very low cost (compared to render farms) AWS Amazon computing instances.

Features

* No command lines or manually changing configuration files
* Select project in gui file browser (zips, uploads and changes config file automatically).
* Regular or one-time frame download to folder selected in gui folder browser.
* Change AMI automatically from up to date suggestions (or enter your own).
* Select frame formats or use the format specified in the uploaded .blend project file.
* Notification at start if I've uploaded a newer version of win_brenda_console than the one you are using.
* frame or sub-frame rendering with tilesize options

I wrote this for myself but thought others might find it useful. It's my first Python program so i'm sure it has issues but seems to work ok for me. I've only put in the commands I use for now but may add more.
 
#HOW TO INSTALL#

Use [win_brenda_installer](https://github.com/rider-rebooted/win_brenda_installer) (an automatic Windows Brenda installation script I wrote with accompanying video tutorial) or follow Todd Mcintosh's [directions](http://brendapro.com/forum/viewtopic.php?f=0&t=76&sid=e6bc8c5335e35bab0605da5a5a6f9965) to get Brenda working on Windows, then download this zip file, extract it and double click the "win_brenda_console.py" file to run.


Tested on Windows 8.1 and Windows 10


