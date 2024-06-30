#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os,sys

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

# ASCII Art with Colors
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'


os.system("clear")

def banner():
  print(f"""{BLUE}              +&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&;{END}
{GREEN}                       x&&.                           .&&&&+{END}
{YELLOW}                    x&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&x ;&+{END}
{MAGENTA}                   $&               _ _ _ _ _ _    $&  ;&+{END}
{CYAN}                      $& ___          |  __   _   \   $&  ;&+{END}
{RED}                       $& \  \        /  / |  |_>  |   $&  ;&+{END}
{WHITE}                     $&  \  \  /\  /  /  |   ___/    $&  ;&+{END}
{BLUE}                      $&   \  \/  \/  /   |  |        $&  ;&+{END}
{GREEN}                     $&    \        /    |  |        $&  ;&+{END}
{YELLOW}                    $&     \__/\__/     |__|        $&  ;&+{END}
{MAGENTA}                 .;$&&&&&&&&&$:                    $&  ;&+{END}
{CYAN}     .&&XXXXXX&&&&&$;..        :&&&.                  $$ {END}
{RED}      .&$      &$                  ;&&&$;.             .;$&&&&& {END}
{WHITE}    .&$      &$                      .+&&&&$.    .X&&&x.   +&& {END}
{BLUE}     .&$      &$                            ;&&; $$+      x&&; {END}
{GREEN}    .&$      &$             .&&&&&x.         &&        &&& {END}
{YELLOW}   .&$  ::  &$                  .;x&&&&&&&&&$.     x&&x {END}
{MAGENTA}  .&$  .   &&.....                            .$&&X {END}
{CYAN}    .&&$$$$$$&&$x+x$&&&&$$+.                ;$&&&; {END}
{RED}      .....................;x&&&&&&$+:..;x&&&&&; {END}
{WHITE}                                 $$$$$$$$$$$ {END}""")
  
  print(f"""{RED}\033[1;41;37m.:.:PengEkstrak Wordpress Sederhana:.:.\033[0m{END}""")

def menu():
    print(f"""
{BLUE}[1]{END} Pindai Semua Users       {BLUE}[2]{END} Pindai Semua Tema      {BLUE}[3]{END} Pindai Semua Plugins

{BLUE}[4]{END} WordPress Version        {BLUE}[5]{END} Download joomla + version
""")


