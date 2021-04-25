KV = '''
ScreenManager:
    MyApp:
    #-------------#
    CreateItinerary:
    ShowItinerary:
    About:


<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "180dp"
    

<MyApp>
    name: "gomain"
    Screen:
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    title: "Itinerary Bike Capture App"
    
                MDLabel:
                    text: "" 
    
                MDLabel:
                    text: "Welcome User!"
                    font_size: 17
                    halign: "center"
                    pos_hint: {'center_y': 0.2}
                    theme_text_color: "Secondary" 
    
                MDGridLayout:
                    cols: 2
                    adaptive_height: True
                    padding: dp(15), dp(15)
                    spacing: dp(10)
    
                    MyTile:
                        source: "Gallery.jpg"
                        text: "[size=15]Show Created Itinerary[/size]"
                        on_press: root.manager.current = "show"
                        
           
                    MyTile:
                        source: "Pin.jpg"
                        text: "[size=15]Create An Itinerary[/size]"
                        on_press: root.manager.current = "iti"
           
                MDLabel:
                    text: "" 
                    halign: "center"
                    pos_hint: {'center_y': 0.6}
                    theme_text_color: "Secondary" 
    
                MDFloatingActionButton:
                    id: button
                    icon: "plus"
                    on_press: root.manager.current = "iti"
                    
                MDBottomNavigation:
                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'Home'
                        icon: 'home'
                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'About'
                        icon: 'account-circle'
                        on_tab_release: root.manager.current = "abt"
     
<CreateItinerary>
    name: "iti"
    Screen:
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    title: "Create Itinerary"
    
                MDGridLayout:
                    cols: 1
                    adaptive_height: True
                    padding: dp(35), dp(35)
                    spacing: dp(30)
        
                    MyTile:
                        source: "Travel.jpg"
                            
                MDTextField:
                    id: place
                    hint_text: "Enter Your Destination"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    helper_text: "Place of your Destination"
                    helper_text_mode: "on_focus"
                    size_hint_x: None
                    width: 300
                    
                MDLabel:
                    id: name
                    text: ""
                    
                MDRectangleFlatButton:
                    text: "Add"
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                    on_release: app.add(place.text) 
        
                     
                MDBottomNavigation:
                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'Home'
                        icon: 'home'
                        on_tab_release: root.manager.current = "gomain"
                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'About'
                        icon: 'account-circle'
                        on_tab_release: root.manager.current = "abt"
<ShowItinerary>
    name: "show"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Show Itinerary"
                    
        MDList:
            id: go
            
             
        MDBottomNavigation:
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Home'
                icon: 'home'
                on_tab_release: root.manager.current = "gomain"
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'About'
                icon: 'account-circle'
                on_tab_release: root.manager.current = "abt"
                
    MDRectangleFlatButton:
        text: "Refresh"
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_release: root.show()
    MDLabel:
        text: "*Click refresh to show the inserted itinerary*"
        theme_text_color: "Secondary" 
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.20}
    MDLabel:
        text: "*Click Place to show/view the pictures"
        theme_text_color: "Secondary" 
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.15}

<About>
    name: "abt"   
    Screen:
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    title: "Itinerary Bike Capture App"
                
                MDLabel:
                    text: "ABOUT"
                    theme_text_color: "Secondary"
                    font_style: 'H4'
                    halign: "center"
                MDLabel:
                    text: "Welcome User Here you can now set your own Itinerary plans for your bike Journey " 
                    halign: "center"
                    theme_text_color: "Secondary"
                    font_style: 'H6'
                MDBottomNavigation:
    
                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'Home'
                        icon: 'home'
                        on_tab_release: root.manager.current = "gomain"
                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'About'
                        icon: 'account-circle'
                  
                        
     
'''