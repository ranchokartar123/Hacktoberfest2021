import math
import sys

#Financial Maths
i = 0.00
def compound_interest():
  print ' '
  P = input('  The starting value: ')
  i = input('  Interest rate:      ')
  r = input('  Compounded:         1: Monthly\n                      2: Yearly\n                   => ')  
  if r in (1,2):
    n = input('  Number of years:    ')
    if i >= 1:
      i = i/100.00
    if r == 1:
      i = i/12.00
      n = n*12
      return P*(1+i)**n
    elif r == 2:
      return P*(1+i)**n
  else:
    print'\n  [E]\n  Please insert 1 or 2'
    return
  

def simple_interest():
        print ' '
        P = input('  The starting value: ')
        i = input('  Interest rate:      ')
        n = input('  Number of years:    ')
        if i >= 1:
                i = i/100.00
        return P*(1+n*i)

def future_value():
        print ' '
        x = input('  Payment per period: ')
        n = input('  Number of payments: ')
        i = input('  Interest rate:      ')
        if i >= 1:
                i = i/100.00
        return x*(((1+i)**n)-1)/i

def present_value():
        print ' '
        x = input('  Payment per period: ')
        n = input('  Number of payments: ')
        i = input('  Interest rate:      ')
        if i >= 1:
                i = i/100.00
        return x*(1-((1+i)**-n))/i

#Financial Maths Menu
def Financial_Maths_Menu():
  options =  '''
  -----------------------------------
  1: Financial Maths
  -----------------------------------
  1: Calculate amount as per compound interest
  2: Calculate amount as per simple interest
  3: Calculate future values
  4: Calculate present value
  0: Return to main menu
  -----------------------------------'''
  while True:
    print options
    try:
      command = raw_input('\n  Please select an option: ')
    except (IOError, KeyboardInterrupt):
      print '\n  [E] Going back to main menu...'
      return
    try:
      if command in '12340':
        if command == '1':
          print '\n  Result: %0.2f' %  compound_interest(),raw_input('    Continue?'),
        if command == '2':
          print '\n  Result: %0.2f' % simple_interest(),raw_input('    Continue?'),
        if command == '3':
          print '\n  Result: %0.2f' % future_value(),raw_input('    Continue?'),
        if command == '4':
          print '\n  Result: %0.2f' % present_value(),raw_input('    Continue?'),
        if command == '0':
          print '\n  [*] Returning to main menu...'
          return
      else:
        print '\n  [-] Invalid option'
    except:
      print '\n  [-] Invalid option'
