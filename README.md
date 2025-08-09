## This was my first project made for fun. **Do NOT** use it in production. Never hardcode API keys, use safe storage such as environment variables.

![](https://res.cloudinary.com/dtsgph9b9/image/upload/v1719337472/screenshot_nkmkoq.png)

**LightInTheDark** is a custom search engine that uses the Google Cloud JSON API and the Python Flask module to handle the search results, the web server and the URL routes.
[Live Demo](https://lightinthedark.eu.pythonanywhere.com/)

---

## Installation
*Tested on Python 3.10, 3.12*

First of all, clone the repository, you must have Git installed, once you install it
on your system, open the terminal and type:

```
git clone https://github.com/AndrewChalikias/lightinthedark.git
```

It is **highly** recommended to create a Python virtual environment in order to containerize the modules and avoid future conflicts.
To do that, `cd ~lightinthedark/` to **navigate** to the repo directory and follow the below commands.

Linux:
- `python3 -m venv venv`
- `source venv/bin/activate`
From now on, everything you install through *pip* will be **only** available on this folder.

##### Use requirements.txt

This file includes all the required modules to make the project work.
You only have to type `pip install -r "requirements.txt"` on the terminal and it will automatically install them.

##### Change the default values

Before you run it, you have to change some default values with your own. The first and most important is the **`key.conf`** file located in the project root, replace the first line with your personal [Google Cloud Custom Search API](https://console.cloud.google.com/marketplace/product/google/customsearch.googleapis.com) Key.

Next, go to the **line 9** of the **`api.py`** file and change the value of the "cx" dictionary key, replace it with your [Programmable Search Engine](https://programmablesearchengine.google.com) ID, you can find it on the overview section.

##### Run the project

Type `python3 main.py` it will start a localhost server, the default port is *5000* but you can change it by passing `port=portnumber` as a parameter inside the app.run() on the last line.
