# Astroy

[<img src="https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7-red.svg">]()
[<img src="https://img.shields.io/badge/Requirements-Up%20To%20Date-green.svg">]()
[<img src="https://img.shields.io/badge/Apache-v2.4.38-lightgrey.svg">]()
[<img src="https://img.shields.io/badge/PHP-v7.3.2-orange.svg">]()
[<img src="https://img.shields.io/badge/License-MIT-blue.svg">]()
[<img src="https://img.shields.io/badge/OS-Kali%20Linux-brightgreen.svg">]()
[<img src="https://img.shields.io/badge/OpenSSH-v7.9-red.svg">]()

> Astroy is a collection of templates that have been outsourced from different projects, combined to launch a powerful, attractive and easy to pull off phishing campaign.

[![asciicast](https://asciinema.org/a/fz787azSdbP34fi9iE7dpf0hd.svg)](https://asciinema.org/a/fz787azSdbP34fi9iE7dpf0hd)

I made this as a tool for personal use, and did not think I would come to open-source it. As a result, a LOT of assumptions have been made when coding this, and it's gonna take you a bit of tweaking and playing around with if the OS you're running isn't configured in accordance to how the script wants. Shouldn't be too hard, though.

## Assumptions

Because I coded this for personal use, I made this without consideration for other Linux OS'. As such, this tool is made with the assumption that:

1. You're system has Python 3. To set up most of the things that the tool needs, you'll need to run the main python file (``setup.py``) with Python 3. Also, the ``index.php`` files in the directories ``download`` and ``account/instagram`` make calls to Python 3 to run ``retrieve.py`` and ``del.py`` respectively. Depending on how you invoke your Python 3 (for example, I run files like this - ``python3 example.py`` - because my system has two Python versions installed), you might need to alter the default invocation in the ``index.php`` files specified above. Lastly, every Python file in Astroy has a shebang that invokes the Python 3 version installed on my system - this assumes that your Python 3 is located at ``/usr/bin/python3``. Change this line as necessary.

2. Your system has ``Apache2`` and that the default directory for serving web pages is ``/var/www/html``. It also assumes that you have correctly set up ``PHP`` with Apache so that any PHP files are correctly rendered by Apache when its webserver is started. The default Apache webserver listens on port `80`, and this tool abides by that.

3. Your system has ``PHP``. I recommend version ``7``, because I haven't tested this tool with other versions of PHP. 

4. Your system has ``OpenSSH`` and ``AutoSSH``. These are used to establish connections to [``Serveo``](http://serveo.net), which forwards ports and allows your locally served web pages to be available to the public.

5.
