# openai_token

On Linux (X11):

xhost +  # Allow X11 from Docker
docker build -t chatgpt-tkinter .
docker run -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    chatgpt-tkinter


On macOS/Windows (with Docker Desktop), you’ll need an X server (like XQuartz for macOS or VcXsrv for Windows). Then:

Start the X server on your machine.

Allow connections.

Replace -e DISPLAY=$DISPLAY with something like:

-e DISPLAY=host.docker.internal:0

5. Security Note

You probably don’t want to hardcode the API key inside app.py. Instead, pass it as an environment variable:

Edit app.py:
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

Run container with your API key:
docker run -it \
    -e DISPLAY=$DISPLAY \
    -e OPENAI_API_KEY=sk-xxxxxxx \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    chatgpt-tkinter


Now you’ll have a Tkinter ChatGPT desktop GUI running from inside Docker, displaying on your host screen.

