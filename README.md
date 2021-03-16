# gnv - _1.0.7_
_**An automation tool that is based on Command Line and Selenium that controls Github repos, themes and data from the developers terminal**_

> _**gnv** uses **'click'** and **'selenium'** modules/packages of python to give the users a feel of both the command line interface and automation at the same time_

**gnv is strictly for lazy developers like me, who wish to get everthing from there console itself**

## Features

 - Controls Github from CLI
 - Doesn't collect any data of the users
 - Fast
 - Open Source
 - Automated look[The best part]
 - Can be used Globally on the developers work-machine
 - gnv signs-out the account after the process has completed to enable developers use git commands and improve security

## ChangeLog:

 - *v1.0.7:* _Minor Bug Fix._ 

 - *v1.0.6:* _Bug Fix._

 - *v1.0.5:* _Big Release. Added Functionallity to create git in any repquired destination path, Improved colors for the terminal, more accuracy in deleting repositories, bug fixes_

 - *v1.0.4:* _Major Release, capability to set Github theme, list repos of the given account._
    
    _Note_: **Please Provide Your Username and account for all the commands as gnv needs it for getting the right data of the right user**

 - *v1.0.3:* _improved speed in creating and deleting Repos, with enabled auto element detection for slow internet and direct URL launching feature to improve the time efficiency_

 - *v1.0.2:* _Bug Fix. Improved Time Efficiency. Password hidden feature in the terminal or console._

 - *v1.0.1:* _Username and Password through the command line instead of the code itself_

 - *v1.0:* _The initial Stable version_

# Prerequisites:

 - Google Chrome Browser
 - Chrome Driver and its path set
 - GitHub Account
 - Python with pip
 - Preferable Python version should be 3
 - And finally a Text-Editor, IDE or a general terminal for running the command
 
_Note:_ ***Please make sure to disable 2FA(2 Factor Authentication) on your GitHub account as gnv uses 'selenium' and the latter needs to get proper elements of the browser at the right time, else the program stops executing. Maybe in the next version of 'gnv' I will make it work even with 2FA enabled. Kindly Oblige***

## Setup:

_There are 2 ways for the setup or installation of **gnv**_:

 1. _Run `pip install gnv` or `pip3 install gnv`_ This will install gnv onto your work machine. 
 2. _**Clone `gnv` repo if you want to use someother browser apart from Chrome.** But make sure to add your browser's driver to your system's path and change the name of the browser in the code above. Once done open the root folder and run `pip install .` or `pip3 install .`_	 
 
 **That's it! Now you can use gnv globally on any terminal of your system**
	 

## Usage
_After installing gnv using any of the above 2 methods run the following commands:_

**To create a GitHub Repo:**
`gnv git create <repo-name>`

**To delete a GitHub Repo**
`gnv git delete <repo-name>`

**To set Theme for GitHub account**
`gnv git theme <light/dark/default>`

**To list your GitHub accounts repositories**
`gnv git list`

**To run commands of git all the git commands**
`gnv git ga`


_After running these command you will be asked to give your github Username and password and some others to know what are your needs. **No worries! No data is taken** It is just for the security purpose_

## Uninstalling

_Hope you don't uninstall **'gnv'**. But if you want so then run_
`pip uninstall gnv` or `pip3 uninstall gnv`

## Any Extras to be installed?

_Nothing else is required to run gnv. Selenium and Click modules with their dependencies are installed during the installation of gnv. Only set your webdrivers path correctly_

### License ![GitHub](https://img.shields.io/github/license/mashape/apistatus)
Copyright 2020 GN Vageesh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "gnv"), to deal in the Software without restriction, including without
limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE F
OR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
