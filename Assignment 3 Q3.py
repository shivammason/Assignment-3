
string = 'X-DSPAM-Confidence: 0.8475'

colposition = string.find(':')              
number = string[colposition+1:]                
confidence = float(number)             
print(confidence)