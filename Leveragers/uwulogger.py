import logging
from datetime import datetime
from colorama import init, Fore, Style

LBL = "\x1b[38;5;27m"
sep = f"{Fore.LIGHTBLACK_EX} ● {Fore.LIGHTWHITE_EX}"

class Leveragers:
    def __init__(self):
        self.logger = logging.getLogger('custom_logger')
        self.logger.setLevel(logging.DEBUG)
        
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)

    def log(self, level, msg):
        time = f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}"
        
        color = {
            'DBG': Fore.LIGHTCYAN_EX,
            'ERR': Fore.LIGHTRED_EX,
            'RATELIMT': Fore.LIGHTYELLOW_EX,
            'INP': Fore.LIGHTRED_EX,  
            'INF': LBL    
        }.get(level.upper(), Fore.WHITE)
        
        tag = f"{color}{level.upper()}{Style.RESET_ALL}"
        
        method = {
            'DBG': self.logger.debug,
            'ERR': self.logger.error,
            'RATELIMT': self.logger.warning,
            'INP': self.logger.info,
            'INF': self.logger.info
        }.get(level.upper(), self.logger.info)

        method(f"{time} - {tag}{sep}{msg}")

    def dbg(self, msg):
        self.log('DBG', msg)

    def err(self, msg):
        self.log('ERR', msg)

    def ratelimt(self, msg):
        self.log('RATELIMT', msg)

    def inp(self, prompt):
        time = f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}"
        prompt_msg = f"{time} - {Fore.LIGHTRED_EX}INP{Style.RESET_ALL}{sep}{prompt}"
        
        userinput = input(prompt_msg + " ")
        
        try:
            return int(userinput)
        except ValueError:
            return userinput
  

    def inf(self, msg):
        self.log('INF', msg)
