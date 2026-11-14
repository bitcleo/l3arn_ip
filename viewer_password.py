import subprocess
profiles = subprocess.check_output("netsh wlan show profiles", shell = True).decode()
names = [line.split(":")[1].strip()
         for line in profiles.split("\n") if "All User Profiles" in line]

for i, name in enumerate(names, 1):
  print(f"[i}] {name}")

ch = int(input("\nChoose WiFi number: "))
wifi = name[ch - 1]

result = subprocess.check_output()
