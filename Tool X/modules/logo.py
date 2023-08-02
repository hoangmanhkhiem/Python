red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
violate="\033[1;37m"
nc="\033[00m"

class logo:
  @classmethod
  def tool_header(cls):
    print(f'''\007

{yellow}
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \    
          |_|\___/ \___/|_|   /_/\_\ {purple}v2.1


{cyan} =============================================
{yellow}|          Install Best Hacking Tool          |
{yellow}|          Copyright : K19                    |
{cyan} ============================================={nc}''')

  @classmethod
  def tool_footer(cls):
    print(f'''{cyan}_______________________________________________
==============================================={nc}''')


  @classmethod
  def not_ins(cls):
    cls.tool_header()
    print (f'''
{cyan}  [ + ]  {red}We can't install Tool-X.
{cyan}  [ + ]  {red}There are some error.
{cyan}  [ + ]  {red}Please try again after some time!''')
    cls.tool_footer()

  @classmethod
  def ins_tnc(cls):
    cls.tool_header()
    print (f'''
{yellow}  [ + ] {green}Use It At Your Own Risk.
{yellow}  [ + ] {green}No Warranty.
{yellow}  [ + ] {green}Use it legal purpose only.
{yellow}  [ + ] {green}We are not responsible for your actions.
{yellow}  [ + ] {green}Do not do things that are forbidden.

{red} If you are installing this tool.
 that means you are agree with all terms.''')
    cls.tool_footer()

  @classmethod
  def ins_sc(cls):
    cls.tool_header()
    print (f'''
{yellow}    [ + ] {green}Tool-X installed successfully.
{yellow}    [ + ] {green}To run Tool-X,
{yellow}    [ + ] {green}Type Tool-X in your terminal.''')
    cls.tool_footer()

  @classmethod
  def update(cls):
    cls.tool_header()
    print (f'''
{yellow}  [ 1 ] {green}Update your Tool-X.
{yellow}  [ 0 ] {green}For Back.{nc}''')
    cls.tool_footer()

  @classmethod
  def updated(cls):
    cls.tool_header()
    print (f'''
{yellow}      [ + ] {green}Tool-X Updated Successfully.
{yellow}      [ + ] {green}Press Enter to continue.{nc}''')
    cls.tool_footer()

  @classmethod
  def nonet(cls):
    cls.tool_header()
    print (f'''
{cyan}  [ + ]  {red}No network connection?
{cyan}  [ + ]  {red}Are you offline?
{cyan}  [ + ]  {red}Please try again after some time.{nc}''')
    cls.tool_footer()

  @classmethod
  def update_error(cls):
    cls.tool_header()
    print (f'''
{red}  [ + ]  {red}We can't Update Tool-X.\033[1;m
{red}  [ + ]  {red}Please try again after some time.{nc}''')
    cls.tool_footer()


  @classmethod
  def about(cls, total):
    cls.tool_header()
    print (f'''
{yellow}       [+] Tool Name :- {green}Tool-X
{yellow}       [+] Latest Update :- {green}23/3/2019.\033[1;m
{yellow}       [+] Tools :- {green}total {total} tools.\033[1;m

{yellow} [+] {green}Tool-x is automatic tool installer.
{yellow} [+] {green}Made for termux and linux based system.
{red} [+] Note :- Use this tool at your own risk.''')
    cls.tool_footer()


  @classmethod
  def install_tools(cls):
    print (f"""{yellow} =============================================
{green}|_____________ Select your tool ______________|
 {yellow}============================================={nc}""")

  @classmethod
  def already_installed(cls, name):
    cls.tool_header()
    print(f'''
{yellow}  [ + ] {green}Sorry ??
{yellow}  [ + ] {violate}'{name}'{green} is already Installed !!
''')
    cls.tool_footer()

  @classmethod
  def installed(cls, name):
    cls.tool_header()
    print(f'''
{yellow}  [ + ] {green}Installed Successfully !!
{yellow}  [ + ] {violate}'{name}'{green} is Installed Successfully !!
''')
    cls.tool_footer()

  @classmethod
  def not_installed(cls, name):
    cls.tool_header()
    print(f'''
{yellow}  [ + ] {red}Sorry ??
{yellow}  [ + ] {violate}'{name}'{red} is not installed !!
''')
    cls.tool_footer()

  @classmethod
  def back(cls):
    print (f"""\033[01;36m =============================================
{yellow}|  00) Back                                   |
 \033[01;36m============================================={nc}""")

  @classmethod
  def updating(cls):
    print (f"""{yellow} =============================================
{green}|______________ Updating Tool-X ______________|
 {yellow}============================================={nc}""")

  @classmethod
  def installing(cls):
    print (f"""{yellow} =============================================
{green}|________________ Installing _________________|
 {yellow}============================================={nc}""")

  @classmethod
  def menu(cls, total):
    cls.tool_header()
    print (f'''
{yellow}  [ 1 ] {green}Show all tools.{yellow} [ {purple}{total} tools{yellow} ]
{yellow}  [ 2 ] {green}Tools Category.
{yellow}  [ 3 ] {green}Update Tool-X.
{yellow}  [ 4 ] {green}About Us.
{yellow}  [ x ] {green}For Exit.''')
    cls.tool_footer()

  @classmethod
  def exit(cls):
    cls.tool_header()
    print (f'''
{yellow}         [ + ] {green}Thanks for using Tool-X
{yellow}         [ + ] {green}Good Bye.....! ){nc}''')
    cls.tool_footer()
