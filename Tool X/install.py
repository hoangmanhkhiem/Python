import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

yellow="\033[1;33m"
blue="\033[1;34m"
nc="\033[00m"

class tool:
  @classmethod
  def install(cls):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input(f"{yellow}Do you want to install Tool-X [Y/n]> {nc}")
      if inp in ["y", "Y"]:
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if not os.path.exists(f"{system.conf_dir}/Tool-X"):
            os.system(f"{system.sudo} mkdir {system.conf_dir}/Tool-X")
          os.system(
              f"{system.sudo} cp -r modules core Tool-X.py {system.conf_dir}/Tool-X"
          )
          os.system(f"{system.sudo} cp -r core/Tool-X {system.bin}")
          os.system(f"{system.sudo} cp -r core/toolx {system.bin}")
          os.system(f"{system.sudo} chmod +x {system.bin}/Tool-X")
          os.system(f"{system.sudo} chmod +x {system.bin}/toolx")
          os.system(f"cd .. && {system.sudo} rm -rf Tool-X")
        else:
          if not os.path.exists(f"{system.conf_dir}/Tool-X"):
            os.system(f"mkdir {system.conf_dir}/Tool-X")
          os.system(f"cp -r modules core Tool-X.py {system.conf_dir}/Tool-X")
          os.system(f"cp -r core/Tool-X {system.bin}")
          os.system(f"cp -r core/toolx {system.bin}")
          os.system(f"chmod +x {system.bin}/Tool-X")
          os.system(f"chmod +x {system.bin}/toolx")
          os.system("cd .. && rm -rf Tool-X")
        if os.path.exists(f"{system.bin}/Tool-X") and os.path.exists(
            f"{system.conf_dir}/Tool-X"):
          os.system("clear")
          logo.ins_sc()
        else:
          os.system("clear")
          logo.not_ins()
        tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
