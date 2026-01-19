##############################################################################################
######################################챕터2: 회상하는 추억#############################################
##############################################################################################
label chapter2:
    stop music
    play sound "se/heartbeat.mp3"
    $ save_name = "2.회상하는 추억"
    scene chapter2 with flash
    $ renpy.pause(2)
    scene black with Dissolve(1.0)
    centered"오후 2시 59분"
    centered"할아버지의 서재"
    scene bg lib_day with moveup
    "나는 도서실에서 일기장을 읽으러 다가갔다."
    "뭘까……{cps=2} {/cps}이 무력감……"
    "할아버지의 몸에서 무언가가 일어나는 동안, 내가 할 수 있는거라곤─여기서 가만히 앉아, 일기장이나 읽는거라니……"
    "아니……"
    "그렇게 생각하는 게 아니다."
    "그래도 이런거라도 할 수 있는것에 다행이라고 생각해보는거다."
    play sound "se/book_page.ogg"
    scene black with moveright
    play sound "se/case_start.mp3"
    show text"{font=fonts/Type_Writer.ttf}{size=60}1958년 11월 5일{/size}{/font}" with memory:
        xalign 0.5 yalign 0.5
    $ renpy.pause(3.0)
    scene ev p_background with dissolve
    play music "bgm/Pathetique_Orgel.mp3"
    python:
        k = puzzle2()
        k.set_sensitive(False)
        k.show()
    while True:
        python:
            k.set_sensitive(True)
            event = k.interact()
            if event:
                renpy.checkpoint()
            k.set_sensitive(False)
        if event == "win":
            jump diary58115
    ################################1958년 11월 5일 일기장 시작############################
label diary58115:
    play sound "se/book_page.ogg"
    stop music
    scene black with memory
    narrator_nvl"1958년 11월 5일 수요일"
    narrator_nvl"에드워드 토머 26세"
    narrator_nvl"날씨 - 추움, 바람이 조금 붐"
    nvl clear
    narrator_nvl"오늘은 나의 첫 출근 일 이다."
    narrator_nvl"생애 첫 출근이기도 해서 그런지 정말 가슴이 두근거린다."
    narrator_nvl"이건 전부 어제 처음 만나게된 메리 슈테른 이라는 사람 덕분에 가능했다."
    narrator_nvl"그런데……"
    narrator_nvl"나는 그 사람에 대해서 아무것도 모르겠다."
    narrator_nvl"그리고 나로썬 그 사람의 행동을 이해하기 힘들었다."
    narrator_nvl"뭐……{cps=2} {/cps}나한텐 아무런 손해가 없으니까 상관 없지만……"
    nvl clear
    play bgs "bgs/people.mp3"
    scene bg employee_office_day with dissolve # 회사 사무실 배경
    centered"노스탤지어 토이즈 B동 사무실"
    "나는 긴장된 마음으로 건물 안으로 들어와서, 슈테른 씨를 찾기 시작했다."
    "분명 여기 어디서 기다리겠다고 했는데……"
    "그때 의자에 앉아있는 금발의 여성이 눈에 띄었다."
    show bg employee_office_day at Zoom((1280,720),(0,0,1280,720),(366,378,608,342),0.5)
    "분명 슈테른 씨라 생각하고 다가갔는데……"
    stop music
    $ mary_hair = 'mad'
    show mary cry with dissolve:
        zoom 1.8 xalign 0.6 yalign -0.3
    mary"흑……"
    edward"……!"
    play music "bgm/sad2.mp3"
    "울고 있었다."
    "헝클어진 머리에다 충혈된 눈으로 봤을때, 꽤 오랫동안 운 거 같았다."
    edward"괜찮으세요?!"
    mary"…………"
    mary"토, 토머 씨?"
    edward"어제 편지에서 분명 여기로 오라고 말씀 하셨는데……"
    play sound "se/search_bag.mp3"
    show mary shock with dissolve
    mary"이거……{cps=2} {/cps}제가 부끄러운 모습을 보여버렸네요……"
    edward"무슨 일 있었나요?"
    show mary shock2
    mary"아무것도 아니에요!"
    show mary
    mary"그, 그보다 제가 볼일이 생기는 바람에 잠시 자리를 비워야 되네요"
    mary"죄송합니다"
    play sound "se/footsteps_running.mp3"
    show mary sad:
        linear 0.5 xalign -2.0
    "슈테른 씨는 마치 무언가로부터 도망치듯이 달려갔다."
    "도대체 무슨 일이 있었길래 다 큰 어른이 눈물을 터뜨릴까……"
    "궁금하긴 하지만, 본인은 아무것도 아니라고 말 했고……{cps=2} {/cps}무엇보다 괜히 남의 일에 참견하는 건 좋지 않다고 생각한다."
    "그럼 난 슈테른 씨가 돌아올때까지 가만히 기다리고 있어야 하나……?"
    hide mary
    $ mary_hair = 'normal'
    stop music
    "허나 그렇게 되면 아까운 시간이 낭비된다."
    "그러니 내가 당장 할 수 있는 것─같이 일하게 될 사람들에게 인사─를 하기로 했다."
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.2)
    scene bg employee_office_day at Zoom((1280,720),(0,0,1280,720),(87,285,669,377),0.0) with moveright # 회사 사무실 배경
    "나는 책상 옆에 있던 직원에게 다가가, 힘들게 미소를 지으면서 말을 걸었다."
    edward"아,{cps=2} {/cps}안녕하세요!"
    edward"제 이름은 \'에드워드 토머\'라고 합니다"
    $ extra_name = '직원'
    extra"안녕하세요─"
    "이 사람은 나를 제대로 쳐다보지도 않고 대충 대답 했다."
    "조금 거슬리긴 했지만, 그래도 이런 취급은 별로 드믄게 아니라서 크게 문제가 되진 않았다."
    edward"이런 데서 일해보는 건 처음이지만 앞으로 잘 부탁드립니다!"
    extra"네에……"
    extra"그럼 전 바쁜 관계로……"
    edward"앗!{cps=2} {/cps}실례 했습니다!"
    "뭐지……"
    "일단 이 사람은 무시하고, 다른 사람에게 인사를 해보기로 했다."
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg employee_office_day at Zoom((1280,720),(0,0,1280,720),(611,198,669,377),0.0) with moveright # 회사 사무실 배경
    edward"안녕하세요.{cps=2} {/cps}이번에 새로 일 하게 된 \'에드워드 토머\'라고 합니다"
    extra"아,{cps=2} {/cps}혹시 그?!"
    edward"……저를 아시나요?"
    extra"아,{cps=2} {/cps}아무것도 아니에요!"
    extra"이,{cps=2} {/cps}이런……{cps=2} {/cps}사장님 께서 부탁하신 걸 아직 덜 끝냈네!"
    extra"그럼 전 이만……!"
    edward"네에……"
    "오늘 무슨 날인가?{cps=2} {/cps}어째서인지 다들 엄청 바뻐보이네"
    stop bgs
    scene black with eyeshut
    "하지만 그건 나의 희망사항에 불과했지……{cps=2} {/cps}사실 다들 날 피하려고 한다는 걸 이미 알고 있었다."
    extend" 나 같은 사람과 같이 일을 한다고 생각하면 보통 저런 식이니까"
    "내가 참 한심하다는 생각이 들었다."
    "공사장이나, 회사도 결국엔 사람들이 움직이고 있는 것"
    "그러니 이렇게 될거라는 건 내심 예상하고 있었는데……"
    play bgs "bgs/people.mp3"
    scene bg employee_office_day at Zoom((1280,720),(0,0,1280,720),(283,190,713,401),0.0) with eyeopen
    edward"어휴―"
    "내 앞엔 힘든 회사 생활 뿐 이라는 것에 한숨이 절로 나왔다."
    show mary shock2 with dissolve:
        zoom 1.7 xalign -0.3 yalign -0.4
    "그리고 얼마가 지났을까?{cps=2} {/cps}누군가 내 어깨 위에 손을 올렸다."
    play music "bgm/happy2.mp3"
    show bg employee_office_day at Zoom((1280,720),(283,190,713,401),(0,190,713,401),0.8)
    show mary shock2:
        linear 0.8 xalign 0.5
    mary"생각보다 늦어서 죄송해요~"
    "뒤를 돌아보니 슈테른 씨가 있었다."
    "묘하게 눈 쪽이 바뀐거 같은 게……{cps=2} {/cps}잠시 자리를 비운다는 게, 화장을 고치러 갔던건가보다."
    mary"아까 한숨을 쉬고 계시던데 혹시 무슨 일이라도 있었나요?"
    edward"그게……"
    edward"혹시 제가 회사 일이랑은 잘 안 맞는 게 아닐까 하는 생각이 들어서요……"
    show mary shock
    edward"물론 일이라는 게 먹고 살기 위해서 어쩔 수 없이 하는거니까 자기 의지는 별로 중요하지 않다는 건 알고 있지만요!"
    show mary
    mary"꼭 그런것만은 아니에요"
    show mary smile
    mary"전 회사에서 일 하는 게 살기 위해서가 아니라 즐거워서 그런걸요?"
    "\'그거야 당신처럼 돈을 많이 버는 사람은 먹고 살 걱정을 하지 않아도 되니까\'"
    "……라고 말 하려고 했지만, 필사적으로 참았다."
    edward"그, 그럼 전 뭘 하면 되는거죠?"
    show mary
    mary"토머 씨는 오늘이 첫 날이니까 간단한 회사 투어를 하도록 하죠"
    mary"……일단 떠나기 전에 저희 노스탤지어 토이즈의 짧은 역사를 알려드리겠습니다"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg employee_office_day with moveright
    show mary:
        zoom 1.7 xalign 0.5 yalign -0.4
    mary"……그러고 나서 지금 노스탤지어 토이즈의 시스템이 도입된게 1956년 부터예요"
    edward"그, 그렇군요……"
    "슈테른 씨는 말하는 내내 기뻐보였다."
    "분명 누군가에게 설명을 해주는 걸 즐기고 있는거겠지"
    "……하지만 난 슈테른 씨의 설명을 잘 이해하지 못했다."
    "아니, 이해 뿐만 아니라 방금 한 말도 기억이 가물가물하다."
    "그게……{cps=2} {/cps}내가 원래 좀 그런 경향이 있다."
    "남들이 쉽게 이해 하는 걸 나는 몇번이고 다시 생각을 해야 겨우 이해를 할 수 있다."
    "그거 말고도 무언가에 대한 집중력도 그리 좋지가 않다."
    "그때 아주머니가 이런 증상을 뭐라고 했더라……?"
    "\'ADD(Attention Deficit Disorder)\'였었나?"
    "\'ADHD(Attention Deficit Hyperactivity Disorder)\'랑 조금 비슷하면서 다른 정신 장애 라는 듯 하다."
    "……아니다.{cps=2} {/cps}둘다 같은건데 그냥 사람들이 다르게 부르는거였나?"
    "모르겠어……"
    "쉽게 말하자면, 난 집중력이 부족하고, 기억력도 별로 좋지 못한 바보다."
    "의사의 말론, 이 증상을 조금이라도 개선 하기 위해서 디테일한 일기를 쓰라고한다."
    mary"나머지는 일을 하다보면 자연스레 알게 될테니 설명은 여기까지만 하겠습니다"
    edward"ㄴ, 네에……!"
    mary"이번엔 회사의 시설에 대해서 알려드릴테니 절 따라오세요!"
    show mary:
        linear 2.0 xalign -0.5
    $ renpy.pause(0.5)
    play sound "se/move.mp3"
    scene bg employee_lounge with moveright
    play music "bgm/happy1.mp3"
    show mary
    mary"여기는 직원 휴게실 입니다"
    mary"일을 너무 많이해서 지쳤거나, 잠깐 숨 좀 돌리고 싶을땐 다들 여기서 시간을 보내죠"
    edward"그렇군요……"
    mary"참고로, 여긴 자주 안오는 걸 추천합니다"
    edward"그건 왜요?!"
    mary"여기서 사람들이 휴식을 취하는동안 가장 많이 하는 게 뭔지 아세요?"
    show mary tease with dissolve:
        yalign -0.2 zoom 1.8
    mary"{size=30}바로 \'뒷담화\'예요!{/size}"
    "그런 말을 하는 슈테른 씨는 마치 자기가 뒷담화를 하듯이 작은 목소리로 말했다."
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}으엑?!{/size}" with lshake
    hide effect1
    mary"아마 지금도 다들 토머 씨를 험담하고 있을 걸요?"
    edward"윽……!"
    "슈테른 씨는 엄청난 사실을 아무렇지도 않게 말 했다."
    show mary:
        zoom 1.0 yalign 1.0
    mary"괜히 자기를 까는 소리를 듣고 싶지 않으시다면 자주 오지 않으시는 걸 추천 할게요"
    edward"주,{cps=2} {/cps}주의 하도록 하겠습니다……"
    mary"그럼 다음 장소로 이동 하도록 하죠!"
    play sound "se/move.mp3"
    scene black with moveleft
    stop bgs
    nvl clear
    narrator_nvl"나랑 슈테른 씨는 거의 하루종일 회사 주변을 돌았다."
    narrator_nvl"식당, 화장실, 직원실 심지어 근처에 있는 공원 까지"
    narrator_nvl"아마 회사 전체를 돌았을 것이다."
    narrator_nvl"첫 날 이라곤 하지만 하루종일 돌아다니기만 할 필요는 있을까?"
    narrator_nvl"……회사랑 관련없는 공원은 왜?!"
    scene bg employee_garden with dissolve # 회사 화단
    centered"화단"
    show mary:
        zoom 1.5 xalign 0.7 yalign -0.3
    mary"여긴 저희 회사에서 가꾸고 있는 화단인데요"
    show mary smile
    mary"실내에서 꽃을 키우다 보니까 계절에 관계없이 꽃을 마음껏 구경할 수 있어요~!"
    edward"네에……"
    mary"또, 여긴 사람도 별로 없다보니까 독서하기 정말 좋은곳이에요"
    show mary
    mary"저도 여기 앉아서 자주 책을 읽어요……"
    stop music
    show mary talk with dissolve
    mary"…………"
    edward"……?"
    "갑자기 슈테른 씨가 말을 멈췄다."
    "그런데 그 모습이……{cps=2} {/cps}조금 우울해 보였다."
    edward"저……"
    show mary shock2
    mary"앗!{cps=2} {/cps}죄송합니다!"
    mary"제가 잠깐 한눈을 팔았네요"
    show mary smile
    mary"그, 그럼 다음 장소로 이동 하죠!"
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg mary_office with moveleft
    show mary:
        zoom 1.7 xalign 0.0 yalign -0.4
    mary"여기가 바로 제 사무실 입니다"
    mary"무슨 일이 있을땐 여기서 저를 찾아주세요"
    "개인 사무실 까지 있는 걸로 봤을때 슈테른 씨는 이 회사에서 조금 높은 자리에 있는 사람인가보다."
    play music "bgm/smooth4.mp3"
    show mary shock2
    mary"아, 아직 제가 사무실을 옮긴지 얼마 안 됐다보니까 물건 정리가 잘 안 돼 있어요"
    mary"그러니까 너무 훑어보진 말아주세요……"
    edward"알겠습니다"
    edward"근데 실례지만, 슈테른 씨는 여기서 무슨 일을 하시는가요?"
    show mary think
    mary"휴먼 리소스 매니지먼트, 재품 컨셉 최종 승인 등을 하고 있는데……"
    show mary talk
    mary"딱 한가지로만 간출여서 말 하기가힘드네요……"
    show mary smile
    mary"저는 직책 상으론 사장입니다!"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}사장?!{/size}" with lshake
    hide effect1
    show mary tease with dissolve:
        xalign 0.5
    mary"넵!{cps=2} {/cps}노스탤지어 토이즈 제조부서의 최고책임자이죠"
    edward"제조부서 라니요?"
    show mary talk
    mary"제가 여기 시스템에 대해서 설명 드리지 않았던가요?"
    edward"죄, 죄송합니다"
    edward"기억력이 별로 좋지 않아서요……"
    show mary think
    mary"흠흠……{cps=2} {/cps}그럼 제가 다시 설명 해드릴게요"
    show mary:
        linear 1.3 xalign -0.1 yalign -0.7
    mary"이 회사에는 A, B, C동으로 직책마다 건물이 나눠져 있어요"
    play sound "se/swing.mp3"
    show cominfo1 with moveright
    mary"A동은 \'제무·회계\'를 주로 담당하죠"
    extend". 들리는대로 회사의 자금 상태 등과 같이 별로 재미없는 일을 하는 곳 이에요"
    play sound "se/swing.mp3"
    show cominfo2 with moveright
    mary"B동은 \'제조\'담당"
    extend". 지금 저희가 서있는 건물 이에요"
    mary"여기선 새로운 장난감의 아이디어 및 \'블루프린트(Blue Print)\'를 만들죠"
    play sound "se/swing.mp3"
    show cominfo3 with moveright
    mary"마지막 C동이 \'마케팅\'을 담당 합니다"
    mary"사람들이 어떻게 해야 장난감을 살지, 포장지 및 TV광고 등을 그쪽에 고안 해요"
    play sound "se/shock2.mp3"
    show effect2
    show mary shock3
    mary"슬프게도 B동 건물의 사장으로써, 저는 그 3가지 전부 공부 해야 하지만요……"
    edward"그,{cps=2} {/cps}그렇군요"
    hide effect2
    "처음 말 해줬을 때 보단 조금 더 이해가 잘 된 거 같았다."
    "즉, 내가 여기에 있다는 건 내 일은 제조와 관련이 있다는 뜻"
    scene bg mary_office with moveright
    show mary:
        zoom 1.7 yalign -0.4 xalign 0.5
    mary"어쨌건, 전 이곳의 사장이기 때문에 혹시 곤란한 일이 있으시면 저에게 오세요!"
    "나랑 그렇게 나이 차이가 없을거 같은 사람이 사장이라……"
    "도대체 나와 그녀의 인생은 어디서부터 달랐기에 이런 결과가 나오는 걸까?"
    "조금 분하기도 했지만, 사장님─슈테른 씨─덕분에 취직이 가능했으니까, 불만은 없었다."
    "근데 사장이나 되는 사람이 나같은 신입 사원에게 회사 투어를 시키다니……"
    "물론 내 머릿속 회사의 이미지랑, 실제 회사가 다른 거뿐일 수도 있겠지만"
    edward"그……{cps=2} {/cps}평소에도 회사에 신입이 들어오면, 사장님 께서 회사 소개를 하는가요?"
    show mary shock2
    mary"{size=20}사, 사장님 이라니……{/size}"
    show mary
    mary"사실 제가 이렇게 회사 소개를 해보는 건 오늘이 처음 이에요……"
    mary"원래라면 다른 사원이 했을텐데……{cps=2} {/cps}토머 씨 같은 경우엔 제가 높으신 분들에게 부탁해서 겨우 취직을 시켜드린거라서……"
    mary"토머 씨가 일을 할 수 있도록 교육 시키는것도, 시스템에 대해서 설명을 하는것도 전부 제 일인걸로 됐어요"
    edward"…………"
    "난 여기서 무슨 표정을 지어야 하는지, 무슨 말을 해야 하는지 몰랐다."
    "확실히 나한텐 엄청난 이익이지만, 그 과정에서 사장님께 폐가 되는 건 별로 원치 않는 일이고……"
    "머릿속이 너무 복잡했다."
    "그 때문에 나는 사장님의 눈을 똑바로 처다보지 못했다."
    edward"어?"
    "시선을 피하다가 내 눈길이 책상 위로 흘렀다."
    "깔끔한 사무실 내부와는 대조된 이것……"
    play sound "se/search_bag.mp3"
    scene bg mary_office at Zoom((1280,720),(0,0,1280,720),(509,107,605,340),0.5) with dissolve
    "한번 가까이서 봤다."
    show old_nostalgia with dissolve:
        zoom 0.5 xalign 0.6 yalign 0.4
    "오르골?{cps=2} {/cps}같은 물건이었다."
    "대화의 주재를 바꾸는 겸사, 사장님께 물어봤다."
    edward"저……{cps=2} {/cps}실례지만, 이건 뭔가요?"
    edward"엄청 오래된거 같은데……"
    show mary shock with dissolve:
        zoom 2.2 xalign -0.2 yalign -0.2
    mary"그건……"
    show mary shock2
    mary"뭐같아 보이세요?"
    edward"글쎄요……"
    extend" 혹시 오르골 인가요?"
    show mary smile
    mary"네"
    mary"그 오르골은 NT0호기……!"
    stop music
    show mary sad with dissolve
    mary"NT0호기……"
    "사장님은 말을 끝마치지 못하면서, 표정은 점점 울상이 되어갔다."
    "왠지 내쪽에서 빨리 말을 끊지 않으면 아침 처럼 울 것 같은 느낌이 들었다."
    edward"그, 그 NT0호기 라는 건 뭔가요?!"
    edward"NT0호기도 있으면 1호기나 2호기 도 있는 건가요……?"
    "……내 머리속에서 가장 만저 떠올랐던 말이 이랬다."
    "막상 입 밖에 내뱉으니까 엄청 후회됐다."
    play sound "se/search_bag.mp3"
    hide mary sad with dissolve
    show mary talk with dissolve:
        zoom 2.2 xalign -0.2 yalign -0.2
    "그래도 사장님은 정신을 차리기 위해서 고개를 좌우로 흔든 다음에, 침착된 어조로 입을 여셨다."
    show mary
    mary"NT 넘버링은 사내에서만 쓰이는 재품 코드명이에요"
    mary"지금은 NT101호기 까지 있어요"
    edward"정말 많네요"
    mary"실제로 시중에 판매 되는 건 그중에서 아주 일부 뿐이지만요"
    mary"대부분은 어른의 사정으로 프로토타입에서만 끝나요"
    edward"그렇군요……"
    show mary talk
    play music "bgm/sad2.mp3"
    mary"하지만 0호기는 조금 특별해요……"
    mary"이 회사가 만들어지기 전에……"
    show mary sad with dissolve
    mary"그 사람이 저에게 만들어준 최초의 장난감 이었으니까……"
    "잠깐?!{cps=2} {/cps}사장님이 눈물을 흘리기 시작했다!"
    "아무래도 내가 말을 잘못 꺼냈는가보다."
    "하지만……"
    play sound "se/think.mp3"
    scene bg employee_office_day at Zoom((1280,720),(0,0,1280,720),(366,378,608,342),0.0) with flash
    $ mary_hair = 'mad'
    show mary cry:
        zoom 1.8 xalign 0.6 yalign -0.3
    $ renpy.pause(1.0)
    $ mary_hair = 'normal'
    scene bg mary_office at Zoom((1280,720),(0,0,1280,720),(509,107,605,340),0.0) with flash
    show old_nostalgia:
        zoom 0.5 xalign 0.6 yalign 0.4
    show mary sad:
        zoom 2.2 xalign -0.2 yalign -0.2
    "……아침에 왜 울었는지도 조금 궁금했다."
    "혹시 지금이라면 물어 볼 수 있지 않을까?"
    edward"저……"
    edward"실례지만, 아침에 왜 우셨는지 물어봐도 괜찮을까요?"
    edward"무, 물론 대답하기 힘드시다면 꼭 하실 필요는 없고요!!"
    edward"하지만……"
    edward"사무실에 있는 동안이라면 말 해도 아무도 모를거고……{cps=2} {/cps}혹시 제가 얘기를 들어주는 것 만으로도 도움이 될 수 있을지도 모르고……"
    edward"그, 그러니까 전 사장님이 계속 우울해 하는 모습을 보고 싶지가 않다고 해야 할까요……"
    "왠지 나 답지 않은 말을 해버렸다."
    "하지만 슈테른 사장님 덕분에 난 예전부터 취직하고 싶었던 장난감 회사에 취직 할 수 있었고……"
    "무엇보다 나는 타인에게 빚지면서 살고싶지는 않다."
    mary"…………"
    mary"혹시 \'에드워드 토머\'라고 아세요?"
    edward"어제 저랑 헷갈려 하셨던 동명인이라는 사람인가요?"
    mary"네"
    mary"오늘 아침에……"
    play music "bgm/sad3.mp3"
    mary"그 친구가 죽었다는 소식을 들었어요……"
    edward"네?!"
    edward"그런 일이있었다면 오늘 여기서 이러지 말고, 장례식장에……!"
    mary"오늘 죽은 게 아니라……"
    extend" 아주 오래전에 죽었대요……"
    mary"한동안 못 만났었는데……{cps=2} {/cps}이미 고인이었기 때문이라는 게……"
    mary"게다가 자택에서 목을 메달고 자살했다니!"
    edward"…………"
    mary"그렇게 착했던 사람이……{cps=2} {/cps}그런 최후를 맞이했다는 게 너무 안쓰러웠어요……"
    show mary cry
    mary"에드는……"
    extend" 누구보다 장난감에 대한 열정이 있었던 사람이었는데……"
    mary"저 오르골도 그 사람이 아주 어렸을때 절 위해서 만들어줬던거예요"
    mary"이렇게 장난감 회사에서 일을 한다면 다시 만날 수 있을 줄 알았는데……"
    show mary shock2
    mary"이, 이거 제가 너무 울기만 하고……"
    show mary smile with dissolve
    mary"이러면 안되는데……"
    edward"에드워드 라는 사람을 많이 좋아하셨는가보네요"
    mary"그땐 제가 \'사랑\'이 뭔지도 몰랐을 정도로 어렸을때라……"
    edward"그래도 사장님께 있어서 소중한 사람 임은 틀리지 않았죠?"
    show mary sad
    mary"…………"
    mary"네……"
    edward"그럼 울어도 괜찮다고 생각해요"
    show mary cry with dissolve
    mary"…………"
    show black with eyeshut
    "소중한 사람을 잃는다면 분명 슬프겠지"
    "……라고 머릿속으론 생각할 수 있었다."
    "하지만 나에겐 소중한 사람이 없다."
    "가족도, 친구도, 아무도……"
    "그렇기 때문에 난 사장님의 기분을 진정으로 이해하는 건 불가능하다."
    "고로, 내가 방금 한 말은 그저 입에 발린 소리에 불과하겠지……"
    "젠장"
    "지금와서 다시 생각해보니까……{cps=2} {/cps}사장님이 왜 울었는지 들어보지 말껄 그랬다."
    "에드워드 토머는 오리엔스 내에서 꽤 흔한 이름이기도 하고……"
    "동명인이 죽었다는 소식을 들으면, 왠지 내가 죽은 것 같은 기분이 들어서 그런가"
    "내 마음만 더 찝찝해졌다."
    stop music
    centered"얼마 후……"
    scene bg mary_office at Zoom((1280,720),(0,0,1280,720),(509,107,605,340),0.0) with eyeopen
    show mary:
        zoom 1.5 xalign 0.5 yalign -0.4
    mary"이제 정신이 좀 드는거 같네요"
    show mary smile
    mary"고맙습니다"
    edward"아니에요"
    show mary
    mary"그럼 이걸로 회사투어를 마치도록 할까요?"
    edward"네"
    scene black with Dissolve(1.0)
    "아직 특기가 확실하지 않았던 나는 신 제품의 아이디어를 떠오르는 일을 맡게 됐다."
    "그래도 한가지 다행인게─다들 나에 대해서 아무런 기대를하지 않고 있다는거다."
    stop music
    centered"오후 6시"
    play bgs "bgs/people.mp3"
    scene bg employee_office_night with moveright
    "시계가 6시를 가리키자 앉아있던 사람들은 자신의 짐을 싸면서 자리에서 일어나 작별 인사를 건네며 밖으로 나갔다."
    show mary smile
    mary"모두 수고했어요!"
    play sound "se/search_bag.mp3"
    scene bg employee_office_night at Zoom((1280,720),(0,0,1280,720),(195,323,706,397),1.0)
    $ renpy.pause (1.4)
    show bg employee_office_night at Zoom((1280,720),(195,323,706,397),(574,323,706,397),0.4)
    "나도 다른 사람들 처럼 챙겨온 짐을 들고 나가려고 했다."
    show mary shy:
        xalign -1.0 yalign -0.3 zoom 1.7
        linear 0.5 xalign 0.0
    "……그때 사장님께서 나를 붙잡으셨다."
    mary"자, 잠시만요!"
    "설마 내가 일하다가 뭔가 잘못한게 있었던걸까?"
    "나는 긴장하면서 대답했다."
    edward"무슨 일이시죠?"
    mary"그게……"
    mary"혹시 같이 퇴근해도 될까요?"
    edward"……?"
    "내가 예상했던 말과는 달라서 조금 놀랐다."
    "그래도 내가 뭔가 잘못한게 아니라서 정말 다행이다……"
    "근데 왜 나랑 같이 퇴근을 하자고 하는거지?"
    edward"네에……{cps=2} {/cps}전 상관 없어요"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    play bgs "bgs/wind.mp3"
    scene bg sidewalk_night with moveleft # 밤 거리
    show mary shy with dissolve:
        zoom 1.5 xalign 0.0 yalign -0.4
    "나와 슈테른 사장님은 밤길을 걸었다."
    "혹시 집 방향이 나랑 같은가?"
    "그때 사장님이 입을 여셨다."
    mary"그게……"
    mary"오늘 여러므로 추태를 보여드려서 죄송합니다……"
    edward"추태라니요?"
    mary"그러니까……"
    extend" 회사에서 울고……{cps=2} {/cps}그랬던거요……"
    "아……"
    "나랑 같이 퇴근을 하자는 것도, 이 것에 대해서─사람이 많은─사내에서 말 하고싶지 않아서 였던건가"
    play music "bgm/sad6.mp3"
    edward"전 아무렇지도 않아요"
    edward"오히려 소중한 사람을 잃으면 누구나 그런 반응을 보일거라 생각하는 걸요?"
    mary"소중한 사람이라……"
    play sound "se/search_bag.mp3"
    show mary with dissolve
    mary"확실히 저한테 소중했던 사람이었죠……"
    show mary smile
    mary"아까 회사에서도 그랬지만, 토머 씨는 정말 이해심이 깊은 사람이세요"
    edward"제가요?"
    show mary
    mary"네"
    show mary talk
    mary"오늘이 회사 첫날인 토머 씨를 꽤 혼란스럽게 만들었는데도……"
    mary"아무런 불만 없이 저를 위로해주시고……"
    edward"전 그냥 첫날부터 찍히는 건 별로 안 좋아해서……"
    edward"그, 그래서 사장님에게 잘 보이고 싶어서 했던 행동 일 뿐이에요!"
    edward"그러니까 제가 이해심이 깊거나 한건 아니니까……"
    show mary smile
    mary"후후후"
    mary"그런 마음가짐이면 분명 프로젝트 코넙적에 어울리는, 유능한 회사원이 되실 수 있을거예요"
    edward"다행이네요……"
    show mary shy with dissolve
    mary"그리고 또……"
    mary"밖에 있는 동안은 저보고 \'사장님\'이라고 부르지 말아주세요……"
    edward"네?"
    edward"그건 무슨 뜻이죠?{cps=2} {/cps}분명 노스탤지어 토이즈의 사장 이시라고……"
    show mary shy2
    mary"그, 그러니까요!"
    show mary shy
    mary"사장님 소리를 들으면 제가 너무……{cps=2} {/cps}늙어보인다고 해야 할까요?"
    mary"아직 26밖에 안 됐는데……"
    "26살?"
    "꽤나 젊다고 생각 했었는데……{cps=2} {/cps}26살……"
    "게다가 26이면 나랑 동갑이다!"
    "사장님이랑 친해질 수 있다면 좋겠는데……"
    "나는 사장님께 말 했다."
    edward"저, 저도 26살인데……{cps=2} {/cps}우연이네요……!"
    mary"그건 저도 이미 알고 있어요"
    mary"면접 서류에 토머 씨에 대한 기록이 전부 적혀 있었으니까요……"
    show mary smile
    mary"사실 어제 제가 토머 씨에게 프로젝트 코넙적 관련 말을 꺼낼 수 있었던것도─저랑 동갑이라 다른사람들보다 편하게 대할 수 있을것 같아서 그랬던거예요"
    edward"그랬군요"
    edward"근데 그럼 전 밖에서 사장님을 뭐라고 부르면 되는거죠?"
    edward"평범하게 \'슈테른 씨\' 라고 부르면 되나요?"
    show mary think
    mary"음……"
    show mary shy
    mary"도, 동갑이기도 하니까 편하게 말 놓는 건 어떤가요……?"
    "말을 놓는다……{cps=2} {/cps}즉, 편하게 반말을 하라는 뜻인가?!"
    "하지만 회사에서 나의 상관이고, 회사의 사장인데?"
    "어떤 반응을 보이는 게 좋을지, 머릿속이 매우 혼란스러웠다."
    "그런 혼란속에서 떠오른 단어는 이거 뿐이었다."
    edward"사, 사장님만 괜찮으시다면……{cps=2} {/cps}전 딱히……"
    show mary happy
    mary"……!"
    show mary smile
    mary"알았어,{cps=2} {/cps}에드워드"
    edward"…………"
    edward"그래……{cps=2} {/cps}슈테른……"
    show mary shock with dissolve:
        zoom 1.7 xalign 0.5
    mary"슈테른이 아니라, \'메리\'라고 이름으로 불러줄 순 없을까?"
    edward"네에?!"
    edward"그, 그래도 괜찮을련지요……"
    mary"말 놓기로 했잖아?"
    edward"음……"
    show mary
    edward"그, 그럼……"
    edward"메리……"
    show mary smile
    mary"응, 에드워드"
    mary"앞으로 나랑 친하게 지내줘"
    edward"그래……!"
    mary"내 집은 이쪽 방향이니까, 난 이만 가볼게!"
    show mary smile:
        linear 1.0 alpha 0.0
    play sound "se/footsteps_running.mp3"
    mary"내일 회사에서 만나자!"
    "그렇게 사장님……{cps=2} {/cps}아니, 메리는 내 시야에서 사라졌다."
    "이걸로 우린 친구사이가 된걸까?"
    "뭐가 뭔지 잘 모르겠다."
    "하지만, 한가지 확실한 건……"
    stop bgs
    stop music
    scene black
    extend" 오늘은 조금 즐거웠다."
    "오늘 아주머니께 쓸 편지의 내용이 늘었는 걸"
    ################################1958년 11월 5일 일기장 끝############################
    play music "bgm/smooth1.mp3"
    centered"오후 6시 5분"
    scene bg lib_night with memory
    "나는 다음장을 읽으려고 손으로 페이지를 넘기려는 찰나, 어디선가 맛있는 냄새가 났다."
    play sound "se/hungry.mp3"
    "……마침 배고픈 참이었는데 이렇게 맛있는 냄새라니"
    "일기장을 읽는데 집중이 될리가 없었다."
    play sound "se/footsteps_wood.mp3"
    "그래서 난 부엌으로 가서 무슨일이 있는지 살펴 보기로 했다."
    scene black with dissolve
    $ renpy.pause(1.5)
    play sound "se/door_open.ogg"
    $ renpy.pause(0.4)
    scene bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(20,260,600,340),0) with moveright
    play sound "se/hit.ogg"
    show seb shock with lshake:
        linear 0.1 zoom 1.8 yalign 1
    seb"아야!"
    "위에서 내려오다가 세바스찬이랑 머리를 부딪혔다."
    show seb shock at right:
        zoom 1.0
    show stephan shock at left
    stephan"괜찮아요?!"
    seb"네에……"
    seb"그냥 갑자기 튀어나와서 좀 놀랐어요"
    show seb at right
    seb"아,{cps=2} {/cps}그보다 저녁 식사가 완성 돼서 부르러 왔습니다!"
    show stephan smile at left
    stephan_think"역시 그 맛있는 냄새의 정체는 저녁이었군!"
    play sound "se/move.mp3"
    play bgs"bgs/eating.mp3"
    scene bg mansion_diningroom_night with moveleft # 식당
    play music "bgm/smooth4.mp3"
    "오늘 메뉴는 생선까스다!"
    "할아버지 께서는 방에서 드시고 있다고 한다."
    stephan"흐음……{cps=2} {/cps}잘먹겠습니다"
    "나는 자리에 앉아서 포크를 짚어 생선까스를 한 입 먹었다."
    show stephan smile with dissolve:
        zoom 1.4 yalign -0.2 xalign 0.0
    "어제도 그랬지만 세바스찬의 요리는 감탄사가 나올 정도로 맛이 좋았다."
    "내가 계속해서 생선까스를 입에 집어 넣기 시작하자 세바스찬은 만족스러운 미소를 보였다."
    stephan_think"패밀리 레스토랑에서 먹는것만 같은 맛이야!"
    show seb think at right with dissolve:
        zoom 1.4 yalign -0.2 xalign 1.0
    seb"저어……{cps=2} {/cps}도련님……"
    stephan"네?"
    "나는 입속에 음식이 가득 차있는 상태로 말했다."
    seb"좀 뜬금 없을수도 있겠지만……"
    show effect1
    play sound "se/shock.ogg"
    show seb blush
    seb"{size=45}앞으론, 저,{cps=2} {/cps}저에게도 말을 놓아 주셨으면 합니다!{/size}" with lshake
    hide effect1
    show stephan shock
    $ renpy.vibrate(0.3)
    stephan"쿨럭 쿨럭" with sshake
    stephan"네?!"
    stephan_think"너무 뜬금 없잖아?!"
    stephan"가,{cps=2} {/cps}갑자기 왜요……?"
    seb"음……"
    extend" 뭐랄까……"
    seb"시아 씨 한텐 편하게 대하면서 저한테만 존댓말을 사용하는 게 좀 그렇습니다!"
    stephan_think"\'좀 그렇다\'니……"
    "나는 고개를 시아의 쪽으로 돌렸다."
    scene bg mansion_diningroom_night with moveright #식당
    show cia smile:
        zoom 1.7 yalign -0.4
    "……아무 생각 없이 우걱우걱 먹고만 있었다."
    scene bg mansion_diningroom_night with moveleft #식당
    show stephan shock2:
        zoom 1.4 yalign -0.2 xalign 0.0
    show seb blush:
        zoom 1.4 yalign -0.2 xalign 1.0
    stephan"으,{cps=2} {/cps}응……"
    extend" 그럼 앞으론 세바스찬 이라고 부르면 되는 건 감……?"
    show seb
    seb"네!"
    "세바스찬은 매우 기쁜 미소를 지었다."
    show stephan shock
    stephan_think"그렇게 까지 시아랑 함께 있고 싶었던거냐;;"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg mansion_diningroom_night with moveright #식당 배경
    show cia think:
        zoom 1.4 yalign -0.5 xalign 1.0
    show seb:
        zoom 1.4 yalign -0.2 xalign 0.0
    cia"근데 세바스찬 씨는 어떻게 해서 이렇게 맛있게 만들었어요?"
    seb"그,{cps=2} {/cps}그런가요?"
    show cia
    cia"정말 맛있는 걸요!"
    cia"저도 언제면 이렇게 맛있게 만들 수 있을까요……"
    seb"한 20년 정도 걸리려나요?"
    show cia mad
    show effect1
    play sound "se/shock.ogg"
    cia"{size=45}네?!{/size}" with lshake
    hide effect1
    show seb shock
    seb"자,{cps=2} {/cps}장난 입니다!"
    hide cia mad
    show stephan talk:
        xalign -1.5 yalign -0.2 zoom 1.4
        linear 0.4 xalign 0.0
    show seb:
        linear 0.4 xalign 1.0
    stephan"왜?{cps=2} {/cps}혹시 시아가 요리를 못한다든가……"
    seb"그,{cps=2} {/cps}그럴리가요!"
    seb"아직 공부 중 이긴 하지만, 그래도 가능성은 있어요"
    show seb talk:
        linear 0.3 xalign 0.5
    seb"{size=20}……정말로 있을진 몰라요{/size}"
    show stephan shock
    show seb:
        linear 0.3 xalign 1.0
    stephan"…………"
    hide stephan shock
    show seb:
        linear 0.3 xalign 0.0
    show cia:
        zoom 1.4 xalign 1.5 yalign -0.3
        linear 0.3 xalign 1.0
    cia"그렇쵸?{cps=2} {/cps}저도 언젠간 세바스찬 씨 처럼 요리를 잘 할 수 있겠죠?!"
    seb"네에!"
    scene bg mansion_diningroom_night # 식당 배경
    show stephan shock2:
        zoom 1.4 xalign 0.5 yalign -0.2
    stephan"하……{cps=2} {/cps}하……{cps=2} {/cps}하……"
    play music "se/phone_ring.mp3"
    "내가 생선까스를 계속 먹던 중 주머니 쪽에서 폰 울림이 들려 왔다."
    "나는 주머니에서 폰을 꺼내서 확인했다."
    stephan_think"왠일로 \'윌리\'한테서 연락이 왔네?"
    stephan"잠시 실례 하겠습니다"
    show stephan talk:
        linear 1.0 xalign 1.8
    stop bgs
    play sound "se/footsteps_wood.mp3"
    scene black with moveright
    $ renpy.pause(2)
    scene bg mansion_hall at Zoom((1280,720),(539,273,646,363),(539,273,646,363),0.0) with moveright # 거실
    stop music
    show stephan talk
    stephan"여보세요?"
    play sound "se/shock.ogg"
    willy"{size=45}스테반?!{/size}" with lshake
    show stephan shock
    stephan"머,{cps=2} {/cps}뭐야 갑자기 소리를 지르고……"
    willy"미안……{cps=2} {/cps}그냥 이런저런 생각이 들어서……"
    willy"너 혹시 이상한 문자 같은거 받은 적 있어?"
    show stephan talk
    stephan"이상한 문자?"
    extend" 무슨 \'포겟몬스터 시간의 탐험대\' 인가?"
    willy"후우─{cps=2} {/cps}안 받았다면 됐어"
    willy"그럼 끊는다"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}그걸로 끝?!{/size}" with lshake
    hide effect1
    willy"왜?"
    stephan"아니, 네가 일방적으로 묻고 끊는거냐고?!"
    willy"그냥 궁금해서 물어본 거 뿐이니까"
    stephan"음……{cps=2} {/cps}종나 제멋대로네"
    stop music
    willy"지금 장난 칠 기분 아니야"
    show stephan talk
    stephan"무슨 일 있어?"
    willy"오늘 내 주변 사람들이 이상한 내용의 문자를 받았다고 말 해서"
    stephan"도대체 어떤 내용 이길래?"
    willy"잠깐만……{cps=2} {/cps}내용이 좀 길어서 문자로 보내야 될 거 같아"
    willy"…………"
    "수화기 너머론 잡음이랑 타자 치는 소리가 들렸다."
    play sound "se/phone_text.mp3"
    stephan_think"문자가 왔군……"
    willy"방금 보냈으니까 확인 해봐"
    stephan"잠깐만……"
    hide stephan talk
    show phone with dissolve:
        xalign 0.5 yalign 0.5
        linear 0.6 zoom 1.8
    "나는 통화중에 홈 버튼을 눌러서 메인 화면으로 넘어 온 뒤, 윌리가 보낸 문자를 확인 했다."
    nvl clear
    narrator_nvl"\'.. / .—— .. .—.. .—.. / —.— .. .—.. .—.. / —.—— ——— ..—\'"
    nvl clear
    show phone:
        linear 0.6 zoom 0.5
    $ renpy.pause(0.6)
    hide phone
    show stephan shock with dissolve
    stephan"확실히 이상한 문자 이긴 하지만 그냥 \'점(.)\'과 \'다시(—)\'로만 이루어진거 잖아"
    stephan"이상한 내용이라고 하기엔 뭐랄까……"
    show stephan shock2
    extend" \'내용\'이 없다 랄까?"
    stephan"…………"
    willy"아까전에 내가 진지하다고 말 했잖아……"
    willy"어쨌건, 방금 내가 보낸 문자는 \'모스 부호(Morse Code)\'야"
    show stephan shock
    stephan"혹시 해석 할 줄 아는 건 아니겠지……?"
    willy"어"
    willy"\'..\'은 대문자 I 니까……"
    stop music
    willy"해석하면 대충\'I Will Kill You\'가 되겠네……"
    stephan"…………"
    "나는 윌리가 머릿속으로 모스 부호를 해석 한 것도 놀라웠지만……"
    "그보단 정체 불명의 누군가가 윌리의 주변 인물 들에게 살인 예고 비슷한 메세지 까지 남길 정도로 대담함에 놀랐다."
    willy"흠……{cps=2} {/cps}잠깐만……"
    play music "bgm/sirius1.mp3"
    willy"스테반, 혹시 날 좀 도와줄 수 있어?"
    show stephan talk
    stephan"내가 도움이 될 수 있으려나?"
    willy"그냥 간단 한 거야"
    willy"며칠 전 부터 나한테 계속 이상한 일이 발생 했거든"
    willy"집에 들어오면 정리 해 뒀을 침대 커버가 엉망이고, 길을 걸을때 마다 누군가 뒤에서 따라 다니는 느낌도 들고……"
    willy"언제는 내 칫솔 까지도 사라졌다니까?!"
    show stephan shock
    stephan"완전 스토커의 짓이네……"
    willy"나도 그렇게 생각하고 있어"
    willy"범인이 어떤 사람인지 알 것 같기도 하고……"
    show stephan talk
    stephan"그정도면 그냥 경찰에 신고해보는 게 어때?"
    willy"스토커가 날 따라 다니고 있다고 하기엔 증거가 너무 없고, 절도 사건으로 입건 시켜버리기엔 도난 당한 물건의 가치가 너무 적어"
    stephan_think"도와줄 수 있는 사람이 나밖에 없다는 건가……"
    show stephan smile2
    stephan_think"후훗"
    if pick_game == True:
        willy"그보다 너 아직까지도 할아버지 댁에 있어?"
        show stephan shock
        stephan"그걸 어떻게……?!"
        willy"오늘 점심때 상점 거리에서 말해줬잖아"
        show stephan talk
        stephan"아……{cps=2} {/cps}생각 해보니까 그랬었지……"
    if pick_game == False:
        willy"지금 집에 있어?"
        stephan"아니,{cps=2} {/cps}지금 할아버지 댁에 있어"
    willy"혹시 네 집에서 자도 될까?"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}우리 집에서?!{/size}" with lshake
    hide effect1
    willy"안되나?"
    stephan_think"나한테 도움을 요청한게 이거였냐?"
    "나는 혼자서 살고 있기 때문에 딱히 문제가 되는 건 아니다."
    "거기다 상대방에게 스토커가 있다는 듯 하기도 하고……"
    stephan"상관은 없다만……"
    stephan"내일 학교는?"
    willy"같이 등교 하지 뭐"
    stephan"그래……"
    willy"그럼 준비 하고 출발 할게"
    play sound "se/phone_end.mp3"
    $ renpy.pause(2)
    "나는 폰을 끊고 다시 식사를 하러 돌아갔다."
    play sound "se/move.mp3"
    scene black with moveleft
    play music "bgm/beat2.mp3"
    centered"오후 7시 50분"
    centered"스테반 집"
    play sound "se/door_open.ogg"
    scene bg room_stephan_night with dissolve
    show stephan:
        xalign 0.25 yalign 1.0
    show willy talk:
        xalign 0.75 yalign 1.0
    stephan"어서와~{cps=2} {/cps}우리집은 처음이지?"
    willy"중학교때 한 번 온 적 있었으니까 처음은 아니지"
    stephan"뭐어 매일매일이 새로운거지"
    show willy
    willy"좋은 마음 가짐이네"
    stephan"같이 PX4게임 할래?"
    show willy talk
    willy"컨트롤러 2개 있어?"
    show stephan shock
    stephan"아……"
    show willy
    willy"난 그냥 네가 하는거 볼게"
    willy"혹시 하다가 막히면 번갈아 가면서 하지"
    show stephan
    stephan"그래"
    show stephan talk
    stephan"그럼 먼저 PX4 계정을 초기화 하고……"
    "정말 윌리가 스토커에게 쫓기고 있다는 게 믿겨지지 않을 정도로 태평하게 놀고 있었다."
    show willy talk
    willy"맞다.{cps=2} {/cps}혹시 나 휴대폰 좀 충전 해도 괜찮을까?"
    stephan"내껀 \'아이퐁(iPhong)\'이라서 충전 단자 안 맞을걸?"
    show willy
    willy"내껀 내가 가져 왔으니까 걱정 마"
    play sound "se/move.mp3"
    scene black with moveright
    "우리는 내일 학교 간다는 사실을 까막히 잊은채, 게임에 몰두했다."
    stop music
    centered"2014년 9월 15일 월요일"
    centered"오전 7시 50분"
    play sound "se/alarm.wav"
    $ renpy.vibrate(1)
    $ renpy.pause(4)
    stop sound
    play music "bgm/beat1.mp3"
    scene white with eyeopen
    $ renpy.pause(0.5)
    scene bg room_stephan_day at Zoom((1280,720),(668,291,612,344),(668,291,612,344),0.0) with dissolve
    show stephan yawn:
        zoom 1.4 yalign -0.2 xalign 1.0
    stephan"후아아암~"
    stephan"지금……{cps=2} {/cps}몇 시……?"
    show willy talk:
        xalign -0.1 yalign 1.0
    willy"7시 50분……{cps=2} {/cps}이제 막 51분 됐어"
    scene bg room_stephan_day at Zoom((1280,720),(668,291,612,344),(0,0,1280,720),0.3) with dissolve
    show effect1
    play sound "se/shock.ogg"
    show stephan shock
    stephan"{size=45}히익!!{/size}" with lshake
    stephan"지각 하겠어!!"
    hide effect1
    willy"밤새서 게임하자고 한 건 너다"
    willy"어떻게 보면 자업자득 이네"
    stephan"넌 좀 닥쳐!"
    stephan"그보다 너도 나랑 같이 밤새서 게임했잖아, 왜 너만 멀쩡한거야?!"
    play sound "se/search_bag.mp3"
    show willy talk:
        xalign -1.0 yalign 1.0
        linear 1.0 xalign 0.0
    willy"그야 난 잠을 안 잤으니까"
    stephan"안 잤다고?!"
    stephan"왜 잠을 안자?"
    willy"그보다 빨리 가는 게 좋지 않을까?"
    stephan"맞다!!"
    play sound "se/footsteps_running.mp3"
    scene black with moveleft
    $ renpy.pause(1)
    play sound "se/door_open.ogg"
    $ renpy.pause(1)
    ####################################이대로 엔 크라운의 시점으로 짧게 플레이 시작
    play music "bgm/happy2.mp3"
    centered"4일 전"
    centered"9월 11일 목요일"
    scene bg school_classroom with memory
    centered"2학년 7반 교실"
    show anne with dissolve:
        zoom 1.4 yalign -0.25
    nvl clear
    narrator_nvl"제 이름은 \'앤 크라운(Anne Crown)\' 이라고 합니다."
    narrator_nvl"음……{cps=2} {/cps}취미는 관찰 입니다."
    narrator_nvl"주로 동물, 곤충 같은 생물이나 주변인 들이 하는 행동을 관찰합니다."
    narrator_nvl"그 외에 조사 하는것도 특기 입니다."
    narrator_nvl"궁금한게 있으면 인터넷을 통해서 검색을 하거나 직접 조사 해보거나……"
    nvl clear
    narrator_nvl"에헴,{cps=2} {/cps}제 취미에 대한 이야기는 이쯤 해두고"
    narrator_nvl"저의 학교 생활에 대해서 한번 알려 드리겠습니다."
    narrator_nvl"저는 현재 고등학교 2학년생 입니다."
    narrator_nvl"그리고 여기는 2학년 7반입니다."
    willy"{size=25}빨리 안오면 놔두고 간다!{/size}"
    show anne think
    anne_think"어?{cps=2} {/cps}이 목소리는?"
    anne_think"복도 쪽에서 들린거 같았는데……"
    show anne:
        linear 0.6 xalign 1.6
    play sound "se/move.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(219,137,823,463),1.0) with moveleft
    play bgs "bgs/people.mp3"
    show stephan shock at left
    stephan"이 새꺄!"
    stephan"내 가방들고 튀지 마!"
    show willy smile2 at right
    willy"너도 운동 좀 해봐"
    "윌리는 토머의 가방을 들고 복도를 달리고 있었다."
    anne_think"힉!{cps=2} {/cps}윌리다!"
    hide stephan shock
    show willy at right:
        linear 1.0 xalign 0.5
    nvl clear
    narrator_nvl"저 사람의 이름은 \'윌리 제임스\' 라고 합니다."
    narrator_nvl"같은 학년 3반 이죠"
    narrator_nvl"그는 공부도 잘 하고, 운동도 그럭저럭 잘 하고, 말도 잘 하고"
    narrator_nvl"인기도 많고……"
    narrator_nvl"그리고 엄청나게 착합니다."
    narrator_nvl"다만……{cps=2} {/cps}거의 모두 에게 친절을 베푼다는 게 조금 흠이죠……"
    show willy:
        linear 1.5 xalign 0.5 yalign 1 zoom 2
    anne_think"어,{cps=2} {/cps}윌리가 점점 이쪽으로 다가온다!"
    play sound "se/hit.ogg"
    scene bg school_hall at Zoom((1280,720),(219,137,823,463),(0,0,1280,720),0.5) with dissolve
    show willy shock
    willy"아야―"
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(580,218,700,394),0.0)
    show willy shock:
        zoom 1.3 yalign -0.1 xalign 1.0
    show anne think:
        yalign -3.3 xalign 0.0 zoom 1.3
    anne"으―"
    "스테반만 보면서 복도를 달리다 보니 결국 윌리는 교실 안에서 복도를 빼꼼이 바라보던 나와 부딪혀 버렸다."
    show willy talk
    willy"엇!"
    willy"괜찮아?"
    willy"정말 미안……"
    show effect1
    play sound "se/shock.ogg"
    show anne shock
    anne"{size=45}아,{cps=2} {/cps}아니에요!!{/size}" with lshake
    hide effect1
    anne"전 괜찮아요……"
    show anne shock2
    anne_think"으아……{cps=2} {/cps}윌리가 이렇게까지 가까이 있다니……!"
    show willy talk:
        linear 0.7 xalign 0.5
    willy"정말 괜찮은거 맞아?"
    "윌리는 나에게 얼굴을 가까이 했다."
    willy"지금 얼굴이 빨간데?"
    anne"전 괜찮아요!!"
    show willy:
        linear 0.4 xalign 1.0
    willy"넌 분명히……{cps=2} {/cps}7반에 앤 크라운 이었지?"
    anne"저를 기억해 주시다니……!"
    willy"중학교 2학년 때도 같은 반 이었던 적이 있었는데"
    willy"당연히 기억하지"
    show willy shock
    willy"그보다 며칠 전에도 만났었잖아"
    hide anne shock2
    show stephan talk:
        zoom 1.3 yalign -0.1 xalign 0.0
    stephan"어이,{cps=2} {/cps}내 가방 내놔"
    willy"어,{cps=2} {/cps}어―"
    hide stephan
    show anne shy:
        yalign -3.3 xalign 0.0 zoom 1.3
    show willy
    willy"그럼 나중에 보자"
    anne"ㄴ, 네!!"
    play sound "se/footsteps_running.mp3"
    show willy:
        linear 0.5 xalign 1.7
    $ renpy.pause(0.5)
    show stephan shock:
        zoom 1.3 yalign -0.1 xalign 1.0
    stephan"아니, 튀지 말라니까!"
    show stephan shock:
        linear 0.5 xalign 1.7
    anne_think"하아~{cps=2} {/cps}윌리랑 같이 있으면 너무 부끄러워서 말을 걸기가 힘들어……"
    hide stephan shock
    hide willy
    nvl clear
    narrator_nvl"그렇습니다……{cps=2} {/cps}저는 윌리를 좋아합니다."
    narrator_nvl"제가 그를 처음 좋아 하게 된건 중학교 2학년때……"
    narrator_nvl"성격 탓에 친구도 별로 없었던 저에게……{cps=2} {/cps}이 넓은 세상에 혼자가 아니라는 걸 알려준 존재였어요."
    narrator_nvl"그것을 시작으로 점점 더 빠지기 시작 했다고 해야 할까……"
    narrator_nvl"하지만 그런 윌리가 중학교 3학년이 됐을 때 전학을 간다는 소식에 정말 슬퍼했어요."
    narrator_nvl"그런데 이렇게 같은 고등학교를 다니게 되다니……"
    narrator_nvl"정말로 운명 같았습니다."
    show anne shock2:
        linear 0.6 xalign 0.5
    anne_think"하아……{cps=2} {/cps}윌리랑……{cps=2} {/cps}접촉 했어……"
    "이런 식으로 나는 혼자서 몇 분간 계속 망상에 빠져 있었다."
    play sound "se/school.mp3"
    $ renpy.pause(3)
    show anne shock
    anne_think"앗,{cps=2} {/cps}벌써 시작 종이 쳐버렸잖아!"
    anne_think"빨리 들어가야겠다"
    play sound "se/move.mp3"
    scene black with moveright
    centered"점심 시간"
    scene bg school_cafe with moveright
    centered"급식소"
    show anne at left
    show lisa at right
    $ lisa_name = '리사 보우만'
    lisa"저기 자리 비어있다!"
    anne"어……"
    scene bg school_cafe at Zoom((1280,720),(0,0,1280,720),(542,314,690,388),1.0) with dissolve
    $ renpy.pause(1.0)
    show lisa with dissolve:
        zoom 1.4 yalign -0.2 xalign 0.5
    nvl clear
    narrator_nvl"이 아이의 이름은 \'리사 보우만(Lisa Bowman)\'"
    narrator_nvl"정말 밝고, 착하고, 재밌고, 적극적인 아이 입니다."
    narrator_nvl"게다가 축구부에서 활동하는 등, 운동 신경도 매우 빼어나죠"
    narrator_nvl"그리고 저랑은 정 반대의 성격을 지녔죠……"
    narrator_nvl"제 마음을 그대로 털 수 있는 몇 안 되는 친한 친구중 한명 입니다."
    narrator_nvl"저희 둘의 만남은 딱히 특별하거나 하진 않았어요."
    narrator_nvl"그저 제가 고등학교에 올라오고 나서 처음으로 말을 걸어준게 리사 였을 뿐이었으니까요."
    narrator_nvl"하지만 저의 내성적인 성격 탓에 다른 사람이랑 말을 섞는 게 힘들었던 걸 생각해보면……"
    narrator_nvl"리사는 저에게 있어서 정말로 소중한 친구임은 사실이에요."
    anne_think"역시 리사에게 말 하는 게 좋겠지……?"
    scene bg school_cafe at Zoom((1280,720),(542,314,690,388),(548,398,521,293),0.0) with moveup
    show lisa:
        zoom 1.4 xalign 0.8 yalign -0.2
    show anne:
        zoom 1.3 xalign 0.2 yalign -3.3
    anne"저기……{cps=2} {/cps}리사……"
    show lisa talk
    lisa"응?{cps=2} {/cps}왜?"
    anne"혹시 내 고민좀 들어줄 수 있어?"
    show lisa think
    lisa"고민?!{cps=2} {/cps}너한테도 고민이 있었어?!"
    show anne shy
    anne"나,{cps=2} {/cps}나도 사람인데 당연히 고민이 있지!"
    show lisa smile2
    lisa"장난이야 장난"
    lisa"그래서 고민이 뭔데?"
    lisa"목소리가 너무 작은거?{cps=2} {/cps}가슴이 너무 작은거?{cps=2} {/cps}아니면 가끔 말을 더듬는거?"
    show effect1
    show anne shock
    play sound "se/shock.ogg"
    anne"{size=45}그,{cps=2} {/cps}그중 이상한게 섞여있잖아!!{/size}" with lshake
    hide effect1
    lisa"에이 에이{cps=2} {/cps}우리 사이에 뭘"
    lisa"다 알고 있는 사실 이라구"
    show anne
    anne"저,{cps=2} {/cps}정말……?"
    show anne think
    anne"아니,{cps=2} {/cps}그보다 내가 가지고 있는 고민은 그런게 아니야!"
    show lisa
    lisa"그럼 뭔데?"
    show anne shy
    anne"{size=20}사랑……{cps=2} {/cps}하는 사람이……{/size}"
    show lisa talk
    lisa"어?{cps=2} {/cps}좀더 크게 말해봐"
    anne"사랑……{cps=2} {/cps}하는 사람이 있어……"
    show lisa shy
    lisa"사,{cps=2} {/cps}사랑?!"
    lisa"네가 사랑하는 사람이 있다고?!"
    anne"어……"
    lisa"우와……"
    anne"그거……{cps=2} {/cps}감탄할 일이야……?"
    lisa"그냥……{cps=2} {/cps}뭐랄까……"
    lisa"내가 아는 넌 언제나 작고 귀엽고 순한 소심쟁이 인줄로만 알았는데"
    lisa"그런 너도 사랑 이라는 걸 하는구나 싶어서"
    anne"내가 그런 이미지였어?!"
    show lisa talk
    lisa"조금……?"
    show lisa
    lisa"그보다 네가 좋아하는 상대는 누구야?"
    show anne shock2
    anne"으……"
    anne_think"생각 하는것 만으로도 부끄러워……"
    show lisa talk:
        linear 0.6 xalign 0.5
    lisa"여보세요~?"
    show anne shock
    anne"히익!"
    show lisa shock
    lisa"왜 그렇게 놀래는거야;;"
    show lisa talk:
        linear 0.5 xalign 0.8
    lisa"아니, 그보다 얼굴은 또 왜이리 붉어?"
    anne"이,{cps=2} {/cps}이건!"
    show lisa smile2
    lisa"혹시 생각하는것 만으로도 부끄러운거야?"
    anne"그,{cps=2} {/cps}그럴리가……"
    lisa"이거~{cps=2} {/cps}도대체 누구길래 우리 앤을 홀딱 빠지게 만든걸까~?"
    show anne shy
    anne"(꿀꺽)"
    anne"위,{cps=2} {/cps}윌리……"
    show lisa shock
    show effect1
    play sound "se/shock.ogg"
    lisa"{size=45}윌리―?!{/size}" with lshake
    lisa"윌리라면 3반에 있는 윌리-윌리?!"
    hide effect1
    show anne
    anne"윌리-윌리?!"
    anne_think"윌리에게 내가 모르는 별명이 있었어?"
    anne"호,{cps=2} {/cps}혹시 둘이 친 한 사이야?!"
    show lisa
    lisa"딱히 친한건 아니고,{cps=2} {/cps}그냥 걔가 가끔 축구부에 놀러오니까"
    show lisa smile2
    lisa"이야~{cps=2} {/cps}실력이 어찌나 좋던지~"
    show lisa
    lisa"그래도 내 실력으로 걔 슛은 막을 수 있었다고!"
    anne"으,{cps=2} {/cps}응―"
    lisa"그 폭풍같은 실력 때문에 축구부에선 걜 윌리-윌리 라고 불러"
    anne_think"즉, 윌리-윌리의 뜻이 태풍의 호주식 이름인 윌리-윌리(Willy—Willy)를 뜻하는 거 였구나아……"
    lisa"이야~"
    extend" 그나저나 참 힘든 상대를 골랐네"
    anne"힘들다니?"
    anne"축구 얘기?"
    lisa"아니, 그런게 아니고, 걔 인기 엄청 많잖아"
    lisa"공부도 잘하고, 키도 크고, 운동도 나보단 아니지만 잘 하고, 말도 잘하고, 얼굴도 나쁘지 않고, 돈도 많다는거 같던데……"
    lisa"걜 탐하는 사람들이 얼마나 많은지 알아?"
    show lisa smile2
    lisa"근데 본인은 딱히 연애에 흥미가 없는거 같고"
    show anne shock
    anne"저,{cps=2} {/cps}정말?!"
    anne"어쩌지……"
    nvl clear
    narrator_nvl"하지만 예상하지 않았던 건 아닙니다."
    narrator_nvl"말했다시피 윌리는 거의 모든 사람들에게 친절하니까……"
    narrator_nvl"인기가 많은것도 당연하다면 당연하겠죠……"
    narrator_nvl"그래도 전 윌리의 옆에 있는것 만으로 만족하니까!"
    lisa"그냥 포기 해"
    lisa"그런 놈은 분명히 바람둥이 일거야"
    show anne
    anne"{size=20}너도……{cps=2} {/cps}그런 말을……{/size}"
    lisa"…………"
    show lisa shy
    lisa"아까 그거 개그였는데……"
    anne"응?!"
    lisa"별명이 윌리-윌리니까"
    extend", 윌리-윌리는 태풍의 호주식 명칭이고……"
    lisa"그래서 윌리가 \'바람\'둥이 라는……"
    show lisa shock
    show effect1
    play sound "se/shock.ogg"
    lisa"재,{cps=2} {/cps}재미 없었지?!" with lshake
    hide effect1
    show anne think
    anne"아니!{cps=2} {/cps}너무 어려워서 이해를 못 했던 거야!!"
    nvl clear
    narrator_nvl"리사는 개그—주로 개드립—을 엄청나게 좋아합니다."
    narrator_nvl"다만 웃기지 않을때가 많은 게 흠일 뿐……"
    narrator_nvl"그,{cps=2} {/cps}그래도 웃길때도 있긴 있습니다!"
    show lisa talk
    lisa"그런데 넌 그렇게 까지 윌리-윌리가 좋은거야?"
    show anne
    anne"응?"
    show lisa smile2
    lisa"너 방금 전에 모습이 완전히 \'내 윌리가 이렇게 바람둥이 일리가 없어!\'"
    lisa"……하는 반응 이었거든"
    anne"그,{cps=2} {/cps}그래?"
    show lisa talk
    lisa"이거 이거……"
    show lisa
    lisa"그럼 이 \'연애 박사\'리사 에게 맡겨만 줘!"
    anne"여,{cps=2} {/cps}연애에도 박사 학위가 있었어……?"
    show lisa shock
    lisa"그냥 말이 그렇다는 거지……"
    show lisa
    lisa"어쨌건! 내가 어떻게 하면 윌리-윌리를 손에 넣을 수 있을지 알려줄게!"
    anne"저,{cps=2} {/cps}정말?!"
    lisa"음!{cps=2} {/cps}나만 믿어!"
    lisa"먼저 가장 중요한 건 바로 자신을 어필하는거야!"
    show anne shy
    anne"어필?"
    anne"어떻게 어필을 하지……"
    lisa"어필을 할 수 있는 기회를 만드는 것 부터 시작을 하면 돼!"
    anne"그건 어,{cps=2} {/cps}어떻게 만들어?"
    show lisa smile2
    lisa"{size=45}데{cps=2}.{/cps}이{cps=2}.{/cps}트{/size}"
    lisa"……밖에 없잖냐"
    anne"…………"
    show anne shock
    anne_think"데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?! 데이트라니?!"
    anne_think"너무 갑작스러워!"
    show anne shock2
    anne_think"하지만……{cps=2} {/cps}그렇게 하면 윌리랑 좀 더 가까이 있을 수 있을지도 몰라……"
    show anne shy
    anne"내가 할 수 있을까……"
    lisa"자신감을 가지라고!!"
    show lisa
    lisa"넌 잘 모르겠지만, 네가 얼마나 귀여운지 알아?!"
    lisa"굳이 윌리-윌리가 로리콘이 아니라도 너의 귀염성을 보면 조금은 심쿵 할 걸?"
    show effect1
    play sound "se/shock.ogg"
    show anne shock2
    anne"{size=45}내내내내내가 귀엽다고?!{/size}" with lshake
    hide effect1
    show lisa smile2
    lisa"그래, 너의 그런 반응이 가장 귀여워"
    show anne
    anne"근데 리사, 로리콘이 뭐야?"
    show lisa talk
    lisa"나도 정의는 몰라.{cps=2} {/cps}그냥 우리 오빠가 귀여운 여자를 좋아하는 사람을 로리콘이라 부른데"
    show lisa smile2
    lisa"네가 딱 그런 사람들이 좋아할만한 스타일이니까  자신감을 가지고 데이트를 신청해봐!"
    lisa"눈을 크게 뜨고, 윌리를 올려다 보면서……"
    show lisa shy
    lisa"\'오,{cps=2} {/cps}오빠……{cps=2} {/cps}같이 데이트 해줄 수 있어?\'라고 하면……"
    show lisa smile2
    show anne think
    anne"크흑!" with sshake
    "너무 당황해서 입에 넣으려고 했던 음식을 도로 뱉어버렸다."
    show effect1
    play sound "se/shock.ogg"
    show anne shock
    anne"{size=45}그,{cps=2} {/cps}그런 남사스러운 일을 내가 어떻게 하냐고!!{/size}" with lshake
    hide effect1
    lisa"이런 반응도 귀여운데?"
    anne"그리고 내가 윌리보다 생일이 빠르니까……"
    anne"오,{cps=2} {/cps}오빠 라고 부르는 건……"
    show lisa think
    lisa"그럼 \'얘야,{cps=2} {/cps}이 누나랑 같이 어른의 세계를……\'"
    anne"리사도 참……{cps=2} {/cps}그만 놀려. 난 진지하단 말이야……"
    stop music
    show lisa
    lisa"나도 진지해!{cps=2} {/cps}지금 먹고 있는 걸!"
    show anne
    anne"…………"
    anne_think"이,{cps=2} {/cps}이번 개그는 정말 너무했다……"
    "리사의 가장 큰 단점……{cps=2} {/cps}개그가 재미 없을땐 진짜 재미가 없다……"
    play music "bgm/beat3.mp3"
    scene bg school_hall with movedown
    centered"오후 12시 44분"
    centered"2학년 3반 교실 앞"
    "여차저차 해서 내가 윌리에게 데이트를 신청하는 꼴이 되어버렸다."
    "솔직히 전혀 자신 없는데……"
    show bg school_hall at Zoom((1280,720),(0,0,1280,720),(211,212,609,342),0.6)
    "나는 작전(?)을 진행 하기 위해 3반 교실 안을 빼꼼히 바라봤다."
    "하지만 안엔 윌리가 없었다."
    show anne think:
        yalign 1.0 xalign 0.3
    anne_think"이거 참……{cps=2} {/cps}윌리는 언제쯤 올까……"
    show lisa smile:
        xalign 2.5 yalign 1.0
        linear 1.0 xalign 0.7
    play sound "se/footsteps_concrete.mp3"
    lisa"룰루랄라~♩"
    "리사가 화장실에서 콧노래를 부르며 걸어나고 있었다."
    show lisa
    lisa"윌리-윌리는?"
    show anne
    anne"아직……"
    lisa"혹시 밖에서 축구라도 하고있는거 아니야?"
    anne"그럴수도 있어……"
    show lisa talk
    lisa"근데 넌 걔 앞에 서면 제대로 말이나 할 수 있어?"
    anne"…………"
    show anne shock
    anne_think"새,{cps=2} {/cps}생각해보니까!"
    anne_think"막상 윌리를 만나도, 제대로 말을 못 꺼내면 의미가 없잖아!!"
    lisa"그 표정을 보아 하니 노답인가 보네……"
    show lisa think
    lisa"이거 어쩌지……"
    show anne shy
    anne"끙……"
    anne"뭔가 좋은 방법이……"
    "내가 윌리 앞에 설 필요 없이 나의 마음을 전할 수 있는 방법……"
    "그런 꿈만 같은 방법이 있었으면 정말 좋겠다고 생각했다."
    show anne think
    anne"음……"
    show anne
    extend" 편지……{cps=2} {/cps} 는 어떨까?"
    show lisa smile2
    lisa"편지?!"
    lisa"너무 유치하지 않냐?"
    show anne shy
    anne"그,{cps=2} {/cps}그런가?!"
    anne"하지만 그거 외엔 떠오르는 게 없는 걸……"
    show lisa talk
    lisa"믿져야본전 인건가……"
    show lisa smile
    lisa"한번 해보자!"
    play sound "se/move.mp3"
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(268,238,682,384),1.0) with moveleft
    centered"7반 교실"
    show anne:
        zoom 1.3 xalign 0.8 yalign -3.3
    show lisa:
        zoom 1.4 yalign -0.2 xalign 0.2
    anne"한 번 써본건데……"
    extend" 어때?"
    play sound "se/search_bag.mp3"
    "나는 리사에게 내가 쓴 편지를 건네 주면서 말했다."
    nvl clear
    narrator_nvl"\'저는 언제나 부끄러워 하며 당신을 옆에서 항상 지켜보고 있었습니다."
    narrator_nvl"저의 용기가 부족하여 이렇게 편지로 말을 전합니다."
    narrator_nvl"저는 예전부터 당신을 정말 좋아했습니다."
    narrator_nvl"하지만 이번엔 용기 내어 저의 마음을 고백 하려고 합니다."
    narrator_nvl"그러니……{cps=2} {/cps}방과 후 에 학교 뒷편에서 당신을 기다리고 있겠습니다.\'"
    show lisa think
    lisa"흠……"
    show lisa shock
    lisa"너 글 쓰는 재주 진짜 없구나"
    show anne shock
    anne"저,{cps=2} {/cps}정말?!"
    lisa"먼저 문장의 끝이 전부 \'다.\'고"
    lisa"또 너무 짧은 감이 든다고 해야할까?"
    lisa"그냥 정성이 부족해 보여"
    anne"생각보다 잘 알고 있네……?"
    show lisa smile
    lisa"훗, \'팬픽(팬 픽션)\', \'인소(인터넷 소설)\', \'동인지(同人誌)\' 경력만 4년 이라구?!"
    anne_think"생각해보니까 리사가 국어에 강했지……"
    show lisa shock
    lisa"아, 근데 내가 딱히 부녀자 이거 한 건 아니니까 오해 하지는 마!"
    anne"아무도 그런 소리는 하지 않았어"
    anne"그,{cps=2} {/cps}근데 너라면 어떻게 썼을거야?"
    show lisa smile
    lisa"나라면 편지 안 쓰고 바로 달려가 고백 해버리지"
    show anne think
    anne"{size=20}확실히 너라면……{/size}"
    lisa"그래서 이 편지는 어떻게 줄거?"
    show anne
    anne"보통은 신발장이나 락커 안에다가 넣지 않나?"
    show lisa think
    lisa"우리 학교의 구조상 신발장은 힘들거 같고……"
    show lisa smile
    lisa"역시 락커 겠네!"
    anne"근데 락커는 자물쇠로 잠겨 있어서 쉽게 열지 못할텐데……"
    lisa"그거라면 걱정 마!"
    lisa"그 왜!{cps=2} {/cps}락커 문 앞에보면 환풍구 비슷한 넙적한 구멍 같은 게 있잖아"
    lisa"거기 사이로 편지를 쏙 집어넣으면 돼"
    anne"그런 방법이 있지……"
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(1)
    show lisa talk
    lisa"응?"
    "복도 쪽에서 발소리가 들려 왔다."
    play sound "se/footsteps_running.mp3"
    show lisa talk:
        linear 0.4 xalign 2.0
    "리사는 혹시나 해서 문앞으로 달려가 발소리의 주인이 누구인지 확인했다."
    lisa"윌리-윌리 왔어!"
    show anne shock2
    anne"힉!"
    lisa"엇!{cps=2} {/cps}방금 친구랑 같이 화장실에 들어갔어!"
    lisa"편지 내용이 좀 오글거리긴 해도 몰래 주려면 지금밖에 없을 걸!"
    show anne shock2:
        linear 0.5 xalign 1.6
    play sound "se/footsteps_running.mp3"
    scene bg school_hall with moveright
    "나는 리사와 함께 재빠르게 3반 앞까지 달려갔다."
    "여기서부터 있는 사물함은 전부 3반 학생들의 것이다."
    "당연히 이중에서 윌리의 것도 있다."
    show lisa talk:
        xalign 0.5 yalign 1.0
    show anne shy:
        xalign 0.7 yalign 1.0
    anne"어,{cps=2} {/cps}어쩌지……"
    lisa"왜?!"
    lisa"무슨 일 있어?!"
    anne"그,{cps=2} {/cps}그게……"
    anne"이 편지 못주겠어……"
    lisa"갑자기 왜?!"
    show anne shock2
    anne"내가 윌리의 락커를 열다니……!"
    show effect2
    play sound "se/shock2.mp3"
    show lisa shock
    lisa"너 진짜……"
    lisa"그거 아주 중증이네"
    lisa"그리고 우리 락커는 열지 않고 편지만 넣을거잖아"
    anne"그, 그래도……"
    anne"가까이 가는것 만으로도 숨이 막히는 걸……"
    hide effect2
    show lisa smile
    lisa"어쩔 수 없지……{cps=2} {/cps}내가 대신 넣고 올게!"
    lisa"윌리-윌리 몇 번 이야?"
    show anne shy
    anne"{size=20}22번……{/size}"
    lisa"오케이"
    play sound "se/footsteps_running.mp3"
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(0,166,505,284),0.5) with moveright
    show lisa think:
        zoom 1.6 xalign 0.8 yalign -0.3
    lisa"12번 이면 이 쪽 어딘가에 있는데……"
    lisa"흠……"
    show lisa
    lisa"여기있다!"
    play sound "se/book_page.ogg"
    "리사는 반으로 접은 편지를 넙적한 구멍 안으로 밀어 넣었다."
    anne_think"근데 저 사물함이 윌리께 맞던가……?"
    lisa"다 됐어"
    anne"음……"
    play sound "se/footsteps_concrete.mp3"
    show lisa:
        linear 1.0 xalign 2.0
    $ renpy.pause(2)
    scene bg school_hall with moveleft
    show anne:
        xalign 0.7 yalign 1.0
    show lisa smile:
        xalign 0.5 yalign 1.0
    anne"저기 리사……"
    anne"혹시나 해서 묻는 건데, 제대로 22번 사물함안에 넣었어?"
    lisa"그러~엄!"
    show lisa talk
    lisa"잠깐,{cps=2} {/cps}22번?"
    show lisa shock
    lisa"12번 아니었어?"
    anne"…………"
    lisa"…………"
    lisa"뭐,{cps=2} {/cps}뭔가 재미있어졌는데?"
    show anne shock
    anne"리사─!"
    play sound "se/footsteps_concrete.mp3"
    "화장실에서 윌리가 나오고 있었다."
    show lisa smile
    lisa"아무대나 빨리 숨자!"
    show anne shy
    anne"숨을 필요가 있나……?"
    anne"그냥 가만히 있어도 모를 거라고 생각 하는데……"
    show lisa shock
    lisa"아……{cps=2} {/cps}그런가……"
    "나랑 리사는 적당히 아무 일도 없다는 듯이 돌아다니기 시작했다."
    show lisa smile
    "윌리가 교실 안으로 들어가는 게 보이자 어째서인지 나보다 리사가 더 들뜨기 시작했다."
    lisa"{size=25}안에 들어간다!{/size}"
    play sound "se/move.mp3"
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(99,202,725,408),0.0) with moveright
    show willy shock:
        zoom 1.5 xalign 1.0 yalign -0.2
    show stephan:
        zoom 1.5 xalign 0.0 yalign -0.2
    willy"저번에 빌려간 내 사회노트 돌려줄 수 있을까?"
    stephan"아, 그거 말이지"
    stephan"내 책상 안에 있을텐데……"
    show stephan talk:
        linear 0.3 xalign 0.1 yalign -0.4
    play sound "se/search_bag.mp3"
    $ renpy.pause(1.0)
    show stephan shock:
        linear 0.3 xalign 0.0 yalign -0.2
    stephan"어라?{cps=2} {/cps}여기 없네?"
    show stephan think
    stephan"그럼 어디에 뒀지……?"
    willy"조금 빨리 부탁할게"
    show stephan talk
    stephan"뭔가 급한 일이라도?"
    willy"노트에 조금 중요한게 있어서"
    stephan"알았어"
    stephan"근데 그 노트 말이야……"
    show stephan shock
    stephan"무역이나, 채무법, 신용도 같은건 고딩 시험에 나올리가 없는데도 왜 적혀 있는 건지……"
    show willy
    willy"예습이야, 예습"
    stephan"너의 높은 성적의 비결이 그거냐;;"
    stephan"치트를 사용 하는거냐고?"
    show willy talk
    willy"예습이 왜 치트야?"
    stephan"아무리 봐도 그렇잖아!{cps=2} {/cps}딱히 가르쳐 주지도 않은걸 혼자서 배워놓고, 학교에선 \'내가 똑똑한거라규~\'라고 자랑하고!"
    willy"내가 그런적이 있었냐"
    stephan"입으론 안 했지만, 너의 행동이 그렇게 말 하고 있어!"
    show willy shock
    willy"으, 응……"
    willy"그보다 내 노트"
    show stephan talk
    stephan"아, 그랬지"
    show stephan think
    stephan"흠……"
    show stephan talk
    stephan"혹시 내가 실수로 교과서랑 같이 락커 안에 넣었나?"
    stephan"한번 가서 확인해볼게"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg school_hall at Zoom((1280,720),(0,166,505,284),(0,166,505,284),0.0) with moveright
    show stephan think:
        zoom 1.6 xalign 0.6 yalign -0.2
    play sound "se/door_open2.ogg"
    stephan"노트가……"
    play sound "se/book_page.ogg"
    show stephan
    stephan"여깄군"
    show stephan talk
    stephan"어?{cps=2} {/cps}위에 왠 쪽지가?"
    "토머는 사물함 안에 있는 쪽지 같은걸 펼쳐서 읽었고 있었는데……"
    stop music
    "근데 이상한게 있었다."
    anne"{size=20}서,{cps=2} {/cps}설마!{/size}"
    scene bg school_hall at Zoom((1280,720),(464,106,559,315),(464,106,559,315),0.0) with dissolve
    show anne shock:
        xalign 1.0 yalign 1.0
    show lisa smile:
        xalign 0.6 yalign 1.0
    anne"{size=20}리, 리사! 다른사람이 편지를 읽겠어!{/size}"
    anne"{size=20}얼른 막는 게……{/size}"
    lisa"쉿"
    lisa"{size=20}지금 재미있어지는 참이니까 가만히 있어봐{/size}"
    anne"…………"
    scene bg school_hall at Zoom((1280,720),(0,166,505,284),(0,166,505,284),0.0)
    show stephan think:
        zoom 1.6 xalign 0.6 yalign -0.2
    stephan"\'당신을 기다리겠습니다\'……?"
    show stephan shock
    stephan"이,{cps=2} {/cps}이거……!"
    play music"bgm/beat3.mp3"
    show stephan smile
    stephan"러브레터 잖아!"
    stephan"누군가 나의 매력을 알아봐줬어!{cps=2} {/cps}잇 힝~☆"
    play sound "se/footsteps_concrete.mp3"
    show willy talk:
        xalign -1.5 yalign -0.2 zoom 1.6
        linear 1.0 xalign 0.0
    willy"너 왜이렇게 늦어?"
    willy"안에 노트 없어?"
    show stephan smile2
    stephan"후후후후……{cps=2} {/cps}윌리여……"
    show willy shock
    willy"머, 뭐야……"
    extend" 너 갑자기 기분나빠"
    stephan"마음대로 생각 해.{cps=2} {/cps}하지만 언젠간, 이 중에서 가장 어른스러운게 나라는 걸 뼈저리게 느낄거야"
    willy"뭐……?"
    willy"혹시 나보다 생일이 빨라서 하는 소리냐?"
    show stephan shock
    stephan"그런게 아니라!"
    show stephan smile2
    stephan"……내가 고백을 받았다는거다"
    show willy
    willy"정말?"
    show willy talk
    willy"근데 나 관심 없어, 그보다 내 노트 좀 찾아줘"
    show stephan shock
    stephan"어, 어이……{cps=2} {/cps}뭔가 반응이 너무 미지근한데?"
    willy"이 학교엔 1, 2, 3학년 포함해서 약 2980명 정도가 있어"
    willy"그 중에서 한명쯤은 너한테 관심이 있다고 해도 별로 이상할게 없는데?"
    stephan"확실히 수치적으로 생각하면 뭔가 그렇긴 하지만……"
    show stephan shock2
    stephan"그래도 \'나\'를 좋아하는 사람 이라고!"
    stephan"확률적으론 놀랄 일이 아닐지라도, 고백의 대상자가 나인걸 감안하면 꽤 놀랄 일이라고 생각 하는데?!"
    show stephan sad
    show effect2
    play sound "se/shock2.mp3"
    stephan"……라고 생각하니까 또 슬프네"
    hide effect2
    show willy shock
    willy"어휴……"
    willy"그래서……{cps=2} {/cps}너한테 고백한 애는 어떤 앤데?"
    show stephan smile
    stephan"완전 귀엽고 수줌음이 많은 애 일듯!"
    willy"\'일듯\'……?"
    stephan"응!{cps=2} {/cps}편지로 고백 받았거든!"
    show willy talk
    willy"아─ 락커 안에 러브레터 비슷한게 들어있었던거구나"
    stephan"맞아!"
    show willy smile2
    willy"그럼 귀엽고 수줍음이 많을 것 같다는 건 너의 희망 사항?"
    show stephan
    stephan"뭐어……{cps=2} {/cps}조금은……"
    stephan"그래도 편지에 쓰여진 문체가 왠지 그런 느낌이야"
    stephan"애초에 21세기에 와서 후지게 러브레터를 쓰는것 만 봐도 충분히 수줍음이 많은 애 라는 게 느껴지지 않나?"
    show willy
    willy"확실히 요즘 시대에 러브레터는 아니지"
    scene bg school_hall at Zoom((1280,720),(464,106,559,315),(464,106,559,315),0.0)
    show anne shock:
        xalign 1.0 yalign 1.0
    show lisa smile:
        xalign 0.6 yalign 1.0
    play sound "se/hit.ogg"
    anne"큭……!" with sshake
    "왠지 내 심장에 칼을 박아 넣는 듯한 기분 이었다."
    lisa"크크크크"
    scene bg school_hall at Zoom((1280,720),(0,166,505,284),(0,166,505,284),0.0)
    show stephan smile:
        zoom 1.6 xalign 0.6 yalign -0.2
    show willy shock:
        xalign 0.0 yalign -0.2 zoom 1.6
    stephan"아~{cps=2} {/cps}가급적이면 키가 작고 흑발에, 말 수는 적지만 여러가지를 생각하는 쿨데레의 아이였으면 좋겠다~"
    stephan"거기다 츤데레 속성까지 추가된다면 좋겠는데……"
    willy"그, 그래;;"
    willy"그보다 내 노트는……"
    show stephan think
    stephan"뭐어……{cps=2} {/cps}난 빈유든 거유는 그쪽엔 수비범위가 넓으니까 문제는 안 되고……"
    stephan"아쉽게도 우리 학교는 급식재라서 같이 도시락 먹는 이벤트는 기대할 수 없겠네"
    stop music
    willy"넌 왜 고백한 상대가 무족건 너의 타입 일거라 단정짓는거야?"
    show stephan talk
    stephan"그야 편지의 문체가 그런 느낌인 걸?"
    show willy talk
    willy"정말……"
    play music "bgm/happy2.mp3"
    willy"스테반, 세상은 아는만큼 보인다는 말 알아?"
    stephan"혹시 \'프란시스 베이컨(Francis Bacon)\'의 말?"
    willy"그 사람은 \'아는 게 힘이다\'라고 말 했지만……"
    willy"둘다 비슷하지"
    stephan"어쨌건, 뭔 뜻인진 나도 알아"
    stephan"근데 그게 이 상황에 어울리는 말 인가?"
    willy"네가 머리속에서 멋대로 그런 이미지를 만드니까 이젠 그렇게밖에 안 보이는거야"
    stephan"그게 어쨌는데?"
    willy"너한테 고백한 여자의 입장이 돼서 생각해봐"
    show willy
    willy"그냥 네가 좋아서 고백 했을 뿐인데, 네가 머릿속에서 멋대로 이미지를 만들고"
    willy"나중에 만났을때 이미지가 너의 생각이랑 다르면 네가 멋대로 실망을 하고"
    scene bg school_hall at Zoom((1280,720),(464,106,559,315),(464,106,559,315),0.0)
    show anne:
        xalign 1.0 yalign 1.0
    show lisa:
        xalign 0.6 yalign 1.0
    willy"여자 입장에선 좀 억울하지 않을까?"
    anne_think"역시……{cps=2} {/cps}윌리야……"
    "언제나 남을 생각해주고……{cps=2} {/cps}똑똑하고……"
    "그런 윌리를 본다면 반하지 않는 게 정말 이상하다."
    scene bg school_hall at Zoom((1280,720),(0,166,505,284),(0,166,505,284),0.0)
    show stephan talk:
        zoom 1.6 xalign 0.6 yalign -0.2
    show willy:
        xalign 0.0 yalign -0.2 zoom 1.6
    stephan"…………"
    stop music
    show stephan smile2
    stephan"프란시스 베이컨도 별거 없네"
    show willy shock
    willy"어……?"
    play music "bgm/beat4.mp3"
    stephan"네가 말 한 \'아는만큼 보인다\'에는 모순이 있잖아"
    stephan"아는 만큼 보인다고 말은 하지만……"
    extend" 알기 위해선 봐야되잖아?"
    stephan"아니면 베이컨 아저씨는 보지 않고도 자기 스스로가 \'알고있다\'라고 말 할 수 있는 자만심이 가득 한 사람인가?"
    willy"그걸 그렇게 해석해버리면 어떻게……"
    stephan"그 양자역학에선 \'불확정성 원리(不確定性原理, uncertainty principle)\'라는 게 있잖아?"
    stephan"\'관찰\'하기 전까진 절대로 알 수 없어"
    stephan"그런데도 그 아저씨는 아는 만큼만 볼 수 있다고 말 하니까 원……"
    stephan"솔직히 베이컨 그거 지방 덩어리라서 몸에 별로 좋지도 않잖아?"
    willy"……너 다운 대답이었어"
    show willy
    stop music
    willy"확실히 네 말대로 알기 위해선 봐야해"
    willy"왜냐면 보는 것 만이 자신의 지식을 증명 할 수 있으니까"
    show stephan smile
    stephan"그치?{cps=2} {/cps}너 나한테 논파 당한거 맞지?"
    willy"하지만 우리가 보는 걸 인식하고 해석 하기 위해선 우선 무엇을 보고 있는지 알아야해"
    willy"그러니까 보기 위해선 그거에 대해서 알아야 하지"
    show stephan talk
    stephan"그냥 \'닭이 먼저냐 알이 먼저냐\'하는 이야기잖아?"
    willy"교육 이라는 게 원래 그런거야"
    willy"어느쪽이든 사실은 상관 없어, 그냥 우리가 이해 할 수만 있으면 되는거지"
    play music "bgm/beat3.mp3"
    show stephan smile
    show willy shock
    stephan"어쨌건 난 이제부터 리얼충이 되는거니까 딱히 상관없음!"
    stephan"난 얼른 자리에 앉아서 만났을때 해야 할 대사나 생각 해봐야지!"
    show stephan smile2:
        linear 2.3 xalign -1.0
    play sound "se/footsteps_concrete.mp3"
    stephan"후후후후……"
    show willy talk
    willy"그럼 공책은 내가 알아서 가져간다?"
    stephan"어~"
    play sound "se/move.mp3"
    scene bg school_hall at Zoom((1280,720),(464,106,559,315),(464,106,559,315),0.0) with moveleft
    show anne:
        xalign 1.0 yalign 1.0
    show lisa laugh:
        xalign 0.6 yalign 1.0
    lisa"푸하하하하!"
    lisa"너 토머 표정 봤냐"
    anne"{size=20}나 어쩌지……{/size}"
    lisa"저 표정 진짜 가관이다!"
    lisa"완전 찍어두고 싶을 정도야"
    lisa"마지막에 그 웃음소리도 정말"
    lisa"{size=45}푸하하하!{/size}"
    anne"결국 편지는 윌리 한테 전달되지 못했어……"
    anne"어쩌지……"
    "나는 걱정을 하고 있는것과 반대로 리사는 계속 토머의 들떠있는 표정을 보고 웃기만 했다."
    play music"bgm/smooth1.mp3"
    lisa"하아~{cps=2} {/cps}오늘 진짜 좋은 구경 했어……"
    lisa"아이고 배야……"
    show lisa smile
    extend" 너무 웃은거 같네……"
    "한참을 웃다가 지쳐버린 리사는 진정을 되찾았다."
    show anne
    anne"혹시 다른 방법 없을까?"
    show lisa
    lisa"다른 방법을 찾는것보단 용기를 내서 걔한테 직접 말해"
    lisa"방금 토머…… {size=25}(푸흡){/size} ……를 봤잖아"
    lisa"저건 너보고 용기를 내서 스스로에게 솔직해지라는 하늘의 뜻인거야!"
    anne"스스로에게 솔직해지라고……?"
    "어째서인지 스스로 솔직해지라는 말이 내 가슴속에 와닿았다."
    anne"솔직해진다 라……"
    lisa"그래!"
    lisa"네가 하고싶은 게 있으면 하고싶다고 당당하게 말하는거야!"
    lisa"당당하고 과감하게!"
    anne"과감하게……"
    stop bgs
    scene black with eyeshut
    "확실히 지금까지의 나는 언제나 숨어있었다."
    "윌리가 다른 사람이랑 놀때도……{cps=2} {/cps}옆에서 지켜보고만 있었을 뿐……"
    "하지만 난 이런 관계를 원했던 적이 없었다!"
    "난 윌리 옆에 있고 싶다!"
    anne_think"하지만 내가 뭘 할 수 있다고……"
    extend" 난 옛날부터 계속 남한테 도움만 받아왔던 사람인데……"
    "아니,{cps=2} {/cps}난 할 수 있어"
    "윌리랑 같이 있을거야……"
    "반드시……"
    play bgs "bgs/people.mp3"
    scene bg school_hall with eyeopen
    show anne smile:
        xalign 0.7 yalign 1.0
    show lisa talk:
        xalign 0.3 yalign 1.0
    lisa"뭐……{cps=2} {/cps}넌 윌리 앞에만 있어도 당황 해버리니까 조금 힘든일 일지도 모르겠지만……"
    anne"좋아!"
    anne"결정했어!"
    lisa"어?{cps=2} {/cps}할 수 있겠어?"
    anne"어……{cps=2} {/cps}좋은 계획이 떠올랐거든"
    anne"어떻게 해야할지 방향성만 있다면 윌리 앞에 서는 건 그리 두렵지가 않아……"
    lisa"그래?"
    anne"리사가 말한대로 당당하고 과감하게 나가기만 한다면……"
    anne"그리고 내 감정에 대해서 솔직해 진다면 분명 방법이 있을거야"
    show lisa
    lisa"오오?{cps=2} {/cps}그래서 윌리-윌리에게 고백 할 용기가 생겼다는거지?!"
    anne"응!"
    extend" 먼저 다음주 월요일날 같이 커피숍에 가자고 할거야!"
    anne"그리고……"
    show lisa talk
    lisa"잠깐, 다음주 월요일?"
    lisa"보통은 주말에 가지 않나?"
    show anne
    anne"그,{cps=2} {/cps}그게 내가 주문할 물건이 있는데 배송시간 때문에"
    anne"그 사이에 윌리가 다른 여자 애들이랑 말을 섞지 못하도록 손을 쓰거나 하는 것도……"
    show lisa shock
    lisa"그,{cps=2} {/cps}그럼 잘 해봐;;"
    show lisa smile
    lisa"혼자서도 잘 할 수 있을거 같으니까 이제 난 필요 없겠지?"
    show anne smile
    anne"응!"
    extend" 오늘 정말 고마웠어!"
    show lisa smile2
    lisa"후훗,{cps=2} {/cps}혹시 둘이 사귀게 되면 한턱 쏘는거야!"
    show anne shock
    anne"사,{cps=2} {/cps}사귄다니!!"
    lisa"{size=20}귀여운 녀석……{/size}"
    stop bgs
    scene black with dissolve
    centered"방과 후"
    anne_think"그래……{cps=2} {/cps}리사가 말 한 것 처럼"
    anne_think"당당하고 과감하게 가는거야!"
    anne_think"윌리랑 함께 라……{cps=2} {/cps}하아……"
    scene bg outside_road with dissolve
    play bgs "bgs/street.mp3"
    show willy shock
    anne_think"윌리가 혼자 있는 지금이 기회야!"
    play sound"se/footsteps_concrete.mp3"
    scene bg outside_road at Zoom((1280,720),(0,0,1280,720),(292,177,696,391),2.0) with dissolve
    $ renpy.pause(2)
    show anne shy:
        zoom 1.3 yalign -3.3 xalign 0.0
    show willy:
        zoom 1.3 yalign -0.1 xalign 1.0
    anne"저,{cps=2} {/cps}저기……"
    willy"응?"
    willy"무슨 볼일 이라도?"
    show anne shock2
    anne"그,{cps=2} {/cps}그……{cps=2} {/cps}그……"
    anne_think"내가 윌리앞에 있다니……{cps=2} {/cps}내가 윌리앞에 있다니……!"
    anne_think"하지만 이번엔 나한테 계획이 있어"
    anne_think"당황 할 필요가 없다고!"
    show anne shy
    anne_think"당당하게 가는거야……"
    anne"저어……{cps=2} {/cps}그……"
    show effect1
    play sound "se/shock.ogg"
    show anne shock2
    anne"{size=45}다,{cps=2} {/cps}다음주 월요일 방과후에 같이 커커커,{cps=2} {/cps}커피숍 어떤가요?!{/size}" with lshake
    hide effect1
    anne_think"하아……{cps=2} {/cps}하아……{cps=2} {/cps}말 했다……"
    show willy shock
    willy"커피숍?"
    show willy thinkt
    willy"음……"
    anne_think"말을 하긴 했지만……"
    stop music
    show anne shy
    anne_think"혹시 거절 하면 어쩌지?!"
    anne_think"이럴땐 어떻게 해야?!"
    anne_think"실패 했을때의 계획이 없어!!"
    anne_think"으아아아!!"
    show willy
    willy"그래"
    anne"네?"
    willy"다음주 월요일 시간 비니까 상관 없어"
    play music "bgm/happy4.mp3"
    anne"저,{cps=2} {/cps}정말인가요?!"
    willy"응"
    show anne shock
    anne_think"아,{cps=2} {/cps}앗싸……"
    anne_think"내가 해냈어!"
    show willy talk
    willy"근데 커피숍 이라면 어디 있는 커피숍을 말하는 거야?"
    show anne shy
    anne"상점가 쪽에 있는 곳이요……"
    willy"그래,{cps=2} {/cps}다음주 월요일, 방과후, 상점가 커피숍이지?"
    show anne smile
    anne"네!"
    willy"알았어"
    anne"가,{cps=2} {/cps}감사합니다!!"
    show anne smile:
        linear 0.5 xalign -2.0
    play sound "se/footsteps_running.mp3"
    scene bg outside_road at Zoom((1280,720),(292,177,696,391),(0,0,1280,720),2.0) with dissolve
    "윌리 옆에 너무 오랫동안 있으면 심하게 흥분 해버릴 거 같아서 말이 끝나자 바로 자리를 떳다."
    anne_think"와……{cps=2} {/cps}너무 기뻐……"
    anne_think"아냐,{cps=2} {/cps}여기서 기뻐해선 아무런 의미가 없어!"
    stop music
    anne_think"윌리가 영원히 내것이 되려면 아직 멀었으니까……"
    stop bgs
    scene black
    anne_think"내 계획은 이제부터 시작이야……"
###############################################앤 시점 끝
    play music "bgm/beat1.mp3"
    centered"4일 후"
    centered"9월 15일 월요일"
    centered"오전 8시"
    scene bg school_classroom with memory
    play bgs "bgs/people.mp3"
    centered"2학년 3반 교실"
    show stephan shock at left
    stephan"허어……{cps=2} {/cps}허어……{cps=2} {/cps}허어……"
    "어제 윌리가 집에서 잠옷 파티를 하자고 하는 바람에 너무 들떳나보다……"
    "새벽까지 게임을 해서 이렇게 늦잠을 자고……"
    stephan"그래도 다행히 오늘은 지각을 면했어……"
    show willy talk at right
    willy"밤새서 게임을 하니까 그런거지"
    stephan"너도 같이 했으면서!"
    show willy shock at right
    willy"그리고 넌 그거 달린거 가지고 지쳤냐"
    willy"맨날 게임 하고 애니만 보니까 그런거잖아"
    willy"운동좀 해"
    stephan"닥쳐……{cps=2} {/cps}허어……"
    stephan"그보다 1교시 뭐야"
    show willy talk at right
    willy"월요일 1교시는 분명……{cps=2} {/cps}과학 이었나?"
    show stephan yawn at left
    stephan"쳇,{cps=2} {/cps}수면 보충은 글렀군……"
    stephan"과학은 너무 빡세단 말이지……"
    willy"너, 과학 좋아하잖아"
    stephan"천문학은 1학기에만 들어가잖아……"
    willy"그렇긴 하지만, 지금 하는 화학도 재미있잖아"
    stephan"화학은 문제 없지만, 외워야 할 게 많다고!"
    stephan"으아아~{cps=2} {/cps}오늘 뭔가 특별한 일이라도 있었으면 좋겠다~"
    willy"예를 들어?"
    stephan"전학생이 온다든가"
    willy"단념 해"
    willy"설령 온다고 해도 순서 상 4반에 올껄?"
    stephan"쳇,{cps=2} {/cps}꿈과 희망이 없네"
    stephan"난 교과서나 챙겨야겠다"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(190,38,540,304),0.5) with moveright
    "나는 복도에 있는 라커 쪽으로 이동하려고 했다."
    "……근데 뭔가 이상한 관경을 목격했다."
    scene ev anne_watching with dissolve # 앤이 몰래 교실 안을 들여다 보는 일러스트
    stephan_think"뭐지?"
    "어떤 여자아이가 소심하게 교실 안을 내다보고 있었다!"
    menu:
        "물어본다.":
            scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(190,38,540,304),0.0) with moveright
            "나는 여학생에게 말을 걸었다."
            show stephan:
                zoom 1.4 xalign 0.2 yalign -0.2
            show anne shock2:
                zoom 1.4 xalign 1.0 yalign -1.5
            stephan"저기……"
            stephan"누구 찾고 있어?"
            stephan"이름 말해주면 내가 불러 줄 수도 있는……"
            show effect1
            play sound "se/shock.ogg"
            anne"히익!" with lshake
            show anne shock2:
                linear 0.5 xalign 3.0
            play sound "se/footsteps_running.mp3"
            $ renpy.pause(2)
            hide anne shock2
            hide effect1
            show stephan shock
            stephan"어……"
            "여자 아이는 그대로 달아나 버렸다."
            show stephan think
            stephan_think"내가 무슨 말 실수라도 했나?"
            hide stephan think 
        
        "못본척 한다.":
            scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(190,38,540,304),0.0) with moveright
            show stephan think:
                zoom 1.4 xalign 0.2 yalign -0.2
            "누군진 모르겠지만, 나랑은 관련 없으므로 무시하고 내 갈길을 가기로 했다."
            play sound "se/footsteps_running.mp3"
            scene ev anne_watching2 with dissolve # 앤은 없고 뒷문만 있는 일러스트
            "근데 내가 복도로 가려고 문 앞에 다가가자 여자는 엄청난 속도로 뛰쳐나갔다."
            stephan_think"귀, 귀신인가……"
    stop bgs
    stop music
    scene black with dissolve
    centered"오후 4시"
    centered"방과후"
    scene bg outside_road with moveup
    play bgs "bgs/street.mp3"
    play music"bgm/smooth4.mp3"
    "나랑 윌리는 같이 집으로 걸어가고 있었다."
    show stephan talk at left
    show willy talk at right
    stephan"쳇,{cps=2} {/cps}설마 오늘 과학 숙제가 있었을 줄이야……"
    show stephan at left
    stephan"넌 오늘도 우리집에서 잘꺼?"
    show willy think at right
    willy"글쎄"
    show willy talk at right
    willy"아마 오늘은 안 자도 괜찮을 거야"
    willy"어쩌면 스토커 사건의 결착이 지어질지도 모르니까"
    stephan"근데 그 스토커는 네가 뭐가 좋다고 그렇게 쫓아다니는 거지?"
    stephan"나도 그런 스토커 같은거라도 있었으면 좋을 텐데……"
    show willy shock at right
    willy"그런말 함부로 하지마;;"
    willy"스토킹도 엄연한 범죄야"
    willy"넌 범죄자가 널 쫓아다니는 게 좋겠냐?"
    stephan"그래도 \'얀데레(ヤンデレ)\'라는것도 모에요소중 하나잖아"
    show willy talk at right
    willy"\'얀데레\'?"
    willy"그게 뭔데?"
    show stephan shock at left
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}헉{/size},{cps=2} {/cps}너도 모르는 게 있었어?!" with lshake
    hide effect1
    show willy shock at right
    willy"나도 인간인데 당연히 모르는 게 있지;;"
    show stephan think at left
    stephan"그러쿤……"
    stephan"윌리도 인간이란 말이지……"
    willy"그 쪽에서 의문이 든거냐?!"
    willy"그보다 얀데레 라는 게 뭐야"
    show stephan at left
    stephan"얀데레 란!"
    stephan"사랑하는 사람을 위해서 살인, 납치, 감금, 협박 등 범죄조차 마다 하지 않는 사람을 뜻해"
    stephan"물론 모든 얀데레가 그런다는 건 아니지만"
    willy"그거 그냥 싸이코잖아"
    stephan"아니지!{cps=2} {/cps}싸이코랑은 다르다! 싸이코랑은!"
    stephan"얀데레는 끝에 \'데레(でれ)\'가 붙어 있잖아?"
    willy"\'데레\'?"
    willy"아―{cps=2} {/cps}역시 얀데레라는 것도 너의 그 오타쿠 문화중 하나였었냐……"
    stephan"얀데레의 시초는 말이지……!"
    stop bgs
    scene black with dissolve
    "나는 거의 몇 분간 쉬지도 않고 \'얀데레\'에 대해서 자세히 설명을 했다."
    "윌리는 그게 귀찮다는 표정이었지만 그래도 듣고는 있었다."
    "그리고 버스 정류장 근처에 도착을 했을때 윌리가 말했다."
    play sound "se/move.mp3"
    scene bg outside_busstop with moveleft
    play bgs "bgs/street.mp3"
    show stephan at left
    show willy shock at right
    stephan"또, 유노라고 하는 캐릭터는 말이야……"
    show willy talk at right
    willy"잠깐"
    show stephan talk at left
    stephan"응?"
    stephan"네 집은 여기서 좀 더 가야되지 않나?"
    willy"가기전에 들려야 할 곳이 있거든"
    willy"그럼 여기서 작별이네"
    stephan"그래"
    show stephan smile at left
    stephan"혹시 스토커가 또 오면 사양말고 우리집으로 와!"
    willy"왜 갑자기 적극적이지?"
    show willy shock at right
    willy"설마 오늘 과학 숙제 때문에?"
    show stephan blush at left
    stephan"따,{cps=2} {/cps}딱히 그런건 아니야"
    willy"여기서 츤데레 설정 추가 안해도 돼!"
    stop bgs
    stop music
    scene black with dissolve
    centered"오후 4시 45분"
    scene bg downtown_outside with dissolve
    play bgs "bgs/people.mp3"
    play music "bgm/happy2.mp3"
    centered"상점가"
    show anne think
    anne_think"윌리는 언제쯤 올까……"
    anne_think"설마 다른 사람이랑 만나고 있나?!"
    show anne
    anne_think"아냐……{cps=2} {/cps}그거라면 벌써 손을 써 놨으니까 문제 없을거야……"
    anne_think"윌리 집에서부터 여기까진 거리가 좀 있으니까 조금 늦을 수도 있어!"
    anne_think"분명 그럴거야!"
    anne_think"혹시 모르니 문자라도 보내 보자!"
    "나는 윌리의 번호로 문자를 보냈다."
    "보낸지 몇 분이 지났을까, 답장이 오기를 기다리고 있었는데 저쪽에서 낯이 익는 누군가가 다가오는 것이 보였다."
    "윌리 였다."
    show anne shy:
        linear 0.5 xalign 0.3
    show willy:
        xalign 1.6 yalign 1.0
        linear 0.6 xalign 0.75
    willy"이거 미안"
    willy"버스 타는데 차가 좀 막혀 있어서 늦었어"
    anne"아,{cps=2} {/cps}아니에요!"
    anne"저도 이제 막 왔는 걸요!"
    willy"후우~{cps=2} {/cps}기다리게 만들지 않아서 다행이네"
    anne"서,{cps=2} {/cps}설마 제 걱정을?!"
    willy"날씨도 쌀쌀해지고 있는데 여자 혼자서 기다리게 만들면……{cps=2} {/cps}죄책감이 든다고 할까나……?"
    play sound "se/shock.ogg"
    show anne shock
    show effect1
    anne_think"{size=45}어떡해!!{/size}" with lshake
    hide effect1
    anne_think"윌리가 나를 걱정해줬어!"
    show anne yanshock
    anne_think"이거 기분이 너무 좋아……"
    scene bg downtown_outside at Zoom((1280,720),(0,0,1280,720),(624,275,656,369),0.7)
    $ renpy.pause(0.7)
    show willy:
        xalign 0.75 yalign 1.0
    show anne shy:
        xalign 0.0 yalign 1.0
        linear 0.4 xalign 0.5
    "나랑 윌리는 같이 카페를 향해 걸어갔다."
    "그것도……{cps=2} {/cps}옆에서……"
    "매우 근접하게……"
    "처음엔 내 심장이 터질 것 같았지만……"
    extend" 시간이 지날수록 점점더 익숙해졌다."
    "……라고 해야 할까"
    "그냥 생각……{cps=2} {/cps}아니, 이 상황에 대해 실감이 잘 안났다."
    "몸에 감각이 없어져 간다고 해야할까……"
    "모든게 꿈만 같았다."
    stop bgs
    play sound "se/move.mp3"
    scene bg downtown_cafe at Zoom((1280,720),(0,0,1280,720),(184,112,674,379),0.5) with moveright # 카페 내부 배경
    $ extra_name = '점원'
    extra"뭘로 하시겠습니까?"
    show anne:
        zoom 1.2 xalign 0.3 yalign 1.0
    show willy think:
        zoom 1.2 xalign 0.7 yalign 1.0
    willy"흠……"
    show willy talk
    willy"전 에스프레소로 주세요"
    anne_think"흐엑!{cps=2} {/cps}그렇게 쓴 걸!"
    willy"넌 뭘로 할거야?"
    show anne shy
    anne"저,{cps=2} {/cps}전……{cps=2} {/cps}모카 라떼로……"
    extra"둘다 뜨거운걸로 드릴까요?"
    willy"네"
    anne"네……"
    extra"다 합쳐서 9.45 달러 입니다"
    show willy shock
    willy"뭔 커피가 이렇게 비싸……"
    show willy
    willy"앗,{cps=2} {/cps}걱정마, 돈은 내가 낼게"
    anne"저,{cps=2} {/cps}정말요?!"
    willy"응"
    willy"돈이 좀 생겨서"
    show effect1
    play sound "se/shock.ogg"
    anne"가,{cps=2} {/cps}감사합니다!!" with lshake
    hide effect1
    willy"에이~{cps=2} {/cps}뭘 이런걸 가지고"
    willy"작은 감사의 표시 라고 생각 해주면 좋겠어"
    show anne
    anne"감사……?"
    willy"저쪽에 비어있네!{cps=2} {/cps}저기 가서 앉자"
    play sound "se/footsteps_wood.mp3"
    scene ev cafe_seat with moveup
    $ renpy.pause(1.4)
    show willy:
        zoom 1.4 yalign -0.1 xalign 0.5
    "나와 윌리는 뒷쪽에 있는 비어있는 자리에 앉았다."
    anne"저어……{cps=2} {/cps}윌리?"
    willy"왜?"
    anne"그게……{cps=2} {/cps}대신 계산해줘서 고마워요……"
    willy"그냥 작은 감사의 표시니까 신경 쓰지 마"
    anne"하지만 제가 딱히 감사를 받을 만한 행동을 한 기억이 없는데……"
    willy"그야 네가 무의식 중에 한 행동 이니까"
    anne"네?"
    "나는 점점 윌리가 무슨 말을 하고 있는지 이해가 안 가기 시작했다."
    extra"{size=40}에스프레소랑 모카 라떼 뜨거운거 나오셨습니다!{/size}"
    anne"제,{cps=2} {/cps}제가 가겠습니다!"
    scene bg downtown_cafe at Zoom((1280,720),(253,356,647,364),(253,120,647,364),0.6) with movedown
    show anne:
        xalign 2.2 yalign 1.0
        linear 0.7 xalign 0.7
    anne_think"윌리는 도대체 무슨 말이 하고 싶은걸까?"
    scene bg downtown_cafe at Zoom((1280,720),(253,120,647,364),(0,262,647,364),0.0) with dissolve
    show anne with dissolve:
        xalign 0.7 yalign -0.2 zoom 1.3
    "나는 점원 에게서 주문 한 커피를 양손에 들고 시럽이 있는 쪽으로 발길을 옮겼다."
    "내가 주문한 모카 라떼에 시럽을 2펌프 정도 넣었고"
    "윌리가 주문한 에스프레소 안엔 내가 미리 준비해둔 가루를 부었다."
    anne_think"뭐, 나중에 천천히 들어보면 되겠지……?"
    show anne yan
    anne_think"당당하고 과감하게 가는거야~♡"
    scene ev cafe_seat with moveup
    show willy:
        zoom 1.4 yalign -0.1 xalign 0.5
    anne"여기 주문하신 에스프레소……"
    "나는 쑥스러운 마음 때문에 조금씩 떨리는 손으로 윌리에게 커피를 건네줬다."
    willy"고마워"
    anne"저어―{cps=2} {/cps}아까 말한 감사의 뜻이라는 게 대체 무슨 뜻인가요?"
    willy"혹시 여기 오면서 나한테 문자 보낸적 있어?"
    anne"네에……"
    anne"한통 보낸적이 있어요……"
    stop music
    "윌리는 커피를 한모금 마셨다."
    show willy talk
    willy"그 문자 덕분에 범인에 대해서 확신을 가질 수 있게 됐거든"
    anne"범인?"
    willy"나도 설마했는데"
    willy"나를 계속 감시했던 사람……"
    play music "bgm/sirius1.mp3"
    extend" 너지?"
    anne"가,{cps=2} {/cps}감시라니?"
    anne"제가 그럴리가!"
    willy"시치미 떼도 소용 없어"
    anne"하지만 제가 그랬다는 증거가 있는 것 도……"
    willy"증거 라……"
    willy"먼저 내 주변인들이 받은 모스 부호로 된 문자"
    willy"대상자가 전부 나랑 대화를 한적이 있었던 인물 이었지"
    willy"그리고 내가 조사를 좀 해봤는데, 그 사람들은 전부 너를 알고 있더라고"
    willy"생각해보면 나도 너랑 꽤 대화를 했었어, 그런데 어째서인지 너한테선 모스 부호가 왔다는 소식이 안들렸지"
    willy"처음엔 내가 너한테 폰 번호를 알려 준 적이 없어서 그런가 싶었는데……"
    anne_think"……하지만 내가 오늘 문자를 보내는 바람에 용의선상에 들어 왔다는 건가"
    anne_think"역시……{cps=2} {/cps}윌리야……"
    anne"근데 모스부호 문자라니……{cps=2} {/cps}무슨 말을 하는지 모르겠어요……"
    show willy shock
    willy"정말 그렇게 나올거야?"
    willy"계속 시치미를 떼겠다면 어쩔 수 없지……"
    willy"그럼 내 번호는 어떻게 알았어?"
    anne"네?!"
    willy"여기 오기 전에 나한테 보낸 문자말이야"
    willy"난 너한테 내 번호를 알려준 기억이 없는데 어째서인지 넌 내 번호를 알고있어"
    anne"예전에 알려주신적이 있었는데 그냥 기억을……"
    show willy talk
    willy"내가 기억을 못하고 있다……{cps=2} {/cps}라고?"
    willy"그건 아니라고 봐"
    anne"…………"
    anne_think"생각해보니까 윌리는 남들보다 기억력이 좀 좋았지……"
    "그래, 지금까지 내가 윌리를 쫓아다녔다는 게 들켜버렸다."
    "하지만 그렇다고 해서 내 계획에 변동은 없다."
    anne"그럼 이번엔 제가 한가지 질문을 할게요……"
    anne"윌리가 저를 범인이라고 생각하게 된 계기가 그 문자 한통 때문이었다고 한다면……"
    anne"그때 만약 제가 그 문자를 보내지 않았으면 어쩔 생각 이었어요?"
    willy"그럼 그냥 집으로 돌아가는거지"
    anne"힉!{cps=2} {/cps}너무해!"
    willy"너무한 건 너잖아……{cps=2} {/cps}왜 내 칫솔을 훔친거야?"
    anne_think"위,{cps=2} {/cps}윌리의 칫솔……!"
    anne_think"지금 내가 사용 중 이라고는 절대 말 못해!!"
    willy"앤……"
    stop music
    extend" 나한테 솔직히 얘기해줘"
    anne"네……?"
    show willy sirius:
        linear 0.4 zoom 1.4
    willy"네가 나한테 이런일을 꾸민다고 해서 뭔가 이득이 되는 건 없어……{cps=2} {/cps}그렇다는 건, 다른 인물이 너한테 시켰겠지"
    willy"……누가 너한테 이런일을 하라고 시켰어?"
    willy"혹시 이 건물 안에 있어?"
    willy"아니면 다른……"
    $ renpy.vibrate(0.3)
    play music "bgm/sirius3.mp3"
    show willy shock2:
        linear 0.4 yalign -0.3
    play sound "se/heartbeat.mp3"
    willy"윽……!" with sshake
    willy_think"뭐,{cps=2} {/cps}뭐지……"
    willy_think"갑자기 몸이……{cps=2} {/cps}나른해지기 시작했어……"
    anne_think"드디어 약빨이 듣기 시작하는 건가……"
    willy"너……"
    willy"무슨 짓을……?!"
    anne"이,{cps=2} {/cps}이 수면제를 구하는데 정말 힘들었습니다!"
    anne"배송 시간이 더 늦었으면 데이트 날짜에 맞추지 못할 거 같았고……{cps=2} {/cps}또, 의료 진단서가 없으면 주문이 힘들어서……"
    willy"수면제……{cps=2} {/cps}라고?"
    willy"그럼 이건 전부……"
    play sound "se/fall.ogg"
    show willy shock2:
        linear 0.3 yalign -2.5
    stop music
    hide willy shock with movedown
    "윌리는 힘없이 테이블에 머리를 박았다."
    play sound "se/search_bag.mp3"
    scene bg downtown_cafe with moveup
    anne_think"후후후후……"
    show anne shock2:
        zoom 1.6 yalign -0.4 xalign 0.5
    anne"위,{cps=2} {/cps}윌리, 아무리 피곤해도 여기서 갑자기 잠드시면 어떻게요?!"
    show anne yan
    anne"빨리 집으로 가요……"
    scene black
    anne_think"조금만 더 있으면……{cps=2} {/cps}영원히 함께예요……{cps=2} {/cps}윌리♡"
##############################################################################################
#########################################사건2: 후회와 반복###########################################
##############################################################################################
    play sound "se/case_start.mp3"
    show case2 with moveright
    $ renpy.pause(1)
    hide case2 with Dissolve(5)
    centered"같은 시각, 스테반의 집"
    play music "bgm/smooth1.mp3"
    scene bg room_stephan_eve with dissolve
    show stephan yawn
    stephan_think"숙제가 참 어렵네……"
    "나는 집에 도착 하자마자 바로 숙제를 시작했다."
    "어차피 인터넷에서 정답을 보고 있긴 하지만 분량때문에 쉽진 않았다."
    show stephan think
    stephan_think"오늘 숙제 때문에 할아버지 댁도 못갔는데……"
    stephan_think"아니지! 숙제를 빨리 끝내면 할아버지 댁에 갈 수 있을지도 몰라!"
    show stephan smile
    play sound "se/phone_text2.mp3"
    stephan"빨리 끝내자아~!"
    show stephan talk
    stephan"응?"
    stephan_think"무슨 소리였지?"
    scene bg room_stephan_day at Zoom((1280,720),(0,0,1280,720),(617,347,663,373),1.0)
    $ renpy.pause(1.4)
    scene bg room_stephan_day at Zoom((1280,720),(617,347,663,373),(0,114,663,373),1.0)
    "나는 소리의 정체를 찾으려고 주변을 한번 훑어봤다."
    scene bg room_stephan_day at Zoom((1280,720),(0,114,663,373),(26,347,663,373),0.5)
    "그때 모니터 뒷쪽에서 충전기에 꽃혀 있는 스마트폰을 발견했다."
    stephan_think"어제 윌리가 우리 집에서 자다가 놔두고 간건가……"
    show phone2:
        xalign 0.75 yalign 0.5 zoom 0.3
    "나는 폰을 들고 자세히 살펴봤다."
    "기종은 걔가 항상 쓰던 \'젤러시 S5(Jalaxy S5)\'다."
    show stephan smile2
    stephan_think"훗"
    stephan_think"윌리가 뭔가를 깜빡할 줄이야"
    stephan_think"녀석 폰엔 뭐가 찍혀있는지 한번 볼까!"
    "……물론 그게 도덕적으로 옳지 않다는 건 알고 있다."
    "어쩌면 불법일 수도 있다."
    show stephan shock
    stephan_think"어,{cps=2} {/cps}어쩌지……"
    hide stephan shock
    show phone2:
        linear 0.3 xalign 0.5 zoom 1.4
    "몇 분간 고민 했지만 역시, 나의 도덕심을 엿 바꿔 먹기로 했다."
    hide phone2 with dissolve
    show stephan smile2:
        xalign 0.3 yalign -0.2 zoom 1.4
    stephan"먼저 사진을 살펴보도록 할까……"
    play sound "se/move.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg room_stephan_day at Zoom((1280,720),(26,347,663,373),(26,347,663,373),0.0) with moveleft
    show stephan yawn:
        xalign 0.3 yalign -0.2 zoom 1.4
    stephan_think"쳇,{cps=2} {/cps}심심한 녀석"
    stephan_think"폰에 어째 아무것도 없을수 가 있냐"
    show stephan
    stephan_think"잠깐,{cps=2} {/cps}생각해보니까 아까 문자가 왔었지?"
    "나는 방금 왔던 문자를 확인했다."
    hide stephan
    nvl clear
    narrator_nvl"지금 기다리고 있는데 어디쯤 왔어요?"
    "발신인은 따로 전화번호부에 등록 되어 있지가 않았다."
    show stephan think:
        xalign 0.3 yalign -0.2 zoom 1.4
    stephan_think"\'지금 기다리고 있는데\'라고?"
    stephan_think"이 폰이 정말 윌리꺼 라면……"
    stephan_think"상대방은 지금 윌리를 기다리고 있다는 뜻이 되는데……"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}설마 윌리가 데이트를?!{/size}" with lshake
    hide effect1
    stephan_think"아,{cps=2} {/cps}아닐꺼야"
    stephan_think"어쩌면 상대방이 남자 일 수도 있는거잖아;;"
    show stephan
    stephan_think"그래!{cps=2} {/cps}분명 아는 친구나 후배랑 같이 어디 놀러다니고 있을지도 몰라!"
    show stephan shock2
    stephan_think"하,{cps=2} {/cps}하지만 아는 사람 이라면 전화번호 부에 등록 했을텐데……"
    show stephan
    stephan_think"내가 신경 쓸 일은 아닐거야!"
    stephan_think"폰은 내일 학교에서 줘야겠다"
    "나는 애써 방금 본 문자의 내용을 잊으려고 했다."
    stephan_think"숙제나 빨리 끝내고 할아버지 댁으로 가야지!"
label at_grandpas_house:
    stop music
    scene black with dissolve
    "나는 숙제를 전부 끝 마치고, 할아버지 댁으로 출발했다."
    scene bg lib_night with moveright
    play sound "se/book_page.ogg"
    show stephan yawn with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"후아아암~"
    "왜일까……{cps=2} {/cps}일기장을 읽는 게 너무 힘들다."
    "딱히 할머니와 할아버지 사이에 뭔가 특별한게 등장하지도 않고……{cps=2} {/cps}이야기에 진전이 있는 것도 아니고"
    show stephan think
    "하지만 할아버지가 매일 편지를 쓰고있는 \'아주머니\'라는 인물이 조금 궁금하다."
    "성함이 \'엘사라 나보코프\'라고 했던거 같던데……"
    stephan_think"성으로 추측 해봤을땐 러시아 계 오리엔스인 인가?"
    "우리나라는 세계 2차 대전 당시 수 많은 외국인들 —특히 일본, 독일, 러시아인— 이 들어왔기 때문에 혼혈 이라고 해도 이상할 건 없다."
    "생각해보니까 내 조상도 영국 사람 이라던거 같던데"
    "그거 말고 어제 내가 읽었던 내용에서 할머니랑 할아버지가 처음 만났을때 보였던 행동도 조금 이상하긴 했다……"
    play sound "se/think.mp3"
    scene bg ravine_night with flash
    show mary
    mary"오랫만이야,{cps=2} {/cps}에드워드"
    scene bg lib_night with flash
    show stephan think:
        zoom 2.0 yalign 0.1 xalign 1.0
    "할아버지랑 똑같은 이름을 지닌 사람……"
    "혹시 그 인물이 할머니의 행동에 대한 열쇠를 지니고 있을까?"
    "물론 그건 나의 희망적인 관칙이지만"
    show stephan yawn
    stephan_think"너무 읽기만 했더니 목이 뻐근하네"
    stephan_think"좀 쉬었다가 다시 읽어야겠다"
    play sound "se/move.mp3"
    scene black with moveright
    play music "bgm/beat2.mp3"
    scene bg mansion_hall at Zoom((1280,720),(0,0,502,282),(0,154,646,363),1.0) with dissolve
    $ renpy.pause(1.0)
    show cia:
        xalign 0.0 zoom 1.3 yalign -1.5
    show seb:
        xalign 0.8 zoom 1.4 yalign -0.2
    cia"있잖아요! 있잖아요!"
    play sound "se/search_bag.mp3"
    show ev book2:
        xalign 0.0 yalign 0.7 alpha 0.0
        linear 0.6 xalign 0.6 alpha 1.0
    cia"이 책 부엌에 있던데……"
    cia"혹시 세바스찬 씨 거예요?"
    show seb talk
    seb"아, 그게 거기 있었군요"
    play sound "se/search_bag.mp3"
    show ev book2:
        linear 0.3 yalign 1.0
    $ renpy.pause(0.3)
    hide ev book2 with dissolve
    show cia think
    cia"근데 무슨 책이에요?{cps=2} {/cps}엄청나게 어려운 말이 많이 쓰여있던데……"
    cia"거기다 왠지모르게 징그러운 사진도 많이 있었고……"
    show cia shock
    cia"호, 혹시 세바스찬 씨는 그런게 취향?!"
    show seb shock
    seb"아뇨!!"
    scene bg mansion_hall at Zoom((1280,720),(0,154,646,363),(0,87,382,215),0.5) with moveup
    play sound "se/footsteps_wood.mp3"
    show stephan yawn with dissolve:
        xalign 0.1 yalign 1.0
        linear 0.4 xalign 0.5
    stephan"…………"
    scene bg mansion_hall at Zoom((1280,720),(0,87,382,215),(0,154,646,363),0.0) with dissolve
    show cia:
        xalign 0.0 zoom 1.3 yalign -1.5
    show seb:
        xalign 0.8 zoom 1.4 yalign -0.2
    cia"도련님!{cps=2} {/cps}볼일은 다 끝나셨나요?"
    stephan"으음……{cps=2} {/cps}잠깐만 좀 쉬려고……"
    show cia smile
    cia"그럼 같이 차라도 마시는 건 어때요?"
    cia"세바스찬 씨의 친가에서 보내온 중국식 차 래요!"
    show cia think
    cia"이름이……{cps=2} {/cps}보리차 였던가……?"
    seb"보이차 예요"
    show cia smile
    cia"네, 그거요"
    show cia
    cia"그래서 어때요?"
    menu:
        "같이 마신다.":
            $ not_drink = False
            scene bg mansion_hall at Zoom((1280,720),(0,154,646,363),(0,87,382,215),0.0) with dissolve
            show stephan smile:
                xalign 0.5 yalign 1.0
            stephan"나도 마실래"
            seb"그럼 제가 컵 한 개 더 가져올게요"
            play sound "se/footsteps_wood.mp3"
            show stephan smile:
                linear 2.0 zoom 1.7 yalign -2.0
            $ renpy.pause(2.6)
            play sound "se/move.mp3"
            scene black with moveleft
            $ renpy.pause(0.5)
            scene bg mansion_hall at Zoom((1280,720),(0,154,646,363),(0,154,646,363),0.0) with moveleft
            show cia think:
                zoom 1.3 yalign -1.5 xalign 1.0
            show seb:
                zoom 1.4 yalign -0.2 xalign 0.0
            cia"그래서 방금 그 책은 뭐였어요?"
            seb"이 책은……{cps=2} {/cps}제가 대학에서 공부하는 교재 같은거예요……"
            show cia shock
            cia"대학교에 다니고 있어욧?!"
            show seb talk
            seb"제가 예전에 말 해줬던걸로 기억 하는데요?"
            show cia think
            cia"흠……"
            extend" 왠지 그랬던거 같기도 하고……"
            hide cia think
            show stephan talk:
                zoom 1.4 yalign -0.2 xalign 1.0
            stephan"책 이라니?{cps=2} {/cps}지금 무슨 책을 말 하고 있음?"
            show seb
            show ev book2 with dissolve:
                xalign 0.2 yalign 0.7
            seb"이건데, 제가 대학교에서 공부하는 교재 같은거예요"
            show stephan shock
            show effect1
            play music "bgm/beat3.mp3"
            play sound "se/shock.ogg"
            stephan"{size=45}대학교?!{/size}" with lshake
            stephan"호호호혹시 세바스찬이 대학생 이거나 하진 않겠지?!"
            show seb talk
            hide effect1
            seb"맞습니다만……?"
            stephan"근데 시아가 분명 여기에서 일하는 정식적인 가정부 라고 했는데?!"
            show ev book2:
                linear 0.4 yalign 1.0
            $ renpy.pause(0.4)
            hide ev book2 with dissolve
            seb"뭐어……{cps=2} {/cps}시아 씨에 비하면 비교적 공식적 이긴 하죠"
            stephan"게다가 이름이 \'세바스찬(Sebastian)\'이잖아?"
            stephan"또, 양복도 입고있고……"
            stephan"또, 날 도련님 이라고 불러주고……"
            stephan"또, 깎듯한 자세와 예의까지……"
            stephan"난 여태까지 네가 가정부의 또다른 이름인, 집사 인 줄 알았다고!!"
            show seb
            seb"확실히 그렇게 생각 하셨을 수도 있겠네요"
            seb"하지만 제가 여기서 일 하는 건 그냥 아르바이트 같은거예요"
            seb"대학교 등록금은 일단 장학금 으로 어떻게든 되지만, 집세가 좀 걱정이라서……"
            show stephan sad
            show effect2
            play sound "se/shock2.mp3"
            stephan"…………"
            hide effect2
            show seb shock
            seb"왜 그렇게 실망 한 표정을 지으시는 거예요?!"
            show stephan sad2
            stephan"이름이 세바스찬 이잖아!"
            stephan"뭔가 태어날때 부터 천재적인 집사의 능력을 타고 났을 거 같은 느낌이랄까……"
            show seb talk
            seb"뭔가 슬픈 능력이네요……"
            show seb shock
            seb"그보다 왜 이름이 세바스찬 이라고 해서 집사라고 생각 하시는거죠?!"
            seb"꽤 흔한 이름 같은데……"
            stephan"세바스찬은 아무리 생각해도 집사 스러운 이름 이잖아!"
            seb"보통은 \'알프레드(Alfred)\'아닌가요?"
            stephan"세바스찬 이지 않나?"
            show seb talk
            seb"도련님, 애니를 너무 많이 보셨어요"
            show stephan shock2
            stephan"(뜨끔)"
            show seb
            seb"근데 생각해보니까 집사나 가정부나 별 다를게 없는거 같네요"
            show stephan talk
            stephan"아니지, 집사가 가정부보다 한단계 레벨이 높지!"
            show seb talk
            seb"그래요……?"
            stephan"가정부가 로리콘 이라면, 집사는 페도 같은 느낌?"
            seb"머,{cps=2} {/cps}뭔가 기분 나쁜 느낌이네요;;"
            show stephan smile2
            stephan"아, 혹시 세바스찬이 맨날 양복을 입는 이유가, 집사 느낌을 내고 싶어서 인가?"
            show seb
            seb"그런건 아니에요"
            show stephan talk
            stephan"그럼 왜 입고 있어?{cps=2} {/cps}하루종일 입고있으면 불편할거 아니야?"
            show seb blush
            seb"그,{cps=2} {/cps}그건……"
            hide stephan talk
            show cia talk:
                zoom 1.3 yalign -1.5 xalign 1.0
            cia"생각해보니까 저도 궁금해요.{cps=2} {/cps}왜 매일 양복을 입고 출근 하시는거예요?"
            show cia smile
            cia"혹시 이웃들한테 대기업에 다닌다고 거짓말을 해서?!"
            seb"그런게 아니라……"
            seb"…………"
            stop music
            play sound "se/think.mp3"
            play bgs"bgs/birds.mp3"
            scene bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(614,231,666,375),0.0) with flash
            show cia talk:
                zoom 1.6 xalign 0.6 yalign -0.3
            show grandpa:
                zoom 1.8 xalign 0.5
            grandpa"평일은 점심부터 밤 8시 까지 있을 수 있다고 했나?"
            seb"네!"
            cia"…………"
            grandpa"아, 내가 깜빡하고 있었군"
            show grandpa:
                linear 0.4 xalign 0.3
            grandpa"이 아이의 이름은 \'쿠이바(Caoimhe)\'……{cps=2} {/cps}아니, 카오이메……{cps=2} {/cps}아니, 캄헤……"
            show grandpa shock
            grandpa"음……"
            extend"발음하기가 힘들구나"
            show cia shock
            cia"하,{cps=2} {/cps}할아버님!{cps=2} {/cps}그냥 \'시아(Cia)\'라고 불러주세요!"
            show grandpa talk
            grandpa"음─{cps=2} {/cps}그렇다는 구나"
            show grandpa
            grandpa"시아, 이쪽은 세바스찬 쟝 이라고 한단다……"
            grandpa"앞으로 같이 일하게 될 사람 이니까 친하게 지내고……"
            show cia talk:
                linear 0.4 xalign 0.8
            cia"음……"
            show cia smile
            cia"양복이 정말 잘 어울리세요!"
            play sound "se/heartbeat.mp3"
            seb"(두근)"
            stop bgs
            scene black with eyeshut
            scene bg mansion_hall at Zoom((1280,720),(0,154,646,363),(0,154,646,363),0.0) with eyeopen
            show cia talk:
                zoom 1.3 yalign -1.5 xalign 1.0
            show seb blush:
                zoom 1.4 yalign -0.2 xalign 0.0
            show effect1
            play sound "se/shock.ogg"
            play music "bgm/beat3.mp3"
            seb"{size=45}그,{cps=2} {/cps}그냥 저만의 이유가 있는거예요!{/size}" with lshake
            hide effect1
            show cia think
            cia"그렇게 반응 하니까 더 궁금해지네요……"
            show seb shock
            seb"전 이제 곧 있으면 퇴근 시간 이라서 이만……!"
            play sound "se/footsteps_running.mp3"
            show seb shock:
                linear 0.4 xalign -2.0
            stephan"…………"
            stop music
            play bgs"bgs/night.mp3" fadeout 1.5 fadein 1.5
            scene bg grandpa_mansion_night at Zoom((1280,720),(508,325,250,141),(460,279,409,230),0.6) with movedown
            show seb think:
                zoom 1.4 xalign 0.7 yalign -0.2
            seb"후우~{cps=2} {/cps}심장이 터지는 줄 알았네……"
            show grandpa talk:
                zoom 2.0 xalign -2.0 yalign 0.0
                linear 2.5 xalign 0.0
            play sound "se/footsteps_concrete.mp3"
            $ renpy.pause(2.5)
            grandpa"어이고─ 어이고─"
            grandpa"벌써 가려는 게냐……?"
            show seb
            seb"네에……"
            show seb talk
            seb"설마 할아버님, 이 늦은 시간에 계속 여기에 있으셨어요?"
            seb"많이 추우실텐데……"
            show grandpa
            grandpa"허허허……{cps=2} {/cps}그냥 잠깐 옛날 추억에 젖어 있었더니 시간 가는 줄 몰랐지"
            hide grandpa with dissolve
            show grandpa with dissolve:
                zoom 1.4 xalign 0.0 yalign -0.7
            grandpa"그럼 조심해서 돌아 가거라"
            show seb
            seb"넵,{cps=2} {/cps}할아버님도 안녕히 주무세요"
            stop bgs
            stop music
        "거절 한다.":
            $ not_drink = True
            scene bg mansion_hall at Zoom((1280,720),(0,154,646,363),(0,87,382,215),0.0) with dissolve
            show stephan:
                xalign 0.5 yalign 1.0
            stephan"아냐, 난 괜찮아"
            stephan_think"잠깐 밖에 나가서 바람이나 쐐야겠다"
            play sound "se/footsteps_wood.mp3"
            show stephan:
                linear 2.0 xalign 0.4 zoom 1.7 yalign -2.0
            $ renpy.pause(2.6)
            scene black with movedown
            $ renpy.pause(0.5)
            stop music
            play bgs "bgs/night.mp3"
            scene bg grandpa_mansion_night at Zoom((1280,720),(508,325,250,141),(460,279,409,230),0.6) with dissolve
            show stephan yawn:
                zoom 1.5 xalign 0.6 yalign -0.2
            stephan"응~차아~!"
            "나는 상쾌한 바깥 공기를 들이키면서 크게 기지개를 켰다."
            "밤이라 그런지 조금 쌀쌀한 감이 있다.{cps=2} {/cps}역시 9월달의 가을 공기 인가"
            show stephan
            stephan_think"근데 여기 정말 추억 돋네"
            stephan"훗……"
            stephan_think"내가 여기서 살고 있었을때, 꽤 많은 일이 있었지……"
            play bgs"bgs/birds.mp3"
            scene bg grandpa_mansion_eve at Zoom((1280,720),(0,0,1280,720),(704,274,576,323),0.0) with memory
            show grandpa shock:
                zoom 1.8 xalign 0.5 yalign -0.2
            stephan"할부지! 할부지!{cps=2} {/cps}저기 서서 가만히 서 있어봐!"
            show grandpa shock with dissolve:
                zoom 1.2 xalign -0.2 yalign -0.2
            grandpa"이,{cps=2} {/cps}이렇게 말이냐?"
            stephan"응!"
            play music "bgm/sirius4.mp3"
            stephan"자!{cps=2} {/cps}이걸로 네녀석의 퇴로는 막았다"
            stephan"괴도 아서!"
            stephan"드디어 엘리자베스의 복수를 할 수 있겠……"
            stop music
            scene bg grandpa_mansion_night at Zoom((1280,720),(508,325,250,141),(460,279,409,230),0.0) with flash
            show stephan blush:
                zoom 1.5 xalign 0.6 yalign -0.2
            show effect1
            play bgs "bgs/night.mp3"
            play sound "se/shock.ogg"
            play music "bgm/beat3.mp3"
            stephan"{size=45}뭐야뭐야?!{/size}" with lshake
            stephan"왜 떠올라도 이딴 흑역사만 나오는거냐고!"
            hide effect1
            "안 되겠다……"
            "분위기 좀 잡으려고 과거를 회상 했다간 기분이 잡쳐버릴지도 모른다."
            show stephan mad
            stephan_think"그보다 내가 인생을 어떻게 살아 왔길래 남는 게 이거 뿐인거지?!"
            show stephan think
            stephan_think"아니야 아니야……{cps=2} {/cps}분명 덜 쪽팔리는 기억이 있을거야……"
            play sound "se/think.mp3"
            scene black with flash
            play bgs"bgs/people.mp3"
            centered"중학교 2학년 때"
            scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(276,107,485,273),0.0) with moveup
            show stephan smile2:
                zoom 1.8 xalign 0.5 yalign 0.1
            $ extra_name = '같은 반'
            extra"야, 지금 교탁에 서서 뭐하냐?"
            extra"그보다 왜 교복 위에 그런 스웨터를……"
            stephan"내 이름은 스테반이 아니다!!"
            stephan"나는 이 나라를 암흑으로 부터 지키는 오리엔스의 수호자……"
            stephan"{size=45}바로 레ㄷ……{/size}"
            stop music
            play bgs"bgs/night.mp3"
            scene bg grandpa_mansion_night at Zoom((1280,720),(508,325,250,141),(460,279,409,230),0.0) with flash
            show stephan blush:
                zoom 1.5 xalign 0.6 yalign -0.2
            stephan"…………"
            show effect1
            play sound "se/shock.ogg"
            show stephan fear:
                linear 0.4 xalign 2.5
            stephan"{size=45}으아아아아아아──!{/size}" with lshake
            play sound "se/move.mp3"
            stop bgs
            scene black with moveright
            centered"얼마 후……"
            play bgs"bgs/night.mp3"
            scene bg grandpa_mansion_night at Zoom((1280,720),(508,325,250,141),(701,337,353,198),0.0) with moveright
            show stephan mad:
                zoom 1.8 xalign 0.5 yalign -0.2
            stephan_think"젠장, 기분 전환으로 밖에 나왔는데, 오히려 더 기분 나빠졌어"
            show stephan mad:
                linear 0.2 xalign 0.6
            play sound "se/fall.ogg"
            $ renpy.pause(0.3)
            show stephan mad with sshake:
                linear 0.2 xalign 0.5
            stephan_think"타임머신을 만들어서 과거의 나를 죽인 뒤, 타임 페러독스를 발생 시켜버리고 싶다고!"
            show stephan mad:
                linear 0.2 xalign 0.6
            play sound "se/fall.ogg"
            $ renpy.pause(0.3)
            show stephan mad with sshake:
                linear 0.2 xalign 0.5
            $ extra_name = '작은 목소리'
            extra"{size=19}……도 잘 지내고 있어……{/size}"
            show stephan talk
            stephan"응?"
            "쪽팔림 때문에 잔디 위에서 가상의 이불 킥을 날리던 중에 작은 목소리가 들려왔다."
            "혹시 할아버지 인가 싶었다.{cps=2} {/cps}하지만 이렇게 늦은 시간에 왜?"
            play sound "se/footsteps_concrete.mp3"
            show stephan talk:
                linear 1.5 xalign -2.0
            "목소리가 나오는 쪽으로 이동했다."
            scene black with moveleft
            $ renpy.pause(0.5)
            play music "bgm/sad4.mp3"
            scene bg ravine_night with moveleft
            show stephan talk:
                zoom 1.4 xalign 2.0 yalign -0.3
                linear 0.6 xalign 0.3
            stephan"어……?"
            "저택에서 서쪽으로 몇 분 정도 걸으면 나오는 장소에 도착했다."
            show stephan think
            "근데 뭔가 많이 익숙한 느낌이 들었다……{cps=2} {/cps}혹시 \'데자뷰(Déjà vu)\'?"
            stephan_think"생각해보니까 어렸을때 할아버지랑 여기서 바베큐 해먹었던 적이 있었지……"
            "하지만……{cps=2} {/cps}그거 말고 또 다른 느낌도 들었다."
            "어디선가 비슷한 장소를 들어 본 것 같은 느낌……"
            scene black with eyeshut
            "분명 할아버지 일기장에서도 여기랑 비슷한 절벽이 나왔던 것 같기도 하고……"
            scene bg ravine_night with eyeopen
            show stephan talk:
                zoom 1.4 xalign 0.3 yalign -0.3
            stephan_think"아!"
            extend" 그래!{cps=2} {/cps}여긴 분명 할머니랑 할아버지가 처음 만났던 장소였어!"
            extra"{size=19}너무 쓸쓸하고……{/size}"
            "내가 느꼈던 기시감의 이유를 파악하고 있던 동안 목소리가 또다시 들렸다."
            show stephan:
                linear 0.5 xalign -2.0
            scene black with moveleft
            "마치 빛에 이끌려가는 나방처럼, 자연스럽게 목소리가 들렸던 쪽으로 향했다."
            $ renpy.pause(0.5)
            scene bg ravine_grave_night with Dissolve(1.0)
            show grandpa:
                zoom 1.7 xalign 0.2 yalign -0.2
            "역시나 내 예상대로 방금 전 까지 할아버지의 목소리 였다."
            "……하지만 대화 상대는 누구 였을까?"
            grandpa"여보……{cps=2} {/cps}조금만 기다려줘……"
            grandpa"당신이 도대체 무슨말이 하고 싶었는지……{cps=2} {/cps}반드시 알아 낼테니까……"
            show grandpa mad
            grandpa"물론……{cps=2} {/cps}그런다고 해서 내 죄가 사라지는 건 아니겠지만……"
            stephan_think"죄?"
            stephan"할아버지"
            play sound "se/search_bag.mp3"
            show grandpa shock with dissolve:
                zoom 1.9 xalign 0.5 yalign -0.1
            grandpa"어어─!{cps=2} {/cps}스, 스테반 이구나……!"
            grandpa"여, 여긴 어쩐 일로 왔느냐?"
            stephan"잠깐 기분전환 겸 산책을 하다가 왔어요……{cps=2} {/cps}근데 저 무덤은……?"
            show grandpa talk
            grandpa"어……{cps=2} {/cps}네 할머니의 무덤 이란다……"
            stephan"…………"
            scene bg ravine_grave_night at Zoom((1280,720),(0,0,1280,720),(388,120,827,465),0.7) with dissolve
            "나는 묘비를 좀 더 자세히 살펴봤다."
            nvl clear
            narrator_nvl"\'메리 토머, 1933년 3월 5일 ~ 1972년 6월 7일\'……"
            narrator_nvl"\'지금까지 고마웠어\'"
            stephan_think"묘비명이 조금 특이하네……"
            grandpa"허허……{cps=2} {/cps}내가 여기서 혼잣말을 하고 있었다는 게 들키니까 조금 부끄럽구나"
            scene bg ravine_grave_night at Zoom((1280,720),(388,120,827,465),(0,0,1280,720),0.5) with dissolve
            show grandpa:
                zoom 1.9 xalign 0.5 yalign -0.1
            stephan"평소에도 이렇게……{cps=2} {/cps}할머니랑 \'대화\'하시는 건가요?"
            grandpa"뭐 그렇지……"
            grandpa"계속 집안에만 있으면 건강에 좋지 않지만, 그렇다고 멀리 산책가기엔 몸이 안 따라주니까 말이다"
            show grandpa shock
            grandpa"그, 그런데 이렇게 혼잣말 하는 걸 들키니까 조금 부끄럽구나……"
            stephan"전혀 그렇게 생각 하실 필요 없어요!"
            stephan"서로 많이 사랑하고 있었다는 증거 잖아요"
            show grandpa talk
            grandpa"사랑……"
            grandpa"과연 메리도 그렇게 생각 하고 있을련지……"
            stephan"무슨 뜻이에요?"
            show grandpa think
            grandpa"아무것도 아니란다"
            grandpa"그냥 내가 원했던 걸 착각하면서 받은 벌 같은거니까……"
            show grandpa cough
            $ renpy.vibrate (0.3)
            grandpa"콜록{cps=2} {/cps}콜록"
            stephan"음……"
            "할아버지의 말슴이 나에겐 조금 난해하게 들렸다."
            show grandpa talk
            grandpa"스테반……{cps=2} {/cps}혹시 잠깐만 같이 어울려 줄 수 있겠니?"
            play sound "se/search_bag.mp3"
            scene ev sky_night with dissolve
            "나는 할아버지 옆에 앉아서 밤 하늘을 올려다 봤다."
            "……거의 산 꼭대기나 마찬가지라 그런지 별이 잘 보인다."
            grandpa"역시 젊은 게 좋은것 같구나……"
            grandpa"나이가 들면……{cps=2} {/cps}한때 겪었던 일이나, 과거의 고생이 갑자기 떠오르면서 괴로워"
            stephan_think"내가 갑자기 과거의 흑역사가 떠오르고 하는거랑 비슷한건가……"
            stephan"그래도 젊어서 고생하면 커서 세상 사는 게 좀 편해진다던데요?"
            grandpa"삶의 \'이유\'가 있다면 그럴 수 있겠지"
            grandpa"근데 할아버지는 조금 다르구나……"
            grandpa"한가지 고민이 있는데……{cps=2} {/cps}혹시 들어줄 수 있겠니?"
            stephan"네, 제가 도움이 될 수 있을진 모르겠지만……"
            play music "bgm/sad5.mp3"
            grandpa"메리와 사별 후, 내가 왜 아직도 살아있는지……{cps=2} {/cps}이유를 모르겠어"
            grandpa"지금까진 계속 \'죽지 않으니까 살아있었을 뿐\'……"
            stephan"살아있는데 정말 이유 같은 게 있어야 해요?{cps=2} {/cps}그냥 가족을 위해서라도 오래 사는거죠"
            grandpa"…………"
            grandpa"그래, 네 말대로 지금 내가 딱 그런 상황이야"
            grandpa"아무런 이유도 없이 살아가고 있어"
            grandpa"……메리는 이걸 \'인과율의 페러독스\'라고 말 했었는데. 혹시 아는가?"
            stephan"네?{cps=2} {/cps}음……"
            "생각해보니까 한때 할아버지가 나에게 준 \'탐정의 서\'에도 비슷한게 기록 되어 있었다."
            stephan"……조금은 알 것 같아요"
            nvl clear
            narrator_nvl"세상의 모든 결과엔 반드시 원인이 있다.{cps=2} {/cps}\'인과율(因果律)\'"
            narrator_nvl"그 결과의 원인 역시 또다른 원인의 결과 이기도 하다."
            narrator_nvl"그렇다면 이 모든것의 \'시작\'은 무엇인가?"
            narrator_nvl"인과율 대로라면 만물의 시작을 발생케 한 원인도 있어야 한다."
            narrator_nvl"그러면 그 시작의 원인의 원인은 무엇인가?"
            narrator_nvl"그리고 그 원인의 원인의 원인의 원인의……"
            nvl clear
            narrator_nvl"……이런식으로 원인은 끝이 없다."
            narrator_nvl"즉, 모든것의 시작은 \'없다\'."
            narrator_nvl"그리고 인과율에 의하면, 시작이 없는 지금 우리들의 존재는 \'모순\'된다."
            narrator_nvl"하지만 우리는 지금 존재하고 있다."
            narrator_nvl"그렇다는 건, 이 세상엔 \'원인이 없는 것\'도 존재 한다는 뜻이 아닌가?"
            narrator_nvl"그것이 바로 양자역학 에서 말 하는 \'불확정성 원리(不確定性原理, uncertainty principle)\'와 비슷 한 거다."
            narrator_nvl"발생 원인이 없기 때문에 명확한 계산을 할 수 가 없다.{cps=2} {/cps}그저 확률적으로만 존재 할 뿐"
            "……대충 이런 내용으로 기억하고 있다."
            "근데 다시 생각해봐도 참 어려운 말이 많다."
            "어쩌면 내가 양자역학을 별로 좋아하지 않다 보니까 비슷한 내용이 언급되는 탐정의 서에도 자동적으로 거부 반응을 보이는 걸까?"
            "난 인과율의 페러독스 라는거에 대해서 꽤 회의적인 마음을 가지고 있다."
            "우선 세계에서도 그렇지만 과학, 특히 물리학 에서는 인과율 이라는 건 절대 불변의 룰.{cps=2} {/cps}즉, \'진리\'다."
            "그런데 여기선 그 진리를 부정한다."
            "만약 이 책에 쓰여진대로 정말 인과율에는 모순이 존재한다면 세계의 과학엔 혼돈이 발생할 수도 있다."
            "……장난 하는 게 아니다."
            "진지하게 혼돈이 찾아온다.{cps=2} {/cps}왜냐면 지금까지 맞다고 증명된 이론들은 인과율을 바탕으로 하기 때문에"
            "그러니 지금까지 나온 모든 이론들은 수정을 거쳐야 하고, 다시 재 증명을 해야한다."
            "그럼에도 불구하고 내가 여기에 써져있는 인과율의 페러독스 이론에 절대 반대가 아니라 \'회의적\'인 생각이 드는 이유는 따로있다."
            "여기선 \'불확정성 원리(不確定性原理, uncertainty principle)\'라는 것을 예로 언급하기 때문이다."
            "자세한건 너무 기므로 인터넷 검색을 추천하겠지만……{cps=2} {/cps}얘를 간단히 설명하자면, \'관측하기 전 까지는 절대로 100\%는 없다\'."
            "어째서 이게 인과율의 페러독스의 예 인가?"
            "……그것도 설명하면 꽤 길지만"
            "수학의 계산은 절대적이다.{cps=2} {/cps}그러니 충분한 자료만 있다면 100\%의 확률 까지 끌어내는것이 가능하다."
            show falling_apple with dissolve:
                xalign 0.5 yalign 0.0
            "예를 들면 1Km 상공에서 사과를 떨어뜨린다고 생각해보자."
            show falling_apple:
                linear 0.4 yalign 2.0
            "공기의 저항이랑 사과의 질량, 중력 가속도 등을 전부 이용해서 계산을 하면 땅에 떨어질때 사과는 쪼개진다는 결과가 나온다."
            hide falling_apple
            "여기서 사과가 쪼개진다의 원인은 공기의 저항, 사과의 질량, 중력 등 이다."
            "이건 굳이 실험을 하지 않아도 변수만 없다면 100\%의 확률로 맞다."
            "하지만 양자역학 에서는 누군가 실험을 하고 관측을 하지 않는 한은 계산 만으론 100\%를 끌어낼 수 없다."
            "이유는 인과율의 페러독스 이론에서 설명 했듯이 \'원인\' 이 없거나 부족하기 때문에"
            "\'알베르트 아인슈타인(Albert Einstein)\'은 우리가 아직 충분한 자료를 찾지 못해서 이지, 양자역학도 반드시 100\%의 확률로 끌어내는 것이 가능하다고 주장했다."
            "근데 지금은 수많은 실험을 통해서 아인슈타인이 틀렸다는 게 받아들여지고 있다."
            "……아오 머리 아파라"
            grandpa"메리가 말 해준 \'인과율의 페러독스\'처럼, 지금 나도 아무 이유없이 목숨을 유지 하고 있는거 같아……"
            grandpa"과거에 난 돈을 위해서만 살아 왔었고,{cps=2} {/cps}훗날 메리 덕분에 막대한 부를 쌓을 수 있게 됐지"
            grandpa"그걸로 난 먹고싶은 걸 먹고, 하고싶은 걸 하고, 보고싶은 걸 보고……"
            grandpa"결국 메리가 죽게 되면서 내 꿈도 함께 죽었지……{cps=2} {/cps}만나고 싶은 사람도 없고……{cps=2} {/cps}이젠 살아 있을 이유도 없어"
            grandpa"다 늙은 할아버지 한테 원하는 소망 같은거라곤 있을리가 없잖아?{cps=2} {/cps}그냥 아들과 손자가 행복하게 살기만을 바랄 뿐이지……"
            grandpa"근데 그 바램은 내 삶과는 아무런 관련이 없어……{cps=2} {/cps}내가 죽어도 얼마 후면 다시 아무 일도 없었듯이 세상은 돌아갈테니까……"
            grandpa"젊은이가 죽으면 사회에서는 귀중한 인적 자원을 잃게 돼, 하지만 늙은 내가 죽는다고 해서 이 사회엔 아무런 손실이 없어……"
            grandpa"난 뭘 위해서 얼마 남지 않은 목숨을 유지 하고 있는 걸까……{cps=2} {/cps}왜 스스로 끝을 내려 하지 않고, 끝이 나에게 찾아 올때까지 기다리고 있을까"
            grandpa"이미 내 존재는 인과를 벗어났다고 봐야겠지……"
            "나는 할아버지의 말을 적극적으로 부정하고 싶었다."
            "하지만……"
            extend" 확실히 할아버지가 돌아가신다고 해서 이 세상이 망하거나 하진 않는다."
            "할아버지는 나에게 진지하게 고민을 상담 했으니 나 역시도 입에 발린 소리는 하고 싶진 않았다."
            "그럼 내가 할 수 있는 건 뭔가?"
            stop music
            stephan"아니요……{cps=2} {/cps}할아버지는 인과를 벗어나지 않았어요"
            grandpa"……?"
            play sound "se/search_bag.mp3"
            scene bg ravine_grave_night at Zoom((1280,720),(388,120,827,465),(0,0,1280,720),0.5) with dissolve
            show stephan smile:
                zoom 1.8 xalign 0.6
            stephan"며칠 전에 저에게 연락을 줬고, 저보고 할머니의 마지막 소원을 들어 달라고 한 건 바로 할아버지 자신이에요"
            stephan"아직 할아버지가 잘 모르고 있을 뿐이지, 분명 할아버지 한테도 이루고 싶은 꿈이 있는거예요!"
            grandpa"…………"
            grandpa"그래……"
            extend" 확실히 네 말대로 최근엔 그런 느낌이 드는구나"
            grandpa"몇 년 전에 네가 여기로 온 이후……{cps=2} {/cps}그때부터 내가 삶을 계속 유지하고 있는 이유를 찾았었 던 걸지도 몰라"
            grandpa"…………"
            grandpa"정말 사랑한다……{cps=2} {/cps}스테반"
            stop bgs
    scene black with Dissolve(1.0)
    centered"9월 16일 화요일"
    centered"오전 7시 50분"
    play music "bgm/beat1.mp3"
    scene bg school_hall with moveleft
    show stephan
    stephan_think"어제 숙제도 끝냈고, 평상시 처럼 지각도 안했고, 윌리 폰도 챙겼고"
    show stephan smile
    stephan_think"왠일로 빠진게 하나도 없네!"
    "나는 가뿐한 마음으로 교실 안으로 들어 갔다."
    play sound "se/door_open.ogg"
    scene bg school_classroom with moveleft
    "교실 안엔 소수의 학생들만 있었다."
    show stephan
    stephan_think"뭐 보통 이 시간대엔 이정도만 있지만"
    "나는 자리에 앉아서 가방에서 책을 꺼내 윌리가 올때까지 읽기로 했다."
    scene black with dissolve
    play bgs "bgs/people.mp3"
    centered"오후 9시 30분"
    scene bg school_classroom with dissolve
    "이제 곧 있으면 1교시가 시작된다."
    "하지만 어째서인지, 윌리는 보이지 않았다."
    play sound "se/footsteps_wood.mp3"
    show extra_social with dissolve:
        xalign -1.4 yalign 1.0
        linear 2.5 xalign 0.7
    $ extra_name = '담임 선생님'
    $ renpy.pause(2)
    extra"자―{cps=2} {/cps}수업 시작할테니까 빨리 자리에 앉아라"
    stop bgs
    show stephan talk at left
    stephan"선생님, 오늘 윌리 학교 안 왔어요?"
    extra"걔라면 오늘 아파서 병결 했다고 하더라"
    stephan"흐음―"
    extra"그보다 너, 왜 사회 교과서 안 꺼내?"
    show stephan shock at left
    stephan"익……!"
    stop music
    scene black with eyeshut
    stephan_think"오늘은 윌리가 병결……"
    stephan_think"아무래도 이 폰은 내일 줘야겠네"
    play music "bgm/beat2.mp3"
    centered"2교시"
    "2교시는 수학이다."
    "참고로 지금 난 자고 있는 것이 아니라, 명상을 하고있다."
    if not_drink == True:
        "아니면, 어제 할아버지와 나눴던 대화를 떠올리고 있다고 해야 할까……"
    else:
        "아니면, 내가 읽었던 일기장의 내용을 정리 한다고 해야 할까……"
    "쨌건, 그냥 아무 생각도 없이 자고 있는것 만큼은 절대 아니다."
    $ extra_name = '수학 선생님'
    extra"{size=25}오늘은 곱셈공식을 한 번 복습 해볼건데……{/size}"
    play sound"se/shock.ogg"
    extra"{size=45}스테반!{/size}" with lshake
    scene white with eyeopen
    scene bg school_classroom with Dissolve(1.0)
    stephan_think"끙……"
    show extra_math at right
    show stephan shock at left
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}히익!{/size}" with lshake
    hide effect1
    extra"혹시 곱셈공식 기억 하고있어?"
    stephan"왜 저한테 그런 질문을?"
    show stephan blush
    stephan"혹시 저 오늘도 코 골았어요?!"
    extra"아니,{cps=2} {/cps}그냥 네가 너무 행복하게 자는 게 짜증나서"
    show stephan shock
    stephan"너무하잖아요……{cps=2} {/cps}저번에 수업을 방해만 안 한다면 자도 괜찮다면서……"
    extra"나도 오늘은 정말 자고 싶거든"
    show stephan smile2
    stephan"혹시 질투?"
    extra"그래,{cps=2} {/cps}질투심 때문에 수업에 브레이크가 걸렸어"
    extra"{size=45}너{cps=2}.{/cps}때{cps=2}.{/cps}문{cps=2}.{/cps}에{/size}"
    show stephan shock
    stephan"그,{cps=2} {/cps}그게 왜 제 탓이에요?!"
    extra"그보다 내 질문에 대답이나 해.{cps=2} {/cps}곱셈공식 기억 하고 있어?"
    menu:
        "죄송합니다 (진실)":
            show stephan shock2
            stephan"죄,{cps=2} {/cps}죄송합니다"
            stephan"하지만 다른 애들도 중학교 때 배운건 다 까먹었을걸요?!"
            extra"호오?{cps=2} {/cps}그럼 물어보도록 하지"
            hide stephan shock2
            "선생님은 아무나 짚어서 질문했다."
            extra"너,{cps=2} {/cps}acx² + (ad + bc)x + bd를 간단히 하면 뭔지 말해봐"
            stephan_think"지,{cps=2} {/cps}진짜 어렵네;;"
            $ extra_name = '학생'
            extra"음……{cps=2} {/cps}(ax+b)(cx+d)인가요?"
            $ extra_name = '수학 선생님'
            extra"그래 정답이야"
            show stephan shock with dissolve
            extra"어때?{cps=2} {/cps}알고 있잖아?"
            stephan"그,{cps=2} {/cps}그건!"
            "생각해보니까 우리 학교는 동네에서 손 꼽힐 정도로 수준이 높은 곳이다."
            "약 70\%정도의 학생들이 삶을 숨쉬는 거랑 공부만 한다고 생각하면 된다."
            "……그리고 난 30\%에 속한다."
            stephan_think"당연히 풀 줄 알겠지……"
            extra"넌 수업 끝나고 쉬는 시간에 남아서 같이 공부 하자"
            show stephan fear
            show effect1
            play sound "se/shock.ogg"
            stephan"{size=45}히익!{/size}" with lshake
            stop music
            play sound "se/move.mp3"
            scene black with moveright
            centered"쉬는 시간"
            play music "bgm/happy5.mp3"
            play bgs "bgs/people.mp3"
            scene bg school_classroom with moveright
            "쉬는 시간 인데도 나는 선생님과 1:1 과외를 하게 됐다."
            stephan_think"흥미 없는 과목을 아무리 공부 하려고 해도 머리속에 들어올리가 없지"
            stephan"왜 계속 시간 낭비를 하는지 모르겠네……"
            "나는 자리에 앉아서 책을 읽기로 했다."
        
        "당연히 알죠! (거짓)":
            show stephan shock2
            stephan"다,{cps=2} {/cps}당연히 알죠!"
            stephan"중학교때 배운거잖아요!"
            extra"그럼 acx² + (ad + bc)x + bd를 간단히 하면 뭐지?"
            show stephan shock
            stephan_think"쉩"
            stephan_think"저 무시무시한 식은 뭐지?!"
            show stephan shock2
            stephan"가,{cps=2} {/cps}간단 하다의 기준이 뭐죠?"
            stephan"저 식을 아무리 짧게 해도 복잡 할 거 같은데……"
            extra"잔머리 부리지 마"
            stephan_think"어떻게 해서든……"
            stop music
            scene black with eyeshut
            "나는 눈을 감고 진지하게 생각 하기로 했다."
            "마치 \'쿠로키의 농구\'에 나오는 \'더 존(The Zone)\'에 들어간듯한 쩌는 집중력을 발휘하는거다."
            stephan_think"분명 뭔가 방법이 있을거야……"
            stephan_think"굳이 머리를 쓰지 않아도 그 문제를 풀 수 있는 환상의 방법이……"
            play sound "se/heartbeat.mp3"
            "그때……{cps=2} {/cps}내 머릿속에 한 가지 생각이 스쳐 지나갔다."
            play music "bgm/sirius4.mp3"
            show stephan smile2:
                xalign 0.5 yalign -0.2 zoom 1.4
            stephan"크크크큭……"
            scene white with eyeopen
            scene bg school_classroom with Dissolve(0.5)
            show stephan smile2 at left
            show extra_math at right
            stephan"선생님……{cps=2} {/cps}정답을 찾았습니다"
            extra"뭔데?"
            stephan"acx² + (ad + bc)x + bd의 답은 2(a + b + c + d + x)입니다!"
            extra"뭔소리야, 답은……"
            show effect1
            play sound "se/shock.ogg"
            stephan"{size=45}잠깐!{/size}" with lshake
            stephan"지금부터 제가 검산을 해보도록 하죠!"
            scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,13,715,402),2.8)
            play sound "se/footsteps_wood.mp3"
            $ renpy.pause(3.0)
            scene ev black_board with dissolve
            play sound "se/chalk.mp3"
            show math1 with moveright
            stephan"제가 지금 증명 하려는 게 acx² + (ad + bc)x + bd = 2(a + b + c + d + x)이잖아요?"
            stephan"여기서 양 변에 같은 숫자를 곱하거나 더하거나 빼도 항상 같다는 게 성립이 돼야 합니다"
            extra"그치"
            stephan"그럼 한 번 양 변에 같은 숫자를 곱해보도록 하죠"
            play sound "se/chalk.mp3"
            show math2 with moveright
            stephan"좌변 우변 둘 다 0 입니다"
            stephan"이번엔 곱했던 값과 같은 값을 나눠 보도록 하죠"
            play sound "se/chalk.mp3"
            show math3 with moveright
            stephan"식이 이렇게 되겠죠?"
            play sound "se/chalk.mp3"
            show math4 with moveright
            stephan"여기서 양 변에 같은 분수가 있으므로 그 둘은 제거 시켜주면……"
            play sound "se/chalk.mp3"
            show math5 with moveright
            stephan"짜잔!"
            stephan"acx² + (ad + bc)x + bd = 2(a + b + c + d + x)임이 증명 됐습니다!"
            stop music
            scene bg school_classroom with movedown
            show stephan smile2 at left
            show extra_math at right
            stephan_think"훗,{cps=2} {/cps}이제 하실 말씀ㅇ……"
            play music "bgm/beat2.mp3"
            show stephan shock
            extra"뭔소리냐"
            extra"어느 숫자든 양 변에 0을 곱하면 당연히 0이 되잖아"
            extra"그리고 분자가 0이 될 순 없어,{cps=2} {/cps}네가 한 행동은 수학을 모욕 한거라고?"
            stephan"저,{cps=2} {/cps}정말 이에요?"
            extra"그래, 네 논리 대로라면 수학은 벌써 망했단다"
            extra"잠깐……"
            extend" 네가 항상 수학을 이렇게 생각하니까 힘들어해 하는 걸지도 몰라……"
            extra"흠흠……{cps=2} {/cps}그래도 이렇게 열심히 한 걸 봐서 딱히 뭐라고 하진 않도록 하지"
            extra"얼른 자리로 돌아 가"
            stephan"네에……"
            stop music
            play sound "se/move.mp3"
            scene black with moveright
            centered"쉬는 시간"
            play music "bgm/happy5.mp3"
            play bgs "bgs/people.mp3"
            scene bg school_classroom with moveright
    play sound "se/footsteps_running.mp3"
    $ renpy.pause(3)
    play sound "se/door_open.ogg"
    $ renpy.pause(0.6)
    play sound "se/footsteps_wood.mp3"
    show lisa talk:
        xalign 2.0 yalign 1.0
        linear 2.0 xalign 0.9
    $ renpy.pause(2)
    $ lisa_name = '어떤 여자'
    show effect1
    play sound "se/shock.ogg"
    lisa"{size=45}혹시 윌리-윌리 어디 있는지 알아?!{/size}" with lshake
    hide effect1
    "그저 얌전히 자리에 앉아서 책—라노벨—을 읽고있었는데 금발의 여성이 나한테 소리를 질렀다."
    "한 번도 만나본 기억은 없다."
    show stephan shock2 at left
    stephan"나……{cps=2} {/cps}보고 하는 말 인가?"
    lisa"지금 여기 너 말고 누가있어?"
    "굳이 따지자면 아주 많이 있다."
    "쉬는 시간이니까 말이야……"
    stephan_think"근데 방금 윌리-윌리 라고 하지 않았나?"
    "윌리-윌리는 내가 고등학교 1학년때 축구부에서 윌리에게 붙여준 별명이다."
    "이유는, 예전에 녀석이 어떤 초등학생이랑 같이 축구 놀이를 하고 있었는데 그때 서로 슛에 이름을 붙이자는 규칙이 있었다."
    "근데 그때 걔가 붙인 자신의 슛의 이름이 \'태풍의 발차기\'라는 매우 진부한 이름이여서 내가 좀더 재미있게 바꿔서 윌리-윌리라고 부른거다."
    "하지만 아이러니하게도 현재 축부에서도 윌리를 그 별명으로 부르고 있다."
    "이유는 폭풍 같은 실력 이어서……"
    "참고로 나도 고1 땐 축구를 했었다."
    show stephan smile2 at left
    "당시 내 별명은 \'사골 국밥\'……"
    "이유는 내가 우리 팀의 중요한 단백질 공급원 이기 때문에!"
    show stephan shock at left
    "……가 아니라 하도 게임을 말아먹어서다."
    "그리고 그 이후론 축구 때려 쳤다."
    show stephan think at left
    stephan_think"그나저나, 쟤가 윌리를 윌리-윌리 라고 부르는 걸로 봐선,{cps=2} {/cps}축구부인가?"
    show stephan shock2 at left
    stephan"윌리라면……{cps=2} {/cps}오늘 병결 이라는 거 같던데……"
    "나도 모르게 긴장해버렸다."
    "모르는 사람이랑 대화를 할땐 항상 이렇단 말이지……"
    show lisa think
    lisa"이거 어쩌지……"
    stephan"용건을 말한다면 내가 나중에 전해 줄 수도 있는데?"
    lisa"음……{cps=2} {/cps}가급적이면 걔한테 직접 말하고 싶은데……"
    show stephan shock at left
    stephan_think"설마 이녀석, 윌리를 좋아하는 건 아니겠지?!"
    stephan_think"윌리를 별명으로 부르는 걸로 봐선 가능성이 아주 없진 않을지도?"
    "내가 살면서 비슷한 사람들을 많이 만나봤다."
    "나랑 윌리가 친하게 지내다 보니까 윌리를 좋아하는 여자들은 날 이용해서 어떻게든 녀석에 대한 정보를 얻으려고 하고……"
    show stephan mad at left
    "그럴때마다 얼마나 짜증났는지……"
    stephan_think"여자들은 왜 하나같이 좋아하는 사람이랑 같이 있을 이유를 찾고만 있는 걸까?"
    show effect1
    play sound "se/shock.ogg"
    stephan_think"{size=45}그냥 당당하게 가서 말하라고!!{/size}" with lshake
    hide effect1
    play music "bgm/smooth1.mp3"
    show stephan shock at left
    "……하지만 이해를 못하는 건 아니다."
    "나도 그런적이 있었으니까……"
    "좋아하는 애랑 같이 있기 위해서 혼자서 이런저런 핑계를 만들고, 조사를 해보고……"
    stephan_think"그렇게 생각하니까 저녀석의 마음도 조금 알거 같네……"
    show stephan:
        linear 0.5 xalign 0.6
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(210,153,902,507),0.0) with dissolve
    show stephan:
        zoom 1.4 yalign -0.2 xalign 0.35
    show lisa shock:
        zoom 1.4 yalign -0.5 xalign 1.0
    "나는 윌리를 짝사랑 하는 걸로 추정되는 여학생의 어깨에 손을 얹고, 공감 한다는 어투로 말했다."
    stephan"힘내는거야"
    show lisa shock
    lisa"어?"
    lisa"갑자기 무슨……"
    stephan"확실히 정보화 시대 이기는 하지만. 무조건 정보가 많다고 해서 유리한게 아니야"
    stephan"중요한 건 용기니까!"
    stephan"사랑은 머리로 생각한 길을 걷는 게 아니라, 가슴이 뛰는 길을 걷는거라고 생각해!"
    show stephan smile
    stephan_think"\'머리로 생각한 길이 아니라, 가슴이 뛰는 길을 걷는다.\'라……"
    stephan_think"{size=45}크~~!{/size}"
    stephan_think"내가 한 말이지만 정말 멋있었어~"
    show lisa talk
    lisa"…………"
    "상대방은 아무런 말이 없었다."
    "혹시 내가 한 말에 감명받아서?!"
    play music "bgm/beat3.mp3"
    show stephan shock
    lisa"너 지금 뭔 개소리야?"
    show effect1
    play sound "se/shock.ogg"
    show lisa shy
    lisa"{size=45}서,{cps=2} {/cps}설마 내가 윌리를 좋아한다고 생각 하는거야?!{/size}" with lshake
    hide effect1
    stephan"아니야……?"
    lisa"당연히 아니지!"
    lisa"오히려 반대라구!"
    show lisa mad
    lisa"지금 난 윌리-윌리를 패고 싶어 죽겠고만"
    show stephan shock:
        linear 0.5 xalign 0.0
    stephan"음?"
    stephan"걔가 뭘 잘못했어?"
    lisa"윌리-윌리  녀석……{cps=2} {/cps}그렇게 안봤는데!"
    show stephan talk
    stephan_think"아아……{cps=2} {/cps}윌리한테 차였구나……"
    stephan_think"잠깐……"
    show effect1
    play sound "se/shock.ogg"
    show stephan blush
    stephan_think"{size=45}힉익!{/size}" with lshake
    stephan_think"그럼 방금 내가 한 말은!!"
    stephan_think"{size=45}으아아아!{/size}{cps=2} {/cps}부끄러워어어!"
    hide effect1
    show stephan shock2
    stephan_think"그보다 쟤, 꽤 힘쎄보이는데, 윌리 고생 좀 하겠구만"
    show stephan smile2
    stephan_think"하지만 그것이 바로 윌리의 운명……"
    stephan_think"이거이거, \'스쿨 데이지\'같은 상황이 될 거 같네"
    "……딱히 윌리가 바람을 핀건 아니지만 서도, 한편으론 통쾌 하다는 생각이 들었다."
    show stephan shock
    "나의 피해의식 때문인가?!"
    stephan_think"그래……{cps=2} {/cps}딱히 윌리가 나쁜게 아니야"
    stephan_think"생각해보니까 윌리도 참 불쌍한 녀석이야"
    stephan_think"역시 말려야겠지?"
    show stephan shock2
    stephan"저,{cps=2} {/cps}저기……"
    stephan"폭력은 아무것도 해결하지 못한다고 생각해……"
    lisa"하지만 그녀석을 두고 어떻게 참겠어?!"
    lisa"고개 숙여 사과를 받아도 부족할 지경인데!"
    stephan"아무리 그래도……{cps=2} {/cps}차였다고 해서 야만스럽게 때리려고 하다니……"
    stephan"이럴때 가장 좋은방법은 윌리가 후회할 정도로 행복하게 사는거라고 생각해!"
    show lisa talk
    lisa"어?"
    lisa"무슨……"
    show lisa shy
    lisa"설마……?"
    show lisa mad
    lisa"으……"
    play sound "se/hit.ogg"
    scene black
    $ renpy.vibrate(0.4)
    $ renpy.pause(0.4)
    scene white with eyeopen
    scene bg school_classroom with dissolve
    show lisa mad:
        xalign 0.9 yalign 1.0
    show stephan fear at left
    stephan"갑자기 왜 때리는거야?!"
    lisa"으으……"
    "아무래도 이녀석은 윌리를 좋아하거나 그런 건 아닌 듯 하다."
    stephan"내가 뭔가 착각을 한 거 같긴 한데 말이야……{cps=2} {/cps}그래 폭력을 휘두를 필요는 없잖아!"
    show stephan shock at left
    show lisa shock
    lisa"미,{cps=2} {/cps}미안!"
    play music "bgm/smooth2.mp3"
    lisa"그냥……{cps=2} {/cps}다들 계속 그런 착각을 하니까 빡쳐서"
    lisa"난 윌리-윌리랑 친구일 뿐. 그 이상도, 그 이하도 아닌데……"
    "저 마음 이해한다."
    "이성이랑 친하게 있으면 그런 착각들을 하니까 정말 피곤해진다."
    "……물론 나한텐 처음부터 이성인 친구가 없지만 말이지"
    "그래도 왠지모르게 이해는 할 수 있을거 같아"
    show stephan at left
    stephan"그……{cps=2} {/cps}윌리한테 하고 싶은 말이 있다고 했지?"
    show lisa smile
    lisa"어!{cps=2} {/cps}그리고 가급적이면 페이스 투 페이스로 직접 말하고 싶어!"
    stephan"그럼 같이 윌리 병문안 가는 건 어때?"
    lisa"그거 괜찮은 생각인데?!"
    show stephan smile at left
    stephan"그럼 방과후에 만나서 같이 가자"
    show stephan shock2 at left
    stephan_think"근데 제가 병문안에 가면 좋아지긴 커녕, 오히려 병이 더 들겠는데?!"
    lisa"아,{cps=2} {/cps}참고로 내 이름은 \'리사 보우만(Lisa Bowman)\'이라고 해"
    $ lisa_name = '리사 보우만'
    show stephan at left
    stephan"난 스테반 토머"
    show lisa
    lisa"네 이름이라면 알고 있어~"
    stephan_think"오?{cps=2} {/cps}내가 은근 인기 있었나?"
    show lisa smile
    lisa"정말 윌리-윌리의 말대로 새빨간 머리카락이네!"
    show stephan shock at left
    show effect2
    play sound "se/shock2.mp3"
    stephan"너,{cps=2} {/cps}너도 그 소리냐;;"
    "아무래도 내 아이덴티티는 머리카락 하나 뿐인가보다……"
    "\'무엇 무엇 잘 하는애\', \'잘생긴 애\', \'똑똑 한 애\'도 아니고 \'머리 빨간 애\'가 뭐냐고요……"
    scene black with moveup
    stop bgs
    play music "bgm/smooth3.mp3"
    play bgs "bgs/street.mp3"
    centered"방과후"
    scene bg outside_road at Zoom((1280,720),(0,0,1280,720),(0,224,711,399),1.0) with moveup
    "나랑 리사 보우만은 같이 대화를 하며 윌리의 집으로 향했다."
    "얘가 —어떤 의미에선— 남자 문제로 고민하는 것을 배려해 호칭은 성으로만 부른다."
    "윌리한테 사전 연락을 취하고 싶었지만, 걔 폰이 내 수중에 있으므로 그건 힘들어 그냥 서프라이즈로 가기로 했다."
    show stephan:
        xalign 0.2 yalign 1.0
    show lisa talk:
        xalign 0.8 yalign 1.0
    stephan"학교에서 네가 윌리를 패고 싶다고 했었는데, 걔가 뭐 잘못했어?"
    show effect1
    show stephan shock
    show lisa mad
    play sound "se/shock.ogg"
    lisa"{size=45}그 녀석이 여자의 마음을 짚밟아 버렸다고!{/size}" with lshake
    hide effect1
    stephan"그렇게 말하면 누가 들어도 네가 차인걸로 밖에 안들려……"
    lisa"내가 아니라 내 친구 얘기야!"
    show stephan
    stephan"아아―{cps=2} {/cps}친구가 차였다는 얘기구나"
    lisa"흣!"
    "갑자기 리사 보우만은 손에 힘을 주기 시작했다."
    show stephan fear
    stephan"죄,{cps=2} {/cps}죄송합니다!!"
    lisa"남들보고 함부로 차였다는 말 하는거 아니야"
    stephan"다음부턴 조심 하겠습니다"
    show lisa talk
    lisa"그래"
    "그리고 그녀는 손에 힘을 풀었다."
    show stephan shock2
    stephan"그래서 그 차인……{cps=2} {/cps}이 아니라!"
    stephan"……킥 당한 친구 때문에 지금 윌리를 때리겠다는 거야?"
    lisa"그건 윌리-윌리의 대답에 따라서 달라"
    lisa"만약 누가 봐도 걔가 나쁜거라면 아주 쥐어 패줄거고!"
    lisa"그냥 서로의 의견차 때문이라면……{cps=2} {/cps}어떻게든 화해 시켜주고싶어……"
    stephan"도대체 무슨 일이 있었는데?"
    lisa"비밀로 해줄 수 있어?"
    stephan"그래,{cps=2} {/cps}그보다 딱히 남들에게 말 할 이유가 없지만 말이야"
    lisa"…………"
    lisa"어제 내 친구 \'앤 크라운\'이 윌리랑 같이 데이트를 했었는데……"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}음?!{/size}" with lshake
    extend"{size=45} 데이트?!{/size}"
    hide effect1
    show stephan mad
    stephan_think"윌리는 배신자"
    stephan_think"집에 도착하면 보우만이랑 같이 2:1로 개털어야지"
    lisa"어이―{cps=2} {/cps}듣고 있냐?"
    show stephan shock2
    stephan"으,{cps=2} {/cps}음―"
    stephan"앤 크라운 이라는 애가 윌리랑 데이트를 하고 나서 어떻게 됐어?"
    stop music
    lisa"그게……{cps=2} {/cps}나도 데이트 이후에 무슨일이 있었는지 몰라서 이렇게 윌리에게 찾아 가는거야"
    show stephan shock
    stephan"모른다고?"
    play music "bgm/sirius3.mp3"
    lisa"어……"
    extend" 그게 어젯 밤에 내가 앤한테 전화를 했었는데……"
    stop bgs
    scene black with memory
    play bgs "se/phone_calling.mp3"
    centered"오후 8시 20분"
    show lisa talk:
        zoom 1.4 yalign -0.5 xalign 0.5
    $ renpy.pause(7.0)
    stop bgs
    lisa"아―,{cps=2} {/cps}여보세요?"
    anne"리,{cps=2} {/cps}사……?"
    show lisa smile
    lisa"앤~!"
    lisa"데이트는 어떻게 됐어?"
    anne"흐……{cps=2} {/cps}흑……"
    show lisa shock
    lisa"어?"
    extend" 너 지금 우는거야?"
    anne"미안해……{cps=2} {/cps}리사……"
    lisa"어?!"
    show effect1
    play sound "se/shock.ogg"
    lisa"{size=45}너 왜그래?!{/size}" with lshake
    hide effect1
    play sound "se/phone_end.mp3"
    $ renpy.pause(3.3)
    lisa"…………"
    play bgs "bgs/street.mp3"
    scene bg outside_road at Zoom((1280,720),(0,0,1280,720),(0,224,711,399),0.0) with memory
    show stephan shock:
        xalign 0.2 yalign 1.0
    show lisa talk:
        xalign 0.8 yalign 1.0
    lisa"갑자기 울면서 나보고 미안하다고 하니까……{cps=2} {/cps}너무 걱정되더라고……"
    lisa"혹시 윌리-윌리가 앤한테 뭔가 나쁜말, 혹은 나쁜짓 이라도 했는 건지……"
    stephan_think"그래서 윌리를 패주고 싶다고 했구나"
    lisa"그 이후로 내가 몇번이고 전화를 해봤지만, 전부 끊어버리고……"
    lisa"결국엔 전원까지 꺼버렸어"
    lisa"오늘 학교에서도 잠시 걸어봤는데, 아직까지도 꺼져있더라고"
    stephan"네 친구도 참……{cps=2} {/cps}남자한테 킥 당했다고 폰 전원 끄고 울고 있다니……"
    lisa"나도 뭔가 앤답지가 않아서 조금 걱정이야……"
    stephan_think"하지만 윌리가 여자를 울릴줄이야……"
    stephan"근데 그런 일이라면 윌리보단, 그 앤 크라운 이라는 애 집으로 찾아가는 게 맞지 않나?"
    lisa"집 주소를 몰라서……"
    stephan"그럼 걔 친구들한테 물어보거나……"
    stop music
    lisa"별로……{cps=2} {/cps}앤이 남자한테 차였다는 걸 소문내고 싶지가 않거든"
    stephan"…………"
    "리사 보우만은 내가 생각했던거 보다 훨씬 착한 성격을 지녔다."
    "친구의 고통을 마치 자신의 고통인 마냥 받아들여주고……"
    "요즘은 보기 드문 배려심이라 그런지, 나도 조금 도와주고 싶다는 생각이 들었다."
    show stephan smile
    play music "bgm/smooth1.mp3"
    stephan"만약 네 말이 사실이라면 나도 윌리한테 엄청 실망했어"
    stephan"도착하면, 같이 때리는거 도와줄게!"
    show lisa
    lisa"고마워……{cps=2} {/cps}토머"
    scene black with moveright
    centered"윌리의 집 앞"
    scene bg willy_house with moveright
    show stephan at left
    show lisa think at right
    stephan"여기가 윌리의 집이야"
    lisa"윌리-윌리의 부모님은 집에 계시려나?"
    show stephan talk
    stephan"글쎄……{cps=2} {/cps}사실 나도 걔 집에 들어가보는 건 처음이라서……"
    scene bg willy_house at Zoom((1280,720),(0,0,1280,720),(861,458,419,235),1.5)
    "일단 주변을 살펴봤는데, 차 한대가 눈에 띄었다."
    "혹시 부모님이 윌리를 간병하고 있는 걸까?"
    "근데 생각해보니까 윌리에겐 룸메이트가 있었다고 한다."
    "……그럼 저 차는 룸메이트 껀가?"
    stephan_think"뭐가 어쨌건 이렇게 되면 노골적으로 때리는 건 힘들겠군……"
    scene bg willy_house at Zoom((1280,720),(861,458,419,235),(0,0,1280,720),0.5) with Dissolve(1.5)
    show stephan shock at left
    show lisa shock at right
    show effect1
    play sound "se/shock.ogg"
    lisa"{size=45}이런!!{/size}" with lshake
    lisa"생각해보니까 우리 병문안 와놓고서 빈손이잖아?!"
    hide effect1
    stephan"너 진짜 윌리의 병문안 왔냐?"
    lisa"맞지않나?"
    stephan"아니,{cps=2} {/cps}방금 전까지 네가 걔를 쥐어 패주고 싶다고 했잖아?!"
    show lisa talk
    lisa"아―"
    lisa"아까도 말했지만, 그건 윌리-윌리의 대답에 따라서 달라"
    show lisa smile
    lisa"그러니까 그때까진 그냥 순수하게 병문안을 가는거라고!"
    stephan"그,{cps=2} {/cps}그러세요?"
    scene bg willy_house at Zoom((1280,720),(0,0,1280,720),(360,391,525,295),3.0)
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(2.8)
    "나랑 보우만은 문 앞까지 다가갔다."
    show stephan:
        zoom 1.2 yalign -0.2 xalign 0.0
    show lisa talk:
        zoom 1.2 yalign -0.5 xalign 0.8
    play sound "se/door_bell.mp3"
    "그리고 초인종을 누른다."
    stephan_think"처음으로 윌리 집에 들어가볼 수 있는 건가?"
    show stephan smile
    stephan_think"(두근 두근)"
    stephan"…………"
    "꽤 기다렸는데도 아무런 반응이없다."
    play sound "se/door_bell.mp3"
    $ renpy.pause(0.3)
    show stephan talk
    stephan"저―{cps=2} {/cps}윌리 친구 스테반 토머 라고 하는데, 혹시 윌리 없나요?"
    lisa"왜 그래?"
    stephan"안에 아무도 없는거 같은 느낌이……"
    $ extra_name = '작은 목소리'
    extra"{size=20}——— 진짜{/size}"
    stephan"어?"
    "문 너머로 작은 목소리가 들렸다."
    "집에 누가 있긴 있나보다."
    play sound "se/footsteps_running.mp3"
    scene bg willy_house at Zoom((1280,720),(360,391,525,295),(572,399,525,295),1.1)
    "나는 목소리가 좀 더 잘 들리는 쪽으로 이동했다."
    "……참고로 도청은 나쁜짓 이니까 착한 어린이는 따라하지 말자"
    lisa"무슨 일이야?"
    "검지 손가락을 위로 올리며 말한다."
    stephan"쉿!"
    stop music
    scene black with eyeshut
    "……눈을 감고, 안에서 들리는 소리에 집중한다."
    "주변에서 들리는 소음 때문에 집중하는 게 쉽진 않았다."
    $ extra_name = '목소리 A'
    extra"밖에 누구 왔음"
    $ extra_name = '목소리 B'
    extra"네가 가"
    "안엔 두 사람이 있는 듯 하다."
    $ extra_name = '목소리 A'
    extra"나 지금 중요한 파트 하고있어서 안돼"
    $ extra_name = '목소리 B'
    extra"그래봤자 게임 일텐데"
    $ extra_name = '목소리 A'
    extra"이게 얼마나 중요한지 알아?!"
    play music "bgm/beat3.mp3"
    extra"윌리가 어떤 새끼한테 내 PX4를 줘버리는 바람에……"
    stephan_think"으익!"
    extra"흑……{cps=2} {/cps}흑……"
    extra"아직 트로피도 백업 하지 못했단 말이야……"
    $ extra_name = '목소리 B'
    extra"최근 윌리의 말 잘 안듣더니, 자업자득이네"
    $ extra_name = '목소리 A'
    extra"그래도 이렇게까지 할 필요는……"
    if pick_game == True:
        $ extra_name = '목소리 B'
        extra"얼마 전에 윌리가 사죄의 의미로 게임 하나 사줬잖아"
        extra"기분 풀어"
        $ extra_name = '목소리 A'
        extra"젠장……"
        extra"난 선라이즈 오버드라이브가 아니라, 블러드 폰을 기대했단 말이야!"
        extra"얼마 후면 PX4에 출시되는 블러드 폰!"
        extra"그거 말고 챠티드4도 기대 하고 있었는데……!"
        extra"SBOX Two엔 재미있는 게 없다구!"
        $ extra_name = '목소리 B'
        extra"……그렇게 말 해도 난 몰라"
        $ extra_name = '목소리 A'
        extra"진짜……{cps=2} {/cps}흑흑……"
        extra"내 PX4 가져간 놈 만나면 아주 죽여버릴거야!"
        scene bg willy_house at Zoom((1280,720),(572,399,525,295),(331,273,754,424),1.1) with eyeopen
        show stephan shock:
            zoom 1.2 xalign 0.25 yalign -0.2
        show lisa talk:
            zoom 1.2 xalign 0.8 yalign -0.5
        stephan"히익!"
        lisa"음?"
        stephan"으,{cps=2} {/cps}음―"
        show stephan shock2
        stephan"내일 윌리가 학교에 나올지도 모르니까 그때 물어보면 안될까?"
        lisa"이제와서 왜?"
        stephan"그냥……{cps=2} {/cps}무서워서 라고 해야할까……"
        show lisa shock
        lisa"도대체 뭐가 무서운건데?!"
        show stephan shock
        stephan"나도 나만의 이유가 있는거라구!"
        "솔직히 그때 PX4를 주겠다고 말 한건 윌리 쪽이었다."
        "그러니까 나한테 잘못이 없다고 생각을 하고 싶긴 했었지만……"
        "PXN 계정에 저장된 트로피를 내가 전부 지워버렸으니……{cps=2} {/cps}잘못이 아주 없는 건 아니다."
        show lisa talk
        lisa"쳇,{cps=2} {/cps}이대로 집으로 돌아가야 하나"
        stephan"미안"
    else:
        extra"흑흑……"
        $ extra_name = '목소리 B'
        extra"너 진짜 우는거냐?"
        $ extra_name = '목소리 A'
        extra"안 울게 생겼어?!"
        extra"내 평생을 들여서 얻은 트로피들 이라고!!"
        $ extra_name= '목소리 B'
        extra"(토닥 토닥)"
        $ extra_name= '목소리 A'
        extra"윌리 진짜……{cps=2} {/cps}흑흑"
        extra"시키는데로 렌스 인가 뭐신가 하는 사람에 대해서 찾아봐 줬더만……"
        $ extra_name= '목소리 B'
        extra"근데 너 PX4 한대 더 있지 않았나?"
        $ extra_name= '목소리 A'
        extra"그건 전시용이야!"
        extra"포장을 뜯지 않은 상태에서 놔둬야 의미가 있어!"
        extra"진짜……{cps=2} {/cps}아무도 날 이해 못할거야……"
        $ extra_name= '목소리 B'
        extra"넌 무슨 사춘기냐;;"
        $ extra_name = '목소리 A'
        extra"으어어엉―!"
        extra"내 PX4랑 트로피―"
        $ extra_name = '목소리 B'
        extra"넌 다른 의미에서 나이를 거꾸로 먹네……"
        extra"그,{cps=2} {/cps}그보다 밖에 사람 기다리고 있을텐데 어쩔까?"
        $ extra_name = '목소리 A'
        extra"그냥 아무도 없다면서 내보내……"
        $ extra_name = '목소리 B'
        extra"어휴―"
        play sound "se/footsteps_wood.mp3"
        scene bg willy_house at Zoom((1280,720),(572,399,525,295),(572,399,525,295),0.0) with eyeopen
        $ renpy.pause(1)
        extra"안에 아무도 없습니다"
        show lisa talk:
            xalign 0.6 yalign 1.0
        show stephan shock at left
        stephan_think"어이?!"
        show effect1
        show lisa mad
        play sound "se/shock.ogg"
        lisa"{size=40}뻥까지마!{cps=2} {/cps}딱봐도 안에 있구만!{/size}" with lshake
        hide effect1
        extra"…………"
        show stephan shock:
            zoom 1.2 xalign 0.25 yalign -0.2
        show lisa talk:
            zoom 1.2 xalign 0.8 yalign -0.5
        stephan"저기……{cps=2} {/cps}보우만?"
        lisa"어?"
        stephan"그냥 가자……"
        lisa"왜?!"
        stephan"윌리 안에 없는거 같아서"
        stephan"가 봤자 시간만 낭비라고"
        stephan_think"그리고 내가 가지고 있는PX4의 원래 주인을 만나는것도 뭔가 부담스럽고……"
        lisa"확실히 일리는 있네……"
        show lisa
        lisa"그럼 어쩔 수 없이 내일 다시 와야겠어!"
        stephan"……윌리가 내일도 결석 이라면 말이지"
    stop music
    stop bgs
    play sound "se/move.mp3"
    scene black with moveleft
    play music "bgm/beat1.mp3"
    centered"다음 날"
    play bgs "bgs/people.mp3"
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(259,146,785,441),1.0) with moveleft
    centered"오후 4시"
    "오늘도 어제와 다를 것 없는 하루가 반복됐다."
    "……어제랑 똑같이 윌리는 학교에 오지 않았다."
    show stephan think with dissolve:
        zoom 1.4 yalign -0.2 xalign 0.0
    "어제 걔 집에서 들었던 대화를 토대로 생각해보면, 윌리는 안에 없었다."
    "심하게 아퍼서 입원이라도 한 걸까?"
    stephan_think"하지만 지금 걔 폰은 내 손안에 있어서 연락은 불가능하고……"
    play sound "se/footsteps_running.mp3"
    show lisa shock:
        xalign 2.0 zoom 1.4 yalign -0.5
        linear 0.5 xalign 0.8
    "혼자서 깊게 생각을 하는데, 누군가 내 옆에 다가왔다."
    lisa"토머!"
    extend" 윌리-윌리에 대해서 뭔가 알아낸거 없나?!"
    show stephan yawn
    show phone2:
        xalign 0.3 yalign 0.5 zoom 0.3
    "나는 윌리의 폰을 보이며 입을 열었다."
    stephan"지금 걔 폰이 나한테 있어서 연락이 불가능해"
    stephan"그리고 당연히 알아낸 건 없지"
    hide phone2 with dissolve
    show lisa think
    lisa"이거 어쩌지……"
    show stephan talk
    stephan"네 친구는 어때?"
    extend" 오늘 왔어?"
    show lisa talk
    lisa"아니……"
    extend" 폰도 여전히 꺼져있고……"
    show stephan yawn
    stephan"걔 진짜 날라리네"
    extend". 어떻게 남자한테 차였다고 학교를 2일간 결석하냐?"
    stop music
    lisa"…………"
    show stephan shock
    stephan"저,{cps=2} {/cps}저기?"
    "보우만은 그저 매우 걱정스러운 표정으로 조용히하고 있었다."
    "아무래도 내가 하지 말아야 할 말을 한 듯 하다……"
    stephan"미안……"
    lisa"어?"
    show lisa
    extend" 왜 네가 미안해 하는거야?!"
    show lisa talk
    lisa"네 말대로 앤이 요즘 이상하긴 한 걸……"
    lisa"평상시엔 얌전하고……{cps=2} {/cps}공부도 잘 하고……"
    lisa"그런 모범적인 애가 아무런 소식도 없이 학교를 쨀 리가 없을텐데……"
    "분위기가 갑자기 무거워졌다."
    "뭐라도 위로의 말을 해야될 거 같아……"
    play music "bgm/happy2.mp3"
    show stephan shock
    stephan"네가 그렇게 생각한다면 조금만 믿어 보자……!"
    show lisa smile2
    lisa"살다살다 너같은 애한테 위로를 받게 될 줄이야……"
    show stephan shock
    stephan"어이,{cps=2} {/cps}그건 또 무슨 뜻이야?!"
    show lisa smile
    lisa"장난이야~{cps=2} {/cps}장난~"
    stephan_think"보우만의 기분이 좀 풀린거 같아서 다행이긴 하지만……"
    stephan_think"나같은 애가 뭐가 어때서?!"
    show lisa talk
    lisa"근데 오늘 학교에서 이상한 소문을 들어서 좀 걱정이야……"
    show stephan talk
    stephan"소문?"
    lisa"응……"
    lisa"걔가 가출을 했다고 하더라고……"
    stop music
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}잠깐,{cps=2} {/cps}그거 위험한거 아니야?!{/size}" with lshake
    hide effect1
    lisa"…………"
    stephan_think"이런!"
    stephan_think"아까전 까지 내가 괜찮을 거라고 말해놓고서!"
    stephan_think"이놈의 입이 방정이야!"
    play music "se/phone_alarm.mp3"
    $ renpy.pause(1)
    show stephan talk
    stephan"어?"
    "어디선가 처음 듣는 노랫 소리가 들려왔다."
    show lisa talk
    lisa"야, 아무리 쉬는 시간이라도 그렇지, 어떻게 학교에서 폰을 켜놓냐?"
    show stephan shock
    stephan"그럴리가……{cps=2} {/cps}내 폰은 분명 무음으로 해놨는데"
    stephan"그보다 이건 내 벨소리가 아니야"
    "하지만 내 주변에서 소리가 크게 나오고 있다."
    stephan_think"도대체……"
    stephan"아!{cps=2} {/cps}생각해보니까 윌리의 폰!!"
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(583,191,593,333),0.0)
    show lisa talk:
        xalign 0.5 zoom 1.5 yalign -0.5
    play sound "se/search_bag.mp3"
    show phone2_alarm with dissolve:
        yalign 7.0 xalign 0.9
        linear 1.0 yalign 1.0
    "나는 주머니에서 폰을 꺼냈다."
    stephan_think"역시 윌리의 폰이 범인 이었군"
    "아무래도 내가 윌리의 폰을 챙기기만 하고, 매너모드로 바꿔놓는 걸 깜빡한 모양이다."
    lisa"전화?"
    stephan"전화가 아니라 알람……{cps=2} {/cps}같아"
    stephan"근데 왜 이런 시간에 알람이 맞춰져 있는거지?"
    "이 시간대에 특별한거 라곤……"
    "종례하기 대략 10분 전 정도?"
    "하지만 알람의 시간보다 더 이상한 건……"
    show phone2_alarm:
        linear 0.5 zoom 3.5 xalign 0.5 yalign 0.5
    "바로 이 레이블……"
    stephan_think"SOS?"
    stop music
    hide phone2_alarm
    show phone2:
        zoom 3.5 xalign 0.5 yalign 0.5
        linear 1.0 zoom 1.0 yalign 1.0 xalign 0.9
    "주변의 시선이 느껴지므로, 일단 시끄러운 알람부터 껐다."
    stephan_think"그나저나 SOS라니……"
    stephan_think"왜 이런 이상한 이름으로 알람을 맞춰 놓은거지……?"
    play sound"se/search_bag.mp3"
    show phone2:
        linear 1.0 yalign 12.0
    $ renpy.pause(1.0)
    hide phone2 with dissolve
    "나는 폰을 다시 주머니에 넣었다."
    stop bgs
    scene black with eyeshut
    stephan_think"근데……"
    extend" 생각해보니까 크라운이랑 윌리"
    stephan_think"둘다 같은 날에 결석했네……"
    "아까 봤던 SOS 알람 때문인지, 조금 불안한 생각이 들었다."
    "……하지만 아직 하루밖에 지나지 않았고"
    "무엇보다 윌리 쪽은 크라운과는 다르게, 명백한 결석 사유가 있다."
    stephan_think"그래도 모르니까 좀 더 지켜봐야겠어……"
    play music "bgm/beat2.mp3"
    play bgs"bgs/street.mp3"
    scene bg willy_house with moveright
    "나는 수업이 끝나고, 다시한번 윌리의 집을 찾아왔다."
    "어젠 이런저런 일이 있어서 만나기 곤란했지만……"
    "오늘은 용기 내어서 윌리의 안부를 묻기로 했다."
    stephan_think"무사하다는 것 만 확인 하고 돌아가야지……"
    play sound "se/footsteps_concrete.mp3"
    scene bg willy_house at Zoom((1280,720),(0,0,1280,720),(360,391,525,295),3.0)
    $ renpy.pause(4)
    show stephan talk:
        zoom 1.2 yalign -0.2 xalign 0.3
    play sound "se/door_bell.mp3"
    $ renpy.pause(0.5)
    stephan"안에 아무도 없나요?"
    stephan"…………"
    "침묵……"
    "저번에 왔을때랑은 조금 상황이 달랐다."
    show stephan think
    stephan"음……"
    scene bg willy_house at Zoom((1280,720),(360,391,525,295),(572,399,525,295),0.5)
    stephan_think"역시……{cps=2} {/cps}도청은 관둬야겠지?"
    scene bg willy_house at Zoom((1280,720),(572,399,525,295),(360,391,525,295),0.5)
    "하지만 이대로 집으로 돌아갈 수는 없다."
    "왠지 정말로 윌리한테 무슨 일이 생긴것 같아서 불안하고……"
    scene bg willy_house at Zoom((1280,720),(360,391,525,295),(861,458,419,235),1.5)
    stephan_think"일단 옆에 차가 있걸로 봐선 안에 사람이 있을 확률은 충분히 있어"
    scene bg willy_house at Zoom((1280,720),(861,458,419,235),(360,391,525,295),1.5)
    show stephan think:
        zoom 1.6 yalign -0.3 xalign 0.5
    play sound "se/door_bell.mp3"
    "난 한번더 초인종을 눌러봤다."
    "……역시 대답은 없었다."
    stephan_think"잠깐 근처에 나갔나?"
    "그럼 이제부터 뭘 어떻게 해야 할까……"
    "조금이라도 연락이 닿는다면 그나마 마음이 편할거 같은데"
    stephan"…………"
    show stephan
    stephan_think"그래!{cps=2} {/cps}쪽지라도 남겨보자!"
    hide stephan with dissolve
    play sound "se/book_page.ogg"
    "난 가방에서 종이 한장을 꺼내서 내 전화번호와 함께 \'연락 부탁드립니다\'같은 느낌의 글귀를 써서 대문 사이에 끼워 넣었다."
    stephan_think"이걸로 좀 안심이군……"
    play sound "se/move.mp3"
    stop bgs
    scene black with moveleft
    centered"다음 날"
    play bgs"bgs/people.mp3"
    scene bg school_classroom with moveleft
    centered"오전 9시 20분"
    "역시나 오늘도 윌리는 학교를 결석했다."
    "……물론 병결이라 일반적인 결석과는 조금 다르긴 하지만"
    stephan_think"근데 시간이 이렇게나 됐는데도 선생님이 안 들어오시다니……"
    stephan_think"오늘 무슨 일 있나?"
    "나는 내 앞에 앉은 —그닥 대화를 해본적이 없는—애 한테 말을 걸었다."
    show stephan talk at left
    stephan"저기,{cps=2} {/cps}오늘 1교시 안하나?"
    $ extra_name = '앞자리 학생'
    extra"내가 듣기론, 교사 회의가 있다고 하던데?"
    stephan"회의?"
    show stephan smile at left
    stephan"그럼 1교시는 자습?!"
    extra"……적어도 지금은 다들 그렇게 생각하고 있어"
    stephan"앗싸!"
    stephan_think"자습이면 윌리랑 같이 체스를……!"
    show stephan shock at left
    stephan_think"아참……"
    extend" 걔 결석 이었지……"
    "이러니까 왠지 내가 윌리 말고는 같이 놀사람이 없는거 같이 보이겠지만!"
    show effect2
    play sound "se/shock2.mp3"
    "맞아……{cps=2} {/cps}없어……"
    hide effect2
    show stephan yawn at left
    stephan_think"그냥 책이나 읽어야겠다"
    play sound "se/move.mp3"
    scene black with moveright
    centered"얼마 후"
    scene bg school_classroom with moveright
    play sound "se/footsteps_wood.mp3"
    show extra_social:
        xalign 3.0 yalign 1.0
        linear 3.0 xalign 0.75
    $ renpy.pause(3.0)
    $ extra_name = '담임 선생님'
    extra"다들 조용히"
    stop bgs
    extra"에헴"
    extend", 오늘은 선생님들끼리 긴급 회의가 있어서 1교시를 건너 뛰었어"
    extra"그래도 다들 얌전히 있었다고 믿고 있을게"
    $ extra_name = '같은 반이면서도 내가 이름을 모르는 학생'
    extra"그럼 지금부터 2교시 시작해요?"
    $ extra_name = '담임 선생님'
    extra"아니,{cps=2} {/cps}아마 2교시도 건너 뛸거 같아"
    play bgs "bgs/people.mp3"
    "주변에서 기뻐하는 소리가 들렸다."
    stop bgs
    stop music
    extra"지금 심각하니까 좀 얌전히 있어줄 수 없겠냐?"
    stephan_think"심각하다고?"
    "선생님은 4등분된 A4용지 여러장을 맨 앞자리에 앉은 학생에게 주고, 뒤로 넘기라고 말 했다."
    "모두 한장씩 받자, 선생님이 입을 열었다."
    extra"7반에 \'앤 크라운\'이라고 알지?"
    play music "bgm/sirius3.mp3"
    extra"걔가 며칠 전 부터 집에 안들어 왔다고 해"
    stephan"…………"
    extra"혹시 걔가 어디 있는지, 아니면 뭔가 수상한 점을 목격했는지 등"
    extra"아는 게 있으면 그 종이에다가 적어"
    stephan"자기 이름도 적어요?"
    extra"어―{cps=2} {/cps}내가 말 하는 걸 깜빡해버렸군"
    extra"자기 이름은 구석에 작게 적으면 돼"
    $ extra_name = '학생'
    extra"구체적으로 어떤걸 적으면 되는거예요?"
    $ extra_name = '담임 선생님'
    extra"예를 들어서, 최근에 앤을 학교 말고 다른곳에서 만났다든가"
    extra"아니면 뭔가 기운이 없어 보였다든가……"
    extra"그냥 앤이 왜 학교를 안 나오는지 알고 있다고 적어주면 더 좋고"
    extra"딱히 아는 게 없으면 그냥 모른다고 적어"
    show stephan talk at left
    stephan"그……{cps=2} {/cps}앤 크라운……"
    stephan"혹시 가출이에요?"
    extra"뭔가 아는거 있어?"
    stephan"아니요……"
    stephan"그냥 그런 소문이 들려서요"
    extra"…………"
    extra"나도 자세히는 모르지만……"
    extra"일단은 가출 이라는거 같더라"
    extra"앤의 부모님의 말씀을 토대로 생각해보면, 원인은 학교 폭력, 혹은 학업에 대한 스트레스 일 확률이 높다고 보고 있어……"
    show effect1
    play sound "se/shock.ogg"
    extra"{size=45}이런!{/size}" with lshake
    extra"내,{cps=2} {/cps}내가 너희들한테 이런 말 해줬다는 건 비밀로!"
    hide effect1
    show stephan think at left
    "아무래도 어제 보우만이 나에게 해준 말이 사실인듯 하다."
    stephan_think"난 크라운의 행방에 대해서 아는 게 딱히 없지만……"
    stephan_think"그래도 윌리는 뭔가 알고 있을 거 같아"
    scene black with eyeshut
    "하지만 문제는, 모든 문제의 해답을 지닌 윌리가 우연찮게도 결석 이라는 점……"
    "그러나 여기서 더 큰 문제는……"
    play sound "se/think.mp3"
    show phone2_alarm with flash:
        zoom 3.5 xalign 0.5 yalign 0.5 alpha 0.5
    $ renpy.pause(1)
    "……과연 진짜로 우연인가?"
    play sound "se/school.mp3"
    scene black with dissolve
    stop music
    centered"점심 시간 후"
    play bgs "bgs/people.mp3"
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(161,182,687,386),0.6) with dissolve
    $ renpy.pause(0.5)
    show lisa talk:
        zoom 1.2 xalign 0.3 yalign -2.0
    "반에 들어가려는데 앞에 보우만이 기다리고 있었다."
    show stephan talk:
        zoom 1.2 xalign 0.8 yalign -0.2
    stephan"무슨 일이야?{cps=2} {/cps}여기서 멍하게 있고"
    lisa"…………"
    lisa"토머……{cps=2} {/cps}뭔가 재미있는 개그 라도 해봐"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}어?!{/size}" with lshake
    stephan"갑자기 뭐야?!"
    hide effect1
    lisa"빨리 개그나 해"
    stephan_think"뭐지?"
    show stephan shock2
    stephan"드,{cps=2} {/cps}드립 정도로 괜찮으려나?"
    lisa"뭐든지 좋아……{cps=2} {/cps}그냥 생각을 다른데로 가도록 해줘"
    show stephan think
    stephan"음……"
    show stephan
    stephan"분식집 에서 사기를 치면 뭐라고 하는지 알아?"
    lisa"뭔데?"
    show stephan smile
    stephan"분식 회계!"
    lisa"분식 회계?"
    extend" 그게 뭐야?"
    show stephan shock
    stephan"아……{cps=2} {/cps}이해 못했구나……"
    show stephan think
    stephan"그럼……"
    show stephan shock2
    stephan"전기가 와이어랑 결혼 했어"
    stephan"그때 전기가 와이어 보고 뭐라고 했는지 알아?"
    lisa"뭔데?"
    stephan"\'언제나 전, 자기 파 예요\'"
    show lisa think
    lisa"전……{cps=2} {/cps}자기 파?"
    lisa"전자기파……"
    show lisa
    show stephan
    lisa"아!!"
    play music "bgm/happy1.mp3"
    show lisa laugh
    lisa"하하하하"
    lisa"그건 좀 웃겼다"
    lisa"그래 그래.{cps=2} {/cps}얼마 전에 과학에서 전류의 흐름을 배웠었지"
    "나,{cps=2} {/cps}나의 개드립에 누군가 웃어줬다!"
    "언제나 맞을 각오로 치는 드립이었는데!"
    lisa"또 없어?"
    stephan"음……"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(161,182,687,386),0.0) with moveright
    $ renpy.pause(0.5)
    show lisa smile:
        zoom 1.2 xalign 0.3 yalign -2.0
    show stephan:
        zoom 1.2 xalign 0.8 yalign -0.2
    lisa"후우~{cps=2} {/cps}역시 웃으니까 기분이 좀 좋아지네"
    show lisa
    lisa"요즘 들어서 제대로 웃어본적이 없는거 같았거든……"
    show stephan talk
    stop music
    stephan"크라운 때문에?"
    show stephan shock
    stephan_think"으익!{cps=2} {/cps}내가 왜 그런 소리를?!"
    show lisa talk
    lisa"……아마도"
    lisa"그냥 이런저런 생각이 들어가지고……"
    "나는 보우만에게 뭔가 위로의 말을 해야 겠다고 생각했다……{cps=2} {/cps}나 때문에 분위기도 망친 거 같기도 하고……"
    show stephan talk
    "그때 내 머릿속에서 떠오른 위로의 말은 정말 한심 했다."
    stephan"혹시……{cps=2} {/cps}같이 크라운을 찾지 않을래?"
    lisa"찾는다고……?"
    show lisa smile2
    lisa"탐정 이라도 될 생각인거냐?"
    show stephan blush
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}탐정?!{/size}" with lshake
    stephan"아니!{cps=2} {/cps}절대로 아니야!"
    stephan"아니라고!!"
    hide effect1
    show lisa talk
    lisa"왜그렇게 예민하게 반응 하는거야?"
    show stephan shock
    stephan"그,{cps=2} {/cps}그냥……"
    stephan"트라우마 라고 해야 할까……"
    show stephan talk
    stephan"그래서……{cps=2} {/cps}어쩔거야?"
    show lisa
    lisa"…………"
    show lisa smile
    lisa"후후"
    lisa"그렇게 말 해줘서 고마워!{cps=2} {/cps}하지만 마음만 받을게"
    lisa"솔직히 우리끼리 뭘 할 수 있다고……"
    lisa"딱히 아는 게 있는것도 아니잖아?"
    stephan"아는거라……"
    jump chapter2_2
