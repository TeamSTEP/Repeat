##############################################################################################
###################################챕터1: 다시 시작하는 첫 만남############################################
##############################################################################################
label chapter1:
    $ save_name = "1.다시 시작하는 첫 만남"
    scene chapter1 with moveright
    $ renpy.pause(2)
    stop music
    scene black with moveright
    centered"오랜 시간 후"
    centered"할아버지의 저택 앞"
    #저택앞 백그라운드
    scene bg grandpa_mansion with dissolve
    play bgs"bgs/birds.mp3"
    play music "bgm/smooth1.mp3"
    "내 눈앞엔─내가 아주 오래전부터 알고 있었던 저택의 풍경이 펼쳐졌다."
    "……내가 기억하던대로 더럽게 높은 산 위에 있었다."
    "올때마다 얼마나 힘든지……"
    "어렸을땐 몰랐지만─지금 생각해보니까 아마 땅값이 싸서 여기에다 집을 지은 것 같다."
    "분명 그렇겠지"
    "그렇다곤 해도, 애초에 이렇게나 큰 저택을 짓는데 사용한 돈은 어떻게 손에 넣으셨는지는 조금 궁금했다."
    "한때 할아버지가 회사에서 높은 자리에 있었다는 소리를 들은 것 같기도 하지만……"
    "허나, 할아버지는 어렸을때 학교를 다니지 못했다고 들은적이 있었다."
    "그럼 어떻게 해서 이런 저택을 손에 넣으신거지……"
    play sound "se/footsteps_concrete.mp3"
    scene bg grandpa_mansion at Zoom((1280,720), (0,0,1280,720),(488,275,304,171),2.5)
    $ renpy.pause(2.8)
    "나는 다가가서 대문을 두드렸다."
    play sound "se/door_knock.mp3"
    $ renpy.pause(2)
    scene bg grandpa_mansion at Zoom((1280,720), (0,0,1280,720),(488,275,304,171),0)
    play sound "se/door_open.ogg"
    $ renpy.pause(1)
    show cia with dissolve:
        zoom 1.3 yalign -0.5 xalign 0.5
    stephan"어?"
    "그런데 내 예상과는 다른 사람이 문을 열었다."
    stephan_think"이상하네……"
    "눈 앞에 서있는 사람은 내가 한번도 본적이 없는 여성"
    "그리고 이곳은 분명 할아버지의 저택 일텐데……"
    stephan_think"호, 혹시 할아버지가 저택을 다른 사람한테 파셨나?"
    scene bg grandpa_mansion at Zoom((1280,720),(0,0,1280,720),(420,236,439,247),0.0)
    show stephan shock2:
        zoom 1.5 xalign -2.0 yalign -0.2
        linear 1.0 xalign 0.0
    show cia:
        zoom 1.4 xalign 1.0 yalign -1.0
    stephan"저, 저기……{cps=2} {/cps}혹시 여기가……"
    show stephan shock2
    $ cia_name = '처음 보는 여성'
    cia"스테반 토머 도련님 이신가요?!"
    stephan"도련님……?"
    "처음 보는 여성은 나를 \'도련님\'이라 불렀다."
    show stephan blush
    "……조, 조금 기분이 좋았다."
    stephan"제 이름이 스테반 토머인 건 맞습니다만……"
    stephan"댁은 누구신지……?"
    show cia shine
    cia"우와!{cps=2} {/cps}정말 할아버님이 말씀하신데로 빨간 머리를 가지고 있네요!"
    stephan"으, 음……"
    show cia shine:
        linear 0.5 xalign 0.5
    "그때 갑자기 그녀는 나의 머리카락을 만지려고 다가갔다."
    show stephan shock
    stephan"에헴"
    show stephan shock2
    stephan"여기가 \'에드워드 토머(Edward Tomer)\'댁이 맞는건가요?"
    show cia smile:
        linear 0.5 xalign 1.0
    cia"그렇습니다!"
    cia"그리고 도련님에 대해선 할아버님 한테서 자주 들었어요!"
    show stephan smile
    stephan_think"휴~{cps=2} {/cps}다행히도 집을 잘못 찾은 건 아니었군"
    show cia
    cia"지금 할아버님께서 기다리고 계실테니 안으로 들어오세요"
    show stephan shock
    stephan"저어……{cps=2} {/cps}근데 누구시죠?"
    show cia shock
    cia"아!"
    cia"이거이거 실례 했습니다"
    show cia smile
    $ cia_name = '시아'
    cia"절 그냥 편하게 \'시아(Cia)\'라고 불러주세요!"
    stephan"시아?{cps=2} {/cps}조금 특이한 이름 이네요"
    cia"이름이 아니라 별명 이에요~"
    cia"제 이름은 보통 사람들에겐 발음 하기 힘들거든요"
    cia"그리고 전 이곳에서 가정부+얹혀살고있는 몸이에요!"
    cia"그러니까 편하게 대하셔도 괜찮습니닷!"
    show stephan shock
    stephan_think"얹혀살고있다고?!"
    cia"그럼 얼른 안으로 들어오세요"
    $ know_seb = False
    play sound "se/footsteps_concrete.mp3"
    scene black with fade
    stop bgs
    "나는 \'시아\'라고 하는 사람의 밝은 태도에 이끌려서 저택 안으로 발길을 옮기게 됐다."
    scene bg mansion_hall with Dissolve(1.0)
    "저택 내부는 5년이 지나도 크게 바뀐게 없었다."
    show bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(761,41,420,236),0.5)
    "아니지, 저기 있는 HDTV는 처음 보는 물건이다."
    stephan_think"내가 저번에 있었을땐 구식 CRT 브라운관이었는데, 새로 사셨나보네"
    show bg mansion_hall at Zoom((1280,720),(761,41,420,236),(234,234,770,433),0.5)
    $ renpy.pause(0.5)
    show stephan shock2 at left
    show cia at right
    cia"할아버님은 2층 침실에 계실거예요!"
    hide cia
    hide stephan
    menu:
        "시아에 대해서 물어본다.":
            show stephan shock2 at left
            show cia think at right
            stephan"…………"
            cia"저한테 뭔가 하실 말씀 이라도 있나요?"
            stephan"제가 시아 씨에 대해선 전혀 아는 게 없어서요……"
            stephan"이, 이곳에선 언제부터 일 하기 시작 하셨어요?"
            cia"몇 년이 지났더라……?"
            show cia smile at right
            cia"까먹었어요!"
            show cia at right
            cia"그래도 몇 년동안 있었던 건 확실해요"
            stephan"그, 그렇군요"
            stephan"근데 이런 다 낡아 빠진 저택에서 어쩌다가 일을 하게 됐어요?"
            stephan"혹시 할아버지가 고용 하신건가요?"
            "하지만 우리 할아버지는 저택에 남을 막 들일만 한 사람은 아닌걸로 기억한다."
            show cia think at right
            cia"그게, 사실 전 여기에 공식적인 가정부는 아니에요"
            cia"일단은 여기서 얹혀살고 있는 몸이니까……"
            stephan"그, 그건 또 무슨 뜻이에요……?"
            stephan_think"입구에서도 그런 말을 했었지"
            cia"흠……{cps=2} {/cps}이걸 짧게 설명 하면……"
            show cia smile at right
            cia"제가 인생의 길을 잃었는데 할아버님이 저를 줏어다가 키워 주셨어요!"
            show stephan shock
            stephan"음?!"
            show cia think
            cia"아니지, 그건 뭔가 아닌거 같고……"
            show cia
            cia"쉽게 말해서……{cps=2} {/cps}할아버님은 갈 길을 잃은 저를 보살펴 주셨어요……"
            cia"하루 세끼 먹기 힘들었고, 당연히 집도 없었고……{cps=2} {/cps}그때 저에게 이렇게 넓은 저택에서 생활 할 수 있게 해주시고"
            cia"그 친절함에 조금이라도 보답하기 위해서 집안 일 만큼은 제가 하기로 했어요!"
            $ know_seb = True
            show cia talk at right
            cia"다만 제가 일하는 게 많이 어설퍼서 아직은 세바스찬에게 배우는 중이지만요……"
            stephan"세바스찬?"
            show cia smile at right
            cia"네!{cps=2} {/cps}여기서 같이 일을 하는 제 후배 가정부예요!"
            cia"어찌나 요리를 잘하던지~"
            cia"물론 저랑 다르게 그 사람은 공식적으로 급여를 받으면서 일을 하다 보니까 출퇴근 시간이 있어요"
            show cia think at right
            cia"24시간 할아버님 곁에 있어줄 순 없는 걸 제외하곤 뭐든지 저보다 뛰어나서……"
            show cia shock at right
            cia"그,{cps=2} {/cps}그래도! 최근엔 제가 받은 돈으로 할아버님께 선물을 해드린적도 있어요!"
            show cia smile at right
            cia"할아버님은 항상 2G폰만 사용하시길래 최신걸로 바꿔 드렸죠!"
            stephan_think"아…… "
            extend"그래서 할아버지가 어제 그런 말을……"
            play sound "se/shock.ogg"
            show effect1
            show stephan shock at left
            stephan_think"{size=45}그보다 이 사람 엄청나게 기특해!{/size}" with lshake
            stephan_think"{size=45}친 손자인 나보다 더!{/size}"
            hide effect1
            show cia shock
            cia"엇!{cps=2} {/cps}오늘 하는 예능 놓치겠다!"
            show cia smile
            cia"그럼 전 잠시 실례 할게요"
            stephan"ㄴ, 네……"
            "나도 할아버지한테 가봐야겠다."
            jump bedroom
        
        "2층 침실로 이동한다.":
            jump bedroom

label bedroom:
    scene bg mansion_hall at Zoom((1280,720),(234,234,770,433),(0,0,600,338),1.0)
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(1.0)
    scene black with dissolve
    $ renpy.pause(2)
    stop music
    play sound "se/door_open.ogg"
    "나는 침실 방문을 열어서 들어갔다."
    "방문을 여는순간 지독한 약품 냄새가 내 코를 찔렀다."
    "왠지 모르게 안좋은 예감이 들었다."
    play music "bgm/sad2.mp3"
    scene ev grandpa_bed at Zoom((1280,720),(0,0,1280,720),(107,238,727,409),0.0) with dissolve #할아버지가 침대위에 누워있는 일러스트
    "할아버지가 침대에 누워 계셨다."
    "하지만 할아버지의 모습이 내가 알 던 모습이랑은 조금 달랐다."
    "내가 마지막으로 봤을때보다 더 말라있으셨고, 주름도 많아지셨고……"
    "어제 통화 했을때랑은 전혀 다르게, 움직이는것 조차 힘들어 보이셨다."
    show ev grandpa_bed at Zoom((1280,720),(107,238,727,409),(0,0,1280,720),0.6)
    $ renpy.pause(0.6)
    show grandpa_bed2 with dissolve
    stephan"할아버지!"
    grandpa"왔느냐……{cps=2} {/cps}스테반……"
    "할아버지의 목소리가 많이 갈라지셨다."
    stephan"할아버지 무슨 일있으셨어요?{cps=2} {/cps}갑자기 폭삭 늙으신거 같은데……"
    grandpa"무슨 소리냐!"
    extend" 난 아직 건강하다고!"
    stephan"하지만 팔도 다리도 이렇게 가늘어 지셨고……"
    grandpa"허허……{cps=2} {/cps}너도 내 나이가 되면 이렇게 될게야"
    $ renpy.vibrate(0.5)
    grandpa"콜록{cps=2} {/cps}콜록" with sshake
    stephan"기침까지 하시는데 정말 괜찮은거 맞아요?"
    grandpa"이건 그냥 사례가들린 것 뿐이니까 너무 호들갑 떨지 말거라"
    stephan"정말 그거 뿐이라면 안심이지만……"
    grandpa"내 걱정은 그만 하고,{cps=2} {/cps}네 얘기가 듣고 싶구나, 스테반"
    stephan"제 얘기요……?"
    stephan"제가 딱히 해드릴 말씀이 있을련지……"
    grandpa"그럼……{cps=2} {/cps}탐정 일은 어떻게 돼 가고 있느냐?"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}타타타타 탐정?!{/size}" with lshake
    stephan_think"오자마자 돌직구를?!"
    hide effect1
    grandpa"그래……{cps=2} {/cps}그때 분명 네가 되고 싶다고 하지 않았느냐"
    "할아버지께선 마치 과거의 나를 보고 있듯이 매우 순수한 눈빛을 하고 계셨다."
    stephan_think"이걸 어떻게 말해야지……?"
    stephan"음……"
    stephan"할아버지,{cps=2} {/cps}저 이거 돌려드리고 싶어요……"
    play sound "se/search_bag.mp3"
    scene black with dissolve
    show ev book:
        xalign 0.5 yalign 0.5 zoom 2.0
    "나는 집에서 챙겨 온 \'탐정의 서\'를 할아버지에게 건냈다."
    scene ev grandpa_bed
    show grandpa_bed2
    grandpa"이 책은……{cps=2} {/cps}아직도 이렇게나 무사하게 있어……!"
    grandpa"혹시 다 읽은거니?!"
    stephan"대충 읽긴 했지만……"
    stephan"그보다 제가 이 책을 반납하는 이유는 그거 때문이 아니에요"
    grandpa"그럼 뭐가 문제인게냐……?{cps=2} {/cps}이건 너희 할머니가 쓴……"
    stephan"저도 들었어요"
    stephan"그냥……{cps=2} {/cps}이 책을 제가 계속 가지고 있을 필요가 없을거 같아서요……"
    grandpa"왜……?"
    "이 책이 나한테 필요하지 않은 이유는 몇 가지 있다."
    "일단 첫째, 내가 탐정이라는 말도 안 되는 꿈에서 졸업 했기 때문에"
    "그럼에도 집에 꽃혀있는 이 책을 볼때마다 계속 그때 했던말이 떠올라서 죽고싶어진다."
    "두번째는……{cps=2} {/cps}이 책의 내용이 너무 엉망진창이다."
    "할아버지께서, 이 책은 할머니가 젊었을때 만드셨다고 하셨는데……"
    "도대체 썼을 당시 무슨 일이 있었길래……{cps=2} {/cps}내용이 매우 복잡하다."
    "무엇보다 제목에 써져있는 \'탐정\'과는 아무런 관계가 없다."
    "대신 이 책에서는 \'진리\'라는 컨셉에 대해서 다루는 일종의 철학 논문 같은거다."
    "어렸을땐 탐정에 대해서 관심이 있었지만, 철학엔 전혀 흥미가 없었는지라 도움이 안 됐다."
    "허나 저 책을 나에게 주던 할아버지의 모습이 어찌나 기뻐 보였던지……{cps=2} {/cps}그 마음을 짚밟고 싶진 않았다."
    stephan_think"이 상황을 어떻게 해야……"
    stephan"그……{cps=2} {/cps}제가 어렸을때 탐정이 되고 싶다고 했잖아요?"
    grandpa"그랬지……{cps=2} {/cps}아마"
    stephan"그때 제가 어떻게 해서 그런 꿈이 생겼는지 아시죠?"
    grandpa"기억이 날 것 같기도 하고……"
    "나에겐 매우 선명하게 기억났다."
    "……물론 선명해봤자 내가 본 것 까지만 이다."
    play sound "se/think.mp3"
    stop music
    scene black with flash
    play bgs"bgs/birds.mp3"
    scene ev tv_barney with memory
    $ extra_name = 'TV'
    extra"아이 러뷰~{cps=2} {/cps}유 럽 미~"
    "때는 내가 막 초6 이었을때."
    "당시 나는 남들에 비해 정신연령이 낮았던건지, 어린이 방송을 즐겨봤다."
    "그, 그래도 그땐 어렸기 때문에 지금와 서봐도 크게 흑역사 취급 하진 않는다."
    "나의 진짜 흑역사는 이 이후에 발생했으니까"
    play sound "se/static.mp3"
    scene ev tv_red
    stephan"어?{cps=2} {/cps}할아버지!{cps=2} {/cps}티비 고장났어요!"
    grandpa"그럴리가……{cps=2} {/cps}얼마 전에 고쳤는데……"
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(2.4)
    grandpa"어이고……{cps=2} {/cps}이게 왜 이러지……"
    "그때 텔레비전에선 높은 피치로 음성 변조 된 누군가가 말을 했다."
    extra"안녕하세요.{cps=2} {/cps}여러분들"
    play music "bgm/sirius4.mp3"
    extend", 제 이름은 \'레드(ReD)\'라고 합니다"
    extra"그리고 방금까지 보고 계셨던 방송을 잠시 중단 시킨것에 대하여 진심으로 사죄의 말씀을 드리겠습니다"
    extra"하지만 지난 목요일 오후 5시에 \'몰턴 은행\'에서 발생한 은행 강도 사건에 대해서 상세히 알고 싶으신 분은 귀 기울여서 들어주셨으면 합니다"
    extra"……전 그 용의자 4명의 위치를 전부 알고 있습니다"
    stephan"……?"
    "\'몰턴 은행 강도 사건\'이라고 당시 꽤나 시끄러웠던 대형 은행털이 사건이 있었다."
    "용의자는 총 4명으로 엄청나게 용의주도했는데……"
    "사전에 미리 도주 경로를 준비 하고, 도주 차량의 번호판을 가짜로 바꿔쳐서 경찰들의 수색망을 어지럽히는 등 완전 영화에 나올법 한 수법이었다."
    "그렇게 훔치는데 성공한 금액이 현금으로 약 9억 달러라고 한다."
    extra"현재 3명은 ***번지에 있는 금빛 빌라 302호에 몸을 숨기고 있고, 나머지 한명은 훔친 금액의 20\%를 소지 한 채로 오리엔스 국제 공항에 있습니다"
    extra"공항쪽은 벌써 손을 써놨으니 지금으로부터 약 4시간 까지 즉, 오후 6시 까지 도착 한다면 잡을 수 있을겁니다"
    stephan"우와!{cps=2} {/cps}할아버지, 저거 완전 명탐정 아니에요?!"
    grandpa"명탐정이라……{cps=2} {/cps}확실히 대단한 사람 같구나……"
    stephan"저거 정말 멋있어요!"
    stephan"뭔가 애니에 나올법한게……"
    grandpa"탐정 이라……"
    grandpa"스테반……{cps=2} {/cps}혹시 너도 저렇게 되고 싶니?"
    stephan"가능 해요?!"
    grandpa"당연하지.{cps=2} {/cps}마침 이 할애비가 좋은 책을 가지고 있는데, 너한테 줄게"
    stephan"정말요?!"
    grandpa"그럼!"
    extend" 할아버지를 따라 오거라"
    stephan"네!"
    stop music
    stop bgs
    scene black with Dissolve(1.5)
    show ev book:
        alpha 0.0 xalign 0.5 yalign 0.5
        linear 0.3 alpha 0.5
    "그리고 이때 할아버지께서 나에게 \'탐정의 서\'를 주셨다."
    "할머니가 젊었을때 쓰신 일종의 탐정 비법서 같은거라고 하셨는데……"
    "처음엔 전부 어려운 말 투성이라서 하나도 이해하지 못했다."
    show ev dic_stephan:
        xalign 0.0 yalign 0.0 alpha 0.0
        linear 0.6 alpha 1.0
    "그럼에도 난 그 날 이후로부터 스스로를 \'명탐정 스테반\'이라고 자칭 했다."
    "책을 가지고 있는 것 만으로도 그 지식이 머리속에 들어왔다고 착각 하고 있었던거다."
    "하지만 지금와서 생각해보니까 당시 내가 탐정의 꿈을 가지게 된게 정말 당연하게 느껴지기도 한다."
    "티비에서 갑자기 레드라고 하는 전설적인 존재가 나와서 그런 발언을 했다면 누구나 잠깐은 열정에 타 올랐을테니"
    "그저 나에게 문제가 되는 것은 내가 탐정을 자칭하고 다니면서 했던 행동들이다……!"
    "정말 그땐 내가 뇌가 없었던건지, 엄청나게 쪽팔리는 짓을 많이 했다."
    show ev dic_stephan:
        linear 1.0 alpha 0.0
    "지, 진정하자……"
    "그때의 일을 떠올리는 건 정신건강에 좋지가 않다."
    "과거는 과거, 난 지금을 살고있다."
    "\'명탐정 스테반\' 때문에 나에게 PTSD가 생겼지만 그건 시간이 해결해준다."
    "……하지만 나에겐 아직도 궁금한게 있다."
    show ev book:
        alpha 0.0 xalign 0.5 yalign 0.5 zoom 2.0
        linear 0.5 alpha 0.5
    "\'탐정의 서\'는 무슨 책인가?"
    "할아버지께선 탐정의 비법서 같은거라고 말씀 하셨지만, 실제론 전혀 그렇지가 않다."
    "뭔가 많이 복잡하고……{cps=2} {/cps}\'진리\'라는 철학적인 걸 서술하는 일종의 논문 같은거였다."
    "뭐가 어쨌건, 일단 난 이 책을 할아버지께 반납하러 온거지, 궁금증을 해결하러 온게 아니다."
    scene ev grandpa_bed at Zoom((1280,720),(0,0,1280,720),(107,238,727,409),0.0) with memory #할아버지가 침대위에 누워있고 링겔 여러개가 할아버지의 왼손에 연결되어 있는 일러스트
    show grandpa_bed2 at Zoom((1280,720),(0,0,1280,720),(107,238,727,409),0.0)
    $ grandpa_body = 'normal'
    $ grandpa_glasses = 'normal'
    stephan"할아버지……"
    extend" 저, 더이상 탐정이 되고 싶지가 않아요"
    scene bg mansion_bedroom at Zoom((1280,720),(0,0,1280,720),(149,113,596,336),0.0) with Dissolve(1.0)
    play sound "se/search_bag.mp3"
    show grandpa talk:
        zoom 1.8 xalign 0.4 yalign -2.0
        linear 1.0 yalign -0.2
    "할아버지는 침대 위에 앉아서 말을 이엇다."
    grandpa"되기……{cps=2} {/cps}싫다고?"
    stephan"네"
    play music "bgm/sad2.mp3"
    grandpa"이거……{cps=2} {/cps}조금 슬프구나……"
    stephan"……예?"
    "할아버지께서 갑자기 우울한 기분이 되셨다."
    grandpa"스테반……{cps=2} {/cps}너도 이렇게 내 곁을 떠나는 게냐……?"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}가,{cps=2} {/cps}갑자기 무슨 소리를 하시는거예요?!{/size}" with lshake
    hide effect1
    grandpa"하지만……{cps=2} {/cps}이제 더이상 탐정이 되고 싶지 않다고……"
    stephan"더 좋은 꿈을 찾아서 그런거예요!"
    stephan"탐정 따위 보다 더 좋고, 자신에게 당당해 질 수 있는 꿈을……!"
    stephan"그, 그래서 이 책을 반납하고 싶은거예요"
    stephan"과거의 미련을 버리고 싶은거랄까……"
    show grandpa
    grandpa"허허허……{cps=2} {/cps}이거, 내가 늙으니까 원……"
    grandpa"그냥 점점 변화 라는것에 예민해지는 거 같구나……"
    stephan"죄송해요……{cps=2} {/cps}할아버지……"
    grandpa"왜 네가 사과를 하는 게냐?"
    grandpa"더 좋은 꿈을 찾았다면 그걸로 된게지"
    grandpa"……그래서, 그 새로운 꿈이 어떤 게냐?"
    play music "bgm/happy2.mp3"
    stephan"\'류인 그룹\'에 취직 해볼까 생각 중이에요!"
    show grandpa think
    grandpa"류인 그룹?"
    stephan"네,{cps=2} {/cps}그 전자 기기 만들고, 자동차도 만드는 대기업 있잖아요"
    "참고로, 요즘 류인에선 그거 뿐만 아니라 식품, 보험, 옷, 건설 등 왠만한거에 다 손 대고 있다."
    stephan"대학교만 잘 다니면 입사 가능할 거 같더라고요!"
    grandpa"\'류인 그룹\'이라……{cps=2} {/cps}어디서 많이 들어본 듯 한데……"
    stephan"그래요?"
    stephan"아마 TV에서 한번쯤 들어 보셨을거예요"
    stephan"우리나라에서 가장 큰 회사니까요"
    grandpa"그럴 수도 있겠지만……{cps=2} {/cps}뭔가 다른데서 들었던거 같기도……"
    stephan"흠?"
    show grandpa
    grandpa"근데 그 회사에 취직하고 싶은 이유가 따로 있는 게냐?"
    stephan"이유라……"
    stephan"제가 가고 싶었던 대학이 류인 그룹에서 만든거라고 하더라고요"
    stephan"확실히 대학교 졸업 후엔 뭘로 먹고 살지 고민 중이었는데, 성적만 잘 나온다면 류인 그룹에 바로 취직할 수 있다길래 한번 도전 해보려고요"
    grandpa"……정말 그걸로 만족 하니?"
    stephan"네?{cps=2} {/cps}만족 이라니……"
    stephan"그 회사에 취직하면 거의 평생을 편하게 보낼 수 있는 걸요?"
    stephan"돈도 많지, 시설도 좋지, 하는 일도 제 관심 분야에서 그리 멀지도 않지……"
    stephan"이건 완전 기회 잖아요!"
    show grandpa talk
    grandpa"그래……"
    grandpa"확실히 너한텐 기회 일 수도 있겠구나……"
    grandpa"근데 참……{cps=2} {/cps}살다 살다 내가 이런 말을 하게 될줄은 몰랐지만……"
    grandpa"수익만을 쫓다보면……{cps=2} {/cps}중요한걸 놓치게 될때가 있어……"
    grandpa"그 회사에 들어가고 싶은 목적이 \'편하게 살기 위해서\'인지, \'행복하게 살고 싶어서\'인지 확실히 구분 해두는 게 좋아"
    stephan"근데 편하게 사는 게 행복한거 아닌가요?"
    grandpa"내가 살다 보니까 좀 다르더라고……"
    show grandpa
    grandpa"어쨌건, 그 탐정의 서가 이제 필요 없다면 할아버지에게 주거라"
    grandpa"그리고 다시 필요해지면 언제든지 찾아오거라"
    stephan"네"
    grandpa"그나저나 네 생활은 요즘 어떻고?{cps=2} {/cps}돈은 필요하지 않든?"
    stephan"돈 이라면 괜찮아요!{cps=2} {/cps}딱히 밖에 나갈 일도 없어서 그닥 필요 없는 걸요?"
    grandpa"그래……?{cps=2} {/cps}그럼 지금 살고 있는 집은 어떻고?"
    grandpa"내가 네 엄마 한테 듣기론 혼자 살고 있다는 거 같던데……"
    stephan"뭐어……{cps=2} {/cps}그렇죠"
    stephan"솔직히 처음엔 혼자 사는 게 좋은 줄 알았는데, 계속 있다보니까 너무 외롭다고 해야 할까……"
    grandpa"그럼 오늘부턴 자주 놀러 오거라"
    grandpa"할아버지는 언제든지 환영 이니까"
    stephan"넵!"
    stephan"아!{cps=2} {/cps}저 한가지 좋은 소식이 있어요!"
    stephan"저번에 본 기말고사에서 제가 전교 90등을 했어요!"
    grandpa"그거 정말 장하구나"
    stephan"후훗"
    stephan"그쵸?{cps=2} {/cps}453명 중에서 90등이면 제가 생각해도 정말 잘한거 같아요"
    stephan_think"뭐, 윌리의 넘사벽 1등 만큼은 아니지만;;"
    grandpa"요즘 부모님은 잘 계시고?"
    stephan"엄마는 아직도 외국에서 공부 중이라서 가끔 오는 연락으로 밖에 소식을 접 할 수가 없지만……"
    stephan"그래도 보니까 재밌게 살고 있는거 같아요"
    grandpa"그렇구나……"
    grandpa"그럼 스테반은 지금 집에서 혼자 살고 있는 게냐?"
    stephan"네……?"
    stephan"방금 전에 제가 혼자서 살고 있다고 말씀 드렸던걸로……"
    show grandpa shock
    grandpa"아,{cps=2} {/cps}아―"
    extend" 그랬었지……"
    show grandpa talk
    stop music
    grandpa"……그럼 헨릭은 요즘 잘 지내고 있는지?"
    stephan"…………"
    grandpa"스테반……?"
    "\'헨릭 토머(Henrik Tomer)\'"
    play music "bgm/sad4.mp3"
    extend" 나의 아버지다."
    stephan"그 사람이 어디 있는지 제가 어떻게 알겠어요"
    stephan"멋대로 나가서 멋대로 연락이 끊기고……"
    show grandpa shock
    grandpa"둘 사이에 무슨 일 있었어……?"
    stephan"혹시 기억 안나세요?"
    stephan"5년 전에 제가 할아버지 댁에서 생활 하게 된 이유가……"
    grandpa"그, 그랬구나!"
    grandpa"이거……{cps=2} {/cps}늙으니까 기억이 좀 가물가물 해져서……"
    grandpa"혹시 다시 말 해줄 수 있겠니?"
    stephan"…………"
    stephan"아빠가……{cps=2} {/cps}엄마랑 이혼을 하면서……"
    stephan"엄마는 해외에 있는 대학원으로 유학을 가고……{cps=2} {/cps}제가 엄마 따라서 외국에 가기 싫다고 하니까 어쩔 수 없이 할아버지 댁에 맡겨졌고……"
    grandpa"그랬지……"
    grandpa"그런데 네가 헨릭이랑 우너래부터 잘 안 어울렸던가?"
    grandpa"언제부터 그렇게 사이가 틀어진게냐?"
    play bgs "se/static.mp3"
    show image "static" onlayer texture
    show black:
        alpha 0.0
        linear 1.0 alpha 1.0
    "헨릭이 처음부터 나쁜 아빠는 아니었다."
    "엄청 똑똑하고, 자상하고, 능력도 있었기 때문에 내가 사고 싶었더 건 왠만하면 다 사줬고……"
    "매우 존경할만한 사람이었다."
    show ev sky_night:
        alpha 0.0
        linear 0.5 alpha 1.0
    "그 중에서 매일 밤, 다니던 초등학교 뒷산에서 돋자리를 깔고 별 관측을 했던게 기억에 가장 많이 남았다."
    "벌레에 물려가면서도 매일 밤 같은 자리에 누워서 별을 보고……{cps=2} {/cps}헨릭은 나한테 별자리에 얽힌 이야기를 들려주고……"
    $ extra_name = '아빠'
    extra"스테반, 아빠 네 생일 선물로 천체 망원경 사줄까?"
    "그게 내가 자랑스럽게 아빠라고 부를 수 있었던 남자의 마지막 목소리였다."
    hide ev sky_night
    "그 이후로 헨릭은 집에 자주 들어오지 않게 됐고, 어투가 뭔가 거칠어지면서 조급하게 들렸다."
    "얼마 안 가서 엄마랑 이혼하고, 우리 가족은 뿔뿔이 흩어지게 됐다."
    "당시 내가 너무 어렸던 것도 있었지만……{cps=2} {/cps}지금도 왜 그렇게 됐는지 전혀 모른다."
    hide black with Dissolve(1.0)
    hide image "static" onlayer texture
    stop bgs
    stephan"그냥……{cps=2} {/cps}언제부턴가 서먹서먹한 사이가 돼버렸어요"
    stephan"거기다 7년 가까이 연락 두절 상태니까 그냥 원망스러워지고, 이젠 관심조차 없어진 거 뿐이죠……"
    stephan"아니면 그냥 제가 사춘기 이거나……"
    grandpa"흠……"
    extend" 스테반"
    stephan"네?"
    grandpa"주제를 좀 바꿀 겸……{cps=2} {/cps}저기 책상에 있는 서랍의 첫번째 칸을 한번 열어 줄 수 있겠니……?"
    grandpa"안에 보면 노트 조각이 있을게야"
    play sound "se/footsteps_wood.mp3"
    scene bg mansion_bedroom at Zoom((1280,720),(0,0,1280,720),(800,267,480,270),2.3) with moveright
    $ renpy.pause(2.5)
    play sound "se/door_open2.ogg"
    "나는 할아버지가 시키신데로 서랍을 열어 보았다."
    "확실히 안에 낡은 노트 조각이 있었다."
    stephan"혹시 이건가요……?"
    grandpa"그래……{cps=2} {/cps}한번 읽어보거라"
    play sound "se/book_page.ogg"
    scene black with dissolve
    scene ev note at Zoom((1280,720),(0,0,1280,720),(0,0,1280,720),0.0)
    show letter1 at Zoom((1280,720),(0,0,1280,720),(0,0,1280,720),0.0)
    show black
    hide black with Dissolve(1.0)
    play sound "se/think.mp3"
    show ev note at Zoom((1280,720),(213,70,453,255),(213,70,453,255),0.0)
    show letter1 at Zoom((1280,720),(213,70,453,255),(213,70,453,255),0.0) with flash
    show ev note at Zoom((1280,720),(213,70,453,255),(690,70,453,255),1.0)
    show letter1 at Zoom((1280,720),(213,70,453,255),(690,70,453,255),1.0)
    $ renpy.pause(1.0)
    show ev note at Zoom((1280,720),(690,70,453,255),(0,0,1280,720),0.3)
    show letter1 at Zoom((1280,720),(690,70,453,255),(0,0,1280,720),0.3) with flash
    stephan"…………"
    "필체가 조금 불안정 했다."
    "혹시 이걸 쓰던 당시에 머릿속이 복잡 했던걸까……"
    "내용은 다음과 같았다."
    narrator_nvl"에드워드"
    narrator_nvl"나는 예전부터 당신을 좋아했고, 앞으로도 좋아할거야."
    narrator_nvl"하지만 당신을 기억하고 있는 사람은 나 뿐인 거 같아."
    narrator_nvl"내가 사랑하는 에드워드를."
    narrator_nvl"아마 당신은─지금 이 편지에 대해서 많이 이상하게 보고 있겠지."
    narrator_nvl"하지만, 때가 될때: 내가 무슨 말을 하려는지 알게 될거야."
    nvl clear
    narrator_nvl"나를 떠올려줘."
    narrator_nvl"내가 쓰고있는 이 수수께끼의 정답을 알아줘."
    narrator_nvl"이전에 있었던 수수께끼를 풀었듯이."
    narrator_nvl"그리고 나를 떠올려줘."
    nvl clear
    stop music
    show ev note at Zoom((1280,720),(0,0,1280,720),(236,524,849,478),0.3)
    show letter1 at Zoom((1280,720),(0,0,1280,720),(236,524,849,478),0.3)
    narrator_nvl"\[내가 사랑하는 그대에게 소리로써 가르쳐 주고, 그대는 나에게 의미로써 보여주네\]"
    nvl clear
    play sound "se/book_page.ogg"
    scene bg mansion_bedroom at Zoom((1280,720),(0,0,1280,720),(800,267,480,270),0.0) with dissolve #할아버지의 방 배경
    show stephan talk:
        zoom 1.8 xalign 1.0 yalign 0.0
    stephan_think"…………"
    "나는 할 말을 잃었다."
    play sound "se/search_bag.mp3"
    show grandpa talk with dissolve:
        xalign -2.0 yalign -0.3 zoom 1.8
        linear 2.3 xalign 0.0
    grandpa"어이구 어이구……"
    "그때 할아버지는 침대에서 일어나서 다가왔다."
    grandpa"어떠냐……?"
    stephan"이게……{cps=2} {/cps}할아버지께서 말씀하신 \'퍼즐\'인가요?"
    grandpa"맞아……"
    "퍼즐 이라기보단 노트에 써진대로 수수께끼에 가까웠다."
    stephan_think"하지만……"
    "내용도 그렇고, 글씨체도 그렇고……"
    "이 노트엔 뭔가 큰 비밀이 있다는 게 느껴졌다."
    show stephan
    play music "bgm/smooth5.mp3"
    "……엄청나게 흥미로웠다."
    stephan"할아버지"
    grandpa"으응?"
    stephan"제가 풀어야 하는 게 여기에 써져있는 \'내가 사랑하는 그대에게 소리로써 가르치고 그대는 나에게 의미로서 가르치네\'의 뜻 인가요?"
    grandpa"아마도"
    show stephan shock
    stephan"아마도?"
    grandpa"나도 잘은 몰라서……"
    grandpa"하지만 거기엔 방금 말 한 걸 퍼즐로써 쓴거 같아"
    show stephan think
    stephan"흠……"
    show stephan talk
    stephan"혹시 할아버지는 이 노트에 대해서 뭔가 아시는거 없나요?"
    grandpa"어떤거면 되느냐?"
    stephan"아무거나요"
    stephan"발견 장소, 할머니가 처음 썼을때 당시 상황이라든가……"
    show grandpa think
    grandpa"흠……{cps=2} {/cps}글쎄……"
    grandpa"내 기억력이 많이 낡아서 도움이 될진 모르겠지만……"
    grandpa"아마 메리가 그 편지를 썼을때 이 저택을 리모델링 했던걸로 기억하는데……"
    grandpa"정확한 날짜나 년도는 기억이 안나는구나……"
    show stephan think
    stephan_think"저택의 리모델링 이라……"
    grandpa"또, 메리는 그 퍼즐 말고도 다른 것도 냈었던걸로 기억해……"
    grandpa"근데 전부 어떻게 됐는지 몰라"
    stephan_think"확실히 편지의 내용에서도 \'이전에 있었던 수수께끼\'라는 말이 들어갔어"
    stephan_think"퍼즐이 총 몇개 인진 모르겠지만, 적어도 2개 이상 이라는 뜻인가?"
    show grandpa cough
    $ renpy.vibrate(0.3)
    grandpa"콜록{cps=2} {/cps}콜록"
    show grandpa talk
    show stephan talk
    stephan"메리{cps=2} {/cps}……가 할머니의 성함 인가요?"
    grandpa"그래"
    grandpa"생각 해보니까 너한텐 할머니에 대해서 그렇게 알려준적이 없었구나"
    stephan"네……"
    stephan"제가 아는 거라곤…… 할머니가 이 탐정의 서를 썼다는 정도?"
    stephan"할머니는 어떤 분 이셨어요?"
    stephan"책을 쓴걸로 봤을땐─작가 이셨나요?"
    show grandpa think
    grandpa"작가라……"
    grandpa"한때 소설가를 꿈꿨다는 건 들어본적이 있구나"
    grandpa"하지만 그녀의 직업은 회사를 경영하는 사람이었어……"
    grandpa"그리고 나중엔 \'철학자\'였지"
    stephan_think"철학자……"
    "탐정의 서의 내용을 생각해보면, 할머니가 철학자셨다는 걸 어느정도 알 수 있었다."
    "하지만 할아버지의 말씀을 들어보니까─매우 베일에 쌓인 분 같았다."
    grandpa"메리……"
    grandpa"똑똑하고……{cps=2} {/cps}예뻤지……"
    grandpa"나같이 아무것도 없는 남자에겐 너무나도 아까운 여자 였어……"
    stop music
    grandpa"그런 여자가 그때 왜 나한테 관심을 보였는지 아직도 의문이야……"
    play music "bgm/sad4.mp3"
    grandpa"처음 만났을땐─내가 죽은 자기 친구와 닮았다고 하고……{cps=2} {/cps}나중엔 내가 그 죽은 친구라는 말도 안 돼는 소리를 하고……"
    grandpa"메리가 원래부터 평범한 사람과는 거리가 멀었지만, 결혼 후엔 점점 내가 이해할 수 없는 말과 행동을 하기 시작했지"
    grandpa"역시 아이를 한번 잃고 나서 정신적인 부담감이 컸었던게야……"
    show stephan shock
    stephan"할머니께서 아이를 잃으신적이 있었어요?!"
    grandpa"어……"
    grandpa"하지만……{cps=2} {/cps}그건 정말 어쩔 수 없었어……"
    grandpa"내가 그런 선택을 하지 않았더라면 메리가 죽었을지도 모르는 건데……"
    show grandpa mad
    show effect1
    play sound "se/shock.ogg"
    grandpa"{size=40}근데 나보고 어쩌라는거야!{/size}" with lshake
    hide effect1
    "할아버지께선 갑자기 눈물을 흘리며 혼잣말을 하기 시작했다."
    "그 떨리는 목소리를 듣는 나도 고통스러워졌다."
    grandpa"난 언제나 메리를 위해서 살아왔는데……"
    grandpa"메리의 모든 소원을 이루어 주겠다고 약속 했는데!"
    grandpa"근데……"
    show grandpa think
    extend" 그 마지막 소원 만큼은……{cps=2} {/cps}역시 힘들어……"
    show stephan talk
    stephan"할아버지……{cps=2} {/cps}그 마지막 소원의 내용……"
    stephan"혹시 이 퍼즐을 풀어 달라는 거 였어요?"
    grandpa"…………"
    grandpa"좀 더 정확히 말하자면……"
    grandpa"\'나를 혼자 두지 마……\'였어"
    grandpa"이 퍼즐은 그게 무슨 뜻 인지 알려 줄거라고만 했지……"
    show grandpa mad
    grandpa"하지만 모르겠다고!"
    grandpa"난 언제나 옆에서 있어줬는데"
    grandpa"그런데도 항상 혼자서 두지 말라고 하니까……{cps=2} {/cps}나로선 정말 힘들지……"
    stephan"그럼 할머니 께선 그 말씀을 하고 나서 이 편지를 쓰신건가요?"
    show grandpa think
    grandpa"맞아……"
    "이걸로 한가지 확실해진게 있다."
    "내 역할은 단순히 이 퍼즐의 정답을 찾는 게 아니라……"
    "할머니의 마지막 소원을 이뤄주는 것"
    stephan_think"하지만 그걸 위해선 먼저 이 상황에 대한 이해가 필요해"
    stephan"할머니가 이 편지를 쓰기 전에 뭔가 특이점 같은거라도 있었어요?"
    grandpa"특이점 이라면……"
    grandpa"언제부턴가 아주 어려운 말만 하기 시작했지……"
    grandpa"하지만 어떤 내용 이었는지 구체적으론 기억이 않나는구나"
    show stephan shock
    stephan_think"안돼,{cps=2} {/cps}뭔가 단서가 있어야 해"
    stephan_think"아주 작은거라도 좋으니까……"
    extend" 뭔가 할머니가 이런 편지를 쓰게 된……"
    stephan_think"아니, 그보다 훨씬 이전에,  \'나를 혼자 두지 마……\'라는 말을 하게 된 이유……"
    stephan"그래도 뭔가 기억에 남는 게 있을거 아니에요?"
    stephan"뭔가 좀……{cps=2} {/cps}할아버지한테 팟 와닿는 말 이라든가"
    grandpa"생각해보니까 한가지 이상한게 있었구나"
    show stephan
    stephan"뭐예요?"
    stop music
    grandpa"\'진리\'를 봤다고 했었지……"
    show stephan shock
    stephan_think"진리?!"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=40}진리를 봤다고 하셨다고요?!{/size}" with lshake
    hide effect1
    grandpa"그래"
    play music "bgs/space.mp3"
    stephan_think"할머니가……{cps=2} {/cps}진리를 봤다고?"
    "참고로 내가 할아버지께 받은 —그리고 할머니가 쓴— 탐정의 서의 내용이 주로 \'진리\'라는 학문을 다룬다."
    "그렇다는 건 저 책을 썼을 당시와 이 편지를 썼을 당시는 비슷 하다는 건가?"
    "그럼 탐정의 서를 통해서 이 퍼즐의 해답을 찾을 수 있다는 건가?"
    "아니{cps=2} {/cps}……라고 말 하고 싶긴하지만……"
    "가능성을 완전히 배제 할 순 없었다."
    "하지만 이 책은 설명문 같은 느낌이라서 진짜 해답이 있을련지는……"
    "그보다 이 기분……"
    "도대체 뭐야……"
    "\'탐정의 서\', \'진리\'그리고 \'수수께끼\'……"
    "분명 뭔가 공통점이 있을거다."
    "하지만……{cps=2} {/cps}모르겠어……"
    show stephan talk
    stephan"이 편지는 어디서 찾으셨어요?"
    show grandpa talk
    grandpa"1층 거실에 있는 벽쪽 금고 안에서 찾았단다……"
    stephan"금고?"
    grandpa"그래, 나도 그런게 있었는지 몰랐어"
    grandpa"시아가 잘 알고 있을게야……{cps=2} {/cps}한번 물어보거라"
    grandpa"미안하지만 할애비는 좀 피곤해서 자야겠구나……"
    hide grandpa talk with dissolve
    play sound "se/search_bag.mp3"
    "할아버지는 그대로 이불 속으로 들어가셨다."
    "아무래도 내가 갑자기 과거 얘기를 듣고 싶다고 해서 지치셨는듯 하다."
    show stephan
    stephan_think"금고에 대한건 시아한테 물어봐야겠다"
    stop music
    scene black with dissolve
    play sound "se/door_open.ogg"
    $ renpy.pause(1)
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(3)
    play music"bgm/smooth3.mp3"
    scene bg mansion_hall with dissolve:
        crop (400,91,479,269)
        size(1280,720)
    "아랫층엔 시아가 피아노 건반을 닦고 있었다."
    "내가 내려온 걸 눈치챘는지 하던 일을 빨리 끝내고 나에게 다가왔다."
    show effect1
    play sound "se/shock.ogg"
    show cia shine:
        zoom 1.4 yalign 0.1 xalign 0.5
    cia"{size=40}혹시 뭔가 찾으신게 있나요?!{/size}" with lshake
    "시아는 눈을 초롱초롱하게 하고선 내쪽으로 고개를 들이댔다."
    hide effect1
    stephan"아,{cps=2} {/cps}아니요"
    stephan"지금 단서가 될만한걸 찾는 중이에요"
    show cia think
    cia"그렇군요……"
    scene bg mansion_hall:
        crop (325,67,731,411)
        size(1280,720)
    show stephan shock2 at left
    show cia think at right
    stephan"퍼,{cps=2} {/cps}퍼즐에 대해서 관심이 있으신가봐요?"
    show cia smile at right
    cia"네!"
    extend" 엄청 있죠!"
    cia"저기 있는 금고를 발견하고 나서 부턴 할아버님이 이상하게 반응 하시니까 뭔가 흥미롭더라고요"
    show cia think at right
    cia"근데 할아버님은 \'이건 토머 집안이 해야 할 일이다!\'라면서 아무것도 못하게 하시니까……"
    stephan_think"\'토머 집안이 해야 할 일\'이라니……{cps=2} {/cps}할아버지도 참……"
    show cia talk at right
    cia"그래도 어쩔 수 없는거겠죠?"
    cia"보니까 뭔가 역사가 있는거 같던데"
    stephan"네……{cps=2} {/cps}확실히 역사가 있는거 같긴 하더라고요……"
    show cia at right
    cia"그렇다면 어쩔 수 없는거겠네요"
    show cia shine at right
    cia"이렇게 된거 제가 최대한 도련님을 지원 해드리겠습니다!"
    stephan"저,{cps=2} {/cps}정말 고마워요……"
    show stephan at left
    stephan"그럼……"
    stephan"혹시 시아 씨는 이 편지를 발견한 곳이 어딘지 아세요?"
    show cia smile at right
    cia"넵!"
    cia"……근데\'시아 씨\'는 또 뭐예요!"
    cia"존댓말 쓰지 않으셔도 괜찮으니까 말 놓으세요!"
    show stephan shock at left
    stephan"네……?{cps=2} {/cps}정말 괜찮은거 맞나요?"
    cia"네"
    stephan"저보다 나이가 훨씬 많아 보이는데……"
    show cia mad at right
    cia"훨씬?!"
    show stephan fear at left
    play sound "se/shock.ogg"
    show effect1
    cia"그냥 반말 까라고 이자식아!!" with lshake
    hide effect1
    stephan"히익!"
    extend" 네!"
    stephan"아니,{cps=2} {/cps}알겠어!!"
    show cia smile at right
    cia"후훗"
    cia"이제 무거운 분위기가 좀 없어졌나요?"
    show cia shine at right
    cia"스테반 도련님과도 부디 친하게 지내고 싶어요!"
    show stephan shock at left
    stephan_think"확실히 무거운 분위기는 없어졌지만……{cps=2} {/cps}대신 무서운 분위기가 생겼어"
    show cia at right
    cia"그래서 할아버님이 가지고 계시던 편지를 발견한 곳이 어딘지 알고 싶으신거죠?"
    show cia smile
    cia"이쪽이에요"
    scene bg mansion_hall at Zoom((1280,720),(325,67,731,411),(826,96,454,255),2.0)
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(2)
    "나는 시아를 따라서 오른쪽 문으로 걸어갔다."
    "그런데 그 곳엔─내가 처음 왔을땐 보지 못한─금고가 있었다."
    "너무 작고 수수해서 몰라봤던 모양이다."
    stephan_think"하지만 5년 전에도 여긴 아무것도 없었을텐데……"
    scene ev safe_closed with dissolve
    show cia:
        zoom 1.8 xalign 1.5 yalign -0.3
    cia"여기, 금고 앞에 쪽지가 끼워져있는 채로 발견했어요"
    stephan"그게 전부였어?"
    show cia talk
    cia"그건 무슨 뜻이에요?"
    stephan"그러니까─혹시 금고 위에 벽지랑 같은 디자인의 커버가 있었다든가 말이야"
    show cia shock
    cia"억!{cps=2} {/cps}그걸 어떻게 아셨어요?!"
    stephan"같이 있었던 편지는 적어도 40년 이상 됐는데, 이제서야 이 금고가 발견됐다는 건 하나 뿐이잖아"
    stephan"\'지금까지 이 금고를 숨겨놓은 장치가 있었다.\'"
    scene ev safe_closed at Zoom((1280,720),(0,0,1280,720),(695,52,512,288),0.5) with dissolve
    stephan"그리고 여기 금고랑 벽 사이의 간격을 봐도 알 수 있어"
    stephan"분명 이 금고를 숨기기 위해, 위에 뭔가를 덮었었다는 사실을"
    scene ev safe_closed
    show cia shine:
        zoom 1.8 xalign 1.5 yalign -0.3
    cia"오오!"
    cia"완전 멋있어요!"
    stephan"헤헤헤……{cps=2} {/cps}뭘 이런걸 가지고……"
    cia"할아버님께서 도련님이 어렸을때 탐정놀이에 푹 빠졌다고 하셨던데!{cps=2} {/cps}그 시간은 결코 낭비되지 않았던거군요!"
    play sound "se/hit.ogg"
    $ renpy.vibrate(0.3)
    stephan"윽……!" with sshake
    stephan"그그, 그보다 말이야!"
    stephan"숨겨져있었을 금고는 어떻게 찾은거야?"
    stop music
    show cia talk with dissolve
    "갑자기 시아의 표정이 굳었다."
    "그리고─지금까지와는 다르게─진지한 말투로 말 했다."
    play music "bgm/sirius5.mp3"
    cia"그건 비오는 어느 날 밤 이었죠……"
    stop music fadeout 0.0
    show cia think
    cia"아니면 새벽 이었던가?"
    show cia talk
    play music "bgm/sirius5.mp3"
    cia"쨌건 아주 어두웠어요……"
    cia"전 그날 화장실을 가려고 했는데……"
    play bgs "bgs/rain.mp3"
    play sound "se/think.mp3"
    scene black with flash
    cia"후아아암~"
    play sound "se/footsteps_wood.mp3"
    cia"불이 어디있더라……"
    cia"으음~"
    cia"불이~"
    play sound "se/hit.ogg"
    $ renpy.vibrate(0.3)
    cia"아얏!"
    cia"내가 방금 벽에 부딪혔나……?"
    play sound "se/door_open2.ogg"
    cia"히읶!"
    cia"벽에 구멍이!"
    cia"할아버님한테 혼나려나?!"
    play sound "se/think.mp3"
    stop bgs
    play music"bgm/smooth3.mp3"
    scene ev safe_closed with flash
    show cia talk:
        zoom 1.8 xalign 1.5 yalign -0.3
    cia"그렇게, 제 머리가 남들보다 단단했다는 사실을 알게 됐죠……"
    show cia shock
    cia"우으……{cps=2} {/cps}지금생각해도 무서워"
    stephan"…………"
    show cia smile
    cia"왜그렇게 쳐다보세요?"
    stephan"아, 아니야"
    stephan"요컨데, 우연히 발견했다 이 소리지?"
    cia"넵!"
    stephan_think"발견하게 된 경위가 우연이어가지곤, 어떠한 단서도 얻긴 힘들겠군"
    scene ev safe_closed at Zoom((1280,720),(0,0,1280,720),(317,238,434,244),0.4) with dissolve
    "이번엔─금고의 문을 여는데 사용된다고 추정되는─다이얼을 자세히 살펴봤다."
    "특이하게도, 이 다이얼은 숫자가 아닌 알파벳으로 되어있었다."
    stephan_think"정답이 뭔지 알기 전에……"
    extend" 왜 굳이 장금장치를 알파벳으로 해놨는지부터 알고싶네"
    stephan_think"혹시 할머니가 어떠한 \'메세지\'를 전달하고 싶었던걸까?"
    play sound "se/think.mp3"
    scene ev note
    show letter1 with flash
    "나는 편지의 내용을 머릿속으로 떠올려봤다."
    "할머니는 할아버지가 꼭 뭔가를 알아주기를 원한다듯이 쓰여 있었다."
    show ev note at Zoom((1280,720),(0,0,1280,720),(236,524,849,478),0.3)
    show letter1 at Zoom((1280,720),(0,0,1280,720),(236,524,849,478),0.3)
    "거기다 마지막에 라는 문장도 조금 이상했다."
    "혹시 그게 이 금고의 비밀번호─라기보단 암호─인걸까?"
    scene ev safe_closed at Zoom((1280,720),(0,0,1280,720),(317,238,434,244),0.4) with flash
    stephan_think"다이얼이 알파벳 형식인걸로 봤을때─꽤 가능성이 높아"
    stephan_think"숫자만 가지곤 표현하기 힘든 정답이라는 뜻이니까"
    "이걸로 대충 비밀번호가 될만한것의 단서는 얻었다."
    "하지만 가장 중요한 \[내가 사랑하는 그대에게 소리로써 가르쳐 주고, 그대는 나에게 의미로써 보여주네\]가 무엇을 뜻하는가?"
    stephan_think"이 편지 자체가 할아버지에게 전하는 \'메세지\'같은거니까, 분명 저 수수께끼에 관한 단서도 할아버지가 가지고 계시겠지"
    stephan_think"그럼 할아버지에게 조금 더 물어보는 수 밖에 없는건가……"
    cia"으으으으으……"
    stephan"……?"
    "내가 나름대로 추리를 하고 있었는데, 갑자기 옆에있던 시아가 안절부절 못하고 있었다."
    scene ev safe_closed at Zoom((1280,720),(317,238,434,244),(0,0,1280,720),0.0)
    show cia shock:
        zoom 1.8 xalign 1.5 yalign -0.3
        linear 0.3 xalign 1.0
        linear 0.3 xalign 1.5
        repeat
    stephan"갑자기 왜그래?"
    cia"그, 그게 말이에요……"
    cia"왠지 도련이라면 말 해도 괜찮을꺼 같은데, 어떻게 말을 꺼내야될지 모르겠어요……"
    cia"그런데도 시간은 계속 지나가고있어서 빨리 결정은 해야되고……"
    stephan"뭐?"
    stephan"무슨 소리야?"
    cia"그러니까 말이에요!"
    show effect1
    play sound "se/shock.ogg"
    show cia shock:
        zoom 2.0 xalign 0.5 yalign -0.2
    stop music
    cia"{size=45}제가 부탁하고 싶은게 있어요!{/size}" with lshake
    scene bg mansion_hall:
        size(1280,720)
        crop(881,95,320,180)
    show stephan blush:
        zoom 1.8 xalign 0.5 yalign -0.3
    stephan"부, 부탁?!"
    play bgs"bgs/clock.mp3"
    stephan_think"뭐야 이 상황……"
    "시아와 나의 얼굴 사이의 간격은 매우 짧았다."
    "그리고 안절부절 못하면서 당황하는 표정과 몸짓이……"
    "그래,{cps=2} {/cps}마치 자신의 마음을 고백하려는 여고생과도 비슷했다."
    stephan_think"혹시 \"처음 보는 순간 반해버렸어요!\"라고 말 하면서, 나에게 고백하려는건가?!"
    stephan_think"그럼 난 뭐라 답 해야하지?"
    stephan_think"……물론 거절 할 생각은 절대 없지만!"
    "─와 같은 망상이 머릿속을 가득 메웠다."
    stop bgs
    scene ev safe_closed at Zoom((1280,720),(317,238,434,244),(0,0,1280,720),0.0)
    show cia shock:
        zoom 2.0 xalign 0.5 yalign -0.3
    if know_seb == True:
        cia"도련님, 세바스찬 이라고 아시죠?"
        play music "bgm/beat2.mp3"
        stephan"어?"
        cia"세바스찬이요!{cps=2} {/cps}제가 아침에 말 했던─같이 일하는 가정부요!"
        stephan"아, 아아!"
        stephan"알고있어!"
        cia"장을 보겠다면서 나간 사람이 아직도 돌아오지 않고 있어서요……"
        show cia mad
        cia"{size=30}지금 배고파 죽겠는데……{/size}"
        show cia shock
        cia"혹시 무슨 일에 말려든게 아닌지 걱정돼요!"
        show cia mad
        cia"{size=30}그 전에 내가 먼저 무슨 일을 벌일지 걱정돼요……{/size}"
        show cia shock
        cia"전 항상 할아버님 곁에 있어드려야 해서 나갈 수 없으니까, 도련님이 대신 세바스찬을 찾아줄 수 있나요?"
        show cia mad
        cia"{size=30}배고파서 밖에나가기 귀찮은데……{/size}"
        show cia shock
        stephan"지금 본심이 아무렇지도 않게 나오는데?!"
        "시아의 말을 듣고, 방금전까지 내가 이상한 망상을 한게 너무 부끄럽게 느껴졌다."
        "왠지 나의 이런 성향도 흑역사로 남게 될 거 같은 기분이 조금 씩 드는데……"
        "그보다 \'세바스찬\' 이라는 사람을 얼른 찾아볼까"
        
    else:
        show cia shock
        cia"\'세바스찬\'이라고, 이 저택에서 저랑 같이 일을 하는 사람이 있는데요……"
        cia"그 사람이 장을 보러 나갔는데……{cps=2} {/cps}아직까지 돌아오지 않아서 걱정이에요……!"
        cia"{size=20}지금 배고파 죽겠는데……{/size}"
        cia"세바스찬은 저랑다르게 여기서 출퇴근을 하는 \'공식적인\' 가정부라서, 그렇게까지 걱정하고싶진 않지만……"
        play music "bgm/beat2.mp3"
        stephan_think"나, 나한테 고백을 하려는 건 아니었구나"
        "방금전까지 내가 했던 상상이 나를 엄청나게 쪽팔리게 만들었다."
        "딱히 내가 입 밖으로 내뱉은것도 아닌데, 왜 이럴까……"
        stephan"잠깐, 공식적인 가정부?"
        stephan"그건 무슨 뜻이야?"
        show cia
        cia"세바스찬 씨는 할아버님께 월급을 받으면서 일 하세요"
        show cia smile
        cia"전 작은 용돈을 받는 대신에─방세, 식비가 전부 무료!"
        stephan"그럼 넌 여기서 살고있어?"
        cia"넵!"
        show effect2
        play sound "se/shock2.mp3"
        show cia shock
        cia"대신 제 요리가 형편없어서……"
        cia"세바스찬 씨가 없으면 굶어야해요……"
        hide effect2
        cia"그러니까 얼른 세바스찬 씨를 찾아주세요!"
        stephan"으, 응……"
        "나는 방금전까지 했던 망상을 머릿속에서 완전히 떨쳐내고, 정신을 집중시켰다."
    stephan"혹시 전화는 해봤어?"
    cia"네, 근데 폰이 꺼져있어서요……"
    stephan_think"발로 뛰어야 하나……"
    stephan"세바스찬 씨는 분명 시장으로 갔다고 했지?"
    show cia
    cia"네"
    stephan_think"이 동네엔 시장이 한군데 밖에 없으니까 직접 가도 찾는 건 문제가 없을 거 같지만……"
    stephan_think"출발한지 오래 됐다고 했으니까 아직까지 시장에 있다곤 보장을 못하겠어"
    stephan"세바스찬 씨는 어떻게 생겼어?"
    show cia think
    cia"흠……"
    extend" 양복을 입고 있고……{cps=2} {/cps}또……"
    show cia talk
    cia"떠오르는 게 그거 밖에 없네요"
    stephan"그냥 사진을 주면 더 편한데"
    play sound "se/shock2.mp3"
    show effect2
    show cia shock
    cia"생각 해보니까 나한텐 세바스찬의 사진이 없잖아!!"
    cia"어쩌죠……{cps=2} {/cps}세바스찬 사진이 저에겐 하나도 없어서……"
    hide effect2
    stephan"뭐 없으면 어쩔수 없지……"
    stephan"시장에 양복을 입고가는 사람은 별로 없을테니까, 그렇게까지 힘들 거 같지도 않고"
    stephan"근데 그분이 시장 어디로 갔을지 아는거 있어?"
    show cia think
    cia"고양이가 있을법한 곳이라면 어디든지 있을 거 같은데……"
    stephan"\'어디든지\'있다니……{cps=2} {/cps}혹시 그거 \'슈뢰딩거의 고양이(Schrödinger\'s cat)\'드립?"
    show cia talk
    cia"네?{cps=2} {/cps}그게 뭐예요?"
    stephan"아니야,{cps=2} {/cps}그냥 이쪽 얘기야"
    stephan"어쨌건, 양복을 입은 사람이랑, 고양이가 있을법한 장소를 중심적으로 찾으면 될 거 같네"
    stephan"찾으면 같이 저택으로 돌아오면 되는거지?"
    show cia smile
    cia"넵"
    cia"잘 부탁드리겠습니다!"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveright
    $ renpy.pause(2)
    play sound "se/door_open.ogg"
    $ renpy.pause(1)
    stop music
    "나는 시장으로 가기 위해서 저택 근처에 있는 버스 정류장으로 걸어 갔다."
    play bgs "bgs/car_driving.mp3"
    centered"수 십 분후"
    scene bg bus_seat with moveright # 시장앞 배경
    "오늘은 어째서인지 도로에 차가 많이 있었다."
    "나는 기다리는 동안 세바스찬 씨에 대해서 곰곰히 생각해봤다."
    stephan_think"내 정보에 의하면, 그 사람은 양복을 입고 있고……{cps=2} {/cps}정식적으로 가정부를 하고 있다……"
    stephan_think"게다가 요리를 잘 한다고 했던 것 같기도 했고……"
    stephan_think"혹시 엄청나게 쩌는 집사 아닌가?!"
    stephan_think"이름도 세바스찬 이잖아?"
    stephan_think"막 /'매트맨(Matman)/'에 나오는 알프래드 같이 엄청나게 유명한 집사일려나!"
    $ extra_name = '버스 벨'
    extra"삐—익!"
    "버스가 목적지에 도착했다."
    stop bgs
    scene bg market_outside with moveright
    play music "bgm/happy3.mp3" fadeout 3.0 fadein 3.0
    play bgs"bgs/people.mp3"
    "가을 이라 그런건지 아직 5시밖에 안됐는데도 하늘은 서서히 어두워지고 있었다."
    "게다가 시장은 사람들로 가득했다."
    "시장에 혼자서 와 보는 건 오늘이 처음이지만, 멀리서\'몰턴시장\'이라고 써있는 거대한 간판 같은 게 눈에 들어와서 나는 시장의 입구가 어디있는지 바로 알수있었다."
    scene bg market_inside with squares # 시장안 배경
    centered"시장 안"
    "생선 냄새와 함께 아저씨들의\'쌉니다 싸요!\'같이 시끄러운 소리로 시장 안을 가득 매웠다."
    "그 뿐만 아니라 사람들도 너무 많아서 누가 누군지 알아보기 힘들었다."
    show stephan think
    stephan_think"내가 생각 했던거 보다 안이 엄청 복잡하네……"
    stephan_think"이런데서 양복을 입었다는 단서 하나만 가지고 사람을 찾는다는 게 가능할까?"
    stephan_think"어쩌지?"
    hide stephan think
    menu:
        "시장 사람들에게 물어본다.":
            "나는 주변을 휙 둘러보며 물어볼 사람을 찾았다."
            "그리고 근처에서 손님이 적은 정육점을 찾았다."
            "나는 정육점 주인에게 다가가 말을 걸었다."
            show stephan talk at left
            stephan"저기요……"
            $ extra_name = '주인 아저씨'
            extra"어서오세요!"
            extra"지금 30퍼센트 행사중입니다!"
            stephan"저어……{cps=2} {/cps}말씀 좀 묻겠습니다"
            stephan"혹시 근처에서 양복을 입은 사람 한 분 못보셨나요?"
            "내가 말을 마치자 아저씨는 내가 물건을 사러 온게 아니라는 걸 알았는지 갑자기 힘이 풀린듯 한숨을 쉬더니 의욕을 잃은 목소리로 대답을 했다."
            extra"난 또……"
            extra"이 근처에서 양복을 입고 장보러 올사람은 그 분 밖에 없죠"
            stephan"그 분?"
            extra"네, 여기서 자주 고기를 사 가시거든요"
            extra"친절하고, 맨날 양복을 입고 장을 보러 와서 꽤 유명해요"
            show stephan
            "정보를 얻으면 얻을수록 점점 쩌는 집사 이미지에 가까워졌다."
            show stephan talk at left
            stephan"그래서 어디있는지 아세요?"
            extra"얼마 전까진 저기 있었는데, 뭔가를 발견했는지 시장 뒷쪽으로 달려나가 던데요?"
            show stephan at left
            stephan"알려주셔서 감사합니다"
            stephan_think"달려서 나갔다는 게 조금 걸리지만 그래도 어디있는지 알았으니 빨리 찾으러 가야겠다!"
            hide stephan
        
        "직접 돌아다니면서 찾아본다.":
            "나는 주변을 둘러보며 양복을 입은 사람을 필사적으로 찾았다."
            "하지만 양복을 입은 사람은 눈씻고 찾아 봐도 없었다."
            show stephan shock
            stephan_think"에초에 그사람이 아직까지 시장에 있을지 없을지도 모르는데……"
            stephan_think"아무래도 시장을 떠나서 다른데로 갔나보다"
            stephan_think"입구 쪽엔 오면서 봤으니까 이번엔 뒷쪽을 통해서 찾아봐야겠다"
            "나는 시장에서 빠져 나오기 위해서 뒷쪽으로 걸어갔다."
            hide stephan shock
    stop music
    scene bg market_back with dissolve # 뒷들판
    "시장 뒷쪽에 도착하자 넓은 들판이 눈에 들어왔다."
    show stephan talk at left
    stephan_think"응?"
    "그때 양복을 입한 한 남성이 보였다."
    "혹시 소문으로만 듣던 세바스찬 씨가 아닌가 싶었는데……"
    scene ev seb_holdcat at Zoom((1280,720),(0,0,1280,720),(533,286,475,267),0.0) with moveright #세바스찬이 고양이랑 놀고있는 일러스트
    play music "bgm/beat4.mp3"
    play sound "se/cat_meow.mp3"
    $ extra_name = '고양이'
    extra"야옹"
    show ev seb_holdcat at Zoom((1280,720),(533,286,475,267),(580,47,475,267),0.7)
    $ renpy.pause(0.7)
    $ seb_name = '고양이를 들고있는 이상한 사람'
    seb"냥냥냥냥냥냥냥"
    seb"야옹~ 야옹~"
    show ev seb_holdcat at Zoom((1280,720),(0,0,1280,720),(0,22,319,179),0.0)
    play sound "se/shock2.mp3"
    stephan_think"{size=45}으에에엑?!{/size}" with sshake
    "뭔가 이상한 사람 이었다."
    "딱히 고양이를 안고 있어서 이상하다는 건 아니다.{cps=2} {/cps}그냥 내가 이상 하다고 생각 한 건……"
    scene ev seb_holdcat at Zoom((1280,720),(0,22,319,179),(689,221,216,121),0.3)
    "바로 저 입!"
    stephan_think"저런 입 모양은 어떻게 나오는거지?!"
    "뭔가 신기하게 느껴졌다."
    scene ev seb_holdcat at Zoom((1280,720),(689,221,216,121,),(447,0,798,449),0.0) with dissolve
    "그거 말고 고양이랑 같이 대화를 시도 하려는 것도 이상하게 느껴졌다."
    stephan_think"이렇게 사람이 많은 곳에서 저런 짓을 하다니……"
    show ev seb_holdcat at Zoom((1280,720),(447,0,798,449),(0,0,1280,720),0.5)
    "어쨌건, 시장에서 양복을 입고있는 사람이 있다."
    scene bg market_back with dissolve
    show stephan shock2:
        xalign 0.0 yalign -0.2 zoom 1.4
        linear 1.0 xalign 0.4
    "나는 용기를 내어 이상한 사람에게 다가갔다."
    stephan"저기……"
    play sound "se/search_bag.mp3"
    show seb talk cat:
        yalign -10 xalign 1.0 zoom 1.4
        linear 0.5 yalign -0.2
    "이상한 사람은 자리에서 일어났다."
    $ seb_name = '이상한 사람'
    seb"저에게 무슨 볼일이라도 있으십니까?"
    stephan"호,{cps=2} {/cps}혹시 세,{cps=2} {/cps}세바스찬 이신가요?"
    $ seb_name = '세바스찬'
    seb"맞습니다만 그걸 어떻게……?!"
    stephan_think"맞았어?!"
    "뭔가 생각 하고 있었던 이미지랑은 많이 달랐다."
    "하지만 시아도 확실히 \'고양이가 있을법한 장소\'에 있을지도 모른다고 했으니까……"
    stephan_think"……하지만 그런 이미지를 내가 멋대로 만든거니까 멋대로 실망하는 건 실례겠지?"
    show stephan:
        linear 0.3 xalign 0.0
    stephan"에헴"
    "난 마음을 가다듬고, 여기로 온 목적을 말했다."
    stephan"저어……{cps=2} {/cps}시아 한테서 세바스찬 씨를 데리고 오라는 부탁을 받았는데……"
    show seb blush
    show effect1
    play sound "se/shock.ogg"
    seb"{size=45}시,{cps=2} {/cps}시아가 저를?!{/size}" with lshake
    hide effect1
    show stephan talk
    play sound "se/cat_meow.mp3"
    show seb shock
    "세바스찬 씨가 안고 있던 고양이가 갑자기 품속에서 뛰쳐나가 도망갔다."
    play sound "se/shock2.mp3"
    show effect2
    seb"이런!"
    hide effect2
    "눈 앞에있는 세바스찬씨는 몇 초간 충격에 빠져 있었다.{cps=2} {/cps}하지만 금새 진정을 되찾고 나에게 질문을 했다."
    show seb talk
    seb"근데 댁은 누구시죠?"
    show stephan shock
    stephan"네?!"
    seb"시아랑 어떻게 아는 사이가 됐죠?"
    seb"시아랑은 어떤 관계죠?"
    stephan"저,{cps=2} {/cps}전 저희 할아버지인 \'에드워드 토머\'의 손자 \'스테반 토머\' 입니다"
    stephan"할아버지가 저를 부르셔서 저택에 있게 되었는데 그때 시아랑 만났습니다……!"
    stephan"그리고……{cps=2} {/cps}저랑 시아는 만난지 아직 하루도 안지났어요;;"
    stephan"이,{cps=2} {/cps}이제 됐나요?"
    show seb
    seb"아……{cps=2} {/cps}할아버님의 손자분 이셨군요……"
    seb"이거 실례했습니다"
    extend" 다시한번 제대로 소개 하겠습니다"
    $ seb_name = '세바스찬 쟝'
    seb"제 이름은\'세바스찬 쟝 (Sebastian Zhāng)\'"
    extend" 시아랑 같이 할아버님을 모시고 있는 사람입니다"
    stephan_think"\'쟝 (Zhāng)\'?{cps=2} {/cps}여기서 보기 흔한 성이 아니네"
    seb"그리고 도련님에 대한 이야기는 할아버님께 자주 들었습니다"
    seb"정말로 빨간색 머리카락을 가지고 계시군요……"
    show seb:
        linear 0.5 xalign 0.75
    "세바스찬 씨는 내 머리카락을 만지려고 다가왔다."
    stephan_think"다들 빨간 머리를 처음보나"
    show stephan shock2
    stephan"에헴"
    show seb shock:
        linear 0.3 xalign 1.0
    seb"앗!"
    seb"죄,{cps=2} {/cps}죄송합니다!"
    extend" 이렇게 빨간 머리는 처음 봐서요……"
    seb"자,{cps=2} {/cps}잘 부탁 드립니다.{cps=2} {/cps}도련님"
    show stephan
    stephan_think"이 사람도 날 도련님 이라고 불러주다니……{cps=2} {/cps}흐흐……"
    stephan"근데……{cps=2} {/cps}휴대폰이 꺼져 있었던거 같던데, 무슨 일 있었어요?"
    seb"방금전에 제가 들고 있던 고양이랑 같이 놀고 있었습니다"
    show seb talk
    seb"휴대폰은 고양이가 놀고있는 사진을 너무 많이 찍는 바람에 배터리가……"
    show stephan shock
    stephan_think"역시 이상한 사람이야"
    show seb shock
    seb"이런!{cps=2} {/cps}벌써 시간이 이렇게 되었군요"
    seb"내가 이렇게까지 오랫동안 있었을 줄이야……"
    show seb
    seb"제 차로 모셔다 드리겠습니다"
    stephan"아……{cps=2} {/cps}감사합니다……"
    scene black with dissolve
    stop bgs
    stop music
    centered"오후 6시 02분"
    scene bg mansion_hall_night with dissolve# 저택 안 거실 배경
    play music "bgm/happy4.mp3"
    show effect1
    play sound "se/shock.ogg"
    show cia mad:
        zoom 1.4 yalign 0.1 xalign 0.5
    cia"{size=45}대체 뭘 하다가 이렇게 늦은거예요!{/size}" with lshake
    hide effect1
    show cia mad:
        zoom 1.0 yalign 1.0 xalign 0.0
    show seb talk at right
    seb"죄송합니다……"
    cia"제가 얼마나 세바스찬 씨를 기다렸는데!"
    show seb blush at right
    seb"저를 기다렸다고요?"
    cia"당연하죠!!"
    cia"배고파 죽겠는데 여기서 재대로된 요리를 만들줄 아는 사람이 세바스찬 씨 밖에 없는 걸요!"
    show seb think at right
    show effect2
    play sound "se/shock2.mp3"
    seb"아……"
    hide effect2
    show cia at left
    cia"아무튼 아무 문제 없었다는 게 정말 다행이에요"
    seb"…………"
    show seb talk at right
    seb"그,{cps=2} {/cps}그럼 전 저녁을 만들러 가겠습니다……"
    hide cia
    play sound "se/footsteps_wood.mp3"
    show seb think:
        linear 3.0 xalign -1.0
    $ renpy.pause(2)
    hide seb think with dissolve
    show stephan shock at left
    stephan_think"왠지 쓸쓸하네"
    show cia at right
    cia"그럼 전 할아버님을 모시고 올게요"
    stop music
    scene black with dissolve
    centered"저녁 시간"
    play music "bgm/happy2.mp3"
    play sound "se/move.mp3"
    scene bg mansion_diningroom_night with moveleft# 식당 배경
    play bgs "bgs/eating.mp3"
    "그때 내가 먹은 저녁 메뉴는 오므라이스랑 닭강정 이었다."
    "이렇게 맛있는 음식은 처음 먹어본것 같다."
    "아니,{cps=2} {/cps}정확히 말하자면 이렇게 많은 사람들과 한자리에 모여서 음식을 먹어본게 처음이다."
    "난 언제나 집에서 혼자 라면이나 배달음식만 시켜먹었으니까"
    "……근데 그것도 생각해보면 나쁘진 않다."
    show seb at right
    seb"음식맛은 괜찮으십니까?"
    show stephan at left with dissolve
    stephan"네!{cps=2} {/cps}정말 맛있어요!"
    hide stephan
    seb"할아버님은 어떠세요?"
    show grandpa at left
    grandpa"세바스찬의 요리 솜씨는 언제나 최상급이야"
    grandpa"오늘은 특히 오므라이스가 맛있군!"
    seb"정말 다행이에요!"
    hide grandpa
    show cia think at left
    cia"근데 세바스찬씨{cps=2} {/cps}시장에서 뭘 하고 있었길래 이렇게 늦었어요?"
    show seb think at right
    seb"그게……"
    show stephan
    stephan"고양이를 보더니 냥냥냥 거리고 야옹~ 거리면서 배터리가 나갈때까지 사진찍고 있었지"
    show seb blush at right
    seb"도련님!{cps=2} {/cps}그걸 말씀하시면!"
    hide stephan
    show cia smile at left
    cia"걱정마세요"
    cia"세바스찬씨의 취향은 존중 해 드린답니다"
    play sound "se/shock.ogg"
    show effect1
    show seb shock at right
    seb"{size=50}잠깐!!{/size}{cps=2} {/cps}뭔가 오해를 살듯한 말투는 하지 말아주세요!" with lshake
    seb"저는 결코 동물 성애자가 아닙니다!"
    hide effect1
    cia"하하하"
    hide cia smile
    show stephan shock at left
    stephan_think"아무도 그런 말은 안했는데……"
    scene bg mansion_diningroom_night with dissolve #식당 배경
    "여럿이서 모여서 밥을 먹는다는 건 정말 재미있는 것이라고 생각하게 됐다."
    "언제 또 이런일이 있을 수 있을까……"
    "그런데 그때 할아버지가 나에게 말을 걸었다."
    play music "bgm/smooth1.mp3"
    show grandpa at right
    show stephan talk at left
    grandpa"스테반……{cps=2} {/cps}퍼즐에 관한건 어떻게 되어 가고 있느냐?"
    stephan"지금은 힌트를 찾는 중 이랄까요……"
    stephan"메세지가 할아버지에게만 직접적으로 전하는 듯한 느낌 때문인지, 뭘 어떻게 해야할지 모르겠어요……"
    grandpa"그렇다면 이 할애비가 뭘 해줘야 되는고?"
    hide grandpa
    hide stephan talk
    menu:
        "이전에 퍼즐 2개의 내용을 알려주세요.":
            show stephan talk at left
            show grandpa at right
            stephan"편지 이전에 있었던 퍼즐 2개의 내용에 대해서 아시는거 없나요?"
            show grandpa think at right
            grandpa"미안 하구나……{cps=2} {/cps}퍼즐에 관한건 기억 나는 게 별로 없어……"
            stephan"그렇군요……"
            show grandpa talk at right
            grandpa"하지만, 메리가 어째서인지 그 퍼즐은 엄청나게 풀어줬으면 했어"
            grandpa"자신을 희생하면서 까지……"
            stephan"희생 이라니……{cps=2} {/cps}어떤 의미에서요?"
            grandpa"말 그대로의 의미지"
            grandpa"그당시 메리의 몸 상태가 많이 안좋았거든……"
            show grandpa think at right
            grandpa"무리 했다간 큰일날거라는 걸 알고 있었으면서도 어째서……"
            grandpa"아직도 메리가 왜 그런 행동을 했는지 전혀 모르겠어……"
            show stephan at left
            stephan"할아버지, 걱정 마세요!"
            stephan"이 퍼즐에 대한 단서만 찾게 되면……"
            stephan"어쩌면 할머니가 그런 행동을 한 이유도 알게 될수 있을지도 몰라요!"
            stephan"그러니 퍼즐의 내용을 포함한 할아버지의 과거를 좀 떠올려 주시면……"
            grandpa"과거라……"
            grandpa"{size=20}일기장……{/size}"
            stephan"네?"
            show grandpa talk at right
            grandpa"과거에 대한 기억이 별로 없지만……"
            grandpa"예전부터 썼었던 일기장엔 분명 기록이 되어 있을게야"
        "할머니가 이 편지를 쓴 이유를 알려주세요.":
            show stephan talk at left
            show grandpa talk at right
            stephan"할머니가 이 편지를 쓴 이유를 알려주세요"
            grandpa"이유?"
            stephan"뭔가 조금이라도 짚이는 게 없어요?"
            stephan"할아버지가 할머니한테 했던 말이나, 행동이나……"
            show grandpa think at right
            grandpa"그렇게 말해도……"
            show grandpa cough at right
            $ renpy.vibrate(0.3)
            grandpa"콜록 콜록"
            show grandpa think at right
            grandpa"짚이는곳이 없구나……"
            stephan_think"역시 무리였나……"
            show grandpa talk at right
            grandpa"그러고보니 내가 옛날에 일기장을 썼던걸로 기억하는데"
            grandpa"혹시 그거라도……"
    play sound "se/shock.ogg"
    show effect1
    show stephan talk at left
    stephan"{size=45}그 일기 어디 있죠?!{/size}" with lshake
    hide effect1
    show grandpa shock at right
    grandpa"아, 아마 서재 쪽에……"
    grandpa"근데……!"
    hide grandpa shock
    "할아버지가 말씀을 다 끝내시기도 전에 나는 식사를 중단 하고 바로 서재로 달려가려고 했다."
    stop bgs
    play sound "se/hit.ogg"
    show cia mad at right with sshake
    "그때 시아가 식탁을 쿵 치더니 마치 화를 참으려고 하듯이 아주 침착하지만 무서운 목소리로 말했다."
    cia"도련님……{cps=2} {/cps}음식을 남기는 게 얼마나 큰 죄인지 아시는가요……?"
    show stephan fear at left
    stephan"그, 그런가요……?"
    cia"식사를 다 마치지 않으시면……{cps=2} {/cps}남은 음식을 다음날에 다시 대접 할거예요"
    stephan"히익!"
    stephan"죄송합니다!"
    scene black with dissolve
    centered"얼마 후……"
    play sound "se/footsteps_running.mp3"
    scene bg lib_night with moveright
    play music "bgm/smooth2.mp3"
    show stephan with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    "이곳은 할아버지의 서재다."
    "어렸을땐 —그리고 지금도— 책에 대한 관심이 없다보니까 딱히 와본적은 없지만, 이곳은 책 몇권만 제외하면 내가 마지막으로 봤을때랑 크게 다른게 없었다."
    show stephan think
    stephan_think"할아버지 말론, 일기장은 검은색 표지를 하고 있었다는 거 같은데……"
    hide stephan
    show inspect_mode: # 탐색모드 시작
        alpha 1.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
    $ renpy.pause(2)
label lib_search:
    scene bg lib_night with dissolve
    call screen lib_imagemap #도서실 조사 장면
    $ result = _return
    if result == "maridge":
        scene black with dissolve
        show ev marrage_image with dissolve# 에드워드랑 메리의 결혼식 일러스트
        stephan_think"이런 사진이 있었던가?"
        "내 기억이 맞다면, 이 사진은 내가 5년전에 있었을땐 없었다."
        "사진을 봤을때 엄청나게 오래전에 찍은거 같다."
        stephan_think"그럼 이거, 할아버지의 결혼식 사진 인가?"
        stephan_think"둘다 정말 젊으시네……"
        "이 사진을 보니까 할아버지가 왜 할머니를 예쁜 사람 이라고 불렀는지 알 것 같았다."
        "정말 아름다우셨다."
        jump lib_search
    if result == "pencil_case":
        show stephan talk with dissolve:
            zoom 2.0 yalign 0.1 xalign 1.0
        "이 필통은 내가 초딩 시절때 잠깐 썼던거다."
        "몇 년 됐는진 잘 모르겠지만, 내가 오기 전부터 있었던 물건이다."
        hide stephan talk with dissolve
        jump lib_search
    if result == "notes":
        show stephan talk with dissolve:
            zoom 2.0 yalign 0.1 xalign 1.0
        "여러가지 노트가 있었다."
        "다른거에 비해서 먼지가 적은걸로 봐선, 꽤 최근에 이쪽으로 옮겨진 듯 하다."
        hide stephan talk with dissolve
        jump lib_search
    if result == "bible":
        show stephan talk with dissolve:
            zoom 2.0 yalign 0.1 xalign 1.0
        "오래된 성경책이다."
        "할아버지가 중년때 교회에 다녔었다는 이야기를 들었던 적이 있었는데, 그때 사용 했던건가보다."
        hide stephan talk with dissolve
        jump lib_search
    if result == "sherlock":
        show stephan with dissolve:
            zoom 2.0 yalign 0.1 xalign 1.0
        "아서 코난 도일의 셜록홈즈 모음이다."
        "난 소설로 읽어본적은 없지만, 영화로는 본적이 있다."
        stephan_think"꽤 재밌었지"
        hide stephan with dissolve
        jump lib_search
    if result == "diary":
        show stephan talk with dissolve:
            zoom 2.0 yalign 0.1 xalign 1.0
        "검은색의 하드커버로 된 낡은 책이 여러권 있었다."
        "그중에서 가장 왼쪽에 있는 걸 짚었는데─표지엔 흰색 레이블이 붙어 있었고 그 위엔 볼펜으로 1958 — 1960 이라고 써있었다."
        show stephan
        "나는 이것이 할아버지의 일기장 이라는 것을 단번에 알 수 있었다."
        show stephan talk with dissolve
        stephan_think"그래……{cps=2} {/cps}할아버지의 일기장……"
        "내가 어렸을때 할아버지는 자기가 젊었을때 느꼈던 걸 하나의 교훈적인 이야기로 압축해서 나에게 자주 들려주셨다."
        "하지만─전부 하나의 \'옛날 얘기\'형식으로만 알려주시기만 했지, 자신의 과거를 있는 그대로 말씀해주신적은 단 한번도 없었다."
        "그런데……"
        "지금 내 손에는 할아버지의 일기장이 있다."
        show stephan think
        play sound "se/book_page.ogg"
        "잠깐 훑어보니까─내용이 예상외로 깔끔하고, 자세하게 쓰여져있었다."
        show stephan
        "원래라면 우리 아버지가 태어난 이후인 60년대 후반부터 읽어도 괜찮을지 몰라도……"
        "나는 할아버지의 과거를 좀 더 알고싶었다."
        "무엇보다 오리엔스의 50년대 후반의 모습을 누군가의 눈을 통해서 볼 수 있는 기회가 자주 있는것도 아니고"
        "그래도 일기장을 읽으면서, 할머니에 대한 정보도 착실하게 얻을 생각이니 그야말로 일석이조다."
        show stephan smile
        stephan_think"얼른 읽어보자!"
        jump found_diary1958
    label found_diary1958:
    stop music
    scene black with dissolve
    narrator_nvl"기억 조각 모드에 진입 하셨습니다."
    narrator_nvl"이 모드에서는 특정 기억의 장면이 여러 조각으로 나뉘어져 있으며, 그것을 전부 맞추면 기억 회상이 시작 됩니다."
    narrator_nvl"조각은 터치로 회전, 드래그로 이동이 가능합니다."
    nvl clear
    play sound "se/case_start.mp3"
    scene black
    show text"{font=fonts/Type_Writer.ttf}{size=60}1958년 11월 3일{/size}{/font}" with memory:
        xalign 0.5 yalign 0.5
    $ renpy.pause(3.0)
    scene ev p_background with dissolve
    play music"bgm/Pathetique_Orgel.mp3"
    python:
        k = puzzle1()
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
            jump  diary1958
label diary1958:################################1958년 11월 3일 일기장 시작############################
    play sound "se/book_page.ogg"
    stop music
    scene black with memory
    play music "bgm/sad2.mp3"
    narrator_nvl"1958년 11월 3일 월요일"
    narrator_nvl"에드워드 토머 26세"
    narrator_nvl"날씨 - 추움"
    nvl clear
    narrator_nvl"오늘, 내가 기다리고 기다리던 면접을 본다."
    narrator_nvl"설마 서류에서 통과되는 날이 올줄이야……"
    narrator_nvl"통과된 회사는 내가 항상 지원 하기를 희망한 장난감 회사다."
    narrator_nvl"이름은 \'노스탤지어 토이즈(Nostalgia Toys)\' 이다."
    narrator_nvl"여담으로 회사의 이름은 저렇지만 실제론 어린이를 위한 장난감만 만든다."
    narrator_nvl"회사 자체는 꽤 크지만 인지도는 그럭저럭 인듯 하다."
    narrator_nvl"이 면접만 통과하면 난 돈을 많이 벌 수 있다."
    nvl clear
    $ extra_name = '면접관 #1'
    extra"{size=50}12번 들어오세요!{/size}"
    play sound "se/footsteps_concrete.mp3"
    "나는 긴장하는 마음으로 면접실 안을 입장했다."
    scene ev edward_interview with Dissolve(1.5) #면접 일러스트
    "안에는 총 세명의 면접관들이 진지한 표정으로 앉아있었다."
    "게다가 조용하고 무거운 공기 때문인지 내 긴장감은 더욱 커졌다."
    show ev edward_interview at Zoom((1280,720),(0,0,1280,720),(708,11,363,204),0.0) with dissolve # 면접관 1
    extra"에드워드 토머 씨 맞으시죠?"
    edward"네"
    extra"만나서 반갑습니다"
    edward"저, 저도 정말 반갑습니다!"
    extra"제가 토머 씨의 서류를 보면서 한가지 궁금한게 있었어요"
    extra"여기 보니까 초등학교를 3년만 다니고 중퇴 했다고 하던데 이게 어떻게 된건가요?"
    show ev edward_interview at Zoom((1280,720),(708,11,363,204),(361,248,557,313),0.6) # 에드워드
    edward"아……"
    edward"거의 16년 넘게 지난 일이라서 기억이 좀 가물가물하지만……"
    edward"저희 집안이 너무 간난해서 학교를 다닐 여유가 없었거든요"
    extra"그럼 10살때부터 지금까지 계속 공장에서 일 하셨다는 뜻인가요?"
    edward"얼마 전에 이쪽으로 이사 오면서 공장에서 일 하는 건 그만 뒀어요"
    edward"대신 지금은 공사장에서 노가다를 뛰고 있습니다"
    extra"잘 알겠습니다"
    show ev edward_interview at Zoom((1280,720),(361,248,557,313),(440,0,363,204),0.4) # 면접관 2
    $ extra_name = '면접관 #2'
    extra"에헴"
    extra"혹시 본인의 인생에서 큰 고난이 있었나요?"
    show ev edward_interview at Zoom((1280,720),(440,0,363,204),(361,248,557,313),0.6) # 에드워드
    edward"저, 저에게 있어서 힘들었던 일은……"
    edward"돈이 부족해서 불이익을 본 것 입니다!"
    edward"제가 가난한게 제 의지가 아닌데도 왜 그 때문에 제가 불이익을……"
    show ev edward_interview at Zoom((1280,720),(361,248,557,313),(440,0,363,204),0.3) # 면접관 2
    extra"그럼 그런 불이익을 어떻게 해서 극복 했나요?"
    "내 말을 중간에 끊어먹었다."
    "자세히 보니까 날 완전히 무시하고 있다는 것이 느껴졌다."
    "그래도 나의 처지를 봐서라도 열심히 참는 수 밖에 없었다."
    show ev edward_interview at Zoom((1280,720),(440,0,363,204),(361,248,557,313),0.4) # 에드워드
    edward"으, 음……"
    edward"도, 돈을 더 많이 벌어서 극복 했습니다!"
    show ev edward_interview at Zoom((1280,720),(361,248,557,313),(440,0,363,204),0.3) # 면접관 2
    extra"그렇군요"
    "윽……{cps=2} {/cps}내가 그런 말을 했다는 게 엄청나게 후회됐다."
    show ev edward_interview at Zoom((1280,720),(440,0,363,204),(708,11,363,204),0.4) # 면접관 1
    $ extra_name = '면접관 #1'
    extra"혹시 취미 같은 건 있는가요?"
    show ev edward_interview at Zoom((1280,720),(708,11,363,204),(361,248,557,313),0.4) # 에드워드
    edward"취미는 딱히 없고……"
    extend" 음악……{cps=2} {/cps}을 좋아합니다"
    edward"아무 음악이나 좋아하는 건 아니고!"
    edward"교,{cps=2} {/cps}교양있게 클래식을 좋아합니다!"
    extra"잘 알겠습니다"
    extra"아쉽게도 면접 시간은 이걸로 끝이고……"
    extra"{size=45}23번 들어오세요!{/size}"
    edward"끄,{cps=2} {/cps}끝인가요!?"
    show ev edward_interview at Zoom((1280,720),(361,248,557,313),(708,11,363,204),0.0) # 면접관 1
    extra"네,{cps=2} {/cps}출구는 왼쪽에 있습니다"
    edward"네……"
    play sound "se/footsteps_concrete.mp3"
    "나는 힘 없이 면접실을 떳다."
    scene black with dissolve
    stop music
    "\'면접에서 합격을 하면 그자리에서 바로 알려줘\'라고 같이 현장에서 일하고 있는 선배가 말해준적이있다."
    "물론 항상 그런건 아니고, 실제론 그러지 않는 경우가 많다는 말도 들었지만……"
    "나에 대한 면접관들의 반응을 보니까 말 할 것도 없다."
    "난 분명 떨어졌다."
    scene bg ravine_night at Zoom((1280,720),(297,0,644,362),(297,0,644,362),0.0) with dissolve # 밤의 뒷산(절벽) 배경
    play bgs "bgs/night.mp3"
    play music "bgm/sad3.mp3"
    "그래도 나만의 비밀 장소에서 싸늘한 밤바람을 맞으며 술을 마시니까 기분이 좀 풀리는 거 같았다."
    "……적어도 면접을 봤을때 보단 훨씬 좋아졌다."
    "여긴 내가 몰턴시로 상경하면서 발견한 외딴 장소다."
    "나만의 비밀기지 같은 장소랄까……{cps=2} {/cps}여기 있으면 아무리 힘든 일이라도, 멀리있는 산들을 바라보면 가슴이 뻥 뚫리면서 기분이 좋아졌다."
    "지나가는 사람도 거의 없다보니까 나의 푸념을 실컷 늘어놓을 수도 있다."
    edward"내 운은 서류 통과에서 끝났나보다……"
    $ renpy.vibrate(.3)
    edward"힐끅" with sshake
    edward"그놈의 학업, 학업, 학업!"
    edward"(벌컥 벌컥)"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}지겹다고!!{/size}" with lshake
    edward"돈이없는 걸 어쩌라고!!"
    hide effect1
    edward"…………"
    edward"공부를 위해선 돈이 필요하고……{cps=2} {/cps}돈을 위해선 공부가 필요하고……"
    edward"참나……"
    $ renpy.vibrate(.3)
    edward"힐끅" with sshake
    edward"도대체 세상이 어떻게 돌아가고 있는거야"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}내가 언젠가 성공해서 반드시 그 새끼들 코를 납작하게 만들어준다!{/size}" with lshake
    hide effect1
    $ renpy.vibrate(.3)
    edward"힐끅" with sshake
    "……이렇게 말은 하지만……{cps=2} {/cps}아무것도 변하지 않는다는 걸 잘 알고있다."
    "세상이 원래 그런거니까"
    edward"이제 어쩌지……"
    edward"다음주 집세도 없는데"
    edward"이 양복도 빌리느라 돈 도 많이 썼고……"
    edward"역시, 그때 내가 너무 섣불리 아주머니 댁에서 나온 걸까……"
    edward"오늘 편지엔 뭐라고 쓰는 게 좋을지……"
    play sound "se/search_bag.mp3"
    "나는 마지막 남은 술 한모금을 한번에 들이킨 뒤 자리에서 일어났다."
    edward"에라이 씨,{cps=2} {/cps}양복이나 반납하러 가야겠다"
    $ renpy.vibrate(.3)
    edward"힐끅" with sshake
    edward"대여 받은지 아직 하루도 안 지났으니까 좀 깎아주려나……"
    stop music
    # 메리의 스프라이트 정보 정의
    $ mary_name = '???'
    $ mary_cloth = 1
    $ mary_hair = 'normal'
    mary"{size=45}에드워드!{/size}"
    edward"응?"
    "나는 뒷쪽에서 들려오는 목소리를 향해서 고개를 돌렸다."
    scene bg ravine_night at Zoom((1280,720),(297,0,644,362),(636,203,644,362),0.6)
    play music "bgm/happy4.mp3"
    $ renpy.pause(0.6)
    play sound "se/heartbeat.mp3"
    show mary with flash:
        zoom 2.0 xalign 1.1 yalign -0.1
    "밤인데도 밝게 빛나는 금발에, 가녀린 하프 소리 같이 아름다운 음색의 목소리……"
    "여신같은 모습이었다."
    "계속 그 사람을 보고있자니 내 술기운은 순식간에 날라가고 알 수 없는 긴장감이 밀려왔다."
    $ mary_name = '금발의 미인'
    show mary smile
    mary"에드워드!{cps=2} {/cps}엄청 오랫만이다!"
    "방금 오랫만 이라고 했나?"
    "하지만 나는 정말 처음보는 여자다."
    "그보다 여길 어떻게 알고 온걸까?{cps=2} {/cps}여긴 나만 알고 있는 장소라고 생각 했는데……"
    "혹시 나 말고 다른 사람들도 이곳을 명당으로 잡았나?!"
    edward"누, 누구시죠……?"
    show mary shock3
    mary"설마 나 기억 못하고 있어?!"
    edward"네에……{cps=2} {/cps}제 기억이 맞다면 오늘 처음 만나 뵈는데……"
    mary"처음 이라고……?"
    mary"정말……{cps=2} {/cps}요?"
    mary"정말 절 처음 보시는거예요?"
    "상대방도 당황했는지 말투가 조금 이상해졌다."
    "근데 왠지모르게 저 여성을 어디서 본적이 있는 거 같은 느낌이 든다."
    edward"흠……"
    play sound "se/think.mp3"
    show ev edward_interview at Zoom((1280,720),(0,0,1280,720),(125,0,529,298),0.0) with flash
    $ renpy.pause(1.0)
    hide ev edward_interview with flash
    edward"아!"
    "잘 생각해보니까 면접볼때 면접관 중 한사람으로 있었다."
    "딱히 나한테 아무런 질문도 하지 않고, 가만히 지켜만 봤었지 아마"
    edward"혹시 면접관 중에 있으셨던 분 이신가요?"
    mary"마, 맞긴 한데……"
    mary"그 외엔 저에 대해서 아무것도 모르신다는거죠?"
    edward"네"
    show mary shy2
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}아아아, 아무래도 제가 사람을 착각했나봐요!{/size}" with lshake
    mary"정말 죄송합니다!"
    hide effect1
    edward"아니에요!{cps=2} {/cps}워낙 흔한 이름이니까 그럴 수도 있는거죠"
    edward"제 주변에도 \'에드워드(Edward)\'라는 이름만 3명이나 있는 걸요"
    show mary shy
    mary"근데 정말 에드워드가 아니신가요……?"
    mary"외모는 조금 다른 거 같기도 하지만, 이름과 성에다 나이까지 제가 알고 있는 사람이랑 진짜 똑같으신데……"
    mary"초등학교때 여기 주변에서 자주 놀고 그랬잖아요!"
    edward"제가 에드워드 인 건 사실이지만, 그런 기억은 전혀 없습니다"
    edward"무엇보다 전 몰턴 출신이 아니라서 어렸을때 여기 있었을리가 없는 걸요"
    mary"음……"
    mary"역시 그런가요……"
    show mary talk
    mary"근데 정말 아니에요?"
    "이 여자가 진짜 끈질기네"
    edward"글쎄 아니라니깐요"
    mary"정말 정말로요?"
    $ mary_name = '메리 슈테른'
    mary"저 \'메리 슈테른(Mary Stern)\' 인데 정말로 기억이 없으세요?"
    stop music
    "잠깐……?"
    "직접 만나본 건 오늘이 처음이지만, 몇 주 전 신문에서 잠깐 관련 기사를 본적이 있다."
    "메리 슈테른은 독일에서 건너온 무기 제조 사업가, \'아브라함 슈테른(Abraham Stern)\'의 외동딸 이다."
    "빼어난 용모에 오리엔스 여성 최초로 하버드를 졸업 할 정도의 뛰어난 두뇌……"
    "무엇보다 그녀의 아버지는 많은 고생을 통해서 막대한 부를 얻었지만, 그녀는 그 모든 부를 부모 잘 만났다는 이유만으로 다 손에 넣었다."
    "그야말로 \'완벽\'이라는 말에 딱 들어맞는 인물,{cps=2} {/cps}그리고 나랑은 정 반대의 인물이기도 하다."
    "아는 사람이 말 하기론, 최근엔 책도 쓰고있다던데……"
    play music "bgm/sad2.mp3"
    "정말 생각만 해도 짜증나는 여자다."
    "나 같은 저소득층의 사람은 평생을 일해도 도달 할 수 없는 곳을……{cps=2} {/cps}그녀는 부모를 잘 만났다는 이유만으로 태어난 순간부터 누리고……"
    "저런식으로 모든 걸 아무런 노력도 없이 손에 넣은 여자는 죽어야 마땅하다고 생각한다."
    "왜 신은 불평등할까"
    "저딴 년은……"
    show mary shock
    mary"저기……?{cps=2} {/cps}괜찮으세요?"
    edward"네─?!"
    mary"절 기억하냐고 물어봤는데 갑자기 멍때리시길래요"
    edward"아……{cps=2} {/cps}음……"
    "젠장, 또 나의 안 좋은 버릇이 나와버렸다."
    "남이랑 대화를 하는 도중에 계속 딴 생각으로 빠져버리고……"
    "근데 지금 내 앞에 있는 여자가 그 슈테른 이라면……"
    edward"저……!{cps=2} {/cps}실례지만 여긴 언제부터 있으셨나요?"
    "내가 방금 전까지 면접에서 있었던 일을 욕한게 들렸다면 꽤나 큰 문제가 될지도 모른다!"
    "몇 달 전엔 부자집 아저씨의 양복에 커피를 쏟았다는 이유만으로 새탁비 300달러를 지불 했어야 했는데……{cps=2} {/cps}모독죄는 얼마나 클지……"
    stop music
    show mary
    mary"\'내가 언젠가 성공해서 반드시 그 새끼들 코를 납작하게 만들어준다\'라고 소리 지르실때 부터 있었어요"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}힉!{/size}" with lshake
    "망했다!"
    "내가 면접관을 욕한게 당사자한테 들켜버렸다!"
    "그것도 하필이면 가장 큰 부자한테 들켜버리다니!{cps=2} {/cps}생 매장을 당해도 이상할게 없어!"
    "이럴 때 내가 취할 수 있는 행동이란……"
    play music "bgm/sad3.mp3"
    show mary shock
    edward"죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다! 죄송합니다!"
    hide effect1
    "나는 눈에 눈물이 글썽이도록 혼심을 다해서 사과했다."
    "명예회손 이라면서 돈을 달라고 하면 난 정말 굶을지도 모르기에 신발이라도 핥을 수 있을 각오로 사과 해야만 한다!"
    mary"{size=20}사, 사과는 한번만 하셔도 괜찮은데……{/size}"
    stop music
    "근데 상대방은 내가 예상한 것과는 조금 다른 반응을 보였다."
    "어쩔 줄 몰라하면서 엄청나게 당황해했다."
    "어쩌면 내 돈과 자존심을 버리지 않고도 넘길 수 있을지도 모른다."
    edward"하지만 제가 엄청난 일을 저질렀는 걸요!"
    mary"그래도 이렇게까지 사과 하실 필요는 없어요"
    show mary
    play music "bgm/beat4.mp3"
    mary"사람들이 자기를 무시하면 그럴 수도 있으니까요"
    show mary shy
    mary"사실 저도 그런거에선 엄청 공감할 수 있어요……"
    edward"정말요?"
    mary"네!"
    "뭔가 예상하지 못한 대답이었다."
    "살면서 여러종류의 사람을 만났지만, 이렇게 자부심이 강한 사람은 처음 봤다."
    "후후……{cps=2} {/cps}운이 좋았군"
    "이젠 이곳을 떠서 다시는 슈테른 씨와 만나지만 않으면 앞으로도 문제 없다."
    stop music
    play sound "se/search_bag.mp3"
    show bg ravine_night at Zoom((1280,720),(636,203,644,362),(440,203,644,362),0.3)
    show mary shy:
        linear 0.3 xalign 1.6
    "나는 작전했던데로 자리를 빨리 뜨려고 했는데, 옷자락이 걸린 것 같은 느낌이 들었다."
    show bg ravine_night at Zoom((1280,720),(440,203,644,362),(636,203,644,362),0.5)
    show mary shy:
        linear 0.5 xalign 1.1
    "고개를 돌리니 내 슈테른 씨가 내 소매를 붙잡고 있었다."
    mary"저, 저기……"
    mary"아까 제가 토머 씨를 공감 할 수 있다고 했잖아요……"
    edward"마, 맞습니다만……!"
    "그냥 가려고 한 나를 왜 붙잡았을까"
    "혹시 이제와서 딴소리 하는 건가?!"
    edward"호, 혹시 뭔가 문제라도 있으신가요?!"
    mary"그런게 아니고……"
    mary"토머 씨가 여기서 혼자말 하고 있었던 걸 듣고 나서 뭔가 떠오른게 있는데……"
    mary"부탁……{cps=2} {/cps}하고 싶은 게 있어요……"
    "엄청나게 불안한 쪽으로 대화가 진전되고 있었다."
    edward"(꿀꺽)"
    play sound "se/search_bag.mp3"
    play music "bgm/happy1.mp3"
    show mary tease with dissolve:
        zoom 2.2 xalign 0.5 yalign 0.0
    mary"혹시 그 사람들의 코를 납작하게 만들어 주고 싶진 않나요?!"
    edward"…………"
    edward"……네?"
    "전혀 예상하지 못한 말이 나를 당황하게 만들었다."
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}면접에서 당신을 무시했던 면접관들의 코를 납작하게 만들고 싶죠?!{/size}" with lshake
    hide effect1
    mary"토머 씨가 면접관들에게 화가 나있듯이, 저도 여러가지로 증명과 복수를 하고 싶거든요!"
    mary"비록 제가 토머 씨를 다른 사람이랑 착각 해서 시작된 만남 일지라도 서로의 목접에 접점이 있으니까 문제는 없다고 봅니다!"
    mary"거기다 제대로 한다면 이 부조리한 체제를 바꿀 수 있을지도 몰라요!"
    edward"…………"
    "지금 자기 자신도 내가 그렇게 욕했던 면접관 중 한명 이라는 사실을 완전히 빼고 있다."
    "그보다 지금 흥분해가지고 말 속도도 엄청 빨랐다."
    mary"어떤가요?!{cps=2} {/cps}저랑 같이 그들의 코를……!"
    show mary cough
    $ renpy.vibrate(0.3)
    mary"{size=45}콜록{cps=2} {/cps}콜록……!{/size}" with lshake
    edward"괜찮으세요?!"
    mary"…………"
    show mary shock2
    mary"제가 너무 열심히 말 했더니 사례가 들려버렸네요"
    edward"아……{cps=2} {/cps}네……"
    "아까전부터 계속 흥분해 하더니, 그럴 줄 알았다."
    show mary tease
    mary"여하튼, 어쩌면 세상을 바꿀 수 있을지도 모를 이 중대한 프로젝트에 동참 하시겠습니까?!"
    edward"으, 음……"
    edward"저한테 무슨 이익이 있는거죠?"
    show mary talk
    mary"이익 이라니……{cps=2} {/cps}당신을 무시한 사람들에게 대한 복수를 할 수 있는 걸요?"
    edward"죄송하지만 전 복수 하는덴 흥미 없습니다"
    "복수는 남는 게 없다."
    "고작 자신의 쾌락을 위해서 타인을 상쳐입히고……{cps=2} {/cps}무엇보다 돈이 남지 않아서 낭비라고 생각한다."
    show mary shock
    mary"네……?"
    edward"왜, 왜 그러시죠?!"
    mary"그런 말을 하는 걸로 봐선 제가 알고 있는 에드워드랑은 다른 인물인 건 확실하네요……"
    "아직도 그 소리냐……"
    show mary
    mary"그래도 상관 없어요!"
    mary"이익이 복수만 있는 건 아니니까요"
    edward"혹시 돈도 있나요?"
    show mary smile
    mary"네!"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}어떤 프로젝트죠?!{/size}" with lshake
    hide effect1
    show mary shock:
        zoom 1.8 yalign -0.1
    mary"아, 음……"
    mary"어째 그런 쪽에선 반응이 좋으시네요……"
    edward"그보다 계획에 대해서나 말씀해주세요"
    show mary tease with dissolve:
        zoom 2.2 yalign 0.0
    mary"저한테 그런식으로 말 하셔도 괜찮을까요?"
    edward"죄, 죄송합니다……"
    show mary think
    mary"에헴"
    show mary
    mary"우선 프로젝트명을 말씀 드리겠습니다"
    "그냥 내용만 알려주지, 왜 불필요한 걸 "
    play music "bgm/beat3.mp3"
    mary"이름하여 \'프로젝트 코 납작\'입니다!"
    "아까전까지 말 했던 것과는 반대로, 엄청나게 대충 지은 이름이었다."
    edward"그, 그래서 전 구체적으로 뭘 하면 되는거죠……"
    show mary smile
    mary"제가 면접에서 합격시켜 드릴테니, 평범하게 일 해주세요!"
    edward"네?!"
    edward"제가 뭔가 잘못 들은 거 같은데……"
    extend" 절 면접에서 합격시켜 주실거라고요?"
    mary"맞아요"
    show mary shock
    mary"설마 싫은건가요?"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}당치도 않습니다!!{/size}" with lshake
    hide effect1
    show mary smile
    mary"역시 그렇게 나오실 줄 알았어요"
    stop music
    "하지만 나같은 사람을 고작 접점이 있었다는 이유만으로 취직 시켜준다는 건 뭔가 이상했다."
    "혹시 다른 속셈이 있는 게 아닌지 확인 해야한다고 생각했다."
    edward"근데……"
    edward"정말 취직후에 평범하게 일만 하면 되는가요?"
    edward"그 외엔 아무것도 할 필요가 없는거죠?"
    mary"에이 설마요~{cps=2} {/cps}당연히 조건이 있죠"
    edward"어떤거죠……?"
    show mary tease
    play music "bgm/beat4.mp3"
    mary"아주 열심히 일을 해서 노스텔지어 토이즈에 없으면 안 되는 인물이 되어주세요"
    mary"그렇게 당신을 얕잡아본 인물들의 코를 전부 납작하게 만들어버리는겁니다"
    edward"하, 하지만 전 아무것도 할 줄 모르는 걸요……"
    mary"그렇기 때문에 토머 씨가 필요한거에요"
    mary"아무것도 할 줄 모른다고 해서 앞으로도 아무것도 할 줄 모를거라는 고정관념을 깨버리는겁니다!"
    show mary smile
    mary"못 할 거 같다는 이유만으로 잘 할 수 있는 기회 조차 주지 않으려는 이 부조리한 세상을 같이 바꿔보자고요"
    "그래……{cps=2} {/cps}난 그걸 원했다."
    "내가 과거에 학비조차 댈 수 없을 정도로 돈이 없었다는 이유만으로 앞으로도 돈을 벌지 못하게 하는 이 부조리한 세계"
    "그걸 바꿔보고 싶었다."
    "그리고 지금 내 눈앞에 그런 기회를 재공 할 수 있을지도 모르는 사람이 있다."
    "어쩌면 이 만남은 운명일지도 모른다."
    edward"정말 감사합니다"
    mary"저야말로 작은 희망을 주셔서 감사합니다"
    show mary
    mary"코납작 건에 대해선 나중에 제가 면접 합격 여부가 확실하게 결정되고 난 뒤에 따로 우편으로 보내 드릴게요"
    edward"아, 아직 확실해진 건 아니군요……"
    show mary shock2
    mary"벌써부터 다 좋게 돌아갔다고 생각하시면 곤란해요"
    mary"실제론 아직 시작조차 하지 않은걸요"
    edward"그렇겠죠……"
    edward"아!{cps=2} {/cps}혹시 제 주소 같은거라도 드려야 하나요?"
    show mary
    mary"그거라면 걱정 하지 않으셔도 괜찮아요.{cps=2} {/cps}면접 전에 내신 서류에 모든 정보가 기록 돼 있으니까요"
    edward"그렇죠……"
    show mary talk with dissolve:
        zoom 1.9 yalign -0.1
    "슈테른 씨는 손목 시계를 보더니 나에게 말했다."
    show mary with dissolve:
        linear 0.4 zoom 2.2 yalign 0.0
    mary"벌써 시간이 이렇게 됐네요"
    mary"그럼 며칠이 걸릴 진 모르겠지만, 다음에 만날땐 회사에서 만날 수 있기를 빌게요"
    edward"넵!"
    show mary shy
    mary"그리고……"
    mary"술 많이 마시면 몸에 안 좋아요"
    mary"특히 이렇게 추운 날씨엔 더더욱……"
    mary"그러니까 다음에 만나면……{cps=2} {/cps}건강하고 밝은 모습으로 만났으면 좋겠네요"
    show mary shy:
        linear 0.3 xalign -1.3
    play sound "se/footsteps_running.mp3"
    "슈테른 씨는 휙 돌아 빠른 걸음으로 갔다."
    hide mary shy
    stop bgs
    scene black with Dissolve(1.0)
    stop music
    play sound "se/book_page.ogg"
    nvl clear
    narrator_nvl"1958년 11월 4일 화요일"
    narrator_nvl"날씨 - 추움"
    narrator_nvl"나는 어제 슈테른 씨가 한 말이 계속 신경쓰여서 잠을 재대로 못이루었다."
    narrator_nvl"시간은 돈이다."
    narrator_nvl"일찍 일어나야 많이 일을 할 수있고"
    narrator_nvl"많이 일을 해야 돈을 많이 벌 수 있다."
    narrator_nvl"무엇보다 아직은 아무것도 확신된게 없기 때문에 괜한 기대를 해선 안 된다."
    nvl clear
    play music "bgm/smooth5.mp3"
    centered"오전 6시 30분"
    "난 잠을 잘 못 잤음에도 불구하고 마치 본능처럼 일찍 일어났다."
    "매일 이 시간쯤 일을 시작하다 보니 몸에 배긴듯 하다."
    "일어 난 뒤 세안을 하기 위해 화장실로 갔다."
    "세안이 끝나면 옷을 갈아 입고, 공사장으로 이동하고…… "
    "오늘도 매일 같은 하루가 반복 된다."
    "이런 생활만 벌써 몇 년 째인가……"
    play music "bgs/building.mp3"
    centered"공사장"
    scene bg working_site with dissolve
    "나는 공사장에 도착해서 평소와 같은 패턴으로 움직였다."
    "현장으로 이동 중에, 입구 쪽에 앉아서 커피를 마시고 있던 선배가 나에게 다가와서 말을 걸었다."
    $ extra_name = '선배'
    extra"에드워드!"
    extra"오늘도 여기 왔다는 건……{cps=2} {/cps}어제 면접은 떨어졌나보네?"
    edward"만나자 마자 무슨 말씀을 하시는 겁니까!!"
    edward"그리고……"
    edward"아직 떨어진 건지 붙은 건지 모르겠어요……"
    extra"응?{cps=2} {/cps}그건 또 무슨 소리야?"
    edward"말하자면 좀 긴데……"
    edward"일단 자세한건 우편으로 알려준다고 하니까 그동안 제가 못 했던 일 이나 마저 하려구요"
    extra"역시 워커홀릭, 에드워드"
    extra"참 성실하네~"
    edward"에이~{cps=2} {/cps}뭘요~"
    "워커홀릭……"
    "매일 쉬지도 않고 일만 하는 나에게 붙은 별명이다."
    "……그다지 좋은 별명 이라고 생각하진 않는다."
    extra"그럼 에드워드는 취직이 확정되면 더 이상 여기에 안나오는 건가?"
    edward"아무래도 그렇겠죠?"
    edward"시간도 안맞고 그러니까요"
    extra"그럼 이 기회에 물어보고싶은 게 있는데……"
    extra"넌 도대체 뭘 위해서 이렇게까지 열심히 일을 한거야?"
    edward"네?{cps=2} {/cps}일을 한다니……"
    extend" 그야 당연히 돈을 벌기 위해서……{cps=2} {/cps}겠죠?"
    extra"그러니까, 그 돈을 버는 이유 말이야"
    extra"나야 집에 가족이 있고 하다 보니까 돈을 벌어야 하지만"
    extra"넌 혼자서 살잖아, 그렇게 까지 힘들게 돈을 벌 필요가 있나?"
    edward"…………"
    edward"……그냥 돈이 좋아서 벌고 있는거지, 딱히 이유는 없어요"
    extra"음……{cps=2} {/cps}그래……?"
    "난 솔직하게 말했을 뿐 이다."
    "확실히 난 여가 생활이나, 챙겨야 할 가족이나, 목적이 있는 것은 아니다."
    "물론 아주머니가 있긴 하지만,{cps=2} {/cps}내가 그 분에게 주는 돈은 그다지 많진 않다."
    "내가 돈을 모으는 이유……{cps=2} {/cps}그냥 뭔가 마음이 안정된다."
    "또, 그와 반대로 돈이 없어지면 불안 해진다."
    "생각해보니까 내가 왜 돈을 벌고있는지 진지하게 생각해 본적이 없네……"
    "뭐, 생각하고 싶은 마음도 없지만……"
    extra"그래도 그렇게 돈만 쫓다 보면 중요한 걸 놓치는수가 있어……"
    edward"무슨 뜻이죠?"
    extra"넌 아직 젊잖아"
    extra"내가 젊었을땐 전쟁 때문에 제대로된 삶을 살기 힘들었지……"
    extra"그래도 고생 끝엔 낙이 있을거라고 생각하면서 힘든 나날을 버텨왔는데"
    extra"어느샌가 난 여기서 겨우 먹고 살수있을 정도로밖에 못벌고 있지……"
    extra"나의 청춘은 끝났다{cps=2} {/cps}……라고 해야 할까"
    edward"그,{cps=2} {/cps}그렇군요……"
    extra"그래도 에드워드는 나랑 다르게 행복한 시대에서 살고 있으니까 정말 부러워"
    extra"나처럼 살기 싫으면 너도 좀 \'현재\'를 즐겨봐"
    edward"…………"
    "나는 선배가 무슨 말을 하려는지 의도는 알겠으나 이유를 모르겠다."
    "돈이 뭐가 나쁘지?"
    "돈은 많으면 많을수록 좋은거잖아?"
    "돈을 벌면서 사는것이 가장 \'현재\'즐기는 행위라고 생각 하는데?"
    "아무래도 선배가 나이가 많아서 뭘 모르는듯 하다.{cps=2} {/cps}옛날엔 전쟁 때문에 돈의 가치가 적었으니까"
    "돈은 많으면 많을수록 기분이 좋아진다."
    "돈을 벌기 위해서 일을 하는 것이야 말로 젊음을 만끽하는 것 이라고 나는 생각한다."
    edward"조언 감사합니다"
    edward"전 빨리 현장에 가 봐야 될듯 하니까 이만……"
    extra"너무 무리 하진 말고!"
    scene black with dissolve
    play music "bgm/smooth1.mp3"
    centered"오후 9시 50분"
    "나의 일과는 매우 규칙적 이면서 단순하다."
    "새벽 6시 반에 공사장으로 출근을 하고"
    "오후 5시에 공사장 일이 끝나면 집에서 1시간 정도 쉬고 나서 식당에서 밤 9시 까지 아르바이트를 한다. "
    "거리 때문에 실제로 집에 도착하는 시간은 10시에 가깝다."
    "집에 도착하고 나선, 다음날을 위해 잠을 잔 뒤, 같은 하루의 반복"
    "정말 단순하고 알아보기 쉽다."
    "하지만……"
    scene bg edward_house_night at Zoom((1280,720),(0,0,1280,720),(603,241,677,381),0) with dissolve# 에드워드 집 앞
    play music "bgm/sad4.mp3"
    play bgs "bgs/night.mp3"
    "오늘 집으로 들어오다가, 우편이 한 통 온 것을 봤다."
    "혹시 매일 편지를 주고받는 아주머니 일까 생각을 하면서 들여다 봤는데……"
    play sound "se/book_page.ogg"
    narrator_nvl"To: 에드워드 토머"
    narrator_nvl"From: 노스탤지어 토이즈"
    narrator_nvl"\'에드워드 토머\'님이 저희 \'노스탤지어 토이즈\'에 공식적으로 채용 됐음을 알리는 바 입니다. "
    narrator_nvl"첫 출근 시간은 아침 7시부터 시작 하며"
    narrator_nvl"깔끔한 복장으로 오시기 바랍니다."
    narrator_nvl"행복한 하루 되세요."
    nvl clear
    "편지의 글씨는 타자기로 친게 아니라 손으로 쓴 것 같아 보였다."
    play sound "se/think.mp3"
    scene bg ravine_night with flash
    show mary tease:
        zoom 2.2 xalign 0.5 yalign 0.0
    $ renpy.pause(0.5)
    scene bg edward_house_night at Zoom((1280,720),(0,0,1280,720),(603,241,677,381),0) with flash# 에드워드 집 앞
    "순간 내 머리속에서 어제 봤던 메리 슈테른 씨의 이미지가 스쳐 지나갔다."
    edward"훗"
    "왠지 모르게 가슴이 두근거리고……{cps=2} {/cps}입가엔 미소가 지어졌다."
    "나는 매일 매일, 하루도 거르지 않고 여러 장난감 회사에 입사 서류를 냈었다."
    "그리고 전부 능력 부족으로 서류조차 통과되지 못했지……"
    "그래도 나의 6번째 도전으로 드디어 목표를 이룰 수 있었다!"
    "이건 전부 슈테른씨 덕분이라고 생각하고있다."
    "하지만……"
    "장난감……"
    "어렸을때 그다지 가지고 놀아본 경험이 없다."
    "그럼에도 불구하고 난 이렇게 장난감 회사에 취직을 하려고 혈안이 되어있다니……"
    "나한테 장난감 이라는 말은 어때서인지 공허하게 들린다."
    "뭔가……{cps=2} {/cps}큰 걸 잃어버린듯한 느낌이 든다 랄까……{cps=2} {/cps}아니면 부족한 느낌?"
    "내가 어렸을때 장난감을 가지고 논 기억이 없음에도 불구하고 그런 회사에 취직을 하고 싶은 마음은 여기서부터 온다."
    "조금이라도 이 공허함을 채울 수 있을것 같은 느낌이 들기 때문이다."
    "뭐가 어쨌건 이걸로 난 공식적인 직장인 이다!"
    edward_think"드디어 나도 사회에 쓸모있는 사람이 됐다고!"
    "……생각해보니까 이걸로 오늘 아주머니께 쓸 편지의 내용이 생겼다."
    scene black with dissolve
    narrator_nvl"To. \'엘사라 나보코프(Elsara Nabokov)\'"
    narrator_nvl"아주머니,{cps=2} {/cps}어제 편지를 쓰지 못해서 죄송합니다."
    narrator_nvl"좀 복잡한 일이 있어서 제가 깜빡 해버렸네요……"
    narrator_nvl"하지만 오늘 무척 좋은 소식이 있어요!"
    narrator_nvl"제가 예전에 서류 냈다고 말씀 드린 노스탤지어 토이즈에 취직 했거든요!"
    narrator_nvl"이제 저도 고정된 월급을 받는 사회인이 됐어요!"
    narrator_nvl"이 좋은 소식을 \'미란다(Miranda)\'에게도 꼭 알려주세요."
    narrator_nvl"사랑하는 에드워드 토머가"
    nvl clear
    edward"오늘은 편하게 잘 수 있겠어"
    stop bgs
    stop music
    play sound "se/book_page.ogg"
    ################################1958년 11월 4일 일기장 끝############################
    scene bg lib_night with memory
    play music "bgm/smooth5.mp3"
    centered"오후 9시 20분"
    show stephan talk with dissolve:
        zoom 2.0 yalign 0.1 xalign 1.0
    "나는 일기장을 읽다가 시간이 꽤 지난걸 확인 한 후에 바로 집으로 향하기로 했다."
    "집에선 내 생각을 정리하는데 더 편하기도 하고"
    scene bg room_stephan_night with Dissolve(1.0)
    centered"스테반의 집"
    show stephan think
    stephan_think"할아버지가 처음으로 할머니를 만난게 이때 쯤이야……"
    stephan_think"그리고 내가 필요한 장면은 할머니가 처음으로 그 편지를 작성 한 날"
    stephan_think"앞으로 갈 길이 멀것 같네……"
    play sound "se/phone_text.mp3"
    "폰에서 문자가 왔다."
    show stephan talk
    stephan_think"이 시간에 문자라……"
    show stephan shock
    stephan"윌리?!"
    "윌리 한테서 문자가 왔다."
    "내용은……"
    narrator_nvl"혹시 내일 오전 10시 이후에 같이 렌스 씨 면회 갈래?"
    nvl clear
    show stephan think
    "렌스와 면회라……"
    "솔직히 안 갈 이유는 없다."
    "……그보다 렌스에 대해서 궁금한게 많다."
    "\'법과 경찰을 넘는다\'는 마르쿠스 고드윈의 두목은 도대체 누구일까?"
    stop music
    scene black with dissolve
    centered"9월 14일 일요일"
    centered"오전 10시"
    centered"유치장 복도"
    scene bg police_hall with moveright# 경찰서 복도 배경
    play bgs "bgs/people.mp3"
    show stephan talk
    stephan"오……"
    stephan"안이 이렇게 생겼구나……"
    hide stephan talk
    play sound "se/footsteps_concrete.mp3"
    "멀리서 이쪽으로 걸어오는 발소리가 들려왔다."
    show willy at right
    willy"안녕"
    show stephan yawn at left
    stephan"나오셨군……"
    show willy shock at right
    willy"뭔가 엄청 싫어하는 반응인데?"
    stephan"기분탓이야……{cps=2} {/cps}그래서 면회는 어떻게 하면 되는거야?"
    show willy talk at right
    willy"잠깐, 멜 누나가 도착할때 까지 기다려봐……"
    show stephan shock at left
    stephan"……!!"
    stephan_think"멜 누나……"
    stephan"혹시 사건 이후 초면?"
    willy"어,{cps=2} {/cps}렌스 씨가 체포 됐다는 소식만 들었지, 그 외엔 모르고있어"
    "멜 누나랑 같이 렌스 씨를 면회 가는 게 조금 두려웠다."
    "하지만 다른 한편으론 보고 싶다는 생각도 들고……"
    "그러나 나에게 선택권이 있을까?"
    extend" 잘 생각해보면 렌스가 잡힌 이유가 나 때문이니까……"
    "여기서 내가 렌스와 면회를 하지 않는다는 건 앞으로 벌어질 일에 대한 책임을 회피 하는거나 마찬가지다."
    show stephan talk at left
    stephan"가자"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveright
    $ renpy.pause(3)
    "우리는 꽤 복잡한 면회 과정을 걸치고 나서, 드디어 렌스를 만날 수 있게 됐다."
    stop bgs
    play sound "se/door_open.ogg"
    play music "bgm/sad2.mp3"
    scene bg police_meeting with moveright
    show mel talk
    show stephan talk at left
    show willy talk at right
    "멜 누나는 렌스 앞에 앉고, 나랑 윌리는 그 뒤에서 둘이 대화 하는 모습을 지켜봤다."
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel talk:
        yalign 1.0 xalign 0.8
    mel"렌스?{cps=2} {/cps}자기, 이게 어떻게 된 일 이야?!"
    mel"불법 흉기에 폭력까지?!{cps=2} {/cps}분명 뭔가 잘못된 거지?!"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,275),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"…………"
    lance"이런 말 만 가지곤 안될지도 모르겠지만……{cps=2} {/cps}미안……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel talk:
        yalign 1.0 xalign 0.8
    mel"그럼……{cps=2} {/cps}자기가 진짜로?"
    mel"하지만 왜?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance mad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"저기 뒤에 있는 녀석들한테 못들었어?!"
    show effect1
    play sound "se/shock.ogg"
    lance"{size=45}난 널 이용하려 했다고!{/size}" with lshake
    lance"내가 너랑 사귀고,{cps=2} {/cps}결혼을 하겠다고 한 것도 전부!"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel talk:
        yalign 1.0 xalign 0.8
    mel"……이용?"
    play music "bgm/sad5.mp3"
    mel"호,{cps=2} {/cps}혹시 지금 결혼사기를 말 하는거야?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,275),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"그래……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel talk:
        yalign 1.0 xalign 0.8
    mel"왜 그런 일을 하는거야?{cps=2} {/cps}자기는 분명 회사의……"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"전부 거짓말 이었어……"
    lance"클라크 무역도, 네 아버지를 위해서 결혼을 한다는 것 도……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sirius:
        yalign 1.0 xalign 0.8
    mel"그,{cps=2} {/cps}그럴리가……"
    show mel sad
    mel"왜……"
    mel"나한테 그런……"
    mel"그럼 지금까지 나랑 같이 있고……{cps=2} {/cps}나한테 해준게 전부……"
    extend" 돈 때문이었어?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"아니……"
    extend" 내 생존을 위해서 였어……"
    lance"그것도 너를……{cps=2} {/cps}희생해서……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"그,{cps=2} {/cps}그건 또 무슨 뜻이야?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"나한테……{cps=2} {/cps}좀 큰 빚이 있어……"
    extend" 갚지 못하면 내가 죽는……{cps=2} {/cps}그런 빚"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"그럼 경찰한테 갔어야지!{cps=2} {/cps}왜 이런 짓을?!"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance mad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"내가 안 해봤을거 같아?!"
    lance"나도 할 수 있는 건 전부 해봤다고!"
    show lance shock
    lance"……하지만 아무리 발버둥을 쳐도 이 것 밖에 없었던 걸 어떻게"
    show lance sad
    lance"나도 이러고 싶진 않았어"
    show lance mad
    lance"않았다고!"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"흑……{cps=2} {/cps}흑……"
    "멜 누나는 흐느끼며 울기 시작했다."
    mel"자기……{cps=2} {/cps}나, 혹시 기다려도 될까?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance shock:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"…………"
    lance"뭐……?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"아직 폭행이랑 불법 흉기 소지 죄로 긴급 체포 된 거 뿐이잖아?"
    mel"그,{cps=2} {/cps}그러니까 분명 기회가 있을거라고……"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance shock:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"지금 무슨 소리야?"
    lance"난 내 빚을 너한테 떠넘기려고 했다고?!"
    show effect1
    play sound "se/shock.ogg"
    lance"{size=45}나 대신 널 죽이게 하려고 했다고!{/size}" with lshake
    hide effect1
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"그래도……{cps=2} {/cps}흑……"
    mel"내가 알고 있는 렌스 클라크는 이런 나쁜 사람이 아닌 걸……!"
    mel"내가 좋아하는 렌스 클라크는 반드시 있다고!"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"멜……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"그러니까……"
    extend" 자기를 기다려도 될까?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"…………"
    "렌스는 아무런 대답을 하지 않았다."
    "하지만 저 표정이 렌스도 멜 누나를 향한 마음이 있었다는 걸 말해줬다."
    "어쩌면 그렇기 때문에 렌스가 멜 누나에게 선물을 잔뜩 사주고, 데이트도 자주 했던 것이 아닐까?"
    "둘의 관계는 앞으로 얼마 남진 않았지만……{cps=2} {/cps}그래도 사귀고 있는 \'현재\'만큼은 즐기고 싶어서……"
    "결말이 어쨌건, 둘이 서로를 사랑 했다는 것 만큼은 사실이어서……"
    "하지만 이 모든것은 그저 나의 가설 일 뿐이다."
    lance"할 말은……{cps=2} {/cps}그거 뿐이야?{cps=2} {/cps}멜?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"흑……{cps=2} {/cps}흑……"
    mel"내 질문의 대답은……?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"미안……{cps=2} {/cps}난 대답 할 자격이 없어"
    show lance
    lance"……하지만 말리진 않을게"
    lance"잘못 한 건 나니까 말이야"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"…………"
    mel"꼭……{cps=2} {/cps}다시 만나자……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(0,0,1280,720),0.6) with dissolve
    play sound "se/footsteps_running.mp3"
    show mel sad:
        yalign 1.0 xalign 0.8
        linear 0.8 xalign -1.0
    "누나는 마치 이 현장을 피하듯, 밖으로 뛰쳐 나갔다."
    stop music
    "……결국 이 면회실엔 나와 윌리, 그리고 렌스가 남아있게 됐다."
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    "몇 초간 흘렀던 정적을 깨며, 렌스가 입을 열었다."
    lance"윌리……{cps=2} {/cps}아무래도 네가 이긴 것 같네……"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 윌리 스테반 시점
    show willy talk:
        yalign 1.0 xalign 0.8
    show stephan talk:
        yalign 1.0 xalign 0.2
    willy"이기다니요?"
    willy"딱히 승부를 하고 있었던 건 아닌데요?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"결국엔 네가 원했던데로 멜을 지켜냈잖아.{cps=2} {/cps}그정도면 네 승리라고 봐도 되지 않을까?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 윌리 스테반 시점
    show willy:
        yalign 1.0 xalign 0.8
    show stephan talk:
        yalign 1.0 xalign 0.2
    willy"글쎄요.{cps=2} {/cps}아직은 좀 이르다고 생각 되는군요"
    stephan"저기……{cps=2} {/cps}나 궁금한게 있어"
    willy"뭔데?"
    stephan"넌 언제부터 렌스가 이런 일을 꾸미고 있다는 걸 알고 있었어?"
    willy"멜 누나가 나한테 자기가 결혼을 한다고 자랑질을 했을때 부터였지"
    willy"나중에 따로 클라크 무역회사에 대해서 조사 해보니까 이런저런게 다 나오더라"
    play music "bgm/smooth3.mp3"
    show willy smile
    willy"정확힌 아무것도 나온게 없었다고 해야겠지?"
    willy"페이퍼 컴퍼니니까 말이야~"
    show stephan shock
    stephan"으,{cps=2} {/cps}응……"
    show willy
    willy"그리고 렌스 씨,{cps=2} {/cps}굳이 승리를 했다면 제가 아니라 바로 이 녀석 이겠죠"
    show willy smile2
    willy"\'이것이 바로 나의 운명 인거지\'……{cps=2} {/cps}아주 멋있더라?"
    play music "bgm/beat3.mp3"
    show stephan blush
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}어어어?!{/size}" with lshake
    stephan"그보다 너, 안에 있었던 걸 어떻게 들은거야?!"
    hide effect1
    show willy
    willy"내가 저번에 방문했을때 미리 도청기를 설치 해뒀거든"
    willy"뭐어……{cps=2} {/cps}말이 도청기지, 실제론 그냥 평범한 블루투스 이어폰이야"
    willy"자동 페어링으로 설정하면 일정거리 내에선 이어폰에 설치된 마이크로 대충 안에서 벌어지는 일을 들을 수 있어"
    show willy shock
    willy"배터리가 걱정돼서 좀 비싼 걸로 샀는데……{cps=2} {/cps}역시나 가격이 좀 쎄더라"
    stephan"그,{cps=2} {/cps}그냥 그걸로 안에서 하는 대화를 녹음 한 뒤 멜 누나한테 들려주면 됐잖아!"
    show willy talk
    willy"과연 누나가 그거만 가지고 납득 할 거 같아?"
    willy"무엇보다 음질이 워낙 안 좋아서 최대한 자신이 좋은 쪽으로 해석 할 가능성이 있어"
    stop music
    willy"……그리고,{cps=2} {/cps}이건 렌스 씨를 위한 거 이기도 해"
    show stephan talk
    stephan"어?"
    willy"렌스 씨, 앞으로 수명이 1년도 채 남지 않았죠?"
    lance"…………"
    stephan"수명이……?"
    show stephan shock
    "…………"
    "윌리가 말 한 \'렌스 씨를 위한 거\'의 뜻을 알 것 같았다."
    "일단 렌스에겐 자신의 목숨을 담보로 잡아놓은 대출이 있다……"
    "그리고 내 기억이 맞다면 그 대출은 내년 2월달에 만료가 된다."
    play music "bgm/sirius3.mp3"
    stephan_think"감옥에 간다고 해서 대출이 사라지는 것은 아니니까……"
    extend" 석방 되는 순간 렌스는 죽겠지……"
    "하지만 현재 렌스는 감옥에 있기 때문에 함부로 죽일 순 없을거다……"
    "즉, 윌리가 이런 방식을 택 한 이유가 바로 렌스를 조금이라도 살리기 위해서"
    stephan"렌스를 위했다는 게……{cps=2} {/cps}그런 뜻이었구나……"
    play sound "se/search_bag.mp3"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    "그때 윌리는 렌스를 자세히 쳐다보면서 진지하게 말을 했다."
    willy"렌스 클라크……{cps=2} {/cps}당신은 여기를 나가는 순간 바로 죽습니다"
    willy"게다가, 당신의 채권자인 마르쿠스 고드윈 이라는 사람의 상사가 경찰과 법을 뛰어 넘는다고 하지 않았나요?"
    willy"뭐어……{cps=2} {/cps}공권력을 행사하면서 까지 당신을 죽일 만한 가치는 없어 보이니까, 후자는 크게 걱정 하실 필요는 없을지도 모르겠군요"
    lance"…………"
    lance"그래……{cps=2} {/cps}이걸로 난 죽는거지……"
    lance"그래서 뭘 어쩔 건데?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0)
    stop music
    show willy talk
    willy"살고 싶습니까?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0)
    show lance talk:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"살고……{cps=2} {/cps}싶냐니……?"
    willy"네"
    willy"여기 안에 있는동안은 목숨을 유지 할 수 있을지도 모르겠지만,{cps=2} {/cps}대신 자유가 없잖아요?"
    show lance shock
    lance"네가 뭘 어떻게 할 수 있는데?!"
    lance"녀석들은 법과 경찰을 넘는다고 했잖아?!"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 윌리 스테반 시점
    show willy talk:
        zoom 1.4 yalign -0.2 xalign 0.5
    willy"법과 경찰……{cps=2} {/cps}아니, 이 사회를 만든 존재……"
    play music "bgm/sirius2.mp3"
    willy"……과연 \'민중\'을 넘는것이 가능 할까요?"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance talk:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"…………"
    willy"어때요?{cps=2} {/cps}살고 싶습니까?"
    show lance
    lance"이런……{cps=2} {/cps}정말 너란 녀석은"
    lance"뭔가 좋은 계획이라도 있어?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 윌리 스테반 시점
    show willy talk:
        yalign 1.0 xalign 0.8
    show stephan talk:
        yalign 1.0 xalign 0.2
    willy"그 전에, 먼저 저랑 몇 가지 약속 해주세요"
    lance"뭔데?"
    willy"첫 번째,{cps=2} {/cps}지금부터 제가 묻는 질문에 절대 거짓말을 하지 말 것"
    show willy
    willy"어쩌면 제 목숨을 걸어야 될지도 모르니까 조심 해야죠"
    show willy talk
    willy"그리고 두 번째……"
    stop music
    hide stephan talk
    show willy talk:
        linear 0.3 zoom 1.4 yalign -0.2 xalign 0.5
    willy"다시는……{cps=2} {/cps}멜 누나 근처에 가지 마세요……"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance shock:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"…………"
    lance"그……{cps=2} {/cps}래……"
    show lance talk
    lance"대신 내 무사귀환도 보장 해 줘야 돼"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) # 윌리 스테반 시점
    show willy smile:
        yalign 1.0 xalign 0.8
    show stephan shock:
        yalign 1.0 xalign 0.2
    willy"그거라면 걱정 마세요.{cps=2} {/cps}저희는 이제 한 배를 탄 동료니까요"
    "잠깐만……{cps=2} {/cps}렌스가 다시는 멜 누나를 못본다고?!"
    play music "bgm/sirius5.mp3"
    stephan"윌리,{cps=2} {/cps}정말 그렇게 해도 괜찮겠어?!"
    show willy talk
    willy"뭘?"
    stephan"앞으로 렌스랑 멜 누나가 못 만난다는거"
    willy"그게 왜?{cps=2} {/cps}당연히 그렇게 해야 될 거 아니야?"
    stephan"하지만……!"
    play sound "se/think.mp3"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) with flash # 멜 시점
    show mel sad:
        yalign 1.0 xalign 0.8
    mel"그러니까……"
    extend" 자기를 기다려도 될까?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) with flash # 윌리 스테반 시점
    show willy talk:
        yalign 1.0 xalign 0.8
    show stephan shock:
        yalign 1.0 xalign 0.2
    stephan"그렇게 되면 멜 누나가 뭘 위해서 기다리는 거야?!"
    willy"잠깐 이쪽으로 와 봐"
    play sound "se/search_bag.mp3"
    show stephan shock:
        linear 0.5 xalign 0.55
    $ renpy.pause(0.5)
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(531,286,553,312),0.0) with dissolve# 스테반이 윌리에게 가까이옴
    show willy talk:
        zoom 1.4 yalign -0.3 xalign 0.8
    show stephan shock:
        zoom 1.4 yalign -0.3 xalign 0.35
    "윌리는 렌스가 듣지 못하도록 나에게 귓속말로 얘기 했다."
    willy"넌 저딴 녀석이 멜 누나랑 같이 있어도 괜찮을거 같아?"
    willy"방금전에 자신의 무사귀환을 전재 조건으로 누나랑 같이 있지 않겠다는 것에 동의 했어"
    willy"렌스는 멜 누나를 전혀 좋아하고 있지 않다고!"
    show stephan sad
    stephan"…………"
    stephan"아무리 그래도……{cps=2} {/cps}네 누나를 평생 기다리게 하는 건……"
    willy"누나한텐 내가 어떻게든 잘 말 할거야"
    willy"그리고……"
    willy"내가 아무리 렌스의 목숨을 붙여 놔도, 쟨 이미 죽은거나 마찬가지야"
    show stephan shock
    stephan"……어?"
    willy"지금 여기가 어디야?"
    show stephan talk
    stephan"경찰서……"
    willy"그래,{cps=2} {/cps}그리고 철창 뒤에 있는 게 바로 렌스 잖아"
    willy"저 사람은 이미 사회에선 죽은거나 마찬가지야"
    show stephan shock
    stephan"…………"
    willy"전과가 붙어버린 이상……{cps=2} {/cps}렌스는 사회에서 본인이 설 위치를 잃게 돼버려"
    willy"특히 전과자가 매우 드믄 오리엔스 내에서는 더욱 불이익이 많지"
    willy"뭐어……{cps=2} {/cps}굳이 따지자면 택시기사 정도는 할 수 있겠지만"
    willy"그래도 그 일을 얼마나 해먹어야 다시 사회에서 일어 설 수 있겠냐?"
    willy"복권에라도 당첨 되지 않는 한은 방법이 없어"
    show willy
    willy"이렇게 하나, 저렇게 하나,{cps=2} {/cps}렌스는 죽을 운명이야"
    show willy smile
    willy"어차피 죽을거면 조금이라도 써먹어야 될 거 아니냐?"
    show stephan mad
    stephan"너……{cps=2} {/cps}왜 이렇게 잔인 한거야?"
    stephan"처음부터 렌스를 구할 목적은 없었지?"
    show willy shock
    willy"…………"
    willy"맞아……{cps=2} {/cps}네 말대로 내가 렌스 씨를 구한 목적은 따로 있었어"
    willy"애초에 렌스 씨의 목숨은 별 상관도 없었지"
    willy"……하지만 그게 잔인 하다고?"
    willy"그럼 마르쿠스 고드윈 이라는 사람이랑 그의 상사가 하는 짓은?!"
    willy"그녀석들 이라도 잡지 않으면 렌스같은 사람들이 더 많이 나온다고!"
    stephan"…………"
    willy"스테반,{cps=2} {/cps}얼마 전에 학교에서 선생님이 이런말을 했지?"
    willy"\'잔인한 건 내가 아니라, 이 사회\'라고"
    willy"생각해봐,{cps=2} {/cps}구제의 방법이 없는 렌스를 이용하면 더 많은 피해자를 없앨 수 있어!"
    show stephan sirius
    stephan"그건 \'공리주의(功利主義, Utilitarianism)\' 잖아……{cps=2} {/cps}절대로 좋을리가 없다고!"
    willy"공리주의?{cps=2} {/cps}좋지 않다?"
    willy"미안하지만 이 사회는 계속해서 공리주의를 실현하고 있어"
    willy"만약 공리주의가 나쁜거라면 감옥에 있는 범죄자들은 어쩔거야?{cps=2} {/cps}소수의 죄인을 격리·희생 해서 다수의 정직한 사람들이 편하게 살 수 있는거잖아?!"
    stephan"…………"
    willy"절대 공리주의가 나쁜게 아니야"
    willy"나쁜 건 무고한 사람들이 희생 되는 것 뿐"
    willy"그리고 그 걸 막기 위해선 두가지 방법이 있어"
    willy"평범하게 무고한 자의 희생을 막느냐,{cps=2} {/cps}아니면 무고한 자를 무고하지 않게 만드느냐"
    willy"공교롭게도 렌스의 경우 후자가 되었지만……"
    stephan"한때 무고했던 사람을 희생 하는 건……{cps=2} {/cps}무고한 사람을 희생 시키는거랑 같은 게 아니야?"
    show willy talk
    willy"정신병을 앓고 있는 소수의 사람들을 제외하곤 대부분의 범죄자들은 자의식과는 관계 없이 범죄를 저질러"
    willy"그런 사람들에게 법의 심판을 내리는 게 잘못됐어?"
    willy"그런 사람들도 죄를 짓기 전엔 평범하게 살고 있었던 사람들이라고?"
    show stephan shock
    stephan"…………"
    willy"나는 이 고드윈 이라는 사람과 그의 상사를 용서할 수 없어"
    willy"어차피 렌스의 인생은 끝이야,{cps=2} {/cps}만약 그 걸 바꿀 수 없다면, 이용해서 더 많은 피해자가 생기지 않도록 만드는거지"
    show stephan sirius
    stephan"그럼 왜 네가 이런 일에 신경 쓰는거야?"
    show willy shock
    willy"어?"
    stephan"넌 그냥 학생이잖아!{cps=2} {/cps}왜 이런 큰 일에 관여 하는거냐고?"
    stephan"이런 건 경찰이 해결 해 주는거고, 혹시 그걸로 제대로 해결되지 못한다면 그런 경찰들을 해결하려는 정치인들과 정책이 나오는거야"
    stephan"네가 커서 그런 꿈을 가지겠다면 모를까,{cps=2} {/cps}이건 뭔가 아니잖아?"
    stephan"그래도 멜 누나 때는 네 누나이기 때문에 네가 그런 행동을 취하려고 한 것에 어느정도 공감은 있었어……"
    stephan"하지만 마르쿠스 고드윈 이라는 사람같이, 우리랑 전혀 접점이 없고, 관련 없는 사람의 문제까지 관여 할 필요는 없다고 봐!"
    show willy talk
    willy"설마 네가 그런 말을 할 줄이야"
    willy"너한테 조금 실망인데?"
    stephan"…………"
    willy"내가 왜 이런 일을 하는지……{cps=2} {/cps}이유는 매우 단순해"
    willy"그저 \'할 수 있으니까\' 하는 것 뿐이야"
    willy"만약 이 손으로 한 사람이 죽을 운명을 바꿀 수 있다면……"
    willy"설령 그것이 나랑 관련 없는 사람 이라고 해도!"
    willy"내가 바꿀 수 있다는 사실을 알면서 모른척 할 순 없어"
    show willy
    willy"안 그러면 죄책감이 들잖아?"
    stephan"할 수 있으니까 하겠다는 건……{cps=2} {/cps}할 수 없으니까 안 하겠다는 뜻이잖아?"
    show willy talk
    willy"…………"
    stephan"렌스를 구할 수 없으니까 아무런 시도도 없이 구하지 않겠다니……"
    stephan"넌 그때랑 하나도 변하지 않았아……"
    show willy shock
    willy"야……!"
    play sound "se/footsteps_running.mp3"
    show stephan sirius:
        linear 0.5 xalign -1.0
    scene black with Dissolve(3.0)
    "나는 윌리가 말을 마치기 전에 면회실을 나갔다."
    "왜 였을까……"
    "내가 윌리의 말에 설득 될 거 같아서……?"
    "하지만 그렇다는 건 윌리가 한 말이 정론 이라는 뜻이 아닌가?"
    "…………"
    "그냥 너무 짜증났다."
    "왠지……{cps=2} {/cps}나를 보는 듯 한 느낌이 들었다."
    play sound "se/static.mp3"
    show ev dic_stephan
    $ renpy.pause(0.5)
    hide ev dic_stephan
    "자신이 할 수 있다는 착각과 자만에 빠지고……{cps=2} {/cps}나중엔 그냥 포기하고……"
    "먼 훗날엔 마치 처음부터 그런 일은 없었다며 \'자기암시(自己菴示, Autosuggestion)\'하고"
    "……그런게 너무 짜증났다."
    "죽이고 싶을 정도로 짜증났다."
    "하지만……"
    "윌리는 나랑 다르다."
    "딱히 나쁜 짓을 하려는 건 아니고, 무엇보다 걘 어쩌면 진짜로 할 수 있을지도 모른다……"
    "설령 렌스를 \'살려\'준다는 듣기 좋은 포장으로 이용해서 버린다고 해도……"
    "설령 자신의 진짜 목적을 위해서 남을 알게 모르게 이용 한다고 해도……"
    "결과적으로 윌리는 자신의 능력이 닿는 한에서 렌스를 구해줬고……{cps=2} {/cps}비록 그의 사회적인 위치는 상실 했어도 목숨은 붙어있게 됐다."
    "그리고 그에게서 얻은 정보로 고드윈 이랑 그의 상사를 찾겠지……{cps=2} {/cps}그렇게 해서 이 이상의 피해자가 생기는 걸 막고"
    "여기서 내가 따져야 할 문제는 공리주의가 아니라 바로 \'결과주의 (結果主義)\'일지도 모른다."
    "그렇다면 과연 여기서 정답은 뭘까……"
    "아니, 애초에 정답 이라는 게 존재는 할까?"
    "할아버지 말로, 진리를 봤다고 하는 할머니는……{cps=2} {/cps}이 문제에 대한 정답을 알고 계실까?"
    stephan_think"훗……{cps=2} {/cps}잘 생각해보면 이건 나랑 아무런 관련도 없는 일이잖아……"
    "윌리가 뭘 하든 말든, 난 방해 하지 않고, 스스로를 위험한 일에 빠뜨리지만 않으면 되는거였다."
    "그렇게 생각하니 지금까지 계속 열을 내고 있던 내 자신이 멍청하게 느껴졌다."
    stephan_think"……끝나면 윌리한테 사과 해야겠다"
    stephan_think"안그러면 내 마음이 찝찝 하겠어"
    stop music
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) with Dissolve(1.5) # 윌리 스테반 시점
    show willy talk:
        yalign 1.0 xalign 0.8
    willy"이걸로 좀 조용해졌군요"
    willy"스테반은 신경 쓰실 필요 없으니까 계속 하도록 하죠"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance talk:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"어……"
    play music "bgm/sirius1.mp3"
    willy"지금부터 제가 몇 가지 질문을 하도록 하겠습니다"
    willy"어째서인지 스테반은 어제 당신과 만날 때 눈치 채지 못했던 거 같았던데……"
    willy"아마 렌스 씨는 알고 있었겠죠?"
    willy"……당신은 이 차용증을 갚을 의무가 없다고"
    lance"그래……"
    willy"그럼 이 대출을 받은 이유가 그 사실을 알고 있었기 때문에?"
    lance"맞아,{cps=2} {/cps}공짜로 주는 돈 이라고 생각하고 있었어……"
    willy"그럼 왜 이제와서 렌스 씨는 멜 누나를 이용하려고 한 거죠?"
    show lance sad
    lance"…………"
    lance"얼마 전에 어떤 여성으로 부터 전화 한 통이 왔었어"
    lance"고드윈 본인은 아니고, 비서 같은 분위기 였다고 해야 할까?"
    play sound "se/think.mp3"
    scene black with flash
    lance"여보세요……?"
    $ extra_name = '수화기 너머'
    extra"네, 혹시 렌스 클라크 님 이신가요?"
    lance"맞습니다만, 무슨 용건이죠?"
    lance"보험 이라면 관심……"
    extra"채납 기간이 앞으로 1년 남으셨다고 확인 전화를 드립니다"
    lance"채납……?"
    lance"지금 무슨 소리인지 잘 모르겠습니다"
    extra"어?{cps=2} {/cps}렌스 클라크 님이 2012년 2월 14일에 마르쿠스 라이언 고드윈 님 으로부터 500만 달러를 빌리신걸로 알고 있습니다만"
    lance"그거 말이야?"
    lance"당신내들 그거 사기인거 다 알아!{cps=2} {/cps}계속 이렇게 하면 내가 경찰 신고를……"
    extra"다시 한번 말씀 드리겠습니다.{cps=2} {/cps}채납 기간이 앞으로 1년 남으셨습니다"
    extra"혹시 기간 내에 갚지 못하실 경우 계약서에 쓰여진 대로 할 예정이오니 주의 해 주시기 바랍니다"
    play sound "se/phone_end.mp3"
    lance"…………"
    lance"뭐야……"
    play sound "se/phone_text.mp3"
    $ renpy.pause(1.0)
    lance"문자?"
    "나는 방금 온 문자를 확인 했는데……"
    play sound "se/shock.ogg"
    lance"으,{cps=2} {/cps}욱!" with sshake
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with flash # 렌스 시점
    show lance sad:
        zoom 1.5 yalign -0.2 xalign 0.5
    lance"몸 속이 텅 비어있는 남성의 시체 사진이 첨부돼서 왔었어……"
    willy_think"계약서에 쓰여진대로 장기를 빼 갈거 라는 뜻인가"
    willy_think"하지만 뉴스나, 그 어디에서도 그런 시체가 발견 됐다는 소식은 들어본적이 없어……"
    lance"나는 무서워서 바로 이 사진과 어제 있었던 일을 경찰에게 알렸지"
    lance"다행히도 신고는 접수가 됐는데……{cps=2} {/cps}문제는 계속 수사 중 이라고만 하고, 그 외엔 아무런 소식이 없었어"
    lance"채납일은 계속해서 다가오고 있었고……"
    lance"그런데 내가 경찰에 신고를 한지 며칠 후에 또다시 연락 왔었어"
    play sound "se/think.mp3"
    scene black with flash
    extra"혹시 렌스 클라크 님 이신가요?"
    lance"내가 경찰에 신고 했으니까 아주 잡히기만 해봐라!"
    extra"그 건이라면 알고 있습니다"
    extra"렌스 클라크 님이 3일 전 오전 11시 21분에 몰턴 경찰청에 신고를 하셨더군요"
    extra"……계속 이런 일이 발생하게 된다면 저희는 어쩔 수 없이 클라크 님의 채납일을 당겨야 할지도 모릅니다"
    extra"그러니 앞으로는 주의를 해주시기 바랍니다"
    extra"그리고 혹시나 클라크 님과 연락이 닿이지 않을경우, 오리엔스 채무법에 의해서 서류상 가장 가까운 가족이 대신 채납의 의무를 가지게 됩니다"
    lance"즉, 내 가족을 가지고 협박 하겠다는 뜻이냐?!"
    stop music
    extra"\'하데스(Hades)\'님이 있는 한은 경찰에 신고를 해도 무의미 하다는 걸 잊지 마세요"
    play sound "se/phone_end.mp3"
    $ renpy.pause(0.5)
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with flash # 렌스 시점
    show lance shock:
        zoom 1.5 yalign -0.2 xalign 0.5
    show effect1
    play sound "se/shock.ogg"
    willy"{size=45}방금 하데스 라고 했어요?!{/size}" with sshake
    hide effect1
    lance"어,{cps=2} {/cps}어─"
    lance"하는 말로 봐선 고드윈의 상사 같은 분위기 였는데……"
    lance"혹시 알아?"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(319,257,769,433),0) with Dissolve(1.5) # 윌리 스테반 시점
    show willy shock:
        yalign 1.0 xalign 0.8
    willy_think"하데스……{cps=2} {/cps}라고?"
    "하데스……"
    "나는 그가 누군지 모른다."
    "성별도, 본명도, 나이도, 위치도, 아무것도 모른다."
    "하지만 하데스라는 사람이 무슨 짓을 했는지, 어떠한 조직에 소속되어 있는지는 알고 있다."
    show willy smile2
    "그 사람은……{cps=2} {/cps}내가 계속 찾고 싶었던 인물이니까"
    "절대로 용서해선 안되는 사람……"
    willy_think"지금까지는 아무런 단서도, 연결점 조차도 찾기 힘들었는데……"
    willy_think"\'마르쿠스 고드윈\'이라는 사람이 하데스와 접점이 있다면 조금이나마 추적할 수 있는 단서가 생겼어"
    play music "bgm/sirius1.mp3"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) with dissolve # 렌스 시점
    show lance talk:
        zoom 1.5 yalign -0.2 xalign 0.5
    willy"알고 있다기보단……{cps=2} {/cps}알고 싶은 사람 이라고 해두죠"
    willy"그럼 그 이후론 연락이 없었나요?"
    lance"어"
    willy"혹시 고드윈의 통장 번호 같은거라도 있나요?"
    willy"일단 그사람 한테 돈을 빌렸으니까 송금 받을때……"
    lance"몰라,{cps=2} {/cps}돈을 그 자리에서 현금으로 받았거든"
    willy"네?!"
    extend" 현금이요?!"
    lance"어─{cps=2} {/cps}처음엔 너무 좋은 조건 이라고 생각 했었는데……"
    willy_think"역시 이상한 사건이야……"
    willy"혹시 당신 말고 같은 사채를 쓴 사람도 었나요?"
    show lance sad
    lance"\'로날드 라지오(Ronald Lazio)\'"
    willy"혹시 어제 같이 있었던 동업자……?"
    show lance talk
    lance"그래,{cps=2} {/cps}나보다 오래전에 사채를 썼다고 했어"
    stop music
    lance"……채납일이 얼마 남지 않았대"
    lance"그래서 같이 동업을 하기로……"
    willy"같이 동업을 하겠다는 건 거짓말이고……"
    play music "bgm/sad4.mp3"
    extend" 사실은 라지오 라는 사람도 이용 할 생각 이었죠?"
    show lance shock
    lance"…………"
    willy"실제론 자신이 가지고 있는 페이퍼 컴퍼니를 좀 더 있어보이기 위해서 놓은 \'장식품\'에 불과했잖아요?"
    lance"이제와서 왜 그런말을 하는거지?!"
    willy"훗, 걱정하지 마세요.{cps=2} {/cps}전 렌스 씨가 쓰래기 같은 인간 이었다는 걸 아주 오래 전 부터 알고 있었으니까요"
    show lance mad
    lance"방금 네가 같은 배를 탄 존재라고 하지 않았던가?"
    willy"죄송해요.{cps=2} {/cps}저랑 렌스 씨가 좀 비슷 하게 보여서 저도 모르게……"
    willy"그럼 당신의 장식품인 라지오 씨의 채납일은 어느정도 남았죠?"
    lance"정확한 날짜는 기억이 안 나고……{cps=2} {/cps}아마 이번 달 내로 끝난다고 했던거 같아"
    willy_think"즉, 라지오 라는 사람이 죽는 순간을 지켜볼 수 만 있다면 일이 편해지겠군……"
    willy"혹시 라지오 씨가 어디 있는지 아시나요?"
    show lance talk
    lance"알 리가 없지……"
    willy"흠……{cps=2} {/cps}아무래도 직접 조사를 해봐야겠군요"
    lance"어떻게 조사를 하려고?"
    willy"제가 당신을 찾은 것과 같은 방법이죠,{cps=2} {/cps}자세한 건 비밀입니다"
    lance"…………"
    lance"윌리엄, 넌 정체가 뭐야?"
    willy"네?{cps=2} {/cps}그건 또 무슨 뜻이에요?"
    lance"네 말을 계속 들으니까 뭔가 평범한 애가 아니라는 게 느껴져……"
    willy"…………"
    willy"괜히 깊게 관여했다간 지금 당신이 처한 상황보다 더 나락으로 떨어질 수 있어요"
    willy"그래도 알고싶나요?"
    show lance shock
    lance"아, 아니……"
    willy"매우 현명하신 판단 입니다"
    show lance talk
    lance"그럼 지금 네가 생각하고 있는 계획을 말 해 줄래?"
    willy"계획이라……"
    willy"아직 남 한테 자랑할 만한 계획은 없고……{cps=2} {/cps}대신 한가지 걸리는 게 있더군요"
    willy"제 기억이 맞다면 당신의 사채가 월 1\%의 이자에, 3년의 계약 기간을 가지고 있었죠?"
    lance"그래"
    willy"이자는 비정상적으로 적고, 채납 기간이 비정상적으로 깁니다"
    willy"거기다 상대방은 사기라는 게 뻔히 보이게 서류에 \'신체 담보\'라는 글귀도 적어 놓았고……"
    lance"대신 서류의 폰트가 좀 작아서 자세히 읽어야 알 수 있었어"
    willy"어쨌건 이 대출은 채권자에게 아무런 이익이 없어요"
    willy"게다가 사채이기 때문에 신용도를 묻지도 따지지도 않잖아요?"
    lance"확실히 이상하다고 느꼈어……"
    willy"어차피 그 차용증엔 법적인 효력은 없어요.{cps=2} {/cps}하지만 그 사람들은 당신에게 현금으로 돈을 지급 했어요"
    willy"거기다 상대방은 공권력도 다룰 수 있을정도의 사회적인 지휘를 가지고 있는 것 같기도 하고……"
    willy"설령 하데스 라는 사람 본인이 이러한 권력을 가지고 있지 않다고 해도, 살인 사건 하나를 통째로 덮어버리는 힘……"
    willy"고작 경찰의 말단 이라면 이런 권한은 없습니다"
    willy"그보단 자신의 직업을 잃어버릴 위험이 있죠"
    willy"이건 단순히 장기 매매를 전문으로 하는 질 나쁜 사채업자의 소행은 아니라는 게 확실해졌군요"
    willy"애초에 돈을 목적으로 일 하는 것 같지도 않고"
    willy"뭔가 더 큰 목적이……"
    lance"그럼 누가 범인 이라고 생각 하고 있는거야?"
    willy"그것도 좀 더 조사를 해봐야 될 거 같군요"
    willy"하지만 이정도면 꽤 많은 진전이 있었습니다"
    willy"지금부터 조금씩 전진 하는거죠"
    scene black with dissolve
    willy_think"아니,{cps=2} {/cps}이정도의 정보가 있으면 오히려 저쪽에서 오도록 만들 수 있을지도 몰라"
    play sound "se/search_bag.mp3"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(319,257,769,433),0.8) with Dissolve(1.5) # 윌리 스테반 시점
    show willy talk:
        yalign 1.0 xalign 0.8
    willy"그럼 오늘은 이정도로만 해두죠"
    willy"나중에 또 찾아 올게요"
    willy_think"어서 전화를……"
    play bgs "se/phone_calling.mp3"
    $ renpy.pause(2.3)
    willy"…………"
    stop bgs
    $ extra_name = '수회기 너머'
    extra"흑……{cps=2} {/cps}여보세요?"
    willy"나야"
    stop music
    scene black with Dissolve(1.9)
    play music "bgm/smooth1.mp3"
    play bgs"bgs/people.mp3"
    scene bg police_hall with moveright
    show stephan talk at left
    show willy:
        xalign 2.0 yalign 1.0
        linear 0.7 xalign 1.0
    willy"기다렸어?"
    stephan"윌리……"
    extend" 있잖아……"
    show willy talk
    willy"왜?"
    show stephan blush
    stephan"그, 그러니까 말이야!"
    show stephan think
    stephan"여기서 곰곰히 생각해보니까 네가 안에서 했던 말이 맞는 거 같기도 하고……"
    stephan"그때 내가 했던 말도 좀 거시기 하고……"
    show willy smile2
    willy"하고싶은 말이 뭔데?"
    show stephan shock2
    stephan"미안……"
    show willy
    willy"네가 사과 할 필요는 없어"
    willy"자신의 의견을 표현 하는 건 나쁜게 아니니까"
    willy"그리고……{cps=2} {/cps}만약 사과를 해야 한다면 아무래도 나겠지……"
    willy"안에서 너한테 심한 말을 한 거 같기도 하고"
    show stephan shock
    stephan_think"윌리……"
    willy"우리 둘다 이렇게 미안해 하고 있는데……{cps=2} {/cps}그냥 퉁 치는 건 어때?"
    stephan"너 은근 대인배다?"
    willy"불 필요한 싸움은 안 하고 싶거든"
    show stephan
    stephan"그건 나도 마찬가지야"
    willy"그럼 이제부터 어디 갈 생각이야?"
    stephan"집……{cps=2} {/cps}이겠지?"
    willy"그럼 같이 상점가에 좀 들릴래?"
    stephan"좋아!"
    play sound "se/move.mp3"
    scene black with moveleft
    stop bgs
    play music "bgm/happy5.mp3"
    play bgs "bgs/market.mp3"
    scene bg downtown_outside with movedown# 상점 거리
    centered"오후 1시"
    centered"상점 거리"
    show stephan at left
    show willy at right
    stephan"어디 들릴 생각이야?"
    willy"게임을 사고싶은데……{cps=2} {/cps}혹시 아는데 있어?"
    stephan"네가 게임을?{cps=2} {/cps}왠일이래?"
    show willy talk
    willy"내가 하려는 게 아니라……{cps=2} {/cps}룸메이트를 위한 선물 이랄까……"
    show stephan shock
    stephan"어?"
    stephan_think"뭔가 불안한데?"
    willy"너한테 PX4를 넘기고 나서부터 완전히 미쳐버렸어"
    show stephan shock2
    stephan"미치다니?{cps=2} {/cps}어떻게?"
    willy"다 큰 어른이 방바닥에 드러누워서 울고불고 있다고 생각하면 돼"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan_think"{size=45}도대체 어떤 사람이야?!{/size}" with lshake
    hide effect1
    show willy smile2
    willy"어떻게 보면 네 잘못 이기도 하니까……{cps=2} {/cps}날 좀 도와줄 수 있을까?"
    stephan"그게 왜 내 잘못이야?"
    stephan"네가 주겠다고 한 거니까 네가 책임을 져야 할 거 아님?"
    show willy talk
    willy"아~{cps=2} {/cps}그래~?"
    willy"하지만 난 게임에 관한 건 잘 몰라서 말이야"
    stephan"내 알 봐 아니거든?"
    willy"너 꽤 심한 게임 폐인 이잖아?"
    willy"게임에 대해서 잘 알 거 아니야?"
    stephan"계속 그딴식으로 말 하면 내가 도와 줄 거 같냐?!"
    show willy smile
    willy"……네 게임 센스가 엄청 좋잖아~"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}칭찬으로 얼버무리지 마!{/size}" with lshake
    hide effect1
    show willy
    willy"그럼 이렇게 하자"
    willy"날 도와주면, 내가 점심 한턱 쏜다"
    show stephan talk
    stephan"오?"
    willy"어때?{cps=2} {/cps}괜찮지?"
    show stephan think at left
    stephan"점심이라……"
    extend" 마침 출출하긴 했지만"
    stephan_think"어쩌지……"
    stephan_think"고민된다……"
    hide stephan think
    hide willy
    menu:
        "나의 센스란 말이지?":
            $ pick_game = True
            jump my_sence
        "일단 뭐좀 먹고 난 다음에……":
            $ pick_game = False
            jump just_eatfood
label my_sence:
    show willy at right
    show stephan at left
    stephan"그,{cps=2} {/cps}그렇게 까지 나의 센스가 필요하다면 어쩔 수 없군……"
    stephan"내가 골라 주도록 하지"
    show willy at right
    willy"그럼 어디로 가야 되나요?"
    extend" 게임계의 앙드레 김~"
    show stephan think
    stephan"흠……"
    "내가 알 리가 없다."
    "딱히 밖에 자주 나가는것 도 아니고……{cps=2} {/cps}무엇보다 요즘은 디지털 다운로드 시대라서 굳이 게임을 사러 밖으로 나갈 필요가 없다."
    "어느 가게가 좋을지 내가 알 턱이 없었다."
    "하지만 거의 평생을 집에서 웹서핑을 한 나의 정보력에 의하면……"
    "분명 이곳엔 게임만 전문적으로 판매 하는 상점이 있다고 한다."
    "이름이 \'게임 스\' 뭐시기 였는데……"
    scene bg downtown_outside at Zoom((1280,720),(0,0,1280,720),(0,340,563,316),0.6) with dissolve
    $ renpy.pause(0.8)
    show bg downtown_outside at Zoom((1280,720),(0,340,563,316),(678,316,563,316),0.6)
    stephan"어디보자……"
    show bg downtown_outside at Zoom((1280,720),(678,316,563,316),(428,234,563,316),0.6)
    stephan"앗!"
    show willy:
        zoom 1.4 yalign -0.3 xalign 0.8
    show stephan smile:
        zoom 1.4 yalign -0.3 xalign 0.2
    stephan"저기가 좋을 거 같아!"
    willy"그래"
    scene bg downtown_outside at Zoom((1280,720),(428,234,563,316),(510,286,379,213),0.3) with Dissolve(0.5)
    play bgs "bgs/people.mp3"
    scene bg downtown_gamestore with moveright
    play music "bgm/beat1.mp3"
    show stephan shock:
        zoom 1.5 yalign -0.3 xalign 0.5
    stephan_think"어……"
    scene bg downtown_gamestore at Zoom((1280,720),(0,0,1280,720),(0,0,681,383),0.3) with dissolve
    "게임……"
    show bg downtown_gamestore at Zoom((1280,720),(0,0,681,38),(599,337,681,383),0.3)
    "게임……!"
    scene bg downtown_gamestore at Zoom((1280,720),(599,337,681,383),(0,0,1280,720),0.3) with dissolve
    "게임!!"
    show stephan smile:
        zoom 1.4 yalign -0.3 xalign 0.2
    stephan"우와아아~~!"
    "이렇게 많은 게임과 관련 상품이 진열 된 곳이 있었다니……"
    "만약 천국이 있다면, 분명 이런 모습 일 거라 생각 했다."
    show stephan smile:
        zoom 1.0 yalign 1.0 xalign 0.0
    show willy talk at right
    willy"오~{cps=2} {/cps}꽤 많이 있네"
    stephan"하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악하악"
    show willy shock
    willy"어이,{cps=2} {/cps}침좀 닦아"
    willy"너 완전 변태 같다고"
    stephan"이런 이런"
    extend" 나도 모르게……{cps=2} {/cps}(추릅)"
    willy"그래서 어느 게임으로 할 거야?"
    show stephan think at left
    stephan"흠……"
    "게임……{cps=2} {/cps}정말 많았다."
    "진심 여기서 평생 살 수 있을 것 같았다!"
    stephan_think"사고 싶은 게 엄청 많아……"
    willy"스테반?"
    show willy talk:
        linear 0.5 xalign 0.4
    "불러도 대답이 없자, 윌리는 내 어깨를 콕콕 찔러 본다."
    willy"어이~{cps=2} {/cps}스테반~"
    "……허나 내 정신은 벌써 승천 해 있었다."
    show willy smile2
    willy"훗"
    willy"설마 너도 사고 싶은거냐"
    "……어?"
    show stephan shock at left
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}으에에에엥~?{/size}" with lshake
    stephan"사,{cps=2} {/cps}사줄꺼야~?"
    hide effect1
    show willy shock:
        linear 0.5 xalign 1.0
    willy"윽……!"
    extend" 너 표정이 너무 무서워!"
    willy"그리고 난 아직 사준다고 말 한 적 없어!"
    show effect2
    show stephan sad at left
    play sound "se/shock2.mp3"
    play music "bgm/sad3.mp3"
    stephan"그래……"
    hide effect2
    willy"야,{cps=2} {/cps}왜 그렇게 좌절해 있어?"
    willy"내가 뭐 잘못 말 한거야?"
    willy"내가 나쁜거냐고?"
    scene black with eyeshut
    stop bgs
    stop music
    show stephan smile2:
        zoom 1.5 yalign -0.2 xalign 0.5
    stephan_think"훗"
    "내가 알고있는 윌리는 죄책감에 약하다."
    "나쁜짓을 하고 있다고 생각 하면 다른 좋은 일로 그 걸 덮어버리려는 성격 이랄까"
    "그런 녀석에게 계속해서 죄의식을 주입 시키면 게임을 사줄지도 모른다!"
    stephan_think"그럼 지금부터 나의 완벽한 계획을!"
    scene bg downtown_gamestore with eyeopen
    play music "bgm/sad3.mp3"
    play bgs "bgs/people.mp3"
    show stephan sad at left
    show willy shock at right
    stephan"넌 나한테 희망을 줬어……"
    stephan"방금 사고 싶냐는 말 한마디가 나한테 괜한 기대감을 심어줘가지고……"
    stephan"넌 내가 이런거에 약하다는 거 잘 알고 있잖아"
    stephan"정말 너무해……{cps=2} {/cps}괴물같은 녀석……"
    willy_think"나도 모르게 희망 고문을 시킨건가……"
    willy_think"괜히 죄책감이 들잖아!"
    show stephan smile2
    stephan_think"후후후,{cps=2} {/cps}계획대로 잘 돼 가고 있어……"
    show stephan sad
    show willy think
    willy"에헴!"
    show willy
    willy"그럼 이렇게 하는 게 어떨까?"
    willy"오늘 점심을 안 사주는 대신 여기서 게임을 한 개 사주는 걸로"
    show stephan smile
    show effect1
    play sound "se/shock.ogg"
    play music "bgm/beat1.mp3"
    stephan"{size=55}정마아아알~~~?!{/size}" with lshake
    extend" 게임 사도 돼!?"
    hide effect1
    show willy shock at right
    willy"어,{cps=2} {/cps}어……"
    willy"근데 음식보다 게임을 바로 선택하냐;;"
    show stephan smile2 at left
    stephan_think"후훗……{cps=2} {/cps}계획대로……"
    stephan_think"이제 남은 건……"
    play sound "se/hungry.mp3"
    show stephan shock
    "(꼬르르르륵……)"
    willy"응?"
    stephan"억……"
    show willy shock at right
    willy"너 정말 점심 대신에 게임으로 골라도 괜찮은거야?"
    willy"게임은 뜯어 먹을 수 없다구"
    show stephan smile2 at left
    stephan"후후"
    stephan"뭘 모르는군……{cps=2} {/cps}윌리……"
    stephan"확실히 게임은 뜯어 먹을 수 가 없어……"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}하지만!{/size}" with lshake
    stephan"게임을 하고 있으면 배고픔이 안 느껴지지!!"
    hide effect1
    stephan"그러니 점심밥을 사는 것보단 게임을 사는쪽이 더 효율적이야!"
    willy"뭐야 그 논리;;"
    show willy talk at right
    willy"그리고 내가 부탁한 거 하기 전까진 아무것도 안 사준다고"
    show stephan shock
    stephan"아차"
    show stephan
    stephan"쏘리,{cps=2} {/cps}깜빡했네"
    hide willy talk
    show stephan think:
        linear 0.6 zoom 1.5 yalign -0.2 xalign 0.5
    show bg downtown_gamestore at blur with dissolve
    stephan_think"흠……{cps=2} {/cps}아무거나 대충 사주면 될까?"
    stephan_think"그래도 그 사람의 PX4를 받은 건 나니까, 조금이라도 할만 한 게임을 골라주는 게 좋겠지?"
    "현재 그 사람의 PX4는 내가 가지고 있다."
    "즉, PX4 게임을 사주는 건 무의미"
    "PX4 말고 다른 게임 이라면 SBox랑 MeeU가 있다."
    "……하지만 MeeU를 사는 사람은 없겠지?"
    "솔직히 \'대난투 시스터즈\'랑 \'마리오 슈퍼 카트\' 빼곤 할만한 게 없는데"
    stephan_think"……그냥 물어볼까?"
    stephan_think"하지만 윌리는 게임기에 대해서 잘 모르는다고 했고……"
    show stephan shock
    stephan_think"으아아아{cps=2} {/cps}어쩌지!"
    show bg downtown_gamestore with dissolve
    menu:
        "물어본다.":
            hide stephan shock
            show stephan at left
            stephan"윌리"
            show willy talk at right
            willy"응?"
            stephan"네 룸메이트가 무슨 콘솔을 가지고 있는지 알고 있어?"
            show willy think at right
            willy"콘솔이라……"
            willy"난 게임 전문가가 아니라서 그런건 잘 모르겠네……"
            stephan_think"역시 이렇게 되는 건가……"
            willy"내가 기억하기로 걔가……"
            willy"PX, PX2, PX3, PXP, PXB, SBox, SBox 180, SBox Tow, Mee, MeeU를 가지고 있고……"
            willy"자주 안 쓰지만 일단 \'세가 토성(Saga Satern)\', \'세가 해왕성(Sega Neptune)\', \'세가 창새기(Sega Genesis)\', \'로리콤(Lolicom)\', \'슈퍼 로리콤(Super Lolicom)\' 그리고 아타리에서 만든 이름 모를 콘솔이 6개 정도 더 있었어"
            show willy at right
            show stephan shock at left
            play sound "se/shock.ogg"
            show effect1
            stephan_think"{size=45}얼마나 심한 게임 폐인 인거야!!{/size}" with lshake
            stephan_think"게임 박물관 차려도 되겠어!"
            hide effect1
            stephan"그보다 너 생각보다 잘 알고있네;;"
            willy"하도 많이 말해서 외워 버렸지"
            show stephan at left
            stephan"뭐 덕분에 무슨 게임을 사주는 게 좋을지 알 수 있게 됐어"
            hide stephan
        "혼자서 생각한다.":
            show stephan think:
                zoom 1.5 yalign -0.2 xalign 0.5
            stephan_think"윌리에게 물어봐도 결국엔 무슨콘솔을 가지고 있는지 모를 확률이 높아"
            stephan_think"윌리의 친구 녀석이 게임 폐인 이라면 새로나온 SBOX Two를 가지고 있을 확률이 높아"
            show stephan shock
            stephan_think"아니 잠깐……!"
            stephan_think"내 PX4는 원래 그사람 꺼라고 했어……"
            stephan_think"만약 그사람이 Soni 빠면 어쩌지……!"
            stephan_think"Soni빠 에게 \'마이크로 하드(Microhard)\'의 콘솔을 준다는 건 엄청난 모욕이야……!"
            stephan_think"으……"
            stephan_think"이럴땐 안전하게 PC로 갈까……"
            stephan_think"하지만 PC엔 Stem이 있어서 따로 사줄 필요가 있을까……?"
            stephan_think"아냐,{cps=2} {/cps}너무 고민하지마"
            stephan_think"넌 할수있어! 스테반!"
            stephan_think"나의 감각을 믿어보는거야!"
            show stephan smile2
            stephan"훗,{cps=2} {/cps}정했어"
            hide stephan smile2
    show stephan at left
    show willy at right
    willy"오호……"
    willy"뭘 사줄건데?"
    scene bg downtown_gamestore at Zoom((1280,720),(0,0,1280,720),(535,301,745,419),0.6)
    $ renpy.pause(0.6)
    show stephan:
        zoom 1.4 yalign -0.2 xalign 0.5
    stephan"이걸로 해야지"    
    "나는 SBox Two 게임 코너에 가서 아무 게임이나 짚었다."
    "……물론 완전히 대충 짚은 건 아니고,{cps=2} {/cps}SBox Two에서만 할 수 있는 특전 게임을 짚었다."
    "게임의 이름은 \'선라이즈 오버드라이브(Sunrise Overdrive)\' 다."
    scene bg downtown_gamestore at Zoom((1280,720),(535,301,745,419),(0,0,1280,720),0.5)
    $ renpy.pause(0.5)
    show willy talk at right
    show stephan smile at left
    willy"그럼 넌 뭘로 할 거야?"
    willy"참고로 말하는데 가격은 20달러 이하로 해라"
    stephan"네에~"
    show stephan shock at left
    stephan"에?"
    stephan"2,{cps=2} {/cps}20달러……?"
    willy"어,{cps=2} {/cps}나 지금 가지고 있는 돈이 얼마 없거든"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}20달러 가지곤 게임을 못 사잖아!!{/size}" with lshake
    hide effect1
    show willy shock at right
    willy"넌 받는 주제에 뭐그리 원하는 게 많냐"
    stephan_think"이런……"
    extend" 윌리한테 당했다!"
    "20달러만 가지고 내가 원하는 건 아무것도 못 산다……!"
    "하지만 윌리는 아무것도 사주는 게 아니니까 죄책감을 들 필요가 없어!"
    stephan_think"그딴 계획을……"
    show willy talk at right
    willy"게임을 못 사면 다른걸로 사"
    stephan"다른 거 라……"
    stephan"아!{cps=2} {/cps}HDMI 케이블!!"
    show willy at right
    willy"잘 됐네"
    willy"그럼 빨리 계산 하고 나가자"
    stephan_think"게임을 사지 못 한 건 아쉽지만, 그래도 게임을 하는데 반드시 필요한 건 살 수 있게 됐으니 상관없으려나……"
    play music "se/phone_ring2.mp3"
    $ renpy.pause(2)
    willy"내 전화다"
    stop music
    show willy talk
    show stephan talk
    willy"여보세요?"
    willy"…………"
    willy"어─"
    willy"그래?{cps=2} {/cps}잘 했어"
    willy"그럼 지금 당장 갈게"
    show willy
    stephan"뭔데?"
    willy"집에서 호출"
    willy"난 먼저 가볼게"
    stephan"그래"
    show willy smile2
    willy"HDMI 케이블 샀으니까 이제 집에 가서 바로 게임 할 거지?"
    show stephan shock
    stephan"없었던거 알고 있었어?!"
    willy"설마"
    willy"그리고 너무 게임만 하진 말고,{cps=2} {/cps}눈 나빠진다"
    stephan"그럼 게임을 안 하면 눈이 착해지냐"
    stephan"그리고 나 바로 게임 안 할 거 거든?"
    stephan"할아버지 댁에 갈 거 거든?"
    show willy shock
    willy"그,{cps=2} {/cps}그래;;"
    stop bgs
    play sound "se/move.mp3"
    scene black with moveright
    jump event_end
label just_eatfood:
    show stephan yawn at left
    show willy at right
    stephan"뭐 좀 먹고 난 다음에……"
    willy"하긴……{cps=2} {/cps}너도 경찰서에서 있었던 일 때문에 여러가지로 피곤할테니까"
    show stephan at left
    stephan"그래서 점심은 네가 쏘는거?!"
    show willy talk
    willy"어디서 잔머리를,{cps=2} {/cps}물건 부터 사고 나서 거든?"
    show stephan yawn at left
    stephan"쳇,{cps=2} {/cps}돈은 나도 있다 뭐"
    stephan"점심이 얼마 한다고 진짜"
    stephan"내가 그거 하나 얻어먹으려고 어디 있는지도 모르는 게임 상점을 돌아다니면서 기력을 허비할 바엔 내돈주고 먹는다."
    willy"삐졌어?"
    stephan"아니"
    show willy smile2 at right
    willy"삐졌네"
    show stephan shock at left
    stephan"삐진게 아니라 사실을 말한 거 뿐이야"
    willy"그래─ 그래─"
    willy"그래서 점심은 어디서 먹을 생각이야?"
    show stephan smile at left
    stephan"당연히 햄버거지!"
    "내가 세상에서 재일 좋아하는 음식이다."
    "물론 추하게 아무 햄버거나 먹진 않고,{cps=2} {/cps}이름있는 명품 브렌드에서만 먹는다."
    "\'막도날드(MacDonald)\'나, \'UFC(Utah Fried Chicken)\'같이 말이야"
    show willy talk
    willy"그런거 먹으면 몸에 안 좋다"
    willy"게다가 넌 평상시 운동도 안 하니까 나중에 더 큰일이 벌어질 걸?"
    show stephan talk
    stephan"네가 우리 엄마냐,{cps=2} {/cps}그런 말 하게"
    willy"그럼 좀 들어"
    show stephan smile
    stephan"싫은데~☆"
    show willy shock:
        linear 0.4 xalign 0.5
    willy"그 짓 다시는 하지마;;"
    show stephan shock
    stephan"어,{cps=2} {/cps}어……"
    show stephan shock2
    stephan"그래서 햄버거 먹으러 갈 건가?"
    show willy:
        linear 0.4 xalign 1.0
    willy"뭐 가끔은 기분 좀 다른 걸 먹어보는 것도 괜찮을 거 같네"
    willy"좋아"
    willy"위치는 알아?"
    stephan"아니"
    stephan"근데 여긴 나라에서 2번째로 밀집한 지역이니까 어딘가 있겠지"
    stephan"수요와 공급 법칙 이라고 있잖아?"
    show willy shock at right
    willy"계획도 없이 먹자고 한 거냐;;"
    show stephan fear
    stephan"모든 사람이 너 처럼 계획적 이라고 생각하지 마!"
    stephan"예기치 못한 일이 얼마나 두근거리는지 알아?"
    show willy talk
    willy"그 마음은 나도 이해 할 수 있을거 같네"
    show willy shock
    willy"근데 그거 때문에 아무것도 예상하고 있지 않으면 안 되지"
    stephan"몰라!{cps=2} {/cps}빨리 햄버거 집이나 찾으러 가자"
    show willy talk
    willy"그럼 저기 있는 햄버거 집은 어때?"
    willy"야채 버거 라는데?"
    show stephan talk
    stephan"난 명품 아니면 안 먹어"
    show willy shock
    willy"어?"
    stephan"UFC, 막도날드, 버거 퀸 같이 이름 있는 데 아니면 안 먹을거야"
    willy"뭐야 그거,{cps=2} {/cps}엄청 귀찮아"
    willy"스테반, 편식 하면 안 좋다고 어렸을때 들어봤어?"
    show stephan
    stephan"윌리, 길에서 아무거나 주워먹으면 안 좋다고 어렸을때 들어봤어?"
    willy"어째서 야채 버거가 아무거나냐?"
    stephan"그런 위험해 보이는 음식을 먹었다가 배탈나면 어쩌려고?"
    willy"고소하면 되지"
    show stephan shock
    stephan"Aㅏ……"
    stephan_think"반박을 못하겠어!"
    show stephan shock2
    stephan"그,{cps=2} {/cps}그래도 좀 이름있는 곳 에서 먹는 게……"
    willy"알았어─{cps=2} {/cps}알았어─"
    stop bgs
    scene black with Dissolve(1.5)
    "우리는 조금 더 걸어서 UFC 치킨 집을 찾았다."
    play sound "se/move.mp3"
    play bgs "bgs/people.mp3"
    scene bg downtown_fastfood_counter at Zoom((1280,720),(203,201,765,430),(203,201,765,430),0.0) with moveleft # KFC 내부
    centered"UFC 치킨 집 안"
    "이곳은 \'유타 프라이드 치킨(Utah Fried Chiken)\', 줄여서 UFC다."
    "이름대로 치킨으로 유명한, 그리고 내가 인정하는 몇 안되는 명품 햄버거집 이기도 하다."
    $ extra_name = '점원'
    extra"주문 도와 드리겠습니다"
    show willy talk at right
    show stephan think at left
    stephan"음……"
    stephan_think"뭐가 좋을까……"
    stephan_think"UFC는 별로 안 와서 뭐가 좋을지 잘 모르겠네"
    show stephan talk at left
    stephan"윌리, 넌 뭐 먹을거야?"
    willy"난 \'그린맥스버거\'세트로 하지.{cps=2} {/cps}뭔진 모르겠지만, 맛있어 보여"
    stephan"그럼 난  무난하게 \'징그러버거\'세트로"
    extra"\'그린맥스버거\'세트랑 \'징그러버거\'세트면 되시나요?"
    stephan"네"
    willy"계산은 따로 해주세요"
    extra"네, 알겠습니다"
    show stephan shock at left
    stephan_think"이 녀석, 정말로 안 사줄 생각이었군;;"
    play sound "se/move.mp3"
    scene bg downtown_fastfood_counter with moveright
    $ renpy.pause(0.5)
    show ev fastfood_sit with moveup
    $ renpy.pause(0.7)
    show stephan smile:
        zoom 1.4 yalign -0.1 xalign -0.1
    show willy talk:
        zoom 1.4 yalign -0.1 xalign 0.85
    stephan"(우물우물)"
    stephan"이야─{cps=2} {/cps}역시 햄버거야"
    stephan"날 실망 시키지 않아"
    play sound "se/search_bag.mp3"
    willy"음……"
    willy"(쩝쩝)"
    willy"그럭저럭 먹을만 하네"
    stephan"그럭저럭?"
    willy"솔직히 이런거 별로 좋아 하지 않다 보니까……"
    show stephan shock
    stop music
    stephan"햄버거를 좋아하지 않는다고?"
    stephan"어,{cps=2} {/cps}어떻게……{cps=2} {/cps}그럴 수 있는거지……?"
    willy"어?"
    play music "bgm/sirius1.mp3"
    show stephan talk
    stephan"너, 이상해……"
    show willy shock
    willy"뭐야 이 분위기;;"
    stephan"햄버거 같이 완벽한 식품을 좋아하지 않는다……"
    stephan"도대체 정체가 뭐야?"
    willy"패스트 푸드 먹으면 살찌잖아"
    stephan"자네 방금 살찐다……{cps=2} {/cps}라고 했는가?"
    willy"왜?{cps=2} {/cps}맞잖아"
    show stephan smile2
    play music "bgm/sirius4.mp3"
    stephan"살찌는 게 뭐가 나쁘다고 생각하는거지?"
    stephan"비만은 인류가 발전 했다는 것을 알려주는 증거라고!"
    stephan"과거 인류는 굶어서, 다른 이에 의해서 혹은 전쟁에서 개인의 의지와는 관계 없이 죽었지"
    stephan"하지만 지금은 어떠한가?"
    stephan"자살, 비만, 질병……"
    stephan"모두 개인의 선택과 오만함에 의해서 죽어!"
    stephan"비만이야 말로 우리 인류가 발전 했다는 증거야"
    stephan"과거에 자신의 목숨은 \'자신\'의 것이 아니었지만, 지금 우리는 기술과 환경의 발전으로 자신의 목숨은 자신의 것이 됐어!"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}비만은 인류의 독립을 증명 해준다!!{/size}" with lshake
    stephan"그리고 비만의 원인으로 기여도가 높은 햄버거는 독립의 상징이지!"
    hide effect1
    stop music
    willy"…………"
    show willy smile2
    willy"뭐래 ㅋ"
    play music "bgm/beat2.mp3"
    show stephan fear
    stephan"비웃지 마!"
    willy"네가 엄청 뜬금없는 소리를 하잖아"
    stephan"나,{cps=2} {/cps}나름 깊게 생각 한 건데……!"
    willy"그건 깊은 게 아니라, 그냥 하고 싶은 데로 하기 위한 핑계야"
    stephan"아니거든……"
    show willy
    willy"그래─{cps=2} {/cps}그래─"
    willy"근데 이거 생각보다 먹을만 하네?"
    show stephan smile
    stephan"그치?!"
    show willy shock
    willy"어,{cps=2} {/cps}어─"
    show stephan talk
    stephan"(냠냠)"
    show willy talk
    stephan"…………"
    "갑자기 분위기가 조용해졌다."
    "뭔가 할 말도 없고……"
    extend" 가만히 서로가 주문한 음식만을 쩝쩝대고……"
    "빨리 대화에 진전이 있어야 게임이 재미있어질텐데 말이다."
    show stephan shock2
    stephan"그거 알아?{cps=2} {/cps}몇 달 후에 \'애시스 크리드(Asses Creed)\'파이브 출시 한다네"
    stephan"근데 이름에 파이브는 없고, 대신 유니티가 붙는데"
    willy"그래?"
    willy"……근데 애시스 크리드가 뭔데?"
    show stephan shock
    stephan"몰라?"
    willy"무슨 게임 인가?"
    show stephan
    stephan"어,{cps=2} {/cps}꽤 재미있음"
    stephan"……물론 3편 빼곤"
    show stephan mad
    show willy shock
    stop music
    stephan"내가 3편을 출시 1달 전에 골드 에디션으로 샀는데……"
    stephan"아오 진짜……{cps=2} {/cps}내 피같은 90달러"
    willy"왜 예약구매 같은 걸 하냐;;"
    stephan"아이템 이랑 미션을 하나 추가로 준다길래……"
    stephan"근데 둘 다 쓸모가 없더라고"
    willy"난 사람들이 뭔가를 예약 구매 하는 게 정말 이해가 안 가더라"
    willy"딱히 할인이 되는것도 아닌데 왜 먼저 사려는 걸까?"
    stephan"전부 망할 기업 자식들의 상술인거지"
    stephan"발렌타인 데이 같이 말이야……"
    play music "bgm/beat4.mp3"
    show willy smile2
    willy"그건 그냥 네가 한번도 초콜렛을 받아본 적이 없어서 잖아"
    show stephan shock
    stephan"아니야!"
    stephan"나,{cps=2} {/cps}나도 받아본 적이 있다고!"
    show willy talk
    willy"오?{cps=2} {/cps}내가 준 우정 초콜렛 이외에 받아본적이 있어?"
    stephan"…………"
    show stephan mad
    stephan"예약 구매는 전부 나쁜 기업들의 상술이야!"
    show willy shock
    willy"내 질문 회피 하지마"
    stephan"기업들은 돈이 그렇게도 좋은거냐?!"
    stephan"돈을 위해서 탈세도 하고, 노이즈 마케팅 같은 걸로 사람들을 속이고!"
    stephan"녀석들이랑 싸이코 패스랑 뭐가 달라?!"
    stephan"도둑 노므 새끼들!"
    willy"네 손실을 기업의 탓으로 돌리는거냐?"
    willy"그냥 네가 좀 더 바람직한 소비자가 되면 되는 걸……"
    stephan"기업들은 약한 소비자들의 마음을 이용해서 자신들의 이익을 챙기고……"
    stephan"용서 못해"
    show willy talk
    willy"스테반"
    stephan"왜"
    willy"혹시 여자한테 인기 있고싶어?"
    show stephan shock
    stop music
    stephan"어……?"
    stephan"왜 갑자기 대화를 그쪽으로?"
    show willy shock
    willy"내가 먼저 너한테 초콜렛 질문을 했거든?"
    willy"질문을 회피 한 건 너잖아"
    show stephan shock2
    stephan"이,{cps=2} {/cps}이건 회피가 아니라 작전상 후퇴 라고……"
    willy"알았어 알았어"
    show willy talk
    play music "bgm/sirius1.mp3"
    willy"그래서……{cps=2} {/cps}여자한테 인기 있고 싶어?"
    show stephan shock
    stephan"그런게 가능해?"
    show willy smile2
    willy"그럼,{cps=2} {/cps}당연하지"
    show stephan smile
    stephan"어떻게 하면 돼?!"
    willy"60달러 만 줘"
    show stephan shock
    stephan"어?{cps=2} {/cps}왜?"
    willy"\'인센티브(Incentive)\'"
    stephan"치,{cps=2} {/cps}친구에 대한 우정의 힘으로는……{cps=2} {/cps}안 되나?"
    willy"우정 이라면 7개월 전에 우정 초콜렛으로 때웠잖아"
    stephan"그럼 내가 60달러를 준 뒤에 만약 나한테 효과가 없으면?"
    show willy talk
    willy"그건 네 팔자지"
    show stephan yawn
    stephan"안 해"
    show willy smile2
    willy"그럼 내가 알고있는 여자 한명을 소개 시켜줄게"
    willy"그렇게 하면 내가 알려 준 방법이 효과 있는지 없는지 바로 확인 할 수 있잖아?"
    show stephan shock
    stephan"…………"
    stephan_think"그,{cps=2} {/cps}그냥 해버릴까?!"
    stephan_think"나한테 여자친구가 생길 수 있는 기회 일지도 모르는 건데?!"
    show stephan think
    stephan_think"게다가 아는 여자 까지 소개 시켜준다고 했고……"
    show stephan talk
    stephan"설마 소개 시켜준다는 여자가 멜 누나 이거나 하진 않겠지?"
    show willy shock
    willy"내가 미쳤냐?{cps=2} {/cps}너같은 사람한테 누나를 소개 시켜주게?"
    show stephan shock
    stephan"나 조금 상처 받았는데……"
    show willy smile
    willy"네가 전혀 모르는 여자를 소개 시켜 줄 거니까 걱정 마!"
    show willy smile2
    willy"게다가 내가 봤을때도 좀 예뻐"
    show stephan smile
    stephan"올?!"
    willy"어때?{cps=2} {/cps}지금 60달러만 주면 내가 내일부터 제대로 비밀을 알려 줄게"
    show stephan shock
    stephan"내일?"
    willy"평일 이잖아.{cps=2} {/cps}학교에서 내가 시범을 보여주면서 하는 게 더 효과적 일 거 같아서"
    show stephan smile
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}좋았어!{/size}" with lshake
    stephan"여기 내 돈!"
    hide effect1
    "나는 윌리에게 10달러 지폐 6장을 건넸다."
    willy"돈은 확실히 받았어 흐흐흐"
    stop music
    show willy
    willy"그래서 \'망할 기업 자식들의 상술\'에 당해본 기분은 어때?"
    show stephan shock
    stephan"어……?"
    play music "bgm/beat2.mp3"
    show willy smile
    willy"방금 네가 나한테서 게임 같이 무형 물질인 \'연애 기술\'이라는 걸 본인이 직접 보기도 전에 샀잖아"
    willy"게다가 내가 여자를 소개 시켜 주겠다는 걸 끼워주므로써 예약 구매의 인센티브를 추가 시켰지"
    willy"마치 게임에서 아이템과 미션을 예약 특전으로 주듯이 말이야"
    stephan"…………"
    willy"그저 너의 \'니드(Need)\'를 분석한 것 만 가지고 난 물건도 주기도 전에 60 달러를 먼저 받았어"
    willy"근데 내가 싸이코 패스 일까?{cps=2} {/cps}내가 도둑 노므 새끼들 인가?"
    stephan"그럼 나한테 인기 많아지는 비결은 안 가르쳐 주는거야……?"
    show willy shock
    willy"그래……"
    show stephan mad
    stephan"그럼 넌 싸이코 패스랑 도둑 노므 새끼를 초월 한 존재야"
    stephan"감히 어리고 순수한 소년의 마음을 가지고 놀다니……"
    willy"네 입으로 말 하기냐?"
    willy"그리고 자, 60달러 돌려줄게"
    play sound "se/search_bag.mp3"
    stephan"…………"
    stephan"정신적 피해 보상은?"
    willy"어?"
    stephan"나의 마음을 가지고 논 피해 보상은?!"
    willy"어이,{cps=2} {/cps}네 약점을 보여준 건 너잖아"
    willy"왜 나한테 피해 보상을 요구하는거야?"
    show stephan fear
    stephan"넌 언제나 여자들한테 인기가 있어서 모르겠지만, 나한텐 타격이 크다고!"
    willy"뭐라……"
    show stephan sad
    stephan"흑……{cps=2} {/cps}흑……"
    stephan"17년 간의 솔로의 고통을 네가 알리가 없지……"
    show willy talk
    willy"나도 딱히 여자를 사귀어본 적이 있는것도 아닌데……"
    stephan"그,{cps=2} {/cps}그래도 여자들이 줄을 서는 너랑은 다르다고!"
    stephan"흑……"
    show willy shock
    willy"왜그렇게 날 과대평가 하는거야,{cps=2} {/cps}난 별로 인기도 없는데"
    stephan"흑흑"
    willy"…………"
    play sound "se/move.mp3"
    scene black with moveleft
    centered"오후 2시 2분"
    play bgs "bgs/market.mp3"
    scene bg downtown_outside with moveleft
    show stephan smile at left
    show willy shock at right
    stephan"에그타르트 ㄳ"
    willy"진짜 귀찮네"
    willy"너 때문에 내가 점점 착해지는거 같아"
    stephan"좋은거잖아"
    willy"아, 몰라"
    play music "se/phone_ring2.mp3"
    $ renpy.pause(2)
    show willy talk at right
    willy"잠깐만 실례"
    stop music
    willy"여보세요?"
    willy"어, 그래─"
    show willy shock at right
    willy"알았어;;"
    willy"지금 돌아갈게"
    "윌리는 통화를 끝내고 나한테 말 했다."
    show willy at right
    willy"집에서 나를 호출하는 바람에 먼저 가봐야 할 듯하네"
    willy"그럼 월요일날 학교에서 보자"
    show stephan at left
    stephan"게임은 안 사?"
    willy"지금 좀 급한일이 있어서 그냥 관 둘려고"
    stephan"그래, 잘가"
    show willy:
        linear 0.5 xalign 1.6
    play sound "se/footsteps_running.mp3"
    $ renpy.pause(3)
    stephan_think"난 이왕 나온김에 게임을 하는데 필요한 HDMI나 사서 돌아갈까……"
    stop bgs
    scene black with dissolve
    "나는 근처 가전제품만을 전문으로 파는곳에서 1미터짜리 HDMI캐이블을 구매했다."
    "……바로 집에 돌아가고 싶긴 하지만, 일단은 할아버지 한테 먼저 들린 뒤 가야겠다."
    "오늘이 주말의 마지막 날 이니까"
label event_end:
    scene black with moveright
    centered"오후 2시 47분"
    centered"할아버지의 저택"
    play music "bgm/smooth3.mp3"
    play sound "se/door_open.ogg"
    scene bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(332,295,640,361),0.0) with dissolve # 저택 거실
    show stephan at left
    show cia at right
    stephan"실례 하겠습니다"
    cia"어서 오세요.{cps=2} {/cps}도련님!"
    stephan_think"\'도련님\'소리……{cps=2} {/cps}정말 언제 들어도 질리지가 않아~"
    show stephan think at left
    stephan_think"하지만 여기서 메이드 복을 입고 \'주인님~\'이라고 해줬으면 ㄷ……"
    show cia think
    cia"도련님 오늘 말 해야 하는……"
    show stephan shock at left
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}오,{cps=2} {/cps}오해야!!{/size}" with lshake
    stephan"난 아무 생각도……!"
    hide effect1
    show cia talk
    cia"네?"
    cia"갑자기 왜그렇게 수상하게 행동 하세요?"
    stephan_think"이런 갓 뎀!"
    stephan_think"망했다!"
    "거짓말이 어설픈 나에게 그 이상 추궁을 하면 나도 모르게 솔직히 말 할지도 모른다."
    "그렇게 되면 분명 나를 변태 오타쿠 라고 생각 할거야"
    "……난 그런게 아니니까 말이야!{cps=2} {/cps}절대 아니라고!"
    "이 상황을 어떻게 해서든 빠져나간다!"
    show stephan shock2
    stephan"수,{cps=2} {/cps}수상하다니?!"
    stephan"누가 상이라도 탔어?!"
    stop music
    cia"…………"
    show cia think at right
    cia"누,{cps=2} {/cps}누가 이 추운 날씨에 에어콘을 튼거지……?"
    cia"꺼야겠다 헤헤……"
    play sound "se/footsteps_wood.mp3"
    show cia think:
        linear 1.0 xalign 1.8
    "그렇게 시아는 상황을 유유히 빠져나갔다."
    hide cia think
    play music "bgm/smooth3.mp3"
    show stephan think at left
    stephan_think"이상하네, 좋은 드립 이라고 생각 하는데……"
    "하지만 난 이런 드립은 언제나 맞을 걸 각오 하면서 치기 때문에 크게 신경쓰이진 않았다."
    show stephan
    stephan_think"그보다 할아버지한테 인사부터 드려야 겠다"
    stephan"할아버지는 윗층에 계시지?"
    scene bg mansion_hall at Zoom((1280,720),(0,0,1280,720),(260,69,474,267),0.0) with moveup
    show cia
    "멀리서 에어콘을 끄는 척 하던 시아가 내 말에 대답했다."
    cia"네!"
    cia"오늘은 의사 선생님이 찾아 오시는 날이라서 아마 하루 종일 방에 계실 거예요"
    show cia shock
    cia"아, 맞다!{cps=2} {/cps}그러고보니까 제가 그거랑 관련해서 할 얘기가 있었는데"
    show cia talk
    cia"그게……{cps=2} {/cps}스테반 도련님은 할아버님의 손자 이기도 하니까……"
    cia"꼭 말 해야될 거 같아서요"
    stephan"음? 어떤거?"
    stop music
    show cia think
    cia"그게……"
    cia"할아버님 께서 며칠 전에 쓰러지신적이 있어요"
    stephan"어?!"
    stephan_think"쓰러지셨다고?!"
    cia"저보곤 도련님한텐 비밀로 해달라고 부탁 하셨지만……{cps=2} {/cps}어제 도련님을 처음만나고 나니까 좀 힘들거 같아서요"
    cia"그리고 오늘은 의사 선생님도 찾아 오셨어요"
    cia"쓰러지고 나서부터 몸이 좀 불편해지셨다고 하던데……"
    cia"지금은 증상이 많이 호전된 상태지만 언제 또 그런일이 생길지 모른데요……"
    stephan"…………"
    play sound "se/footsteps_running.mp3"
    scene black with moveright
    "나는 할아버지의 방을 향해서 전력으로 달렸다."
    play music "bgm/sad3.mp3"
    "어제 처음 할아버지를 만났을때 부터 들었던 기분이었다……"
    "불안하고……{cps=2} {/cps}등골이 오싹해지는 기분"
    show grandpa talk:
        alpha 0.0 xalign 0.8 yalign 1.0 zoom 2.4
        linear 0.6 alpha 0.4
    "생각해보니까 할아버지가 지팡이를 들고 계셨다."
    "……내가 5년 전에 봤을땐 분명 없었는데"
    stephan_think"도대체 어떻게 돼 가는거야……"
    play sound "se/think.mp3"
    scene bg room_stephan_night with flash
    show stephan smile
    grandpa"콜록{cps=2} {/cps}콜록"
    grandpa"급하다고 하면 급하다고 할 수 있지……"
    scene black with flash
    "그저 불안 할 뿐이다……"
    scene bg mansion_bedroom with moveleft# 할아버지의 방 배경
    show stephan shock:
        zoom 1.5 yalign -0.2 xalign 0.5
    play sound "se/door_open.ogg"
    $ renpy.pause(0.5)
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}할아버지!!{/size}" with lshake
    hide effect1
    hide stephan shock
    show extra_doctor with dissolve
    $ extra_name = '의사'
    extra"쉿!"
    extra"토머 씨는 방금 잠드셨습니다"
    show extra_doctor at right
    show stephan shock at left
    stephan"아……{cps=2} {/cps}네……"
    "할아버지 옆엔 청진기와 이런저런 의료 기기를 들고있는 의사로 추정되는 중년의 남성이 앉아있었다."
    "내가 예상했던 할아버지의 상황과는 다르게 이분은 목소리도, 말투도 매우 나긋하고 침착했다."
    stephan_think"……큰 일은 아닌가?"
    extra"혹시 토머 씨의 손자분 이신가요?"
    show stephan talk at left
    stephan"네……"
    extra"여기서 이렇게 만나게 될줄이야~"
    extra"토머 씨 한테서 이야기 자주 들었어요"
    stephan"혹시 할아버지의 치료를 하고 있는 의사 선생님 이신가요?"
    extra"네"
    stephan"할아버지는 어떻죠?!"
    stephan"상태가 심각한가요……?"
    extra"아뇨"
    extra"그렇게 까지 심각한 건 아니에요"
    extra"그냥 당뇨병 증상이 조금 보여가지고 인슐린 주사를 맞추고 있었어요"
    show stephan shock at left
    stephan"당뇨병이면 심각한거 아니에요?!"
    extra"원래 이 나이가 되면 그런게 걸리기 쉬우니까 너무 걱정하실 필요는 없어요"
    extra"적어도 아직까진……"
    stephan"아직까지 라니……"
    extra"토머 씨가 연세가 있으시다보니 합병증이 생길 위험이 있어서요"
    stephan"…………"
    extra"저는 입원을 권하는데 토머 씨는 계속 여기에 있겠다고 하시니까 좀 문제 이기도 하죠"
    extra"계속 무언가를 찾을때 까지 기다리겠다고 하시던데……"
    stephan_think"그 퍼즐을 말씀 하시는 건가……?"
    stephan"그랬군요……"
    extra"뭔가 아시는거 있어요?"
    stephan"조금은요……"
    show stephan at left
    stephan"근데, 정말로 할아버지의 상태는 걱정 할 정도는 아닌거죠?"
    extra"네, 원래 나이가 들면 몸 구석구석이 망가지기 시작하니까요……"
    extra"하지만 토머 씨 같은 경우엔 오히려 몸이 꽤 건강한 편 이라고 보셔도 돼요!"
    show stephan talk
    stephan"제가……{cps=2} {/cps}할아버지가 얼마 전에 쓰러지신적이 있다고 들었는데……"
    stephan"혹시 그거랑 관련해서 몸에 다른 문제가 있거나 하진 않겠죠?"
    stephan"당뇨병 이외에……"
    extra"…………"
    extra"이름이 어떻게 되죠?"
    stephan"제 이름이요?"
    extra"네"
    stephan"스테반 토머 입니다"
    extra"스테반 씨……"
    show stephan shock
    extra"병은 환자와 그의 주변 사람들의 \'걱정\'으로 인해서 더 심각하게 바뀝니다"
    extra"……제가 해 드릴 수 있는 말이 그정도네요"
    scene black with Dissolve(1.0)
    "방금 전에 의사 선생님의 말투……{cps=2} {/cps}왜 그렇게 침착하고 나긋하게 말 하고 있었는지 알 것 같았다."
    "또 생각해보니까 선생님은 단 한번도 할아버지의 상태가 좋다고 한적이 없다."
    "그저 \'걱정\'하지 말라고만 할 뿐……"
    "하지만 내가 뭘 할 수 있겠는가"
    "그냥 할아버지의 부탁을 빨리 들어주고……{cps=2} {/cps}기쁘게 만들어주기만 하면 된다."
    "하지만……"
    show grandpa:
        zoom 2.0 xalign 0.0 yalign -0.3 alpha 0.0
        linear 0.5 alpha 1.0
    show willy talk:
        zoom 2.0 xalign 1.0 yalign 0.0 alpha 0.0
        linear 0.5 alpha 1.0
    "윌리와 할아버지……{cps=2} {/cps}도대체 무슨 일이 있는 걸까"
    stephan_think"그냥 내가 너무 깊게 생가 하려는 걸 거야……"
    jump chapter2
