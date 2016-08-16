
class MyApp(object):                                                         

    def __init__(self, stdscreen):                                           
        self.screen = stdscreen                                              
        curses.curs_set(0)                                                   

        submenu_items = [                                                    
                ('turd', curses.beep),                                       
                ('crap', curses.flash)                                      
                ]                                                            
        submenu = Menu(submenu_items, self.screen)                           

        main_menu_items = [                                                  
                ('beep', curses.beep),                                       
                ('flash', curses.flash),                                     
                ('submenu', submenu.display)                                 
                ]                                                            
        main_menu = Menu(main_menu_items, self.screen)                       
        main_menu.display()                                                  

