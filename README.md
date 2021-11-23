# Welcome!

Open up two terminals, one for client and for server each
Terminal 1
Terminal 2

Now navigate to the CW2_code directory in both like so
$ cd CW2_code

add to both terminals
$ module add python/3.4.3
$ source flask/bin/activate
This is to ensure the correct version of python is present and the environment is activated

In terminal 1 navigate to the Server_api directory and execute the Web Service like so
$ python Warm_EU_api.py

Open up http://127.0.0.1:5050/ which will be the server displaying the resources
Keep this terminal running throughout this application!


Now we can start the client!
In terminal 2 navigate to the ClientApp directory and execute the client like so
$ python Client.py

Open up http://127.0.0.1:5001/

The client interface is up and running! Enjoy!
