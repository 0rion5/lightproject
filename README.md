<!DOCTYPE html>
<html>
    <head>
      <title>Light Project</title>
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
            <li>cd lightproject</li>
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
        </p>
    </body>
</html>
