import aiml
import time
kernel = aiml.Kernel()
time.clock = time.time
kernel.learn("std2_startup.xml")
kernel.respond("LOAD PRAC 2")

while 1:
    input_text = input("-->Shardul-->")
    response = kernel.respond(input_text)
    print("-->Bot-->"+response)
