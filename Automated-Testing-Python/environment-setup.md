[Check against this](https://github.com/schoolofcode-me/testing-python-apps/tree/master/section3/video_code)

<br>

# Setting up the Enviroment

<br>

> **Same for flask and the unit Tests**

Whenever you start a new project, set up a virtual environment to go with it. They're small and reccommended.

```
$ pip install virtualenv
```

CD into directory for the project

I already ran into problems and here is the solution
> <br>
> If you installed it with
> 
> ```pip install virtualenv```
> 
> You need to run 
> 
> ```sudo /usr/bin/easy_install virtualenv```
>
> The above directory by default should be in your PATH; otherwise, edit your .zshrc (or .bashrc) accordingly.
> 
> <br>

<br>

Then try the next step.

```
virtualenv venv --python=python'Your-Version'
virtualenv venv --python=python3.9
```

This creates a folder called ```venv``` (virtual environment?). It copies Python into this folder **without** packages and libraries.

> Activating Virtual Env

MAC OS Activate the Virtual environment
```
source venv/bin/activate
(name of venv) path/names/show/here/in-terminal
```

Windows Activate the Virtual environment
```
.\venv\Scripts\activate.bat
(name of venv) path/names/show/here/in-terminal
```
> Installing Requirements

```
pip install -r example_folder/requirements.txt
```


<br>

Create a new directory called "Blog"
```
mkdir blog
```

Change the interpreter in VSCode or PyCharm to the path found for the ```venv/bin/python```. Which version, I don't know yet.

Copy this location and tell VSCode to use it as the interpreter.

```
/Users/******/Documents/GitHub/cog-training/Automated-Testing/test/venv/bin/python
```

Create new python package inside **blog** called tests.
Add new files inside test called app.py, blog.py, post.py.