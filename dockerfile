FROM python:3.10-slim

# Install Tkinter & system tools
RUN apt-get update && apt-get install -y python3-tk x11-apps && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Run the Tkinter app
CMD ["python", "app.py"]
