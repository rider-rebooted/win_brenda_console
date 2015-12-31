# win_brenda_console (beta)

*WARNING, THIS IS MY FIRST PYTHON PROJECT AND IT MAY HAVE SERIOUS ISSUES WHICH COULD COST YOU MONEY.*

31/12/2015 **UPDATE - AMIs now selectable**
List of recommended AMIs is now selectable. Also, if I've uploaded a newer version of win_brenda_console than the one you're running, a notification will pop up at the start.

30/12/2015 **UPDATE - Gives you a list of compatible AMIs when updating**
When entering a new AMI name you are now presented with a list of compatible options (scraped from a text file on my website). Also a file is modified at startup which makes win_brenda_console more compatible with newer AMIs.

28/12/2015 **UPDATE - ability to change AMI**
You can now change the AMI used by instances so that projects created with newer Blender versions can be rendered. Commands sent from cancel menu have their status checked and failure or sucess message is given.

17/12/2015 **UPDATE - option to create a new project**
You can now create a new project automatically by selecting a .blend file. Win_brenda_console will delete all the files from your project and frame buckets, zip up the file, upload it and then make changes to the brenda.conf file so you can start rendering immediately.

12/12/2015 **UPDATE - option to download frames**
You can now download frames automatically by selecting a download folder. You can also set it to download frames every n minutes so save a large final download.


Simple console for operating James Yonan's [Brenda](https://github.com/jamesyonan/brenda) for Blender on Windows without command lines. Brenda is an open source piece of software which lets you render Blender projects with very low cost (compared to render farms) AWS Amazon computing instances.

I wrote this for myself but thought others might find it useful. It's my first Python program so i'm sure it has issues but seems to work ok for me. I've only put in the commands I use for now but may add more.
 
#HOW TO INSTALL#

Use [win_brenda_installer](https://github.com/rider-rebooted/win_brenda_installer) (an automatic Windows Brenda installation script I wrote with accompanying video tutorial) or follow Todd Mcintosh's [directions](http://brendapro.com/forum/viewtopic.php?f=0&t=76&sid=e6bc8c5335e35bab0605da5a5a6f9965) to get Brenda working on Windows, then download this zip file, extract it and double click the "win_brenda_console.py" file to run.


Tested on Windows 8.1 and Windows 10


