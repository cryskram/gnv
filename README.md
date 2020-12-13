# gnv - _1.0.0_
_**An automation tool that is based on Command Line and Selenium that creates or deletes Github repos from the developers terminal**_

> _**gnv** uses **'click'** and **'selenium'** modules/packages of python to give the users a feel of both the command line interface and automation at the same time_

**gnv is strictly for lazy developers like me, who wish to get everthing from there console itself**

## Features

 - Creates or Deletes yourGitHub repos
 - Doesn't collect any data of the users
 - Fast
 - Open Source
 - Automated look[The best part]
 - Can be used Globally
 - Once done with the creation or deletion of the repo, gnv signs-out with the account making it much secure and finally closes the browser to let you run other git commands to commit and push files to your repo

# Prerequisites:

 - Google Chrome Browser
 - Chrome Driver and its path set
 - GitHub Account
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
`gnv github create <repo-name>`

**To delete a GitHub Repo**
`gnv github delete <repo-name>`


_After running these command you will be asked to give your github Username or email and password and some others to enhance your repo. **No worries! No data is taken** It is just for the login and logout purpose_

## Uninstalling

_Hope you don;t uninstall **'gnv'**. But if you want so then run_
`pip uninstall gnv` or `pip3 uninstall gnv`

## Any Extras to be installed?

_Nothing else is required to run gnv. Selenium and Click modules with their dependencies are installed during the installation of gnv_

### License
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