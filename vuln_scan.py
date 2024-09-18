# Automate vulnerability scanning using Nmap
import os

# Run Nmap scan and save results to a file
os.system('nmap -A -T4 192.168.1.0/24 -oN scan_results.txt')