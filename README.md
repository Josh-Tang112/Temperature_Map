
# Temperature Map
Because of global warming, I would like to make a map that can show the change in temperature when we click on it. I use the climate data in the National Centers for Environmental Information (NECI) to accomplish my goal. 
  

## Installation and How to Start Server

Use git clone or download the zip from Github to obtain the code.  
The aforemention software is a Django web app. <br>
Before you can start the server, make sure that you have Python installed, then execute installer.bat to install the dependencies. To start the server, go to temp_map folder and run
~~~
python3 manage.py runserver 0.0.0.0:{port}
~~~
where {port} will be replaced by the port number you desire. If you have no idea about port, just use 8000. <br>
After the server is running, open your browser and type 
~~~
IP:{port}/mark
~~~
in the address bar, where IP is you IP address or domain name and {port} is the number you entered above. <br>
Use Control + C to stop the server. 
WARNING: the provided Django code is not a production server. There are no guarantee for the security of the server. 
If you don't want to run the server on your local computer, you can run the Jupyter notebook 'Weather_Map.ipynb' in Google Colab by clicking the "Open in Colab" when you open the notebook in Github.  

## How to Use
After you type and hit enter in the address bar, the web server will bring to this page. <br>
![Start HTML](./images/start.png)  
You can click anywhere on the map. After you click, there will be a marker appearing on where you click. Click the marker, and it will bring up a link you can use. <br>
![Click HTML](./images/click.png)  
After you click, there are three possibilities. 
1. NECI does not have data for the area you click.
2. NECI only has part of the data
3. NECI has all of the data
<br>

**No data**
![No HTML](./images/no_temp.png)
**Partial data**
![Part HTML](./images/one_temp.png)
**Full data**
![Full HTML](./images/two_temp.png)
<br>

You can also click on another point after you finish viewing the temperature graph.
![2Click HTML](./images/see_then_click.png)
