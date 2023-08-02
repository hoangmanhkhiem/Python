import os
import json
from time import sleep
from .logo import *
from .system import *

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
violate="\033[1;37m"
nc="\033[00m"

class main:
  def install_tools(self):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.install_tools()
      print(f"\007")
      for num, tool_name in enumerate(tool.names, start=1):
        print (f" {green}[ {violate}{num} {green}] {yellow}Install {green}{tool_name}{nc}")
      print(f"")
      logo.back()
      cmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      if cmd in ["00", "back"]:
        self.menu()
        break
      else:
        try:
          if int(cmd) >= 1 and int(cmd) <= total:
            os.system("clear")
            logo.installing()
            print(f"{green}Installing ....{nc}")
            tool.install(tool.names[int(cmd)-1])
          else:
            print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
            sleep(1)
        except ValueError:
          print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
          sleep(1)

  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      os.system("clear")
      logo.tool_header()
      print(f"")
      for num, cat in enumerate(tool.category, start=1):
        print (f"  {green}[ {violate}{num} {green}] {yellow}{tool.category_data[cat]}{nc}")
      print(f"")
      logo.back()
      cmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      if cmd in ["00", "back"]:
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1, total + 1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              os.system("clear")
              logo.tool_header()
              print(f"")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" {green}[ {violate}{cnt} {green}] {yellow}Install {green}{tool.data[i]['name']}{nc}")
                  cnt+=1
              print(f"")
              logo.back()
              tcmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
              if tcmd in ["00", "back"]:
                break
              try:
                cat_total=len(tmp_cat_tool)
                if int(tcmd) in range(1, cat_total + 1):
                  os.system("clear")
                  logo.installing()
                  print(f"{green}Installing ....{nc}")
                  tool.install(tmp_cat_tool[int(tcmd)-1])
                else:
                  print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!{nc}")
                  sleep(1)
              except ValueError:
                print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!{nc}")
                sleep(1)
          else:
            print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
            sleep(1)
        except ValueError:
          print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
          sleep(1)

  def update(self):
    while True:
      os.system("clear")
      logo.update()
      cmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      if cmd=="1":
        system=sys()
        if system.connection():
          os.system("clear")
          logo.updating()
          if system.sudo is None:
            if not os.path.exists(f"{system.home}/Tool-X"):
              os.system(
                  f"git clone https://github.com/rajkumardusad/Tool-X.git {system.home}/Tool-X"
              )
            if os.path.exists(f"{system.home}/Tool-X/install.aex"):
              os.system(f"cd {system.home}/Tool-X && sh install.aex")
              if os.path.exists(f"{system.bin}/Tool-X") and os.path.exists(
                  f"{system.conf_dir}/Tool-X"):
                os.system("clear")
                logo.updated()
              else:
                os.system("clear")
                logo.update_error()
            else:
              os.system("clear")
              logo.update_error()
          else:
            if not os.path.exists(f"{system.home}/Tool-X"):
              os.system(
                  f"{system.sudo} git clone https://github.com/rajkumardusad/Tool-X.git {system.home}/Tool-X"
              )
            if os.path.exists(f"{system.home}/Tool-X/install.aex"):
              os.system(f"cd {system.home}/Tool-X && {system.sudo} sh install.aex")
              if os.path.exists(f"{system.bin}/Tool-X") and os.path.exists(
                  f"{system.conf_dir}/Tool-X"):
                os.system("clear")
                logo.updated()
              else:
                os.system("clear")
                logo.update_error()
            else:
              os.system("clear")
              logo.update_error()
          cmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        else:
          os.system("clear")
          logo.nonet()
          tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      elif cmd in ["0", "back"]:
        self.menu()
        break
      else:
        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
        sleep(1)

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.about(total)
      cmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      self.menu()
      break

  @classmethod
  def menu(cls):
    while True:
      tool=tools()
      total=len(tool.names)
      os.system("clear")
      logo.menu(total)
      cmd=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
      if cmd == "1":
        cls.install_tools(cls)
        break
      elif cmd == "2":
        cls.category(cls)
        break
      elif cmd == "3":
        cls.update(cls)
        break
      elif cmd == "4":
        cls.about(cls)
        break
      elif cmd in ["x", "X", "exit"]:
        os.system("clear")
        logo.exit()
        break
      elif cmd in ["rm -t", "rm -T", "uninstall tool-x", "unistall Tool-X"]:
        system=sys()
        if system.sudo:
          os.system(f"{system.sudo} rm -rf {system.bin}/Tool-X")
          os.system(f"{system.sudo} rm -rf {system.bin}/toolx")
          os.system(f"{system.sudo} rm -rf {system.conf_dir}/Tool-X")
        else:
          os.system(f"rm -rf {system.bin}/Tool-X")
          os.system(f"rm -rf {system.bin}/toolx")
          os.system(f"rm -rf {system.conf_dir}/Tool-X")
        os.system("clear")
        logo.exit()
        break
      else:
        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!{nc}")
        sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open(f"{system.conf_dir}/Tool-X/core/data.json") as data_file:
      self.data=json.load(data_file)
    with open(f"{system.conf_dir}/Tool-X/core/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection():
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")

      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          os.system("clear")
          logo.already_installed(name)
          tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            os.system("clear")
            logo.installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
    else:
      os.system("clear")
      logo.nonet()
      tmp=input(f"{blue}Tool-X{nc}@{blue}space {yellow}$ {nc}")
