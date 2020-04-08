# 이 파일에는 저작권이 없습니다. 
# 원하는 스크린을 만들 수 있도록 마음껏 수정하세요.

##############################################################################
# 스플레쉬 화면 (로고)
#
# 게임이 시작 되기 전에 뜨는 화면
# http://www.renpy.org/wiki/renpy/doc/cookbook/Adding_a_Splashscreen
image splash = "system/logo_teamstep.png"
#image splash2 = "system/logo_warning.png"
image splash2 = "system/logo_warning.png"
image cia_chibi = "sprite/cia_chibi.png"


label splashscreen:
    scene black 
    with Pause(0.5)
    
    scene white
    play sound "se/logo_teamstep.mp3"
    show splash with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.5
    with Pause(0.6)
    
    scene white with dissolve
    with Pause(0.4)
    
    show splash2
    show cia_chibi with dissolve:
        zoom 0.8 xalign 0.8 yalign 1.2
        xanchor 0.5 yanchor 1.0
        rotate 20
        linear 1.0 rotate -20
        linear 1.0 rotate 20
        repeat
    with Pause(3.0)
    
    scene black with movedown
    with Pause(0.4)

    return

##############################################################################
# 대사 화면
#
# ADV모드 대사를 표시할 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say:

    # side_image 와 two_window 의 기본값
    default side_image = None
    default two_window = False

    # 창을 1개 사용할지, 2개 사용할지 결정합니다.
    if not two_window:

        # 창을 1개 쓰는 대사창
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # 이름과 대사, 창을 2개 쓰는 대사창
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # 사이드 이미지가 있다면 텍스트 위에 표시한다.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# 선택지 화면
#
# 게임 내 선택지를 표시할 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 10

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# 텍스트 입력 화면
#
# renpy.input을 나타낼 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# 비주얼노벨 대사 화면
#
# NVL모드의 대사와 선택지를 나타낼 때 사용하는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # 대사를 표시한다.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # 선택지가 있다면 선택지를 나타낸다.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# 메인 메뉴 화면
#
# 렌파이 게임이 처음 시작되었을 때 나타나는 메인 메뉴를 표시하는 스크린
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        
    imagemap:
        ground "system/main_menu_idle.png"
        hover "system/main_menu_hover.png"
        
        # hotspot (x,y,xsize,ysize) action action("action_name")
        hotspot (1000,80,280,120) action Start()
        hotspot (1000,240,280,120) action ShowMenu("load")
        hotspot (1000,400,280,120) action ShowMenu("preferences")
        hotspot (1000,560,280,120) action Quit(confirm=False)
        hotspot (0,40,240,120) action ShowMenu("help_menu")
        hotspot (0,586,246,134) action Start(label='fx_test')

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"

##############################################################################
# 도움말 화면
#
screen help_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        
    imagemap:
        ground "system/help_idle.png"
        hover "system/help_hover.png"
        
        # hotspot (x,y,xsize,ysize) action action("action_name")
        hotspot (0,580,240,100) action ShowMenu("main_menu")
        textbutton _("제작자 블로그") action OpenURL("http://bit.ly/1GiqQrY")

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"

##############################################################################
# 네비게이션 화면
#
# 게임 메뉴 네비게이션 버튼과 배경 화면을 표시하는 스크린이 포함된 스크린.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    imagemap:
        # auto "system/navigation_%s.png"
        ground "system/navigation_ground.png"
        idle "system/navigation_idle.png"
        hover "system/navigation_hover.png"
        selected_idle "system/navigation_hover.png"
        selected_hover "system/navigation_hover.png"
        
        #hotspot (980,120,220,110) action Return()
        #hotspot (980,300,220,110) action ShowMenu("save")
        #hotspot (980,480,220,110) action ShowMenu("load")
        #hotspot (720,210,220,110) action ShowMenu("preferences")
        #hotspot (720,380,220,110) action MainMenu()
        #hotspot (720,550,220,110) action Quit()
        
        hotspot (1000,0,280,100) action Return()
        hotspot (1000,120,280,100) action ShowMenu("preferences")
        hotspot (1000,240,280,100) action ShowMenu("save")
        hotspot (1000,360,280,100) action ShowMenu("load")
        hotspot (1000,480,280,100) action MainMenu()
        hotspot (1000,600,280,100) action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"

##############################################################################
# 저장하기, 불러오기 화면
#
# 게임을 저장하거나 불러올 수 있는 화면.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# 저장하기와 불러오기는 기능이 비슷하기 때문에, file_picker라는 스크린 하나에 통합했습니다.
# 그리고 file_picker 스크린을 load 및 save 스크린에 간단히 추가했습니다.

screen file_picker:
    imagemap:
        ground "system/loadsave_ground.png"
        idle "system/loadsave_idle.png"
        hover "system/loadsave_hover.png"
        selected_idle "system/loadsave_hover.png"
        
        hotspot (40, 40, 80, 80) clicked FilePage("quick") # 큇세이브 슬롯
        hotspot (140, 40, 80, 80) clicked FilePage(1) # 슬롯1
        hotspot (240, 40, 80, 80) clicked FilePage(2) # 슬롯2
        hotspot (340, 40, 80, 80) clicked FilePage(3) # 슬롯3
        hotspot (440, 40, 80, 80) clicked FilePage(4) # 슬롯4
        hotspot (540, 40, 80, 80) clicked FilePage(5) # 슬롯5
        hotspot (642, 50, 132, 64) clicked FilePage("auto") # 큇세이브 슬롯
        
        hotspot (1000,0,280,100) action Return()
        hotspot (1000,120,280,100) action ShowMenu("preferences")
        hotspot (1000,240,280,100) action ShowMenu("save")
        hotspot (1000,360,280,100) action ShowMenu("load")
        hotspot (1000,480,280,100) action MainMenu()
        hotspot (1000,600,280,100) action Quit()
        
        hotspot (40, 160, 580, 160) clicked FileAction(1):
            use load_save_slot(number=1)
        hotspot (40, 340, 580, 160) clicked FileAction(2):
            use load_save_slot(number=2)
        hotspot (40, 520, 580, 160) clicked FileAction(3):
            use load_save_slot(number=3)

screen save:
    # This ensures that any other menu screen is replaced.
    tag menu
    use file_picker

screen load:
    # This ensures that any other menu screen is replaced.
    tag menu
    use file_picker

screen load_save_slot:
    $ file_text = "%2s. %s\n  %s" % (
                        FileSlotName(number, 3),
                        FileTime(number, empty=_("Empty Slot.")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 30 ypos 30
    text file_text xpos 260 ypos 50 size 32 color "#000000" outlines [ (2, "#ffffffff") ]
    
init -2 python:
    config.thumbnail_width = 200
    config.thumbnail_height = 120
    
##############################################################################
# 환경설정 화면
#
# 환경설정을 변경할 수 있는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # 네비게이션 스크린을 포함한다.
    use navigation

    # 환경설정 메뉴들을 1x4 행렬로 배치한다.
    grid 1 1:
        style_group "prefs"
        xfill True

        # 첫 번째 열
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")
                
        # 두 번째 열
        #vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                textbutton _("모든 구간 스킵") action Preference("skip", "toggle") style "soundtest_button"
                #textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
                    
        # 세 번째 열
        #vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")
                
        # 네 번째 열
        #vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"


init -2 python:
    style.pref_frame.xfill = False
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = False

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 0.5
    
    style.soundtest_button.xalign = 0.5
    
    style.pref_button.background = Frame("system/button_idle.png",10,10)
    style.pref_button.hover_background = Frame("system/button_hover.png",10,10)
    style.pref_button.selected_background = Frame("system/button_selected.png",10,10)
    style.pref_button.selected_hover_background = Frame("system/button_hover.png",10,10)
    style.pref_button.yminimum = 80
    
    style.pref_button_text.color = "#0000"
    style.pref_button_text.size = 28
    style.pref_button_text.font = "fonts/RepeatFont.ttf"
    style.pref_button_text.outlines = [(0, "#ffff", 0, 0)]
    style.pref_button_text.hover_outlines = [(2, "#929292", 0, 0)]
    style.pref_button_text.selected_outlines = [(2, "#363636", 0, 0)]
    style.pref_button_text.selected_hover_outlines = [(2, "#929292", 0, 0)]
    
    style.pref_label.xalign = 0.5
    style.pref_label_text.color = "#ffff"
    style.pref_label_text.outlines = [(2, "#000000", 0, 0)]
    
    style.pref_frame.background = Frame("system/frame.png",10,10)
    
    style.pref_slider.left_bar = "system/bar_full.png"
    style.pref_slider.right_bar = "system/bar_empty.png"
    style.pref_slider.hover_left_bar = "system/bar_hover.png"
    style.pref_slider.ymaximum = 90
    style.pref_slider.xmaximum = 560
    style.pref_slider.xalign = 0.5
    style.pref_slider.thumb = "system/thumb.png"
    style.pref_slider.thumb_offset = 1
    style.pref_slider.thumb_shadow = None
    
    

##############################################################################
# 예/아니오 확인 화면
#
# 예 또는 아니오를 묻는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen confirm(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"
        add FileCurrentScreenshot() at blur:
            xzoom 6.4 yzoom 6

    frame:
        style_prefix "confirm"

        xfill True
        xmargin .3
        ypos .25
        yanchor 0
        ypadding .05

        vbox:
            xfill True
            spacing 25

            text _(message):
                text_align 0.5
                xalign 0.5

            hbox:
                spacing 100
                xalign .5
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    # 마우스 우클릭과 esc 키는 No 버튼과 같다.
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 1
        layout "subtitle"


##############################################################################
# 단축 메뉴 화면
#
# say 스크린에 기본적으로 포함되어 일부 유용한 기능을
# 빠르게 사용할 수 있는 버튼이 포함된 스크린.
screen quick_menu:
    imagemap:
        ground "system/gui_idle.png"
        hover "system/gui_hover.png"
        # hotspot (x,y,xsize,ysize) action action("action_name")
        hotspot (1160,20,100,100) action ShowMenu('preferences')
        hotspot (1040,20,100,100) action QuickSave()
        hotspot (920,20,100,100) action FileTakeScreenshot(), QuickLoad()
        hotspot (20,20,100,100) action Skip()#(fast=False, confirm=False) #빨리 넘기기 단축 메뉴
        hotspot (20,140,100,100) action FileTakeScreenshot(), Preference("auto-forward", "toggle") #자동 넘기기 단축 메뉴
        
        #hotspot (20,20,100,100) action [SetVariable("yvalue", 1.0), ShowMenu('text_history')] #텍스트 기록 보기 메뉴
        #hotspot (800,20,100,100) action ShowMenu("tips")

# init -2:
    # style quick_button:
        # is default
        # background None
        # xpadding 20

    # style quick_button_text:
        # is default
        # size 34
        # idle_color "#ffff"
        # hover_color "#ccc"
        # selected_idle_color "#0000"
        # selected_hover_color "#880300"
        # insensitive_color "#7d7d7d"

init python:
    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random number's we'll generate.
    import random
    
    # initialize random numbers
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    class SnowFactory(object):
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            self.max_particles = max_particles
            self.speed = speed
            self.wind = wind
            self.xborder = xborder
            self.yborder = yborder
            self.depth = kwargs.get("depth", 10)
            self.image = self.image_init(image)
        def create(self, particles, st):
            if particles is None or len(particles) < self.max_particles:
                depth = random.randint(1, self.depth)
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]
        def image_init(self, image):
            rv = [ ]
            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )
            return rv
        def predict(self):
            return self.image
    class SnowParticle(object):
        def __init__(self, image, wind, speed, xborder, yborder):
            self.image = image
            if speed <= 0:
                speed = 1
            self.wind = wind
            self.speed = speed
            self.oldst = None        
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
        def update(self, st):
            if self.oldst is None:
                self.oldst = st
            lag = st - self.oldst
            self.oldst = st
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None
            return int(self.xpos), int(self.ypos), st, self.image
    
##############################################################################
# 캐릭터 애니메이션
#
# 캐릭터의 스텐딩 CG에 눈 깜빡임과 입술 움직임을 표현
# http://www.renpy.org/wiki/renpy/doc/cookbook/Blink_And_Lip_Flap
init python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)
    
##############################################################################
# 조사 장면
#
# 게임 내에서 조사를 하는 장면들을 모아놓은 코드 입니다.

############################렌스 사무실 조사 이미지맵###########################
init:
    screen desk_imagemap:
        imagemap:
            ground "event/office_desk.png"
            hover "event/office_desk.png"
        
            hotspot (660,300,80,80) clicked Return("cup")
            hotspot (820,120,180,220) clicked Return("computer")
            hotspot (820,320,460,100) clicked Return("doc")
            hotspot (320,420,200,300) clicked Return("drawer")
############################서재 (일기장 조사)#############################
init:
    screen lib_imagemap:
        imagemap:
            ground "bg/lib_night.png"
            hover "bg/lib_night.png"
        
            hotspot (878,0,402,250) clicked Return("maridge") # 액자
            hotspot (141,167,179,216) clicked Return("pencil_case") # 필통
            hotspot (640,236,236,228) clicked Return("notes") # 노트
            hotspot (343,492,236,228) clicked Return("bible") # 성격
            hotspot (335,130,236,284) clicked Return("diary") # 일기장
            hotspot (144,501,183,219) clicked Return("sherlock") # 셜록홉즈 책
##############################폐건물 입구 조사##############################
init:
    screen case2_imagemap:
        imagemap:
            ground "bg/case2_inside.png"
            hover "bg/case2_inside.png"
        
            hotspot (454,234,297,167) clicked Return("entrance") # 입구
            hotspot (986,268,294,273) clicked Return("wall") # 벽
            hotspot (0,0,412,678) clicked Return("2ndfloor") # 2층
            hotspot (622,483,658,237) clicked Return("floor") # 바닥
            hotspot (705,302,297,167) clicked Return("garbage") # 쓰래기 더미
##############################################################################
# 게임오버 화면
#
# 환경설정을 변경할 수 있는 스크린.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
init:
    screen gameover_imagemap:
        imagemap:
            ground "system/game_over_idle.png"
            hover "system/game_over_hover.png"
        
            hotspot (80,480,400,160) action ShowMenu("load") # 로드
            hotspot (870,510,330,140) action MainMenu() # 타이틀
label game_over:
    stop bgs
    stop sound
    play music "bgm/sad1.mp3"
    scene red with Dissolve(2.0)
    $ renpy.pause(1)
    scene ev game_over with memory
    call screen gameover_imagemap
    
    






