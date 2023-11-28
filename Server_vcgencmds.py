## TPRG 2131 Fall 2023 Asmt 2
## Course code Fall 2023
## Jack Dunford <jack.dunford@dcmail.ca>
## Used Chat GPT for making edits to the modified code.




import socket
import os, time
import json

s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)

# Get Core Temperature
temp_output = os.popen('vcgencmd measure_temp').readline()
temperature = temp_output.strip().split('=')[1].split("'")[0]

# Get Clock Frequencies
clock_output = os.popen('vcgencmd measure_clock arm').readline()
clock_frequency = clock_output.strip().split('=')[1]

# Get Memory Information
mem_output = os.popen('vcgencmd get_mem arm').readline()
memory_info = mem_output.strip().split('=')[1]

# Get Display Power State
display_output = os.popen('vcgencmd display_power').readline()
display_state = display_output.strip().split('=')[1]

# Get Codec Licensing Information
codec_output = os.popen('vcgencmd codec_enabled H264').readline()
codec_state = codec_output.strip().split('=')[1]

# Create a dictionary with the collected information
result_dict = {
    "Temperature": temperature,
    "Clock Frequency": clock_frequency,
    "Memory Info": memory_info,
    "Display Power State": display_state,
    "Codec Licensing": codec_state
}

# Convert dictionary to JSON string
result_json = json.dumps(result_dict, indent=2)

# Print or use the result_json as needed
print(result_json)

while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  res = bytes(str(result_dict), 'utf-8') # needs to be a byte. Sending temperature
  c.send(res) # sends data as a byte type
  c.close()
