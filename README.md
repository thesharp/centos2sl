# centos2sl: Convert your CentOS installation to Scientific Linux using fabric

## Overview
This is a [fabfile](http://docs.fabfile.org/en/1.4.3/index.html) for people who prefer to work with Scientific Linux distribution, but their hosting/cloud provider can only provision CentOS boxes (e.g. [Linode](http://linode.com)).

## What it does exactly
First of all, it will set up a correct time zone for you and sync the time with the ntp server. Next it will perform the steps gathered from [here](http://nixgeek.com/convert-centos-6-server-to-scientific-linux-6.html). It is recommended to do this procedure on clean box only. The conversion of already-in-production boxes wasn't tested.

## How much time does it take
I've created a test t1.micro AWS instance using one of the minimal CentOS 6.2 AMIs (ami-1fa4a16b in the european region) and ran this fabfile against it. For a CentOS 6.2 to Scientific Linux 6.3 conversion it took almost 22 minutes.

## How to use
First of all you have to install fabric. Here's the easiest way to install it:

	$ pip install fabric

Then you should set the desired timezone in the fabfile. Replace the "Europe/Moscow" with what you want. Right after that you can fire up this script, replacing USER with your AWS ssh user and HOST with your AWS host:

	$ fab -H HOST --set user=USER main

Your user should have a passwordless sudo permissions or you will need to add ``--set password=PASSWORD`` to your command line.

It's recommended to reboot your host after a successful conversion.

## Bugs
Right now the fabfile has two hardcoded URLs for ``yum-conf`` and ``sl-release`` packages. So if those will change, the fabfile will require an alteration of those variables.