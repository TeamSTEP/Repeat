##############################################################################################
#####################################챕터3: 변하는 물질적 가치##########################################
##############################################################################################
label chapter3:
    $ save_name = "3.변하는 물질적 가치"
    scene chapter3 with moveright
    $ renpy.pause(2)
    stop music
    play sound "se/book_page.ogg"
    scene black with moveright
    centered"9월 20일 토요일"
    centered"오후 2시 10분"
    play bgs"bgs/birds.mp3"
    play music "bgm/smooth3.mp3"
    scene bg grandpa_mansion with blinds
    centered"저택 앞"
    show stephan
    "나는 사전에 할아버지와 연락해서, 주말 동안은 저택에서 묷기로 했다."
    play sound "se/footsteps_concrete.mp3"
    scene bg grandpa_mansion at Zoom((1280,720),(0,0,1280,720),(497,274,308,173),2.0)
    $ renpy.pause(1.9)
    "문을 향해서 손을 뻗자……"
    play sound "se/door_open.ogg"
    $ renpy.pause(0.3)
    $ renpy.vibrate(0.4)
    play sound "se/hit.ogg"
    scene bg grandpa_mansion at Zoom((1280,720),(497,274,308,173),(450,235,380,214),0.4) with lshake
    "문이 갑자기 열리면서 내 이마에 부딫혔다."
    show seb shock cat:
        xalign 0.5 yalign 1.0 alpha 0
    show stephan yawn:
        zoom 1.5 xalign 0.2 yalign -0.2
    stephan"아야야……"
    show seb shock cat:
        linear 0.4 alpha 1.0
    seb"도, 도련님!{cps=2} {/cps}괜찮으세요?!"
    stephan"어……"
    seb"정말 죄송합니다.{cps=2} {/cps}제가 딴생각을 하다보니까……"
    show stephan with dissolve
    stephan"아니야……{cps=2} {/cps}별로 아프지도 않은걸"
    show stephan talk
    stephan"근데 손에 그 고양이는 뭐야?"
    show seb talk cat
    seb"이 아이는 제가 오면서 주워왔는데……"
    seb"이미 주인이 있다고 하길래 돌려주러 가던 참이었어요……"
    show stephan shock2
    stephan"히, 힘들겠네……"
    seb"네……"
    seb"오늘은 여기서 주무시고 가신다고 했죠?"
    stephan"응"
    seb"오늘 좋은 하루 보내시고 가세요"
    seb"그럼 전 이만"
    show seb talk cat with dissolve:
        zoom 1.5 yalign -0.2
    play sound "se/footsteps_concrete.mp3"
    show seb talk cat:
        linear 1.0 xalign 2.0
    $ renpy.pause(1.0)
    show stephan shock
    stephan_think"나도 들어가서 빨리 인사 해야겠다"
    scene black with moveright
    play sound "se/door_open.ogg"
    $ renpy.pause(0.5)
    stop bgs
    scene bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(295,332,690,388),0.0) with moveright
    centered"저택 거실"
    show cia smile:
        zoom 1.6 xalign 1.0 yalign -0.5
    show stephan:
        zoom 1.6 xalign 0.0 yalign -0.2
    cia"어서오세요! 도련님!"
    stephan"응, 오늘 신세 좀 질게"
    grandpa"왔구나~"
    scene bg mansion_hall at Zoom((1280,720),(295,332,690,388),(737,99,482,271),0.5)
    "할아버지는 소파에 앉아서 TV를 보고 계셨다."
    play sound "se/search_bag.mp3"
    show grandpa with dissolve:
        zoom 1.7 xalign 0.8 yalign -0.3
    grandpa"오늘은 자고 간다고 했지?"
    grandpa"할아버지가 네가 지낼 방까지 안내 해주마"
    show cia:
        zoom 1.7 xalign -1.5 yalign -0.5
        linear 0.7 xalign 0.0
    cia"할아버님, 제가 대신 안내 해 드릴게요"
    cia"몸 자주 움직이시면 안되잖아요?"
    show grandpa talk
    grandpa"그럼 부탁 할게"
    scene bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(295,332,690,388),0.0) with moveright
    show stephan:
        zoom 1.6 xalign 0.0 yalign -0.2
    show cia with dissolve:
        zoom 1.6 xalign 1.0 yalign -0.5
    cia"도련님, 절 따라오세요~"
    play sound "se/move.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg mansion_emptyroom with moveleft
    show cia:
        xalign 0.5 yalign 1.0
    show stephan shock:
        xalign 0.0 yalign 1.0
    cia"여기가 도련님의 방 이에요"
    show cia shine
    cia"평소엔 먼지만 쌓였던 곳을─제가 열심히 청소했죠!"
    stephan"청소를 넘어서서 아예 아무것도 없는데?"
    show cia
    cia"그야 여기 있던 물건을 전부 다른데로 옮겼으니까요"
    cia"잠은 장롱에 있는 이불깔고 바닥에서 자면 된데요"
    stephan"음……"
    stephan"알겠어"
    cia"또 필요하신게 있으시면 말씀 해 주세요"
    show stephan
    stephan"응"
    play sound "se/footsteps_wood.mp3"
    scene black with dissolve
    "나는 들고 온 짐을 풀고, 내가 여기로 온 이유─일기장을 읽기 위해서 내려갔다."
    scene bg lib_day with dissolve
    show stephan think with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"오늘 읽을 페이지는……"
    play sound "se/book_page.ogg"
    scene black with moveright
    stop music
    play sound "se/case_start.mp3"
    show text"{font=fonts/Type_Writer.ttf}{size=60}1959년 11월 16일{/size}{/font}" with memory:
        xalign 0.5 yalign 0.5
    $ renpy.pause(3.0)
    scene ev p_background with dissolve
    play music "bgm/Pathetique_Orgel.mp3"
    python:
        k = puzzle3()
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
            jump diary591116
label diary591116:
    ################################1959년 11월 16일 일기장 시작############################
    stop music
    scene black with memory
    play music "bgm/beat2.mp3"
    nvl clear
    narrator_nvl"1959년 11월 16일 월요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 추움"
    nvl clear
    narrator_nvl"어느새 이 회사에 취직 한 지 1년이 넘었다."
    narrator_nvl"1년동안 변한게 있다면……"
    narrator_nvl"나의 부서가 영업부로 바뀌었다는거다."
    narrator_nvl"하는 일은 주로 밖에 나가서 제품을 팔거나, 설문조사등을 통해 고객층을 확보하는 것"
    narrator_nvl"처음엔 힘들었지만, 지금와서 다시 생각해보면 나름 괜찮았다."
    narrator_nvl"물론 나의 \'괜찮다\'의 의미는 회사생활을 버틴다는 의미다."
    narrator_nvl"메리는 즐기면서 다니라고 하지만 그렇게 하기엔 사내에 친구가 단 한명도 없어서 지금은 하루를 버틴다는 생각으로 다니고있다."
    play bgs"bgs/people.mp3"
    centered"오전 10시 10분"
    scene bg employee_office_day with dissolve
    $ extra_name = '막스 부장'
    extra"토머 씨, 혹시 판매 500달러 달성 했어?"
    edward"네?{cps=2} {/cps}그건 뭐죠?"
    extra"우리 영업부로 들어온지 1년 이내에 500달러를 벌어오는 건데……"
    extra"설마 모르고 있었어?!"
    edward"네에……"
    extra"이거이거 어떡하나……"
    edward"호, 혹시 중요한건가요?!"
    extra"아주 중요하지"
    extra"일종의 회사 전통 같은거야"
    extra"아무튼, 토머 씨는 앞으로 1주일 정도 남았으니까 열심히 해"
    edward"1주일?!"
    "1주일 안에 장난감 500달러를 팔아오라니……"
    "이건 정말 불가능하다는 생각이 들었다."
    play sound "se/move.mp3"
    stop bgs
    scene black with moveright
    $ renpy.pause(0.5)
    play bgs"bgs/people.mp3"
    scene bg employee_lounge at Zoom((1280,720),(0,0,1280,720),(735,237,545,307),0.0) with moveright
    "500달러……{cps=2} {/cps}500달러……"
    "마음속으로 계속 중얼거렸다."
    "하지만 그렇다고 해서 바로 돈이 생기거나 하진 않았다……"
    show mary:
        zoom 2.0 xalign -2.0 yalign 1.0
        linear 2.0 xalign -0.1
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(2.0)
    mary"합석해도 괜찮을까요?"
    edward"맘대로 하세요……"
    play sound "se/search_bag.mp3"
    show mary:
        linear 0.6 yalign -0.3
    $ renpy.pause(0.6)
    edward"……?"
    play sound "se/shock.ogg"
    show effect1
    edward"{size=45}사, 사장님!{/size}" with lshake
    edward"있는지 몰랐습니다!"
    hide effect1
    show mary shock
    mary"토머 씨는 절 볼때마다 놀라시네요"
    "역시 사장님 이라는 엄청나게 높으신 분이 옆에 있으면 진정하기 힘들다."
    "특히 주변에서 날 죽일듯이 바라보는 게 더더욱 참기 힘들다."
    "근데……"
    extend" 생각해보니까 사장님이라면 지금 내가 가지고 있는 문제를 어떻게 해줄 수 있을지도 모른다."
    "저래봬도 일단 사장이니까 나만 특별 면제라든가……"
    edward"저, 저기…… 슈테른 사장님……"
    edward"제가 지금 곤란한 일에 처해 있는데……{cps=2} {/cps}혹시 도와주실 수 있을까요?"
    show mary talk
    mary"한번 말씀해보세요.{cps=2} {/cps}제 권한 내에서라면 어떻게든 도와 드릴게요"
    show mary tease
    mary"물론 제 권한이 안 닿는곳은 없지만"
    show black with dissolve
    "나는 500달러 건에 대해서 전부 말 했다."
    show mary think
    hide black with dissolve
    mary"흠……"
    show mary shock
    mary"그거 그냥 토머 씨를 놀리려는거 같은데요……"
    edward"정말요?!"
    edward"그, 그럼 전 굳이 장난감을 판매 할 필요없는거겠죠?"
    show mary think
    mary"글쎄요……"
    show mary talk
    mary"오히려 하는 게 좋지 않을까요?"
    show mary tease
    mary"\'프로젝트 코넙적\'이 있잖아요"
    mary"요구했던 판매량─500달러를 넘어서서 토머 씨를 놀렸던 사람의 코를 넙적하게 만들어요!"
    edward"음……"
    "난 그냥 아무것도 안해도 된다는 대답을 기대하고 있었지만, 오히려 더 힘든 요구를 해왔다."
    "장난감을 500달러 만큼 파는것도 힘든데, 그 이상을 버라니……"
    extend" 그것도 1주일 안에"
    edward"그건 진짜 힘들거 같은데요……"
    show mary smile
    mary"제가 같이 도와드릴게요"
    mary"그러면 문제 없겠죠?"
    edward"하, 하지만 그렇게 되면 제 힘으로 한게 아니니까 프로젝트 코넙적 이랑은 거리가 엄청 멀지 않나요?"
    show mary tease
    mary"\'역사는 승자의 기록이다\'라는 말이 있죠"
    mary"그러니 과정이 얼마나 더러워도, 나중에 토머 씨가 혼자서 달성했다고 서류에 기록하면 아무 문제 없잖아요?"
    edward"문제가 없다니……{cps=2} {/cps}그거 자체가 문제잖아요"
    mary"나중에 토머 씨가 크게 성공하면 문제가 안 될텐데요?"
    mary"어떤가요?"
    edward"뭔가 엄청 더러운 수 같은데……"
    "그래도 사장님의 말을 부정 할 순 없었다."
    "왜냐면 이 세상은 예나 지금이나 항상 결과만을 봤으니까"
    "어차피 나도 그런 결과주의적인 생각을 가지고 있으니까 뭐라 할 순 없겠지만……"
    edward"잘 알겠습니다"
    show mary smile
    mary"그럼 출근 후에 같이 생각해보도록해요"
    scene black with Dissolve(1.0)
    stop music
    stop bgs
    "나는 사장님과 늘 만나던 공원에서 기다렸다."
    play sound "se/move.mp3"
    scene bg diary_park_night at Zoom((1280,720),(279,237,408,229),(319,267,331,186),0.0) with moveright
    play music "bgm/smooth1.mp3"
    show mary:
        zoom 1.6 xalign 0.7 yalign -0.2
    mary"그럼 판매 전략을 세워볼까?"
    edward"네에……"
    show mary talk
    mary"밖에선 말 놓아도 된다고 했잖아"
    edward"그, 그랬지"
    show mary
    mary"우선 목표 금액부터 정하자"
    mary"실제 현장에서 영업은 내가 할테니까, 목표 금액 정도는 직접 정해줘"
    mary"물론 회사에서 널 놀린 사람들의 코를 넙적하게 할거니까, 목표 금액은 최대한 높게"
    edward"음……"
    "나는 그냥 옆에 따라가고, 실제 영업은 메리가 전부 한다고 했으니까 아무리 금액을 높게 잡아도 나한텐 별로 힘들게 없다."
    "하지만 일도 안하면서 돈을 많이 벌려는 건 내 양심이 허락하지 않는다."
    edward"600달러……{cps=2} {/cps}정도는 어떨까?"
    show mary shock
    mary"고작 100달러 더 벌어왔다고 회사에서 널 다시 봐줄 거 같진 않은데?"
    edward"그럼 700!"
    show mary smile
    mary"1000 어때?!"
    edward"그, 그건 너무 많지 않나?!"
    show mary shock2
    mary"확실히 처음부터 1000달러 까진 힘들겠네……"
    mary"그럼 안전하게 800으로 가자"
    edward"그래……"
    show mary
    mary"이젠 장소를 정해볼까?"
    edward"근처 대형 마트 같은 게 좋지 않을까?{cps=2} {/cps}거긴 돈이 많으니까"
    show mary talk
    mary"하지만 몰턴에서 가까운덴 내가 널 도와줬다는 소식이 닿일 확률이 높아서 힘들어"
    show mary
    mary"그래서 나한테 한가지 제안이 있지!"
    mary"\'이스티아나(Eastiana)\'는 어때?"
    edward"그 촌구석에……?"
    mary"맞아"
    edward"거길 고른 이유는 따로 있어?"
    show mary smile
    mary"동양음식이 맛있으니까"
    show mary shock
    mary"……물론 먹는거 하나 때문에 고른건 아니고"
    mary"내가 알기로, 거긴 에드워드의 고향이라서 비교적 편할거 아니야?"
    edward"어, 어떻게?"
    show mary shock2
    mary"얼마 전에 말해줬잖아"
    edward"아……{cps=2} {/cps}생각해보니까 잠깐 말 한 적이 있었구나……"
    "이렇게 일기장을 쓰면서도 나는 가끔 내가 과거에 무슨 말을 했는지 까먹을때가 많다."
    "원인은 내 기억력이 나쁘다기 보단, 내가 한 행동에 대해서 집중을 하지 않기 때문이라 생각된다."
    show mary
    mary"어쨌건, 그럼 목적지는 이스티아나로 괜찮지?"
    edward"근데 거긴 엄청난 시골인데?{cps=2} {/cps}거기서 장난감을 800달러 어치 팔 수 있을까?"
    show mary tease
    mary"그런식으로 시골이기 때문에 가능한 전략도 있거든"
    mary"날 믿어봐"
    edward"으, 응……"
    show mary
    mary"그럼 내일은 출장으로 돌려서 바로 몰턴역에서 만나자!"
    scene black with Dissolve(1.0)
    "이스티아나는 나의 고향……{cps=2} {/cps}거긴 아주머니도 살고계신다."
    "물론 일 때문에 가는거라서 내가 아주머니를 만나 뵐 수 있을진 모르겠지만, 그래도 사전에 연락은 드리고 싶었다."
    "귀찮긴해도 자기전에 집주인 아저씨한테 가서 전화를 좀 이용해야겠다."
    stop music
    play bgs "bgs/people.mp3"
    centered"다음 날"
    centered"몰턴역"
    play music "bgm/beat4.mp3"
    scene bg diary_trainstation with moveup
    $ renpy.pause(0.5)
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(445,251,835,469),0.7)
    $ renpy.pause(0.7)
    show mary tsun with dissolve:
        zoom 1.5 xalign 0.4 yalign -0.2
    mary"숙녀를 기다리게 만들다니"
    edward"미, 미안……"
    edward"길을 잃어버려서……"
    "몰턴역은 내가 여기로 처음 이사왔을때 딱 한번 와봤다."
    "……역시나 사람이 가득하다."
    mary"암튼, 담부턴 내가 오기 5분 전에 미리 도착하도록 해"
    edward"근데 사장ㄴ……{cps=2} {/cps}이 아니라, 메리가 언제 올지 내가 어떻게 알아?"
    mary"그야 감으로 알아야지"
    "메리의 매우 힘든 요구를 듣자, 절로 한숨이 나와버렸다."
    "근데 처음 왔을땐 몰랐는데, 자세히 보니까 메리의 짐이 엄청 많았다."
    edward"짐이 많네……?"
    show mary
    mary"오늘 팔아치울 장난감.{cps=2} {/cps}원가 기준으로 전부 800달러야"
    show mary shock
    mary"이거 얼마나 무거운지 알아?"
    mary"물론 차로 운반해서─싣고, 내릴때만 무거웠지만"
    edward"수고하셨습니다……"
    edward"그, 근데 혹시 하루만에 800달러 다 팔 생각이야?!"
    show mary talk
    mary"그럴건데?"
    edward"힘들텐데……"
    show mary
    mary"이거 드는 거 보단 덜 힘들거야"
    show mary smile
    mary"그리고 그런 말 하기 전에 내가 준비한 애들을 봐바!"
    play sound "se/search_bag.mp3"
    show mary think:
        linear 0.3 yalign -0.6
        linear 0.3 yalign -0.2
    $ renpy.pause(0.6)
    "메리는 샘플용 장난감 여럿을 꺼내들었다."
    show mary tease
    mary"첫번짼 NT121호기, 알루봇!"
    "알루미늄 재질로 만들어진 장난감 로봇이다."
    "특징이라면, 재질이 알루미늄이라서 플라스틱으로 만든 것 보다 훨씬 로봇스러워서 인기가 있다."
    mary"두번짼 재고가 쌓인 NT95호기, 광선빔"
    "플라스틱으로 만든 장난감 총이다."
    "제품 자체는 흔히 볼 수 있는 광선총 같지만, 세일즈 포인트가 바로 방아쇠를 당기면 내부에 달린 모터로 인해 짧은 진동이 생기는거다."
    "소비자의 반응은 좋지만, 아쉽게도 가격이 타 제품보다 비싸서 비교적 안 팔린다."
    mary"세번짼 대량생산에 용의한 NT32호기, 미니 벌레 플라스틱 모델"
    "역시나 플라스틱으로 된, 손바닥보다 작은 벌레 모형이다."
    "개미, 풍뎅이, 나비 등 종류도 다양하고, 가격도 싸서 판매량만 따지면 꽤 높다."
    mary"마지막이 신제품인 NT129호기, 기지 조립세트"
    show mary talk
    mary"내가 들고온거 중에서 가장 비싼거라 어떨련진 모르겠지만……"
    "NT129호기는 이름대로 집접 조립 할 수 있는 기지 같은거다."
    "거기다 안에 작은 병정 같은것도 있기 때문에 가지고 놀면 꽤 재미있다는 듯 하다."
    show mary
    mary"그래도 만일의 사태를 위해서 저가의 작은 애들이랑 회사 카탈로그도 들고왔으니까 상관없지"
    edward"역시 준비성이 철저하네"
    show mary tease
    mary"난 하버드 졸업한 여자니까"
    play sound "se/train.mp3"
    show mary shock
    mary"엇!{cps=2} {/cps}기차온다!"
    mary"얼른 짐 들어!"
    edward"내가?!"
    mary"남자잖아!"
    play sound "se/move.mp3"
    stop music
    stop bgs
    scene black with moveright
    centered"오전 10시 20분"
    centered"이스티아나"
    play music "bgm/happy5.mp3"
    play bgs "bgs/birds.mp3"
    scene ev sky_clear with moveright
    "우린 몇시간 동안 기차를 타서 이스티아나 역에 도착했다."
    scene bg diary_country at Zoom((1280,720),(686,0,547,307),(686,0,547,307),0.0) with Dissolve(1.0)
    scene bg diary_country at Zoom((1280,720),(686,0,547,307),(686,349,547,307),1.0)
    "그리고 즉시 영업을 개시하러 사람들이 있는 쪽으로 이동했다."
    "일단 여긴 내 고향이기도 하니까 자연스럽게 길은 내가 안내하기로 됐다."
    show mary shock with dissolve:
        zoom 1.6 xalign 0.9 yalign -0.3
    mary"동네는……"
    extend" 아직이야……?"
    edward"이 언덕만 넘으면 되는 걸로 기억 해……"
    edward"허어……{cps=2} {/cps}허어……"
    edward"근데 짐을 너무 많이 챙겨와서 힘들잖아……"
    mary"800달러의 무게라고 생각 해……"
    show mary cough
    $ renpy.vibrate(0.3)
    mary"콜록……{cps=2} {/cps}콜록……" with sshake
    mary"아, 너무 숨이 차버렸어……"
    edward"그럼 그쪽 짐도 이리 줘"
    show mary shock with dissolve
    mary"괜찮겠어?"
    edward"평생을 노가다로 단련시킨 몸이니까……{cps=2} {/cps}고작 그정도론 문제 없어"
    show mary shy
    mary"음……{cps=2} {/cps}자, 여기"
    play sound "se/search_bag.mp3"
    show mary shy with dissolve:
        linear 0.3 zoom 1.8 yalign -0.4
    show mary shy with dissolve:
        linear 0.3 zoom 1.6 yalign -0.3
    "메리는 나에게 짐을 옮겼는데……{cps=2} {/cps}일단 무게는 그렇다 쳐도, 손에 들 공간이 없어서 생각보다 힘들었다……!"
    edward"영차!"
    "기합을 넣어서 짐을 제대로 들었다."
    edward"빠, 빨리 가자!"
    mary"응"
    play sound "se/footsteps_concrete.mp3"
    scene bg diary_country at Zoom((1280,720),(686,349,547,307),(269,0,661,371),2.0) with dissolve
    $ renpy.pause(2.2)
    play sound "se/move.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg diary_ssm with moveleft
    play sound "se/footsteps_concrete.mp3"
    edward"으으……"
    edward"후우……"
    "처음엔 괜찮을거라 생각했던 짐을 계속 들다보니까─어느새 숨이 헐떡이는 지경으로 힘들었다."
    show mary talk with dissolve:
        zoom 1.6 xalign 0.7 yalign -0.2
    edward"저, 저기……{cps=2} {/cps}몇 개만 대신 들어주면 고맙겠는데……"
    mary"어?"
    "메리는 힘들어하는 나의 제안을 무시하더니, 길가에 있는 구멍가게를 보더니 멈춰섰다."
    mary"에드워드, 저거 뭐야?"
    "나는 짧은 한숨을 내쉬면서 답 했다."
    edward"구멍가겐데……{cps=2} {/cps}혹시 처음봐?"
    mary"아─{cps=2} {/cps}저게 구멍가게구나"
    mary"몰턴에서도 비슷한건 몇개 봤는데 이렇게 생긴 건 처음보네"
    show mary
    mary"역시 이스티아나"
    mary"오리엔스의 오리엔탈 이라는 소문이 사실이었어"
    edward"일단 거주민들의 대다수가 오리엔탈 이니까"
    show mary smile
    mary"좋아!{cps=2} {/cps}여길 우리들의 첫 공략지로 하자!"
    edward"서, 설마 여기다 장난감을 납품하게?!"
    edward"여긴 그렇게 돈이 많아보이진 않은데"
    show mary tease
    mary"내 계획대로 하면 문제 없어"
    show mary with dissolve:
        zoom 1.0 xalign 0.5 yalign 1.0
    play sound "se/door_knock.mp3"
    mary"안에 누구 있나요~?"
    $ renpy.pause(0.5)
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(2.5)
    play sound "se/door_open.ogg"
    $ extra_name = '구멍가게 주인 할머니'
    extra"아이고오……"
    show mary with dissolve:
        xalign 0.6
    extra"어서 오세요……"
    show mary smile
    mary"만나서 반갑습니다!"
    play sound "se/book_page.ogg"
    show mary smile:
        linear 0.6 xalign 0.5
        linear 0.3 xalign 0.7
    "메리는 주인 할머니에게 미소를 잃지 않고 명함을 건네줬다."
    mary"저는 이런 사람인데요……"
    extra"음?"
    extra"이렇게 높으신분이 여긴 무슨일로?"
    mary"저희 회사에서 여기에 장난감을 납품 하고 싶어서 왔습니다!"
    extra"여기에?{cps=2} {/cps}이런 볼꺼 없는 촌구석까지 왔다고?"
    mary"여러 가게에 물건을 내놓을 수록 좋다고 생각해서 여기까지 발길을 옮기게 됐어요"
    extra"으음……{cps=2} {/cps}근데 이런 구멍 가게에서 팔겠다고 해도……"
    extra"일단 뭐가 있는지 보기라도 하겠네"
    mary"넵!"
    play sound "se/search_bag.mp3"
    show mary with Dissolve(1.0):
        alpha 0.0
    "메리는 우리가 들고온 많은 짐들을 풀어헤치기 시작했다."
    "그리고 NT32호기, 미니 벌레 플라스틱 모델을 꺼내서 보여줬다."
    show mary with dissolve:
        alpha 1.0
    mary"얘가 지금 저희 회사에서 가장 판매량이 높고, 가격이 가장 저렴한 벌레 장난감 입니다!"
    mary"거의 24종 넘게 있으니 모으는 재미도 있어서 좋죠"
    extra"가격이 어떻게 되는고?"
    mary"2개에 한박스로, 박스당 99센트 입니다"
    extra"으음~{cps=2} {/cps}조금 비싼거 같은데?"
    "할머니의 대답 때문에 팔지 못할까봐 두려워진 난 다급해하며 입을 열었다."
    edward"그, 그래도 이정도면 도시에선……"
    show mary shock with dissolve:
        zoom 1.7 yalign -0.4
    mary"쉿!"
    mary"내가 다 알아서 할거니까 가만히 있어"
    show mary with dissolve:
        zoom 1.0 yalign 1.0
    mary"개당 99센트라 해도 여기에 팔려면 적어도 50박스 이상은 사야되고, 그정도면 약 50달러라 싼 가격은 아니죠"
    extra"뭐어……{cps=2} {/cps}바로 50박스 씩이나 살 생각은 없었지만, 내 말이 그말이지"
    mary"하지만 반대로 생각해보면, 완판되면 이익이 생기잖아요?"
    extra"하지만 정말로 이런 장난감만 가지고 완판 될 수 있으려나……"
    show mary tease
    mary"이런 장난감이기 때문에 완판되기 쉽죠"
    mary"제가 미리 말씀 드리지 않았나요?"
    stop music
    extend" 24종이 넘기 때문에 모으는 재미가 있다고요"
    extra"그랬다만 그게 어쨌다는 건가?"
    play music "bgm/sirius4.mp3"
    mary"그 말은 즉슨 한번 구매한 아이도 다시 한번 더 구매할 확률이 높아진다는 뜻입니다"
    mary"특히 소비자가 도시에 비해서 적은 여기선 정말로 필요한게 아닌가요?"
    mary"또한 이 장난감은 박스당 99센트 입니다"
    mary"애들 용돈과 거의 맞먹는 금액이죠"
    mary"보통 장난감은 애들이 부모님을 졸라서 사달라는 형태를 띄지만, 이 장난감은 가격이 애들의 용돈과 맞먹기 때문에 부모님의 허락이 필요 없어지게 되죠"
    mary"즉, 이 장난감은 다른 물건들보다 아이들에게 파는데 매우 용의 합니다"
    extra"드, 듣고보니까……"
    extra"하지만 내가 이걸 99센트에 사서 99센트에 팔아버리면 남는 게 없잖아?"
    extra"그렇다고 가격을 더 올려버리면 아까 말했던게 무산이 되고"
    show mary
    mary"아,{cps=2} {/cps}제가 말한 99센트는 \'희망 소비자 가격(MSRP)\'이에요"
    mary"실제로 언니가 내실 금액은 50박스에 35달러죠"
    extra"흠……{cps=2} {/cps}생각보다 저렴하구만……"
    extra"그럼 그걸……"
    show mary shock2:
        linear 0.3 xalign 0.5
    stop music
    mary"앗!{cps=2} {/cps}우선 제가 가져온 물건들을 더 보신 다음에 결정해주세요"
    mary"그렇게 섣불리 사버렸다간 어쩌면 더 좋은 이익을 놓칠 수 있을지도 모른다고요?"
    play music "bgm/happy3.mp3"
    show mary:
        linear 0.6 xalign 0.7
    extra"하하하!{cps=2} {/cps}이거, 젊은 처자가 말을 아주 잘 하는구나!"
    extra"맘에들어!"
    show mary smile
    mary"과찬이십니다……"
    extra"그래서 다음 물건은 뭔가?"
    play sound "se/search_bag.mp3"
    show mary with dissolve
    "메리는 가장 비싼 장난감인 NT129호기를 꺼내들었다."
    mary"바로 이겁니다!"
    mary"분리된 파츠를 조립해서 자신만의 비밀기지를 직접 만들 수 있는 장난감이에요"
    mary"안엔 제가 앞서 보여드린 벌레 모델들이랑 비슷한 크기의 플라스틱 병정들도 들어있죠"
    extra"근데 이건 엄청나게 비싸보이는데……"
    show mary shock2
    mary"가격은 도매가로 개당 38.54달러 예요……"
    extra"음……{cps=2} {/cps}역시 그건 대량으로 구매하기 힘들거 같군……"
    mary"확실히 이 장난감은 제가 처음 보여드린 것 과는 정 반대의 특징이죠"
    mary"애들 용돈으론 살 수 없고……{cps=2} {/cps}딱히 종류가 여럿이 있는것도 아니고……"
    extra"그치, 내가 비싼 돈 주고 팔릴지 말지 모를만한 물건을 어떻게 내 가게에 올릴겠나"
    show mary tease
    play music "bgm/sirius4.mp3"
    mary"하지만 시간만 들인다면 그 무엇보다 잘 팔린다는 걸 약속드립니다"
    extra"……?"
    mary"혹시 오늘이 며칠인지 아세요?"
    extra"11월 17일 이었던걸로 기억 하는데……"
    mary"크리스마스 까지 앞으로 1개월 하고 8일정도가 남았죠"
    mary"그리고 크리스마스는 장난감이 가장 잘 팔리는 시기예요"
    extra"지금 무슨 말을 하려는진 잘 알겠는데, 그렇다면 지금 그걸 사기엔 너무 이르지 않나?"
    mary"아니요.{cps=2} {/cps}딱 적당하다고 생각해요"
    mary"제가 잠깐 둘러봤는데, 이 구멍가게 안엔 이거처럼 큰 장난감은 없더군요?"
    extra"우린 단순한고 싼거만 파니까"
    mary"그렇기 때문에 더더욱 충분한 시간을 둬서 사람들에게 저 장난감의 존재를 인식 시킬 필요가 있는거예요"
    mary"이 장난감을 가게 안에서 잘 보이는 곳에 놔두면 애들은 가지고 싶어 할겁니다"
    mary"하지만 당장은 살수 없기 때문에 아이들은 부모님에게 떼를 쓰겠죠"
    mary"그것도 크라스마스 당일이 올때까지 반복적으로"
    show mary smile
    mary"물론 모든 애들이 다 그럴거란 보장은 없지만요"
    extra"아니, 뭔가 일리가 있는거 같구나"
    extra"굳이 모든 애들이 그렇게 하지 않아도, 이렇게 비싼건 10개만 팔아도 나름 괜찮은 수익이지"
    show mary tease
    mary"정말 똑똑하세요~"
    mary"근데 생각해보니까 여긴 동네에서 엄청 가깝네요?"
    extra"그렇지"
    mary"그럼 이걸 살 부모님들도 먼 길을 걸을 필요가 없으니까 확률적으로 봤을땐 판매에 많이 유리하네요"
    extra"으음……"
    extra"근데 역시 가격이 좀 쎄네……"
    show mary shock2
    mary"그런가요?"
    extra"혹시 조금만 더 깎아줄 순 없는가?"
    show mary think
    mary"그럼 저희 쪽에서가 좀 곤란한데……"
    show mary
    mary"대신, 이걸 20박스 이상 사시겠다면 개당 2달러 정도 깎아서 36.54달러에 드릴순 있어요"
    show mary shock
    extra"에이, 좀 더 깎을 수 있잖아"
    "할머니는 아까보다 더 흥정을 하기 시작했다."
    "원래는 원칙상 가격을 깎는 건 가급적 금지돼 있는데……{cps=2} {/cps}메리도 무슨 생각을 했던건지 난 그때 잘 몰랐다."
    mary"언니,{cps=2} {/cps}저희도 전부 원가랑 인건비 계산해서 가격을 정하는거라 1달러도 깎기 힘들어요"
    extra"그래도 이쪽은 돈이 많은 게 아닌데……"
    show mary think
    mary"하지만……"
    mary"어쩔 수 없나……"
    show mary smile
    mary"언니한텐 제가 특별히 개당 33.76달러에 드릴게요!"
    show mary shock2
    mary"원래 가격에서 5달러 이상이나 깎은 거니까 저희한테도 남는 게 거의 없어요"
    extra"오호호!{cps=2} {/cps}정말 구맙구나~!"
    extra"그렇게까지 깎아주고"
    show mary smile
    mary"역시 장난감은 아이들의 손에 있어야 비로서 빛을 발하잖아요~"
    mary"저도 팔수만 있다면 정말 기뻐요"
    extra"보면 볼수록 맘에 드는구나~!"
    show mary
    mary"근데 크리스마스를 노릴거면 장난감 종류를 좀 더 많이 진열하시는 게 판매량을 높이는데 좋을거예요"
    mary"여기 카탈로그 한번 보세요"
    extra"음음"
    "할머니는 한동안 물건을 보면서 생각하다가 입을 열었다."
    extra"음!{cps=2} {/cps}결정했어!"
    extra"이거하고 이거 60박스"
    extra"그리고 이거 35박스 주시구려!"
    show mary smile
    mary"정말 감사합니다~"
    mary"장사 잘 되시길 바랄게요!"
    extra"나도 처자가 많이 팔길 빌게"
    "와……"
    "메리의 말 솜씨와 판매 전략을 보면서 감탄사 밖에 안 나왔다."
    "하지만 신제품인 NT129호기를 좀 깎아서 우리에게 개당 5달러의 손해가 온게 조금 걸렸다."
    stop music
    show mary with dissolve:
        zoom 1.7 yalign -0.2 xalign 0.7
    mary"에드워드,{cps=2} {/cps}이제 슬슬 가볼까?"
    edward"근데 많이 깎아버려서 우리쪽에서 큰 손해를 봤는데도 괜찮아?"
    mary"그건 나중에 가면서 말 해줄게"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg country_way with moveright
    show mary:
        zoom 1.7 xalign 0.3 yalign -0.3
    mary"아까 내가 영업하면서 손해를 봤었다고 했지?"
    edward"응"
    show mary smile
    play music "bgm/beat5.mp3"
    mary"그거 사실 내가 처음부터 높은 금액을 제시해서 원래 도매가로 깎은거야"
    mary"금액을 정수가 아니라 소수점 까지 해서 복잡하게 한것도 첨에 제시한 높은가를 쉽게 기억하지 못하기 위한 전략이었고"
    mary"거기다 이런 시골은 정보가 많이 부족하기 때문에 원래 장난감이 얼마정도 하는지 전혀 모르고있어"
    edward"그, 그럼 어제 말한 시골이기 때문에 가능한 전략이라는 게……"
    show mary tease
    mary"딩동댕~♪"
    edward"음……{cps=2} {/cps}뭔가 수가 더럽네……"
    show mary shock
    mary"처음부터 가격을 높게 제시하는 건 판매 전략의 기초중에서 기초인데?"
    mary"어쨌건 난 결과적으로 원래 가격대로 판거니까 딱히 그쪽에서 손해가 있었던것도 아니고"
    edward"그런가……"
    show mary
    mary"근데 내가 쓴 전략은 단순히 그거만 있는 건 아니야!"
    mary"NT32호기를 팔때 내가 먼저 소매 희망가를 불러서 했잖아?"
    mary"그렇게 하면 내가 두번째로 말 한 도매가가 소매가에 비해 상대적으로 적게 보이니까 상대방이 좀 더 안심 하지"
    mary"내가 굳이 이런 구멍 가게에 팔겠다는 것도 말이야"
    mary"구멍 가게는 굳이 따지자면, 개인 사업에 해당되거든"
    mary"그래서 대형 마트 같은데서 납품할때 요구되는 귀찮은 절차가 바로 생략돼!"
    show mary tease
    mary"뿐만 아니라, 할머니랑 얘기할땐 장난감의 특징보단 그걸 팔았을때의 수익과 그 전략에 중점을 둔것도 일부러 한거지"
    mary"사람들은 자신의 이익이 뭔지를 알고 싶어하거든"
    mary"애들을 상대로 할 땐 이게 왜 재미있는가, 어른을 상대로 할땐 이걸 왜 사야 하는가"
    edward"정말 대단하네……"
    edward"이대로라면 하루만에 800달러를 채우는거 가능할지도 몰라"
    show mary smile
    mary"내가 말했잖아!{cps=2} {/cps}나만 믿으라고!"
    "메리는 정말 똑똑한 여자다."
    "단순히 똑똑한걸 넘어서서 대단하다는 생각이 들었다."
    "고작 나같은 인간이 계속 옆에 있어도 괜찮은걸까 라는 생각이 들 정도로……"
    show mary shock2
    mary"에드워드 혹시 배고프지 않아?"
    edward"전혀"
    extend", 왜, 배고파?"
    show mary shy with dissolve
    mary"…………"
    edward"……?"
    show effect1
    play sound "se/shock.ogg"
    show mary shy2
    mary"{size=45}어! 배고파!{/size}" with lshake
    edward"히익!"
    hide effect1
    edward"왜왜왜 화를내…… 세요?"
    show mary tsun
    mary"아, 몰라"
    mary"그냥 다음 가게 찾아서 빨리 장난감들 팔아 치우자"
    edward"그래……"
    show mary shock3 with dissolve
    mary"잠깐, 설마 진짜로 그냥 갈거야?"
    edward"그, 그런데?"
    mary"밥은……?"
    edward"아까 네가 그냥 가자고 해서……"
    edward"그리고 이렇게 많은 짐을 들고있으면 식당에 들어가기 힘드니까 빨리 처리하는 게……"
    mary"그럼 어디 짐 좀 맡길때를 찾고, 밥을 먹으러 가야될거 아니야?!"
    mary"내가 굳이 이스티아나로 오자고 한것도 밥 때문이라고 했거늘……"
    edward"미안……{cps=2} {/cps}난 그런거 잘 몰라서……"
    edward"그리고 짐을 어디에 맡겨야 할지도 모르고"
    mary"여관 같은데서 방이라도 잡고, 거기다 짐 다 놔두고 편하게 움직이면 되잖아?"
    mary"돌아다니면서 어디다 납품할지 장소 체크도 할 겸사"
    mary"진짜 센스가 하나도 없네"
    edward"그건 센스를 넘어서서 완전 초능력에 가까운 요구야……"
    show mary tsun
    mary"어쨌건 난 이대론 힘들어서 영업 못해"
    "짐을 들고있는 건 난대도 저런 반응을 보이니까 정말 짜증났다."
    "역시 부자집의 딸이라 엄청 귀하게 자라서 저런걸까"
    "하지만 짐을 맡긴다라……"
    "아주머니를 만나러 가면 될지도 모른다!"
    "여관까진 아니지만, 아주머닌 아파트 주인이시니까!"
    edward"그럼 짐부터 좀 놔두고 돌아다닐까?"
    mary"뭐 좋은 여관 같은거라도 알아?"
    edward"내가 아는 사람이 여기 살고 있거든,{cps=2} {/cps}그 사람 한테 찾아가면 될거야"
    mary"그래"
    stop music
    stop bgs
    scene black with dissolve
    centered"10분 후"
    "아주머니 집 앞까지 도착했다."
    "이게 몇 년 만인가……"
    "나는 떨리는 손으로 문을 두드렸다."
    play sound "se/door_knock.mp3"
    $ renpy.pause(2.0)
    play sound "se/door_open.ogg"
    scene bg room_tatami:
        crop(554,0,726,408)
        size(1280,720)
    show elsara mad:
        xalign 1.0 yalign 1.0
    show ev elsaras_door
    show white
    "그리고 얼마 지나지 않아서 문이 열렸다."
    hide white with dissolve
    show elsara talk:
        linear 2.0 xalign 0.7
    play sound "se/footsteps_wood.mp3"
    elsara"……?"
    hide elsara talk with dissolve
    show elsara talk with dissolve:
        xalign 0.6 yalign 1.0
    elsara"뭐야, 너였냐"
    play music"bgm/beat2.mp3"
    edward"아아아아, 안녕하세요!"
    edward"몇 년 만이네요!"
    elsara"이 시간에 여긴 왜 왔어?"
    edward"그게 회사 출장 때문에 제가……"
    elsara"그건 어제 너한테서 전화로 들었으니까 됐고"
    elsara"여기 온 이유가 뭐냐고,{cps=2} {/cps}설마 몇 년 만에 와본거라면서 고작 인사만 하겠다고 온 건 아니겠지?"
    "아주머니는 하나도 바뀐게 없었다."
    "잔정 같은건 없고, 필요한 것만 딱딱 말 하는 저 태도……{cps=2} {/cps}난 편해서 좋다."
    edward"설마 제가 그냥 인사만 하러 왔겠습니까?!"
    show elsara talk
    elsara"그래, 내가 네 엄마가 되주겠다고 한적은 없으니까 그냥 얼굴만 보러 오는 건 사절이야"
    edward"제가 찾아 봰 이유는……"
    extend" 짐 좀 맡기려고요"
    show elsara mad
    show effect1
    play sound "se/shock.ogg"
    elsara"{size=45}그 이유는 더 싫어!{/size}" with lshake
    hide effect1
    elsara"내가 아까 한 말의 의미는 선물을 가지고 왔냐고, 선물을!"
    elsara"넌 어째 사회인이 돼서도 그 모양이냐?"
    edward"죄, 죄송합니다……"
    elsara"자주 사과하지 말고!"
    show elsara talk
    elsara"음?"
    "아주머니의 큰 소리 때문에 겁먹고 내 뒤에 숨어있는 메리를 보면서 입을 열었다."
    elsara"근데 뒤에 누군가 있는 고운 처자는 누군가?"
    play sound "se/search_bag.mp3"
    show mary shock2:
        zoom 1.8 xalign 2.0 yalign -0.3
        linear 0.7 xalign 1.2
    "내 뒤에 있었던 메리는 나와서 아주머니께 인사 드렸다."
    mary"아, 안녕하세요……"
    mary"메리 슈테른 이라고 합니다"
    stop music
    show elsara mad with dissolve
    elsara"메리……{cps=2} {/cps}슈테른……?"
    edward"혹시 아세요?"
    show elsara talk
    elsara"알긴 하다만……{cps=2} {/cps}직접 만나보는 건 오늘이 처음이네"
    "메리는 꽤나 유명한 인물이다."
    "나 역시도 신문을 통해서 관련 소식은 여러번봤으니, 아주머니도 한번쯤 들어봤다고 해도 이상할 건 없다."
    elsara"…………"
    elsara"차라도 한잔 내올테니까 일단 안으로 들어 오거라"
    scene black with Dissolve(1.0)
    play music "bgm/smooth3.mp3"
    scene bg room_tatami with movedown
    "우린 방 안으로 발길을 옮겼다."
    "근데 내가 저번에 왔을때에 비해서 방의 모습이 조금 바뀐거 같았다."
    "한때 편지로 집을 리모델링 한다고 한적이 있었는데, 그 때문인가보다."
    scene bg room_tatami at Zoom((1280,720),(0,0,1280,720),(807,336,473,266),0.5)
    "우린 아주머니가 내온 차를 마시며 식탁에 둘러 앉았다."
    show elsara talk:
        zoom 1.6 xalign 0.0 yalign -0.3
    edward"집안에 많이 깔끔해지고, 좋네요"
    elsara"네가 회사에 취직 한 이후로부턴 우리한테 돈을 많이 보내주니까 할 수 있었어"
    elsara"근데 내 얘기는 됐고……"
    show mary talk with dissolve:
        zoom 1.6 xalign 1.0 yalign -0.3
    "아주머니는 나와 메리를 번갈아 보면서 입을 여셨다."
    elsara"둘이서 어떻게 만났니?"
    edward"만났다니……{cps=2} {/cps}그냥 제가 회사에 들어가려고 면접을 봤을때 만났는데요"
    elsara"그 장난감 회사 말 하는거지?"
    edward"네"
    show elsara with dissolve
    "갑자기 아주머니의 입가에 푸근한 미소가 번진게……{cps=2} {/cps}평상시 내가 알고 지냈던 아주머니와는 사뭇 다른 느낌이었다."
    elsara"너희 둘은 정말 운명이라고 밖에 설명 할 수 없는 사이 같아보이는구나……"
    show effect1
    play sound "se/shock.ogg"
    show mary shy2
    edward"{size=45}네?!{/size}" with lshake
    hide effect1
    "아주머니는 엄청나게 뜬금없는 말씀을 하셔서, 나를 당황케 만들었다."
    mary"큽……!"
    "메리도 얼마나 당황했으면 마시고 있던 차를 살짝 뿜었다."
    elsara"정말 너흰 지금 당장 결호ㄴ……"
    play sound "se/footsteps_running.mp3"
    scene bg room_tatami at Zoom((1280,720),(807,336,473,266),(0,141,621,349),0.7)
    "나는 아주머니가 이 이상 엉뚱한 말을 하지 못하도록 아주머니의 팔을 붙잡고 재빨리 구석으로 자리를 옮겼다."
    stop sound
    show elsara mad:
        zoom 1.8 xalign 0.5 yalign -0.3
    elsara"이놈! 갑자기 무슨 짓이냐!"
    edward"재, 재발 그런 소리는 하지 말아주세요!"
    edward"메리는 회사에서 제 상사란 말이에요!"
    show elsara talk
    elsara"그럼 둘이서 사귀거나 하진 않는거냐?"
    edward"그런건 전혀 없어요!"
    scene bg room_tatami at Zoom((1280,720),(0,141,621,349),(807,336,473,266),0.0)
    show mary shy:
        zoom 1.6 xalign 1.0 yalign -0.3
    elsara"근데 저 아이는 너한테 관심 있는거 같은데?"
    scene bg room_tatami at Zoom((1280,720),(807,336,473,266),(0,141,621,349),0.0)
    show elsara talk:
        zoom 1.8 xalign 0.5 yalign -0.3
    edward"그, 그럴지도 모르지만……"
    "……문제는 내가 메리한테 별 감정이 없다."
    "솔직히 말해서 메리가 나의 상사이자 노스탤지어 토이즈의 사장만 아니었다면 내가 이러지도 않았을거다."
    "나도 어디까지나 일 때문이라는 생각만으로 메리를 상대하고 있으니……"
    edward"어쨌건, 부탁이니까 앞으론 괜한 말은 삼가해주세요"
    elsara"알겠어─"
    play sound "se/footsteps_wood.mp3"
    scene bg room_tatami at Zoom((1280,720),(0,141,621,349),(807,336,473,266),2.0)
    $ renpy.pause(2.0)
    show elsara:
        zoom 1.6 xalign 0.0 yalign -0.3
    show mary shy:
        zoom 1.6 xalign 1.0 yalign -0.3
    elsara"이거, 아깐 내가 정말 실례 했수다"
    elsara"듣자하니까 우리 에드워드의 회사 상사라고 하시던데……"
    mary"ㄴ, 네……!"
    elsara"부족한 녀석이지만, 잘 부탁 드려요"
    "아주머니는 내 엄마 역할은 사절이라고 했던 말과는 반대로, 고개까지 숙여가면서 말하셨다."
    show mary shock2
    mary"아뇨!{cps=2} {/cps}저야말로!"
    elsara"이스티아나가 좁아터진 시골이긴 하지만, 그래도 정겨운 곳이니까 짐은 여기 놔두고 천천히 편하게 있다가세요"
    mary"정말 감사합니다"
    edward"아, 근데 여기 혹시 뭐 맛있는 곳 없어요?"
    edward"돌아다니면서 배가 많이 고파졌거든요……"
    show elsara talk
    elsara"음식이라면, 쟝 네에 가보거라"
    elsara"거기 최근에 새로운 레시피를 발명했다면서 맛이 좋아졌다고 하던데"
    edward"거기 아직도 영업 해요?"
    show mary talk
    mary"쟝 네……?"
    edward"쟝 아저씨라고 중국에서 오신 분이 있는데, 근처에서 식당을 하셔"
    edward"혹시 중국요리 괜찮다면 거기 들려도 되는데……"
    show mary smile
    mary"응!{cps=2} {/cps}난 좋아!"
    edward"그럼 점심은 거기로 결정인가……"
    show elsara
    elsara"늦으면 여기서 자도 되니까 천천히 있어"
    edward"갑자기 왜그렇게 친절하게 대하시는거예요……{cps=2} {/cps}무서워요"
    show elsara mad
    show effect1
    play sound "se/shock.ogg"
    elsara"예끼! 이놈이!" with lshake
    scene black with Dissolve(1.0)
    stop music
    centered"몇 분 후……"
    play bgs "bgs/birds.mp3"
    scene bg country_way at Zoom((1280,720),(0,0,1280,720),(659,186,621,349),0.0) with moveright
    show mary smile with dissolve:
        zoom 1.6 xalign 0.6 yalign -0.3
    mary"성함이 나보코프 씨였지?"
    extend" 정말 착하신분이네"
    edward"너무 부담 되지 않았으면 좋겠네……"
    show mary
    mary"아니, 난 정말 좋은 분이라고 생각해"
    show mary talk
    mary"근데 에드워드랑은 어떤 관계야?"
    edward"음……"
    edward"나의 은인 이라고 해야 할까……"
    edward"내가 옛날에 말 해줬는지 모르겠지만, 난 어렸을때 고아 였거든"
    edward"가족도 없고, 갈때도 없었던 날 받아주셨어"
    edward"물론 나한테 엄청나게 많은 일을 시키셔서 정말로 착한 사람이라고는 생각하지 않지만"
    mary"어렸을때……{cps=2} {/cps}그랬구나……"
    edward"지금은 성인이 돼고, 일자리를 잡아서 혼자서 살림 다 차렸으니까 이젠 아무런 상관 없지만"
    edward"그럼 당장 먹으로 갈까?"
    show mary smile
    mary"응"
    stop bgs
    scene black with movedown
    play sound "bgs/people.mp3"
    centered"중국집 음식점"
    play music "bgm/happy1.mp3"
    scene bg chinesefood_seat with movedown
    $ extra_name = '쟝 아저씨'
    extra"어서오세요"
    "아주머니의 말대로 식당 안엔 사람이 많았다."
    "근데 손님들에 비해서 점원의 수가 압도적으로 적었다."
    play sound "se/search_bag.mp3"
    scene bg chinesefood_seat at Zoom((1280,720),(0,0,1280,720),(442,289,455,256),0.0) with dissolve
    "일단 나랑 메리는 자리에 앉아서 메뉴판을 살폈다."
    show mary with dissolve:
        zoom 1.8 xalign 0.5 yalign -0.4
    mary"어떤게 좋을까?"
    edward"난 볶음밥이 좋을거 같네"
    show mary smile
    mary"그럼 나도 같은걸로 먹을래"
    edward"여기 주문 좀요!"
    $ extra_name = '어린 점원'
    extra"잠시만요!"
    play sound "se/footsteps_running.mp3"
    "16살 내외로 보이는 어린 남자아이가 주문을 받으러 왔다."
    stop sound
    extra"뭘로 하실건가요?"
    edward"볶음밥 2개로 주세요"
    play sound "se/chalk.mp3"
    extra"볶음밥 2개……"
    extra"사람이 많은 관계로 조금 기다리셔야되는데 괜찮죠?"
    edward"네"
    play sound "se/shock.ogg"
    show effect1
    $ extra_name = '쟝 아저씨'
    extra"{size=45}쑨! 저기도 주문 받아라!{/size}" with lshake
    $ extra_name = '어린 점원'
    extra"{size=45}알았어 아빠!!{/size}" with lshake
    hide effect1
    show mary shock2
    mary"가족이서 음식집을 하고 있는가보네……"
    edward"그래서 점원이 얼마 없었구나"
    play sound "se/move.mp3"
    stop music
    stop bgs
    scene black with moveleft
    $ renpy.pause(0.5)
    extra"볶음밥 2개 나왔습니다"
    "오랜 시간을 기다린 끝에 우리가 주문한 요리가 왔다."
    "둘 다 배가 고파서 쓰러지기 일보 직전의 사태까지 와서 그런지 요리를 보는 것 만으로도 그 맛이 전달되는거 같았다."
    "그릇이 식탁위에 놓이고……{cps=2} {/cps}나는 숟가락을 짚고, 음식을 먹으려는 찰나……"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(461,0,819,461),0.2) # 메리가 볶음밥을 우걱우걱 먹는 장면
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(461,0,819,461),0.2)
    play bgs "bgs/eating.mp3"
    "메리가 빛의 속도로 숟가락을 짚고, 볶음밥을 입에 넣기 시작했다!"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) # 메리가 볶음밥을 우걱우걱 먹는 장면
    show mary_eating 2 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0)
    mary"맛있어~"
    mary"맛의 비결이 뭘까~"
    play music "bgm/sirius6.mp3"
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0)
    "……라고 말을 마치고 다시 먹기 시작했다."
    mary"(우걱 우걱)"
    mary"이 맛……"
    extend" 도대체 뭣 때문이지?"
    mary"(쩝쩝)"
    mary"입에서 펼쳐지는 조금 짜면서도 적당히 매운 맛……"
    mary"그래, 조미료!"
    mary"밥의 식감과 조미료가 환상의 조합을 이루고 있어!"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(389,173,612,345),0.0) # 에드워드 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(389,173,612,345),0.0)
    edward"그, 그렇게 말을 하면서 먹을 필요가 있나?"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) # 메리 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0)
    mary"거기다 새우가 너무나도 잘 어울려……"
    edward"…………"
    mary"하지만 이게 전부가 아닌거 같아……"
    mary"쌀은 딱히 특별한게 없는거 같은데……"
    extend" 이 감칠맛은 뭐지?"
    mary"몸 전체를 멤도는 이 맛……"
    mary"혹시 계란 노른자?!"
    scene ev mary_eating at Zoom((1280,720),(711,12,467,263),(0,52,484,273),0.3) # 쟝 아저씨 시점
    show mary_eating 1 at Zoom((1280,720),(711,12,467,263),(0,52,484,273),0.3)
    $ extra_name = '쟝 아저씨'
    extra"훗, 소문대로 대단한 여자구나"
    "이곳의 주방장인, 쟝 아저씨가 옆에와서 메리에게 말 했다."
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(389,173,612,345),0.0) # 에드워드 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(389,173,612,345),0.0)
    edward"아, 아저씨……{cps=2} {/cps}딱히 어울려 주실 필요 없어요"
    scene ev mary_eating at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.3) # 쟝 아저씨 시점
    show mary_eating 1 at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.3)
    extra"아니!{cps=2} {/cps}내가 그냥 어울려 주는 게 아닐세"
    extra"저, 분석 능력……"
    extra"역시 구멍가게 할머니가 대단하다고 칭찬 할만 해"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) # 메리 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0)
    mary"구멍가게에서 제 말을 했어요?"
    scene ev mary_eating at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0) # 쟝 아저씨 시점
    show mary_eating 1 at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0)
    extra"이 좁은 시골에선 소문이 금방 퍼진다네"
    edward"…………"
    extra"하지만 그 분석 능력으로도 아직 내 볶음밥의 진짜 비밀은 알지 못했나보군……"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) # 메리 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0)
    mary"(우걱우걱)"
    mary"확실히 계란 노른자만 있는 건 아니야……"
    mary"조금 더 고소한 향기가 퍼지는 듯한 느낌도 들고……"
    extend" 무엇보다 전체적인 재료의 밸런스를 잡아주는 이것……"
    mary"특히 맛이 밥에서부터 우러나오는 게……{cps=2} {/cps}나중에 넣은 게 아니라 밥을 볶는 과정에서 넣은거야"
    play sound "se/heartbeat.mp3"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) # 메리 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) with flash
    mary"엇……"
    mary"혹시 볶을때 사용한 버터?!"
    mary"하지만 버터가 이렇게까지 맛있게 느껴졌었나?!"
    scene ev mary_eating at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0) # 쟝 아저씨 시점
    show mary_eating 1 at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0)
    extra"훗……"
    extra"역시 대단한 아가씨야"
    extra"아기씨의 말대로 이 볶음밥의 가장 큰 비밀은 바로 쌀을 볶을때 사용한 버터지!"
    extra"하지만 진짜 비결은 바로 내가 사용한 버터의 재료!"
    extra"……물론 그 버터의 재료는 비밀이지만"
    scene ev mary_eating at Zoom((1280,720),(0,52,484,273),(389,173,612,345),0.5) # 에드워드 시점
    show mary_eating 1 at Zoom((1280,720),(0,52,484,273),(389,173,612,345),0.5)
    $ renpy.pause(0.5)
    edward"어, 언제까지 이럴거야"
    scene ev mary_eating at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0) # 메리 시점
    show mary_eating 1 at Zoom((1280,720),(0,0,1280,720),(711,12,467,263),0.0)
    mary"정말 대단해요!"
    mary"조미료도, 주 식재료도 아닌 볶을때 사용한 버터에 진정한 비밀을 넣고……"
    scene ev mary_eating at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0) # 쟝 아저씨 시점
    show mary_eating 1 at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0)
    extra"아가씨야말로 정말 대단하네"
    extra"혹시 그쪽도 요리가 특기인가?"
    scene ev mary_eating at Zoom((1280,720),(0,52,484,273),(711,12,467,263),0.3) # 메리 시점
    show mary_eating 2 at Zoom((1280,720),(0,52,484,273),(711,12,467,263),0.3)
    mary"아뇨,{cps=2} {/cps}전 먹는것만 특기예요"
    mary"요리는 완전 못해요~"
    scene ev mary_eating at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0) # 쟝 아저씨 시점
    show mary_eating 1 at Zoom((1280,720),(389,173,612,345),(0,52,484,273),0.0)
    extra"그럼 여기에 자주 오게나"
    extra"아가씨의 입맛이라면 내 요리를 개선하는데 도움이 될거 같거든"
    scene ev mary_eating at Zoom((1280,720),(0,52,484,273),(389,173,612,345),0.5) # 에드워드 시점
    show mary_eating 1 at Zoom((1280,720),(0,52,484,273),(389,173,612,345),0.5)
    $ renpy.pause(0.5)
    edward"그, 그냥 먹으면 안될까……"
    stop bgs
    play music "bgm/beat2.mp3"
    scene ev mary_eating
    show mary_eating 2
    mary"후우~{cps=2} {/cps}잘 먹었다~"
    edward"어, 어;;"
    mary"어라?{cps=2} {/cps}에드워드는 한숟가락도 안 먹었네?"
    edward"그, 그냥 먹기가 힘들어져서……"
    mary"그럼 내가 대신 먹어줄게~"
    scene black with Dissolve(1.0)
    "나는 아쉽게도 음식을 전혀 먹지 못했다."
    "그래도 메리는 만족 한 거 같으니 나도 좋다."
    "메리의 컨디션도 좋아졌겠다. 이제 우리가 이스티아나로 온 진짜 이유─영업을 하러 출발할 수 있게 된 거 같다."
    stop music
    centered"34분 후……"
    centered"이스티아나의 어느 거리"
    play bgs"bgs/birds.mp3"
    scene bg country_way with moveup
    play music "bgm/smooth4.mp3"
    show mary smile with dissolve:
        zoom 1.6 xalign -2.0 yalign -0.3
        linear 2.0 xalign 0.7
    mary"우우우~{cps=2} {/cps}기분 좋다~♪"
    edward"많이 먹었으니까"
    "메리는 중화요리 다음엔 근처 포장마차에서 닭꼬치가 먹고 싶다면서 거기서도 먹었다."
    "그래도 나도 조금 먹은 덕분에 배가 부르다."
    edward"그럼 이제 장난감을 납품할 장소를 찾으러 가볼까?"
    show mary shock
    mary"아, 우리 그거 때문에 왔었지?"
    show mary think
    mary"근데 솔직히 말해서 나 하기 귀찮은데……"
    edward"그, 그럼 안 되지!"
    mary"이스티아나를 관광하는 게 더 재미있는 걸?"
    edward"일을 재미로 하는 건 아니잖아"
    show mary talk
    mary"난 재미로 하는데?"
    edward"…………"
    show effect2
    play sound "se/shock2.mp3"
    edward"메리가 날 안 도와주면 어떡하지……{cps=2} {/cps}난 혼자서 아무것도 못하는데……"
    edward"이대로 갔다간, 회사에서 분명 더 심한 왕따가 될거야……"
    edward"아니, 벌써부터 심한 왕따가 맞지만……"
    hide effect2
    show mary tsun
    mary"알았어─"
    mary"도와주면 되잖아─"
    mary"대신에 납품점 마킹 하고, 물건 다 팔면 이스티아나 관광하는 건 어때?"
    edward"그래"
    "어차피 난 약속한 800달러만 채울 수 있다면 아무런 문제 없다."
    "이걸로 회사에서 날 무시한 녀석들을……"
    scene black with Dissolve(1.0)
    stop bgs
    play music "bgm/beat3.mp3"
    show mary smile:
        zoom 1.3 xalign 0.5 yalign -0.2
    mary"안녕하세요~{cps=2} {/cps}저는 이런 사람 인데요……"
    play sound "se/move.mp3"
    hide mary smile with moveright
    show mary with dissolve:
        zoom 1.7 xalign 0.7 yalign -0.4
    mary"안녕하세요~!"
    play sound "se/move.mp3"
    hide mary with moveright
    show mary tease with dissolve:
        zoom 1.5 xalign 0.3 yalign -0.3
    mary"이걸 팔면 기존에 판매 하시던 다른 제품들도 동시에 광고가 될테니까 꿩먹고 알먹고, 일석이조잖아요?"
    play sound "se/move.mp3"
    hide mary tease with moveleft
    show mary shock2:
        zoom 1.3 xalign 0.0 yalign -0.2
    mary"저, 저는 이런 사람 이라고 합니다……"
    hide mary shock2 with dissolve
    "우린—주로 메리— 곳곳을 돌아다니면서 영업을 했다."
    "하지만 시골이다 보니까 물건을 팔 수 있을만한 장소가 별로 없어서 조금 예상 외의 고생을 하게 됐다."
    stop music
    play bgs "bgs/night.mp3"
    centered"오후 8시 40분"
    scene bg room_tatami with moveup
    show mary shock3:
        zoom 1.7 xalign 1.0 yalign -0.3
    show elsara talk:
        xalign 0.5 yalign 1.0
    elsara"둘이 이제 왔냐?"
    mary"하아……{cps=2} {/cps}하아……"
    elsara"밖에서 아주 재미있게 놀았는가봐?"
    mary"아뇨……{cps=2} {/cps}하루종일 일만 하다가 시간이 이렇게……"
    mary"관광은 하나도 못하고……!"
    edward"그래도 목표로 한 800달러는 채웠으니까 힘 내!"
    mary"일단 좀 쉬고 싶어……"
    play sound "se/footsteps_wood.mp3"
    hide mary shock3 with dissolve
    "메리는 지친듯이 몸을 끌면서 바닥에 드러누웠다."
    play sound "se/door_open.ogg"
    "얼마 후 갑자기 문이 열리면서 교복은 입은 여학생이 들어왔다."
    $ extra_name = '교복을 입은 여학생'
    extra"으─"
    extra"저, 학교 다녀왔습니다"
    show elsara with dissolve:
        zoom 1.5 xalign 0.2 yalign -0.3
    elsara"왔구나"
    extra"근데 어째 신발이 평상시보다 많은……"
    extra"오빠……?"
    play sound "se/shock.ogg"
    show effect1
    play music "bgm/happy3.mp3"
    hide elsara
    extra"{size=45}오빠!!{/size}" with lshake
    hide effect1
    edward"오빠 라고……?"
    "그 여자는 나를 오빠라고 불렀다."
    "이 집에 있으면서 날 오빠라고 부를 사람은……"
    edward"혹시 마린다?!"
    edward"몇 년 사이에 진짜 많이 컸구나!"
    "역시 아주머니의 딸인 마린다였다."
    "내가 마린다를 마지막으로 봤을땐, 이제 막 중학교에 입학 하기 시작한 꼬마였는데……"
    extra"설마 날 아직도 어린이 취급 하는거야?!"
    edward"설마!"
    edward"근데 네 학교는 어때?"
    extra"당연히 재미없지"
    extra"오빠야말로 회사는 어때?"
    edward"나도……{cps=2} {/cps}당연히 재미없어……"
    extra"풉"
    extra"어?{cps=2} {/cps}근데 저기 바닥에 누워있는 여자분은 누구신지……?"
    "마린다는 메리를 가리키며 말 했다."
    extra"호, 혹시 오빠의 여자친구거나 하진 않겠지?!"
    extra"아니면 같이 결혼 할 상대?!{cps=2} {/cps}여기 온것도 엄마한테 인사 시키려고?!"
    edward"그런거 전혀 아니야!"
    edward"그냥 내 회사 상사일 뿐이니까!"
    extra"후우~{cps=2} {/cps}순간 놀랬네"
    edward"왜?"
    extend" 내가 결혼하면 안 돼?"
    extra"그런건 아니고……"
    extra"그냥 오빠같은 사람을 남편으로 두면 골치아플거 같았을 뿐이야"
    edward"음……"
    edward"어쩌면 네 말이 맞을지도 모르겠네……"
    scene bg room_tatami at Zoom((1280,720),(0,0,1280,720),(381,244,648,364),0.3)
    $ renpy.pause(0.3)
    play sound "se/search_bag.mp3"
    show elsara talk:
        zoom 1.5 xalign -1.5 yalign -0.3
        linear 1.0 xalign 0.4
    show mary tired:
        zoom 1.5 xalign 0.7 yalign -0.3
    "나랑 마린다가 대화를 하던 중에, 아주머니가 메리에게 다가갔다."
    elsara"슈테른 씨, 잠깐 나 좀 따라올 수 있을까?"
    mary"저요……?"
    elsara"그래, 꼭 해야 할 말이 있어서……"
    edward"아주머니, 무슨 일 있어요?"
    show elsara mad
    elsara"나랑 슈테른 씨랑 단 둘이서 할 말이니까 넌 신경 꺼"
    elsara"마린다,{cps=2} {/cps}너 해야 할 숙제 있지 않았냐?"
    show elsara
    elsara"여기 돈 많이 버는 \'회사원\'씨 한테 도와달라고 해라"
    edward"저, 전 공부 잘 못하는데……!"
    extra"그럼 내가 가르쳐 줄게!"
    edward"그건 내 자존심이……"
    show elsara talk:
        linear 1.0 xalign -1.5
    show mary talk:
        linear 1.0 xalign -1.5
    "아주머니가 메리랑 단 둘이서 무슨 대화를 하려는 건진 잘 모르겠지만, 일단 같이 어디론가 이동하셨다."
    "딱히 내가 신경 쓸 일은 아니므로 무시했다."
    scene black with Dissolve(1.0)
    stop music
    stop bgs
    nvl clear
    narrator_nvl"1959년 11월 18일 수요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 너무 추움"
    nvl clear
    narrator_nvl"어제 기차 시간을 놓치는 바람에 잠을 아주머니 댁에서 자고, 아침 일찍이 첫 차로 몰턴으로 떠났다."
    narrator_nvl"근데 어제 아주머니랑 메리가 도대체 무슨 대화를 나눴던걸까?"
    narrator_nvl"그 날 이후로부터 메리의 상태가 조금……{cps=2} {/cps}달라졌다."
    narrator_nvl"하지만 구체적으로 어디가 어떻게 달라졌는진 말 하기 힘들었다."
    play bgs "bgs/birds.mp3"
    scene bg country_way with moveup
    show elsara:
        xalign 0.5 yalign 1.0
    show mary smile:
        zoom 1.7 xalign 0.7 yalign -0.3
    mary"안녕히계세요~"
    elsara"너희 둘, 몸 조심해서 가라!"
    edward"걱정하지 않으셔도 돼요"
    show elsara mad
    elsara"내가 너 때문에 걱정 하는거잖냐!"
    play sound "se/move.mp3"
    stop bgs
    scene black with moveright
    $ renpy.pause(0.5)
    centered"5시간 후……"
    play music "bgm/smooth2.mp3"
    play bgs "bgs/people.mp3"
    scene bg diary_trainstation with moveright
    centered"몰턴역"
    show mary shock2 with dissolve:
        zoom 1.7 xalign 0.6 yalign -0.3
    mary"원랜 어젯밤에 몰턴에 도착할 예정이었는데……{cps=2} {/cps}우리가 기차를 놓치는 바람에 회사에 지각 하게 됐는 걸"
    edward"놓쳤다기보단, 완전히 까먹고 있었지"
    mary"아주머니가 말씀을 밤 늦게까지 하시는 바람에 어쩔 수 없었는 걸"
    edward"근데 어제 둘이서 무슨 대화를 그렇게 까지 오랫동안 했어?"
    show mary shock
    mary"그건……"
    extend" 혹시 나중에 말 할 기회가 생긴다면 그때 해줄게"
    show mary smile
    mary"그래도 네가 걱정 할 건 아니니까……"
    stop music
    show mary shock3
    mary"……!"
    edward"어……?"
    "갑자기 귀신이라도 본 듯 메리의 표정이 굳었다."
    edward"왜그래?"
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(2.2)
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),1.0) with dissolve
    $ dad_name = '메리의 아버님'
    $ renpy.pause(1.0)
    show marydad mad with dissolve:
        xalign 0.8 yalign 1.0
    "메리의 시선을 따라가보니까, 어떤 정장을 입은 아저씨가 메리를 쳐다보고 있었다."
    "하지만 이 분이 누구시길래……"
    mary"아, 아빠……"
    scene bg diary_trainstation
    show mary shock3:
        zoom 1.7 xalign 0.6 yalign -0.3
    show effect1
    play music "bgm/sirius3.mp3"
    play sound "se/shock.ogg"
    edward"{size=45}아빠?!{/size}" with lshake
    hide effect1
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0.0)
    show marydad mad:
        zoom 1.7 xalign 0.8 yalign -0.3
    "저분이 바로 메리의 아버님 이신가?!"
    "처음 알았다."
    "과연 어떤 분이실까?{cps=2} {/cps}메리에 대해선 자주 들어봤지만, 아버님에 대해선 전혀 모른다."
    "일단 좋은 인상을 남기기 위해서 난 메리의 아버님께 인사를 드리려고 했다."
    edward"아, 안녕하세……"
    dad"메리, 이게 지금 무슨 일인지 설명 할 수 있을까?"
    "아버님은 나의 인사를 듣지도 못했다는 듯이 말 하셨다."
    scene bg diary_trainstation
    show mary shock3:
        zoom 1.7 xalign 0.6 yalign -0.3
    mary"…………"
    show mary shock with dissolve
    mary"출장으로 이스티아나에 갔다왔어……"
    mary"그런데 오는길에 작은 변수가 발생해서 막차를 놓치고……{cps=2} {/cps}어쩔 수 없이 아침 일찍이 첫차로 여기에……"
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0.0)
    show marydad mad:
        zoom 1.7 xalign 0.8 yalign -0.3
    show effect1
    play sound "se/shock.ogg"
    dad"{size=45}그래서 아비한텐 아무 말도 없이 외박을 했다는 게냐?!{/size}" with lshake
    dad"더군다나 결혼도 안 했으면서 남자랑 외박을 하다니!"
    "메리의 아버님은 나를 가리키며 윽박 지르셨다."
    scene bg diary_trainstation
    show mary mad:
        zoom 1.7 xalign 0.6 yalign -0.3
    mary"또 그런다!{cps=2} {/cps}내가 하고싶은 걸 하면 안 돼는거야?!"
    "메리도 뒤지지않는 언성으로 답 했다."
    mary"아빤 맨날 그렇게 날 가둬놓고, 이제 좀 그만해줬으면 좋겠어!"
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0.0)
    show marydad mad:
        zoom 1.7 xalign 0.8 yalign -0.3
    dad"이게 다 널 위한 거라고 말 했잖느냐?"
    dad"제발 네 아빠 고생시키는 일 좀 하지 말거라!"
    "둘의 대화가 점점 험악해지고, 분위기도 살벌해졌다."
    "주변의 시선도 조금 신경쓰이고 해서, 나는 둘을 어떻게든 막겠다며, 메리의 아버님에게 말 했다."
    edward"저, 저기……{cps=2} {/cps}우선 화를 좀 가라 앉히시는게……"
    dad"자네는 메리랑 무슨 사이길래 같이 출장을 간게냐?"
    dad"네가 메리를 꼬득여서 가자고 한게지?!"
    edward"확실히 저 때문에 가긴 했지만……"
    dad"네가……!"
    scene bg diary_trainstation
    show mary mad:
        zoom 1.7 xalign 0.6 yalign -0.3
    mary"그 사람은 만일의 사태를 대비해서 함께 동반하기로 한 \'보호자 대리인\'같은 사람이야"
    mary"그러니까 괜한 사람한테 화풀이 하지 마"
    mary"아빠도 내가 혼자 가는 것보단 누군가랑 같이 가는 게 더 안심일 것 아니야?"
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0.0)
    show marydad mad:
        zoom 1.7 xalign 0.8 yalign -0.3
    dad"…………"
    dad"네 몸을 생각해서라도 다음부턴 아무말 없이 멀리가진 말거라!"
    "어?"
    dad"그리고 다음부터 누군가랑 같이 멀리 갈 땐, 아빠도 아는 사람이랑 같이 가도록해!"
    dad"너도 어른이면 이런 건 내가 입 아프게 말 안 해도 알 거 아니냐?"
    scene bg diary_trainstation
    show mary mad:
        zoom 1.7 xalign 0.6 yalign -0.3
    mary"아빠는 내가 어엿한 어른으로 크기를 원한다면, 이제 나를 좀 놔줘"
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0.0)
    show marydad mad:
        zoom 1.7 xalign 0.8 yalign -0.3
    dad"네가 제대로된 어른으로 크지 못한다고 해도, 네가 건강하게 있을수만 있다면 상관없어!"
    scene bg diary_trainstation
    show mary mad:
        zoom 1.7 xalign 0.6 yalign -0.3
    mary"…………"
    mary"여기서 계속 의미없게 시간을 낭비할 순 없지"
    mary"가자, 에드"
    edward"…………"
    "메리의 아버님의 말씀이 조금 걸렸다."
    "지금 메리의 몸이 아픈 건가?"
    play sound "se/footsteps_concrete.mp3"
    scene black with Dissolve(1)
    stop bgs
    stop music
    $ renpy.pause(0.5)
    scene bg diary_park at Zoom((1280,720),(0,0,1280,720),(802,206,432,243),0.0) with movedown
    play bgs "bgs/wind.mp3"
    "출근을 위해서 급하게 회사를 향해서 걷고있던 중에, 나는 메리아버님의 말씀이 너무 걸려서 참을수가 없었다."
    "그래서 공원에서 잠깐 메리에게 물어보기로 했다."
    show mary shock with dissolve:
        zoom 1.6 xalign 0.7 yalign -0.4
    mary"…………"
    edward"마, 말하기 힘들 안 해도 괜찮아"
    edward"하지만, 나 때문에 몸에 무리가 가해진다면……"
    show mary shock2
    mary"그런건 아니야!"
    show mary think
    mary"그러니까……"
    show mary talk
    mary"내가 어렸을 때부터 몸이 많이 약했어"
    mary"그러다 내가 한번 크게 아픈적이 있었는데……"
    mary"아마 아빠는 나한테 또 그런일이 일어날까봐 두려워하는 걸꺼야"
    show mary shock2
    mary"사실 아빠가 저렇게 화를 내고, 나를 과대보호 하게 된 것도 전부 내 탓인데……"
    mary"그땐 내가 화내지 말아야 했어……"
    edward"그럼 지금이라도 아버지한테 가봐"
    edward"둘다 각자가 원하는 게 있으니까, 그걸 확실하게 말 한다면 이해해주실거라 생각해"
    show mary happy
    mary"넌 정말 착하고, 이해심이 깊은 사람이네"
    mary"그렇게 말 해줘서 고마워"
    show black:
        alpha 0.0
        linear 3.0
    "메리는 나를 착하고, 이해심이 깊은 사람이라고 말했다."
    "하지만 나에겐 메리같이 돈도, 명예도, 가족도 없다."
    "그러니─당연히 내가 메리를 이해했을 리가 없다."
    "난 그냥 메리랑 앞으로도 메리랑 같이 있고싶었다."
    "그녀는 한 회사의 사장이고, 돈이 많은 부자이고, 나를 싫어하지 않으니까"
    "메리 곁에 있으면 나에게 손해가 찾아오지 않을태고, 어쩌면 이익이 올지도 모르니까"
    play bgs "bgs/people.mp3"
    scene bg employee_office_day with movedown
    centered"노스탤지어 토이즈 사무실"
    "메리는 지금 쯤 아버지와 함께 대화를 나누고 있어서, 여기엔 없을거다."
    "……대신 나는 오늘 회사에 지각을 했다면서 상사에게 혼났다"
    "그리고 회사에서 내가 영업으로 800달러를 판매 했다는 사실을 알려도 큰 반응이 없었다."
    "근데 잘 생각해보니까─내가 많이 판다고 해도 결국엔 내가 소속돼 있는 부서의 판매 성과만 올리는 꼴이었잖아……"
    "메리가 말 한 \'프로젝트 코납작\'내가 사장이라도 되지 않는 한, 성공하기 힘들 것 같았다."
    stop music
    stop bgs
    play sound "se/book_page.ogg"
    scene bg lib_day with memory
    show stephan talk with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"이 날 이후론 며칠간 할머니에 대한 말이 전혀 없어……"
    stephan_think"그때까지 만나지 못했다는 뜻인가?"
    "나는 할머니에 대한 언급이 나오는 구간이 보일때 까지 계속 일기장의 페이지를 넘겼다."
    show stephan
    "그러다 몇 페이지 후에 할머니에 대한 언급이 나오는 구간을 찾았다."
    ################################1959년 11월 22일 일기장 시작############################
    play sound "se/case_start.mp3"
    scene black
    show text"{font=fonts/Type_Writer.ttf}{size=60}1959년 11월 22일{/size}{/font}" with memory:
        xalign 0.5 yalign 0.5
    $ renpy.pause(3.0)
    scene ev p_background with dissolve
    play music"bgm/Pathetique_Orgel.mp3"
    python:
        k = puzzle4()
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
            jump  diary19591122
label diary19591122:
    play sound "se/book_page.ogg"
    stop music
    scene black with memory
    nvl clear
    narrator_nvl"1959년 11월 22일 일요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 첫 눈이 옴"
    nvl clear
    narrator_nvl"오늘도 주말이다."
    narrator_nvl"나는 주말이 너무나도 싫다."
    narrator_nvl"취직하기 전엔 주말동안도 일을 했기 때문에 시간을 낭비한다는 생각이 전혀 없었는데……"
    narrator_nvl"근데 오늘은 집에서 꽤나 의외의 손님을 보게 됐다."
    play sound "se/door_knock.mp3"
    "누군가 문을 두드리는 게 들려오자, 나는 자리에서 일어나서 이동했다."
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(2.5)
    play sound "se/door_open.ogg"
    $ mary_cloth = 2
    play bgs "bgs/birds.mp3"
    play music "bgm/happy1.mp3"
    scene bg edward_house_day at Zoom((1280,720),(0,0,1280,720),(409,157,871,490),0.0) with flash
    show mary smile with dissolve:
        zoom 1.7 xalign 0.5 yalign -0.3
    mary"안녕, 에드"
    edward"사장님?"
    "사복 차림의 사장님이 서 있었다."
    show mary shock
    mary"밖에선 메리 라고─이름으로 부르기로 한거 벌써 잊었어?"
    "생각해보니까 옛날에 그런 일이 있었지"
    "며칠간 메리가 없는 일상에 너무 익숙해지는 바람에 오히려 있는 게 더 어색하게 느껴져 버렸다."
    edward"아, 아니!"
    edward"그런데 오늘 무슨 용건으로 왔는지……?"
    show mary
    mary"혹시 지금 시간 있어?"
    edward"있긴 한데……"
    show mary smile
    mary"그럼 나랑 같이 공원에 가자!"
    mary"오늘 꼭 하고싶은 말이 있거든……"
    edward"굳이 공원까지 가야 돼?"
    show mary shock2
    mary"맨날 집에만 틀여박혀 있으면 몸과 정신에 좋지 않잖아?"
    mary"그리고 내가 특별히 보여주고 싶은것도 있고……"
    "그 말을 듣자, 메리가 손에 쇼핑백을 지니고 있는 게 보였다."
    "혹시 나에게 주는 선물 같은건가?"
    edward"아, 알았어, 나갈게"
    play sound "se/search_bag.mp3"
    scene black with dissolve
    stop music
    "나는 집에 들어가서 외출복으로 갈아입었다."
    scene bg diary_park with moveright
    play bgs"bgs/kids.mp3"
    centered"공원"
    "메리가 나를 데려온 곳은, 우리동네에 있는 공원이었다."
    "주말이라 그런지─공원엔 어린아이들로 가득했다."
    show bg diary_park at Zoom((1280,720),(0,0,1280,720),(290,265,373,210),1.0) with dissolve
    $ renpy.pause(1.2)
    show mary with dissolve:
        zoom 1.5 xalign 0.6 yalign -0.3
    mary"저번에 에드가 나한테 해준 말 덕분에 아버지랑 어느정도 타협할 수 있게 됐어"
    show mary smile
    mary"고마워"
    edward"내가 그랬다고?"
    show mary shock
    mary"기억 안 나?"
    "처음엔 내가 정말 그랬는지 의아했지만, 곰곰히 생각해보니까 그럴수도 있었던 거 같았다."
    edward"아, 아니, 떠올랐어"
    edward"도움이 됐다니까 다행이야"
    show mary talk
    mary"그런데……"
    mary"넌 최근에 회사 일이 많이 힘들었지?"
    mary"주변에서 안 좋은 소리가 많이 들리더라고"
    edward"힘들다기보단……{cps=2} {/cps}진전이 없었다고 봐야겠지……"
    edward"옛날부터 계속 그랬으니까"
    mary"…………"
    "메리는 잠시동안 말을 멈추더니, 먼 곳을 바라보는 듯한 눈을 했다."
    "그리고 시선이 주변에서 뛰어놀고있는 어린아이들에게 향하면서 말 했다."
    mary"어렸을때……{cps=2} {/cps}다들 꿈 같은 게 있었잖아"
    edward"그랬겠지…… 아마"
    "나는 어렸을때부터 공장에서 돈벌로 나갔기 때문에 꿈이라는 걸 가질 여유는 없었다."
    "굳이 있다면, 어디서 돈을 벌었으면 좋겠다는 정도?"
    edward"근데 왜 갑자기 그런 말을……?"
    show mary
    mary"그거 알아?"
    mary"난 어렸을때 꿈이 엄청나게 많았어"
    mary"우리 엄마처럼 피아노 선생님이나, 현모양처가 돼보고 싶었고……"
    mary"내가 좋아하는 작가처럼 나도 소설 작가가 돼보고 싶었어……"
    play music "bgm/sad2.mp3"
    show mary talk
    mary"근데……"
    extend" 시간이 지나니까 그 많던 꿈이 전부 잊혀져버렸어"
    mary"내 꿈보단 지금 당장 먹고 사는 게 더 중요해졌고, 오직 안정적인 삶을 유지하는데만 전념하게 됐고……"
    edward"그건 나랑 똑같네"
    edward"나도 당장 먹고 사는데만 신경쓰고……{cps=2} {/cps}애초에 나한테 꿈같은 게 있었나 하는 심정 이니까"
    mary"아니"
    mary"넌 달라"
    show mary
    mary"어렸을때부터 장난감 회사에서 일 하는 게 꿈이었잖아?"
    edward"……!"
    edward"그걸……{cps=2} {/cps}어떻게……"
    edward"혹시 저번에 이스티아나에서 아주머니한테 들었어?!"
    show mary shock2
    mary"으, 응……"
    mary"맞아"
    "그랬군……"
    "그 날 아주머니랑 메리가 했던 대화가 내가 아주머니 집에서 얹혀 살면서 있었던 일 이었구나"
    "물론 꿈 이라기보단, 근거 없는 희망사항에 불과했지만"
    show mary
    mary"에드가 장난감 회사에 취직하기 위해서 계속 노력했다는 게 정말 의외였어"
    mary"거기다 막상 회사 내에서 사원들에게 왕따를 당하거나, 힘든 요구를 해와도 꾹 참고 회사를 다니고……"
    mary"일 하는 능력은 떨어져도, 무슨 일을 시키든 불만없이 하고"
    mary"그렇게 자기의 꿈을 위해서 열심히 하는 에드의 모습을 생각하니까 나 엄청나게 감동받았어"
    "생각해보니까 내가 정말 그렇다."
    "이유는 몰라도 난 예전부터 장난감 회사를 다니길 원했고, 지금도 그만두겠다는 생각 없이 꾸준히 일 하고있고……"
    "하지만 한가지 이해가 안 가는 게 있다."
    "만약 내 꿈이 정말로 장난감 회사에서 일을 하는거라면……"
    "지금은 그 꿈을 이뤘다는 뜻일텐데, 왜 나는 행복하지 않은걸까?"
    "허나, 나의 의문점에 대한 해답은 내가 처음부터 계속 알고 있었다."
    "\'돈이 없기 때문에\'"
    "그리고 나의 생각을 증명해주듯이 메리가 입을 열었다."
    mary"그래서 나도 에드를을 본받아서……"
    show mary smile
    mary"내가 잊고 있었던 꿈에 다시한번 도전해볼까 싶어!"
    mary"우선은 쉬워보이는 소설가 부터!"
    "역시……"
    "메리는 돈이 많다."
    "젊은 나이에 비교적 큰 기업의 사장이고, 똑똑하고……"
    "나같은 사람은 몇 번이고 계속 도전해야 겨우 그 꿈을 이룰 수 있고, 그리고 막상 이뤄도 큰 행복감을 느끼지 못한다."
    "하지만 돈과 시간을 가지고 있는 사람은 아무렇게나 도전할 수가 있다."
    "……옛날의 나는 그게 부조리하다고 생각 했지만, 일정한 수당과 안정된 생활을 확보한 지금에선 그것이 나쁘다고 생각하지 않는다."
    "오히려 돈이 있는 사람만이 꿈을 이룰수 있기 때문에 공평하다고 생각됐다."
    "과거에 내가 빈부격차를 욕하고, 돈 많은 사람들이 사치하는 걸 부조리하다고 생각 했던건 지금와서 보면 전부 피해의식에 불과했다."
    "역시 돈이 좋다."
    edward"정말 부러워……"
    show mary shock2
    mary"나야말로 네가 부러운 걸?"
    show mary talk
    mary"난 너처럼 대단하지가 못하니까……"
    edward"내 어디가 대단하다는 건지……"
    edward"난 돈 때문에 이렇게 목이 메여서 살고 있고……{cps=2} {/cps}네가 말 하기 전까진 나한테 꿈이 있었는지도 몰랐고……"
    edward"그리고 난 그 꿈을 이뤘을텐데도 행복하지 않고……"
    show mary talk
    mary"안 행복해?"
    edward"어"
    show mary
    stop music
    mary"나도 그래"
    edward"너도 행복하지 않다고……?"
    mary"응"
    edward"하, 하지만 넌 돈도 많고, 똑똑하고, 인기도 많고, 착하고, 예쁘고……"
    edward"모두가 원하는 걸 다 손에 넣었는데도 행복하지 않다고?"
    show mary happy
    play music "bgm/happy1.mp3"
    mary"저, 정말 내가 예쁘다고 생각해?"
    edward"…………"
    "나도 모르게 그런 말을 했다는 걸 알자, 얼굴이 확 달아올랐다."
    edward"그, 그건 그러니까……!"
    show mary smile
    mary"후후후……{cps=2} {/cps}잠깐 놀려본거야"
    show mary
    mary"네가 날 그렇게 까지 높게 평가하고 있었을 줄은 몰랐네"
    mary"근데 난 행복하지 않아……"
    show mary talk
    mary"왜냐면 난 가지고 싶은걸 한번도 가져보지 못했으니까"
    mary"아까도 말 했지만, 공부하는데만 집중하다보니까 내가 뭘 원하는지 생각 할 틈이 없었어"
    mary"애초에 내가 원하는 게 뭔지도 모른 상태인데 어떻게 행복을 알겠어?"
    show mary
    mary"그러니까 나도 네가 했던것 처럼……{cps=2} {/cps}내 꿈에 도전해보려고"
    mary"비록 나에겐 시간이 많지 않을지라도, 열심히 해보고 싶어"
    play sound "se/search_bag.mp3"
    show mary think:
        linear 0.3 yalign -0.6
    "메리는 들고온 쇼핑백에서 뭔가를 꺼냈다."
    show mary:
        linear 0.3 yalign -0.3
    show ev book with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.8
    mary"내가 지금 쓰고있는 소설이야"
    "붉은색의 하드 커버로 된 두꺼운 책 이었다."
    "표지엔 제목으로 추정되는 \'탐정의 서\'라는 글귀가 써 있었다."
    mary"아직, 많이 쓰진 못했지만, 꾸준히 노력해서 완성할꺼야"
    show mary smile
    mary"나도 내 꿈을 위해서 노력할거니까,{cps=2} {/cps}에드도 회사가 힘들다고 너무 좌절하지 말아줘"
    show mary happy with dissolve
    mary"넌 혼자가 아니야……{cps=2} {/cps}라고 말 해야 할까"
    "설마 메리가 오늘 날 데리고 온게 전부……{cps=2} {/cps}회사에서 있었던 일에 대해서 위로하기 위해서……?"
    "어쨌건 날 격려해주려는 마음이 너무 아름다워 보였다."
    "솔직히 조금……{cps=2} {/cps}감동 받았다."
    "왜냐면 난 지금까지 살면서 언제나 \'혼자\'라는 마음으로 가득했으니까"
    "뭔가 안 좋은 일이 생기거나, 힘든 고난이 닥쳐오면 항상 내 스스로가 해결해야 했다."
    "근데……{cps=2} {/cps}메리를 만나면서 내가 혼자가 아니라는 생각이 살짝 들기 시작했다."
    stop music
    "하지만 왜 메리는 나를 격려했을까?"
    "딱히 날 격려한다고 해서 돈이 나오는것도 아닐텐데"
    "그 이유가 궁금해진 나는 말 했다."
    edward"근데……{cps=2} {/cps}왜 나한테 그런 말을 해주는거야……?"
    show mary talk
    play sound "se/search_bag.mp3"
    show ev book:
        linear 0.8 xalign 0.7 yalign 0.9
    mary"응?"
    edward"무, 물론 나한테 그런 말을 해줘서 정말 고마워!"
    edward"그냥……"
    edward"어느날 갑자기 우리 집에 찾아오더니 공원에서 이런 말을 하는 게 이해가 안 가서……"
    show mary shock
    mary"그, 그건!"
    show mary shy
    play music "bgm/sad6.mp3"
    mary"예전부터 조금씩 들었던 건데……"
    mary"너한테서 내가 겹쳐보였거든……"
    edward"나랑?"
    extend" 어디가?"
    mary"나도 너처럼 회사에서 따돌림 당하고……"
    mary"이렇게─같이 대화를 나눌 사람도 너밖에 없고"
    edward"네가?!"
    mary"놀랍지?"
    show mary talk
    mary"근데 나한텐 이렇게 되는게 조금 당연하다고 생각해……"
    mary"우선 내가 노스탤지어 토이즈에서 사장 자리에 있을 수 있었던 건……{cps=2} {/cps}내 능력 때문이 아니야"
    mary"알고있었는진 모르겠지만…… 우리 아빠가 노스탤지어 토이즈의 회장이거든"
    edward"회, 회장?!"
    play sound "se/think.mp3"
    stop bgs
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0) with flash
    show marydad mad:
        xalign 0.8 yalign 1.0
    "그때 봰 사람이 바로 노스탤지어 토이즈의 회장……"
    "같은 회사라 하더라도, 일단 건물도 다르고, 무엇보다 나같이 낮은 사람이 회장님을 볼 일은 절대로 없다."
    "예상치도 못한 방법으로 회장님에게 내 첫 인상이 전달 될 줄이야……"
    play bgs"bgs/kids.mp3"
    scene bg diary_park at Zoom((1280,720),(0,0,1280,720),(290,265,373,210),0) with flash
    show mary talk:
        zoom 1.5 xalign 0.6 yalign -0.3
    show ev book:
        zoom 1.3 xalign 0.7 yalign 0.9
    mary"쉽게 말 해서─나도 낙하산 같은 거야"
    "내가 메리 덕분에 회사에 들어올 수 있었다면……{cps=2} {/cps}메리는 회장인 아버지 덕분 이었다는 건가"
    mary"그래도 난 명문대를 졸업했고, 실제로 지금의 노스탤지어 토이즈가 계속 수익을 내고 있는것도 대부분 내 힘이었으니까 사람들도 능력 자체는 인정 해줘"
    mary"하지만 가장 큰 문제는……"
    mary"내가 여자 라는 점이겠지……"
    mary"여자의 말에는 따를 수 없다는 사람까지 나올 정도로 회사에서 나의 위치는 엉망이야"
    show mary shock2
    mary"사람들한테서 집안 일이나 해라 같이 온갓 욕을 다 들었다니까……"
    edward"많이 쓸쓸했겠네……"
    show mary
    mary"그래도 네가 있어서 난 괜찮아"
    "내가 있어서……"
    "그럼 메리가 나를 회사에 취직 시켜준것도……{cps=2} {/cps}전부 자기를 위로하기 위해서 였던걸까?"
    "하지만 나도 그 과정에서 많은 이익을 봤으니, 서로 윈-윈 개념으로 아무런 문제가 없다."
    "아니, 내가 메리한테서 받은걸 생각해보면 아직 윈-윈은 아니다."
    "난 아직 메리를 위해서 뭔가를 해주지 못했으니까"
    "하지만 고작 내가 메리를 위해서 무엇을 해줄 수 있겠는가……"
    "나 자신도 제대로 도울 수 없는데……"
    "그때 내 머릿속에서 떠오른 건─지금 메리가 쓰고있다는 소설이었다."
    "그거라면 내가 제대로 도움이 될 수도있다고 생각했다."
    edward"그 쓰고있는 소설 책 말이야……"
    play sound "se/search_bag.mp3"
    show mary talk
    show ev book:
        linear 0.4 xalign 0.5 yalign 0.8
    mary"이거?"
    edward"응"
    edward"필요하다면, 내가 읽어줄게"
    show mary shy2
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}이, 읽는다고?!{/size}" with lshake
    hide effect1
    show mary shy
    mary"그건 너무 부끄러운데……"
    edward"그래도 누군가 읽어줘야 소설쓰는데 도움이 될꺼 아니야"
    mary"그, 그럼 주제만이라도……"
    edward"좋아"
    mary"이건 그러니까……"
    mary"어렸을때 탐정이 되고 싶었던 할아버지가 늙으면서 자신의 꿈을 이룰 수 없게 되자, 같은 꿈을 가진 손자에게 자기가 한때 쓴 탐정의 비법책……"
    mary"\'탐정의 서\'를 물려주면서, 손자가 여러 탐정짓을 하는 이야기야"
    stop bgs
    scene bg lib_day with memory
    show stephan talk with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"탐정의 서……"
    stephan_think"지금은 정체모를 철학책이……{cps=2} {/cps}한땐 제목에 걸맞는 소설이었다니……"
    stephan_think"무슨 일이 있었길래 지금의 내용으로 바뀌었던걸까……"
    "그보다 탐정의 서의 원래 내용도 조금 거슬렸다."
    "할아버지가 탐정이 되고 싶어하는 손자에게 책을 물려준다……"
    "……혹시 5년 전에 할아버지가 나에게 그 책을 준것도, 이거랑 관련이 있었던걸까?"
    "나는 다음 내용을 기대하면서 일기를 계속 읽었다."
    play sound "se/book_page.ogg"
    scene bg diary_park at Zoom((1280,720),(0,0,1280,720),(290,265,373,210),0) with memory
    play bgs "bgs/kids.mp3"
    show mary shy:
        zoom 1.5 xalign 0.6 yalign -0.3
    show ev book:
        zoom 1.3 xalign 0.7 yalign 0.9
    mary"어때……?"
    edward"내 평이 어느정도 도움이 될진 모르지만……"
    edward"들어봤을땐 왠지 재미있을거 같아"
    show mary
    mary"정말?!"
    mary"그럼 열심히 써야겠네!"
    edward"혹시……"
    edward"혹시 내가 도와줄 수 있는 게 있다면 말 해줘……"
    show mary talk
    mary"……?"
    edward"무, 물론 너도 이스티아나 때 처럼 날 도와줄 경우에만!"
    edward"너 덕분에 내 꿈을 이룰 수 있었으니까……"
    edward"앞으로도 내 꿈을 도와주면, 나도 네 꿈을 도와줄게……"
    "내가 그때 왜 그런 말을 했는지……{cps=2} {/cps}지금와서 생각해보면 꽤나 부끄러웠다."
    "하지만 딱히 손해가 있었던것도 아니니까……"
    show mary happy
    mary"고마워,{cps=2} {/cps}에드"
    "메리의 그 대답이 나를 살짝 웃게 만들었다."
    "이런식으로 자연스럽게 미소가 나오는 게 과연 얼마 만이었을까……"
    play sound "se/search_bag.mp3"
    scene ev sky_cloudy with moveup
    "나는 하늘을 올려다봤다."
    scene black with eyeshut
    "그리고 가만히 생각에 잠겼다."
    "난 주말이 정말 싫다."
    "주말은 시간이 많이 낭비 되기 때문에"
    "내가 지금 여기서 메리랑 대화를 하고 있다고 해서 얻는 게 있는 건 아니다."
    "아니, 오히려 시간이라고 하는 가장 소중한 자원을 계속 잃어간다."
    "이 시간동안 내가 일을 했다면 과연 얼마를 벌 수 있었을까 하는 생각을 자주 했다."
    "하지만……"
    extend" 그게 싫지 않다."
    "오늘은 좋은 시간낭비였다."
    stop music
    edward"……?"
    "그때 내 얼굴에 뭔가 차가운게 떨어졌다."
    "깜짝 놀라서 눈을 떴는데……"
    scene ev sky_snow with eyeopen
    play music "bgm/happy4.mp3"
    "하늘에서 눈이 내렸다!"
    scene bg diary_park at Zoom((1280,720),(0,0,1280,720),(290,265,373,210),0) with movedown
    show mary talk:
        zoom 1.5 xalign 0.6 yalign -0.3
    edward"지, 지금 눈이 오는거 같은데……{cps=2} {/cps}이제 슬슬 헤어질까?"
    show snow
    mary"정말이네?"
    mary"…………"
    show effect1
    show mary shock3
    play sound "se/shock.ogg"
    mary"{size=45}잠깐, 눈?!{/size}" with lshake
    mary"이거 어쩌지……{cps=2} {/cps}나 완전히 까먹고 있었어!"
    mary"오늘 일기예보에서도 첫 눈이 내릴거라고 했는데……"
    hide effect1
    edward"혹시 빨래 널고 그냥 왔어?"
    edward"그럼 빨리 가보는 게……"
    mary"아니!"
    extend" 가지 마!"
    edward"……?"
    show mary shy with dissolve
    mary"그, 그러니까……"
    mary"네가 아까 내 꿈을 이뤄준다고 했지?"
    edward"이뤄준다기보단, 도와준다고 해야겠지……"
    mary"어쨌건……{cps=2} {/cps}나한테 한가지 꿈이 있는데……"
    mary"이걸 이뤄주는데 날 도와줄 수 있는 건 에드 밖에 없어!"
    edward"어떤건데?"
    show effect1
    play sound "se/shock.ogg"
    show mary shy2
    mary"{size=45}연애가 해보고 싶어!{/size}" with lshake
    edward"{size=45}어어?!{/size}"
    hide effect1
    show mary shy
    mary"그그그, 그러니까 내 꿈 중에서 한번 쯤 연애를 해보고 싶다는 게……!"
    mary"쉽게 말해서……"
    mary"나랑……"
    mary"사귀어줘……"
    play sound "se/heartbeat.mp3"
    edward"……!"
    "나는 엄청나게 당황했다."
    "설마 오늘 날 여기로 데리고 온 궁극적인 목적이 바로 고백 하려고?"
    "그럼 난 메리의 제안을 승락 해야 하는가?!"
    "그보다 내가 아까전까지 했던 말들을 생각해보면……{cps=2} {/cps}과연 선택권 같은 게 있을까……"
    "머릿속으론 뭐라 대답 해야 하는지 알고 있었지만, 입이 내 마음처럼 떨어지지 않았다."
    "나는 한동안 물고기처럼 입만 뻐금거렸다."
    "그리고……"
    "마침내 내 입이 떨어졌다."
    edward"그, 그래……"
    show mary happy with dissolve
    mary"에드워드……"
    play music "bgm/smooth6.mp3" fadeout 0.7
    play sound "se/heartbeat.mp3"
    scene ev edward_hug at Zoom((1280,720),(597,303,266,150),(0,0,1280,720),0.4) with dissolve
    edward"윽……!"
    "그때 메리는 갑자기 나에게 포옹을 했다."
    "눈 때문에 식었던 내 몸을 따뜻하게 데워주는 것 같아서 싫진 않았다."
    "여기선 나도 메리를 안아야 하나?{cps=2} {/cps}아니면 이대로 있어야 하나……"
    "그래서 조금 애매하지만, 살짝 중립적인 자세로 메리의 포옹을 받아들였다."
    "그리고……{cps=2} {/cps}그녀의 따뜻함으로 눈 때문에 식어버린 나의 몸을 녹였다."
    scene ev edward_hug at Zoom((1280,720),(333,69,803,451),(465,75,587,331),0.0)
    mary"첫 눈이 내리는 날에 고백하면……{cps=2} {/cps}이루어진다는데……"
    mary"사실이라서 다행이다"
    "그래서 굳이 오늘로 찾아 온건가……"
    stop bgs
    scene bg lib_day with memory
    show stephan mad with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"…………"
    stephan_think"할머니랑 할아버지가 서로 사랑 했다는 건 알고 있었지만……"
    stephan_think"그래도……"
    stephan"리얼충……{cps=2} {/cps}폭발해라……"
    play sound "se/book_page.ogg"
    stop music
    scene black with memory
    play music "bgm/smooth4.mp3"
    nvl clear
    narrator_nvl"1959년 11월 25일 수요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 쌓임"
    nvl clear
    narrator_nvl"메리랑 사귄지 며칠이 됐을까……"
    narrator_nvl"하지만 아무리 시간이 지나도 나는 연애가 뭔지 전혀 모르겠다."
    narrator_nvl"그래도 메리가 딱히 어려운 요구를 하는것은 아니기에 정말 다행이다."
    narrator_nvl"거기다 메리 본인도 연애 경험이 전혀 없다고 하니까 나에게 부담감은 매우 적다."
    narrator_nvl"대신 우리가 하는 \'연애\'라는 건, 같이 밥먹고, 같이 퇴근하고, 가끔 같이 산책을 하는 게 고작이었다."
    narrator_nvl"하지만 오늘은 메리가 조금 다른 데이트 코스를 소개 시켜줬다."
    centered"오전 11시 40분"
    centered"노스탤지어 토이즈 사내 화단"
    scene bg employee_garden with movedown
    $ mary_cloth = 1
    show mary with dissolve:
        zoom 1.4 xalign 0.6 yalign -0.2
    mary"역시 여긴 언제나 조용해"
    play sound "se/search_bag.mp3"
    scene bg employee_garden at Zoom((1280,720),(0,0,1280,720),(289,112,868,489),0.0) with dissolve
    "나랑 메리는 밖에서 도시락을 사와, 회사 화단에서 같이 먹기로 했다."
    show mary with dissolve:
        zoom 1.7 yalign 1.0 xalign 0.6
        linear 0.6 yalign -0.5
    mary"내가 오늘 지인으로부터 유명한 피아니스트의 연주회 표를 받았는데, 같이 보러 갈래?"
    edward"피아노라……"
    mary"내가 알기로, 에드워드는 피아노를 좋아한다면서?"
    edward"좋긴 하지만, 그런덴 한번도 가본적이 없는데……{cps=2} {/cps}내가 잘 할 수 있을까……"
    show mary shock
    mary"잘 한다니……"
    extend" 그냥 앉아서 음악 감상만 하면 되잖아?"
    edward"그, 그런거야?"
    edward"정말 그거면 되는거야?"
    mary"당연하지……"
    mary"뭘 해야된다고 생각 했는데?"
    edward"그냥 그런덴 식사 예절같이 뭔가 규칙 같은 게 있지 않을까 생각했는데……"
    show mary smile
    mary"참 엉뚱하긴"
    show mary
    mary"거기서 지켜야 할 규칙은 조용히 있는거랑 즐기는거 뿐이야"
    edward"그렇다면 한번 가보고싶네"
    show mary smile
    mary"그럼 퇴근 후에 바로 가자"
    stop music
    play sound "se/move.mp3"
    scene black with moveright
    centered"오후 7시 10분"
    centered"몰턴 극장"
    play bgs "bgs/people.mp3"
    scene bg diary_stage with moveright
    "꽤나 이름있는 사람이 공연을 하는 것인지, 사람들이 엄청나게 많았다."
    "우리도 겨우 들어올 수 있었을 정도였다."
    show bg diary_stage at Zoom((1280,720),(0,0,1280,720),(591,180,426,240),0.3) with dissolve
    show mary:
        zoom 1.5 xalign 0.1 yalign -0.4
    mary"오늘은 \'블라디미르 호로비츠(Vladimir Horowitz)\'라는 사람이 연주를 한다네"
    mary"나는 누군지 몰랐는데, 꽤 유명한 천재 피아니스트래!"
    edward"많이 기뻐보이네"
    show mary smile
    mary"어렸을때부터 꼭 와보고 싶었거든!"
    show mary
    mary"옛날에 엄마가 같이 데려가 주겠다고 했었는데……"
    edward"결국엔 못 갔어?"
    show mary talk
    mary"그런거지……"
    stop bgs
    play sound "se/footsteps_wood.mp3"
    show mary
    mary"어!{cps=2} {/cps}이제 연주 시작 한다!"
    mary"조용히 하고 듣자"
    scene bg diary_stage at Zoom((1280,720),(591,180,426,240),(0,0,1280,720),0.5) with Dissolve(1.0)
    $ renpy.pause(1.0)
    play music "bgm/Appassionata.mp3" fadein 0.3 fadeout 1.0
    "관객들이 순식간에 조용해지면서 무대 위에 피아니스트는 연주를 시작했다."
    "내가 기억하기로, 그때 들었던 곡은 베토벤의 \'열정(Appassionata)\' 이라고 했던것 같았다."
    "확실히 내가 피아노 곡을 좋아하긴 하지만……{cps=2} {/cps}이렇게 가만히 앉아서 듣기만 하는 건 좀 불편했다."
    show bg diary_stage at Zoom((1280,720),(0,0,1280,720),(591,180,426,240),0.0) with dissolve
    show mary happy with dissolve:
        zoom 1.5 xalign 0.1 yalign -0.4
    "하지만 메리는 나와는 정 반대로 이 상황이 정말 기쁜 듯 했다."
    "마치 어린 여자애 처럼 기뻐하는 저 표정……"
    "그 표정을 보니까, 내가 여기에 따라온 보람이 있었다는 게 느껴졌다."
    scene black with Dissolve(1.0)
    $ renpy.pause(0.5)
    stop music
    centered"오후 8시 2분"
    play bgs "bgs/wind.mp3"
    play music "bgm/smooth5.mp3"
    scene bg diary_park_snow_night at Zoom((1280,720),(0,0,1280,720),(688,193,592,334),0.0) with moveleft
    show snow
    show mary smile with dissolve:
        zoom 1.7 xalign 0.5 yalign -0.3
    mary"오늘 정말 재밌었지?"
    edward"으, 응……"
    "메리의 기뻐하는 모습 덕분에 보람은 있었지만, 연주회 자체는 나에겐 재밌지 않았다."
    "아무래도 내가 교양이랑은 잘 안 어울리는 족속인가보다."
    show mary
    mary"혹시 너 피아노 칠 줄 알아?"
    edward"내가?"
    mary"응"
    mary"어렸을때 어디선가 배웠다든가……"
    edward"어디서 배웠는지는 잘 모르겠지만─나도 피아노는 칠 줄 알아"
    edward"……아주 조금"
    "사실 한 곡밖에 칠 줄 모른다."
    show mary tease
    mary"자랑은 아니지만─나도 피아노 칠 줄 안다"
    mary"그것도 아주 잘~"
    show effect2
    play sound"se/shock2.mp3" 
    edward"너는 뭐든지 잘 하는구나……"
    show mary shock2
    mary"그렇게 기운빠지게 말하면 어떻게……"
    hide effect2
    edward"미안!"
    edward"내가 딴생각을 조금 했나봐"
    show mary think
    mary"으음……"
    show mary tease
    mary"내가 언젠간 내 피아노 실력을 보여줄테니까, 그땐 너도 보여줘"
    mary"오늘 본 연주회같이 말이야!"
    edward"그건 좀 쪽팔리는데……"
    show mary
    mary"물론 사람은 부르지 않고……{cps=2} {/cps}장소만 따로 구해서 둘이서만 하자고"
    edward"난 그런거 별로 하고싶지 않은데……"
    show mary talk
    mary"그래?"
    mary"서로를 위해서 피아노 치는 거─왠지 연인같고, 로맨틱해서 좋지 않아?"
    edward"아, 알았어……"
    "메리의 \'로맨틱\'과 \'연인\'의 이미지는 드라마와 소설에 가까웠다는 사실을 알 수 있었다."
    show mary shock2
    mary"에드, 미안하지만 난 이만 가봐야 될 거 같아"
    mary"또 늦게 돌아오면 아빠가 뭐라고 할테니까……"
    edward"그래……{cps=2} {/cps}조심해서 들어가"
    show mary
    mary"내일 회사에서 보자"
    play sound "se/footsteps_running_snow.mp3"
    show mary talk:
        linear 0.6 xalign 2.0
    $ renpy.pause(0.7)
    hide mary talk
    "메리는 빠른 걸음으로 내 시야에서 사라졌다."
    edward"…………"
    play sound "se/search_bag.mp3"
    show bg diary_park_snow_night at Zoom((1280,720),(0,0,1280,720),(310,250,391,220),0.0) with Dissolve(1.0)
    "나는 공원 벤치에 앉아서 잠시동안 생각에 잠겼다."
    stop music
    scene black with eyeshut
    "……과연 나는 계속 메리의 연인으로 있어도 괜찮은걸까?"
    stop bgs
    nvl clear
    narrator_nvl"1959년 11월 26일 목요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 내림"
    nvl clear
    narrator_nvl"나와 메리는 정말 다르다."
    narrator_nvl"이 사실은 처음 만났을때부터 계속 알고 있었던 사실이었다."
    narrator_nvl"그런 전혀 다른 우리 둘이 어째서 지금 연인 사이가 됐는지, 참으로 신기하다."
    narrator_nvl"근데 잘 생각해보면 말만 연인 사이고, 실제론 연인 같은 행동은 거의 없다."
    narrator_nvl"그럼 나는 왜 이러고 있는 걸까?"
    narrator_nvl"메리와 계속 이런 사이를 유지해도 괜찮은걸까?"
    play bgs "bgs/people.mp3"
    play music "bgm/smooth4.mp3"
    scene bg employee_office_day with moveup
    show mary talk:
        xalign 0.8 yalign 1.0
    mary"이 제품의 CM을 만들땐 최대한 화려한 색상을 사용하도록 하세요"
    mary"그리고 캐릭터가 움직이는 장면은 만화 대신에 실제 제품을 \'스톱 모션(Stop Motion)\'으로 찍는 게 더 좋겠군요"
    $ extra_name = '사원'
    extra"알겠습니다"
    "메리는 정말 일을 잘 한다."
    "그녀는 회장인 아버지의 덕으로 왔다고 말 했지만, 그 능력 만큼은 진실이다."
    scene bg employee_office_day at Zoom((1280,720),(0,0,1280,720),(327,368,625,352),0.3)
    $ extra_name = '막스 부장'
    extra"이봐, 토머"
    extra"지금 한눈 팔고있지?"
    edward"아, 아닙니다!"
    extra"내가 부탁한 설문조사 자료 정리는 끝냈어?"
    edward"아뇨……"
    extra"왜 이거 하나 제대로 못 끝내는거야?!"
    edward"죄, 죄송합니다!"
    "……나는 이 모양인데"
    "그래도 내 능력이 부족해서 받는 대우니까 가끔 짜증은 나도, 화가 나진 않는다."
    stop bgs
    scene black with moveright
    centered"점심 시간"
    play bgs "bgs/people.mp3"
    scene bg employee_lounge at Zoom((1280,720),(0,0,1280,720),(646,191,634,357),0.0) with moveright
    "나는 혼자 앉아서 간단한 식사를 했다."
    "다른 사람들은 전부다 누군가와 같이 앉아서 대화를 하고 있지만,{cps=2} {/cps}난 혼자서……"
    play sound "se/footsteps_concrete.mp3"
    show mary:
        zoom 1.6 xalign -1.0 yalign 1.0
        linear 2.0 xalign 0.2
    $ renpy.pause(2.0)
    "그때 메리가 나에게 다가왔다."
    play sound "se/search_bag.mp3"
    show mary:
        linear 0.4 yalign -0.4
    mary"토머 씨, 합석해도 될까요?"
    edward"네……"
    dad"메리야~!"
    show mary talk
    mary"……?"
    scene bg employee_lounge at Zoom((1280,720),(646,191,634,357),(0,0,1280,720),0.5) with dissolve
    $ renpy.pause(0.5)
    show marydad:
        xalign 0.2 yalign 1.0
    dad"오늘 아비랑 같이 식사라도 하지 않겠는가?"
    show mary shock2 with dissolve:
        xalign 0.8 yalign -0.5
        linear 0.4 yalign 1.0
    mary"지, 지금?"
    dad"그래,{cps=2} {/cps}어차피 점심만 먹고 돌아올거니까 일은 걱정하지 마렴"
    show mary shock
    mary"…………"
    show marydad talk
    dad"요즘 이 추운 날씨에도 늦게 들어오고, 계속 걱정만 끼치잖니"
    dad"아빠랑 같이 식사 하자는 게 힘든 요구도 아니고"
    show mary shock2
    mary"아, 알았어"
    mary"금방 갈게"
    scene bg employee_lounge at Zoom((1280,720),(0,0,1280,720),(646,191,634,357),0.0) with dissolve
    show mary shock with dissolve:
        zoom 1.6 xalign 0.2 yalign -0.4
    mary"미안……"
    play sound "se/footsteps_concrete.mp3"
    hide mary shock with dissolve
    "지금까지 내가 봤을때, 메리의 아버지는 항상 메리를 곁에 두시려고 하는 것 같았다."
    "물론 부녀지간에 그런건 매우 자연스럽지만……"
    "메리의 나이를 생각해보면 아버지의 행동이 조금 과할지도……"
    stop music
    stop bgs
    scene black with dissolve
    nvl clear
    narrator_nvl"1959년 11월 28일 토요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 잠깐 그침"
    nvl clear
    narrator_nvl"최근들어서 나랑 메리가 계속 사귀어도 괜찮은건지 의문이 들었다."
    narrator_nvl"그보다 우리가 지금 하고 있는 게 \'연애\'가 맞는지도 모르겠다."
    narrator_nvl"애초에 연애가 뭐지?"
    narrator_nvl"왜 나는 이렇게 마음속으로 고민하고 있을까?"
    narrator_nvl"메리와 사귀기 전엔 이런 잡생각없이 내 인생이 잘 돌아갔을텐데……"
    centered"오후 6시 20분"
    play bgs "bgs/wind.mp3"
    play music "bgm/sad2.mp3"
    scene bg edward_house_night at Zoom((1280,720),(0,0,1280,720),(716,228,564,317),0.0) with moveup
    "오늘은 주말이라서 시간이 많이 남아, 메리와 같이 영화관에서 영화를 봤다."
    "내용은 별로 기억에 남지 않았지만, 같이 먹은 카라멜 팝콘은 맛있었다."
    edward"어후─"
    "짧은 한숨을 내면서 집에 들어갈려는 찰나……"
    "우편함에 편지가 온게 보였다."
    play sound "se/book_page.ogg"
    "아주머니에게서 온 편지였다."
    "…………"
    "아주머니……"
    "혹시 지금 내가 느끼고 있는 감정에 대한 해답을 아주머니는 가지고 있지 않을까?"
    "그래서 나는 아주머니께 전화를 드려보기로 했다."
    scene bg edward_house_night at Zoom((1280,720),(716,228,564,317),(309,205,628,353),0.4)
    $ renpy.pause(0.5)
    play sound "se/door_knock.mp3"
    edward"할아버지!{cps=2} {/cps}저 전화좀 빌릴게요!"
    "안에 아무런 반응이 없었다."
    "그냥 내일 아침에 전화할까 싶었지만, 난 분명 까먹을테니 불편하더라도 공원 옆에 있는 공중전화로 걸기로 했다."
    scene black with moveright
    $ renpy.pause(0.5)
    play sound "se/phone_calling.mp3"
    scene bg diary_park_snow_night at Zoom((1280,720),(0,0,1280,720),(113,27,548,308),0.0) with moveright
    stop sound
    elsara"여보세요?"
    edward"아주머니?{cps=2} {/cps}저 에드워드예요"
    elsara"왠일이냐, 나한테 전화를 다 하고……"
    edward"그게……"
    edward"제가 최근에 어떤 여자하고 연애를 하고 있는데……"
    show effect1
    play sound "se/shock.ogg"
    elsara"{size=45}어어?!{/size}" with lshake
    elsara"네가?!"
    hide effect1
    elsara"혹시 그 슈테른 처자랑 사귀고 있는 게냐?"
    edward"그, 그걸 어떻게 아셨어요?"
    elsara"후우~{cps=2} {/cps}역시나"
    elsara"네가 그 애 이외엔 같이 있지 않을거라 생각 했거든"
    elsara"그래서 나한테 묻고 싶은 게 뭐니?"
    edward"연애가 뭘까요?"
    elsara"……너 술마셨냐?"
    edward"전 진지하단 말이에요!"
    elsara"흐음……"
    elsara"쉽게 말해서……{cps=2} {/cps}남녀간의 사랑이지"
    elsara"다만 단순히 사랑이 아니라, 서로가 서로를 위해주는 것"
    elsara"그게 연애이자 연인관계가 가져야 할 마음 가짐 이란다"
    elsara"……이, 이렇게 말하니까 조금 낯 간지럽네"
    "사랑하는 사이가 서로를 위해주는 것……"
    "그럼 나랑 메리는 서로를 사랑 하는가?"
    "사랑이 뭔지 명확하게 말은 못하겠지만, 적어도 서로를 사랑한다고 부를 수 있는 사이 라는 건 알 것 같았다."
    "허나……"
    play sound "se/think.mp3"
    play bgs "bgs/kids.mp3"
    scene bg diary_park at Zoom((1280,720),(0,0,1280,720),(290,265,373,210),0) with flash
    show snow
    show mary shy2:
        zoom 1.5 xalign 0.6 yalign -0.3
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}연애가 해보고 싶어!{/size}" with lshake
    play bgs "bgs/wind.mp3"
    scene bg diary_park_snow_night at Zoom((1280,720),(0,0,1280,720),(113,27,548,308),0.0) with flash
    "나랑 메리는 \'연애\'라는 걸 하면서 단 한번도 서로를 사랑한다고 한적이 없었다."
    "즉, 나와 메리의 관계는 연인이 아니라는거다."
    "하지만 생각해보면 이게 맞는 말이다."
    "나와 메리는 서로의 꿈을 이루기 위해서 하는 협력관계니까"
    "메리 본인도 꿈 중에서 연애를 해보고 싶었는 게 있었기에 나에게 물었던거고……"
    play sound "se/think.mp3"
    stop bgs
    show bg diary_stage at Zoom((1280,720),(0,0,1280,720),(591,180,426,240),0.0) with flash
    show mary happy with dissolve:
        zoom 1.5 xalign 0.1 yalign -0.4
    "……무엇보다 메리는 나와 같이 있어서 행복해 보였기 때문에 나로썬 족하다."
    "나는 그녀의 꿈을 이루는 걸 도와줬으니까"
    play bgs "bgs/wind.mp3"
    scene bg diary_park_snow_night at Zoom((1280,720),(0,0,1280,720),(113,27,548,308),0.0) with flash
    elsara"넌 이해력이 딸리니까, 그냥 여자가 원하는대로 해주기만 하면 되는거라고 생각 해라"
    elsara"또, 여자는 \'사랑\'과 \'낭만\'을 좋아하니까, 괜히 너 좋은대로 하려고 하지도 말고"
    elsara"분위기를 잘 맞춰"
    edward"덕분에 조금은 알 것 같아요.{cps=2} {/cps}고맙습니다. 아주머니"
    elsara"난 별로 말 해준게 없는 걸"
    elsara"암튼, 도움이 됐다니까 다행이구나"
    scene black with Dissolve(1.0)
    stop bgs
    "서로의 목적을 이루기 위한 협력관계……"
    "생산성이 없는 연인사이보단 이쪽이 압도적으로 좋다고 생각했다."
    stop music
    play sound "se/book_page.ogg"
    scene black with moveright
    play sound "se/case_start.mp3"
    show text"{font=fonts/Type_Writer.ttf}{size=60}1959년 12월 20일{/size}{/font}" with memory:
        xalign 0.5 yalign 0.5
    $ renpy.pause(3.0)
    scene ev p_background with dissolve
    play music "bgm/Pathetique_Orgel.mp3"
    python:
        k = puzzle5()
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
            jump diary591220
label diary591220:
    stop music
    stop bgs
    scene black with memory
    play music "bgm/happy4.mp3"
    nvl clear
    narrator_nvl"1959년 12월 20일 일요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 많이 옴"
    nvl clear
    narrator_nvl"나는 메리와 연애를 하는것이 아니라고 생각을 하니까 쓸대없는 걱정이 많이 없어지면서 마음이 편해졌다."
    narrator_nvl"연애라고 하는 나에게 생소한 이미지를 떠올리려고 하는 부담감이 없어져서 그런가보다."
    narrator_nvl"나와 메리는 협력관계."
    extend" 즉, 내가 메리의 꿈에 협력을 하고, 메리도 내 목표를 달성하는데 협력을 하는 거다."
    narrator_nvl"마음가짐에 따라서 이렇게 기분이 달라지다니……"
    scene bg diary_park_snow at Zoom((1280,720),(0,0,1280,720),(290,265,373,210),0) with movedown
    play bgs "bgs/kids.mp3"
    $ mary_cloth = 2
    show mary with dissolve:
        zoom 1.5 xalign 0.6 yalign -0.3
    show snow
    "그리고 오늘은 메리의 소설을 쓰는것에 대해서 듣고있다."
    mary"혹시 녹스의 10계 라고 알아?"
    edward"아니"
    extend", 그게 뭔데?"
    mary"\'로날드 A. 녹스(Ronald A. Knox)\'라고 하는 유명 추리 소설 작가가 만들어낸 일종의 미스테리 장르의 기본 규칙이야"
    mary"이거랑 비슷하게 반 다인의 20칙이 있는데, 그건 나한텐 별로 와닿지가 않더라고"
    mary"어쨌건 최근엔 그걸로 공부를 해서 시나리오를 구상중인데, 혹시 들어볼래?"
    edward"그래"
    show mary think
    mary"에헴"
    show mary
    mary"우선 주인공을……"
    "이렇게 가만히 메리의 말을 듣는 것만으로도 그녀에게 도움이 될 수 있다는 게 너무 좋다."
    "그녀에게 도움이 된다는 뜻은, 나의 목표를 이루는데도 도움을 받을 수 있다는 뜻이기 때문이기도 하지만……"
    "말로는 설명하기 힘든 작은 기쁨이 있었다."
    show mary tsun
    mary"듣고 있는거야?"
    edward"어, 어?!"
    mary"역시, 그럴 줄 알았어"
    edward"미, 미안……"
    "또 무의식적으로 나의 버릇이 나와버렸나보다."
    show mary talk with dissolve
    mary"혹시 나랑 소설얘기하는 게 재미없어?"
    edward"그럴리가!"
    edward"이건 그냥 내가 평상시에 가지고 있는 안 좋은 버릇 같은 거라고 할까……"
    edward"딱히 메리의 이야기랑은 관련 없어!"
    mary"소설 쓰는데 독자의 흥미를 끄는 게 가장 중요하니까 솔직히 말 해도 돼"
    edward"글쎄 그런게 아니래도……"
    "하지만 아주 틀린건 아니다."
    "물론 메리의 소설이 재미없어서가 아니라, 내가 별로 관심이 없어서 라고 해야 할까……"
    show mary
    mary"그럼 그냥 대화 주제를 바꾸자"
    mary"혹시 이번 크리스마스때 약속 있어?"
    edward"내가 있을리가 없지"
    mary"그럼 그때 같이 시내에 있는 대공원에 가자"
    mary"거긴 밤에 조명이 아주 끝내준다고 하더라고!"
    show mary shy
    mary"또……{cps=2} {/cps}연인들 끼리가면 잘 된다는 이야기도 있고……"
    show mary shy2
    mary"이, 일단 우리 둘은 연인 이기도 하니까 말이야……!"
    edward"그래,{cps=2} {/cps}왠지 재미있을거 같네"
    show mary
    mary"어?"
    mary"에드, 뭔가 바뀐거 같아"
    edward"정말?{cps=2} {/cps}어디가?"
    mary"말로는 하기 힘들지만……"
    show mary smile
    mary"그래도 난 지금의 에드가 더 좋은 거 같아"
    show mary shy2
    mary"악……!"
    mary"아, 아무것도 아니야!"
    mary"그보다 책 얘기나 계속하자!"
    edward"으, 응"
    scene black with movedown
    stop bgs
    play music "bgm/smooth6.mp3"
    nvl clear
    narrator_nvl"1959년 12월 25일 금요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 많이 옴"
    nvl clear
    narrator_nvl"오늘은 크리스마스"
    narrator_nvl"메리와 같이 시내에 있는 대공원에 가기로 했다."
    narrator_nvl"어제 메리 말론, 거긴 먹을곳이 하주 많기 때문에 밤에 가는것보단 오전에 일찍이 가는 게 더 좋다고 한다."
    narrator_nvl"그래서 약속 시간을 넉넉하게 오전 10시로 잡았다."
    narrator_nvl"근데 내가 괜한 시간 낭비를 하는 바람에 약속 시간에 좀 많이 늦게 됐다."
    centered"오전 10시 21분"
    play bgs"bgs/people.mp3"
    scene bg diary_walkway with dissolve
    show snow
    "여긴 사람이 엄청나게 많았다."
    "그리고 그 사람들 중 80\%는 서로 붙어있었다."
    "으으……"
    "얼른 메리를 찾아야겠다는 생각이 들었다."
    show bg diary_walkway at Zoom((1280,720),(0,0,1280,720),(0,0,640,365),0.6)
    $ renpy.pause(1.0)
    show bg diary_walkway at Zoom((1280,720),(0,0,640,365),(640,0,640,365),0.6)
    $ renpy.pause(1.0)
    show bg diary_walkway at Zoom((1280,720),(640,0,640,365),(640,355,640,365),0.6)
    $ renpy.pause(1.0)
    show bg diary_walkway at Zoom((1280,720),(640,355,640,365),(0,355,640,365),0.6)
    $ renpy.pause(1.0)
    edward"……?"
    "이리저리 돌아다녀도 메리가 보이지 않았다."
    "혹시 나랑 엇갈린걸까?"
    "아니면 기다리다 지쳐서 그냥 돌아 갔을까?"
    play sound "se/footsteps_running_snow.mp3"
    scene black with moveright
    $ renpy.pause(1.0)
    scene bg diary_walkway at Zoom((1280,720),(0,0,1280,720),(694,249,461,263),0.0) with dissolve
    show snow
    edward"허어……{cps=2} {/cps}허어……"
    edward"어디에 있는거지……"
    show mary cough with dissolve:
        zoom 1.7 xalign -0.4 yalign -0.4
    "그때 내 시야에 익숙한 금발이 들어왔다."
    play sound "se/footsteps_running_snow.mp3"
    edward"메리~!"
    "나는 손을 흔들면서 메리를 향해서 달려갔다."
    show bg diary_walkway at Zoom((1280,720),(694,249,461,263),(448,249,461,263),0.6)
    show mary cough:
        linear 0.6 xalign 0.5
    "근데 어째 상태가 조금 이상했다."
    "뭔가 많이 힘들어 하는듯 한 느낌이……"
    edward"괜찮아?!"
    mary"에드……"
    show mary cough:
        yalign -0.2
        linear 1.0 rotate 20 xalign 0.9
    stop bgs
    stop music
    $ renpy.pause(0.5)
    scene black with flash
    "그때 순식간이었다."
    play bgs "bgs/clock.mp3"
    play sound "se/heartbeat.mp3"
    scene ev mary_falling at Zoom((1280,720),(0,0,1280,720),(611,0,669,382),0.0) with flash
    "메리가 고통스러워 하는 표정을 짓더니……"
    play sound "se/heartbeat.mp3"
    scene ev mary_falling at Zoom((1280,720),(0,0,1280,720),(0,239,669,382),0.0) with flash
    "몸을 겨우 지탱해주던 마지막 힘이 풀리고……"
    play sound "se/heartbeat.mp3"
    scene ev mary_falling at Zoom((1280,720),(0,0,1280,720),(480,338,669,382),0.0) with flash
    "균형을 잃고서……"
    play sound "se/heartbeat.mp3"
    scene ev mary_falling at Zoom((1280,720),(305,169,669,382),(0,0,1280,720),0.3) with flash
    $ renpy.pause(1.0)
    play sound "se/fall.ogg"
    scene black
    $ renpy.vibrate(0.3)
    $ renpy.pause(0.7)
    edward"어……?!"
    "내가 본 관경을 믿을수가 없었다."
    "어제까지만 해도 건강했던 메리가……{cps=2} {/cps}왜?"
    "모든게 현실 같지가 않았다."
    "아주 나쁜 악몽을 꾸는 것만 같았다."
    play sound "se/heartbeat.mp3"
    show bg diary_walkway at Zoom((1280,720),(694,249,461,263),(448,249,461,263),0.0) with eyeopen
    $ renpy.pause(0.5)
    scene black with eyeshut
    "……하지만 현실이었다."
    stop bgs
    play music "bgm/sad5.mp3" fadein 0.5 fadeout 0.8
    nvl clear
    narrator_nvl"메리에게 무슨 일이 발생 한걸까?"
    narrator_nvl"얼마 전까지만 해도 그렇게 건강했던 메리가……"
    narrator_nvl"자신이 쓰고있는 소설에 대해서 자신있게 얘기 해줬던 메리가……"
    narrator_nvl"왜……?"
    narrator_nvl"내가 본 관경 때문에 정신이 없었던 나는, 급하게 메리를 병원으로 옮겼던것만 기억하고있다."
    narrator_nvl"그리고 그 이후로 어떻게든 메리의 아버지 —회장님— 께 연락을 취하고……"
    narrator_nvl"그래도 메리의 아버지가 노스탤지어 토이즈의 회장이어서 연락은 비교적 쉽게 할 수 있었다."
    scene bg diary_hospital_hall at Zoom((1280,720),(339,128,870,488),(339,128,870,488),0.0) with movedown
    show marydad mad:
        zoom 1.5 xalign 0.7 yalign -0.3
    show effect1
    play sound "se/shock.ogg"
    dad"{size=45}네놈 때문에!{/size}" with lshake
    hide effect1
    edward"지, 진정해주세요……!"
    dad"진정하라고?!"
    dad"너 때문에 내 하나뿐인 딸이 죽을지도 모르는데?!"
    edward"죽는다니요?!{cps=2} {/cps}메리한테 무슨 일이라도 있는거예요?!"
    dad"…………"
    show marydad mad:
        linear 0.3 zoom 1.8
    dad"자네가 누군지, 메리랑은 어떤 관계인진 잘 모르겠지만, 지금부터 내 말을 똑똑히 듣게나"
    dad"다시는……"
    dad"메리랑 만나지 마"
    dad"자네가 메리를 죽이고 있으니까!"
    edward"…………"
    "회장님의 말이 내 가슴에 쐐기를 박았다."
    "내가 메리를 죽이고 있다……"
    "난 그저 메리가 시키는대로 따랐을 뿐이었는데……"
    "나한텐 아무런 잘못이 없을텐데도……"
    "회장님의 표정을 보니까 가슴이 아팠다."
    "진짜로 내가 메리를 죽인 사람이 된 것 같은 기분이었다."
    "지금 무슨 일이 벌어지고 있는 건진 잘 모르겠지만……"
    "난 그녀가 죽는 건 원치 않다."
    "우린 서로의 목표를 이룰때까지 함께하는 협력관계"
    "그녀가 죽어버리면 난 또다시 혼자 남게 된다."
    "그건 안 돼……"
    edward"알겠습니다……{cps=2} {/cps}회장님……"
    edward"그럼 전 이만……"
    play sound "se/footsteps_concrete.mp3"
    scene black with Dissolve(1.0)
    "나는 무거워진 마음을 끌고 힘겹게 병원을 나왔다."
    "방금 무슨 일이 있었는지 알고싶지 않다."
    "그냥 이 모든게 꿈으로 끝났으면……"
    play music "bgm/sad4.mp3"
    nvl clear
    narrator_nvl"1959년 12월 26일 토요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 조금 옴"
    nvl clear
    narrator_nvl"오늘은 주말"
    narrator_nvl"난 주말이 너무 싫다."
    narrator_nvl"일을 할 수 없고, 돈을 벌 수 없는, 아무런 생산성이 없는 주말이 너무나도 싫었다."
    narrator_nvl"하지만 그런 주말도 메리랑 같이 보내면 희한하게 싫지 않았다."
    narrator_nvl"메리가 죽는다니……"
    narrator_nvl"메리가 죽는다니……"
    narrator_nvl"메리가 죽는다니……"
    narrator_nvl"메리가 죽는다니……"
    narrator_nvl"나 때문에……{cps=2} {/cps}메리가 죽는다니……"
    nvl clear
    narrator_nvl"내가 예전부터 일 하고 싶었던 장난감 회사에 취직 할 수 있게 됐고, 내가 원했던 돈을 벌 수 있게 됐고……"
    narrator_nvl"이 모든건 메리 덕분에 할 수 있었던거다."
    narrator_nvl"그리고 앞으로도 메리 덕분에 더 얻을 수 있었을지도 모른다."
    narrator_nvl"근데 그런 메리가 죽는다니……"
    narrator_nvl"더이상 만날 수 없게 된다니……"
    narrator_nvl"그것도 내가 같이 있었기 때문에 발생 한거였다니……"
    narrator_nvl"앞으로 그녀를 만나지 못하는거랑, 그녀가 죽는거랑 뭐가 다른거지?!"
    narrator_nvl"모르겠어……"
    narrator_nvl"아무것도 모르겠어"
    play sound "se/book_page.ogg"
    scene bg lib_day with memory
    show stephan talk with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"26일 날에 쓴 내용은 이게 전부야……"
    stephan_think"그날은 특별한 활동 없이, 하루종일 할머니 생각만 했던걸까?"
    play sound "se/book_page.ogg"
    scene black with memory
    nvl clear
    narrator_nvl"1959년 12월 27일 일요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 바람이 붐"
    nvl clear
    narrator_nvl"오늘은 주말의 마지막 날이다."
    narrator_nvl"그리고 내일 나는 회사에 출근을 하겠지"
    narrator_nvl"살면서 타인 때문에 이렇게 마음 고생을 해본건 처음 인 것 같았다."
    narrator_nvl"메리가 왜 갑자기 그렇게 쓰러졌는지도 모르겠지만, 지금 나의 행동도 이해가 안 갔다."
    narrator_nvl"왜 나는 이렇게까지 걱정을 하고 있는거지?"
    narrator_nvl"몇 년 전까지만 해도 메리 없이도 아무런 문제 없이 잘 살았을텐데……"
    narrator_nvl"이 감정에 대해선 잘 모르겠지만, 한가지 확실한건……"
    narrator_nvl"엄청나게 싫다."
    narrator_nvl"어떻게든 메리에 대해서 잊고 싶었다."
    narrator_nvl"하지만……"
    stop music
    centered"오전 11시"
    play sound "se/door_knock.mp3"
    $ extra_name = '집 주인 할아버지'
    extra"총각─!{cps=2} {/cps}총각 앞으로 전화가 왔어!"
    edward"잠시만요"
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(1.0)
    play sound "se/door_open.ogg"
    play bgs "bgs/wind.mp3"
    scene bg edward_house_day at Zoom((1280,720),(0,0,1280,720),(613,238,644,361),0.0) with movedown
    "나는 주인 할아버지 댁으로 들어갔다."
    play sound "se/door_open.ogg"
    scene black with moveleft
    stop bgs
    edward"여보세요?"
    $ extra_name = '남성의 목소리'
    extra"자네가 혹시 에드워드 토머군 인가?"
    "어디서 들어본적이 있었던 목소리였다."
    "분명……"
    dad"난 메리 아비 되는 사람인데……"
    "……역시나"
    play sound "se/think.mp3"
    scene bg diary_hospital_hall at Zoom((1280,720),(339,128,870,488),(339,128,870,488),0.0) with flash
    show marydad mad:
        zoom 1.8 xalign 0.7 yalign -0.3
    $ renpy.pause(1.0)
    scene black with flash
    "내가 어떻게 그 목소리를 잊었겠는가"
    dad"긴 말은 안 하마……"
    dad"메리가……{cps=2} {/cps}만나고 싶어 해……"
    play sound "se/heartbeat.mp3"
    edward"네……?"
    "메리가 날 만나고 싶어한다?"
    "그 말을 듣자 가슴이 떨렸다."
    "하지만 메리랑 만난다고 해서 뭘 하지?"
    "가는것이 망설여졌다."
    "어쩌면……"
    play sound "se/heartbeat.mp3"
    scene ev mary_falling with flash
    $ renpy.pause(0.5)
    scene black with flash
    "……나 때문에 메리가 그렇게 된걸지도 모르는 건데"
    dad"토머군, 몰턴 스미스병원 201호실로 와다오"
    play music "bgm/sad6.mp3"
    play bgs "se/footsteps_running.mp3"
    "메리가 있는 장소를 듣자마자, 나는 판단이 서기도 전에 몸이 먼저 움직여졌다."
    "회장님의 전화를 제대로 끊지도 않은체, 메리가 있는곳으로 달려갔다."
    show mary smile:
        alpha 0.0 xalign 0.5 yalign -0.4 zoom 1.7
        linear 1.0 alpha 0.8
    edward"메리……!"
    "아직 그녀가 죽은 게 아니라면 기회는 있다."
    "나는 더이상 그녀 때문에 고생하고 싶지 않다."
    "메리를 다시한번 만날 수만 있다면, 어떻게든 이 찝찝하고 싫은 감정을 떨쳐낼 수 있을지도 모른다는 생각을 가지면서 뛰었다."
    "그녀를 만날 수만 있다면……"
    "그리고 그녀 때문에 고생하는 이 마음만 어떻게 해결 할 수 있다면……"
    hide mary smile with dissolve
    stop bgs
    centered"몰턴 스미스병원 복도"
    scene bg diary_hospital_hall at Zoom((1280,720),(339,128,870,488),(755,202,525,295),0.0) with movedown
    "여기가 201호실 앞……"
    "긴장된 탓인지 문고리를 잡는 손이 많이 떨렸다."
    play sound "se/door_open.ogg"
    scene white with dissolve
    "그래도 깊은 심호흡을 한번 한 뒤에 있는 힘껏 문을 열었고……"
    scene bg diary_hospital_bed with dissolve
    $ renpy.pause(0.5)
    show bg diary_hospital_bed at Zoom((1280,720),(0,0,1280,720),(0,89,622,349),0.3)
    $ mary_cloth = 3
    $ mary_hair = 'mad'
    show mary tired with dissolve:
        zoom 1.6 xalign 0.4 yalign -0.4
    "메리가 있었다!"
    "안심과 기쁨의 파도에 휩쓸려버린 난 망설임 없이 입을 열었다."
    edward"메ㄹ……"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,89,622,349),(0,0,1280,720),0.2)
    show marydad talk:
        zoom 1.4 xalign 1.0 yalign -0.2
    dad"역시 자네가 토머 군 이었나……"
    "그때 내가 말을 마치기도 전에, 회장님이 나를 붙잡으셨다."
    dad"잠깐 날 따라오게나"
    edward"…………"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg diary_hospital_hall at Zoom((1280,720),(339,128,870,488),(755,202,525,295),0.0) with moveright
    show marydad talk with dissolve:
        zoom 1.6 xalign 0.6 yalign -0.3
    dad"자네에 대해선 메리에게 들었네"
    dad"둘이 서로 사귀는 사이 라면서?"
    edward"음……"
    extend" 그렇다고 해야겠죠"
    dad"어제 내가 자네한테 좀 심한 말을 한거 같았네……"
    dad"미안……"
    edward"아니에요!{cps=2} {/cps}그땐 저도 많이 당황 했는지라, 충분히 이해 합니다!"
    dad"고맙네"
    dad"그리고 메리에 대해선데……"
    dad"난 자네랑 메리가 서로 사랑 하는것에 대해선 진심으로 기쁘게 느끼고 있네"
    dad"나도 원랜 이렇게까지 말 하고 싶진 않지만……"
    show marydad mad
    stop music
    dad"미안하지만,{cps=2} {/cps}그녀랑 헤어져주게나"
    dad"메리가 토머 군 때문에 자기 몸에 대해서 제대로 생각 하지 않고 있어"
    dad"그러니 자네 쪽에서가 먼저 메리한테 헤어지자고 한다면 그녀도……"
    "어……?"
    "내가 지금 무슨 소리를 듣고 있는거지?"
    "메리랑 헤어지라고?"
    "어떻게 해야 할지 잘 모르겠다."
    "내가 그녀랑 헤어지면 앞으로 더이상 만날 수 없는 걸까?"
    "아니면 연인 —협력관계— 로만 있을 수 없을 뿐, 계속 만나는 건 가능 한가?"
    "이렇게 잡생각을 했지만……"
    "어제 회장님이 메리가 죽는다는 소리를 한게 떠올랐다."
    "곰곰히 생각해보면 난 뭘 어떻게 하든, 결국엔 메리랑 만날 수 없게 된다."
    "그럼 조금이라도 편한 쪽으로……"
    edward"회장님……"
    edward"메리랑 헤어지는 건 조금만 더 생각을 해보고 결정 하겠습니다"
    edward"하지만 그 전에……{cps=2} {/cps}전 지금 일어나고 있는 상황에 대해서 아무것도 모르겠어요"
    edward"혹시 알려 주실 수 있을까요?"
    show marydad talk
    dad"그건……"
    extend" 안에 들어가서 메리한테 직접 듣거라"
    dad"내 입으론 말 하지 말아달라는 메리의 부탁이 있어서……"
    edward"…………"
    dad"곧 있으면 메리 주사맞을 시간일테니까─대화는 빨리 끝낼 수 있도록 하게"
    play sound "se/footsteps_concrete.mp3"
    show marydad talk:
        linear 2.0 xalign 1.7
    "회장님께선 메리의 병실을 잠깐 바라보더니, 이내 자리를 비켜주셨다."
    "이런……"
    "또다시 여길 처음 왔을때처럼 병실 안을 들어가는 게 엄청 힘들어졌다."
    "그래도 이번엔 조금은 가벼워진 손으로 문을 열 수 있었다."
    play sound "se/door_open.ogg"
    scene black with dissolve
    $ renpy.pause(0.5)
    scene bg diary_hospital_bed with dissolve
    edward"메리……?"
    show bg diary_hospital_bed at Zoom((1280,720),(0,0,1280,720),(0,89,622,349),0.3)
    show mary tired with dissolve:
        zoom 1.6 xalign 0.4 yalign -0.4
    mary"……?"
    "방금 잠에서 깬듯한 메리가 고개를 들었다."
    mary"혹시 에드?"
    show effect1
    play sound "se/shock.ogg"
    show mary shock3
    mary"{size=45}잠깐, 에드워드?!{/size}" with lshake
    hide effect1
    play sound "se/search_bag.mp3"
    hide mary shock3 with Dissolve(1.0)
    $ mary_hair = 'normal'
    show mary shock2 with dissolve:
        zoom 1.6 xalign 0.4 yalign -0.4
    mary"에, 에드 와줬구나……!"
    edward"그보다 몸은 괜찮아?!"
    edward"갑자기 쓰러지니까 얼마나 걱정 했는데!"
    mary"지금은 아무런 문제 없으니까 걱정하지마~"
    show mary shock
    mary"근데……"
    mary"크리스마스때 했던 약속을 지키지 못해서 미안"
    edward"지금 그건 별로 중요하지 않아!"
    edward"메리……"
    play music "bgm/sad3.mp3"
    edward"네가 죽는다는 게 사실이야?!"
    mary"내가 죽는다고?"
    mary"확실히 내가 걸린 병이 심각하긴 하겠지만……"
    mary"혹시 그거 아빠한테서 들었어?"
    edward"자세한 건 너한테서 들으라고 했고……{cps=2} {/cps}일단 네가 죽을지도 모른다는 소리만 들었어"
    mary"내가 말 하지 말라고 했는데도 진짜……"
    show mary shock2
    mary"여기까지 알아버렸으면 어쩔 수 없겠구나……"
    mary"듣고 놀라지 않았으면 좋겠는데"
    mary"……아무래도 그건 힘들겠지?"
    edward"빨리 말 해줘"
    show mary talk
    mary"…………"
    mary"그게……"
    show mary shock
    mary"나 폐암이야……"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}진짜?!{/size}" with lshake
    hide effect1
    "나도 모르게 큰 소리를 내버렸다."
    mary"암 이긴 하지만……"
    show mary shock2
    mary"그, 그래도 수술하면 나을 수 있으니까 너무 걱정하진 마!"
    edward"정말이지?"
    show mary shock
    mary"확률의 문제니까 반드시라고는 말 못하겠지만……"
    show mary
    mary"그래도 옛날과 다르게─요즘은 의료기술이 좋아져서 아무 문제 없을거라 생각해"
    mary"과거에도 수술이 성공적이었으니까"
    edward"그래도 정말 괜찮겠어?"
    mary"얼마전가지만해도 일상생활에는 아무런 지장이 없었고……{cps=2} {/cps}분명 괜찮을거야"
    stop music
    edward"그렇구나……"
    edward"후우─"
    "메리의 대답이 나를 안심케 했다."
    play music "bgm/smooth1.mp3"
    "그녀는 아직 죽지 않는다."
    "수술을 받아야 하니까 잠시동안은 평상시처럼 있을 순 없겠지만, 그래도 시간이 지나면 모든게 원래대로 돌아올 수 있어……"
    "근데 한가지 의문점이 남았다."
    "왜 회장님은 나보고 더이상 메리와 만나지 말라고 하신걸까?"
    "혹시 그녀의 상태가 더 심각해지는 걸 막기 위해서?"
    "하지만 내가 그렇게 까지 할 필요가 있을까?"
    "그냥 나보고 메리랑 자주 돌아다니지 말라고 하셨어도 괜찮았을텐데……"
    edward"저기……"
    edward"그 암 말이야……{cps=2} {/cps}과거에도 그랬다고 했던데─언제부터 그랬어?"
    show mary talk
    mary"의사말론, 유전적으로 가졌을 확률이 높대……{cps=2} {/cps}그러니까─사실상 태어날때부터 계속 가지고 있었다고 봐야지"
    show mary think
    mary"생각해보니까 내가 미국에 있었을때도 한번 쓰러진적이 있었는데……"
    mary"그때부터 폐암이 생긴걸까?"
    show mary
    mary"그래도 그땐 수술해서 금방 일상생활에 들어갈 수 있었으니까, 이번에도 수술하면 괜찮아지겠지"
    mary"분명……"
    "회장님은 메리에게 계속 숨겨왔던 건가……"
    "이걸로 왜 회장님께서 평상시 메리를 곁에 두시려고 했는지 조금은 알 것 같았다."
    "그녀가 예전에 암에 걸렸었다보니까 항상 신경이 곤두서셨던거겠지"
    "그럼 나랑 메리가 헤어지라고 하라는것도 그저 메리가 걱정돼서……"
    play sound "se/door_open.ogg"
    $ extra_name = '간호사'
    extra"슈테른 씨, 주사 맞을 시간 입니다"
    show mary talk
    mary"아, 네─"
    show mary shock
    mary"저기 에드……{cps=2} {/cps}미안한데……"
    edward"어, 어!"
    edward"난 이만 가볼게!"
    show mary smile
    mary"응"
    mary"그리고 오늘 와줘서 고마워……"
    show mary shock2
    mary"여긴 엄청 심심하니까 자주 병문안 와주면 고맙겠어"
    edward"…………"
    play sound "se/footsteps_concrete.mp3"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,89,622,349),(0,0,1280,720),0.6)
    $ renpy.pause(0.6)
    scene black with moveright
    "나는 복도로 나갔다."
    stop music
    scene bg diary_hospital_hall at Zoom((1280,720),(339,128,870,488),(755,202,525,295),0.0) with moveright
    show marydad talk with dissolve:
        zoom 1.6 xalign 0.6 yalign -0.3
    dad"어때, 말 했는가?"
    edward"아……"
    "생각해보니까 내가 메리랑 헤어질지 말지에 대해서 생각하지 못했다."
    "하지만 고작 내가 그런 주제를 어찌 빨리 정할 수 있겠는가……"
    edward"그게……"
    extend" 조금만 더 고민 해볼 시간을 주세요……"
    dad"하긴……{cps=2} {/cps}그렇게 쉽게 결정 할 일은 아니지"
    edward"하지만 제가 꼭 메리와 헤어져야만 하는가요?"
    show marydad mad
    dad"메리한테 그녀의 상태를 듣지 않았는가?"
    edward"폐암이라고 들었습니다"
    edward"하지만 수술을 하면 치료 된다고 했어요!"
    edward"그러니까 굳이 헤어질 것 까지는……"
    show marydad talk
    dad"…………"
    dad"그게……{cps=2} {/cps}내가 아직 메리한테 알리지 못한 사실이 있어……"
    dad"어제 쓰러지자마자 받은 검사 결과에 의하면……{cps=2} {/cps}그녀는……"
    play music "bgm/sad5.mp3"
    dad"더이상 가망이 없어……"
    edward"네……?"
    edward"그, 그건 또 무슨……"
    dad"수술을 하기엔……{cps=2} {/cps}조금 늦었다는군"
    dad"살 날이 앞으로 길어봤자 1~2년 정도……"
    dad"지금 여기서 할 수 있는 최선이 항생제를 통한 수명 연장 정도밖에 없다더군"
    edward"…………"
    dad"혹시 어제 왜 메리가 갑자기 쓰러졌는지 아는가?"
    edward"아니요……"
    dad"아파서 기절했던거야……"
    dad"그런 몸이 될때까지 자네랑 같이 있겠다고 참았던거라고!"
    edward"…………"
    dad"그래도 자기 몸 관리를 제대로 할 수 있다면 어제같이 고생할 필요는 없어질지도 몰라!"
    show marydad talk
    dad"메리가 자네를 얼마만큼 생각하는지 다 들었다네……"
    dad"그리고 나도 아버지로써 내 딸이 누군가를 사랑하는 걸 진심으로 기쁘게 생각해"
    dad"하지만……"
    dad"그만큼 그녀가 고통스러워하는 걸 원치 않아……"
    dad"하지만 메리는 자네에게 약한 모습을 보이기 싫다면서─힘들게 기침을 참으려고 하고, 자네의 눈이 닿지 않는 곳에서 피를 토하고……"
    dad"그녀가 예전부터 앓고 있어서 증세를 심하게 보이진 않는 체질이라서 불행중 다행일지도 모르지만"
    dad"계속 고통받고있었다는 사실에는 변함이 없다네"
    edward"정말 메리와 헤어지는 거 이외에는 없는겁니까?"
    dad"자네를 생각했기 때문에 나온 결론일세"
    dad"계속 메리와 있다간 분명 후회할거야"
    dad"자네는 자기 곁에 있는 사람이 눈앞에서 죽는 걸 보기엔 너무 젊으니까"
    edward"…………"
    scene black with Dissolve(1.0)
    centered"오후 7시 20분"
    play bgs "bgs/wind.mp3"
    scene bg ravine_night with movedown
    edward"후우……"
    "그 이후로 계속 고민을 해봤지만, 이러지도 저러지도 못해서 결국 여기로 왔다."
    edward"여기도 참 오랫만에 와보네……"
    "내가 이곳을 마지막으로 방문해을때가 아마……"
    play sound "se/heartbeat.mp3"
    scene bg ravine_night at Zoom((1280,720),(297,0,644,362),(636,203,644,362),0.0)
    $ mary_cloth = 1
    show mary with flash:
        zoom 2.0 xalign 1.1 yalign -0.1
    $ renpy.pause(1.0)
    scene bg ravine_night with flash
    "내가 면접에 떨어졌을때 였지……"
    "여긴 아무리 힘든일이 있건, 괴로운 일이 있건, 저 멀리 있는 산을 보고있으면 마음이 뻥 뚫렸다."
    "그리고 내 고민이 어느정도 해소 되기도 한다."
    "몰턴에 처음 왔을땐 이곳에 자주 와서 내 기분을 풀었는데……"
    "메리와 만나고 나선……{cps=2} {/cps}자주 오지 않게 되었다."
    "아니, 올 필요가 없었다."
    "근데 오늘은……"
    scene black with eyeshut
    "도대체 난 어떻게 해야 하는 걸까……"
    "메리와 헤어져야 하는가?"
    "애초에 난 메리를 이성으로써 생각하지 않는다."
    "나의 가장 친한 친구, 혹은 스승과 같은 존재로써 인식하고있다."
    "그러니 헤어진다고 해도 난 크게 바뀐게 없다."
    "하지만……"
    show mary smile :
        zoom 1.7 xalign 0.5 yalign -0.4 alpha 0.0
        linear 1.0 alpha 1.0
    "과연 메리는 어떨지……"
    "내가 지금까지 본 메리의 반응으로 생각해보는 건데……"
    "어쩌면 그녀는 나를 좋아하고 있을지도 모른다."
    "적어도 나를 타인보다는 더 많은 관심을 두고 있다는 것 만큼은 확신했다."
    "설령내가 그녀를 사랑하지 않는다고 해도, 난 그녀에게 상처를 주고싶지 않다."
    "하지만 내가 그녀에게 헤어지자고 하면 분명 적지 않은 충격을 받겠지……"
    hide mary smile with dissolve
    edward"회장님께서 왜 내가 메리를 죽이고 있다고 말씀 하셨는지……{cps=2} {/cps}이제서야 알것 같아……"
    edward"난 너무 약해……"
    edward"너무 약하니까 항상 메리에게만 휘둘리는거야"
    edward"언제나 그녀가 시키는대로만 하고, 내가 스스로 의견을 내려고 하지 않고……"
    edward"지금도 내 생각보단 메리를 우선시하고……"
    edward"이렇게 약한 내가 계속 메리와 사귄다면, 난 옆에 있어도 그녀를 지켜줄 수 없겠지"
    edward"그렇기 때문에 그녀가 자신의 몸을 버려가면서 까지 나와 함께 있다고 해도 난 아무 말 없이 따르고……"
    edward"회장님의 말대로……{cps=2} {/cps}내가 메리를 죽이고 있는 걸지도 몰라"
    "현 상황에 대해서 심각한 갈등에 놓인 나는, 스스로에게 질문을 해봤다."
    "그럼 어떻게 해야 하는가?"
    "그리고 답 했다."
    edward"몰라……"
    edward"아무것도 모르겠어……!"
    "그럼 내가 아는 게 뭔가?"
    show ev mary_falling:
        alpha 0.0
        linear 1.0 alpha 0.5
    edward"메리는 죽는다는 걸 알고 있다"
    show ev mary_falling:
        linear 1.0 alpha 0.0
    "내가 할 수 있는 건 뭔가?"
    edward"메리와 헤어지든가,{cps=2} {/cps}그녀와 계속 관계를 유지한다"
    "나는 무엇을 원하는가?"
    edward"내가 꿈을 이뤄도 행복을 느끼지 못하는 이유의 원천을 해소 하는 것……"
    edward"즉, 돈을 버는 것……"
    "애초에 나와 메리가 서로 협력관계를 맺은 이유도 그렇다."
    "우리는 서로가 목표로 하고 있는 꿈을 이뤄나가기 위해서"
    "메리와 헤어지면 내 꿈은 더이상 이룰 수 없다."
    "또한 메리가 죽어도 마찬가지다."
    stop music
    stop bgs
    "하지만……"
    play bgs "bgs/clock.mp3"
    "메리는 죽어도 나는 살아있다."
    "메리와 헤어져버리면 더이상 협력관계로 있을수가 없겠지만, 그녀가 죽을때까지 옆에 있어주면 관계는 유지가 가능하다."
    "나도 그녀를 위해서, 그녀도 나를 위해서……"
    "이것이 바로 우리들"
    "하지만 메리는 어차피 살 날이 앞으로 1~2년 정도밖에 안 남았다고 한다."
    "아무리 사람한테 잘 대해줘도, 그 사람이 죽어버리면 전부 없었던걸로 돌아간다."
    "즉, 생산성이 없다."
    "그러니 내가 메리를 위해서 뭔가를 해도 그것은 \'낭비\'……"
    edward"그래……"
    edward"내가 아무리 메리 걱정을 해도, 그건 무의미해……"
    edward"하지만 내가 그녀를 통해서 얻을 수 있는것은 낭비가 아니야"
    play bgs "bgs/wind.mp3"
    scene bg ravine_night with eyeopen
    "지금 내가 어떻게 해야할지 알 것 같았다."
    scene black with Dissolve(1.0)
    stop bgs
    nvl clear
    narrator_nvl"1959년 12월 28일 월요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 눈이 잠깐 왔음"
    nvl clear
    narrator_nvl"오늘은 회사에 반차를 내서 일찍이 빠져나왔다."
    narrator_nvl"어제 내가 고민 끝에 도달한 결론을 메리에게 고백하기 위해서다."
    narrator_nvl"물론 내가 도달한 결론이 정답이라고 생각 하는 건 아니다."
    narrator_nvl"하지만 계속 쓸대없는 걸 가지고 망설였다간, 시간이 낭비된다."
    narrator_nvl"그러니 손실이 가장 적은 쪽, 그리고—또는 이익이 가장 많은 쪽으로 선택하는 게 상책이라 생각한다."
    centered"오전 11시 23분"
    play sound "se/door_open.ogg"
    scene bg diary_hospital_bed with flash
    play music "bgm/happy1.mp3"
    edward"실례하겠습니다"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,0,1280,720),(0,89,622,349),0.6)
    $ mary_cloth = 3
    $ renpy.pause(0.6)
    show mary shock with dissolve:
        zoom 1.6 xalign 0.4 yalign -0.4
    mary"에드?!"
    edward"안녕, 문병왔어"
    "메리의 목소리가 조금 쉰 것 같았다."
    "내가 평상시에 알고있었던 목소리와 달라서 작은 괴리감을 느끼긴 했지만, 그래도 메리는 메리라고 자신에게 되새겼다."
    show mary talk
    mary"이 시간에?{cps=2} {/cps}회사는 어쩌고?"
    edward"그건 걱정하지 않아도 돼"
    edward"그리고 일찍이 와야 더 오랫동안 같이 있을 수 있잖아?"
    show mary happy
    mary"에드……"
    show mary shock
    mary"뭐 잘못먹었어?"
    edward"어어?!"
    mary"평소와는 다른 모습이니까……"
    edward"그게……"
    edward"네가 그때 쓰러진 게 너무 아파서 기절 했던거라고 들었어……"
    edward"그래서 나도 여러가지 생각을 해봤거든……"
    show mary shock2
    mary"…………"
    edward"난 네가 또 그렇게 아파하는 건 원치 않아"
    edward"그래서……"
    edward"그래서 널 더이상 아프게 놔두지 않을거야"
    show mary shy
    mary"…………"
    play sound "se/search_bag.mp3"
    show mary smile with dissolve:
        zoom 2.0
    "메리는 웃으면서 나를 포옹했다."
    mary"정말 고마워……{cps=2} {/cps}에드 덕분에 난 행복해"
    edward"나도……"
    extend" 네 덕분에 정말 행복해"
    stop music
    play sound "se/door_open.ogg"
    scene bg diary_hospital_bed
    show marydad talk with dissolve:
        xalign 0.8 yalign 1.0
    dad"…………"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,0,1280,720),(0,89,622,349),0.3)
    $ renpy.pause(0.3)
    show mary shock3 with dissolve:
        zoom 2.0 xalign 0.4
    mary"…………"
    edward"…………"
    play sound "se/shock.ogg"
    show mary shock2:
        zoom 1.6
    mary"{size=45}아아아 아빠!{/size}" with lshake
    "회장님도 오늘은 출근을 안 하셨다?!"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,89,622,349),(0,0,1280,720),0.3)
    $ renpy.pause(0.3)
    show marydad talk:
        xalign 0.8 yalign 1.0
    dad"아, 아무래도 내가 좋지 못한 타이밍에 들어왔구나"
    dad"방해꾼은 사라져 줄테니 할거 계속 하거라"
    play sound "se/footsteps_concrete.mp3"
    show marydad mad:
        linear 2.0 xalign 1.5 zoom 1.8 yalign -0.6
    "회장님은 다시 밖으로 나가시려고 했다."
    edward"저, 저기 회장님!!"
    stop sound
    show marydad mad:
        linear 0.3 xalign 0.8 zoom 1.0 yalign 1.0
    "그때 나는 빠른 동작으로 회장님을 붙잡았다."
    dad"뭐지……?"
    "원랜 메리랑 둘이서 천천히 말 하려고 했는데……"
    "회장님 께서도 여기에 계신다면 그냥 바로 말 해야겠다."
    edward"저번에 말씀하신거……{cps=2} {/cps}결정 했습니다"
    play sound "se/search_bag.mp3"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,0,1280,720),(658,248,622,349),1.0) with dissolve
    $ renpy.pause(1.0)
    show marydad talk with dissolve:
        zoom 1.7 xalign 0.6 yalign -0.3
    "회장님께서는 병실에 있는 소파에 앉으시면서 입을 여셨다."
    dad"흐음……"
    dad"그래서 어떻게 하기로 했는가?"
    "무의식적으로 긴장하게 되자, 나는 침을 꿀꺽 삼키면서 마음을 가다듬었다."
    scene bg diary_hospital_bed at Zoom((1280,720),(658,248,622,349),(0,89,622,349),0.3)
    $ renpy.pause(0.3)
    show mary shock with dissolve:
        zoom 1.8 xalign 0.4 yalign -0.4
    "그리고 천천히……{cps=2} {/cps}메리를 바라보면서 입을 열었다."
    edward"메리……"
    edward"크리스마스때 내가 늦게 나오는 바람에……{cps=2} {/cps}그렇게 됐잖아……"
    mary"그, 그건 에드워드의 잘못이 아니니까 딱히 책임감을 느낄 필요는 없는데……"
    edward"이건 단순히 책임감의 문제가 아니야"
    edward"내가 예전에 말 했잖아,{cps=2} {/cps}네가 날 도와준다면 나도 널 도와주겠다고"
    edward"난 네 곁에서 널 도와주고 싶어"
    edward"그리고 네 곁에서 나도 너한테 도움받고 싶어"
    edward"크리스마스때 처럼 널 혼자 둬서 이번 같은 일을 반복시키고 싶지 않으니까……"
    edward"그러니까……"
    "말이 좀처럼 쉽게 나오질 않았다."
    "그냥 평범하게 입으로 하는 소리가 아니라……{cps=2} {/cps}마음으로 하는 소리라서 그런걸까……"
    edward"나랑……"
    edward"나랑 결혼 해 줄 수 있을까?"
    play music "bgm/smooth6.mp3"
    show mary shy2
    mary"……!"
    show mary shy
    mary"결혼 이라니……"
    mary"음……"
    "메리는 온몸을 베베 꼬면서 가만있지를 못했다."
    edward"역시 너무 갑작스러운걸까?"
    edward"하지만 네 몸 상태도 그렇고 해서……{cps=2} {/cps}지금이 아니면 제대로 말 해줄 기회를 놓칠거 같았거든"
    mary"내 몸은 문제 없다고 했는데도 그렇게까지 걱정해줬구나……"
    mary"근데 너무 결혼은 너무 갑작스러운 거 같기도 하고……"
    edward"역시 힘들려나?"
    show mary shy2
    mary"절대로 싫은 건 아니야!"
    show mary shy
    mary"아니, 오히려 좋기도 하고……"
    scene bg diary_hospital_bed at Zoom((1280,720),(0,89,622,349),(658,248,622,349),0.3)
    $ renpy.pause(0.3)
    show marydad mad:
        zoom 1.7 xalign 0.6 yalign -0.3
    dad"토머 군, 잠깐 나랑 대화 좀 함세!"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveleft
    "그렇게 회장님은 내 손목을 붙잡으면서 복도로 끌고 가셨다."
    stop music
    scene bg diary_hospital_hall at Zoom((1280,720),(339,128,870,488),(755,202,525,295),0.0) with moveleft
    show marydad mad:
        zoom 1.6 xalign 0.8 yalign -0.3
    show effect1
    play sound "se/shock.ogg"
    dad"{size=45}자네 방금 한 말이 진심인가?!{/size}" with lshake
    hide effect1
    edward"네, 처음부터 끝까지 다 저의 진심입니다"
    dad"내가 분명 메리가 처해있는 상황에 대해서 말 하지 않았는가?"
    dad"그럼에도 불구하고 그런 선택을 하겠다고?"
    edward"메리의 상태가 그렇기 때문에 더더욱 빨리 말 해야 한다고 생각 했어요"
    edward"그러니까 회장님……{cps=2} {/cps}아니, 아버님"
    edward"저에게 메리를 맡겨주세요"
    dad"어린 녀석이……"
    dad"자네……{cps=2} {/cps}그런 선택을 했다간 분명 후회 할게야"
    edward"설령 제가 후회를 한다고 해도……"
    edward"여기서 메리에게 아무것도 안 해주고 그녀를 보내는 것보단 더 좋다고 생각합니다"
    edward"전 메리 없인 아무것도 아니니까요"
    play music "bgm/sad6.mp3"
    dad"…………"
    show marydad talk with dissolve
    dad"그게……"
    extend" 그게 정말로 자네가 고민 끝에 도달한 결론인가?"
    edward"네"
    "그래……"
    "이게 바로 내가 도달한 결론이다."
    show black:
        alpha 0.0
        linear 5.0 alpha 1.0
    "나와 메리는 협력관계"
    "서로가 서로의 꿈과 목표, 그리고 소원을 위해서 협력하는 관계"
    "난 아직 나의 꿈을 완전히 달성하지 못했고, 그녀도 그녀의 꿈을 완수하지 못했다."
    "그러니 난 메리 곁에서 모든 꿈을 이뤄주고 싶다."
    "메리가 행복해지지 못한 상태에서 죽게 놔두고 싶지가 않다."
    "그리고 그녀가 죽었을때……"
    stop music
    "난 메리의 남편의 이름으로 그녀의 재산을 전부 가져간다."
    "그렇게 하면 나와 메리의 목표는 전부 이루게 된다."
    "난 메리를 통해서 내가 원하는 걸 얻고, 그녀는 나를 통해서 그녀가 원하 는 걸 이루게 된다."
    "사랑하지도 않는 여자를 강제로 사랑하도록 만드는 것보다 자연스럽고……"
    "낭비 없이……{cps=2} {/cps}서로가 행복해지는……{cps=2} {/cps}가장 이상적인 해답……"
    "그것이 바로 내가 도달한 결론이었다."
    ################################1959년 12월 28일 일기장 끝############################
    play music "bgm/sad2.mp3"
    play sound "se/book_page.ogg"
    scene bg lib_day with memory
    show stephan shock with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan"…………"
    "나는 할 말을 잃었다."
    "내가 알고있었던 할아버지는 할머니를 매우 사랑하셨는데……{cps=2} {/cps}그 두분의 결혼 계기가 이랬다니……"
    "물론 무족건 사랑이 있어야만 결혼이 가능한건 아니다."
    "아니, 현실엔 오히려 다른 목적에 의해서 결혼을 하게되는 경우가 더 많다."
    "하지만 할아버지는……"
    "적어도 내가 지금까지 알고 있었던 할아버지는 그러실분이 아닌것 같았는데……"
    scene black with eyeshut
    show grandpa mad with dissolve:
        zoom 1.7 xalign 0.5 yalign -0.4
    "역시 일기장에서 묘사된 할아버지와, 내가 평생을 알고 있었던 할아버지의 모습이 너무 달라서 이런 느낌이 드는가보다."
    "그때 한가지 가설이 생겼다."
    "혹시 할아버지가 할머니가 남긴 비밀에 집착하시는 이유가……{cps=2} {/cps}일종의 속죄하는 마음에서부터 나오는것이 아닐까?"
    hide grandpa mad with dissolve
    scene bg lib_day with eyeopen
    show stephan talk:
        zoom 2.0 yalign 0.1 xalign 1.0
    stephan_think"계속 일기장을 읽다보면 언젠간 내가 알고싶은 정답에 도달할 수 있겠지"
    ################################1959년 12월 29일 일기장 시작############################
    stop music
    play sound "se/case_start.mp3"
    scene black
    show text"{font=fonts/Type_Writer.ttf}{size=60}1959년 12월 29일{/size}{/font}" with memory:
        xalign 0.5 yalign 0.5
    $ renpy.pause(3.0)
    scene ev p_background with dissolve
    play music"bgm/Pathetique_Orgel.mp3"
    python:
        k = puzzle6()
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
            jump  diary19591229
label diary19591229:
    stop music
    play sound "se/book_page.ogg"
    scene black with memory
    play music "bgm/sad2.mp3"
    nvl clear
    narrator_nvl"1959년 12월 29일 화요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 하루종일 눈이 옴"
    nvl clear
    narrator_nvl"어제 메리에게 청혼을 하고나서부터 나에게 온 대답이라곤\'잠깐 생각할 시간을 줘\'뿐이었다."
    narrator_nvl"메리의 아버님도 나와 메리가 같이 결혼하는 것에 회의적인 반응을 보이셨다."
    narrator_nvl"혹시 이러다 메리가 나의 청혼을 거절하진 않을까 하는 걱정도 생겼다."
    narrator_nvl"그렇게 되면 매우 곤란한데……"
    narrator_nvl"물론 그녀가 싫다고 한다면, 나도 어떻게든 단념 할 생각이다."
    narrator_nvl"하지만 내가 메리랑 결혼하지 못 한다는 건……{cps=2} {/cps}내가 행복해질 수 있는 기회를 놓치는 것 같았다."
    narrator_nvl"그건 죽어가는 메리의 존재 가치를 낭비하는 것이겠지"
    narrator_nvl"일단 오늘도 병문안을 가보는거다."
    narrator_nvl"그러면 어떻게든 확실해지겠지"
    scene bg employee_office_night at Zoom((1280,720),(0,0,1280,720),(375,389,588,331),0.0) with Dissolve(1.0)
    centered"퇴근 전"
    "어제 회사를 일찍 퇴근해보니까─병문안이 끝나고, 나에겐 특별이 할 일이 없다는 사실을 알게 됐다."
    "그래서 오늘은 회사가 끝난 뒤에 메리의 병문안을 가기로 했다."
    "덕분에 집에서 의미없게 시간을 낭비하지 않아도 됐다."
    "하지만 내가 회사에서 일을 많이 한다고 해서 직장생활이 좋은 건 아니다."
    "오히려 처음 여기서 일 했을때보다 더 대우가 안 좋은 거 같다."
    "내 생각이지만─사내에서 메리와 같이 보내는 시간이 많은게 원인인 거 같다."
    "하지만 난 그런 시각을 별로 중요시 하지 않는다.{cps=2} {/cps}딱히 남들이랑 어울려다닌다고 해서 돈이 생기는것도 아니니까……"
    "괜히 신경쓰면 내 머리만 아프고"
    play bgs "bgs/people.mp3"
    $ extra_name = '다른 사람들'
    extra"(소근소근)"
    edward"……?"
    "갑자기 주변이 소란스러워졌다."
    "그리고 \'안녕하십니까\'와 같은 인삿말 까지 나오기 시작했다."
    play sound "se/search_bag.mp3"
    scene bg employee_office_night at Zoom((1280,720),(375,389,588,331),(375,247,588,331),0.4)
    "무슨일인지 궁금해진 나는, 자리에서 일어났다."
    "그리고 사람들이 몰려있는 쪽을 봤는데……"
    scene bg employee_office_night at Zoom((1280,720),(0,0,1280,720),(757,327,523,294),0.0) with dissolve
    show marydad with dissolve:
        zoom 1.6 xalign 0.3 yalign -0.3
    $ extra_name = '사원'
    extra"여긴 어쩐일로 오셨나요?{cps=2} {/cps}회장님"
    "주변이 소란스러웠던게 바로 회장님의 출현 때문이었다."
    dad"잠깐 사람을 데리러 왔네"
    play sound "se/footsteps_concrete.mp3"
    scene bg employee_office_night at Zoom((1280,720),(757,327,523,294),(375,247,588,331),0.4) with dissolve
    show marydad talk with dissolve:
        zoom 1.7 xalign 0.5 yalign -0.3
    "회장님은 내 앞에 다가오셨다."
    "그때문인지, 주변의 시선이 따갑게 느껴졌다."
    "어제 병원에서 만났을땐 그저 메리의 아버님 이라는 느낌으로 봐서 아무런 감정이 없었는데……"
    "회사에선 진짜로 회장님이라는 느낌이 들어서 그런지─옆에 있는 것 만으로도 짙눌려버릴 것 같은 기분이었다."
    stop bgs
    dad"토머 군……"
    extend" 오늘 내가 저녁식사를 대접하고 싶은데, 어떤가?"
    "그것이 회장님의 말씀이었다."
    edward"제안해주셔서 감사하지만, 제가 회사 끝나고 약속이 있어서요"
    edward"죄송하지만 거절해야 될 듯 합니다"
    edward"정말 죄송합니다"
    "다시 생각해보니까 나도 많이 성장했다는 게 느껴졌다."
    "원래같았으면 말 조차 제대로 하지 못했을텐데……"
    dad"자네의 약속 이라는 게─메리의 병문안 이라면 걱정 말게나"
    dad"그거에 관해서 말하고싶은 게 있어서 식사를 하자는 거니까"
    "메리에 관해서 하시고싶은 말 이라……"
    "생각해보니까 그거 말곤 나와 회장님이 같이 대화를 할 일이 없겠지"
    "그렇게 따지고보면 식사중에 할 말도 조금은 예상됐다."
    "……\'메리와의 결혼을 허락할 수 없다.\', \'더이상 만나지 마라\'와 같은 말씀을 하시려는 거 겠지"
    "그럼 가지말아야 하나?"
    "하지만 간다고 해서 나에게 손해가 오는 것도 아니고……"
    "아니, 오히려 저녁밥 이라는 이익이 생긴다."
    "식사자리에서 회장님이 나에게 무슨 말씀을 하시던, 난 내가 옳다고 생각하는 걸 관철시키면 되니까"
    edward"알겠습니다"
    dad"준비가 끝나면 따라오게나"
    stop music
    scene black with movedown
    centered"근처 페밀리 레스토랑"
    play bgs "bgs/people.mp3"
    play music "bgm/smooth1.mp3"
    scene bg diary_restaurant with movedown
    "시간이 저녁대라 그런지, 이곳엔 사람들이 꽤 있었다."
    "특히 주변에서 화목한 가족들을 많이 볼 수 있었다."
    "나와 많이 대립되는 이미지 때문일까……{cps=2} {/cps}그들을 보고 있자니, 조금 쓸쓸했다."
    show marydad talk with dissolve:
        xalign 0.2 yalign 1.0
    dad"왜그렇게 멍하니 있는가?"
    edward"아, 아닙니다"
    edward"그냥, 여긴 사람이 많구나 싶어서요……"
    dad"점심땐 예약 없인 자리에 앉을 수도 없다네"
    dad"이건 그나마 좋은 편이지"
    edward"그렇군요"
    dad"그보다 얼른 자리에 앉게나"
    play sound "se/search_bag.mp3"
    scene bg diary_restaurant at Zoom((1280,720),(0,0,1280,720),(446,147,475,267),0.0) with dissolve
    show marydad talk with dissolve:
        zoom 1.7 xalign 0.5 yalign -0.4
    "나는 회장님 앞에 마주어 보면서 앉았다."
    dad"토머 군"
    dad"내가 사는거니까, 걱정말고 마음껏 시키게나"
    edward"저, 정말로 괜찮나요?"
    show marydad mad
    dad"내 얘기를 들어준다는 전제하에서 사주는 거니까 착각하진 말거라"
    edward"아, 알겠습니다……!"
    show marydad talk
    dad"너무 긴장하지는 말고……"
    dad"어제 자네가 한 말을 듣고 내가 곰곰히 생각해서 말니까"
    dad"……그보다 얼른 주문을 합세"
    show black with Dissolve(1.0)
    "그 짧은 대화를 끝으로, 잠깐동안 무거운 침묵이 흘렀다."
    "하지만, 회장님의 표정을 봤을때─무겁다고 생각한 건 나 뿐이었을지도 모른다."
    "과연 무슨 생각을 하시는 걸까?"
    "처음엔 여기에 오자마자 나보고 더이상 메리와 만나지 말라고 말씀하실 줄 알았는데……"
    "회장님이 바로 본론으로 넘어가지 않는 게 조금 걸렸다."
    "그때 우리가 주문한 요리가 도착했다."
    hide black with eyeopen
    "회장님은 본인이 주문 한 요리─양송이 소스 스테이크─를 한입 드시곤, 드디어 말씀하셨다."
    dad"며칠전에 내가 자네에게 심한 소리를 해서 미안하네……"
    dad"병약한 아이를 둔 부모로써 너무 흥분해서 나온 소리라……"
    edward"아, 아닙니다!"
    edward"회장님께서도 그만큼 메리를 아끼셨다는 뜻 이니까요!"
    show marydad
    dad"이해심이 깊어서 다행이구나"
    show marydad talk
    dad"세삼스럽지만, 자네에게 다시 묻겠네"
    dad"토머 군,{cps=2} {/cps}자네는 아직도 메리랑 결혼하고 싶다고 생각하는가?"
    edward"그렇습니다"
    show marydad mad
    dad"메리의 몸 상태에 대해서 알고있으면서도 그런 선택을 하겠단 말인가?"
    edward"그렇기 때문에 한시라도 더 빨리 메리와 결혼을 해야된다고 생각했습니다"
    show marydad talk with dissolve
    dad"…………"
    dad"저번과 똑같은 대답을 하는구나"
    dad"거기다 자네의 눈을 보아하니……{cps=2} {/cps}쉽게 마음이 바뀔 거 같지도 않고……"
    dad"역시 자네는 나랑 처음 만났을때보다 말을 잘 하게 됐어"
    "처음 만났을때?"
    play sound "se/think.mp3"
    scene bg diary_trainstation at Zoom((1280,720),(0,0,1280,720),(632,235,648,364),0.0) with flash
    show marydad mad:
        zoom 1.7 xalign 0.8 yalign -0.3
    $ renpy.pause(1.0)
    scene bg diary_restaurant at Zoom((1280,720),(0,0,1280,720),(446,147,475,267),0.0) with flash
    show marydad talk:
        zoom 1.7 xalign 0.5 yalign -0.4
    "혹시 나랑 메리가 이스티아나에서 몰턴으로 돌아올때를 말 하시는 건가?"
    "하지만 그때 나는 회장님과 별다른 대화를 하지 않았던 걸로 기억한다."
    "아니면 내가 기억을 못하고 있을 뿐, 이전에도 만나뵌적이 있었나?"
    dad"그때 자네는 남의 눈을 똑바로 쳐다보지도 못 했고, 목소리에 떨림이 있었고……"
    dad"어느 하나도 잘난 구석이 없었던 남자였는데……"
    "회장님은 마치 말썽꾸러기 제자에게 잔소리를 하는 스승의 어투로 나의 단점을 늘어놓으셨다."
    "처음엔 기분이 불쾌했지만, 말씀을 계속 들어보니까 어째 상황이 전부 낯이 익었다."
    "그런데 그 상황이 언제 였었는지……"
    stop bgs
    play sound "se/think.mp3"
    show ev edward_interview at blur with flash:
        crop(440,0,363,204)
        size(1280,720)
    $ renpy.pause(1.0)
    hide ev edward_interview with flash
    play bgs"bgs/people.mp3"
    "그래……"
    "작년에 내가 노스탤지어 토이즈에서 면접을 봤을때의 모습을 연캐했다."
    "기억이 많이 가물가물하지만……{cps=2} {/cps}어쩌면 내가 면접을 봤을때 회장님도 그 자리에 있었을 가능성이 있다."
    "즉, 나와 회장님의 첫 만남은 몰턴역에서가 아니라, 회사 면접때 였었던거다."
    "그러자 내가 과거에 어떤 모습을 하고 있었는지가 회장님의 말을 통해서 피부에 와닿았다."
    edward"그, 그때 전 사회 경험 같은 것도 없었으니까요……"
    edward"지금의 제가 있는 것도, 그때 메리를 만났기 덕분이라 생각합니다"
    dad"그것이 바로 자네가 메리를 사랑하는 이유인가?"
    edward"사랑……{cps=2} {/cps}이라고 불러야 할지는 모르겠네요……"
    edward"전 그저 메리에게 받은 만큼 다시 해주고싶고"
    edward"그리고 제가 해준만큼, 다시 메리에게 받고 싶은 거죠……"
    show marydad
    dad"서로가 서로를 위하고, 정을 주고받는 사이"
    dad"그걸 사랑이라고 부르지 않는다면 뭐라 하는가?"
    edward"협력관계……{cps=2} {/cps}려나요?"
    dad"허허허"
    dad"재밌는 얘기를 하는구나"
    edward"그, 그랬는가요?"
    dad"자네가 말 한 사랑은 남녀간의 연애가 아니라, 부부사이의 감정에 가까운데"
    dad"자네는 벌써부터 메리를 인생의 동반자로 생각을 하는겐가"
    edward"으, 음……"
    dad"점점 자네가 마음에 드는구나"
    dad"메리를 맡겨도 안심이야……"
    edward"그 말은 저랑 메리의 혼인을 허락하신다는 뜻 인가요?!"
    show marydad talk
    dad"허락이고 뭐고, 난 메리의 행복만을 최우선으로 한다네"
    dad"그래서 지금까지 계속 메리 곁에 있어줬는데……"
    dad"나도 평생 그녀 옆에 있어줄 순 없다는 사실을 알고 있었다네"
    dad"솔직히, 언젠간 이런 일이 올거라는 것도 알고 있었어"
    show marydad
    dad"자네같은 사람이 메리 곁에 있어주겠다고 하니까 다행일세"
    dad"거기다……"
    dad" 암 이라는 병 자체가 스트레스를 받지 않으면 괜찮다고도 하니까……"
    dad"일에서 조금 멀어지고, 자기가 사랑하는 사람 곁에 항상 있으면 기적이라도 일어날지 모르잖은가?"
    dad"그러니……"
    edward"잘 알겠습니다. 회장님……"
    dad"이럴땐 아버님 이라고 불러야 하지 않는가?"
    edward"그, 그렇군요!{cps=2} {/cps}아버님!"
    "회장님께서는 스트레스를 받지 않으므로써 메리의 병이 나을지도 모른다고 말씀 하셨다."
    "하지만 그럴 일은 절대 없겠지"
    "애초에 스트레스 하나 받지 않는다는 이유만으로 큰 병이 났는다면 의사는 왜 있겠는가?"
    "하지만 그런 근거없는 말 조차도 믿어보는……{cps=2} {/cps}안될 걸 알면서도, 됐으면 좋겠다고 굳게 믿고있는……"
    "지푸라기라도 잡아보려는 회장님의 마음이 나의 시선을 끌었다."
    "처음엔 많이 딱딱하고 고리타분한 성격을 가지신 분이라고 생각했지만, 실제론 정 반대였다."
    "만약 내가 생각하는 이상적인 아버지의 모습이 있다면, 분명 회장님같은 사람이리라 생각한다."
    show marydad talk
    dad"…………"
    dad"자네라면 분명 메리를 잘 지켜줄거라 믿어 의심치 않네만……"
    dad"그 선택을 후회하게될지도 모른다는 생각이 나를 불편하게 만드는구나"
    dad"왜냐면 나도 과거에 자네랑 똑같은 상황이었으니까"
    edward"똑같다니요……?"
    dad"혹시 메리가 어째서 폐암에 걸렸는지 아는가?"
    edward"전 유전이라고 들었습니다"
    dad"흠……{cps=2} {/cps}거기까지 들었다면, 길게 말 할 필요는 없겠군"
    dad"메리의 암은, 자기 엄마에게서 유전 됐다네"
    edward"그럼 어머님은 지금……?"
    show marydad mad
    stop music
    dad"메리가 아주 어렸을때 생을 마감했지"
    edward"아……"
    edward"이거, 죄송합니다……"
    show marydad talk
    dad"아니네, 자네가 그런 마음을 가질 필요는 없네"
    dad"나도 그녀가 그렇게 가게 될거라는 걸 예전부터 알고있었으니까"
    dad"그저……{cps=2} {/cps}메리 만큼은 달랐길 원했을 뿐이지……"
    dad"메리는 자기 엄마를 아주 좋아했었는데……"
    dad"어렸을때 자기 엄마가 피아노를 치면, 메리는 옆에서 그걸 듣고, 직접 쳐보기도 하고, 음악에 맞춰서 노래를 부르기도 하고……"
    play sound "se/think.mp3"
    $ mary_cloth = 1
    scene bg diary_stage at Zoom((1280,720),(0,0,1280,720),(591,180,426,240),0.0) with flash
    show mary happy:
        zoom 1.5 xalign 0.1 yalign -0.4
    "메리의 어렸을 적 모습을 듣고─나는 생각해봤다."
    "저번에 메리랑 같이 연주회에 갔을때 메리가 보인 미소가, 어쩌면 자신이 어렸을때 좋아했던 걸 회상하면서 생긴 미소였을 수도 있다고"
    scene bg diary_restaurant at Zoom((1280,720),(0,0,1280,720),(446,147,475,267),0.0) with flash
    show marydad talk:
        zoom 1.7 xalign 0.5 yalign -0.4
    dad"당시에 사업이 지금처럼 크지 않았기에, 나는 일 때문에 바빠서 메리 곁에 있어주진 못 했지만……"
    extend" 메리엄마가 있었기 때문에 나는 조금 안심이었어"
    dad"전쟁 때문에 집안이 경재적으로 힘들었을 때도, 그녀는 작은 피아노 학원을 차려서 어떻게든 보탬이 되려고 노력했고……"
    show marydad mad
    play music "bgm/sad3.mp3"
    dad"그렇게 좋았던 사람을……{cps=2} {/cps}내가 일에만 너무 열중 한 나머지, 계속 고통스러웠다는 사실을 미쳐 알지 못했어……"
    dad"지금 생각만 해도……"
    edward"많이……{cps=2} {/cps}괴로우셨겠어요……"
    show marydad talk
    dad"나보단 메리가 더 힘들었지……"
    dad"나는 그때의 일을 다시는 반복시키지 않겠다는 의지로 항상 메리를 곁에 두고, 그녀가 행복하기만을 바라왔는데……"
    dad"설마 이렇게 반복 될 줄이야"
    dad"그러니까 토머 군"
    show marydad mad
    dad"자네가 메리랑 결혼을 결심하겠다면─이거 하나 만큼은 알아줬으면 한다네"
    dad"모든게 끝났을 때……{cps=2} {/cps}후회 할 일은 하지 말게나"
    edward"알겠습니다"
    show marydad talk with dissolve
    dad"…………"
    dad"이걸로 자네는 어떻게든 됐구나"
    dad"문제는 메리 뿐인데……"
    edward"메리한테 무슨 일이라도 있나요?"
    dad"메리……"
    dad"최근들어서 그녀도 자기 몸에 심각한 문제가 있다는 걸 눈치채기 시작했다네"
    dad"병세가 시간이 지날수록 점점 악화돼가고 있으니 무리도 아니지"
    dad"그때문인지, 그녀는 자기가 정말로 자네랑 결혼을 해도 괜찮은지 망설이고있어"
    dad"난 메리의 의견을 최우선 하지만─그녀 스스로가 원했던 걸 부정하는 건 부모로써 보고싶지 않구나……"
    "메리가 나의 청혼을 거절할 수도 있다니……"
    "─그런 생각이 나를 초조하게 만들었다."
    "메리가 결혼하기 싫었기 때문에 하는 선택이라면, 난 그 선택을 받아들일 생각이었다."
    "하지만 메리도 사실은 하고싶다거나 하는─나에게 기회가 주어진 상태에서 포기해버리는 건 싫다."
    "아버님도 내가 메리랑 결혼하기를 원하시고, 아마 메리 스스로도 싫어하진 않을거다."
    show black with Dissolve(1.0)
    "하지만 지금 상황은 조금 곤란해……"
    "마음이 점점 초조해졌다."
    "그래……"
    "절대 이 기회를 놓쳐선 안 돼"
    "그녀가 죽는다는 사실은 거의 확정 돼 있다."
    "메리의 얼마 남지 않은 삶 동안, 나는 그녀를 행복하게 만들어주고싶다."
    "결혼만 성공한다면……"
    "난 항상 메리 곁에 있어주고싶다."
    "그리고 그녀의 꿈과 소원을 전부 이뤄주고싶다."
    "어차피 나의 행복은 메리가 죽고 난 뒤에─그녀의 재산을 통해서─찾아오니까"
    "그때까지만이라도 얼마남지 않은 사람에게 행복을 주고싶다."
    "그렇기에 지금 내 행동엔 아무런 문제가 없다."
    play sound "se/door_open.ogg"
    stop music
    stop bgs
    scene bg diary_hospital_bed_night with moveleft
    $ mary_cloth = 3
    edward"실례하겠습니다"
    show bg diary_hospital_bed_night at Zoom((1280,720),(0,0,1280,720),(0,152,588,331),0.4)
    $ renpy.pause(0.4)
    show mary shock2 with dissolve:
        zoom 1.7 xalign 0.4 yalign -0.4
    mary"에, 에드!"
    mary"왔구나"
    edward"응"
    edward"몸은 괜찮아?"
    show mary
    mary"어제보다 좋아진 건 아니지만……{cps=2} {/cps}그래도 살만해"
    edward"많이 힘들었구나……"
    show mary shock2
    mary"그런 건 아니야!"
    mary"여기 밥을 제외하곤 다 좋은 걸!"
    mary"침대도 푹신푹신하고, 일 생각도 하지 않아도 되고……"
    mary"거기다 이 환자복이 어찌나 편하던지!"
    extend" 집에가져가서 잠옷으로 쓰고싶은 기분이라니까!"
    show mary shock
    mary"…………"
    show mary smile
    mary"그, 그보다─오늘은 평상시보다 많이 늦었네? 무슨 일 있었어?"
    edward"회장님……{cps=2} {/cps}아버님이랑 만났어"
    show mary talk
    mary"아빠랑?"
    extend" 왠일이래?"
    edward"우리 둘의 결혼을 허락하신대"
    show mary shy2
    mary"……!"
    edward"메리, 넌 어떻게 생각하고있어?"
    edward"어제 내 고백에 대한 대답을 들려줘"
    show mary shy
    mary"난……"
    show mary hurt
    $ renpy.vibrate(0.3)
    mary"윽……!" with sshake
    edward"괜찮아?!"
    show mary cough
    mary"후우……{cps=2} {/cps}후우……"
    mary"그게……"
    play music "bgm/sad2.mp3" fadein 1.0
    show mary sad with dissolve
    mary"내가 너랑 결혼을 해도 괜찮을지 모르겠어……"
    edward"어……?"
    mary"난 청소도 못하고, 요리도 못하고, 몸도 약해서 자주 못나가고……"
    mary"이런 내가 정말 좋은 아내가 될 수 있을지……"
    mary"혹시 결혼하고 나서, 내가 네 짐이 되지 않을지……"
    mary"너무 걱정 돼……"
    "메리는 직접적으로 말 하는 걸 피하고있었지만─아버님 말대로 본인이 앞으로 살 날이 얼마 남지 않았다는 걸 어떻게든 느끼고 있다는 걸 알 수 있었다."
    edward"그럴리가없잖아!"
    edward"요리나 집안일은 나중에 메이드 같은 걸 고용하면 되고, 몸이 약한 건─차가 있으니까 굳이 걸을 필요도 없어!"
    edward"나랑 결혼하면, 도움이 된다면 되는거지, 절대 짐이 되진 않아!"
    edward"그러니까 괜찮아"
    mary"그렇게 말해줘서 고맙지만……{cps=2} {/cps}난 어떻게 해야할지 모르겠어……"
    mary"에드, 조금만 더 생각 할 시간을 줘"
    edward"왜 그렇게까지 망설이고 있는지 물어봐도 될까?"
    mary"…………"
    mary"그냥 내 기분 탓 일지도 모르지만……"
    mary"정말로 내 몸이 수술받는다고 해서 나을 수 있을지 모르겠어"
    edward"그건 결혼이랑 관계 없잖아!"
    edward"오히려 나을 수 없다면─내가 옆에서 널 지켜줄께"
    edward"그러니까─"
    stop music fadeout 2.0
    mary"에드,{cps=2} {/cps}왜 그렇게까지 나랑 결혼하려는 거야?"
    edward"어?"
    edward"왜냐니……"
    play bgs"bgs/clock.mp3"
    mary"내가 암이라는 말을 하자마자 바로 다음 날에─아무런 예고도 없이─청혼하고……"
    mary"아무리 내가 치료될 수 있다고 말 했지만……"
    mary"나랑 결혼하면 분명 힘들텐데"
    mary"일부러 그렇게 자기를 힘들게 하려는 행동……{cps=2} {/cps}나로썬 이해하기 힘들어……"
    edward"…………"
    "혹시 내 행동을 의심하고 있는가?"
    "나의 진짜 의도를 눈치챌까 봐 불안했다."
    "그렇게된다면, 나랑 결혼은 커녕─오히려 나를 피하고, 나쁜사람 취급을 하겠지……"
    "결혼 이전보다 더 안 좋게 끝난다."
    "여기선 어떻게든 잘 핑계대야 할텐데……"
    stop bgs
    edward"그, 그러니까……"
    edward"솔직히 나도 내가 왜이러는지 잘 모르겠어……"
    play music "bgm/sad6.mp3"
    edward"그런데, 왠지 널 잃어버릴 것 같아서 두려운 걸!"
    edward"그래서 널 놓치기 전에……{cps=2} {/cps}조금 더 가까이서 있고싶었어……"
    edward"결혼 후가 어쨌건, 네 곁에 있을 수 있는 게─나에겐 행복이니까"
    show mary shy with dissolve
    mary"…………"
    mary"정말 그렇게 생각하는 거야?"
    edward"그래"
    edward"난 널 잃고싶지 않아"
    mary"하지만 난 누군가가 나 때문에 힘들어지고, 괴로워지고, 고통받는 걸 원치 않아……"
    mary"특히 에드, 너라면 더욱……"
    show mary sad
    mary"그러니까 결혼에 대해서 조금더 깊게 생각해봐야 한다고 생각해"
    edward"계속 생각만 했다간─막상 행동으로 옮겼을땐─이미 늦어있을지도 모르잖아"
    mary"생각없이 방황하는 것보단, 늦더라도 길을 아는게 훨씬 좋잖아"
    mary"그러니까 에드……"
    scene black
    stop music fadeout 2.0
    mary"지금 당장은 나도 잘 모르겠어……"
    play bgs"bgs/people.mp3"
    scene bg diary_hospital_hall at Zoom((1280,720),(0,0,1280,720),(597,168,683,384),0.0) with Dissolve(1.0)
    edward"큭……"
    "순간 화가났다."
    "메리는 날 사랑한다면서, 왜 계속 결혼을 피하려는 거지?!"
    "이해할 수 없었다."
    "사랑하는 사람이 청혼을 해왔으면 보통 받아주는 게 정상이 아닌가?"
    "아무래도 메리가 나를 의심했던 것 때문에 머릿속이 많이 복잡한가보다."
    stop bgs
    scene black with Dissolve(1.0)
    "우선 머리를 좀 식히기로했다."
    centered"오후 8시 12분"
    play bgs"bgs/wind.mp3"
    scene bg ravine_night with movedown
    "뭐가 문제였길래, 메리가 그런 반응을 보였을까……"
    "방금 메리가 나에게 한 말을 생각해봤을때─그녀는 결혼 자체를 싫어하진 않은 것 같았다."
    "그냥 나에게 피해주고싶지 않다 등의 이유만 있었을 뿐"
    "즉, 내가 어떻게든 잘만 한다면, 충분히 결혼을 승락받을 수 있을 것이다."
    "하지만 내가 뭘 어떻게 해야 하는가……"
    "가장 중요한게 떠오르질 않았다."
    "일단 메리도 잠시만 기다려달라는 말을 했기 때문에, 지금은 시간이 약일지도 모른다."
    "……라는 생각을 하자─아버님의 말씀이 떠올랐다."
    "메리는 길어봤자 1~2년 정도밖에 남지 않았다."
    "물론 최대가 그정도이지, 실제론 더 짧을 수도 있다."
    "어쨌건, 결혼하기 전에 메리가 죽어버리는 건 나에게 곤란하다."
    "그럼 어떡게 하는게 좋을까……?"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}아아!{cps=2} {/cps}모르겠어!{/size}" with lshake
    hide effect1
    "나는 홧김에 소리쳤다."
    "하지만 들려오는거라곤─바람소리와, 나의 메아리 뿐"
    "그래도 이 장소에서 소리를 지르니까 기분이 조금 풀리긴 했다."
    "헌데……{cps=2} {/cps}기분이 풀려봤자, 편안해진 걸 제외하곤 딱히 좋은게……"
    play music "bgm/beat4.mp3"
    play sound "se/heartbeat.mp3"
    edward"……!"
    "순간 머릿속에서 한가지 생각이 떠올랐다."
    "\'혹시 말하는 분위기가 중요한게 아닌가?\'하고"
    "우선─지금까지 나는 환자들이 많은 병원에서 메리에게 청혼했다."
    "게다가 생각해보니까 아주머니께서도 \'여자는 분위기에 약해\'같은 말을 했었던 것 같기도 했고"
    "혹시 다음엔 메리가 기뻐할만한 장소나 상황에서 청혼을 해본다면 어떨까?"
    "시험해볼 가치는 있다고 생각했다."
    "하지만 메리가 과연 어디를 좋아할지……"
    play sound "se/think.mp3"
    $ mary_cloth = 1
    stop bgs
    scene bg diary_stage at Zoom((1280,720),(0,0,1280,720),(591,180,426,240),0.0) with flash
    show mary happy:
        zoom 1.5 xalign 0.1 yalign -0.4
    $ renpy.pause(0.5)
    play bgs"bgs/wind.mp3"
    scene bg ravine_night with flash
    "그래……"
    "나는 예전부터 피아노를─한 곡 뿐이지만─칠 줄은 알았다."
    "그렇게하면 분명 메리가 원하는 \'분위기\'를 만들 수 있을지도 몰라"
    "하지만 어떻게 준비 할 수 있을까 생각해봤는데……"
    "나에겐 아버님이 있었다.{cps=2} {/cps}그분의 힘을 빌린다면 어떻게든 될지도 몰라"
    stop music fadeout 1.0
    scene black with Dissolve(1.0)
    stop bgs
    nvl clear
    narrator_nvl"1959년 12월 30일 수요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 맑음"
    nvl clear
    narrator_nvl"오늘, 나는 회사에서 아버님에게 나의 계획을 간청드렸다."
    narrator_nvl"예상외로 흥쾌히 도와주시겠다고 하셨다."
    narrator_nvl"이렇게 나온다면 내 계획에 조금더 뼈와 살을 붙여서 성공률을 높힐 수 있을지도 모른다."
    narrator_nvl"하지만 내가 회사에서 사적인 일에 얽메힌 탓일까, 예전같이 일이 손에 잡히질 않았다."
    narrator_nvl"또한─직장 동료들의 시선도 예전보다 더 안 좋았다."
    narrator_nvl"그래도 상관없다."
    narrator_nvl"메리와의 결혼만 성공하면, 여기서 일 하는 것 보다 훨씬 더 많은 돈을 빠르고, 쉽게 벌 수 있을테니까"
    narrator_nvl"여기서 멍청하게 일하는 것보단 훨씬 더 성공해 있을 거니까"
    play music "bgm/happy1.mp3"
    nvl clear
    narrator_nvl"1959년 12월 31일 목요일"
    narrator_nvl"에드워드 토머 27세"
    narrator_nvl"날씨 - 구름이 조금 있음"
    nvl clear
    narrator_nvl"오늘 나는 메리에게 다시한번 청혼한다."
    narrator_nvl"대신 이번엔 조금더─메리가 생각하는─로맨틱 한 분위기를 연출해보기로 했다."
    narrator_nvl"오늘 이 작전의 시간이 어느정도 걸릴지 몰라서, 그냥 회사에 연차를 냈다."
    narrator_nvl"이걸로 나에겐 하루종일 준비 할 시간이 주어졌다."
    stop music fadeout 2.0
    scene bg diary_stage with movedown
    "내가 어제 아버님에게 간청 드린 결과─나에게 몰턴 극장 전체를 잠시동안 사용할 수 있게 해주셨다."
    "그 뿐만 아니라, 반지도, 그리고 두번째 서프라이즈도 준비할 수 있었다."
    "내 계획대로만 된다면 확실하게 메리가 결혼을 승락해주겠지"
    "그런데 여기, 저번에 왔을 땐 사람들로 가득했는데……{cps=2} {/cps}지금은 횡하기만 했다."
    "아버님이 어떻게해서 극장을 통째로 빌리셨는 진 잘 모르겠지만, 역시 돈과 인맥이 있으면 못하는 게 없는가보다."
    "그렇게 생각하니까 세삼스럽게 돈이 얼마나 좋은 건지 다시 떠올랐다."
    "하지만 내가 메리와의 결혼만 성공시킬 수 있다면……{cps=2} {/cps}나도 극장 한대 쯤은 문제없이 빌릴 수 있는 힘을 가질 수 있게 될꺼야"
    "그때 문득 한가지 의문점이 들었다."
    "나는 돈을 원하는 걸까?{cps=2} {/cps}아니면 힘을 원하는 걸까?"
    edward"아니야……"
    extend" 돈이 곧 힘, 둘 중 하나를 얻으면─다른 하나는 자연스럽게 손에 들어오게 돼"
    "주변이 너무 조용해서 나도 모르게 쓸대없는 생각으로 시간을 낭비할뻔했다."
    "나는 고개를 좌우로 격하게 흔들고, 양손으로 볼을 툭툭 쳐서 정신을 집중했다."
    "지금 시간은 9시"
    extend", 내가 메리보고 여기로 오라고 한 시간까진 앞으로 2시간 정도 남았다."
    "그때까지 리허설을 하면서 기다리기로 했다."
    play sound "se/footsteps_concrete.mp3"
    scene bg diary_stage at Zoom((1280,720),(0,0,1280,720),(204,260,640,360),2.0)
    $ renpy.pause(2.0)
    scene ev edward_piano2 with dissolve:
        size(1280,720)
        crop(566,272,640,360)
    "나는 피아노 앞에 다가가서─건반위에 손을 살포시 얹었다."
    "내가 마지막으로 피아노를 쳐봤을때가 언제였을까……"
    "기억상으론 몰턴시로 자취하기 이전─이스티아나에서 생활 했을때─였다."
    "그때 마린다가 다니던 초등학교에 있던 학교 피아노로 한번 쳐본적이 있었지"
    "당시 나는 피아노를 특별히 배워본 기억은 없었는대도 희한하게─마치 전생에 기억을 떠올렸다는 듯이……"
    "아니, 마치 나의 태생적인 본능이었다는 듯이─매우 쉽게, 감각적으로 칠 수 있었다."
    "주변에선 혹시 내가 모챠르트나 베토벤 같은 피아노 천재가 아닌가 하는 생각도 했지만……"
    "오직 한곡만 칠 수 있었고, 피아노나, 음악 전체에 대한 음감이 있는 것도 아니라─내가 알고있는 그 한곡에 대한 감각만 본능처럼 알고있었다."
    "무엇보다 연주를 한다고 즐겁게 느껴지지 않았다."
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    "그럼에도 불구하고─이렇게 가만히……{cps=2} {/cps}피아노 앞에 앉고, 건반위에 손을 얹으면 다음 동작이 저절로 머릿속에 떠올랐다."
    edward"메리가 올때까지 시간도 얼마 남지 않았는데……"
    extend" 그때까지 메리를 위한 최고의 연주회를 준비해볼까"
    play sound "se/case_start.mp3"
    scene white
    $ renpy.pause(3.0)
    centered"약속 시간"
    scene bg diary_stage with moveright
    $ renpy.pause(1.0)
    $ mary_cloth = 2
    play sound "se/footsteps_concrete.mp3"
    show bg diary_stage at Zoom((1280,720),(0,0,1280,720),(761,200,389,218),1.0) with dissolve
    "내가 리허설을 마치고, 메리가 오기를 기다리다. 입구에서 이쪽으로 걸어오는 오는 발소리가 들렸다."
    show mary talk:
        xalign 0.3 zoom 1.5 yalign -0.5 alpha 0.0
        linear 0.5 alpha 1.0
    show marydad:
        xalign 0.7 zoom 1.5 yalign -0.4
        linear 0.5 alpha 1.0
    "메리와 아버님이었다."
    mary"에드?"
    mary"여긴……"
    scene bg diary_stage at Zoom((1280,720),(761,200,389,218),(406,159,790,444),0.5)
    $ renpy.pause(0.5)
    "피아노와 함께 스테이지에 서 있던 나는 메리에게 말 했다."
    edward"어서와, 메리"
    edward"널 위해서 아버님과 함께 이 무대를 준비해봤어"
    show bg diary_stage at Zoom((1280,720),(0,0,1280,720),(761,200,389,218),0.0)
    show mary shock:
        xalign 0.3 zoom 1.5 yalign -0.5
    show marydad:
        xalign 0.7 zoom 1.5 yalign -0.4
    mary"날 위해서……?"
    mary"그게 무슨 소리야?{cps=2} {/cps}내가 지금 상황이 조금 이해가 안 가는데……"
    scene bg diary_stage at Zoom((1280,720),(761,200,389,218),(406,159,790,444),0.5)
    $ renpy.pause(0.5)
    edward"최근들어서 같이 시간을 보낸적이 없었잖아"
    edward"가끔은 이런것도 좋다고 생각돼서……"
    edward"그러니까 넌 그냥 가만히 자리에 앉아서 음악을 감상해줘"
    edward"단지 그 뿐이야"
    edward"너에게 주는……{cps=2} {/cps}선물이니까……"
    play music "bgs/clock.mp3"
    "그럼……"
    scene black with dissolve
    "나는 말을 마치고 피아노 앞에 앉았다."
    "이제……"
    "피아노를 치기만 하면 돼……"
    "그렇게 손을 건반위에 올렸다."
    "그리고……{cps=2} {/cps}나머지는 자연스럽게 나의 감각에 맡겼다."
    play music "bgm/Pathetique.mp3"
    scene ev edward_piano1 with eyeopen
    $ renpy.pause(2.0,hard=True)
    scene ev edward_piano1 at Zoom((1280,720),(0,0,1280,720),(361,0,919,517),0.0) with dissolve
    show ev edward_piano1 at Zoom((1280,720),(361,0,919,517),(361,203,919,517),8.0)
    $ renpy.pause(8.0,hard=True)
    scene ev edward_piano2 at Zoom((1280,720),(522,147,758,427),(0,147,758,427),10.0) with dissolve
    $ renpy.pause(10.0,hard=True)
    scene ev edward_piano2 at Zoom((1280,720),(0,0,1280,720),(0,0,1280,720),0.0) with memory
    $ renpy.pause(2.0,hard=True)
    scene ev edward_piano2 at Zoom((1280,720),(640,0,640,360),(0,360,640,360),8.0) with dissolve
    $ renpy.pause(8.0,hard=True)
    scene ev edward_piano1 at Zoom((1280,720),(590,138,640,360),(530,360,640,360),5.0) with dissolve
    $ renpy.pause(6.0,hard=True)
    scene ev edward_piano3 with Dissolve(1.0)
    show expression (StarField().sm) as starfield with dissolve
    $ renpy.pause(5.0,hard=True)
    show ev edward_piano3 at Zoom((1280,720),(640,0,640,360),(640,360,640,360),8.0) with Dissolve(1.0)
    $ renpy.pause(9.0,hard=True)
    show image "static" onlayer texture
    show ev edward_interview with flash
    $ renpy.pause(1.0,hard=True)
    show ev edward_interview with flash:
        size(1280,720)
        crop(221,20,364,204)
    $ renpy.pause(3.0,hard=True)
    show ev mary_falling with flash:
        size(1280,720)
        crop(0,0,1280,720)
    $ renpy.pause(1.0,hard=True)
    show ev mary_falling at Zoom((1280,720),(595,0,579,324),(332,396,579,324),3.0) with flash
    $ renpy.pause(3.0,hard=True)
    show ev edward_hug at Zoom((1280,720),(320,198,579,324),(0,0,1280,720),3.0) with flash
    $ renpy.pause(3.0,hard=True)
    scene ev edward_piano2 at Zoom((1280,720),(0,0,1280,720),(492,270,640,360),0.0) with memory
    $ renpy.pause(5.0,hard=True)
    hide image "static" onlayer texture
    stop music
    scene bg diary_stage at Zoom((1280,720),(416,332,347,195),(416,332,347,195),0.0) with movedown
    $ renpy.pause(1.0,hard=True)
    play bgs "se/clapping.mp3"
    scene bg diary_stage at Zoom((1280,720),(416,332,347,195),(597,200,618,347),2.0)
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(2.5)
    play sound "se/search_bag.mp3"
    scene bg diary_stage at Zoom((1280,720),(597,200,618,347),(597,310,618,347),0.5)
    "연주를 마친 나는, 자리에서 일어난 뒤에, 관중들─메리와 아버님─에게 고개를 숙였다."
    scene bg diary_stage with dissolve:
        size(1280,720)
        crop(593,290,315,180)
    show mary cry:
        zoom 1.6 xalign 0.3 yalign -0.5 alpha 0.0
        linear 1.0 alpha 1.0
    show marydad:
        zoom 1.6 xalign 0.7 yalign -0.5 alpha 0.0
        linear 1.0 alpha 1.0
    "그리고, 그 상태로 메리와 아버님의 상태를 살짝 엿봤는데……"
    "박수를 치고 있었던 건 아버님 뿐이었고, 메리는 눈가에 눈물이 맺혀있는 상태로 가만히 있었다."
    stop bgs fadeout 1.0
    show marydad talk:
        alpha 1.0
        linear 0.5 xalign 0.6
    dad"메리, 왜그러느냐?!"
    mary"…………"
    play music "bgm/smooth6.mp3"
    mary"\'비창(Pathetique)\'……"
    edward"어?"
    mary"그 곡의 이름이야……"
    mary"예전에 엄마가 나한테 가르쳐 준적이 있었거든……"
    play sound "se/search_bag.mp3"
    hide mary cry with dissolve
    show mary happy with dissolve:
        zoom 1.6 xalign 0.3 yalign -0.5
    mary"이렇게 다시들어보니까 옛날 생각이 났어"
    show marydad
    mary"에드, 정말 아름다운 연주야"
    show mary tease
    mary"내가 오늘 아픈 몸을 이끌고 힘들게 온 보람이 있었네"
    edward"호, 혹시 내가 폐가 되거나 하진 않았겠지?!"
    show mary smile
    mary"그런건 아니야~"
    show mary
    mary"여긴 병원에서부터 별로 멀지도 않았고, 아빠가 차로 태워줘서 오는데는 아무런 문제 없었어"
    "메리의 표정을 보니까, 그녀가 행복해 하는 기분을 알게 되니까─지금 내가 잘 하고 있다고 생각해서─나는 조금 안심이 됐다."
    "이렇게 계속 그녀의 앞엔 죽음 뿐이라는 사실은 잊게 하고……{cps=2} {/cps}\'지금\'이 순간 만큼은 기쁘다는 걸 알려준다면……"
    "분명 메리도 나와 결혼 하고 싶다고 생각하겠지"
    "무엇이 \'서로\'의 \'행복\'이라는 걸 알게 되겠지"
    show mary talk
    mary"근데 아빠랑 같이 이 이벤트를 준비 했다고 했는데……"
    show mary shock
    mary"설마 극장을 통째로 빌린거야?"
    edward"맞는데?"
    show mary happy
    mary"왠지 드라마에 나올법한 시츄에이션이라 그런지, 두근거렸어"
    edward"다, 다행이야……"
    "사실 극장을 빌릴땐─전부 아버님의 힘이었지, 난 한 게 아무것도 없었지만"
    edward"그런데, 아직 이거가지고 두근거리기엔 일러"
    show mary talk
    mary"……?"
    mary"뭔가 더 준비한게 있어?"
    edward"메리, 이제 슬슬 점심시간인데, 배고프지 않아?"
    edward"내가 알고있는 레스토랑이 있거든"
    show mary shock
    mary"으, 음……"
    mary"확실히 조금 출출하긴 한데……"
    edward"왜그래?"
    show mary shock2
    mary"아니야.{cps=2} {/cps}그냥, 무슨 또 무슨 이벤트를 준비 했는지 궁금했어"
    edward"후후. 그럼 가볼까?"
    dad"운전은 내가 할테니, 걱정 말거라"
    edward"감사합니다. 아버님"
    play sound "se/footsteps_concrete.mp3"
    scene black with Dissolve(1.0)
    stop music
    play bgs "bgs/people.mp3"
    scene bg diary_restaurant with moveup
    "지금 시간은 바로 점심"
    "내가 예상했던대로 안엔 사람들로 가득했다."
    "딱 원했던 상황이다."
    show mary shock with dissolve:
        zoom 1.7 xalign 0.0 yalign -0.4
    mary"사람이 많네"
    edward"걱정하지마"
    "나는 식당 입구에 있는 점원에게 말 했다."
    edward"에드워드 토머로 예약했습니다만"
    $ extra_name = '점원'
    extra"두분이시죠?{cps=2} {/cps}이쪽으로 모시겠습니다"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveright
    $ renpy.pause(2.0)
    scene bg diary_restaurant with moveright:
        size(1280,720)
        crop(497,113,529,298)
    "그렇게 점원은 주문판을 테이블위에 올려놓고, 주문이 끝나면 불러달라며 다른 테이블로 이동했다."
    show mary shock with dissolve:
        zoom 1.6 xalign 0.4 yalign -0.5
    mary"피아노 연주회에 이어서, 페밀리 레스토랑 까지……"
    mary"다음엔 어딜 데려갈 생각일지……{cps=2} {/cps}상상도 안 가"
    edward"그럼 뭘 해도 너에겐 서프라이즈가 되겠네?"
    edward"기대해도 좋아"
    show mary shock3 with dissolve
    mary"…………"
    mary"에드, 조금 무서운데?"
    "메리의 어리둥절해 하는 반응도 어느정도 이해됐다."
    "이건 평소의 내가 아니다."
    "평소의 나는 이런 생산성 없는 시간낭비는 하지 않겠지"
    "하지만 그건 \'생산성\'이 없었을 때 뿐"
    "오늘 나에겐 확실한 이익이 있다."
    "나는 평소에는 보이지 않던 순수한 미소를 하면서 말 했다."
    edward"여기 양송이 스테이크가 맛있다더라"
    edward"근데 여기있는 파스타도 좋아보이고……"
    edward"넌 어떤걸로 먹을래?"
    show mary
    mary"에드"
    mary"오늘은 나보다, 네가 더 기뻐해하는 거 같네"
    edward"그, 그런가?"
    show mary smile
    mary"그래서 나도 기뻐"
    show mary think
    mary"평소에 보지 못했던 모습을 보니까……{cps=2} {/cps}진짜 연인같은 느낌?"
    show mary smile
    mary"아무튼 그런 느낌이 들어서 좋아"
    edward"진짜 연인 이란 말이지……"
    "순간 기분이 이상했다."
    "우린 예전부터 진짜 연인이었는데……"
    extend" 왜 이제와서 그런 소리를?"
    "혹시 내가 평상시엔 하지 않았던─\'연인\'들이 할 법 한 이벤트를 해서 그런건가?"
    edward"갑작스런 호기심에 묻는건데……"
    edward"오늘의 나랑, 평소의 내가 구체적으로 어떻게 다른거야?"
    show mary think
    mary"음……"
    mary"구체적이라 말 하니까 조금 힘든데……"
    show mary
    mary"뭔가를 엄청 열심히 하는 듯 한 느낌이려나?"
    mary"나랑 같이 있을땐 전혀 보지 못한 모습이었어"
    edward"…………"
    "열심히 하는 모습이라……"
    "돈을 벌 수 있는 기횐데……"
    "열심히 하지 않으면 아무것도 이루지 못할텐데, 당연하지"
    "라고 스스로에게 되새기며, 쓸대없는 생각을 접었다."
    edward"먹고싶은 건 골랐어?"
    show mary smile
    mary"음. 난 이걸로 할 게"
    show black with Dissolve(1.0)
    play music "bgs/eating.mp3"
    "그렇게 우리는 같이 식사를 했다."
    "맛은……{cps=2} {/cps}별로 기억에 남지 않았다."
    "아무래도 나의 \'작전\'을 시행에 옮길 타이밍을 계속 기다리고 있어서 그랬는가보다."
    "얼마후, 나와 메리가 잡담으로 대화의 꽃을 피울때 였다."
    "나는 이제 슬슬 \'프로포즈\'의 타이밍이 왔다고 판단했다."
    show mary
    hide black with eyeopen
    $ renpy.pause(1.0)
    play sound "se/search_bag.mp3"
    scene bg diary_restaurant at Zoom((1280,720),(497,113,529,298),(214,58,908,512),0.5) with dissolve
    show mary talk with dissolve:
        zoom 1.2 xalign 0.5 ypos 0.2
    stop music
    mary"……?"
    mary"갑자기 왜그래?"
    "현재 나는 의자에서 일어나 있는 상태이다."
    "이제부터 메레에게 프로포즈를 한다."
    play music "bgs/clock.mp3"
    "하지만……{cps=2} {/cps}이번 프로포즈는 저번과 다르다."
    "저번에 내가 실수했던 걸로 추정되는 문제점들을 전부 보완시켰고, 만일의 사태의 대비도 해놨다."
    "이렇게하면 분명 메리는 내 프로포즈를 승락해줄 수 밖에 없겠지"
    play sound "se/search_bag.mp3"
    show bg diary_restaurant at Zoom((1280,720),(214,58,908,512),(214,150,908,512),0.5)
    show mary shock:
        linear 0.5 yalign -0.1
    "나는 메리 앞에 무릎을 꿇고─아버님의 힘으로 얻은─반지상자 안의 반지를 보이면서, 영화나 드라마에서 나올법한 장면을 그대로 따라했다."
    "저번엔 내가 말만 했었지만……{cps=2} {/cps}이번엔 달라"
    stop music
    edward"메리"
    show mary shy2
    stop bgs
    edward"나랑 결혼해줘"
    mary"……!"
    mary"여, 여기서 말 하는거야?!"
    "주변의 시선이 느껴진다."
    "당연하겠지, 이 시간대엔 사람이 많으니까"
    "조금 부끄럽다는 생각도 들었다."
    "하지만 후회는 없었다.{cps=2} {/cps}돈을 버는데, 잠깐의 부끄러움 쯤이야 못 참으랴"
    "그리고 내가 굳이 이 시간에, 이 장소를 고른데엔 한가지 이유가 있다."
    play music "bgm/sirius6.mp3"
    scene bg diary_restaurant at Zoom((1280,720),(0,0,640,360),(640,0,640,360),30) with dissolve
    show letterbox
    "……그것은 바로 사람들의 시선"
    "이렇게 많은 사람들의 면전에서 메리에게 프로포즈를 한다면─그녀도 엄청난 압박감을 느낄것이다."
    "메리같은 성격을 지닌 사람이라면 이 상황을 미안해서라도 받아주겠지"
    hide letterbox
    show bg diary_restaurant at Zoom((1280,720),(214,58,908,512),(214,150,908,512),0.0)
    show mary shy2:
        zoom 1.2 xalign 0.5 yalign 1.0
    "난 메리의 대답이 오기도 전에 벌써부터 입가에 미소가 지어져 있었다."
    "이럴 수록 냉정해져야 되는데……{cps=2} {/cps}벌써부터 메리가 죽은 이후의 상황을 생각 하니까, 웃음을 참기가 힘들었다."
    "아직 성공한 것도 아닌데, 벌써부터 둘이 결혼 한 것 처럼 기뻤다."
    mary"에, 에드! 어서 일어나!"
    mary"사람들이 보고있단 말이야……"
    edward"난 하루종일 이렇게 너의 대답을 기다릴 수 있어"
    show mary shy with dissolve
    mary"…………"
    mary"지금까지 했던 행동들……{cps=2} {/cps}전부 이걸 위해서였구나"
    mary"하지만 내가 어떤지 넌 잘 알고 있잖아……"
    edward"네가 필요하다면 몇번이고 다시 말 할 게"
    edward"난 너랑 결혼해서 절대로 후회하지 않을거야"
    mary"하, 하지만……"
    "메리는 끝까지 망설이며, 대답을 주체하고 있었다."
    "난 그 망설임의 이유를 알고있었다."
    "그녀는 자신의 죽음으로써 타인에게 피해를 주는것을 싫어했다."
    "……하지만 나는 그 심정을 이해할 수 없었다."
    "왜 메리는 자기보단 남을 더 신경쓰는걸까?"
    "그래서 나는 메리에게 말 했다."
    edward"메리……"
    extend" 네가 원하는게 뭔데?"
    edward"할 수 \'있다\' \'없다\'를 넘어선……{cps=2} {/cps}지금 네가 \'원하는게\' 뭐야?"
    mary"난……"
    mary"널 사랑해……"
    mary"너랑 같이있고 싶어……"
    mary"하지만 그렇게 때문에 너를 괴롭게 만들고싶지 않아"
    edward"내가 괴로워하는건 내가 신경써야 할 몫이야"
    edward"그러니까 넌 네가 하고싶은 선택을 해줬으면 해"
    mary"…………"
    "그녀는 또다시 망설였다."
    "하지만 이번 망설임은 꽤나 짧았다."
    "메리도 결심을 한거겠지"
    "그녀도 나처럼 \'지금\'당장 원하는 걸 얻고자 하는거겠지"
    show mary happy with dissolve
    mary"사랑해, 에드"
    scene white with Dissolve(1.0)
    "그리고 나는 메리의 가느다랗고, 고운 손가락에 반지를 끼워줬다."
    "주변에선 식사를 하던 손님들의 갈채소리가 들렸다."
    "메리의 눈에 눈물이 고여있는 게 보였다."
    "분명 그 눈물은 기쁨에서부터 우러나오는 눈물이겠지"
    "그리고 내가 지금 짓고있는 미소는……"
    "분명 나의 바램이 이루어졌다는 쾌감에서부터 나오는 미소겠지"
################################1959년 12월 31일 일기장 끝############################
    return
    stop music
    stop bgs
    if not_drink == True:
        scene bg ravine_grave_night with memory
        play music "bgm/sad2.mp3"
        play bgs "bgs/wind.mp3"
        centered"오후 6시 26분"
        "나는 차갑고도 은은한 바람을 쐐면서, 할머니의 묘비 앞에 쭈그려서 앉았다."
        "그리고 비석에 쓰여진 문자를 검지손가락으로 어루만졌다."
        "이 묘비에 의하면 할머니가 돌아가셨던 날짜는 1972년 6월 7일"
        "내가 마지막으로 읽었던 부분이 59년도의 마지막 날 이었던 걸 생각해보면……"
        "할머니는 약 12년 하고도 반년정도 더 사셨다는 뜻이다."
        "확실히 보통사람 치고는 일찍이 돌아가셨지만……"
        "폐암을 앓고 계셨다는 걸 생각해보면 꽤 오래사셨다고 볼 수 있다."
        stephan_think"할머니의 수명 하니까"
        stephan_think"처음엔 할아버지께서 어떻게해서 이렇게 큰 저택을 지을 수 있는 자금을 확보하셨는지 궁금했었는데, 이젠 알겠네"
        "예전부터 궁금했던 질문에 대한 답을 얻었음에도……{cps=2} {/cps}그리 기쁜 감정은 없었다."
        "난 예전부터 할아버지를 많이 존경했는데, 그런 존경대상의 과거를 보니까 적지않은 충격을 받게 됐다."
        "언제나 올바른 말씀만 하시고, 물질주의에서부터 가장 멀 것 같았던 존재의 반전된 과거……"
        stephan_think"하지만 지금까지 할아버지가 나에게 하셨던 말씀이 전부 자신의 경험을 통해서 나온 말이라면……"
        stephan_think"지금은 자신의 과거를 후회하고 있다는 뜻이겠지"
        "그렇게 생각하니 할아버지의 인생에 대해서 조금 씁쓸하게 느껴졌다."
        "일기장에서 할머니에게 프로포즈를 하기 전에 나한테 있어 외증조할아버지가 되는 사람이 말씀 하신대로……"
        "결국 할아버지는 자신의 선택에 대해서 후회했다는 뜻이니까"
        "하지만 이제막 할아버지가 프로포즈한 부분까지 읽었다."
        "본방은 지금부터라고 해도 과언이 아니겠지"
        play sound "se/search_bag.mp3"
        stop music
        scene bg ravine_grave_night at Zoom((1280,720),(585,256,695,390),(0,256,695,390),0.4)
        stephan"……?"
        "그때 사람의 기척이 느껴지자, 그 쪽으로 고개를 돌렸다."
        show grandpa talk with dissolve:
            zoom 1.5 xalign -0.3 yalign 0.0
        grandpa"스테반, 네가 여기에 있을 줄이야"
        "……할아버지가 조심스럽게 모습을 보이시면서 말씀하셨다."
        scene bg ravine_grave_night
        show stephan:
            zoom 1.7 xalign 0.5 yalign -0.5
        stephan"오늘은 하루종일 서재에서 일기장만 읽었더니, 몸이 뻐근해져 잠깐 바람 좀 쐐러 왔어요"
        grandpa"그랬구나"
        grandpa"젊은게 몸 조심하거라"
        show stephan talk
        stephan"할아버지는 그……{cps=2} {/cps}여기 할머니 때문에 오신거죠?"
        scene bg ravine_grave_night:
            size(1280,720)
            crop(0,256,695,390)
        show grandpa talk:
            zoom 1.5 xalign -0.3 yalign 0.0
        grandpa"뭐어…… 그런게지"
        scene bg ravine_grave_night at Zoom((1280,720),(0,256,695,390),(0,0,1280,720),0,5) with dissolve
        $ renpy.pause(0.5)
        show stephan talk with dissolve:
            zoom 1.7 xalign -0.3 yalign 0.0
        play sound "se/footsteps_concrete.mp3"
        show grandpa think:
            zoom 1.7 xalign -1.5 yalign -0.2
            linear 0.4 xalign 0.9
        "할아버지께서 묘비 근처로 다가가셨다."
        "그리고 기도하는 자세를 취하시면서 나에게 말씀 하셨다."
        grandpa"메리는……{cps=2} {/cps}내가 이렇게 기도 하는 걸 별로 좋아하지 않았지……"
        grandpa"기도라는 건 사람에게 \'난 무언가를 했다\'라는 착각을 심어준다면서……"
        stephan"그럼 지금은 왜 기도 하시는거예요?"
        grandpa"습관이라는 게 쉽게 고쳐지는 게 아니니까"
        grandpa"아무리 오랜 시간이 지난다고 해도, 누군가가 그걸 제제해주는 사람이 없으면 나도모르게 다시 반복하게 된단다"
        play sound "se/search_bag.mp3"
        show grandpa with dissolve
        "이번에 할아버지는 기도하던 사세를 풀고는 나를 바라보시면서 말씀 하셨다."
        grandpa"스테반, 넌 기도하는 것에 대해서 어떻게 생각하느냐?"
        show stephan shock
        stephan"이거 무슨 함정문제 인가요?"
        grandpa"그럴리가"
        grandpa"그냥 궁금해서 물어보는게야"
        extend". 세상엔 많은 의견이 있으니까"
        show stephan think
        stephan"흠……"
        stephan"전 솔직히 할아버지가 기도 하시는 거거엔 별로 아무생각 없어요"
        stephan"할아버지가 말슴하신대로 \'세상엔 많은 의견\'이 있는 것 처럼, 기도도 하나의 의견이라고 볼 수 있는거잖아요?"
        grandpa"음음 좋은 대답이구나"
        
        
        
        
        
        
        
    
    else:
        scene bg mansion_hall_night with memory
        centered"오후 6시 26분"
        scene bg mansion_hall_night with dissolve:
            size(1280,720)
            crop(432,118,415,233)
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return
    stop music
    scene black with dissolve
    "나는 방으로 들어가 잠을 취했다."
    jump chapter_3_2