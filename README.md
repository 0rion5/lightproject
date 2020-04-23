<!DOCTYPE html>
<html>
    <head>
      <h1>Light Project</h1>
    </head>
    <body>
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#section1">Installation</a></li>
            <li><a href="#section2">Setup</a></li>
            <li><a href="#section3">Usage</a></li>
        </ul>
        <h2 id="section1">Installation</h2>
        <p>
          <ul>
            <li>sudo apt-get update && sudo apt-get -y upgrade</li>
            <li>git clone https://github.com/0rion5/lightproject.git</li>
            <li>cd lightproject/light</li>
          </ul>
        </p>
        <h2 id="section2">Setup</h2>
        <p>
          <ul>
            <li>sudo nano /etc/rc.local</li>
            <li>add "python3 /home/pi/lightproject/light/sunrise-and-sunset.py" above exit 0</li>
          </ul>
        </p>
        <h2 id="section3">Usage</h2>
        <p>
            Some modification will be needed to get the sunrise and sunset times correct for your specific location. to do this you will             want to navigate to https://dateandtime.info/citysunrisesunset.php?id= [ Your citys id number ] and in the search bar enter your city.
        </p>
    </body>
</html>
