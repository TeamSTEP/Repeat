# 이 파일에 게임 스크립트를 입력합니다.
# 게임에서 사용할 배경을 정의 합니다.
image bg test = "bg/test_room.png"
image bg test2 = "bg/test_room2.png"
image bg galaxy = "bg/galaxy.png"
image bg ravine_day = "bg/ravine_day.png"
image bg ravine_night = "bg/ravine_night.png"
image bg grandpa_mansion = "bg/grandpa_mansion.png"
image bg grandpa_mansion_eve = "bg/grandpa_mansion_evening.png"
image bg grandpa_mansion_night = "bg/grandpa_mansion_night.png"
image bg mansion_hall = "bg/mansion_hall.png"
image bg mansion_hall_night = "bg/mansion_hall_night.png"
image bg mansion_emptyroom = "bg/mansion_emptyroom.png"
image bg mansion_kitchen = "bg/mansion_kitchen.png"
image bg mansion_kitchen_night = "bg/mansion_kitchen_night.png"
image bg mansion_bedroom = "bg/mansion_bedroom.png"
image bg mansion_bedroom_night = "bg/mansion_bedroom_night.png"
image bg mansion_diningroom = "bg/mansion_diningroom.png"
image bg mansion_diningroom_night = "bg/mansion_diningroom_night.png"
image bg lib_night = "bg/lib_night.png"
image bg lib_day = "bg/lib_day.png"
image bg market_inside = "bg/market_inside.png"
image bg market_inside_night = "bg/market_inside_night.png"
image bg market_outside = "bg/market_outside.png"
image bg market_back = "bg/market_back.png"
image bg room_stephan_day = "bg/room_stephan_day.png"
image bg room_stephan_eve = "bg/room_stephan_eve.png"
image bg room_stephan_night = "bg/room_stephan_night.png"
image bg school_classroom = "bg/school_classroom.png"
image bg school_hall = "bg/school_hall.png"
image bg school_cafe = "bg/school_cafe.png"
image bg room_mel = "bg/room_mel.png"
image bg office_inside = "bg/office_inside.png"
image bg office_outside = "bg/office_outside.png"
image bg willy_house = "bg/willy_house.png"
image bg outside_road = "bg/outside_road.png"
image bg outside_busstop = "bg/outside_busstop.png"
image bg mel_house = "bg/mel_house.png"
image bg edward_house_night = "bg/edward_house_night.png"
image bg edward_house_day = "bg/edward_house_day.png"
image bg police_meeting = "bg/police_meeting.png"
image bg police_hall = "bg/police_hall.png"
image bg downtown_outside = "bg/downtown_outside.png"
image bg downtown_gamestore = "bg/downtown_gamestore.png"
image bg downtown_cafe = "bg/downtown_cafe.png"
image bg downtown_fastfood_counter = "bg/downtown_fastfood_counter.png"
image bg fastfood_bathroom = "bg/fastfood_bathroom.png"
image bg employee_lounge = "bg/employee_lounge.png"
image bg employee_office_day = "bg/employee_office_day.png"
image bg employee_office_night = "bg/employee_office_night.png"
image bg employee_garden = "bg/employee_garden.png"
image bg employee_meeting_room = "bg/employee_meeting_room.png"
image bg working_site = "bg/working_site.png"
image bg sidewalk_night = "bg/sidewalk_night.png"
image bg bus_seat = "bg/bus_seat.png"
image bg diary_stage = "bg/diary_stage.png"
image bg diary_trainstation = "bg/diary_trainstation.png"
image bg diary_park = "bg/diary_park.png"
image bg diary_park_snow = "bg/diary_park_snow.png"
image bg diary_park_snow_night = "bg/diary_park_snow_night.png"
image bg diary_park_night = "bg/diary_park_night.png"
image bg diary_park_eve = "bg/diary_park_eve.png"
image bg diary_walkway = "bg/diary_walkway.png"
image bg diary_country = "bg/diary_country.png"
image bg diary_ssm = "bg/diary_ssm.png"
image bg diary_hospital_med = "bg/diary_hospital_med.png"
image bg diary_hospital_bed = "bg/diary_hospital_bed.png"
image bg diary_hospital_bed_night = "bg/diary_hospital_bed_night.png"
image bg diary_hospital_hall = "bg/diary_hospital_hall.png"
image bg diary_mansion_hall = "bg/diary_mansion_hall.png"
image bg diary_mansion_hall_night = "bg/diary_mansion_hall_night.png"
image bg country_way = "bg/country_way.png"
image bg mary_office = "bg/mary_office.png"
image bg book_store = "bg/book_store.png"
image bg case2_outside = "bg/case2_outside.png"
image bg case2_outside_night = "bg/case2_outside_night.png"
image bg case2_inside = "bg/case2_inside.png"
image bg case2_inside2 = "bg/case2_inside2.png"
image bg case2_inside2_night = "bg/case2_inside2_night.png"
image bg case2_inside3_night = "bg/case2_inside3_night.png"
image bg ravine_grave = "bg/ravine_grave.png"
image bg ravine_grave_night = "bg/ravine_grave_night.png"
image bg room_tatami = "bg/room_tatami.png"
image bg room_edward = "bg/room_edward.png"
image bg chinesefood_seat = "bg/chinesefood_seat.png"
image bg diary_walkway = "bg/diary_walkway.png"
image bg diary_restaurant = "bg/diary_restaurant.png"
image bg store_outside_night = "bg/store_outside_night.png"
image bg store_inside = "bg/store_inside.png"

# 게임에서 사용할 챕터와 사건 타이틀을 정의 합니다.
#image chapter1 = "chapters/tobecontinued.png"
image chapter1 = "chapters/chapter1.png"
image chapter2 = "chapters/chapter2.png"
image chapter3 = "chapters/chapter3.png"
image chapter4 = "chapters/chapter4.png"
image chapter5 = "chapters/chapter5.png"
image case1 = "chapters/case1.png"
image case2 = "chapters/case2.png"
image case_close = "effect/case_close.png"

# 임펙트를 정의 합니다.
image effect1:
    "effect/effect1.png"
    linear 0.1 zoom 1.3 xalign 0.5 yalign 0.5
    0.2
    linear 0.1 zoom 1.0
    0.2
    repeat
    
    
    
image effect2 = "effect/effect2.png"

# GUI 를 정의합니다.
image inspect_mode = "system/gui_inspect.png"

# 게임에 사용될 에니메이션을 정의 합니다.
# 커서
#image ctc1 = Animation("ctc/ctc1.png", 0.3, "ctc/ctc2.png", 0.3, "ctc/ctc3.png", 0.3, "ctc/ctc4.png", 0.6, "ctc/ctc3.png", 0.3, "ctc/ctc2.png", 0.3, "ctc/ctc1.png", 0.5, xpos=1, ypos=0.95, xanchor=1.0, yanchor=1.0)
image ctc1 = Animation("ctc/ctc1.png", 0.3, "ctc/ctc2.png", 0.3, "ctc/ctc3.png", 0.3, "ctc/ctc4.png", 0.6, "ctc/ctc3.png", 0.3, "ctc/ctc2.png", 0.3, "ctc/ctc1.png", 0.5, xpos=1, ypos=1, xanchor=0.0, yanchor=0.0)

init:
    image snow = Snow("effect/snowflake.png") #show snow로 눈 효과를 표시
    if not persistent.set_afm_time:
        $ persistent.set_afm_time = True
        $ _preferences.afm_time = 6

# 게임에서 사용할 이벤트를 정의합니다.
image ev game_over = "system/game_over_idle.png"
image ev p_background = "puzzles/background.png"
image ev soc_dec = "event/soc_dec.png"
image ev dic_stephan = "event/dic_stephan.png"
image ev phone_stephan = "event/phone_stephan.png"
image ev anne_ontop = "event/anne_ontop.png"
image anne_ontop 1 = "event/anne_ontop1.png"
image anne_ontop 2 = "event/anne_ontop2.png"
image anne_ontop 3 = "event/anne_ontop3.png"
image ev grandpa_bed = "event/grandpa_bed.png"
image grandpa_bed2 = "event/grandpa_bed2.png"
image ev seb_holdcat = "event/seb_holdcat.png"
image ev quantum = "event/quantum.png"
image ev safe_closed = "event/safe_closed.png"
image ev safe_opend = "event/safe_opend.png"
image ev bis_card = "event/biscard.png"
image ev alarm_clock = "event/alarmclock.png"
image ev cafe_seat = "event/downtown_cafe_sit.png"
image ev fastfood_sit = "event/downtown_fastfood_sit.png"
image ev diary_laydown = "event/diary_laydown.png"
image ev snowfight_hit = "event/diary_snowfight.png"
image ev office_desk = "event/office_desk.png"
image ev ribbon_stephan = "event/ribbon_stephan.png"
image ev ribbon_mary = "event/ribbon_mary.png"
image phone = "event/phone.png"
image phone2 = "event/phone2.png"
image phone2_alarm = "event/phone2_alarm.png"
image ev book = "event/book.png"
image ev book2 = "event/book2.png"
image ev book3 = "event/book3.png"
image ev edward_interview = "event/edward_interview.png"
image ev note = "event/note.png"
image letter1 = "event/letter1.png"
image ev sky_snow = "event/sky_snow.png"
image ev sky_cloudy = "event/sky_cloudy.png"
image ev sky_eve = "event/sky_eve.png"
image ev sky_clear = "event/sky_clear.png"
image ev sky_night = "event/sky_night.png"
image badcurry = "event/badcurry.png"
image ev lib_night_door = "event/lib_night_door.png"
image ev tv_barney = "event/tv_barney.png"
image ev tv_red = "event/tv_red.png"
image ev black_board = "event/blackboard.png"
image ev anne_watching = "event/anne_watching.png"
image ev anne_watching2 = "event/anne_watching2.png"
image anne_watching_yan = "event/anne_watching_yan.png"
image ev willy_mid = "event/willy_mid.png"
image willy_mid2 = "event/willy_mid2.png"
image ev marrage_image = "event/marrage_image.png"
image ev willy_cuffed = "event/willy_cuffed.png"
image ev watching_bug = "event/watching_bug.png"
image ev cheese_cream = "event/cheese_cream.png"
image ev elsaras_door = "event/elsaras_door.png"
image phone_unknown = "event/phone_unknown.png"
image falling_apple = "event/falling_apple.png"
image ev anne_killing_body = "event/anne_killing_body.png"
image ev anne_killing_bodyb = "event/anne_killing_bodyb.png"
image anne_killing cutter = "event/anne_killing_cutter.png"
image anne_killing cutter2 = "event/anne_killing_cutter2.png"
image anne_face mad = "event/anne_killing_face1.png"
image anne_face talk = "event/anne_killing_face2.png"
image anne_faceb = "event/anne_killing_faceb.png"
image ev mel_calling = "event/mel_calling.png"
image mel_calling talk = "event/mel_calling_talk.png"
image mel_calling smile = "event/mel_calling_smile.png"
image mel_calling smile2 = "event/mel_calling_smile2.png"
image op1 = "event/op_1.png"
image op2 = "event/op_2.png"
image op3 = "event/op_3.png"
image op4 = "event/op_4.png"
image op5 = "event/op_5.png"
image op6 = "event/op_6.png"
image cominfo1 = "event/cominfo1.png"
image cominfo2 = "event/cominfo2.png"
image cominfo3 = "event/cominfo3.png"
image title = "event/title.png"
image math1 = "event/math1.png"
image math2 = "event/math2.png"
image math3 = "event/math3.png"
image math4 = "event/math4.png"
image math5 = "event/math5.png"
image ev mary_eating = "event/mary_eating.png"
image mary_eating 1 = "event/mary_eating1.png"
image mary_eating 2 = "event/mary_eating2.png"
image ev edward_hug = "event/edward_hug.png"
image ev mary_falling = "event/mary_falling.png"
image old_nostalgia = "event/old_nostalgia.png"
image ev edward_piano1 = "event/edward_piano1.png"
image ev edward_piano2 = "event/edward_piano2.png"
image ev edward_piano3 = "event/edward_piano3.png"
image ev ruin_logo = "event/Ruin_logo.png"


# 주인공
define stephan = Character("스테반 토머",ctc="ctc1", ctc_position="nestled",callback=speaker("stephan"), what_prefix="\"", what_suffix="\"")
define stephan_think = Character("스테반 토머",ctc="ctc1", ctc_position="nestled",window_background = Frame("system/box_dark.png", 40, 40))# 대화창 변경
define edward = Character("에드워드 토머",ctc="ctc1", ctc_position="nestled", what_prefix="\"", what_suffix="\"")
define edward_think = Character("에드워드 토머",ctc="ctc1", ctc_position="nestled",window_background = Frame("system/box_dark.png", 40, 40))
define willy = Character("윌리 제임스",ctc="ctc1",ctc_position="nestled",callback=speaker("willy"), what_prefix="\"", what_suffix="\"") ###
define willy_think = Character("윌리 제임스",ctc="ctc1", ctc_position="nestled",window_background = Frame("system/box_dark.png", 40, 40))
$ mary_name = '메리 슈테른'
define mary  = Character("mary_name",ctc="ctc1", ctc_position="nestled", dynamic = True,callback=speaker("mary"), what_prefix="\"", what_suffix="\"")

define grandpa = Character("할아버지",ctc="ctc1",ctc_position="nestled",callback=speaker("edward"), what_prefix="\"", what_suffix="\"")
$ cia_name = '시아'
define cia = Character("cia_name",ctc="ctc1",ctc_position="nestled", dynamic = True, callback=speaker("cia"), what_prefix="\"", what_suffix="\"")
$ seb_name = '세바스찬 쟝'
define seb = Character("seb_name",ctc="ctc1",ctc_position="nestled", dynamic = True,callback=speaker("seb"), what_prefix="\"", what_suffix="\"")

define anne = Character("앤 크라운",ctc="ctc1",ctc_position="nestled",callback=speaker("anne"), what_prefix="\"", what_suffix="\"")
define anne_think = Character("앤 크라운",ctc="ctc1", ctc_position="nestled",window_background = Frame("system/box_dark.png", 40, 40))
define mel = Character("멜 다운스",ctc="ctc1",ctc_position="nestled",callback=speaker("mel"), what_prefix="\"", what_suffix="\"")
define lance = Character("렌스 클라크",ctc="ctc1",ctc_position="nestled",callback=speaker("lance"), what_prefix="\"", what_suffix="\"")
$ lisa_name = '리사 보우만'
define lisa = Character("lisa_name",ctc="ctc1",ctc_position="nestled", dynamic = True,callback=speaker("lisa"), what_prefix="\"", what_suffix="\"")
define nixon = Character("루드윅 닉슨",ctc="ctc1",ctc_position="nestled",callback=speaker("nixon"), what_prefix="\"", what_suffix="\"")
define nixon_think = Character("루드윅 닉슨",ctc="ctc1", ctc_position="nestled",window_background = Frame("system/box_dark.png", 40, 40))
$ dad_name = '메리의 아버님'
define dad = Character("dad_name",ctc="ctc1",ctc_position="nestled", dynamic = True,callback=speaker("dad"), what_prefix="\"", what_suffix="\"")
define elsara = Character("엘사라 나보코프",ctc="ctc1",ctc_position="nestled",callback=speaker("elsara"), what_prefix="\"", what_suffix="\"")

# 엑스트라
define doc = Character("의사",ctc="ctc1",ctc_position="nestled",what_prefix="\"", what_suffix="\"")
$ extra_name = '엑스트라'
define extra = Character("extra_name",ctc="ctc1",ctc_position="nestled", dynamic = True, what_prefix="\"", what_suffix="\"")

# 기타
define narrator = Character(_(None),ctc="ctc1", ctc_position="nestled",window_background = Frame("system/box_dark.png", 40, 40))
define someone = Character("???",ctc="ctc1",ctc_position="nestled", what_prefix="\"", what_suffix="\"")
# 트렌지션 효과 정의
define flash = Fade(0.1, 0.2, 0.5, color="#fff")

init python:
    def typing_sound(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.music.play("se/typing.ogg",channel='channel1')
        elif event == "slow_done":
            renpy.music.stop(channel='channel1')
    pixellate = Pixellate(0.4, 10)

# NVL 형식의 대화 정의
init:
    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve
    $ config.window_hide_transition = dissolve
    $ config.window_show_transition = dissolve
    $ narrator_nvl = Character(_(None),color="fff",kind=nvl,ctc="ctc1", ctc_position="nestled",window_left_padding=120,window_right_padding=360,what_xalign = 0.5, show_who_window_style="say_who_window1",what_size = 25)
    $ centered = Character(_(None),callback=typing_sound,window_left_padding=0,window_top_padding=120,window_background = '#00000000',what_size = 55,what_font="fonts/Type_Writer.ttf",what_slow_cps = 4) #타자기 효과

# 화면을 흔드는 효과
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    
#레터박스 효과
image letterbox_up:
    "effect/letterbox_up.png"
    xalign 0.0 yalign 1.0 alpha 0.0
    linear 0.5 yalign 0.0 alpha 1.0

image letterbox_down:
    "effect/letterbox_down.png"
    xalign 0.0 yalign 0.0 alpha 0.0
    linear 0.5 yalign 1.0 alpha 1.0

image letterbox = Fixed(At("letterbox_up", Position(pos=(0,0))), At("letterbox_down", Position(pos=(0,config.screen_height))), xysize=(config.screen_width,config.screen_height))

image letterboxhide_up:
    "effect/letterbox_up.png"
    xalign 0.0 yalign 0.0 alpha 1.0
    linear 0.5 yalign 1.0 alpha 0.0

image letterboxhide_down:
    "effect/letterbox_down.png"
    xalign 0.0 yalign 1.0 alpha 1.0
    linear 0.5 yalign 0.0 alpha 0.0

image letterbox h = Fixed(At("letterboxhide_up", Position(pos=(0,0))), At("letterboxhide_down", Position(pos=(0,config.screen_height))), xysize=(config.screen_width,config.screen_height))

#잡음 효과
image static:
    "effect/noise1.png" with Dissolve(0.2, alpha=True)
    0.2
    "effect/noise2.png" with Dissolve(0.2, alpha=True)
    0.2
    "effect/noise3.png" with Dissolve(0.2, alpha=True)
    0.2
    "effect/noise4.png" with Dissolve(0.2, alpha=True)
    0.2
    repeat
    
#별 효과
init python:

    class StarField(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            # A list of (sprite, starting-x, speed).
            self.stars = [ ]

            # Note: We store the displayable in a variable here.
            # That's important - it means that all of the stars at
            # a given speed have the same displayable. We render that
            # displayable once, and cache the result.

            d = Transform("effect/snowflake.png", zoom=.05)
            for i in range(0, 50):
                self.add(d, 1)

            d = Transform("effect/snowflake.png", zoom=.055)
            for i in range(0, 50):
                self.add(d, 2)

            d = Transform("effect/snowflake.png", zoom=.06)
            for i in range(0, 50):
                self.add(d, 3)

            d = Transform("effect/snowflake.png", zoom=.065)
            for i in range(0, 50):
                self.add(d, 4)

            d = Transform("effect/snowflake.png", zoom=.07)
            for i in range(0, 50):
                self.add(d, 5)

            d = Transform("effect/snowflake.png", zoom=.075)
            for i in range(0, 50):
                self.add(d, 10)

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1280)
            s.y = renpy.random.randint(0, 720)

            self.stars.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.stars:
                s.x = (start + speed * st) % 1280 - 20

            return 0

init:
    
    $ memory = ImageDissolve("effect/memory.png", 2.0, 1)
    $ lshake = Shake((0, 0, 0, 0), 1.5, dist=20)
    $ sshake = Shake((0, 0, 0, 0), 0.4, dist=10)
    transform blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.15 xoffset -2
        contains:
            child
            alpha 0.15 xoffset 2
        contains:
            child
            alpha 0.15 xoffset -3
        contains:
            child
            alpha 0.15 xoffset 3
        contains:
            child
            alpha 0.15 xoffset -4
        contains:
            child
            alpha 0.15 xoffset 4
        contains:
            child
            alpha 0.15 xoffset -5
        contains:
            child
            alpha 0.15 xoffset 5
        contains:
            child
            alpha 0.15 xoffset -6
        contains:
            child
            alpha 0.15 xoffset 6
        contains:
            child
            alpha 0.15 xoffset -7
        contains:
            child
            alpha 0.15 xoffset 7


init python:
  def eyewarp(x):
    return x**1.33
  eyeopen = ImageDissolve("effect/eyeblink.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
  eyeshut = ImageDissolve("effect/eyeblink.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
  moveleft = ImageDissolve("effect/moveleft.png", 1, ramplen=128, reverse=False, time_warp=eyewarp)
  moveright = ImageDissolve("effect/moveright.png", 1, ramplen=128, reverse=False, time_warp=eyewarp)
  moveup = ImageDissolve("effect/moveup.png", 1, ramplen=128, reverse=False, time_warp=eyewarp)
  movedown = ImageDissolve("effect/movedown.png", 1, ramplen=128, reverse=False, time_warp=eyewarp)
image white = Solid("#FFF")
image red = Solid("#bb0000")

######################시계
init:
    #This makes a clock and sets it to 3:00pm
    $ myClock = Clock(True, 3, 0, 150, False)

# UDD's as far as I can tell, need to be added to something (a screen, a vbox, a frame, etc)...so here I'm making
# a screen to add the clock to. I want the clock all in the center!
screen clock_screen:
    add myClock:
        xalign 0.5 
        yalign 0.5

jump start
