# win_brenda_console (beta)

*WARNING, THIS IS MY FIRST PYTHON PROJECT AND IT MAY HAVE SERIOUS ISSUES WHICH COULD COST YOU MONEY.*

Simple console for operating James Yonan's [Brenda](https://github.com/jamesyonan/brenda) for Blender on Windows without command lines. Brenda is an open source piece of software which lets you render Blender projects with very low cost (compared to render farms) AWS Amazon computing instances.

I wrote this for myself but thought others might find it useful. It's my first Python program so i'm sure it has issues but seems to work ok for me. I've only put in the commands I use for now but may add more.
 
#HOW TO INSTALL#

Use [win_brenda_installer](https://github.com/rider-rebooted/win_brenda_installer) (an automatic Windows Brenda installation script I wrote with accompanying video tutorial) or follow Todd Mcintosh's [directions](http://brendapro.com/forum/viewtopic.php?f=0&t=76&sid=e6bc8c5335e35bab0605da5a5a6f9965) to get Brenda working on Windows, then download this zip file, extract it and double click the "win_brenda_console.py" file to run.


Tested on Windows 8.1 and Windows 10

12/12/2015 **UPDATE - option to download frames**
You can download frames automatically by selecting a download folder. You can also set it to download frames every n minutes so save a large final download.

17/12/2015 **UPDATE - option to create a new project**
You can create a new project automatically by selecting a .blend file. Win_brenda_console will delete all the files from your project and frame buckets, zip up the file, upload it and then make changes to the brenda.conf file so you can start rendering immediately.
