#!/usr/bin/env python3

import sys
import re

def findTheIP(fileLine):
  regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'     #Regular Expression for IP address
  matched = re.search(regex, fileLine)                #searches the String fileLine for anything that matches the regular expression and stored the Match object in "matched"
  if matched != None:              #checks to see if object exists
    return matched.group(0)        #if it exists, returns a String representation
  return ""                        #if it doesn't exist, returns empty string
def main():
  
  log = sys.argv[1]                #file argument from shell
  totalIPS = 0                    #counter for total IPs found
  ips = {}                        #creates an empty dictionary
  with open(log) as file:          #opens the file for I/O
    for line in file:             #loops through each line in the file
      IP = findTheIP(line)        #Searches for IP and stores in variable called IP
      if IP != "":                #checks to see if any IP was found
        if IP in ips:              #checks to see if the IP string is already in dictionary
            ips[IP] += 1          #if it is, add one to its matching value    
        else:
          ips[IP] = 1              #if not, make a new key, value pair in the dictionary
        totalIPS += 1              #either way, add one to the total number of IPS

  print("-------------------------------------")
  print("| Percent | Count |              IP |")
  print("-------------------------------------")
  for IP in ips:                  #loop through all values in dictionary
    count = ips[IP]                #store the count of the IP in "count"
    print("|\t"+ '{:.4f}'.format(count/totalIPS*100)+ "\t|\t"+str(count)+"\t|\t"+IP+"\t|")  #calculate and print out the percentage, count and IP
if __name__ == "__main__":
  main()