==========
naturalcropping
==========
:Info:Natural cropping backend for sorl-thumbnail
:Version: 0.0.1
:Author: Alexey Boriskin (http://github.com/uruz)

Features
========

Installation
============
* Install from github: 
	pip install -e git://github.com/uruz/naturalcropping.git#egg=naturalcropping
	
* Then put the following line in your `settings.py`:
    THUMBNAIL_ENGINE = 'naturalcropping.Engine'	

* Then use sorl-thumbnail as usual with crop="natural" setting. Example: 
    {% thumbnail picture.image "100x100" crop="natural" as img %}
    	<img src="{{img.url}}" alt="image" />
    {% endthumbnail %}
    
Notes
=====
* `upscale` options is overriden and is always True
* if image is more horizontal then needed algorithm crops out left and right margins
* if image is more vertical then needed algorithm crops top part because we usually don't want to crop out heads