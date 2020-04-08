##############################################################################################
#################################여기에서부터 게임이 시작합니다.############################################
##############################################################################################
label start:
    $ save_name = "0.프롤로그"
    play sound "se/heartbeat.mp3"
    stop music
    scene black with flash
    $ renpy.pause(1)
    play music "bgs/space.mp3" fadein 2.0
    scene bg galaxy at blur with eyeopen:
        size(1280,720)
        crop(640,0,640,360)
    $ renpy.pause(1.0)
    show splash with moveright:
        zoom 0.5 xalign 0.0 yalign 1.0
    $ renpy.pause(1)
    hide splash with moveright
    play sound "se/heartbeat.mp3"
    scene bg galaxy at blur with flash:
        size(1280,720)
        crop(0,360,640,360)
    $ renpy.pause(0.5)
    show text "{font=fonts/Type_Writer.ttf}{size=55}Story/Programing - 김훈{/size}{/font}" at left with moveright
    $ renpy.pause(1)
    hide text with moveright
    play sound "se/heartbeat.mp3"
    scene bg galaxy at blur with flash:
        size(1280,720)
        crop(640,360,640,360)
    $ renpy.pause(0.5)
    show text "{font=fonts/Type_Writer.ttf}{size=55}CG - 옥율{/size}{/font}" at left with moveright
    $ renpy.pause(1)
    hide text with moveright
    scene bg galaxy at Zoom((1280,720), (320,180,640,360),(0,0,1280,720),0.0) with Dissolve(1.0)
    show expression (StarField().sm) as starfield with dissolve
    show title with dissolve
    $ renpy.pause(3)
    hide title with moveup
    "\'우주(Space)\'……" with moveup
    "매우 신비롭고, 우리가 아직 모르는 게 많은 미지의 공간이다."
    show ev quantum:
        alpha 0
        linear 2.0 alpha 1.0
    "그리고 \'양자역학(量子力學, Quantum Mechanics)\'……"
    "우주와 마찬가지로 매우 신비롭고, 우리가 아직 모르는 게 많은 미지의 공간"
    show ev quantum:
        linear 2.0 alpha 0.5
    "그런 의미에서 둘은 비슷하다고 할 수 있다."
    "사실 생긴것도 꽤나 흡사하다."
    "원자핵 주변을 둥글게 도는 전자, 행성 주변을 둥글게 도는 위성."
    "허나 사실 둘의 존재는 전혀 다르다."
    "우선 전자는 원자핵 주변을 도는 것이 아니라, 주변에 분포 돼 있을 뿐이다."
    "그리고 행성 주변을 도는 위성 같은 경우 완벽한 원형으로 도는 것이 아니라, 타원에 가깝게 돈다."
    show ev quantum:
        linear 2.0 alpha 0
    "즉, 둘이 비슷하다고 생각하는 것은 바로 우리들의 \'착각\'일 뿐"
    "다순히 표면상으로 보이는 것과 느껴지는 감각만으로 판단해서 생기는 오류라고 할 수 있다."
    "그래서 인류는 \'수학(Mathematics)\'이라는 학문을 이용한다."
    "과학이 우리가 사는 세상에 대해서 실질적인 해석을 하는 학문이라면, 수학은 그걸 증명·전달 하는 매체라고 보면 된다."
    "좀 더 쉽게 말하자면……"
    hide ev quantum
    "수학은 우리들(인류)이 무언가를 논리적·객관적으로 표현할 때 사용되는 일종의 \'언어\' 같은 것이다."
    "그리고 과학은 인류가 존재하기 훨씬 전부터 있었던 것"
    "즉, 수학이 인간의 언어라면, 과학은 바로 신의 언어라 볼 수 있다."
    "그리고 수학이 순수 인간이 만들어낸 학문 인 만큼, 그것은 완벽하지 못하다."
    "확실히 눈과 감각만으로 판단하는 것 보단 훨씬 좋을지 몰라도, \'진리(Truth)\'에 도달하기엔 턱없이 부족하다."
    "왜냐면 수학에도 \'오류\'가 존재하기 때문이다."
    "예를 들어서 √2(루트 2) 를 생각해보자."
    "√2를 풀면 답은 1.41421… 이 된다."
    "순환 하지 않는 \'무한\' 소수다."
    "하지만 무한은 결코 존재할 수 없다."
    "이것을 한번 시각적으로 표현 해보겠다."
    show op1 at right with dissolve:
        yalign 0.5
    show op1 at right:
        yalign 0.5
        linear 0.4 xalign 0.5
    "여기 있는 이 빚나는 사각형을 생각해보자"
    show op2 with dissolve:
        yalign 0.5 xalign 0.5
    "그리고 이때 이 사각형의 밑변과 높이는 1인 정사각형 이다."
    hide op1
    show op3:
        yalign 0.5 xalign 0.5
    show op4:
        yalign 0.5 xalign 0.5
    show op4:
        yalign 0.5 xalign 0.5
        linear 1.0 xalign 0.0
    hide op4 with dissolve
    "이번엔 사각형을 대각선으로 잘라서 삼각형을 만들어 보겠다."
    "삼각형의 빗변을 구하는 방법은 \'피타고라스의 정리\'를 이용하면 된다."
    "피타고라스의 정리란, 이름대로 피타고라스라는 고대 그리스의 철학자가 정리한 직각삼각형에 대한 공식이다."
    "밑변(a)의 길이의 제곱과 높이(b)의 제곱을 더하면 반드시 직각삼각형의 빗변(c)의 길이의 제곱이 나온다는 공식인데……"
    "짧게 정리 하자면 a² + b² = c²이다."
    "이번엔 한번 이 빛나는 직각삼각형에 피타고라스의 정리를 대입해서 빗변을 구해보겠다."
    "이 삼각형의 경우 a² = 1, b² = 1 이므로 c² = 2……"
    show op5 with dissolve:
        yalign 0.5 xalign 0.5
    "삼각형의 빗변 즉, c = √2 다."
    "그리고 여기서 부터 인간의 언어의 오류가 나타난다."
    "수학적으로 √2는 절대로 끝이 없으며 순환도 하지 않는 무한 소수다."
    hide op5
    hide op2
    show op6:
        yalign 0.5 xalign 0.5
    "하지만 물리적으로 √2는 시작과 끝이 있는 \'유한\'이다."
    "수학적으로 √2는 끝이 없지만, 같은 길이를 가진 이 빗변엔 끝이 존재한다."
    "많은 수학자들이 이 문제를 가지고 고민했지만, 난 이것에 대해서 스스로에게 결론을 지었다."
    "수학은 완벽하지 못하다."
    "완벽하지 못하기 때문에 이러한 모순이 발생하는 것이라 나는 생각한다."
    scene bg galaxy with moveright
    show expression (StarField().sm) as starfield with moveright
    "여담이지만 방금 내가 설명한─일명 \'페러독스\'─를 처음 발견한 사람은 바로 \'엘레아의 제논(Zeno of Elea)\'이라는 고대 그리스의 수학자이자 철학자이다."
    "그럴때마다 난 생각한다."
    "\'만약 내가 고대 그리스에 태어났더라면 어땠을까?\', \'혹시 나도 위대한 수학자가 될 수 있지 않았을까?\' 하고"
    "이런 단순한 계산식을 발견한 것 만으로 위대한 인물 취급을 하는 걸 보면 그럴싸하다."
    "실제로 앞서 내가 설명한 \'제논의 페러독스\'는 내가 혼자서 스스로 발견한것이다."
    "즉, 이런 나라도 가망은 있다는 뜻"
    "하지만 현실적으로 생각해보자"
    "내가 고작 나무에서 사과가 떨어지는 걸 보고 아이작 뉴턴과 같은 결론에 도달하였다고 해도, 난 절대 뉴턴만큼 똑똑해질 수 없다."
    "왜냐면 지금까지 난 뉴턴과 다른 삶을 살아왔으니까"
    "그리고 현대 시대엔 고대 그리스나 르네상스 시대 보다 훨씬 많은 정보를 접 할 수 있다."
    "아무것도 없이 그들과 같은 결론에 도달 한다는 건 나로썬 불가능하겠지"
    "그럼 내가 그들을 따라잡을 수 있는 건 과연 무엇일까?"
    "이론도, 환경도 이미 그들과 다른 나의 삶에서 내가 그들과 공유할 수있는 것은 무엇인가?"
    "바로 \'철학(哲學, Philosophy)\' 이다."
    "비록 수식도, 발견하게 된 경위도, 환경도 다르다 하더라도"
    "자신이 도달한 결론의 의미는 모두 같다."
    "그 결론에 대한 신념도 모두 같다."
    "전부 우리가 살고 있는 세상에 대해서 조금이라도 더 알기 위해서 만든 이론들이다."
    "즉, 결과물에 담긴 이념과 철학은 모두 같다."
    "허나, 난 철학을 그렇게 긍정적으로 보지 않는다."
    "첫번째 이유로, 인간의 삶에 가장 필요한 \'사회성\'이 철학엔 결여되어있다."
    "단순히─결코 틀린말은 아니지만─철학을 연구했던 사람들 중에 괴짜가 많아서 하는 소리가 아니다."
    "\'사회성\'은 즉, 자신 뿐만 아닌 다른 사람들에게도 의미전달이 잘 돼야 한다는 뜻이다."
    "다르게 말 하자면 '보편성' 이라고 할 수도 있겠지"
    "철학은 전부 해석하기 나름이고, 수학이나 과학같이 객관적이 자료를 바탕으로 하는 게 아니라, 단순히 논리 만 가지고 한다."
    "그 증거로 \'종교(Religion)\'가 있다."
    "확실히 과학에서도─주로 양자역학에서─특정 이론에 대해 편갈리는 경우가 있지만, 불교, 크리스트교, 이슬람교 같은 경우는 말이 필요없다."
    "그도 그럴만한 게─철학은 수학이나 과학보단 비교적 보수적인 성향을 띄기 때문이다."
    "물론 그게 나쁘다는 건 결코 아니다."
    "다만 그러한 성향 때문에 좋아할 사람들은 계속 좋아하고, 싫어할 사람은 계속 싫어하게 되기 때문이다."
    "수학 과학은 아무리 이해가 안 가는 부분이 있어도, 누군가 새로운 이론을 만드므로써 난해했던 부분을 보충하는 것이 가능하다."
    "하지만 철학은 스스로가 깨달지 않으면 백날 해봐도 모른다."
    "그리고 또……"
    "솔직히 요즘 세상에선 철학만 가지곤 어느 회사에도 취직할 수 없다."
    "입으론 \'산은 산이고, 물은 물이로다\'같은 소리하고 있다간 배에선 \'꼬르륵\' 소리 듣게 된다."
    show ev soc_dec:
        alpha 0.0
        linear 0.6 alpha 1.0
    "역사상 가장 위대한 철학자라고 추앙 받고있는  \'소크라테스(Σωκράτης, Sokrátis)\'나 \'데카르트(Descartes)\'의 삶을 생각해봐라"
    "하나는 젊은이들에게 좋지 않은 사상을 주입 시킨다면서 독극물 마셔서 사망하고"
    "나머지 하나는 비교적 좋은 대우를 받아왔지만, 내가 보기엔 꽤나 지루한 삶을 살다가 죽었다."
    "그래도 한가지 반론의 여지가 있다면, 과거엔 유흥수단이 많지 않았다.{cps=2} {/cps}그러니 철학에 관심을 보이는 것도 이해가 안 가는 건 아니다."
    "하지만 지금 시대에 철학은 하나의 학문으로써 취급하기 힘들다."
    "이건 단순히 내 생각 뿐만 아니라, 우리가 살고 있는 사회의 의견이다."
    hide ev soc_dec with Dissolve(1.0)
    "허나, 철학에 대한 나의 시각은 지극히 편중 돼 있다고 볼 수 있다."
    "애초에 철학을 공부하는 이유가 바로 세상 사람들의 시선을 신경쓰지 않도록 훈련하는게 아닌가?"
    "그런데 다른 사람들이 높게 보지 않는다고 해서 무족건 그 학문이 가치가 없다고 볼 순 없다."
    "다만 내가 철학에 대해 이러한 생각을 갖는 이유는 따로있다."
    show ev book:
        alpha 0.0 zoom 1.5 xalign 0.5 yalign 0.5
        linear 0.5 alpha 1.0
    "바로 내가 어렸을때 친할아버지 에게서 받은 \'탐정의 서\' 라는 책의 영향 때문이다."
    "이책은 특이하게도 출판사도 없고, 작가 명도 없고, 내용은 전부 펜으로 써져있는데……"
    "그게 왜그러냐면, 나의─지금은 돌아가신─할머니가 직접 쓰셨던 것이기 때문이다."
    "내가 이 책을 받았을 때가 지금으로부터 약 5년전……{cps=2} {/cps}그러니까─내가 초등학교 6학년 이었을 때였다."
    play sound "se/static.mp3"
    scene image "static" onlayer texture
    show ev tv_red
    $ renpy.pause(2.0)
    hide image "static" onlayer texture
    scene bg galaxy
    show expression (StarField().sm) as starfield
    "지금은 완전 도시전설이 됐지만, 당시에 우리나라─\'오리엔스(Oriance)\' 전체를 떠들썩하게 한 어떠한 \'전파 납치 사건\'이 있었다."
    "80년도 후반, 미국에서 발생한 일명 \'맥스 헤드룸 사건(Max Headroom Incident)\' 만큼, 혹은 그 이상으로 신기했던 사건……"
    show ev tv_red with Dissolve(1.0)
    "그때 있었던 일을 우리는 \'ReD 사건\'이라 부른다."
    "갑작스럽게 TV에 나와서 당시에 뉴스를 떠들썩 하게 한 어떠한 사건에 대해서 아주 생생하게 범인에 대해서 얘기하더니, 그 이후론 보이지 않았다."
    "ReD가 모든 방송에 나왔던 건 아니고, 오리엔스에서 가장 큰 방송국 2곳에서 만 나왔었다."
    "……5년 전 할아버지 댁에서 살고있던 난 우연히 그 방송을 보게 됐다."
    "보통 사람이라면 무척 신기한 일이라고 생각하면서 넘기거나, 기껏해야 ReD라는 인물이 누구인지에 대해서 조사를 하는 정도겠지만……"
    "난 달랐다."
    "그 방송을 목격한 순간─내 마음에 불이 짚혔다."
    "어떠한 투지를 불태웠다."
    "그리고……{cps=2} {/cps}어떠한 \'꿈\'이 생겼다."
    "베일에 쌓인 수수께끼의 인물이 기상천외한 방법으로 경찰들이 힘들어해 하던 사건을 해결한 모습을 보면서 생긴 나의 꿈……"
    scene ev dic_stephan
    "바로 \'명탐정\'이었다."
    show ev dic_stephan at Zoom((1280,720),(0,0,1280,720),(204,136,896,504),0.2)
    "그 \'범인은 바로 당신이야!\'하는 탐정"
    show ev dic_stephan at Zoom((1280,720),(204,136,896,504),(391,197,502,282),0.2)
    "어디를 가도 항상 죽음이 따라다니는 그 탐정"
    play sound "se/scream.mp3"
    show ev dic_stephan at Zoom((1280,720),(391,197,502,282),(507,268,272,153),0.2) with lshake
    scene bg galaxy with memory
    show expression (StarField().sm) as starfield with dissolve
    "지금 나는 그때를 흑역사 취급한다."
    "초등학교 6학년씩이나 됐으면서, 그런 민망한 꿈을 가졌다니……"
    "지금 생각만해도 온 몸에 소름이 돋는다."
    show ev book:
        alpha 0.0 zoom 1.5 xalign 0.5 yalign 0.5
        linear 0.5 alpha 1.0
    "내가 할아버지에게 탐저으이 서를 받게 된 계기가 그것 때문이었다."
    "나의 꿈과, 책의 제목이 일치했기에.{cps=2} {/cps}나에게 조금이라도 도움이 되고싶으셨던 할아버지의 마음에 의해서."
    "어쩌면 내가 이 책을 받게 된 건 필연이었을지도 모른다."
    "이 책만 없었더라도 나의 \'명탐정\'의 꿈은 그저 어렸을때 한번 쯤 드는 충동적인 사고로 끝낼 수 있었을지도 모른다고 생각한다."
    "왜냐면 \'탐정의 서\'라는─왠지 모르게 설득력 있는─제목의 책을 주면서, 아무것도 몰랐던 난 괜히 더 불타오르게 됐으니까"
    "하지만 이 책에 쓰여져 있던 것이 나의 기대를 배신했다."
    "어려운 단어, 이해하기 힘든 내용……"
    "그 책엔 엄청난 철학이 담겨 있었기 때문이었다."
    "왜 제목은 탐정의 서 이면서, 안에 쓰여져 있는 내용은 탐정이랑 아무런 상관이 없는 진 모르겠으나, 내 기대를 져버린 책에 대해서 조금 짜증났다."
    "그리고 나이가 들고, 내가 정신적으로 어느정도 성장을 하면서 철학에 대해서 알게 되면 알 수록 그것에 대해서 반발하고 싶었다."
    "어렸을때 있었던 사건 때문이라고는 절대로 말 할 수 없지만……"
    "난 그 이후로 왠지모르게 철학이나, \'사상\'에 대해서 반박하고 싶어졌다."
    "전체주의, 사회주의, 공산주의, 독재주의, 자본주의, 민주주의, 인간주의, 실존주의……"
    "전부 싫었다."
    "그렇게 사람의 생각을 분류하고, 옳다 그렇다 평가 하는 걸 혐오한다."
    "왜 전부 하나의 \'생각\'이자 \'의견\'이라고는 받아들이지 못하는 걸까?"
    "그냥 내가 아직 어려서 그런 생각을 하는걸까?"
    "나이가 들면 사실 내 생각이 잘못 됐다는 걸 깨달게 될까?{cps=2} {/cps}아니면 이 세상이 잘못 됐다는 걸 깨달게 될까?"
    $ extra_name = '수학 선생님'
    extra"에휴……{cps=2} {/cps}저 녀석 또 자고 있냐"
    stephan_think"응?"
    "나의 머릿속에서 많이 익숙한 목소리가 울렸다."
    stop music
    scene black with eyeshut
    centered"2014년 9월 12일 금요일"
    centered"1교시 수학"
    extra"수학 시간만 되면 맨날 저러니까 성적이 안 오르는 거지……"
    extra"윌리, 쟤 깨워라"
    willy"선생님, 스테반은 아침부터 계속 아파하던 거 같던데 그냥 놔둬도 괜찮지 않을까요?"
    extra"쟨 매일 아파하니까 걱정 마렴"
    willy"음……"
    extra"아니다. 그냥 내가 깨우마"
    play sound "se/hit.ogg"
    $ renpy.vibrate(0.2)
    "─라는 말이 끝나기가 무섭게, 마치 선생님의 학생 깨우는 방식을 증명해주듯이 내 정수리부근에 작은 충격이 느껴졌다."
    scene white with eyeopen
    play music "bgm/beat2.mp3"
    scene bg school_classroom at blur with dissolve
    stephan_think"으, 음……"
    "아까전의 충격을 시작으로부터 시작해, 몸 전체에 감각이 되살아나면서 잠에서 깼다."
    "하지만 아직도 몽롱한 기분이었다."
    "방금 전 이미지가 현실인지……{cps=2} {/cps}지금의 감각이 현실인지…… 잘 모를 정도로"
    scene bg school_classroom with dissolve
    "하지만 얼마지나지 않아서 바로 정신이 들었다."
    "그리고 방금전까지의 관경에 대해서 마음속으로 중얼거렸다."
    stephan_think"슈발꿈 인가……?"
    "……꿈이라고 해도 꽤나 특이한 꿈이었다."
    "하지만 방금전과 같이─우주를 꿈꾸는게 이번이 처음이 아니다."
    "이유는 나도 잘 모른다……{cps=2} {/cps}허나, 언제부턴가 이런식으로 우주가 눈앞에 펼쳐지면서 철학이나 진리에 대해서 생각해보는 이상한 꿈을 자주 꾸게 된다."
    "그리고 마지막엔 머리가 맑아지면서 뭔가 집중력이 좋아지는 듯 한 느낌이 든다."
    stephan_think"역시 내가 게임을 너무 많이 했나……"
    stephan_think"\'스카이렘(SkyRAM)\'만 벌써 몇 달째 하고 있었으니까 무리도 아니겠지?"
    "그 이상한 꿈의 원인이 게임 때문이라고 단정짓긴 했지만, 나도 그게 진짜 원인 이라고 확신하고 있는 건 아니었다."
    "그냥 아무것도 신경쓰고싶지 않은 기분이었다."
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,66,420,237),0.0) with dissolve
    show extra_math:
        xalign 0.5 yalign 1.0
    extra"잠 깻냐?"
    stephan"ZzZz……"
    "나는 서생님을 놀리듯이 일부러 코고는 소리를 냈다."
    show extra_math:
        linear 0.3 zoom 1.4 yalign -0.2
    extra"흠!"
    "그랬더니─다연하지만─선생님이 분필을 손에 쥐면서 던질 자세로 나를 위헙했다."
    "살짝 봤는데, 선생님의 손에 들고 있던 분필이 전혀 사용되지 않는 새거였다."
    "즉, 방금 내 정수리에 맞은 건 선생님이 사용하시던 분필 이었다는 뜻이다."
    "겁에 질린 나는 재빠른 동작으로 입가에 묻은 침을 닦고, 선생님의 말씀에 대답했다."
    hide extra_math
    scene bg school_classroom:
        size(1280,720)
        crop(0,239,594,334)
    show stephan fear:
        zoom 1.5 xalign 0.5 yalign -0.2
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}자, 잠 깻습니다!!{/size}" with lshake
    hide effect1
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,66,420,237),0.0)
    show extra_math:
        xalign 0.5 yalign 1.0
    extra"하여간……"
    extra"수학시간에 자는게 벌써 몇 번째냐?"
    scene bg school_classroom:
        size(1280,720)
        crop(0,239,594,334)
    show stephan smile2:
        zoom 1.5 xalign 0.5 yalign -0.2
    show letterbox behind stephan with dissolve
    "후훗,{cps=2} {/cps}미개한 인간의 언어 따윈 흥미가 없기 때문이다……"
    show stephan shock
    "……라고 내가 생각했던대로 말 할 순 없었다."
    "그보다 방금 내 대사는 머릿속에있던 것 보다 훨씬 오글거렸다는 사실을 뒤늦게 깨달았다."
    show letterbox h
    show stephan shock2
    "그래서 나는 다른 핑계를 대기로 했다."
    stephan"선생님,{cps=2} {/cps}학생이 수업시간에 잠을 잔 것이 학생의 탓이라고 할 수 있겠습니까?"
    stephan"학생마다 각기 다른 흥미 분야가 있으며, 교사의 목적은 아직 흥미 분야를 찾지 못한 학생들에게 교육을 알려주는 것 입니다"
    stephan"반면 저 같은 경우 이미 흥미 분야를 찾았으니 선생님께서 편하신 거 아닌가요?"
    stephan"그리고 학생이 수업시간에 잔 걸 자신의 교육 방식에 탓 하지 않고, 학생의 탓으로 돌리려는 것도 문제가 있다고 생각합니다"
    "최대한 선생님이 나쁘게 듣지 않도록, 정중하고 나긋나긋한 목소리로 말했다."
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,66,420,237),0.0)
    show extra_math:
        xalign 0.5 yalign 1.0
    extra"…………"
    scene bg school_classroom:
        size(1280,720)
        crop(0,239,594,334)
    show stephan smile2:
        zoom 1.5 xalign 0.5 yalign -0.2
    stephan_think"훗,{cps=2} {/cps}이제 하실 말씀ㅇ……"
    extra"말투가 매우 짜증나긴 했지만,{cps=2} {/cps}그래도 말은 잘 하는데 말이야……"
    show stephan shock
    extra"넌 흥미 분야를 찾았다는 놈이 왜 성적이 다 평균 밖에 안되는 거니?"
    extra"어느 하나도 높은 게 없어"
    stephan"그, 그건 과학에서 천체학 단원이 끝나버려서……"
    extra"또, 난 사실 수업시간에 딱히 방해만 안 한다면 학생이 자는 것에 대해서 크게 신경 안 쓰거든?"
    show stephan blush
    extra"근데 넌 코를 얼마나 크게 골았는지 알아?!"
    extra"너 때문에 수업에 브레이크가 걸려서 이렇게 훈계하고 있는 거잖아!"
    stephan"제가 자면서 코골았어요?!"
    extra"그것도 아주 크게"
    stephan_think"끙……"
    "내가 코고는 버릇이 있었다는 건 처음 들어보는 소식이다."
    "그런데 그런 버릇을 하필이면 이렇게 쪽팔리는 상황에서 알게 되다니……"
    "주변에선 학생들의 웃음소리가 작게 들렸다."
    stephan_think"죽고싶다……"
    stephan_think"그냥 이대로 죽고싶어……"
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,66,420,237),0.0)
    show extra_math:
        xalign 0.5 yalign 1.0
    extra"그보다, 너 \'류인 그룹\'에 취업 하고 싶다고 장래희망 조사서에 써놓지 않았냐?"
    extra"거기 들어가려면 전 과목 다 잘해야 한다는 건 알고 있을거 아니야?"
    stephan"그, 그건……"
    scene bg school_classroom:
        size(1280,720)
        crop(0,239,594,334)
    show stephan shock2:
        zoom 1.5 xalign 0.5 yalign -0.2
    stephan"나중에 대학 들어가면 수석으로 졸업 할 예정입니다!"
    scene ev ruin_logo with Dissolve(1.0) #류인 주식회사 로고
    "\'류인 그룹(Rūin .Inc)\'은 우리나라 즉, \'오리엔스(Oriance)\'에서 가장 큰 대기업이다."
    "류인 주식회사라고 부르기도 하며, CEO는 우리나라를 혼자서 이렇게 까지 발전 시켰다고도 볼 수 있는 \'루드윅 닉슨(Ludwik Nixon)\'이라고 한다."
    "류인의 사업 분야는 처음엔 가전제품으로 인지도를 얻자, 지금은 식품, 보험, 건설, 전자 등등 왠만하면 모든 일에 다 손을 대고있다."
    "그리고 조사결과 류인 주식회사 밑에있는 자회사까지 전부 합치면 안 하는게 없다고 한다."
    "즉, 실질적으로 우리나라를 정복 한 셈이다."
    "여담이지만 현 회장인 루드윅 닉슨은 젊었을때 국적을 미국에서 오리엔스로 바꾸고, 혼자서 류인을 부흥시킨 장본인이다."
    "그 때문인지 회사자체에 대해서 노골적으로 욕을 하는 사람은 없다."
    "허나, 규모가 규모인 만큼, 회사에 대해서 여러가지 안 좋은 소문이 많이 나돌고 있다."
    "예를 들면 몰래 무기를 생산해서 전쟁하는 국가에 팔아 넘긴다든가, 아니면 오리엔스 정치에 큰 영향력을 가지고 있다든가 등등"
    "물론 전부 음모론에 불과하다."
    "하지만 그 점이 내가 이 회사에 관심을 보이는 이유이기도 하다."
    "난 그런 미스테리를 좋아하니까"
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,66,420,237),0.0)
    show extra_math:
        xalign 0.5 yalign 1.0
    extra"스테반, 네가 진짜 빼어난 천재가 아니면 류인에 들어가는 걸 포기하거나, 그냥 열심히 공부나 해라"
    stephan"선생님 너무하세요"
    stephan"왜 그렇게 학생의 꿈을 짓밟으시고……"
    extra"너무한 건 내가 아니라 이 세상이라는 생각은 안 해봤나?"
    stephan"…………"
    extra"그럼, 수업을 재개하도록 하지"
    "선생님의 말씀이 나를 몰아넣었다."
    play sound "se/move.mp3"
    scene black with moveleft
    play sound "se/school2.mp3"
    centered"쉬는 시간"
    play bgs "bgs/people.mp3"
    scene bg school_classroom with eyeopen #교실 안 배경
    "길이길이 흑역사로 남을 것만 같은 1교시, 수학 시간이 끝났다."
    stephan"어휴―"
    "내가 교과서를 정리 하고 있는 동안 뒤에서 누군가 내 어깨를 툭툭 쳤다."
    show willy
    willy"푹 잤어?"
    show letterbox behind willy
    show bg school_classroom at blur with dissolve
    "\'윌리 제임스(Willy James)\'였다."
    "윌리는 별명이고, 본명은 \'윌리엄 R 제임스(William R. James)\'"
    "우리 둘이 처음 만난 건 중학교 3학년때"
    "윌리가 시골에서 이쪽 도시로 전학왔을 때였다."
    "생긴것도 꽤 잘생겼고, 목소리도 좋고, 성격도 비교적 착하고, 공부도 잘 하고, 인간관계도 좋고, 말도 잘 하고……"
    "그야말로 나의 정 반대의 인물이다."
    "그런 윌리가 어째서 나의 친구로 있는가……"
    "이렇게 둘을 나란히 비교해서 본다면 그런 의문이 들 수 있을지도 모르지만……"
    "우리둘이 처음 만나게 된 계기를 거슬러 올라가보면 이렇게까지 친한게 당연할지도 모른다."
    "……허나, 그때 일을 다시 생각해보면 오글거리는 과거도 한 둘은 나오니까 일부러 떠올리고 싶은 마음은 없다."
    "하지만 윌리가 단순히 나와 정 반대의 인물이라 해서 그를 높게 평가하는게 아니다."
    "실제로 윌리는 주변에서 천재 소리를 자주 들을 정도로 똑똑하다."
    "솔직히 말해서 나도 마음속으론 조금씩 윌리를 동경하고있다."
    "하지만 윌리 본인은 자신에 대한 평가가 다르다."
    "본인은 그저 기억력이 남들보다 조금 좋은 걸 제외하곤 결코 좋을게 없다고"
    "그 뿐만 아닌, 자신을 평가할땐 언제나 부정적으로만 평가한다."
    "그 행동도 조금씩 있었다면 하나의 겸손이라 생각할 수 있겠지만……"
    "윌리의 행동은 \'겸손\' 보단 \'자기혐오\'에 가까웠다."
    "하지만 그런 모습을 느낄 수 있는건 분명 윌리랑 2년 가까이 알고 지낸 나 뿐이겠지"
    show letterbox h
    show bg school_classroom with dissolve
    show willy:
        linear 0.4 xalign 1.0 yalign 1.0
    show stephan yawn:
        alpha 0.0
        linear 0.4 alpha 1.0 xalign 0.0 yalign 1.0
    "나는 표정을 찡그리면서 윌리의 말에 답 했다."
    stephan"영원히 자고 싶은 생각이 들었어……"
    show willy think
    willy"흠흠……"
    extend"지금 네 모습을 보아하니……"
    show willy talk
    willy"너 어제 \'그 여자\'한테 바람맞았지?"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}어어?!{/size}" with lshake
    stephan"그, 그럴리가 없잖아!"
    stephan"바람맞은게 아니라, 만나자고 한 장소에 나오지 않은 거 뿐이야!"
    hide effect1
    show willy shock at right
    willy"둘다 같은 뜻이라는 건 알고 하는 말이지?"
    "윌리가 말 한 \'그 여자\' 란……"
    "내 락커에 익명으로─방과후에 나랑 만나자는─러브레터를 놓고간 인물이다."
    "거기까진 좋았는데, 어째서인지 내가 막상 만나러 갔을때 아무도 나오지 않았었다."
    stephan_think"엄청나게 기대하고 있었는데……"
    show stephan mad
    stephan"나같이 순수한 남학생에게 그런 장난을 치는게 뭐가 좋다는 건지……"
    show willy
    willy"결과야 어찌됐건, 그때 그 편지는 넣었던 사람은 너한테 관심이 있었다는 것 만큼은 사실이잖아?"
    willy"그렇지 않고서야 굳이 네 락커 안에 러브레터를 넣었겠어?"
    show stephan fear
    stephan"그런 관심은 필요 없다고!"
    stephan"난 좀 더 핑크빛 학교생활을 기대하고 있었단 말이야!"
    show willy talk:
        linear 0.7 xalign 0.4
    "윌리는 좌절해 있는 나의 등을 손으로 토닥여 줬다."
    "분명 위로를 하겠다는 명목으로 하는 행동일텐데, 괜히 더 짜증만났다."
    show willy
    willy"그런데 스테반, 너 혹시─"
    $ extra_name = '여학생'
    extra"윌리~"
    extra"나 이 문제 잘 모르겠는데 혹시 도와줄 수 있을까~?"
    show stephan mad
    show willy talk:
        linear 0.3 xalign 0.7
    willy"…………"
    show willy
    willy"그래"
    show willy:
        linear 0.5 xalign 1.5
    "이 자식은 인기가 많다."
    "단순히 여자한테 뿐만 아니라, 모든 사람들한테"
    stephan_think"그런 녀석이 정 반대의 사람인 나를 토닥여줘도 위로가 될리가 없지"
    stephan"{size=20}커서 여자 잘못만나길……{/size}"
    "마음속으로 건 저주가 실수로 입밖으로 새어나갔다."
    show willy talk:
        linear 0.3 xalign 0.9
    willy"……?"
    willy"방금 나한테 무슨 말 했어?"
    "하지만 윌리한테는 아주 작게 들렸는가보다."
    show stephan shock2
    stephan"아무것도 아니야"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(1.0)
    scene bg school_classroom with moveright:
        size(1280,720)
        crop(0,239,594,334)
    stop music
    show stephan talk with dissolve:
        zoom 1.5 xalign 0.0 yalign -0.3
    play sound "se/footsteps_wood.mp3"
    show willy:
        zoom 1.5 xalign 2.0 yalign -0.3
        linear 1.0 xalign 1.0
    "동급생이 헷갈려하는 수학 문제를 도와준 윌리는 책상에 앉아있던 나에게 다가왔다."
    willy"있잖아 스테반"
    stephan"어?"
    willy"아까전에 너한테 하고 싶었던 말인데 말이야……"
    willy"너 방과후에 시간 있지?"
    stephan"너, 나 알잖아{cps=2}. {/cps}당연히 있지, 남아돌지"
    willy"그럼 혹시 탐정짓 안 해볼래?"
    play music "bgm/beat3.mp3"
    show stephan shock
    play sound "se/shock.ogg"
    stephan"{size=45}푸후후흡?!{/size}" with dissolve
    "입엔 아무것도 없었으면서도 내가 얼마나 놀랬는지를 어필하기 위해 무언가를 내뿜는 시늉을 했다."
    stephan"타, 탐정 짓?!"
    stephan"무슨 소리야?!"
    stephan"그보다 갑자기 왜?!"
    show willy talk
    willy"너 그런거에 흥미있지 않았어?"
    show willy think
    willy"분명 중학교때 였었던걸로 기억하는데……"
    stephan"그, 그걸 네가 어떻게 알고있는거야?!"
    show willy smile2
    willy"너의 명탐정 이야기는 꽤 유명한 걸?"
    stephan"정말?"
    willy"어떻게 중학생이나 돼서 장래희망 직업에 \'명탐정\'이라 적을 수가 있는거냐?"
    willy"조금 디테일하게 사립탐정이나, 강력계 형사 같은거라도 적었으면 모를까"
    show stephan fear
    stephan"그, 그건 알았으니까 여기서 그런 말 꺼내지 말아줘!"
    show willy think
    willy"……?"
    show willy smile2
    willy"알겠다─"
    willy"즉, 지금─너와 같은 중학교를 나오지 않은─다른 애들이 너의 부끄러운 과거에 대해서 아는게 두렵다는 거구나"
    show stephan shock:
        linear 0.3 xalign -0.3
    stephan"그, 그게 왜!"
    "나는 잡아먹히기 싫다는 위협의 포즈와 함께 얼굴로 \'샤아아아\' 소리를 냈다."
    show willy shock
    willy"내가 그거 가지고 널 협박하거나 하진 않을거니까 진정해"
    show willy smile
    willy"그리고 \'탐정짓\' 이라는 표현은 그냥 네 반응을 잠깐 보고싶어서 한 거야"
    show willy
    willy"실제론 네가 잠깐 만나줬으면 하는 사람이 있는데─"
    show willy shock
    show effect1
    play sound "se/shock.ogg"
    stephan"내 반응이 보고 싶다는 이유가 더 저질이잖아!" with lshake
    stephan"너 혹시 변태?{cps=2} {/cps}사디스트?"
    hide effect1
    willy"그, 글쎄 진정하라니까"
    willy"계속 이러면 대화를 진행할 수가 없잖아"
    stephan"…………"
    willy"계속해도 될까?"
    stephan"그래……"
    show willy think
    willy"에헴"
    show willy talk
    willy"나랑 같이 우리 누나집에 가줬으면 해"
    show stephan talk
    stephan"누, 나?"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}너한테 누나가 있었어?!{/size}" with lshake
    hide effect1
    willy"그러고보니까 너한텐 처음 말하는거구나……"
    
    
    
    
    
    
    
    
    willy"처음 들어봐……?"
    stephan"어!"
    show willy think
    willy"음……"
    show willy talk
    willy"생각해보니까 너에겐 처음 해보는 소리네"
    willy"나한테 누나가 있어. 친 누나는 아니고, 그냥 부모님 끼리 친하게 지내면서 알게된 일명 \'옆집 누나\'야"
    show stephan think
    stephan"흠……{cps=2} {/cps}그야말로 러브코미디 같은 이야기로군"
    show stephan talk
    stephan"부럽다"
    show willy shock
    willy"그, 그래……?"
    willy"그런데 거의 친누나 같은 사이니까 괜한 환상은 가지지 않도록 해"
    show willy talk
    willy"어쨌건, 우리 누나가 얼마 후에 결혼을 한데"
    show willy
    willy"그리고 여기서부터 이야기가 꽤 흥미로워지지……"
    willy"결혼 하는 상대가 사업가야"
    show stephan shock
    stephan"사업가?!"
    stephan"혹시 네 누나 완전 미인?!"
    stephan"그래서 막 부자 아저씨가 꼬이고!"
    show willy smile
    willy"누나 얼굴은 꽤 좋다고 봐"
    show willy shock
    willy"그런데 부자 아저씨가 꼬이거나 한 건 아니야"
    stephan"누나 얼굴 부분에서 이상하게 자신감 넘치는 목소리가 들린 건 기분탓인가……"
    show stephan
    stephan"그보다 축하한다 야"
    stephan"너 나중에 용돈도 많이 받겠네"
    show willy talk
    willy"꼭 그렇게 축하해 할 일은 아니야……"
    willy"누나의 결혼 상대가 조금 수상하거든"
    show stephan smile
    stephan"수상하다니?"
    stop music
    extend" 그 사람 상이라도 탔음?"
    show willy shock
    willy"…………"
    show stephan shock2
    stephan"머, 뭐라고 반응을 해주면 고마울꺼 같은데"
    play sound "se/school2.mp3"
    "그리고 나의 말에 답 하듯이─쉬는 시간이 끝나는 종소리가 울렸다."
    show willy
    willy"다음 쉬는 시간에 이어서 하자"
    show stephan shock
    stephan"내 드립은 무시?!"
    play sound "se/move.mp3"
    stop bgs
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg school_classroom at Zoom((1280,720),(0,0,1280,720),(0,239,594,334),0.0) with moveright #교실 안 배경
    play bgs "bgs/people.mp3"
    play music "bgm/beat2.mp3"
    show stephan:
        zoom 1.7 xalign -2.0 yalign -0.2
        linear 0.5 xalign 0.0
    show willy talk:
        zoom 1.7 xalign 1.0 yalign -0.2
    stephan"윌리!"
    "이번엔 내 쪽에서 윌리의 자리로 이동했다."
    stephan"그래서 그 사람이 수상하다고 했잖아!"
    stephan"어디가 어떻게 수상하다는거야?"
    willy"에헴……"
    willy"일단 그 사람이 누나에게 접근한 방법이 조금 신경 쓰여"
    willy"처음엔 자신을 중소기업을 운영하는 사장 이라고 소개를 했어"
    willy"돈이 많은걸 과시하려고 했는지, 선물도 사주고"
    willy"데이트도 자주 하고……"
    show stephan talk
    stephan"그게 수상 하다는거?"
    show stephan think
    stephan"네가 연애를 안 해봐서 그러는가본데.{cps=2} {/cps}그건 수상한게 아니라 노력하는거야"
    show stephan smile
    stephan"완전 수상감 이라니ㄲ……"
    show willy shock
    willy"드립은 거기까지만 하자……{cps=2} {/cps}널 때리고 싶어질지도 모르니까"
    show stephan shock2
    stephan"아, 알았어……"
    show stephan
    stephan"어쨌건 사업가 아저씨가 네 누나한테 접근 하기 위해서 온갓 방법을 사용하는 게 보기 좋네"
    show willy shock
    willy"아저씨는 아니고, 형에 가까운 외모야"
    willy"그리고 내가 수상하다고 생각 한 건 그거 때문이 아니야"
    show stephan talk
    stephan"그럼 뭔데?"
    show willy talk
    willy"운영하는 회사의 상태가 그럼에도 불구하고 계속 누나한테 찝접대는 게 이상해"
    stephan"무슨 회사를 운영하셔?"
    stop music
    show stephan shock
    willy"페이퍼 컴퍼니"
    "\'페이퍼 컴퍼니(Paper Company)\'"
    "절대 종이 만드는 회사가 아니다."
    "내가 알기로 그것은 아무런 수익이 없고, 건물도 없는……"
    "서류상 존재하는 일종의 유령회사 같은 거다."
    "하지만 유령회사와는 다르게 서류상으론 존재하기 때문에 페이퍼 컴퍼니라 불린다."
    "그런데……{cps=2} {/cps}그 남자가 페이퍼 컴퍼니를 운영하고 있다니……"
    stephan"설마 네 누나가 결혼 할 예정인 남자가 사기꾼 이라고 생각 하고 있는 거야?"
    show willy
    willy"역시 스테반,{cps=2} {/cps}이해가 빨라서 좋아"
    stephan"그럼 네가 나한테 하고 싶은 부탁은……"
    willy"그래"
    play sound "se/school.mp3"
    extend", 누나와 그 남자의 결혼에 관해서 날 도와줘"
    stephan_think"뭔가 예상 하기도 했는데……"
    stop bgs
    scene black with Dissolve(1.5)
    centered"방과후"
    play music "bgm/happy4.mp3"
    play bgs "bgs/street.mp3"
    scene bg outside_road with moveup# 하굣길 백그라운드
    show stephan talk at left
    show willy at right
    willy"그래서 날 도와줄 거?"
    stephan"내가 왜 그래야 되는데?"
    stephan"난 빨리 집에 가서 스카이렘 이나 마저 하고 싶다고"
    willy"쉬는 시간 때 도와준다고 말했잖아?"
    stephan"난 네 말을 들어준다고만 했지 도와준다고 한 적은 없는 걸로 기억하는데?"
    show willy shock at right
    willy"쳇"
    stephan"네가 그런 행동을 하려는 건 이해 되지만, 거기에 내가 간섭하는 건 좀……"
    show willy
    willy"네가 그렇게 나올 줄 알았다"
    willy"물론 그에 대한 대비책도 준비 해뒀지"
    stephan"어떤건데……?"
    show effect1
    play sound "se/shock.ogg"
    willy"{size=45}우리 집에 있는 PX4를 줄게!{/size}" with lshake
    show stephan shock at left
    play sound "se/shock.ogg"
    stephan"{size=45}뭐?!{/size}" with lshake
    hide effect1
    stephan_think"뭐야"
    stephan_think"400달러나 하는 PX4를 그냥 준다고?"
    stephan_think"그 귀한 게임기를!"
    stephan_think"나도 사고 싶었지만 사지 못했던 물건을?!"
    stephan_think"그렇게까지 누나를 도와주고 싶은 거냐?!"
    "PX4란……"
    "\'Play Xtation 4\'라는 Soni의 짱 좋은 게임기다."
    "좋은 게임들이 잔뜩 출시 될 예정에다가, 내 주변사람들은 전부 가지고 있고……"
    "엄마한테 사달라고 졸랐다가 된통 혼났었는데……"
    "……참고로 Play Xtation을 발음 할 땐 \'플레이 스테이션\'이 아니라 \'플레이 크스테이션\'이다."
    show stephan shock2 at left
    stephan"그,{cps=2} {/cps}그렇게까지 너의 누나를 도와주고 싶다면 어쩔 수 없네……"
    stephan"이 몸이 특별히 도와주도록 하지"
    show willy smile
    willy"역시 든든해"
    show willy smile2 at right
    stop music
    stop bgs
    willy_think"훗"
    scene black
##############################################################################################
######################################사건1: 뒤틀린 운명 시작###########################################
##############################################################################################
    play sound "se/case_start.mp3"
    show case1 with dissolve
    $ renpy.pause(5)
    scene bg outside_road with dissolve
    play bgs "bgs/street.mp3"
    play music "bgm/beat3.mp3"
    show stephan smile at left
    show willy shock at right
    willy"근데 곰곰히 생각해보니까 네 마음을 움직인 건 친구에 대한 우정이 아닌 PX4네……"
    willy"그리고 내가 줄 PX4는 중고니까 너무 기대하진 말고;;"
    stephan"그래도 돈 주고 사는 것보단 낫지"
    willy"그래, 알아서 해……"
    stephan"그럼 난 뭘 하면 되는 거지?"
    show willy talk at right
    willy"……너 최근에 경제학에 대해서 공부하고 있었지?"
    show stephan at left
    stephan"뭐……{cps=2} {/cps}일단은 취업을 목표로 공부중이니까"
    willy"그럼 무역에 대해서라든가, 사업 같은 것도 잘 알겠네?"
    stephan"이론 이라면 알고 있다만……"
    stephan"혹시 너도 공부하고 싶은 거야?"
    show willy talk at right
    willy"딱히 그런 건 아니고,{cps=2} {/cps}네가 그런 지식이 있다면 됐어"
    show stephan talk at left
    stephan"싱거운 녀석이군"
    show willy smile at right
    willy"그건 제쳐두고 일단 같이 누나 집에 가자"
    show stephan shock at left
    show effect1
    play sound "se/shock.ogg"
    show willy shock at right
    stephan"{size=45}잠깐!{/size}" with lshake
    stephan"거기 가서 난 뭐라고 말해야 하는 건데?!"
    stephan"계획을 말하라고!{cps=2} {/cps}계획을!"
    willy"그걸 전부 말해버리는 건 좀 곤란한데……"
    stephan"그럼 내가 네 누나를 만났을 때 해야 할 말이라도……!"
    stephan"나 뻘쭘한 거 진짜 싫어한다고!"
    hide effect1
    show willy think at right
    willy"흠……"
    show willy talk at right
    willy"아!"
    show willy smile at right
    willy"너 \'류인 주식회사\'에 들어가고 싶어 했지?"
    stephan"그렇긴 한데……"
    willy"우리 누나가 거기서 일하거든!"
    show stephan at left
    stephan"정말?!"
    stephan_think"설마 이런 곳에서 내 장래에 도움이 되는 사람을 만나게 될 줄이야"
    show stephan shock at left
    stephan_think"근데 누나의 남친이 사업하는 사람이라고 하지 않았나?"
    stephan_think"둘이 결혼하면 완전 로얄 패밀리 되겠네……"
    "……물론 다른 쪽이 사기꾼일 가능성이 있긴 하지만 말이지"
    willy"대화를 시작 할 땐 대충 그런쪽의 내용이 좋겠어"
    willy"아,{cps=2} {/cps}내가 말 하는 걸 깜빡했는데,  누나의 이름은 \'멜 다운스(Mel Downs)\' 라고 해"
    stephan_think"멜 이라……"
    "별로 흔한 이름은 아니었다."
    willy"그럼 지금부터 네가 거기에 가서 해야 할 행동 인데……"
    scene black with Dissolve(1.0)
    stop music
    stop bgs
    "윌리는 나한테 누나를 만나고 나서, 어떤 말을 해야 하는지 설명 해줬다."
    "일단 걔가 원하는 건 누나의 피앙셰의 명함"
    "그때 난 명함을 얻는데 왜 내가 필요한지 물어봤는데……"
    play sound "se/think.mp3"
    play bgs"bgs/street.mp3"
    scene bg outside_road with flash
    show willy talk at right
    show stephan talk at left
    willy"당연히 내가 먼저 시도 해봤지"
    willy"근데 접근 방법이 잘못 됐었던 건지, 내 말을 믿으려고 하지도 않았어"
    willy"이 이상 내가 말 하는 건 무의미 한 거 같으니까, 누나도 처음 보는 네가 해보는 게 어떨까 생각해봤어"
    willy"처음 만나는 사람에다. 내 친구라고 한다면 왠만한 부탁은 들어 줄 수 있을지도 모르잖아?"
    stop bgs
    scene black with flash
    "명함을 얻고 나선, 거기에 적혀있을 사무실 주소로 이동 하면 된다고 한다."
    "그러고 나서의 작전은 이후에 추가로 설명 해준다고 하고……"
    stephan_think"그나저나 사기꾼 남자 친구라……{cps=2} {/cps}내가 괜한 일에 말려드는 건 아니겠지?"
    play music "bgm/smooth1.mp3"
    centered"멜 다운스의 집"
    scene ev mel_calling #멜이 머리카락을 휘날리며 아름답게 미소 지으면서 전화를 받고있는 일러
    show mel_calling smile2
    show black
    hide black with dissolve
    mel"여보세요?{cps=2} {/cps}아버지?"
    $ extra_name = '멜 아버지'
    extra"멜?{cps=2} {/cps}멜 이니?"
    mel"네~{cps=2} {/cps}아버지 요즘 건강 하게 지내세요?"
    extra"건강이라……{cps=2} {/cps}통증 이라면 많이 사라졌지"
    extra"근데 여전히 머리는 지끈거리는 구나……"
    mel"분명 괜찮을거예요!"
    extra"흠흠……"
    extra"내 얘기는 됐고……{cps=2} {/cps}넌 요즘 어떻게 지내고 있니?"
    show mel_calling talk
    mel"저야 평상시랑 똑같죠"
    extra"그럼 저번에 네가 말해준 그 남자랑은 어떠니……?"
    extra"잘 돼 가고 있지?"
    show mel_calling smile
    mel"아!{cps=2} {/cps}그거랑 관련해서 제가 말씀 드릴게 있어요!"
    mel"들으시면 깜짝 놀랄 수도 있으니까 각오 하세요!"
    extra"무슨 소식이길래……"
    mel"저, 결혼 날짜가 잡혔어요!"
    show effect1
    play sound "se/shock.ogg"
    extra"{size=45}정말?!{/size}" with lshake
    hide effect1
    show mel_calling smile2
    mel"네!{cps=2} {/cps}제가 우편으로 청첩장을 보냈으니까 도착하면 자세히 읽어보세요"
    extra"우리 멜이 드디어……"
    show mel_calling talk
    mel"그렇게 기뻐 해주시니까 정말 다행이에요……"
    extra"{size=20}흑……{/size}"
    extra"에헴"
    extra"이야─{cps=2} {/cps}엊 그제 까지만 해도 용돈 달라고 졸라대던 아이가 벌써 결혼을 하게 된다니~"
    extra"세월이 참 빠르구나"
    show mel_calling smile
    mel"아버지도 참~{cps=2} {/cps}갑자기 고등학교 시절을 꺼내면 어떡해요"
    extra"하지만 정말 순식간 처럼 느껴지는 걸 어떡하겠니"
    extra"난 몸이 점점 말을 듣지 않기 시작했는데……{cps=2} {/cps}넌 너의 인생을 잘 살고 있는거 같고"
    show mel_calling talk
    mel"아……{cps=2} {/cps}혹시 아직도 그 증상은 낫지 않았어요……?"
    extra"증상 이라니?"
    mel"…………"
    mel"아니에요……{cps=2} {/cps}그냥 잊어주세요"
    mel"전 아버지만 행복하면 되니까요……"
    extra"우리 멜이 어느세 이런 훌륭한 어른이 됐을까~"
    extra"이 아버지는 정말 자랑스럽단다!"
    extra"이렇게 백옥 같은 우리 딸을 가져가는 남자는 얼마나 복이 많은걸까"
    mel"후후후……"
    mel"우리 아버지가 저를 그렇게 칭찬 해주시고~"
    show mel_calling smile2
    mel"평상시엔 윌리만 편애 했으면서~"
    extra"그, 그건 좀 다르지"
    extra"윌리는 든든하잖니?"
    mel"그건 저도 부정 할 수 없겠네요"
    extra"그러고보니까 걔는 요즘 어쩌고 있니?{cps=2} {/cps}잘 지내고 있어?"
    show mel_calling smile
    mel"네~ 윌리야 평상시랑 같죠~"
    extra"그래……{cps=2} {/cps}너, 윌리 말은 잘 듣고 있지?"
    mel"에이 아버지도~{cps=2} {/cps}제가 윌리보다 누나 라고요?"
    extra"그래도 잘 들으렴.{cps=2} {/cps}걘 널 많이 아끼니까"
    extra"그리고 어쩌면 너보다 더 어른스러울 걸?"
    show mel_calling talk
    mel"에이~{cps=2} {/cps}윌리도 어쩔 수 없는 애예요~"
    mel"오늘 저한테 친한 친구를 한명 소개 시켜준다고 하던걸요?"
    play sound "se/door_bell.mp3"
    $ renpy.pause(0.5)
    show mel_calling smile2
    mel"아, 마침 왔네!"
    extra"윌리한테 친구가……?"
    mel"저도 엄청 놀랐다니까요?"
    show mel_calling talk
    mel"그래도……{cps=2} {/cps}뭔가 평범하게 지내고 있는 게 정말 보기 좋아요……"
    play sound "se/door_bell.mp3"
    show mel_calling smile2
    mel"어머!{cps=2} {/cps}저 이만 가봐야 될거 같네요"
    mel"그럼 끊어요"
    extra"그래"
    extra"그리고 말 할 기회가 없을거 같으니까 미리 말 할게……"
    show mel_calling talk
    extra"결혼 축하해"
    mel"…………"
    mel"그런 말은 제 결혼식장에 와서 해주세요……"
    mel"꼭……"
    extra"…………"
    scene bg mel_house at Zoom((1280,720),(0,0,1280,720),(380,400,560,315),0.0) with moveleft# 멜의 집앞 배경
    show stephan at left
    show willy talk at right
    willy"우리 누나가 성격이 좀 시원시원 하니까 너무 당황하진 마"
    stephan"시원시원 하다면……{cps=2} {/cps}많이 개방적 이라는 뜻인가?"
    willy"그렇다고 할 수 있겠지"
    show stephan think at left
    stephan"근데, 생각해보니까 시원하다, 차갑다, 쿨하다 는 전부다 낮은 온도를 뜻하는 말 인데……"
    stephan"어째서 사람의 성격으로는 전부 다른 의미를 지니고 있을까?"
    willy"생각해보니까 그런 거 같기도……"
    show stephan talk at left
    stephan"그치?"
    stephan"시원한 성격은 많이 개방적이고 활발하다는 뜻이고"
    stephan"차가운 성격은 냉정하고 이성적이고"
    stephan"쿨한 성격은 시원한 성격이랑 비슷하지만 조금 묵묵함이 섞여있고……"
    show stephan shock at left
    stephan"생각해보니까 왜 높은 온도의 성격은 따뜻하다 하나 밖에 없는 거지?!"
    stephan"더운 성격이나 뜨거운 성격은 없잖아?!"
    willy"뜨거운 성격은 있지 않나?"
    stephan"보통 열혈이라고 하지, 뜨겁다고 하진 않지"
    stephan"……물론 뜨거운 성격이 동사로는 쓰이기도 하겠지만"
    stephan"그래도 차가운 성격과는 다르게 명사로 쓰이진 않잖아?!"
    show willy shock at right
    willy"너 갑자기 왜이래?"
    show stephan shock2 at left
    stephan"미,{cps=2} {/cps}미안……"
    extend" 대기업에 다니면서 사업하는 남친을 가진 능력자를 만나려니까 떨려서……"
    willy"너, 누나를 너무 과대평가 하고 있어……"
    stephan"그래……?"
    willy"그래"
    show willy at right
    willy"실물은 전혀 그런 거 없으니까 걱정 마"
    stephan"으,{cps=2} {/cps}응―"
    willy"아참, 누나는 지금 결혼식 준비로 한창 들떠 있으니까 이왕이면 배우자에 대해서 나쁘게 말하는 건 피해줬으면 해"
    show stephan smile at left
    stephan"ㅇㅋ"
    show willy talk
    willy"근데 누나가 왜이렇게 늦게 나오지?"
    show willy talk:
        linear 0.4 xalign 0.5
    $ renpy.pause(0.4)
    show willy talk:
        linear 0.3 xalign 0.8
    play sound "se/door_bell.mp3"
    $ renpy.pause(1.7)
    mel"네~{cps=2} {/cps}나가요~"
    hide stephan smile
    hide willy talk
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(2)
    play sound "se/door_open.ogg"
    $ renpy.pause(1)
    show mel with dissolve
    mel"역시 윌리였구나~!"
    show mel:
        linear 0.5 xalign 0.0 yalign 1.0
    show willy at right
    willy"안녕"
    mel"혹시 옆에 있는 애는 요번에 말 한 친구?"
    willy"응"
    hide willy 
    show stephan shock2 at right
    stephan"아,{cps=2} {/cps}안녕하세요!"
    stephan"\'스테반 토머(Stephan Tomer)\' 라고 합니다"
    mel"안녕~{cps=2} {/cps}누난 멜 다운스 라고 해~"
    mel"어제 윌리가 친구를 데리고 온다더니 이렇게 귀여운 친구를 데리고 올 줄이야~"
    stephan"귀,{cps=2} {/cps}귀엽다니요;;"
    stephan_think"그보다 윌리가 사전에 연락을 줬었다고?!"
    mel"여자를 데려 왔으면 더 재미있었을 텐데……"
    hide stephan shock2
    show willy shock at right
    willy"에헴"
    mel"후후후"
    hide willy shock
    show stephan shock2 at right
    mel"우리 윌리가 겉보기와는 다르게 많이 섬세한 아이니까 네가 잘 돌봐주면 좋겠네~"
    stephan"네……"
    stephan_think"이러니까 윌리의 누나가 아니라, 윌리의 엄마 같네"
    show stephan think at right
    stephan_think"근데 내가 윌리를 돌봐준다라……"
    show stephan smile2 at right
    stephan_think"뭔가 윌리를 넘는 거 같아서 좋아"
    stephan_think"흐흐흐"
    hide stephan smile2
    show willy at right
    willy"잠깐 안에 들어가도 될까?"
    show mel talk at left
    mel"어머!{cps=2} {/cps}내 정신좀 봐라!"
    show mel at left
    mel"마침 내가 커피를 선물 받았는데, 일단 같이 마시면서 천천히 얘기를 나눠 볼까?"
    play sound "se/door_open.ogg"
    scene black with moveright
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(2)
    play music "bgm/smooth3.mp3"
    scene bg room_mel with moveright# 멜의 집 안
    "멜 누나가 커피를 준비하는 동안 나랑 윌리는 소파에 같이 앉았다."
    scene bg room_mel at Zoom((1280,720),(0,0,1280,720),(259,103,744,419),0.5)
    $ renpy.pause(0.5)
    show stephan talk:
        xalign 0.25 yalign 1.0
    show willy:
        xalign 0.75 yalign 1.0
    stephan"너 멜 누나한테 내가 올 거라고 미리 전화 했어?"
    willy"그랬다만?"
    show stephan shock
    stephan"그럼 나한테 말하기도 전에 미리 말 했다는 거잖아?!"
    stephan"내가 가지 않겠다고 하면 어쩔 생각이었어?!"
    willy"그래서 내가 그 비싼 PX4를 걸었잖아"
    show stephan talk
    stephan"아……"
    stephan_think"확실히 나한테 PX4를 주겠다고 하면 거절 할리가 없겠지"
    "하지만 그렇다는 건 윌리는 훨씬 전부터 나를 이용할 생각이었다는 거다."
    "도대체 무슨 계획 일까?"
    "과연 어떻게 해서 사기꾼—으로 추정되는— 남친이 멜 누나랑 결혼 하는 걸 막는 걸까?"
    scene bg room_mel at Zoom((1280,720),(259,103,744,419),(0,0,1280,720),0.5)
    play sound "se/footsteps_wood.mp3"
    show mel:
        xalign 1.9 yalign 1.0
        linear 2.0 xalign 0.9
    "나랑 윌리가 대화 하고 있던 동안, 멜 누나는 커피를 가지고 왔다."
    mel"자~"
    mel"글쎄 이 커피가 해외에서 직구 한거라고 하더라!"
    mel"난 맛있던데, 너희들 입맛에도 맞았으면 좋겠네~"
    stephan_think"윌리가 말한, 멜 누나의 남자친구가 줬다는 선물중 하난가?"
    show stephan:
        xalign 0.4 yalign 1.0
    stephan"잘 먹겠습니다"
    play sound "se/search_bag.mp3"
    scene bg room_mel at Zoom((1280,720),(0,0,1280,720),(259,103,744,419),0.5) with dissolve
    $ renpy.pause(1)
    "나는 앉아서 커피를 한 모금 마셨다."
    "맛이야 그냥 평범한 커피맛 —흙 맛—이지만……"
    extend" 대신 향이 정말 좋다."
    scene bg room_mel at Zoom((1280,720),(259,103,744,419),(536,103,744,419),0.5)
    $ renpy.pause(0.5)
    show mel at right
    show stephan talk:
        xalign 0.25 yalign 1.0
    mel"후후"
    mel"윌리가 친구를 데리고 온다고 하길래 설마 했는데"
    mel"이런 친구가 있었을 줄이야~"
    mel"어렸을 때 있었던 일 때문에 친구 만드는 걸 힘들어 할 줄 알았거든……"
    mel"하지만 지금 보니까 내가 괜한 걱정을 한 거 같네!"
    stephan"어렸을 때요?"
    scene bg room_mel at Zoom((1280,720),(536,103,744,419),(259,103,744,419),0.5)
    $ renpy.pause(0.5)
    show willy shock:
        xalign 0.75 yalign 1.0
    show stephan talk:
        xalign 0.25 yalign 1.0
    willy"넌 몰라도 돼"
    willy"그리고 누나도 너무 말하진 말아줘……"
    willy"나한테도 프라이버시 라는 게 있으니까"
    scene bg room_mel at Zoom((1280,720),(259,103,744,419),(536,103,744,419),0.5)
    $ renpy.pause(0.5)
    show mel at right
    mel"그래~{cps=2} {/cps}그래~"
    show stephan shock:
        xalign 0.25 yalign 1.0
    show mel:
        linear 1.0 xalign 0.8
    mel"……스테반 이라고 했지?"
    extend" 윌리랑은 어떻게 해서 친해졌니?!"
    show stephan talk
    stephan"저랑 윌리요?"
    stephan_think"나랑 윌리가 친해지게 된 게……"
    play sound "se/heartbeat.mp3"
    show ev willy_mid at blur with flash
    $ renpy.pause(0.5)
    hide ev willy_mide with flash
    show stephan blush
    stephan_think"으익!"
    stephan_think"생각해보니까 그,{cps=2} {/cps}그땐……!"
    "멜 누나가 매우 낯 간지러운 주제를 꺼내버렸다."
    "그땐 내가 좀 철이 없어서……{cps=2} {/cps}이리저리 하다가……"
    stephan_think"으으……"
    scene bg room_mel at Zoom((1280,720),(536,103,744,419),(259,103,744,419),0.5)
    $ renpy.pause(0.5)
    show willy shock
    "난 윌리를 구원의 표정으로 바라봤다."
    stephan_think"내가 부끄러운 과거를 떠올리지 못하도록 구해줘!"
    willy"어휴―"
    willy"누나"
    scene bg room_mel at Zoom((1280,720),(259,103,744,419),(536,103,744,419),0.5)
    $ renpy.pause(0.5)
    show willy talk:
        xalign 0.25 yalign 1.0
    show mel:
        xalign 0.8 yalign 1.0
    mel"왜~?"
    willy"요즘 일은 어때?"
    show mel talk
    mel"일?"
    mel"뭐어……{cps=2} {/cps}딱히 문제는 없는데?"
    willy"정말?{cps=2} {/cps}뉴스 보니까 구조조정이 있다는 거 같던데"
    willy"뭔가 일이 있는 거 아니야?"
    show mel
    mel"참 넌 여전하네~"
    mel"그런 거나 보고"
    mel"그래도 네가 걱정 할 일은 아니니까 괜찮아~"
    show mel talk
    mel"굳이 있다면……"
    extend" 그 외에 여파 때문에 내 급여가 좀 많이 줄었지……"
    mel"좀 더 정확히 말하자면, 내 월급 빼고 물가가 올랐다고 해야 할까나?"
    show mel
    mel"그,{cps=2} {/cps}그래도 걱정 할 정도는 아니야!"
    willy"그럴 줄 알았다"
    show mel talk
    mel"정말?"
    extend" 어떻게?!"
    show willy smile
    willy"내가 오늘 친구를 데리고 온 이유도 그거야!"
    willy"얘가 류인 그룹에 취직하는 게 꿈이거든!"
    willy"그래서 알고 있는 게 많아"
    "참고로 난 윌리 한테 류인 그룹에 대해서 말 한 적이 없다."
    "……물론 거기에 취직하고 싶다고 말은 한적이 있다."
    "다만 그 이상은 없었어……"
    "아니, 류인 그룹에서 구조조정을 한다는 소식도 처음 알았다."
    stephan_think"즉, 윌리가 미리 조사를 했다는 뜻이로군"
    mel"류인에 취직을 하고 싶다고?"
    mel"공부를 잘하는가보네?"
    show willy smile2
    willy"나보단 아니지만 말이지~"
    stephan_think"윽!"
    "사실이지만……"
    show mel
    mel"윌리도 참~"
    show willy smile
    willy"스테반이 아마 누나한테 하고 싶은 질문이 많을 거야"
    hide willy smile
    show stephan shock at left
    show mel:
        linear 1.0 xalign 1.0
    show stephan at left
    "멜 누나는 나를 바라봤다."
    "아무래도 여기서부턴 내가 대화를 할 차례인 듯 하다."
    stephan_think"어떻게 해서든 남친의 명함을 얻는 쪽으로 대화를 주도하는 거다……!"
    show stephan shock2 at left
    stephan"ㄴ,{cps=2} {/cps}네헤!"
    stephan_think"{size=45}쉩!{/size}{cps=2} {/cps}긴장했더니 혀를 깨물어 버렸어!"
    stephan"지문 하고 싶은 게 있는데 괜찮효?"
    stephan"……가 아니라!{cps=2} {/cps}질문 하고 싶은 게 있는데 괜찮죠?"
    mel"응!"
    extend" 뭐든지 물어보렴~"
    stephan"그……{cps=2} {/cps}언제 류인 그룹에 취직을 하셨어요?"
    mel"2년 됐지"
    stephan"2년……?"
    stephan"실례지만 나이가 어떻게 되시는지?"
    mel"숙녀의 나이를 묻다니……{cps=2} {/cps}배짱이 좋구나?!"
    show stephan smile at left
    stephan"헤헤……{cps=2} {/cps}뭘요~"
    willy"그거 칭찬 아니야"
    mel"후후"
    mel"누난 올해로 24살 이란다~"
    show stephan shock at left
    stephan"진짜요?!"
    "현재 24살이고, 2년전에 취직을 했다는 건 22살에 취업 시험에 합격 했다는 뜻이다."
    "쉽게 말해서 대학 졸업 후 한 번에 대기업 취직을 했다."
    stephan_think"엄청 똑똑하신가 보네……"
    "그보다 누나가 곧 있으면 결혼을 한다고 했다."
    "24에 결혼이면 좀 많이 빠른편인데……{cps=2} {/cps}혹시 무슨 사정이 있는 걸까?"
    show mel talk
    mel"왜 그렇게 당황 하는 거야?"
    mel"혹시 내가 늙어 보이거나?!"
    stephan"그런 거 아니에요!"
    show stephan shock2 at left
    stephan"오히려 반대인걸요!"
    show stephan think at left
    stephan"정말 고등학생 이라고 해도 믿을걸요!"
    show stephan shock at left
    stephan_think"너무 속 보였나?"
    show mel smile
    mel"호오~호호호!"
    mel"고등학생 이라니~"
    extend" 그렇게 말 해줘도 나오는 거 없다구~"
    show stephan smile2 at left
    stephan_think"칭찬에 약한 성격이시군"
    show stephan at left
    mel"또 물어볼 거 있니?"
    stephan"회사 시설은 어때요?"
    stephan"컴퓨터도 스펙 빵빵하고 그런가요?!"
    show mel
    mel"음……{cps=2} {/cps}난 기술적인 덴 관여를 안 해서 그런 건 잘 모르겠고……"
    mel"안이 엄청 깨끗해!"
    mel"에어컨도 빵빵하고!"
    mel"……물론 여름에 만"
    show stephan shock2 at left
    stephan"그,{cps=2} {/cps}그렇군요……"
    stephan"혹시 회사 일은 안 힘드세요?"
    show mel talk
    stop music
    mel"…………"
    mel"역시 대기업이다 보니까……"
    mel"사내 분위기가 정말 장난 아니게 살벌하다고 해야 할까?"
    mel"회사에 있는 게 정말 숨이 막혔어……"
    play music "bgm/smooth1.mp3"
    show mel
    mel"그래도 전부 다 그런 건 아니야"
    mel"직장 선배 중에서 꽤 친절하신 분이 있었거든~"
    mel"정말 착하고, 상사한테 혼나도 표정 하나 변치 않고……"
    mel"나한테도 정말 친절하게 대해 주셨지"
    mel"……지금은 관둬 버려서, 나 혼자 남았지만"
    mel"그래도 말이야~{cps=2} {/cps}몇 달 전에 다시 만났지 뭐야~"
    show stephan think at left
    stephan_think"지금 만나고 있는 사람이라는 건가?"
    show stephan at left
    stephan_think"슬슬 내가 원하는 정보에 다가가는 듯 한 느낌이 들어"
    show stephan smile at left
    stephan"정말요?!"
    stephan"혹시 곧 있으면 같이 결혼 하시는?"
    show mel talk
    mel"어?"
    extend" 그걸 어떻게?"
    show stephan shock2 at left
    stephan"위,{cps=2} {/cps}윌리한테 들었어요!"
    stephan"곧 있으면 자기 누나가 결혼을 하는데, 마침 류인 주식회사에서 일을 한다면서……"
    show mel
    mel"그랬구나아~"
    show stephan at left
    stephan"혹시 사내 연애부터 시작했나요?!"
    show mel talk
    mel"류인에 대해서 궁금한 건 어쩌고……?"
    show stephan shock at left
    stephan"으,{cps=2} {/cps}음……"
    show stephan shock2 at left
    stephan"누나가 회사 얘기를 하는 것보단 남자 친구 얘기를 하는 걸 더 좋아하시는 거 같아서……{cps=2} {/cps}랄까요……"
    stephan"또, 솔직히 전 남의 연애담 듣는 거 좋아 하거든요!"
    stephan"그리고 회사에 관한 건 나중에 인터넷을 통해서 조사 해 볼 수도 있는 걸요!"
    show mel
    mel"어머어머~"
    mel"얘가 참~"
    mel"그래……{cps=2} {/cps}솔직히 네 말대로 회사 생각은 별로 안하고 싶긴 해"
    show mel talk
    mel"거긴 너무 따분 하고"
    mel"선배님이랑 같이 있었을 땐 좀 더 좋았는데……"
    mel"훗……{cps=2} {/cps}이젠 선배님이 아니라 렌스 지만……"
    stephan"렌스?"
    show mel
    mel"응,{cps=2} {/cps}\'렌스 클라크(Lance Clark)\'가 그이의 이름이야~"
    show stephan shock2 at left
    stephan"그렇군요"
    show stephan smile at left
    stephan"그래서 사내 연애부터 시작 했어요?!"
    mel"아니~"
    mel"내가 렌스랑 본격적으로 사귀기 시작한 건 몇 개월 안됐어"
    mel"그래도 그이랑 예전부터 알고 지냈던 사이라서 그런지 어색함은 전혀 없었지~"
    show stephan at left
    stephan"그럼 프러포즈는 누가 먼저 했어요?!"
    mel"프러포즈는 원래 남자 쪽에서 먼저 하는 게 정석이야~"
    stephan"……즉, 남자친구 분이 먼저 했다는 뜻 인가요?"
    mel"당근이지!"
    show stephan think at left
    stephan_think"먼저 고백을 했다라……"
    stephan_think"정말 남자가 사기꾼 이라면 당연하겠지"
    stephan_think"그러나 이걸 어떻게 해서 알리는 것이 좋을까?"
    stephan_think"아니,{cps=2} {/cps}애초에 멜 누나한테 말 하는 것이 좋긴 할까?"
    hide stephan think
    hide mel
    narrator_nvl"대답 모드에 진입 하셨습니다."
    narrator_nvl"대답 모드는\'진실\'혹은\'거짓\'으로 나눠지며"
    narrator_nvl"상황에 따라서 다른 결과를 불러일으킵니다."
    nvl clear
    menu:
        "남자친구가 무슨 일을 하고 있죠? (진실)":
            show mel at right
            show stephan at left
            stephan"남자 친구가 나중에 회사를 관뒀다고 하셨는데……"
            stephan"그렇다는 건 지금은 다른 일을 하고 있다는 뜻이겠네요?"
            mel"그치"
            extend", 애초에 그이가 회사를 관둔 이유가 그런 이유 였으니까……"
            stephan"아,{cps=2} {/cps}그래서 지금은 사업을 하고 있다는 거 군요"
            show mel talk at right
            mel"어?{cps=2} {/cps}내가 그걸 말 해줬던가?"
            show stephan shock2 at left
            stephan"다,{cps=2} {/cps}당연히 윌리한테 먼저 들었죠!"
            mel"윌리가 거기 까지 말해 줬어?"
            show stephan shock at left
            stephan"네에……"
            show stephan shock2 at left
            stephan"그래도 무슨 사업을 하고 있는 진 구체적으로 듣지 못했어요!"
            show stephan talk at left
            stephan"혹시 아세요?"
            mel"……무역 회사를 하고 있었던 걸로 기억하는데?"
            hide stephan talk
            hide mel talk
            menu:
                "페이퍼 컴퍼니가 아니고요? (진실)":
                    show stephan talk at left
                    show mel talk at right
                    stop music
                    stephan"페이퍼 컴퍼니가 아니고요?"
                    mel"뭐?"
                    stephan"서류엔 어떻게 등록 되었는진 모르겠지만……"
                    extend" 일단 그 회사가 페이퍼 컴퍼니라고 들었습니다"
                    stephan"거기다 연애한지 1년도 되지 않아서 결혼을 하겠다니……"
                    stephan"뭔가 이상하다고 생각 하지 않나요?"
                    stephan"전부 결혼사기의 수법이랑 너무 일치 하는 게……"
                    show mel sirius at right
                    mel"…………"
                    play music "bgm/sad2.mp3"
                    mel"렌스가 빨리 결혼을 하자고 한 건……"
                    mel"아마 나를 위해서 였을거야……"
                    show stephan shock at left
                    stephan"네?"
                    show mel talk at right
                    show effect1
                    play sound "se/shock.ogg"
                    mel"{size=45}그러니까 절대 렌스가 사기꾼이라서 그런 게 아니야!{/size}" with lshake
                    hide effect1
                    stephan"그건 또 무슨 뜻이에요?"
                    stephan"분명 프러포즈를 먼저 한 게 남자친구 쪽 이라고……"
                    mel"사실……{cps=2} {/cps}얼마 전에 아버지가 사고를 당하신 적이 있었어……"
                    mel"병원에선 이제 일 년도 남지 않았다고……"
                    stephan_think"이런"
                    stephan_think"내가 괜한 말을 한 걸까?"
                    mel"아버지의 마지막 소원이, 신랑의 얼굴을 보는 거라면서……"
                    mel"아마 렌스는 그 사실을 알고 있어서 일부러 일찍 결혼 하자고 한 걸꺼야……"
                    stephan"그,{cps=2} {/cps}그럼 남자 친구가 페이퍼 컴퍼니를 운영 하는 건……"
                    mel"그건……{cps=2} {/cps}솔직히 나도 모르겠어"
                    mel"하지만 분명 뭔가 사정이 있어서 그럴거야!"
                    "누나의 말투로 봐선, 윌리가 미리 페이퍼 컴퍼니에 대해서 말 한 적이 있었던 것 같았다."
                    "그럼에도 불구하고 남자친구를 의심하지 않다니……"
                    show stephan talk at left
                    stephan"그럼 이 질문에 솔직히 대답 해주셨으면 합니다……"
                    stephan"혹시 남자친구 한테 돈을 빌려 준 적이 있나요?"
                    mel"…………"
                    stephan"대답 해주세요……"
                    mel"어……"
                    mel"하지만 렌스는 사업을 하고 있으니까 그런 건!"
                    "이걸로 모든 사건은 정리 됐다."
                    "렌스 클라크는 결혼사기를 꾸미고 있다."
                    "게다가 누나의 아버지가 편찮으시다는 걸 알고 있다면 더욱 더 가능성이 높다."
                    show mel sirius at right
                    mel"혹시……{cps=2} {/cps}이것도 전부 윌리가 말 해준 거야?"
                    stop music
                    stephan"…………"
                    stephan"네……"
                    mel"역시 그랬구나"
                    mel"{size=20}내가 이 녀석을 진짜……{/size}"
                    scene bg room_mel at Zoom((1280,720),(536,103,744,419),(259,103,744,419),0.5)
                    $ renpy.pause(0.5)
                    "멜 누나는 윌리를 향해서 고개를 돌렸다."
                    "그런데 어째서인지 윌리가 자리에 없었다."
                    scene bg room_mel at Zoom((1280,720),(259,103,744,419),(536,103,744,419),0.5)
                    $ renpy.pause(0.5)
                    show mel talk at right
                    mel"윌리?"
                    show willy talk:
                        xalign -2.0 yalign 1.0
                        linear 1.0 xalign 0.2
                    play sound "se/footsteps_running.mp3"
                    $ renpy.pause(1.0)
                    "윌리의 이름을 부르자, 금방 달려왔다."
                    willy"불렀어?"
                    mel"그래"
                    play music "bgm/sirius1.mp3"
                    mel"너, 내가 결혼 하겠다고 한 뒤로부터 이상해"
                    show willy shock
                    willy"이상한 건 누나잖아!"
                    willy"렌스 씨가 페이퍼 컴퍼니를 운영하고 있다고 말 해줬는데도!"
                    mel"뭔가 사정이 있을 거야……"
                    mel"렌스는 사업을 하고 있잖아!"
                    mel"분명 그거랑 관련이……"
                    willy"그건 또 그거 나름대로 문제잖아"
                    willy"\'분식회계\'는 불법 이라고"
                    "참고로, \'분식회계(粉飾會計)\'란……"
                    "음……{cps=2} {/cps}쉽게 말하자면, 회사의 재무 변화를 인위적으로 조작하는 행동이다."
                    "방법은 여러 가지로 복잡한 게 있지만, 내가 알기론 페이퍼 컴퍼니를 만드는 것도 그 방법 중 하나이다."
                    "그리고 당연하지만 불법이다."
                    willy"렌스 씨가 무슨 목적으로 페이퍼 컴퍼니를 운영 하고 있는 진 모르겠지만, 그런 회사를 가지고 있는 순간부터 좋은 사람은 아니라고"
                    show mel sirius at right
                    mel"…………"
                    mel"그건 내가 알아서 할 일이야……"
                    mel"그러니까 넌 제발 신경 쓰지 말아줘"
                    willy"도대체 왜?!"
                    willy"그렇게까지 렌스라는 사람이 좋은 거야?"
                    mel"그래……"
                    mel"렌스는 정말 착한 사람이니까"
                    willy"거짓말 하지 마"
                    willy"아저씨 때문이잖아"
                    mel"…………"
                    willy"누나는 지금 아저씨 곁에 있어주지 못한 것에 대한 죄책감 때문에 자신에게 결혼을 강요하고 있어!"
                    mel"어쩌면……{cps=2} {/cps}네 말대로 내가 자신에게 너무 결혼을 강요하고 있는 걸지도 몰라"
                    show mel at right
                    mel"……하지만 내가 렌스를 사랑하는 것도 사실이야"
                    mel"그리고 결혼 하는 덴 그거면 되지 않을까?"
                    willy"하지만 상대방이 자신을 사랑하지 않을지도 모르는 건데?!"
                    willy"만약 렌스 씨는 누나를 그저 도구로써 보고 있다면 어쩔 거야?!"
                    show mel talk at right
                    mel"그건……"
                    show mel sirius at right
                    mel"…………"
                    mel"모르겠어……"
                    show effect1
                    play sound "se/shock.ogg"
                    mel"{size=45}나도 모르겠다고!{/size}" with lshake
                    hide effect1
                    mel"뭘 어떻게 해야 할지……"
                    willy"…………"
                    willy"스테반,{cps=2} {/cps}가자"
                    show willy shock:
                        linear 0.3 xalign 0.3
                    show stephan shock at left
                    stephan"어,{cps=2} {/cps}어―"
                    "뭔가 엄청나게 뻘쭘 한 상황이 되어버렸다."
                    play sound "se/footsteps_wood.mp3"
                    scene black with moveright
                    stop music
                    $ renpy.pause(1)
                    scene bg mel_house at Zoom((1280,720),(380,400,560,315),(380,400,560,315),0) with moveright
                    show stephan shock at left
                    show willy talk at right
                    stephan"명함……{cps=2} {/cps}못 얻었네……"
                    play sound "se/book_page.ogg"
                    willy"자"
                    "윌리는 나한테 작은 종잇조각을 줬다."
                    stephan"이건?!"
                    hide stephan shock
                    show willy talk:
                        xalign 0.55 yalign 0.3 zoom 1.7
                    play sound "se/book_page.ogg"
                    show ev bis_card:
                        yoffset 720
                        linear 0.7 yoffset 0
                    play music "bgm/smooth1.mp3"
                    "명함이다."
                    show ev bis_card:
                        linear 0.5 yoffset 720
                    $ renpy.pause(0.5)
                    hide ev bis_card
                    hide willy talk
                    show willy at right
                    show stephan shock at left
                    stephan"이걸 언제?"
                    willy"네가 페이퍼 컴퍼니 얘기를 할 때부터 뭔가 이렇게 될 거 같은 느낌이 들더라고"
                    willy"그래서 둘이서 대화 하는 동안 난 미리 명함을 챙겼지"
                    stephan"…………"
                    show stephan talk at left
                    stephan"렌스는 사기꾼이 맞는 거지……?"
                    show willy talk at right
                    willy"뭐어……{cps=2} {/cps}솔직히 나도 100\%라곤 말 못하지만……"
                    willy"그럴 확률이 높지"
                    willy"근데 이제 와서 왜?"
                    stephan"과연 멜 누나랑 렌스 씨가 결혼하는 걸 막는 게 좋은 건지 고민이 돼서……"
                    show willy shock at right
                    willy"결혼하면 더 큰 문제가 발생하잖아"
                    stephan"하지만……"
                    extend" 멜 누나의 아버지의 마지막 소원 이라고 하니까……"
                    stephan"갈 길이 얼마 남지도 않았는데, 자기 딸이 결혼 하려고 했던 상대가 사기꾼 이라는 걸 알면……"
                    show willy at right
                    willy"훗,{cps=2} {/cps}너 의외로 착하네?"
                    show stephan shock at left
                    stephan"그건 또 무슨 뜻이야?!"
                    willy"들리는 그대로의 뜻이야"
                    show willy talk at right
                    willy"그래,{cps=2} {/cps}네 말대로 렌스를 잡게 되면 누나는 아저씨의 마지막 소원을 이뤄주는 게 힘들지도 모르겠지……"
                    willy"하지만 나도 아저씨한테 부탁받은 게 있거든"
                    show stephan talk at left
                    stephan"무슨 부탁?"
                    willy"\'멜을 나쁜 사람들로 부터 지켜줘\'라고"
                    show willy smile at right
                    willy"멜 누나가 렌스랑 결혼 해버리면, 내가 부탁받은 걸 지켜주는 게 힘들어져서 말이야"
                    stephan"…………"
                    show stephan at left
                    stephan"차라리 네가 멜 누나랑 결혼하는 거 어때?"
                    show willy shock at right
                    willy"뭐?!"
                    stephan"아니,{cps=2} {/cps}너도 몇 년 만 있으면 결혼 가능하잖아?"
                    stephan"그러면 멜 누나는 상처받을 필요도 없을 거 같고……"
                    show willy talk at right
                    stop music
                    willy"……하지만 그렇게 되면, 내가 부탁 받은걸 어기는 게 되잖아"
                    show stephan shock at left
                    stephan"…………"
                    show willy at right
                    willy"그리고 방금 받은 명함은 나한테 줄 수 있을까?"
                    show stephan talk
                    stephan"어, 어─"
                    play sound "se/book_page.ogg"
                    show stephan talk:
                        linear 0.5 xalign 0.7
                        linear 0.5 xalign 0.0
                    willy"그럼 이제 크라크 무역 사무실로 가자"
                    scene black with moveleft
                
                "정말요?! 대단하네요! (거짓)":
                    show stephan at left
                    show mel at right
                    stephan"정말요?"
                    show stephan think at left
                    stephan"우와……{cps=2} {/cps}대단하시네요……"
                    show stephan at left
                    mel"규모는 그렇게 크진 않지만 말이야"
                    stephan"그래도 무역회사라면 앞으로의 가능성이 있잖아요!"
                    show mel talk at right
                    mel"그렇겠지?"
                    mel"내가 투자하길 잘했겠지?"
                    stephan_think"투자?"
                    show stephan think at left
                    "상대방이 자신은 무역회사를 운영하고 있다고 말 한건 꽤 현명한 판단이었다고 생각한다."
                    "일단 오리엔스에선 벤처기업들의 생존이 좀 어렵다."
                    "이유는 류인 그룹에서 조금 뜰 것 같은 아이디어가 있으면 전부 사들이기 때문"
                    "그래도 예전보단 훨씬 좋아졌다."
                    "내가 기억하기로, 몇 년 전엔 류인에서 아이디어를 사들이는 대신 바로 뺏겨서 사용했으니까"
                    "법적인 문제는 대기업의 막대한 자금과 인맥, 변호사 등으로 조용히 처리 시켰고……"
                    "물론 내가 류인에 들어가고 싶은 이유가 그런 식의 \'목적을 달성하기 위해선 뭐든지 한다.\'라는 마음가짐이 멋있어 보여서 지만"
                    "……어쨌건 무역회사 같은 경우 류인에서 직접 하는 것보단 서드 파티 회사를 이용하는 게 더 효율 적이다."
                    "또, 국가에서 해주는 지원 및 혜택 때문에 앞으로의 가능성도 있어서 이런 페이퍼 컴퍼니를 만들게 된다면 사람들을 쉽게 낚을 수 있다."
                    stephan_think"그리고 방금 누나가 \'투자\'라고 했어……"
                    stephan_think"아마 렌스 씨가 시켜서 한 거 겠지?"
                    show stephan at left
                    stephan"이건 좀 개인적인 질문 이긴 한데요……"
                    stephan"렌스 씨를 처음 만난 지 몇 년 밖에 되지 않았고, 거기다 실제로 둘이서 같이 연애를 한 건 몇 개월 밖에 안됐다고 하셨는데……"
                    stephan"연애 몇 개월도 안돼서 결혼 하는 건 너무 빠른 거 아니에요?"
                    show stephan shock at left
                    stephan"따,{cps=2} {/cps}딱히 둘의 결혼을 반대 하는 건 아니고요!"
                    show stephan talk at left
                    stephan"그냥 저희 엄마가 연애는 오래 하고 나서 결혼을 해야 행복 해진다고 말 하셔서……"
                    show mel at right
                    mel"후후……{cps=2} {/cps}정말 옳은 말씀이야"
                    show mel talk at right
                    stop music
                    mel"사실 나도 좀 더 오랫동안 연애를 하고 싶었어……"
                    mel"하지만……{cps=2} {/cps}아버지가……"
                    show mel at right
                    mel"이,{cps=2} {/cps}이거 내가 너무 사적인 말을 꺼내버렸나?"
                    stephan"저는 딱히 신경 안 쓰니까 말씀 하시고 싶으면 하셔도 괜찮아요"
                    show mel talk at right
                    play music "bgm/sad2.mp3"
                    show stephan at left
                    mel"그럼……"
                    mel"얼마 전에 아버지가 사고를 당하신 적이 있으셨어……"
                    show stephan talk at left
                    extend" 그런데 시간이 지날수록 점점 더 상태가 악화되어 가고 있다고 하니까……"
                    mel"병원에선 이제 얼마 남지 않았다고 해서 더 걱정이야"
                    mel"요즘 좀 불경기라서 돈도 잘 안 들어오고 하니까 내가 뭘 어떻게 해주기도 힘들지……"
                    show mel at right
                    mel"그래도 렌스를 만난 덕분에 아버지의 마지막 소원은 지켜줄 수 있게 되어서 아주 나쁜 일만 있는 건 아니야!"
                    stephan"마지막 소원이라는 게 혹시……?"
                    show mel talk at right
                    mel"응……{cps=2} {/cps}아버지께서 내가 결혼 하는 모습을 보는 걸……{cps=2} {/cps}원하셨거든……"
                    show mel sirius at right
                    mel"일 때문에 바빠서 자주 못 찾아뵀었는데……{cps=2} {/cps}혹시 갈때까지 난 그저 아무런 도움도 못되는 딸로 남을까봐 두려웠어……"
                    mel"…………"
                    "멜 누나의 어깨가 조금씩 떨리는 게 보였다."
                    show mel at right
                    mel"어머!{cps=2} {/cps}내가 왜 이렇지?!"
                    mel"이제 다 좋게 돼 가고 있는데!"
                    mel"난 사랑하는 렌스랑 결혼 하고, 아버지도 기뻐 하실 거고!"
                    "확실히 이대로 가면 멜 누나는 행복한 삶을 살 수 있을 거다."
                    "렌스 씨는 사업을 하고 있으니까 누나의 힘든 자금 사정도 해결 될 테고, 아버지의 돌아가시는 소원도 이룰 수 있게 됐고"
                    "하지만……"
                    "문제는 상대방이 페이퍼 컴퍼니를 운영하고 있다는 점……"
                    "그 때문에 멜 누나가 바라고 있는 \'행복한\'미래는 찾아오지 않을 확률이 높겠지"
                    "단순히 찾아오지만 않는다면 모를까……{cps=2} {/cps}더욱 불행해 질 것 같았다."
                    show stephan at left
                    stephan"남자친구……{cps=2} {/cps}아니, 예비 신랑이 운영하고 있는 무역 회사가 번성했으면 좋겠네요……"
                    stephan"제가 응원 해 드릴게요!"
                    mel"후후후"
                    mel"고마워~"
                    play sound "se/search_bag.mp3"
                    "나는 몸을 일으키기 위해서 팔에 힘을 줬다."
                    "그런데……"
                    show stephan shock at left
                    show effect1
                    play sound "se/shock.ogg"
                    stop music
                    stephan_think"{size=45}……잠깐!{/size}" with lshake
                    play music "bgm/beat3.mp3"
                    stephan_think"생각해보니까 내가 렌스 씨의 명함을 얻으려고 왔었지?!"
                    hide effect1
                    stephan"저어……{cps=2} {/cps}누나?"
                    show mel talk at right
                    mel"왜?"
                    show stephan shock2 at left
                    stephan"그……{cps=2} {/cps}남자 친구 분의 무역 회사 있잖아요?"
                    stephan"생각해보니까 어쩌면 제가 뭔가 도움이 될지도 몰라요!"
                    mel"음?{cps=2} {/cps}어떻게……?"
                    stephan"저,{cps=2} {/cps}제 어머니가 관련 업종에 종사하시거든요!"
                    stephan"그러니까 어쩌면 바이어 한 둘이라도 소개 시켜 드릴 수 있을지도……"
                    show mel at right
                    mel"정말?!"
                    show stephan smile2 at left
                    stephan_think"훗"
                    "일단 멜 누나는 렌스 씨에게 돈을 투자했다."
                    "그러니 당연지사 렌스 씨가 하는 일의 번성을 기여 하겠지 —물론, 굳이 투자 때문이 아니라 연인이라서 이기도 하지만—"
                    "그리고 내가 딱히 돈을 달라는 것도 아니고, 그저 아는 사람을 소개시켜 주겠다고 말 한거 뿐이니까 상대방에겐 아무런 손실이 없다."
                    "즉, 망설임이 필요 없다는 뜻"
                    "여기서부턴 내가 명함을 요구하는 게 매우 당연하지"
                    mel"혹시 어머님 명함 같은 거라도 있어?"
                    show stephan shock at left
                    stephan"앗……"
                    "하지만 이렇게 나와도 아무런 문제없다."
                    show stephan shock2 at left
                    stephan"제,{cps=2} {/cps}제가 평상시에 명함을 가지고 다니는 게 아니라 서요!"
                    stephan"저한테 남자 친구 분의 명함을 주시면 제가 어머니께 잘 말씀 드릴게요"
                    show mel talk at right
                    mel"렌스의 명함이란 말이지?"
                    mel"음……{cps=2} {/cps}잠깐만……"
                    play sound "se/footsteps_wood.mp3"
                    show mel talk:
                        linear 1.0 xalign 2.0
                    $ renpy.pause(3.0)
                    hide mel talk
                    play sound "se/search_bag.mp3"
                    $ renpy.pause(2.0)
                    mel"찾았다!"
                    show mel:
                        xalign 2.0 yalign 1.0
                        linear 1.0 xalign 0.8
                    mel"여기!"
                    play sound "se/book_page.ogg"
                    hide stephan shock2
                    hide mel
                    show ev bis_card:
                        yoffset 720
                        linear 0.7 yoffset 0
                    "나는 명함을 봤다."
                    stephan_think"\'클라크 무역\' 이라……"
                    stephan_think"이름에서 부터 완전 페이퍼 컴퍼니 냄새가 풀풀 나는구만"
                    willy"혹시 둘이 대화 끝났어?"
                    play sound "se/book_page.ogg"
                    show ev bis_card:
                        yoffset 0
                        linear 0.7 yoffset 720
                    $ renpy.pause(0.7)
                    show stephan at left
                    show mel at right
                    show willy:
                        xalign 0.3 yalign 1.0
                    stephan"응"
                    willy"그럼 이제 슬슬 가볼까?"
                    mel"둘 다 잘 가렴~"
                    stephan"안녕히 계세요"
                    stop music
                    play sound "se/footsteps_wood.mp3"
                    scene black with moveright
                    $ renpy.pause(1.5)
                    play music "bgm/smooth4.mp3"
                    scene bg mel_house at Zoom((1280,720),(380,400,560,315),(380,400,560,315),0) with moveright
                    show stephan talk at left
                    show willy at right
                    willy"아까 안에서 말 잘하더라?"
                    stephan"그래?"
                    willy"응"
                    willy"근데 너희 어머님 진짜로 관련 업종에서 일 하셔?"
                    stephan"아니, 우리 엄마 대학원생이야"
                    stephan"아마 일 할 시간도 없어 할 걸?"
                    show willy talk at right
                    willy"그럼 안에서 한 말은 거짓말 이었다는 거로군……"
                    stephan"…………"
                    stephan"거짓말……{cps=2} {/cps}이라고 하니까 좀 걸리는 게 있어……"
                    willy"뭔데?"
                    stephan"멜 누나랑 렌스 씨가 결혼 하는 걸 막는 게 과연 좋은 일 일까?"
                    show willy shock at right
                    willy"어?!"
                    extend" 왜 그런 생각을?"
                    stephan"일단 누나한테 클라크 무역이 페이퍼 컴퍼니라는 사실에 대해서 아무 말도 안했으니까……"
                    stephan"혹시 나중에 그 사실 때문에 충격 받지 않을까 싶어서"
                    show willy talk at right
                    willy"누나도 페이퍼 컴퍼니라는 사실에 대해서 어느 정도 알고 있어"
                    show effect1
                    show stephan shock at left
                    play sound "se/shock.ogg"
                    stephan"{size=45}정말?!{/size}" with lshake
                    hide effect1
                    willy"예전에 내가 말 해 준 적이 있었거든"
                    willy"……근데 끝까지 부정을 하더라고"
                    willy"지금도……"
                    willy"아무튼, 내가 미리 말 해줬으니까 네가 생각하는 만큼의 충격은 안 먹을 거야"
                    willy"그러니까 누나가 쇼크 받을 걸 걱정은 하지 마"
                    show stephan talk at left
                    stop music
                    stephan"그거 말고도 걱정되는 게 또 있어……"
                    stephan"멜 누나의 아버지 있잖아……"
                    stephan"돌아가시기 전에 멜 누나가 결혼 하는 걸 보고 싶다고 했는데……{cps=2} {/cps}사실은 그 신랑이 사기꾼 이라는 걸 알아도 괜찮을까?"
                    show willy shock at right
                    willy"그 쪽은……"
                    show willy talk at right
                    willy"…………"
                    play music "bgm/smooth1.mp3"
                    show willy at right
                    willy"그거 알아?{cps=2} {/cps}나도 멜 누나의 아버지랑 꽤 아는 사이 라는 거?"
                    stephan"네 부모님이랑 누나의 부모님이 친하셨다고 했던 거 같기도 하고……"
                    willy"응"
                    willy"그래서 나도 아저씨한테 부탁 받은 게 있거든……"
                    extend" \'멜을 나쁜 사람들로 부터 지켜줘\'라고 말이야"
                    show willy smile at right
                    willy"그러니까 멜 누나가 아저씨의 마지막 약속을 지켜주고 싶은 것처럼, 나도 지켜주고 싶어"
                    willy"그 뿐이야"
                    show stephan at left
                    "그 말을 들으니까 조금 마음이 가벼워졌다."
                    "멜 누나랑 윌리……{cps=2} {/cps}둘 다 한 사람의 마지막 소원을 이뤄 주겠다는 공통점을 가지고 있다."
                    "그러니 내가 누군가의 마음을 짚 밟는다는 생각을 할 필요가 없다."
                    show willy at right
                    willy"아, 그리고 방금 받은 명함은 나한테 줄 수 있을까?"
                    show stephan talk
                    stephan"어, 어─"
                    play sound "se/book_page.ogg"
                    show stephan talk:
                        linear 0.5 xalign 0.7
                        linear 0.5 xalign 0.0
                    willy"그럼 클라크 무역으로 갈까?"
                    show stephan smile at left
                    stephan"응"
                    play sound "se/move.mp3"
                    stop music
                    scene black with moveleft
            
        "혹시 비결 같은 거라도 있나요? (거짓)":
            play music "bgm/beat3.mp3"
            show stephan smile at left
            show mel talk at right
            stephan"혹시 인생의 비결 같은 거라도 있나요?!"
            show mel at right
            mel"에이~{cps=2} {/cps}비결 이라니~"
            mel"그런 게 있을 리가 없잖아~"
            show stephan at left
            stephan"하지만 우연 이라고 하기엔 너무 좋은 일이 많으신 거 아니에요?"
            stephan"전직 대기업에서 일 했던 능력 있는 남자 친구랑 곧 있으면 결혼 하고, 이렇게 멋있는 집에서 살고 있고!"
            stephan"뭔가 연애의 비결이 있으면 전술 해주세요!"
            stephan"제가 거의 평생을 솔로로 살다보니까 워낙 외롭고……"
            show stephan sad at left
            show effect2
            play sound "se/shock2.mp3"
            stephan_think"생각해보니까 내가 진짜 평생을 솔로로 살아왔었네……"
            hide effect2
            show stephan sad2 at left
            show mel talk at right
            stephan"흑……"
            stephan"……어,{cps=2} {/cps}어쨌건, 저한테도 좋은 연인이 생겼으면 좋겠어요!"
            stephan"그,{cps=2} {/cps}그러니까 제발 뭔가 비결을……!"
            show willy shock:
                xalign 0.3 yalign 1.0
            willy"{size=25}너, 지금 마음속에서 부터 호소하는 게 느껴져;;{/size}"
            show stephan shock2 at left
            stephan"아……{cps=2} {/cps}음……"
            hide willy shock
            mel"그,{cps=2} {/cps}그렇게 비결을 말 해달라고 해도……"
            extend" 딱히 뭔가 있는 게 아니라서 말이지……"
            stephan"…………"
            stephan"역시……"
            play music "bgm/beat1.mp3"
            show stephan smile at left
            extend" 누나의 비결은 \'겸손\'이군요!"
            mel"겸……{cps=2} {/cps}손?"
            stephan"네!"
            show willy smile2:
                xalign 0.3 yalign 1.0
            willy"확실히 너한텐 없는 거네"
            show stephan shock at left
            stephan_think"이 새끼가?!"
            show stephan shock2 at left
            stephan"무,{cps=2} {/cps}무슨 소리야, 나의 친구 윌리"
            stephan"누나만큼은 아니지만, 나도 충분히 겸손 하다고?"
            show willy
            willy"하지만 자기 자신을 \'겸손\'하다고 칭하는 건 \'자만\'인데?"
            show stephan shock at left
            stephan"윽……"
            show mel at right
            mel"어머어머 윌리가 무슨 소리야"
            mel"내가 보기엔 스테반이 너보다 훨씬 겸손해 보이는데?"
            show stephan smile at left
            show willy shock
            stephan"메롱~"
            willy"어이;;"
            mel"윌리가 어렸을 땐 자기가 어찌나 똑똑하다고 생각했는지……"
            mel"막 나한테 공부를 가르쳐 주겠다고 하더라고!"
            show stephan smile2 at left
            stephan"훗,{cps=2} {/cps}설마 윌리가 그랬을 줄 이야~"
            willy"그,{cps=2} {/cps}그래도 내 스스로가 똑똑 하다고 말 한 적은 한 번도 없었거든!"
            willy"그리고 그때 내가 가르쳐준 덕분에 누나는 류인에 합격 할 수 있었잖아?"
            show mel talk at right
            mel"뭐어……"
            extend" 확실히 네 공이 컸긴 했지……"
            show stephan shock at left
            stephan_think"어?!"
            extend" 윌리가 가르쳐줘서 합격 할 수 있었다고?!"
            "매우 놀랄 일 이었다."
            "누나가 류인에 일 하기 전 이라면 윌리는 최소한 중학생"
            "근데 고작 중학생이 대학생도 힘들어하는 문제를 가르쳐줬다니……"
            show effect1
            play sound "se/shock.ogg"
            show stephan fear at left
            stephan"{size=45}이,{cps=2} {/cps}이건 사기다!!{/size}" with lshake
            hide effect1
            willy"갑자기 무슨 소리야?"
            stephan"어렸을때 부터 공부를 잘했다니!{cps=2} {/cps}너무한 거 아니야?!"
            show willy talk
            willy"나, 그렇게 공부 잘하는 것도 아니거든?"
            show willy
            willy"그냥 누나의 이해력이 좋아서 쉽게 합격 할 수 있었던 거지"
            mel"어머?{cps=2} {/cps}언제는 \'누나는 왜 이것도 몰라?!\'라면서 혼냈더니"
            show willy shock
            willy"으……"
            willy"누나 나한테 무슨 원한이라도 있어?"
            extend" 왜 계속 내 흑역사를……"
            show mel at right
            mel"후후……{cps=2} {/cps}윌리의 당황하는 모습이 참 귀여워서~"
            willy"으……"
            mel"그래,{cps=2} {/cps}그 표정이야"
            mel"스테반~ 스테반~{cps=2} {/cps}윌리가 어렸을 때 나한테 또 뭐라고 했냐ㅁ……"
            show willy shock:
                linear 0.3 xalign 0.7
            willy"그,{cps=2} {/cps}그만;;"
            mel"후후후"
            show stephan talk at left
            "저런 윌리는 처음 본다."
            "평상시엔 냉정하고 침착 하면서도 밝게 있던 윌리가……{cps=2} {/cps}자기 누나 앞에선 이렇게도 변하는구나 싶었다."
            play sound "se/move.mp3"
            scene black with moveleft
            $ renpy.pause(0.3)
            scene bg room_mel at Zoom((1280,720),(536,103,744,419),(536,103,744,419),0) with moveleft
            show mel at right
            show willy shock:
                xalign 0.3 yalign 1.0
            show stephan shock at left
            "둘이서 아주 알콩달콩하게 티격태격 한 지 벌써 몇 분이 지났다."
            "그때 멜 누나가 분위기를 깨는 말을 해버렸다."
            mel"으이그 이 시스콘이 어찌나 질투가 많든지~"
            stop music
            mel"언제는 또 내가 렌스랑 결혼 한다고 하니까 막 그이가 페이퍼 컴퍼니를 운영하고 있다고 하고~"
            willy"누나, 그건……"
            "페이퍼 컴퍼니 얘기가 나왔다.{cps=2} {/cps}생각 해보니까 애초에 내가 여기에 온 이유가 그거랑 관련이 있었지"
            show stephan at left
            "나는 이때가 명함을 얻을 수 있을 찬스라고 생각 했다."
            hide willy shock
            show stephan talk at left
            stephan"페이퍼 컴퍼니라니요?{cps=2} {/cps}혹시 사업 하시는 분이에요?"
            play music "bgm/smooth1.mp3"
            mel"응~{cps=2} {/cps}그것도 무역 회사를 하고 있지!"
            mel"자랑은 아니지만 말이야~{cps=2} {/cps}요즘 정부에서 무역에 대한 투자가 많다보니까 앞날이 아주 창창해!"
            mel"근데 윌리가 계속 그 회사가 페이퍼 컴퍼니라면서 거짓말을 하니까……"
            show willy talk:
                xalign 0.3 yalign 1.0
            mel"윌리,{cps=2} {/cps}다시 말하지만, 그건 페이퍼 컴퍼니가 아니라 규모가 작은 중소기업 이야"
            mel"그래서 인터넷에서 자료를 많이 찾아 볼 수가 없는 거란다~"
            willy"…………"
            "하지만 윌리는 꿈쩍도 하지 않았다."
            "페이퍼 컴퍼니임을 확신 하고 있었던 것 같았다."
            play sound "se/footsteps_running.mp3"
            show mel:
                linear 0.5 xalign 2.0
            $ renpy.pause(2.5)
            play sound "se/footsteps_running.mp3"
            show mel:
                linear 0.5 xalign 1.0
            $ renpy.pause(1.0)
            play sound "se/book_page.ogg"
            mel"여기 제대로 된 명함도 있다고?"
            "참고로, 명함을 가지고 있다고 해서 페이퍼 컴퍼니가 아니라는 건 아니다."
            "명함은 그냥 근처 명함 집에 가면 싼 값에 아무 질문도 없이 바로 만들어준다."
            stephan_think"하지만 대기업의 \'직장인\'이나 되는 사람이 그걸 모를 리가 없을 텐데?"
            "……억측 일지도 모르겠지만, 멜 누나는 지금 렌스 씨가 페이퍼 컴퍼니를 운영 하고 있다는 걸 부정 하는 듯 보였다."
            "왜 일까?"
            "곧 있으면 같이 결혼을 하기 때문에?{cps=2} {/cps}그래서 결혼에 방해되는 부정적인 생각은 하지 않으려고?"
            "아니, 그러면 오히려 더 말려야 하지 않은가?"
            stephan_think"하지만 난 멜 누나한테 \'누나의 남친이 사기꾼이에요\' 라고 말 하러 온 게 아니니까……"
            stephan_think"그냥 명함만 얻으면 되는 거야"
            "나는 누나의 결혼에 대한 환상을 깰만한 말은 전혀 하지 않기로 했다."
            hide willy talk
            show stephan smile at left
            stephan"남자 친구가 사업을 하세요?!"
            extend" 그것도 무역을?!"
            mel"그럼~!"
            stephan"거기다 누나는 류인 라는 초 대기업에서 일 하시잖아요?!"
            show stephan think at left
            stephan"또, 곧 있으면 같이 결혼을 하신다고 했고……"
            show stephan shock at left
            stephan"이거 너무 쩌는 커플 아닌가요?"
            show stephan smile at left
            stephan"역시 겸손 말고 다른 비결도 있는 거죠?!"
            "내가 조금 과장되게 말을 한 것 같은 느낌이 들었다."
            mel"전부 엄청난 우연에 불과해~"
            mel"내가 시내에서 렌스를 만난 것도 전부 우연의 일치였을 뿐이니까……"
            show stephan at left
            stephan"그게 전부 운 이라면, 누나는 엄청난 행운을 타고나셨어요!"
            stop music
            show mel talk at right
            mel"내가 운이 좋다기보단……{cps=2} {/cps}불행을 다 써버렸다고 해야 할까……"
            show stephan talk at left
            "그런 말을 하는 누나의 표정은 조금 우울해 보였다."
            stephan"누나……?"
            show mel at right
            mel"미,{cps=2} {/cps}미안!"
            mel"그냥……{cps=2} {/cps}그날 내가 우연히 렌스를 만난 덕분에 이전에 있었던 많은 일들이 해결 돼서 말이야……"
            mel"확실히 운이 좋다고 생각해도 되겠지?"
            show stephan at left
            play music "bgm/smooth6.mp3"
            stephan"그건 단순한 \'우연\'이 아니라 \'운명\'이 아닐까요?"
            mel"후훗,{cps=2} {/cps}꽤 낭만적인 말을 하는구나?"
            show stephan blush at left
            stephan"나,{cps=2} {/cps}낭만적 이라니?!"
            stephan"……정말요?"
            mel"그럼~{cps=2} {/cps}이 누나도 \'운명론\'같은 거 좋아하거든~"
            mel"뭔가 낭만이 느껴진다고 해야 할까?"
            show stephan talk at left
            mel"후훗,{cps=2} {/cps}정말 이렇게 생각하면 또 모든 게 운명적 인 것 같은 느낌이 드네"
            stephan"어떤게요?"
            mel"그게……"
            extend" 내가 렌스를 만남으로써 나한테 있던 모든 문제가 다 해결이 되더라고……"
            show mel talk at right
            mel"아버지의 마지막 소원도……{cps=2} {/cps}전부……"
            stephan"마,{cps=2} {/cps}마지막 소원이라니요?!"
            mel"얼마 전에 아버지가 교통사고를 당하셨는데……{cps=2} {/cps}계속 몸이 회복이 안돼다가,{cps=2} {/cps}병원에선 더 이상 가망이 없다고 하더라고……"
            mel"길어봤자 일 년……"
            mel"게다가 류인에선 이런저런 일이 있어서 지금의 내 경제력만 가지곤 뭔가 특별한 걸 해 드릴수도 없었고……"
            show mel sirius at right
            mel"정말 미치는 거 같았어……"
            mel"어렸을 땐 맨날 폐만 끼쳤는데……{cps=2} {/cps}막상 내가 해줄 때가 되니까 사회가 그걸 용납하지 않고……"
            mel"하지만 그런 말괄량이 딸에 대한 아버지의 마지막 소원은 정말 작은 거였어"
            mel"그저……{cps=2} {/cps}신랑의 얼굴을 보고 싶다고 하셨어……"
            extend" 자기가 안심하고 갈 수 있도록……"
            show mel at right
            mel"하지만 얼마 전에 우연히 렌스를 만난 덕분에 모든 게 잘 풀릴 수 있었어!"
            mel"사업가에, 회사에 있었을 때부터 좋아했었고, 정말 상냥하고……"
            mel"그때의 만남은 그야말로 \'운명\'이었지"
            "왜 누나가 젊은 나이에 결혼 하고, 렌스 씨의 회사가 페이퍼 컴퍼니임을 부정하는지 이제 알 것 같았다."
            "바로 자신의 아버지를 위해서 였다."
            show stephan mad at left
            "그리고 만약 그게 사실이라면 렌스 씨는 정말 천하의 개쌍놈 이다."
            stephan"혹시……{cps=2} {/cps}렌스 씨가 운영 중인 무역 회사에 투자 같은 거라도 하셨어요?"
            show mel talk at right
            mel"그렇긴 하다만……{cps=2} {/cps}왜?"
            stop music
            "렌스 클라크……{cps=2} {/cps}역시 멜 누나한테서 돈을 뜯었다."
            play music "bgm/smooth1.mp3"
            show stephan smile at left
            stephan"저도 투자가 하고 싶어져서요!"
            mel"투자를 하겠다고?"
            stephan"네!{cps=2} {/cps}무역 회사는 앞으로의 길이 밝으니까 딱히 손해가 될 거 같진 않아서요"
            stephan"그리고 또……{cps=2} {/cps}누나의 말을 듣고 좀 감동 받았다고 해야 할까요……"
            mel"많이 어른 스럽구나?"
            show stephan shock2
            stephan"그, 그런가요?"
            mel"투자 해주겠다면 정말 고맙지!"
            show mel talk at right
            mel"하지만 아직 회사 규모가 작다보니까 증권회사엔 등록을 하지 못했다고 하더라고……"
            show stephan at left
            stephan"명함 같은 거라도 주시면 제가 나중에 따로 연락을 드릴게요!"
            stephan"모의 주식을 제외한, 저의 첫 주식 투자이기도 하니까 뭔가 어드바이스 라도 들으면 좋을 거 같기도 하고요"
            show mel at right
            mel"그거 좋은 생각이네!{cps=2} {/cps}어쩜 윌리는 이렇게 똑똑한 친구를 사귈까 몰라~"
            play sound "se/book_page.ogg"
            mel"자"
            "멜 누나는 나한테 명함을 줬다."
            hide mel
            hide stephan
            show ev bis_card:
                yoffset 720
                linear 0.7 yoffset 0
            "이걸로 내가 여기에 온 목적은 달성했다."
            stephan_think"죽어가는 사람의 마지막 소원을 이용하는 사기꾼……{cps=2} {/cps}절대 용서 할 수 없어……"
            stephan_think"하지만……{cps=2} {/cps}마지막 소원 이라는 것도 조금 걸려……"
            play sound "se/book_page.ogg"
            show ev bis_card:
                yoffset 0
                linear 0.7 yoffset 720
            "나는 명함을 주머니에 놓고 나갈 준비를 했다."
            hide ev bis_card
            show stephan at left
            show willy:
                xalign 0.3 yalign 1.0
            show mel at right
            willy"시간이 벌써 이렇게 됐네?{cps=2} {/cps}슬슬 가볼까?"
            stephan"그래"
            stephan"오늘 여러모로 즐거웠어요 누나"
            mel"응~{cps=2} {/cps}언제든지 또 오렴~"
            play sound "se/footsteps_wood.mp3"
            stop music
            scene black with moveright
            "나랑 윌리는 집 밖으로 나갔다."
            scene bg mel_house at Zoom((1280,720),(380,400,560,315),(380,400,560,315),0) with moveright
            show willy at right
            show stephan talk at left
            willy"이제 클라크 무역으로 가볼까?"
            stop music
            stephan"그 전에 한 가지 물어볼게 있어……"
            willy"뭔데?"
            play music "bgm/sirius5.mp3"
            stephan"렌스 라는 사람이 사기꾼 이라는 걸 밝히고 나면……{cps=2} {/cps}멜 누나랑, 아버지는 어떻게 돼?"
            show willy shock at right
            willy"그건……"
            "역시 윌리도 망설이는 게 보였다."
            "만약 렌스 씨가 사기꾼임이 밝혀진다면……{cps=2} {/cps}멜 누나는 아버지가 살아 계시는 동안은 결혼을 하지 못하게 된다."
            "그렇게 되면 당연히 신랑의 얼굴을 보고 싶다는 아버지의 마지막 소원도 이뤄줄 수 없게 되겠지……"
            "멜 누나가 말 한 \'운명\'이라는 게……{cps=2} {/cps}생각했던 것 보다 낭만적이지 못했다."
            stephan"우리가 하고 있는 일이 과연 옳은 일 일까?"
            show willy talk at right
            willy"……혹시 내가 학교에서 해줬던 말 기억해?"
            willy"나랑 멜 누나의 부모님이 서로 가까웠다는 거"
            stephan"응"
            willy"그 때문인지, 나도 아저씨한테서 마지막 소원을 들어버렸어"
            stop music
            willy"\'멜을 나쁜 사람들로 부터 지켜줘\'라고"
            show willy smile at right
            willy"그러니까 설령 이번일이 실패 한다고 해도 아저씨한텐 아무런 손해가 없지~"
            stephan"…………"
            show willy at right
            willy"그리고 방금 받은 명함은 나한테 줄 수 있을까?"
            stephan"자"
            play sound "se/book_page.ogg"
            show stephan talk:
                linear 0.5 xalign 0.7
                linear 0.5 xalign 0.0
            willy"그럼 이제 크라크 무역 사무실로 가자"
            scene black with dissolve
    centered"\'클라크 무역\' 사무실 근처"
    scene bg office_outside with moveup
    play bgs "bgs/street.mp3"
    play music "bgm/smooth2.mp3"
    "주소대로라면 여기가 회사다."
    "내가 생각했던 회사의 이미지랑은 많이 다르긴 하지만……"
    "중소기업이니까 어쩔 수 없는 건가?"
    "아니……{cps=2} {/cps}건물이 저래가지곤 중소기업 이라는 타이틀도 크게 느껴진다……"
    "저건 영세기업에 가깝다……"
    show willy at right
    show stephan talk at left
    willy"저번에 왔을 때랑 변한 게 없네……"
    stephan"여기 와본 적 있어?"
    willy"어,{cps=2} {/cps}조금 다른 이유로 와본적이 있었어"
    stephan"그런데 명함에다, 건물까지……"
    stephan"정말 페이퍼 컴퍼니가 맞긴 하냐?"
    willy"공들이긴 했지만, 내가 마지막으로 조사 해봤을 땐 이 회사는 소유자산은 물론, 아무런 활동이 없었어"
    willy"고로,{cps=2} {/cps}페이퍼 컴퍼니로 분류되는 거지"
    show stephan think at left
    stephan"그렇구나……"
    show willy shock at right
    willy"윽!"
    show stephan shock at left
    willy"나 화장실이 좀 가고 싶은데……"
    stephan"타이밍 한번 최악이잖아!"
    willy"아무래도 내가 뭔가 잘못 먹었나봐"
    stephan"그럼……{cps=2} {/cps}난 네가 돌아올때까지 여기서 기다리고 있을게"
    willy"아니,{cps=2} {/cps}먼저 들어가서 렌스 씨랑 얘기 하고 있어"
    stephan"하지만 계획이!"
    willy"그냥 렌스 씨가 사기꾼임을 증명하는 서류나 증거물을 모으기만 하면 돼"
    willy"……아주 심플하지?"
    play sound "se/footsteps_running.mp3"
    show willy shock:
        linear 0.7 xalign 2.0
    willy"그럼 난 간다~!"
    "그대로 윌리의 모습이 내 시야에서 사라졌다."
    hide willy shock
    stephan"나쁜 자식……"
    "하지만 나의 물주는 윌리다.{cps=2} {/cps}PX4를 위해서라면 이런 이런 것 쯤이야"
    show stephan think at left
    stephan_think"일단 윌리는 사기를 증명하는 증거를 모으라고 했지?"
    stephan_think"아무래도 멜 누나한테 렌스 씨의 정체를 밝힌 뒤 결혼을 하지 말라고 할 생각 인가보군……"
    play sound "se/footsteps_concrete.mp3"
    scene bg office_outside at Zoom((1280,720),(0,0,1280,720),(517,291,763,429),2.5) with Dissolve(1.0)
    "나는 사무실의 문 앞으로 다가가서 두드린다."
    play sound "se/door_knock.mp3"
    $ renpy.pause(2)
    play sound "se/door_open.ogg"
    show lance talk with dissolve
    $ renpy.pause(1)
    "잠시 후 문을 연 건 양복을 입고 안경을 낀 남성이었다."
    "잠깐 사무실 내부를 곁눈질로 바라봤는데, 안엔 검게 태닝 됐으면서, 하와이 셔츠를 입고 있는 건장한 남성이 있었다."
    "정말 방금 전까지 하와이에서 놀고 왔다고 해도 믿을 것 같았다."
    someone"누구세요……?"
    show lance talk at right
    show stephan at left
    stephan"혹시 성함이 \'렌스 클라크\' 이신가요?"
    lance"맞습니다만……"
    extend" 그쪽은 누구신지?"
    menu:
        "제 이름은 \'스테반 토머\' 라고 합니다 (진실)":
            $ lance_truth = True
            show stephan at left
            stephan"제 이름은 \'스테반 토머\' 라고 합니다"
            stephan"멜 누나랑 아는 사인데 혹시 아시나요?"
            lance"멜 이랑 아는 사이라고……?"
            "렌스 씨는 내 몸을 잠깐 훑어봤다."
            "기분 나쁜 건 둘째 치더라도, 저 반응이 나를 불안케 했다."
            "뭔가 내가 올 걸 예상 한듯 한 반응 이라고 해야 할까?"
            "하지만 그럴 리가 없다.{cps=2} {/cps}나랑 렌스 씨는 오늘이 초면인 걸"
            show lance sad at right
            lance"죄송합니다.{cps=2} {/cps}아직 멜 친구에 대해선 잘 몰라서요……"
            show stephan shock2 at left
            stephan"아,{cps=2} {/cps}아니에요!"
            stephan"멜 누나한테서 많이 들었는데……{cps=2} {/cps}혹시 시간 있으신가요?"
            show lance at right
            lance"네,{cps=2} {/cps}시간이라면 꽤 많죠"
            stephan"전 아직 학생이니까 그냥 편하게 말씀 하셔도 괜찮아요!"
            lance"아……{cps=2} {/cps}그렇단 말이지……?"
            lance"그럼 서서 얘기하기도 그렇고 누추하지만 들어와"
            stephan"실례하겠습니다"
            scene black with moveright
            stop bgs
            play sound "se/footsteps_wood.mp3"
            $ renpy.pause(3)
            play music "bgm/smooth1.mp3"
            scene bg office_inside with moveright
            "나는 사무실 안으로 들어왔다."
            "내부는 꽤 평범했다."
            "책상에, 소파에, 컴퓨터 까지……"
            extend" 한 가지 특이점이 있다면, 인테리어가 좀 텅텅 비어있는 듯한 느낌 정도려나?"
            "안에 사람은 알록달록한 하와이풍의 와이셔츠를 입은 건장한 남자 —편의상 미스터 하와이 라고 부르겠다— 한명과 렌스, 둘 뿐이었다."
            lance"여기 앉아"
            play sound "se/search_bag.mp3"
            scene bg office_inside at Zoom((1280,720),(0,0,1280,720),(462,269,802,451),0.5) with dissolve # 사무실 내부
            show stephan talk at left
            "나는 렌스의 말대로 소파에 앉았다."
            show stephan shock2 at left
            "그때 미스터 하와이가 내 뒤로 이동한 뒤 그곳에서 가만히 나를 노려보고 있었다."
            "……그것도 엄청 부담스럽게"
            show lance at right
            lance"오늘 여기로 찾아 온 이유가 뭐지?"
            stephan"어……{cps=2} {/cps}음……{cps=2} {/cps}그게……"
            stephan_think"잠깐,{cps=2} {/cps}나 뭐라고 해야지?!"
            stephan_think"사업에 관심이 있는데 직업 인터뷰를 하고 싶다고 하면서 접근을 하는 게 좋으려나?!"
            show stephan think at left
            "나는 어떻게 해야 렌스 씨에게 서류를 얻을 수 있을지 생각했다."
            stephan_think"역시 직업 인터뷰와 관련을 지어서 여러 질문을 하면 돼"
            stephan_think"그때 사업 하는데 필요한 서류의 종류나 그의 작성 방법 등을 물어보면서 슬쩍 보는 거지……"
            stephan_think"하지만 그렇게 하면 렌스 씨가 나를 의심하면서 내 쫓지 않을까?"
            stephan_think"음……"
            show stephan shock at left
            "뭔가 특별한 계획도 없이 와서 그런 건지, 뭘 어떻게 해야 할지 잘 떠오르지 않았다."
            show lance talk at right
            lance"\'로날드(Ronald)\'씨, 혹시 나가서 커피 좀 사와 주실 수 있나요?"
            "렌스 씨가 나를 노려보고 있던 미스터 하와이에게 말 했다."
            "……이름이 로날드로 추정되긴 하지만, 저 모습 때문에 나는 미스터 하와이 라고 부르고 싶다."
            $ extra_name = '미스터 하와이'
            extra"네"
            play sound "se/footsteps_concrete.mp3"
            $ renpy.pause(3.0)
            play sound "se/door_open.ogg"
            "미스터 하와이는 건물 밖으로 나갔다."
            "아무래도 렌스 씨는 내가 어쩔 줄 몰라 하는 이유가 저사람 때문인 줄 알았나보다."
            stephan_think"……아주 틀린 말은 아니지만"
            show lance at right
            lance"그래서 오늘 날 찾아 온 이유가?"
            "나는 그냥 대충 직업 조사를 위해서 왔다고 얼버무리기로 했다."
            show stephan shock2 at left
            stephan"그,{cps=2} {/cps}그게……{cps=2} {/cps}사업에 대해서 여러 가지 듣고 싶어서요!"
            show stephan think at left
            stephan"제가 나중에 크면 사업을 하고 싶은데 제 주변에선 그런 사람이 없었거든요……"
            show stephan smile at left
            stephan"근데 멜 누나가 곧 있으면 같이 결혼 하는 상대가 사업을 한다면서 소개 받았어요!"
            show stephan shock2 at left
            stephan"그래서 사업에 관한 일종의 직업 인터뷰……{cps=2} {/cps}같은 거 라고 해야 할까요?"
            stephan"이,{cps=2} {/cps}인터넷 보단 그런 일을 하고 있는 장본인한테서 직접 듣는 게 더 좋을 거 같기도 하고……"
            lance"확실히 그렇긴 하네"
            extend", 멜이 너한테 나를 소개 시켜줬다면 나도 기대에 부응해야겠지?"
            lance"궁금한 건 뭐든지 물어봐도 좋아"
            lance"대신……{cps=2} {/cps}나도 몇 가지 질문해도 될까?"
            stephan"제,{cps=2} {/cps}제가 뭔가 도움이 될까요?"
            lance"멜이랑 아는 사이 라면서?{cps=2} {/cps}난 곧 있으면 같이 결혼하는 사이기도 하니까 말이야"
            lance"가능하면 많은 정보를 얻고 싶거든"
            show stephan think at left
            stephan_think"이거, 내가 제대로 대답을 할 수 있으려나……"
            show stephan at left
            stephan_think"어떻게든 되겠지!{cps=2} {/cps}보니까 뭔가 복잡 한 걸 물어볼 거 같지도 않고"
            stephan"네!{cps=2} {/cps}제가 대답해드릴 수 있는 거라면 뭐든지 해드리겠습니다"
            stephan"그럼……"
            play sound "se/door_open.ogg"
            $ renpy.pause(0.5)
            extra"……저기"
            "내가 렌스 씨에게 질문을 하려는 찰나, 방금 전까지 이 방에 있었던 미스터 하와이가 문을 열며 고개만 빼곰히 내밀면서 렌스 씨를 불렀다."
            extra"클라크 사장님……?{cps=2} {/cps}잠깐 좀 하고 싶은 말이 있는데 괜찮을까요?"
            show lance shock at right
            lance"급한 용무야?"
            extra"네"
            show lance at right
            lance"이거, 내 동업자가 날 필요로 하는군.{cps=2} {/cps}토머 군의 질문은 나중에 들어볼게"
            play sound "se/footsteps_concrete.mp3"
            scene bg office_inside at Zoom((1280,720),(462,269,802,451),(75,269,802,451),1.4) with dissolve
            $ renpy.pause(2.0)
            show lance:
                xalign 0.5 yalign 1.2
                linear 1.5 yalign -1.5 zoom 1.3
            $ renpy.pause(1.5)
            play sound "se/door_open.ogg"
            hide lance with dissolve
            "렌스 씨와 미스터 하와이는 밖으로 나갔다."
            "이 찬스를 이용하면 윌리가 말했던 \'사기꾼임을 증명하는 물건\'을 찾을 수 있을지도 모른다."
            "……하지만 밖에서 둘이서 무슨 대화를 하는지도 궁금했다."
            "일단 아까 봤던 미스터 하와이는 진짜 동업자 같은 느낌이 아니었고……{cps=2} {/cps}뭔가 힘 좀 쓸것 같은 느낌이 더 강했다."
            stephan_think"후훗……{cps=2} {/cps}힘 좀 쓸것 같은 이미지가 \'강하다\'니……{cps=2} {/cps}좋은 드립이네"
            stephan_think"…………"
            stephan_think"……그건 됐고, 빨리 일에 착수 해야겠다.{cps=2} {/cps}PX4를 받고 싶으니까"
            menu:
                "밖에 대화를 엿듣는다.":
                    "나는 밖에서 렌스 씨와 미스터 하와이가 하는 대화를 엿듣기로 했다."
                    "……참고로 도청은 나쁜 짓 이니까 착한 어린이는 따라하지 말자"
                    stop music
                    scene black with eyeshut
                    "나는 조용히 눈을 감고, 귀를 문에다가 댔다."
                    "철문의 차가움이 내 귀에 닿으면서 조금 소름이 돋았다."
                    "…………"
                    lance"{size=25}……다고?{/size}"
                    extra"{size=25}네, 가능성이 아주 없진 않잖아요?{/size}"
                    lance"{size=25}뭐어……{cps=2} {/cps}나도 예상은 했지만 말이지{/size}"
                    extra"{size=25}또 잘난 척 하시긴{/size}"
                    lance"{size=25}긍정적인 마음가짐이라도 있어야 조금이라도 더 오랫동안 살 수 있을거 아니야?{/size}"
                    lance"{size=25}그리고 걱정 하지 마, 급한 일이 될 때를 대비해서 \'그걸\'준비 해놨으니까{/size}"
                    extra"{size=25}생각해보니까 그랬었군요?!{/size}"
                    lance"{size=25}그래, 고드윈이 생각보다 준비성 있어가지고 택배로 친절하게 보내 주더라고{/size}"
                    stephan_think"\'그것\'?"
                    stephan_think"도대체 뭐지?"
                    extra"{size=25}그러고 보니까 클라크 씨 최근에 데이트 하는데 돈을 좀 많이 쓰시는 거 같던데요?{/size}"
                    lance"{size=25}괜찮아―{cps=2} {/cps}일종의 선행투자 같은 거니까{/size}"
                    stephan_think"여기서 계속 듣고 있다간 시간이……!"
                    play music "bgm/smooth1.mp3"
                    scene bg office_inside at Zoom((1280,720),(136,327,698,393),(75,269,802,451),0.5) with eyeopen
                    $ renpy.pause(0.7)
                    scene bg office_inside at Zoom((1280,720),(75,269,802,451),(0,318,713,402),0.8)
                    play sound "se/footsteps_running.mp3"
                    "계속 둘의 대화를 엿듣고 있다간 사기의 증거를 확보하지 못 할 것 같아서 빨리 이동하기로 했다."
                
                "바로 서류를 찾아본다.":
                    "나는 렌스 씨가 밖에 있는 지금 이 순간의 1분 1초라도 소중하게 느껴져서, 바로 사기를 증명할만 한 무언가를 찾기로 했다."
                    scene bg office_inside at Zoom((1280,720),(462,269,802,451),(0,318,713,402),0.8) with dissolve
            
        "제 이름은 \'윌리 제임스\' 라고 합니다 (거짓)":
            show stephan at left
            stephan"제 이름은 \'윌리 제임스\' 라고 합니다"
            stephan"……멜 누나랑 아는 사이인데 혹시 모르시나요?"
            show lance at right
            lance"당연히 알지!"
            lance"멜의 남동생 이었나?"
            lance"서서 얘기하기도 그러니 일단 안으로 들어와"
            stop music
            scene black with moveleft
            play sound "se/footsteps_wood.mp3"
            $ renpy.pause(3)
            stop bgs
            scene bg office_inside with dissolve # 사무실 내부
            play music "bgm/smooth1.mp3"
            "나는 사무실 안으로 들어갔다."
            "실내장식은 어느 사무실과 다를 바 없이 평범하게 책상, 소파, 서류 등등이 있었다."
            "조금 다른 게 있다면, 내부가 많이 비어있는 듯한 느낌 정도?"
            "그리고 좀 이상하지만 알록달록한 하와이풍 옷을 입은 건장한 남성도 소파 뒤에 서 있었다."
            scene bg office_inside at Zoom((1280,720),(0,0,1280,720),(462,269,802,451),0.5) with dissolve # 사무실 내부
            "눈치를 보며 소파에 앉았고 내 맞은편엔 렌스가 앉았다."
            show lance talk at right
            show stephan at left
            lance"그래서 여기 온 이유가 뭐지?"
            show stephan shock at left
            stephan_think"이유라……"
            stephan_think"뭔가 신빙성이 있는 이유가 필요한데……"
            stephan_think"견학하러 왔다고 하면 되려나……{cps=2} {/cps}윌리라면 그럴싸할지도 모르겠군"
            show stephan smile at left
            stephan"무역 회사를 견학해보고 싶어서 왔어요!"
            lance"그래?"
            lance"네가 저번에 여기에 왔을 때 알려 줬던 것 같은데 말이지?"
            stop music
            show stephan shock at left
            stephan"네?"
            play music "bgm/sirius3.mp3"
            lance"넌 윌리가 아니잖아"
            lance"내가 기억하는 윌리는 머리카락이 빨간색이 아니었거든?"
            lance"넌 도대체 뭐하는 녀석이지?"
            lance"윌리가 불러서 온 거냐?"
            stephan_think"뭐지 이 상황?!"
            lance"설마 녀석이 다른 사람에 말 했을 줄이야……"
            stephan_think"윌리에 대해서 알고 있었다고?"
            stephan_think"그러고 보니 아까……"
            play sound "se/think.mp3"
            scene bg office_outside with flash # 사무실 문 앞
            show willy at right
            show stephan talk at left
            willy"저번에 왔을 때랑 변한 게 없네……"
            stephan"여기 와본 적이 있어?"
            willy"어,{cps=2} {/cps}렌스 씨 랑은 그리 오랫동안 대화를 나누진 못했지만 말이지"
            scene bg office_inside at Zoom((1280,720),(462,269,802,451),(462,269,802,451),0) with flash# 사무실 내부
            show stephan shock at left
            show lance talk at right
            stephan_think"윌리를 만난 적이 있었다면 당연히 생김새도 알고 있겠지……"
            stephan_think"젠장,{cps=2} {/cps}조금만 더 생각을 했더라면……"
            lance"그래서 넌 녀석에게 어디까지 들었지?"
            lance"이 회사에 대해서는 알고 있나?"
            stephan"…………"
            show lance at right
            lance"묵비권을 행사하시겠다?"
            lance"걱정 마{cps=2} {/cps}네가 여기에 와서 윌리의 이름을 댄 것만 가지고도 꽤 많은 걸 증명하거든"
            stephan_think"이제 어쩌지……"
            show lance talk at right
            "렌스는 뒤에 있던 건장한 남성들에게 눈빛을 주었다."
            play sound "se/footsteps_wood.mp3"
            $ renpy.pause(3)
            play sound "se/hit.ogg"
            $ renpy.vibrate(0.2)
            scene black
            "순간 뒤통수에 엄청난 충격이 느껴지더니……{cps=2} {/cps}내 의식이 흐려졌다."
            stop music
            scene bg office_inside with Dissolve(1.5)
            show lance shock at left
            lance"윌리……"
            lance"경찰이 안 되니까 이런 녀석을 데리고 오다니"
            $ extra_name = '건장한 남성'
            extra"얜 어쩔까요?"
            show lance talk at left
            lance"꽤 젊어 보이는 녀석인데……{cps=2} {/cps}나 대신에 데리고 가면 안 되나?"
            extra"음……{cps=2} {/cps}그건 좀 힘들지 않을까요?"
            show lance shock at left
            lance"왜?!"
            lance"내 장기보단 훨씬 비싸게 팔릴 텐데?"
            extra"하지만 \'고드윈(Godwin)\'씨가 사후처리가 힘든 사람은 데리고 오지 말라면서……"
            play music "bgm/sirius5.mp3"
            show lance at left
            lance"너나, 나나 둘 다 같은 처지잖아?"
            lance"솔직히 언제 우리 장기가 뜯기는지도 모르는 건데……"
            lance"저 녀석을 팔아 치우기만 한다면 우리 빚은 갚고도 남을걸?"
            extra"그럴지도……"
            lance"그리고 그 고드윈 씨의 상사, \'하데스(Hades)\'인가 하는 사람 보니까 발 넓던데?"
            lance"고작 학생 하나의 사후처리가 뭐가 힘들겠어?"
            extra"그럼 당장 물어보러 가볼게요"
            play sound "se/search_bag.mp3"
            $ renpy.pause(2)
            extra"여엉차!"
            extra"그럼 일단 얘 몸부터 구속 시키도록 하죠"
            show lance talk at left
            lance"그래,{cps=2} {/cps}저기 책상 옆에 끈이 하나 있었을 거야. 그걸로 묶어"
            show lance at left
            stop music
            lance"훗,{cps=2} {/cps}그래도 이걸로 멜을 이용할 필요는 없어졌군"
            jump game_over
    scene ev office_desk with dissolve
    show inspect_mode: # 탐색모드 시작
        alpha 1.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
    narrator_nvl"조사 모드에 진입 하셨습니다."
    narrator_nvl"조사를 하고 싶은 곳을 터치하면 이벤트를 진행 시킬 수 있습니다."
    nvl clear
    $ found_ev1 = False
    $ found_ev2 = False
    
label office_desk:
    if found_ev1 and found_ev2 == True:
        jump office_desk_finish
    call screen desk_imagemap #오피스 조사 장면
    $ result = _return
    if result == "cup":
        "빈 머그컵이 있다."
        jump office_desk
        
    if result == "computer":
        "컴퓨터가 있다."
        "모니터의 크기로 봐선 800x600 해상도의 SVGA 식 컴퓨터 인 듯 하다."
        "……무슨 원시인 인가?"
        stephan_think"하지만 텅텅 비어있는 인테리어에 초저가 모니터 까지……{cps=2} {/cps}돈이 어지간히도 없나보네"
        jump office_desk
    
    if result == "doc":
        hide inspect_mode
        "여러 가지 서류가 어질러져 있다.{cps=2} {/cps}종류는 빚 문서"
        "아무래도 내가 여기 오기 전 까지 읽고 있었는 듯 하다."
        show stephan talk
        play sound "se/search_bag.mp3"
        "나는 서류 뭉치 중에서 맨 윗쪽에 놓여있는 구깃구깃 한 서류를 짚어서 읽어봤다."
        show stephan think
        stephan_think"흠……"
        narrator_nvl"원금: 500만 달러"
        narrator_nvl"변제기일: 2015년 2월 16일"
        narrator_nvl"이자: 윌 1\%"
        narrator_nvl"채권자: \'라이언 마르쿠스 고드윈(Ryan Markus Godwin)\'"
        nvl clear
        "이 차용증은 2년 전 인 2012년에 작성 되었다."
        stephan_think"이걸로 왜 이 사무실의 인테리어가 텅텅 비어 있는 진 설명이 됐군.{cps=2} {/cps}돈을 갚기 위해 필요한 걸 제외하곤 전부 팔았겠지"
        show stephan shock
        "하지만 이 차용증에 몇 가지 이상한 게 있다."
        "첫 번째론, 바로 이자"
        "보통은 연 단위로 이자가 쌓일 텐데, 이건 월 단위다."
        "게다가 1\%밖에 없다."
        "뭔가 비약적으로 적은데……"
        "두 번째, 채권자의 이름"
        "채권자의 이름에 돈을 빌린 은행의 이름이 아닌 사람의 이름이 적혀있다."
        "즉, 이건 단순한 차용증이 아닌 사채다.{cps=2} {/cps}다만 평범한 사채와는 다르게 빌려주는 기간이 3년으로 꽤 길다."
        stephan_think"이자가 월 1\%에 3년 이라니……{cps=2} {/cps}채권자에겐 이익이 너무 적은데 말이야……"
        "나는 계속해서 이 차용증을 읽어 내렸는데……{cps=2} {/cps}더욱 이상한 걸 찾았다."
        "……물론 나 같은 고딩이 채무에 관해서 뭘 알겠는가"
        extend", 하지만 이건 내가 봐도 뭔가 이상했다.{cps=2} {/cps}사채 이기 때문에 당연 하다면 당연 할 수도 있겠지만……"
        stop music
        stephan_think"\'신체 담보\'……{cps=2} {/cps}라니……"
        play music "bgm/sirius5.mp3"
        "하지만 내가 이상하다고 생각 한 건 바로 이 계약서의 존재 그 자체다."
        "신체 담보는 불법 일 텐데……{cps=2} {/cps}도대체 어떻게?"
        "렌스 씨가 이걸 경찰들에게 보여주면 아무 문제없을 텐데……"
        stephan_think"혹시 그렇게 했지만, 실패해서……?"
        show stephan think
        "이건 그저 나의 망상 일 뿐 일수도 있겠지만……"
        "혹시 렌스 씨는 벌써 경찰에 가서 도움을 요청 해봤지만, 아무런 도움을 받지 못했던 게 아닐까?"
        "이렇게 생각하면 왜 렌스 씨가 사기를 꾸미려는 지는 설명이 된다."
        stephan_think"그런데 왜 이 회사는 여전히 남겨뒀던 걸 까?"
        extend" 사기를 치기 위해서?"
        stephan_think"하지만 왜 사기를 쳐서 돈을 벌려고 하는 거지?"
        stephan_think"다른 방법도 많을 텐데……"
        play sound "se/search_bag.mp3"
        "나는 증거물이 될 만한 차용증을 주머니에 넣고, 이번엔 다른 서류들을 살펴봤다."
        stephan_think"전부 다 대출이야……"
        "하지만 내가 방금 전 까지 보고 있었던 꾸깃꾸깃한 신체 담보 대출을 빼면 전부 갚았다고 되어있다."
        stephan_think"즉, 대출을 갚기 위해서 또 다른 대출을 했고……{cps=2} {/cps}그 굴레가 반복되어서 지금까지 왔다는 뜻이로 군"
        show stephan shock
        stephan_think"렌스 씨가 조금 불쌍하게 느껴지네……"
        hide stephan shock
        $ found_ev1 = True
        show inspect_mode: # 탐색모드 시작
            alpha 1.0
            linear 1.0 alpha 0.0
            linear 1.0 alpha 1.0
            repeat
        jump office_desk
        
    if result == "drawer":
        "서랍이 있다."
        menu:
            "열어본다.":
                hide inspect_mode
                play sound "se/door_open2.ogg"
                "나는 첫 번째 서랍을 열었다."
                "안엔 잘 정리된 폴더가 있었다."
                play sound "se/search_bag.mp3"
                "폴더를 A~Z까지 살펴보았다."
                "대부분 사업 계획서로 추정 되는 서류들 이었다."
                show stephan talk
                stephan_think"날짜를 보니까……{cps=2} {/cps}고작 몇 년 전에 작성했어"
                "아무래도 렌스 씨가 처음부터 페이퍼 컴퍼니를 가지고 있었던 건 아닌가보다."
                "한땐 다른 이름으로 실존 했던 회사 였는데……{cps=2} {/cps}망하면서 이렇게 된거겠지……"
                play sound "se/door_open2.ogg"
                "나는 첫 번째 서랍을 닫고 두 번째 서랍을 열어봤다."
                "안엔 아무것도 없이 딱 권총 한 자루가 있었다."
                show stephan shock
                stephan_think"어……"
                show effect1
                play sound "se/shock.ogg"
                stephan_think"{size=45}왜 이런 게?!{/size}" with lshake
                hide effect1
                "우리나라는 이웃나라, 미국과는 다르게 총기 소지가 불법이다."
                "물론 따로 자격증을 따면 구매 자체는 가능 하겠지만……{cps=2} {/cps}렌스 씨가 그런 걸 가지고 있을 리가 없겠지"
                stephan_think"근데 도대체 무슨 속셈으로 이런 위험한 물건을 가지고 있는거지?!"
                stephan_think"혹시 모르니까 총알을 빼서 보관하는 게 좋겠어"
                play sound "se/search_bag.mp3"
                "나는 총을 꺼내 들고는 안에 있는 탄약을 전부 비웠다."
                "꺼낸 탄약을 오른쪽 주머니에 넣은 뒤 총을 제자리에 넣고 서랍 문을 닫았다."
                play sound "se/door_open2.ogg"
                hide stephan shock
                $ found_ev2 = True
                show inspect_mode: # 탐색모드 시작
                    alpha 1.0
                    linear 1.0 alpha 0.0
                    linear 1.0 alpha 1.0
                    repeat
                jump office_desk
            "열지 않는다.":
                jump office_desk
    
label office_desk_finish:
    play music "bgm/smooth1.mp3"
    play sound "se/search_bag.mp3"
    scene bg office_inside at Zoom((1280,720),(0,318,713,402),(75,269,802,451),0.5) with dissolve
    show stephan think
    stephan_think"여기서 내가 찾을 수 있을만 한 건 거의 다 찾아 본거 같긴 한데……"
    extend" 결혼 사기를 증명하는데 차용증 정도면 충분하려나……?"
    show stephan yawn
    stephan_think"에라 모르겠다"
    play sound "se/footsteps_running.mp3"
    scene bg office_inside at Zoom((1280,720),(75,269,802,451),(462,269,802,451),0.5) with dissolve # 사무실 내부
    "나는 밖에 나간 렌스 씨가 들어올 것 같아서, 빨리 봤던걸 제자리에 두고, 소파에 앉았다."
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.4)
    scene bg office_inside at Zoom((1280,720),(462,269,802,451),(462,269,802,451),0) with moveright
    show stephan talk at left
    play sound "se/door_open.ogg"
    $ renpy.pause(1.0)
    play sound "se/footsteps_running.mp3"
    show lance with dissolve:
        xalign -1.0 yalign 1.0
        linear 1.5 xalign 1.0
    lance"이거, 생각보다 오래 기다리게 해서 미안"
    show stephan shock2 at left
    stephan"아,{cps=2} {/cps}아니에요!{cps=2} {/cps}전 괜찮아요!"
    "급하게 앉는 바람에 숨이 차버렸다.{cps=2} {/cps}그거 때문에 내가 이 사무실을 뒤진 게 들킬 것 같아서 가슴이 조마조마 했다."
    stephan_think"근데 아까 미스터 하와이 보고 사오라고 한 커피는 안 사왔네?"
    "아무래도 저쪽도 저쪽 사정으로 머릿속이 복잡해서 까먹었다고 생각하기로 하고, 따로 묻지 않았다."
    stephan"그럼 아까 하려고 했던 질문을 계속 하도록 하죠!"
    lance"그래"
    play sound "se/search_bag.mp3"
    show stephan talk at left
    "나는 주머니에서 휴대폰을 꺼내, 마치 미리 준비한 질문 목록을 읽고 있는 듯이 화면을 바라봤다."
    stephan"첫 번째 질문은……"
    show stephan at left
    extend" 이 회사를 설립한지 어느 정도 됐어요?"
    lance"작년 3월에 했으니까……{cps=2} {/cps}정확히 1년 반 됐네"
    show stephan think at left
    stephan"그렇군요……"
    show stephan at left
    stephan"다음 질문 입니다"
    show stephan talk at left
    stephan"회사를 차릴 땐 꽤 많은 돈이 필요 하다고 하던데……{cps=2} {/cps}렌스 씨는 그 걸 어떻게 구하셨어요?"
    show lance talk at right
    lance"내 방법이 너한테 도움이 되려나?"
    show stephan shock2 at left
    stephan"그,{cps=2} {/cps}그냥 참고로만 들을 거니까요!"
    lance"그게 참고가 될 진 모르겠지만……"
    show lance at right
    lance"난 예전에 류인 주식회사라는 대기업 에서 일을 한 적이 있었어"
    show stephan at left
    stephan"아,{cps=2} {/cps}그거라면 멜 누나한테서 들어본 적이 있어요"
    stephan"거기서 처음 만나셨다면서요?"
    lance"그래?"
    lance"흠,{cps=2} {/cps}그럼 길게 말 할 필요가 없겠군"
    lance"쉽게 말해서, 류인에서 근무하는 동안 모은 돈으로 사업을 했어"
    lance"보통 월급쟁이 회사원 이라면 이런 게 쉽진 않겠지만……{cps=2} {/cps}류인 그룹이 워낙 대기업이라서 불가능 한 것도 아니었지"
    lance"그 \'밸브(Belve)\'사를 만든 \'게이브 뉴웰(Gabe Newell)\'같이 말이야"
    lance"그런데 중요한 건 사업 자금의 확보가 아니라, 사업 아이템이야"
    extend". 자금은 확보 할 방법이 비교적 많거든"
    stephan"그럼 렌스 씨는 대출 한 번도 받지 않고 사업 자금을 모았어요?!"
    show lance shock at right
    lance"대출……?"
    lance"뭐……{cps=2} {/cps}특별히 할 필요는 없었지"
    lance"무역은 나라에서 지원을 해주니까 말이야……"
    show stephan think at left
    stop music
    "렌스 씨의 반응이 뭔가 이상했다."
    stephan_think"아까 본 대출증을 봤을 때 렌스 씨는 분명 대출을 받은 적이 있었어"
    "참고로 사업을 하면서 대출 받는 건 딱히 이상할게 없다.{cps=2} {/cps}하지만 왜 방금 전에 대출을 받지 않았다고 거짓말을 했을까?"
    show stephan talk at left
    stephan_think"……뭔가 숨기고 있어"
    "사기를 증명할 만한 증거물은 확보했기 때문에 이대로 대충 질문만 하고 그대로 밖으로 나갔도 됐겠지만……"
    "나의 호기심이 그 마음을 삼켜버렸다."
    play sound "se/search_bag.mp3"
    "나는 주머니에 넣었던 차용증을 꺼내들면서 입을 열었다."
    play music "bgm/sirius4.mp3"
    stephan"그렇다면 이 사채 받은 500만 달러는 어떻게 설명 하실 건가요?"
    show lance shock at right
    lance"…………"
    lance"뭐?"
    stephan"방금 전에 대출을 받지 않았다고 하셨는데……{cps=2} {/cps}그럼 이 차용증은 뭔가요?"
    lance"으……"
    lance"그,{cps=2} {/cps}그래,{cps=2} {/cps}방금 전엔 내가 한 말은 거짓말이었어"
    show lance talk at right
    lance"하지만 대출받은 게 어쨌다고?{cps=2} {/cps}사업을 하다보면 대출 같은 건 받아야 할 때도 있는 법이야"
    stephan"그럼 방금 전에 대출 사실을 숨긴 이유는 뭐죠?"
    show lance at right
    lance"그야 네가 나의 사랑, 멜 이랑 아는 사이라고 하니까 잘 보이려고 그랬지!"
    lance"아까 내가 너를 속인 건 정말 미안해"
    lance"나중에 네가 커서 사업을 할 땐 나처럼 대출 받아가면서 하진 않았으면 좋겠다는 의미도 있었는데……"
    show lance shock at right
    lance"그보다 너, 남이 잠시 자리를 비운 사이 함부로 건물을 뒤지는 건 나쁜 짓이야"
    "저 떨리는 눈동자에 가만히 있지를 못하는 손가락 까지……"
    "방금 전에 차용증을 숨기려고 했던 이유를 조금 알 것 같았다……{cps=2} {/cps}지금 렌스 씨는 엄청나게 긴장하고 있다."
    "자신은 그저 페이퍼 컴퍼니나 결혼 사기와 연관되어 있는 것 들은 전부 숨기려고 했지만……{cps=2} {/cps}너무 긴장하는 바람에 사업하는 사람한테 있어도 크게 이상할게 없는 차용증에 대한 사실 까지도 숨기려고 했던 거지"
    "하지만 렌스 씨를 너무 탓 할 순 없었다."
    "만약 렌스 씨가 대출을 받은 적이 있었다고 했으면 내가 그것에 대해서 질문 했을 확률이 있었으니까"
    "그리고 그렇게 되면 나중엔 들키겠지"
    show stephan smile2 at left
    stephan_think"훗,{cps=2} {/cps}이젠 내 손 안이야"
    show stephan smile at left
    stephan"죄송해요!{cps=2} {/cps}사업하는 게 어렸을 때 부터 꿈 이다보니까 너무 흥분 해버려서 저도 모르게 건물을 샅샅이 조사하게 되더라고요!"
    show lance at right
    lance"알았으면 그거 이제 돌려줄 수 있겠니……?"
    show stephan talk at left
    play sound "se/search_bag.mp3"
    stephan"여기……"
    extend" 음?{cps=2} {/cps}근데 이 차용증이 좀 특이하네요?"
    show lance shock at right
    lance"뭐,{cps=2} {/cps}뭐가?"
    stephan"보통 차용증은 연 단위로 이자가 붙지 않나요?{cps=2} {/cps}근데 이건 월 단위로 이자가 붙어요"
    stephan"거기다 채권자 이름은 보통 대출을 받은 은행의 이름 일 텐데,{cps=2} {/cps}여긴 라이언 마르쿠스 고드윈이라는 사람의 이름이 적혀있네요?"
    lance"…………"
    show stephan smile2 at left
    stephan"혹시 이거……{cps=2} {/cps}사채 아닌가요?"
    lance"그게 왜?!"
    lance"은행과는 다르게 \'신용등급(信用等級, credit grade)\'이 필요 없으니까……!"
    show lance shock2 at right
    stephan"\'신용도\'가 떨어지셨어요?"
    lance"…………"
    "신용등급이란, 한 사람의 신용 정보를 바탕으로 매긴 그 사람에 대한 신용도를 뜻한다."
    "대출 받을 때 뿐만 아니라, 사회생활을 하는데 정말 중요한 수치다."
    "여차 할 때 솟아 날 구멍이 만들어지기 때문이라고 해야 할까?"
    "뭐가 어쨌건, 렌스 씨 같이 사업을 하는 사람들에겐 신용등급이 투자자 확보 하는데도 쓰이기 때문에 더더욱 중요하다."
    "하지만 방금 본인 입으로 신용도가 낮거나 없다고 말을 함으로써, 클라크 무역이 페이퍼 컴퍼니임을 자백한 거나 마찬가지다."
    stephan"무역 회사는 국가에서 지원을 해주기 때문에 굳이 대출을 받을 필요가 없다고 하셨으면서, 사채까지 받을 필요가 있었나요?"
    show lance shock at right
    show stephan talk at left
    stephan"게다가 이거 자세히 보니까 본인의 신체 까지 담보로 잡혀 있는데요?"
    stephan"500만 달러가 그리 적은 금액은 아닌데……{cps=2} {/cps}빨리 갚으시고 싶으시겠어요……?"
    show stephan smile2 at left
    stephan"멜 누나를 이용해서라도 말이죠"
    lance"내가 지금 결혼 사기라도 치고 있다고 말하고 싶은 거냐?!"
    stephan"전 아직 \'결혼 사기\'라는 말은 안했는데요?"
    show lance mad at right
    lance"으……"
    "렌스 씨의 표정이 조금 무서웠다……"
    show stephan shock at left
    stephan"아,{cps=2} {/cps}아직 제 질문은 끝나지 않았어요!"
    show stephan talk at left
    stephan"클라크 무역은 어떤 회사죠?"
    lance"이름대로 무역 회사야"
    stephan"건물을 봐도 그렇고……{cps=2} {/cps}최근 들어서 일거리가 전혀 없었겠네요?"
    lance"불경기니까"
    stephan"그럼 현재 이 회사는 완전히 \'페이퍼 컴퍼니\' 같은 상태겠어요?"
    show lance shock at right
    lance"어이,{cps=2} {/cps}날 놀리려고 온 거냐?"
    stephan"아니요,{cps=2} {/cps}그냥 궁금해서요"
    stephan"렌스 씨는 이 회사를 작년에 설립 했다고 했고"
    extend", 이 차용증은 2년 전인 2012년에 썼죠"
    stephan"왜 그랬죠?{cps=2} {/cps}500만 달러의 신체를 담보로 잡힌 사채를 안고 있으면서도 왜 굳이 돈을 들여가며 이 회사를 만든 거죠?"
    stephan"이런 상황에서 회사를 가지고 있으면 오히려 자신의 발목을 붙잡고 있다는 걸 아실텐데?"
    stephan"국가에서 주는 무역 특혜 때문에?{cps=2} {/cps}하지만 그건 바이어와의 계약이 이루어 졌을때만 적용되기 때문에 빚 갚는 덴 전혀 도움이 안될 텐데?"
    show stephan smile2 at left
    stephan"……뭔가 다른 목적을 가지고 계시는 거죠?"
    stephan"이 회사로 어떻게든 빚을 갚으려고……{cps=2} {/cps}물론 조금 다른 방법으로"
    stephan"방금 그 쪽 입으로 말씀하신 \'결혼 사기\'같이"
    lance"도대체 내가 이 회사를 어떻게 써야 돈을 벌 수 있겠냐?"
    show stephan talk at left
    stephan"여자를 꼬셔서 돈을 버는 것도 방법 중 하나죠"
    stephan"무역 회사를 운영하고 있는 사업가라고 한다면 여자들의 집중을 받는 건 쉽고……"
    lance"내가 여자를 꼬신다고 해서 빚이 갚아지는 건 아니잖아?!"
    lance"생각해봐, 내가 사업가라고 하면 확실히 여자들은 돈이 많다고 생각해서 나에게 호감을 보일 수도 있겠지만."
    extend" 그런 여자들은 대부분 돈이 없기 때문에 그런 반응을 보이는 거잖아?"
    lance"내 빚을 갚는 덴 전혀 도움이 안 된다고?"
    stephan"확실히 이 방법으론 렌스 씨의 말대로 부자 여자들이 붙기는 힘들 겁니다"
    show stephan smile2 at left
    stephan"하지만 \'사업을 위해서 돈 좀 빌려줘\'같은 말을 한다면……"
    stephan"굳이 여자가 부자가 아니어도 돈을 벌 순 있겠죠"
    stephan"심지어 둘 사이에 벌어지는 거례에선 계약서조차도 쓸 필요가 없어요"
    stephan"구두 계약은 법적인 증거물이 되지 못하니까 그대로 돈을 들고튀어도 걸릴 확률은 제로"
    show lance mad at right
    show effect1
    play sound "se/shock.ogg"
    lance"{size=40}무,{cps=2} {/cps}무슨 소리야?!{/size}" with lshake
    lance"너 여자에 대해서 꽤 아는 듯이 말을 하는데……"
    lance"연애 경험이 있긴 한거냐?!"
    extend" 네가 여자의 심리에 대해서 어떻게 알아?!"
    stop music
    hide effect1
    show stephan mad at left
    stephan_think"(빠직)"
    stephan_think"그게 지금 하고 있는 말이랑 무슨 상관이야"
    stephan_think"그런 건 굳이 여자가 아니라도 사람이라면 누구나 생각하는 건데……"
    stephan_think"꼭 연애 경험이 있어야만 하는 건가……"
    stephan_think"그리고 이건 내가 인기가 없는 게 아니라 아직 순수하다는 증거라고……!"
    "나는 렌스 씨가 생각없이 던진 말에 혼자 흥분해 있었다."
    show lance shock at right
    lance"네가 말 한 방법으론 실패 할 확률이 있어"
    lance"반면 돈이 많은 여성을 상대로 접근을 하면 리스크가 매우 적지"
    stephan"{size=25}그렇긴 하겠지만……{/size}"
    lance"하지만 지금 내가 결혼 하려는 상대 인 멜은 대기업에 근무를 하곤 있겠지만, 절대 부자는 아니야!"
    lance"그런 사람을 상대로 사기를 쳐봤자 나한테 아무런 이득이 없다는 건 잘 알고 있을텐데?"
    play music "bgm/sad5.mp3"
    stephan"{size=15}멜 누나의 아버지……{/size}"
    show effect1
    play sound "se/shock.ogg"
    show stephan sirius
    show lance sad at right
    stephan"{size=45}멜 누나의 아버지가 편찮으시다는 걸이용 할 생각이셨잖아요!{/size}" with lshake
    hide effect1
    stephan"누나의 아버지는 병이 아닌, 사고로 인해서 병원에 입원했기 때문에 보험 적용 대상이죠……"
    stephan"거기다 멜 누나랑 같이 결혼을 하게 된다면 그 돈을 전부 다 가질 수 있게 될 테고……"
    stephan"하지만 제가 당신을 가장 용서 할 수 없는 건……{cps=2} {/cps}멜 누나는 렌스 씨를 진심으로 사랑했다는 것……"
    "나는 너무나도 화가 나서 제대로 말도 못이었다."
    lance"그 소식 이라면 들었어……"
    lance"하지만……{cps=2} {/cps}내가 만약 정말로 멜의 아버지를 이용하려고 했다면……"
    lance"너무 불확정 요소가 많잖아?"
    lance"멜의 아버지는 앞으로 길면 약 1년 정도 남았다고 들었어"
    lance"그리고 내가 받은 사채도 앞으로 1년도 채 남지 않았지……"
    show lance talk at right
    lance"내가 정말 멜의 아버지를 이용할 작정 이었다면 너무 아슬아슬하다고 생각하지 않아?"
    show stephan shock at left
    stephan"생각해보니까……"
    "렌스 씨의 말이 맞다."
    "멜 누나의 아버지를 이용 한다는 건 너무 아슬아슬해……"
    "거기다 이 사채는 자기 목숨이 담보로 잡혀 있기 때문에 그런 리스크에 걸리가 없다."
    "그럼 뭐 때문에……?"
    "설마 정말로 멜 누나를 좋아해서?!"
    lance"네가 생각했던 대로, 난 신체가 담보로 잡힌 위험한 사채를 받았어, 그리고 이 회사는 페이퍼 컴퍼니가 맞아"
    show lance at right
    lance"하지만 그건 절대 멜을 이용하기 위해서가 아니야!"
    lance"난 정말로 멜을 사랑한다고!{cps=2} {/cps}나중에 결혼해서 같이 이 빚을 갚아나가고 싶었을 뿐이야!"
    show stephan sad at left
    stephan_think"내가 너무 렌스 씨가 사기꾼 이라는 이미지에 집착 하고 있어서 진실을 못보고 있었던 걸까?"
    stephan_think"그냥 윌리가 사기꾼 이라고 했으니까 난 그런가보다 하며, 내 생각을 차단하고……"
    show lance talk:
        linear 3.0 xalign -1.5
    play sound "se/footsteps_concrete.mp3"
    stephan_think"렌스 씨는 그저 멜 누나를 사랑했고……{cps=2} {/cps}같이 결혼을 해서 서로의 부족한 점을 채워주기 위해……"
    "근데 그렇다면 한 가지 이상한 게 있었다."
    "만약 정말 렌스 씨가 멜 누나를 사랑했다면……{cps=2} {/cps}왜 결혼을 하는 걸까?"
    "이런 위험한 사채를 지고 있다면 오히려 결혼을 하지 않는 게 더 상대방을 위한 게……"
    stop music
    show stephan shock at left
    "…………"
    "그때 난 모든 걸 이해했다."
    "렌스 씨가 결혼을 하려는 이유……"
    stephan_think"렌스 씨는 사채를 갚기 위해서 필요한 돈을 마련하려고 결혼을 하는 게 아니야!"
    stephan_think"무엇보다 사랑 하기 때문에 결혼을 하는것도 아니라……"
    show stephan sirius at left
    play music "bgm/sirius3.mp3"
    extend" 이 빚을 떠넘기려는 거야……"
    "다른 나라는 모르겠지만, 우리나라에선 채무자가 실종·사망 될 경우 그 빚을 가장 가까운 가족 구성원이 갚도록 되어있다."
    "참고로 법적으로 가장 가까운 가족 구성원은 배우자이다."
    "앞으로 이 빚은 얼마 안 남았고……{cps=2} {/cps}게다가 —비록 월 1\% 라고 해도—이자가 어느정도 쌓여서 빠른 시일에 갚는 건 불가능할 것 같았다."
    "왜 멜 누나랑 결혼을 하려고 했는지 이해됐다."
    "애초에 이 빚을 갚을 생각 따윈 없었어"
    stephan_think"렌스……{cps=2} {/cps}이 개자식……"
    show stephan mad:
        linear 0.7 xalign 0.5
    play sound "se/search_bag.mp3"
    "나는 자리에서 일어났다."
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    show lance:
        zoom 1.5 yalign -0.3 xalign 0.3
    lance"벌써 가려고?"
    scene bg office_inside at Zoom((1280,720),(462,269,802,451),(462,269,802,451),0.0)
    show stephan mad
    stephan"렌스……{cps=2} {/cps}그런 사람으론 안 봤는데……"
    extend" 설마 멜 누나한테 빚을 떠넘기려고 했을 줄이야……"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    show lance talk:
        zoom 1.5 yalign -0.2 xalign 0.3
    lance"혹시 방금 한 말만 가지고 추리 한 거야?"
    show lance shock
    lance"그,{cps=2} {/cps}그래도……"
    show lance gun
    show effect1
    play sound "se/shock.ogg"
    lance"{size=45}이,{cps=2} {/cps}이미 늦었어!{/size}" with lshake
    hide effect1
    "렌스는 서랍에 있던 총을 꺼냈다."
    lance"고드윈 그 자식 때문에 내가……"
    scene bg office_inside at Zoom((1280,720),(462,269,802,451),(462,269,802,451),0.0)
    show stephan mad
    stephan"정말 이렇게까지 할 필요가 있는 거야?!"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    show lance gun:
        zoom 1.5 yalign -0.2 xalign 0.3
    lance"나도 이렇게까지 할 생각은 없었어!"
    lance"하지만……{cps=2} {/cps}이렇게라도 안하면 내가 죽는 걸 어떻하냐고!"
    stephan"그런 문제라면 경찰에 가서……"
    lance"해봤어……"
    lance"근데 전부 소용 없었어……{cps=2} {/cps}녀석의 상사는……"
    stop music
    lance"법과 경찰을 넘는다고……!"
    scene bg office_inside at Zoom((1280,720),(462,269,802,451),(462,269,802,451),0.0)
    show stephan shock
    stephan_think"법과 경찰을 넘는다고?"
    play music "bgs/space.mp3"
    "그런 사람이 실제로 있다고?"
    "마치 음모론과도 같은 얘기였다."
    "하지만 방금 한 말이 사실이라면 렌스는 피해자 중 한명이다."
    stephan_think"확실히 사채의 형태가 많이 이상하다고 생각 했어……"
    "그 사채의 채무자의 상사가 그렇게나 큰 인물이라면……"
    "혹시 지금 내가 여기에 있는 것 만으로도 큰 사건에 휘말린게 아닐까?"
    stephan_think"아, 아닐거야"
    stephan_think"난 아무런 잘못도 하지 않았으니까"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    play music "bgm/sad2.mp3"
    show lance gun:
        zoom 1.5 yalign -0.2 xalign 0.3
    "그때 렌스는 푸념 하듯이 나에게 말 했다."
    lance"난 그저 어렸을 때부터 가졌던 꿈을 이루고 싶었을 뿐인데……"
    lance"그런데……{cps=2} {/cps}막상 그 꿈에 다가가자 내 인생을 차례대로 망하기 시작하고!"
    lance"사업 자금을 위해서 대출을 받고……{cps=2} {/cps}대출을 갚기 위해서 친구들에게 돈을 빌리고……"
    show effect1
    play sound "se/shock.ogg"
    lance"{size=45}그 과정에서 내가 얼마나 많은 사람들과 인연이 끊기고,{cps=2} {/cps}얼마나 많은 사람들에게 배신당했는지 알아?!{/size}" with lshake
    hide effect1
    lance"눈을 떠보니까 어느새 난 이렇게 위험한 사채 까지 하게 됐고……"
    lance"내가 이 걸 갚을 수 있을 리가 없잖아……{cps=2} {/cps}안 그래?"
    lance"그런데 말이야……{cps=2} {/cps}모든 걸 포기했던 어느 날, 커피숍에서 멜을 만났어"
    lance"한때 나랑 친했던 후배,{cps=2} {/cps}아직도 날 사랑하는 마음,{cps=2} {/cps}시간이 얼마 남지 않은 아버지……"
    lance"나한테 있어서 정말 완벽한 여자였어!"
    show effect1
    play sound "se/shock.ogg"
    lance"{size=45}그때 내가 멜을 만나게 된 건 단순한 우연 이 아니라 \'운명\'이야!{/size}" with lshake
    scene bg office_inside at Zoom((1280,720),(462,269,802,451),(462,269,802,451),0.0)
    show stephan mad
    "처음엔 렌스도 피해자 일거라 생각 했다."
    "하지만……"
    stephan"분명 멜 누나도……{cps=2} {/cps}너 따위와의 만남이 운명 이라고 생각 하고 있을 텐데……"
    stephan"운명 이라는 말을 더럽히지 마……"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    show lance gun:
        zoom 1.5 yalign -0.2 xalign 0.3
    lance"네가 어떻게 생각하든 상관없어,{cps=2} {/cps}지금 방아쇠를 쥐고 있는 건 나니까"
    play sound "se/footsteps_concrete.mp3"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,216,896,504),1.0)
    show stephan mad with dissolve:
        xalign 1.3 yalign 1.0
        linear 0.7 xalign 0.6
    show lance gun at left
    show effect1
    play sound "se/shock.ogg"
    lance"어이!{cps=2} {/cps}방금 내가 한 말 못 들었어?!"
    lance"죽기 싫으면 가만히 있으라고!"
    hide effect1
    stop music
    stephan"그럼 왜 나를 쏘지 않는 거지?"
    lance"어?"
    stephan"방아쇠를 쥐고 있는 건 너잖아?"
    stephan"내가 밖에 나가서 다른 사람한테 말하기 전에 빨리 날 죽이는 게 좋을 텐데 말이야?"
    stephan"왜 방아쇠를 쥐고 있는 네 손가락이 딱딱하게 굳어있는 거지?"
    lance"…………"
    stephan"그 이유는 단순해……"
    play music "bgm/sirius6.mp3"
    stephan"네가 각오가 안 돼 있기 때문이야"
    lance"각오……?"
    stephan"네 스스로가 논 한 \'운명\'이라는 걸 받아들일 각오가 안 돼 있으니까. 그런 식으로 자기가 진 빚을 남에게 넘기려는 거지"
    stephan"넌 삶의 각오도 못 한 겁쟁이 일 뿐이야"
    lance"입만 살아가지고……"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    show lance gun:
        zoom 1.4 yalign -0.2 xalign 0.5
    show effect1
    play sound "se/shock.ogg"
    lance"{size=45}지금 당장 네놈의 운명을 보여주마!{/size}" with lshake
    hide effect1
    "렌스는 각오를 다지며, 방아쇠를 힘껏 당겼다."
    $ renpy.pause(0.5)
    play sound "se/bullet_none.mp3"
    $ renpy.pause(1)
    lance"어?"
    play sound "se/bullet_none.mp3"
    $ renpy.pause(0.3)
    play sound "se/bullet_none.mp3"
    $ renpy.pause(0.2)
    play sound "se/bullet_none.mp3"
    $ renpy.pause(0.3)
    "하지만 총알은 나오지 않았다."
    show effect1
    play sound "se/shock.ogg"
    lance"{size=40}젠장 뭐야!!{/size}" with lshake
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(354,341,602,339),0.0)
    show stephan smile2:
        zoom 1.4 yalign -0.2 xalign 0.5
    "나는 주머니에 넣어 뒀던 총알 바닥에 떨어뜨리면서 입을 열었다."
    play sound "se/bullet_drop.mp3"
    stephan"이것이 바로 나의 \'운명\'인거지"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0)
    show effect1
    play sound "se/shock.ogg"
    show lance mad:
        zoom 1.4 yalign -0.2 xalign 0.5
    lance"{size=45}이 새끼가!!{/size}" with lshake
    play sound "se/swing.mp3"
    "렌스는 비명을 지르며 총알이 없는 권총을 나에게 던졌다."
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(354,341,602,339),0.0)
    show stephan shock:
        linear 0.5 zoom 3.4
    $ renpy.pause(0.5)
    play sound "se/hit.ogg"
    $ renpy.vibrate(0.3)
    scene black
    stop music
    "총의 개머리판이 내 눈 위를 쎄게 강타했다."
    "뇌가 지끈지끈 거리는고……{cps=2} {/cps}귀가 멍멍하고……{cps=2} {/cps}느껴지는 거 라곤 고통 뿐"
    $ renpy.vibrate(0.3)
    stephan"윽……!"
    "머리에서 부터 흘러나오는 차가운 액체……{cps=2} {/cps}피가 나오고 있었다……"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(354,341,602,339),0.0) with eyeopen
    "잠시 후 서서히 나의 시야가 되돌아오고, 아팠던 머리도 조금은 참을 만 해졌다."
    show stephan hurt with dissolve:
        zoom 1.7 yalign -0.2 xalign 0.5
    play music "bgm/sirius5.mp3"
    stephan"으윽……"
    scene bg office_inside at Zoom((1280,720),(354,341,602,339),(0,179,961,541),0.5) with dissolve
    show stephan hurt at right
    show lance shock2 at left with dissolve
    stephan"멍청하긴……"
    stephan"그 총으로 날 죽이게 되면……{cps=2} {/cps}주변에서 총소리를 듣고, 수상하다고 생각해서 경찰에 신고 할 거 아니야?"
    stephan"그렇게 되면 네가 범인 이라는 게 쉽게 알려질 텐데……"
    lance"으……"
    hide lance shock2
    hide stephan hurt
    play sound "se/door_knock.mp3"
    "그때 정적을 깨며 누군가 문을 두드렸다."
    show lance
    lance"로날드!"
    "렌스는 희망 찬 목소리로 로날드 라는 이름을 불렀다."
    "……잠깐"
    "생각해보니까 미스터 하와이가 있었다는 걸 깜빡했다!"
    stephan_think"여기서 그 힘 쎄 보이는 아저씨가 와버리면 난 진짜 죽을지도 모르는데……!"
    play sound "se/door_open.ogg"
    "렌스는 빨리 대문을 열어줬다."
    stop music
    "하지만……"
    $ extra_name = '경찰'
    extra"여기 미성년자 폭행 사건이 있다고 접수 받았는데 혹시 안에서 조사를 좀……"
    play music "bgm/sirius2.mp3"
    show lance mad
    extra"잠깐,{cps=2} {/cps}저거 총이잖아!?"
    "경찰관이 용케 이곳을 알고 찾아왔다."
    "렌스의 미소는 절망으로 바뀌더니……"
    play sound "se/fall.ogg"
    show lance mad:
        linear 0.5 yalign 2.8
    extend" 그대로 허탈한 듯이 자리에 주저 앉아버렸다."
    scene black
    play sound "se/case_start.mp3"
    show case_close
    $ renpy.pause(5)
    scene bg office_inside with dissolve
    "경찰관은 렌스의 손에 수갑을 채워 현행범으로 긴급 체포했다."
    "체포 사유는 \'폭행 죄 및 불법 무기 소지 죄\' 라고 한다."
    stop music
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(3)
    "모든 사건이 정리되자 누군가가 이쪽으로 오는 소리가 들렸다."
    play music "bgm/smooth1.mp3"
    show willy
    willy"어이!"
    willy"너 괜찮아?"
    "걸어 들어온 건 윌리였다."
    stephan_think"잠깐,{cps=2} {/cps}왜 쟤가?"
    play sound "se/think.mp3"
    scene bg outside_road with flash
    show willy talk
    willy"……너 최근에 경제학에 대해서 공부하고 있었지?"
    play sound "se/think.mp3"
    scene bg office_outside with flash
    show willy shock
    willy"윽!"
    willy"갑자기 큰 게 마렵네;;"
    scene bg office_inside with flash
    show willy at right
    show stephan hurt at left
    stephan_think"그런 거였군……"
    "즉, 난 처음부터 윌리의 손바닥 위에서 놀아나고 있었던 거다."
    stephan_think"날 미끼로 쓰다니"
    stephan"너 변비 걸렸냐?"
    stephan"뭐 이리 오래 걸렸어……"
    willy"헤헤"
    willy"그래도 나 덕분에 네가 더 심한 꼴을 당하지 않았잖아"
    stephan"하아……{cps=2} {/cps}그래도 날 미끼로 쓰는 건 좀 너무한 거 같은데 말이지……"
    show willy talk at right
    willy"설마 지금까지 모르고 있었어?"
    stephan"내가 그걸 어떻게 알겠냐!{cps=2} {/cps}네가 그냥 사기를 증명할 만한 증거물만 가지고 오라고 시켜놓고선……!"
    willy"아니,{cps=2} {/cps}애초에 사기를 증명 할 수 있는 증거물 같은 건 없잖아"
    stephan"어……?"
    willy"사기는 살인과 다르게, 사전에 미리 예방해서 범인을 체포하는 게 불가능해"
    willy"살인은 발생 후 되돌리는 게 불가능하지만, 사기는 합의를 통해서 보상을 받을 수가 있거든"
    willy"하지만 렌스 씨 같은 경우 상대방의 돈을 뜯는 게 아니라, 얼마 안남은 빚을 떠넘기는 거다 보니까……"
    willy"누나가 당하고 나서는 좀 늦는다고 해야겠지?"
    stephan"그래서 날 이용해 사기 이외에 다른 방법으로 렌스를 체포하기로 했다……?"
    show willy smile at right
    willy"바로 그거야!"
    willy"넌 체력이 약하니까!"
    willy"……가 아니라 똑똑 하니까 금방 녀석을 궁지에 몰아 넣을 수 있을 거라 생각 했어!"
    stephan"이 미친놈!{cps=2} {/cps}상대방은 총을 들고 있었다고!"
    stephan"그런 사람을 상대로 날 미끼로 사용하다니!"
    show willy
    willy"그 총 말이야……{cps=2} {/cps}내가 택배로 준거야"
    stephan"어?!"
    willy"물론 렌스 본인은─그게 나였는지 몰랐겠지만……"
    willy"참고로 그 총은 진짜이긴 하지만, 고장난거라 쏠 순 없어"
    stephan"…………"
    "황당했다."
    "뭔가 업청나게 황당 하다는 생각이 들었다."
    show willy talk at right
    willy"그래도 긍정적으로 생각해"
    willy"넌 사람 한 명을 살린거나 마찬가지라고"
    willy"……어쩌면 두 명 일 수도 있겠지만"
    willy"그리고 나중에 렌스 씨랑 합의 볼때 돈을 많이 요구 하면 PX4 몇 십개는 살 수 있을 걸?"
    stephan"내가 무슨 보험 사기를 치는 것도 아니고……{cps=2} {/cps}그리고 엄청 귀찮을 거 같아……"
    stephan"그냥 PX4나 받고 말란다……"
    willy"일단 피 부터 닦아{cps=2} {/cps}꼴이 그게 뭐냐"
    stephan"그래……"
    play sound "se/search_bag.mp3"
    show stephan talk with dissolve
    "나는 소매로 이마에서 흐른 피를 아무렇게나 닦았다."
    show willy shock at right
    willy"많이 아프겠네"
    show stephan shock
    stephan"알면 네가 대신에 가지 그랬어"
    willy"내가 갔으면 원하는 대답을 들을 수가 없었을 거 같아서"
    show stephan talk
    stephan"무슨 대답을 원했는데?"
    show willy smile
    willy"비밀"
    willy"그래도 렌스 씨가 내가 원했던대로 말 해줬으니까 나한텐 이득이야"
    stephan"혹시 안에서 무슨 일이 생겼는지 듣고 있었어?"
    show willy
    willy"당연히 듣고 있었지, 그렇지 않고서야 내가 어떻게 타이밍 맞춰서 경찰에 신고 했겠냐?"
    show stephan shock
    stephan"…………"
    show willy smile at right
    willy"너무 걱정하진 마!"
    willy"PX4는 제대로 줄 거니까"
    show willy talk
    willy"그 전에……"
    play sound "se/footsteps_concrete.mp3"
    scene ev office_desk with moveleft
    show willy talk:
        xalign 2.0 yalign 1.0
        linear 1.0 xalign 0.6
    $ renpy.pause(1.0)
    willy"…………"
    play sound "se/camera.mp3"
    "그때 윌리는 조용히, 책상위에 있는 대출증의 사진을 찍었다."
    play sound "se/footsteps_concrete.mp3"
    scene bg office_inside with moveright
    show willy:
        xalign -1 yalign 1.0
        linear 1.0 xalign 0.2
    show stephan talk:
        xalign 0.0 yalign 1.0
    $ renpy.pause(0.7)
    show stephan talk:
        linear 0.6 xalign 0.7
    stephan"사진은 왜?"
    willy"아, 잠깐 필요해서"
    willy"네가 해줬으면 하는 일은 이제 끝났으니까, 신경쓰지 않아도 돼"
    show stephan shock
    stephan_think"참 영문모를 녀석이야……"
    play sound "se/search_bag.mp3"
    "그때 옆에서 렌스를 연행하던 경찰관이 우리들에게 말 했다."
    extra"거기 두 분도 같이 서까지 와주세요"
    stephan"저, 저희도 가는건가요?!"
    show willy talk
    willy"당연히 가야지,{cps=2} {/cps}넌 피해자고, 내가 그걸 신고 했으니까"
    stephan"으흠……{cps=2} {/cps}그렇기도 하지만……"
    stephan_think"이렇게 되면 난 언제부터 PX4를 받을 수 있는거지?!"
    play sound "se/move.mp3"
    stop music
    scene black with moveright
    "우리는 이렇게 경찰서 까지 같다."
    "근데 곰곰히 생각해보니까 나랑 윌리가 한 짓이 보험 사기랑 뭔가 비슷했다."
    "서로 짜고 쳐서 일부러 얻어 맞은 뒤, 가해자랑 합의를 하고……"
    "그래도 우리는 렌스랑 합의를 보지 않는 걸로 어떻게든 위기를 아주 잘 모면했습니다!"
    play bgs "bgs/street.mp3"
    scene black with moveright
    centered"윌리의 집 앞"
    scene bg willy_house at Zoom((1280,720),(0,0,1280,720),(159,318,677,381),0.6) with moveright
    show willy at right
    show stephan talk at left
    willy"여기서 잠시 기다리고 있어봐. 금방 가지고 올 테니까"
    stephan"그래……"
    hide stephan talk
    hide willy
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(3)
    play sound "se/door_open.ogg"
    "윌리는 집으로 들어갔다."
    show stephan shock
    stephan_think"그나저나 윌리 녀석……"
    stephan_think"내가 명함을 얻으려고 한 거랑 차용증을 얻으려고 한 것도 전부……{cps=2} {/cps}렌스한테 얻어맞기 위한 거였다니"
    "하지만 그것보다 더 신경 쓰였던 건……"
    stop bgs
    play sound "se/think.mp3"
    stop bgs
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0) with flash
    show lance gun:
        zoom 1.5 yalign -0.2 xalign 0.3
    lance"근데 전부 소용 없었어……{cps=2} {/cps}녀석의 상사는……"
    lance"법과 경찰을 넘는다고……!"
    scene bg willy_house at Zoom((1280,720),(0,0,1280,720),(159,318,677,381),0.0) with flash
    play bgs "bgs/street.mp3"
    show stephan shock
    "뭐였을까……"
    "뭔진 모르겠지만, 지금 아주 큰 일이 벌어지고 있다는 느낌이 들었다."
    "아무런 근거 없는 나의 감 뿐이지만……"
    stephan_think"제발 뭔가 큰 일에 말려들지 않았으면 좋겠다"
    play music "bgm/smooth1.mp3"
    show stephan smile at left
    play sound "se/door_open.ogg"
    show willy at right
    willy"오래 기다렸지?"
    willy"자!"
    play sound "se/search_bag.mp3"
    "나는 윌리에게서 PX4가 들어있는 쇼핑백을 건네받았다."
    stephan_think"에라 몰라!{cps=2} {/cps}드디어 나한테도 게임 콘솔이 생겼으니까 다 좋아!"
    show willy talk
    willy"……그리고 미안"
    willy"왠지 널 속인거 같아서……"
    willy"그 사죄의 뜻으로 안에 게임도 두둑이 넣어줬으니까……"
    stephan"올?!"
    stephan"그래 그래, 너의 성의는 잘 봤어"
    stephan"용서 하도록 하지"
    show willy shock at right
    willy"정말 그걸로 되는거냐;;"
    stephan"당연하지!"
    extend" 게임은 진리니까!"
    show willy
    willy"…………"
    show willy shock
    willy"아차, 너 PX4의 주인이 나오기 전에 빨리 가는 게 좋을 거야"
    show stephan shock at left
    stephan"왜?{cps=2} {/cps}이거 네꺼 아니야?"
    willy"어,{cps=2} {/cps}사실 그거 내 룸메이트 꺼 거든"
    willy"그보다 빨리 가보는 게 좋을 거라니까!"
    show stephan smile at left
    stephan"예~{cps=2} {/cps}알겠슴다"
    show willy smile2 at right
    willy"사건 해결했다고 그렇게 기뻐하다니,{cps=2} {/cps}너도 참 사악한 녀석이야"
    stephan"이거 네가 주겠다고 한 거잖아!{cps=2} {/cps}그러니 당연히 모든 책임은 네가 져야지!"
    willy"그거 말고……{cps=2} {/cps}렌스 씨 말이야"
    show stephan talk at left
    stephan"어?"
    extend" 무슨 뜻이야?"
    show willy smile at right
    willy"아무것도 아니야. 그냥 잊어줘"
    $ extra_name = '룸메이트'
    extra"윌리……{cps=2} {/cps}지금 밖에서 뭐하냐?"
    show willy shock at right
    willy"갈게"
    play sound "se/footsteps_concrete.mp3"
    show willy shock:
        linear 3.0 xalign 2.0
    $ renpy.pause(3.0)
    play sound "se/door_open.ogg"
    scene black with Dissolve(1.0)
    stephan_think"……근데 윌리 그 자식,{cps=2} {/cps}결국 자기는 아무런 손해도 없이 이 사건을 전부 해결 했잖아?!"
    stephan"난 나의 아까운 뇌세포 몇 억 개를 희생했구만!"
    play music "bgm/smooth4.mp3"
    stop bgs
    centered"오후 8시 집" with fade
    ##############################스테반의 집###########################
    scene bg room_stephan_night with dissolve #스테반의 방안 백그라운드
    play sound "se/search_bag.mp3"
    "나는 윌리가 준 PX4를 설치하기 위해서 쇼핑백 안에 있는 모든 걸 꺼냈다."
    "안엔 꽤 다양한 PX4 게임들이 들어 있었는데……"
    "어째서 인지 가장 중요한 게 안 들어있었다."
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}HDMI케이블이 없잖아!{/size}" with lshake
    hide effect1
    "참고로 HDMI 케이블 이란, 본체를 모니터에 출력하는데 필요한 선 같은 거다."
    "비슷한 걸 로 지금은 안 쓰이는 VGA, A/V 등이 있다."
    stephan"이거 우리 집엔 없는데 어쩌지……"
    show effect2
    play sound "se/shock2.mp3"
    show stephan sad
    stephan"이래가지곤 게임을 할 수가 없어……"
    stephan"내 고생이 전부 물거품이 된다고!"
    hide effect2
    play music "se/phone_ring.mp3"
    stephan_think"흑……{cps=2} {/cps}누구지?"
    "절망하고 있었던 나는 폰이 울리는 걸 보고 폰을 짚어 올렸다."
    "내가 모르는 번호가 찍혀 있었다."
    stephan_think"이런 절망적인 상황에 누구냐고……"
    play sound "se/search_bag.mp3"
    stop music
    "나는 흐르는 눈물을 급하게 닦고 전화를 받았다."
    show stephan talk
    stephan"여보세요?"
    someone"오랜만이구나"
    show stephan think
    stephan_think"뭔가 낯이 많이 익는 목소린데?"
    show stephan talk
    stephan"누구신지……?"
    someone"으이구 이 자식아!"
    grandpa"네 할아버지의 목소리도 기억 못하는 게냐!"
###################################데모 버전##############################
    play music "bgm/happy2.mp3"
    show stephan shock
    stephan"할아버지?!"
    grandpa"어,{cps=2} {/cps}그래 정말 오랜만이구나"
    extend", 5년 만인가?"
    grandpa"그동안 건강하게 지냈고?"
    show stephan smile
    stephan"네!{cps=2} {/cps}전 잘 지내고 있어요!"
    stephan"할아버지야 말로 잘 지내고 계시죠?"
    grandpa"나야 뭐 나잇값을 하고 있지 허허……"
    stephan"5년 동안 무슨 일 있으셨어요?"
    stephan"전혀 연락이 없으셨잖아요!"
    stop music
    grandpa"그때 네가 급한 일이 아니면 절대 연락 하지 말라고 했잖니"
    show stephan talk
    stephan"네……?"
    stephan_think"내가 그런 말을?"
    play sound "se/think.mp3"
    play music "bgm/sad4.mp3"
    scene ev phone_stephan with flash # 쇼타 스테반이 집 앞에서 눈물을 글썽이며 할아버지에게 작별 인사를 하는 카와이한 일러스트
    stephan"할아버지……{cps=2} {/cps}흑흑"
    stephan"제 번호 절대 잊으시면 안돼요!!"
    grandpa"그래,{cps=2} {/cps}걱정 말거라"
    stephan"흑흑,{cps=2} {/cps}제가 언젠간 반드시 세계적인 탐정이 돼서……"
    grandpa"그,{cps=2} {/cps}그래 기대하고 있을게;;"
    "그땐 내가 워낙 멍청해서 몰랐지만, 탐정은 아무리 해봤자 결국엔 경찰안에 있는 직책에 불과하다."
    "절대 세계적인게 될 순 없다."
    "……물론 잘 하면 \'인터폴(국제형사경찰기구, INTERPOL)\' 같은덴 참석 할 수 있겠지만"
    stephan"통화는……{cps=2} {/cps}훌쩍……{cps=2} {/cps}꼭 필요할 때만 해요"
    grandpa"응?"
    grandpa"그건 왜?"
    stephan"엄마가 통화료 비싸다면서 안된데요……"
    grandpa"그,{cps=2} {/cps}그렇구나……"
    grandpa"그럼 연락은 꼭 필요 할 때만 하자구나……!"
    play sound "se/think.mp3"
    stop music
    scene bg room_stephan_night with flash
    show stephan shock
    stephan_think"…………"
    play music "bgm/happy2.mp3"
    stephan"확실히 제가 그런 말을 하긴 했지만……{cps=2} {/cps}그렇다고 정말로 5년만에 연락을 주시면 어떻해요……"
    stephan"저한텐 폰을 바꾼 탓에 할아버지 번호가 없어서 연락을 할 수가 없단 말이에요"
    grandpa"미안하구나……"
    stephan"뭐어……{cps=2} {/cps}딱히 미안해 할 것 까진 없고요……"
    show stephan smile
    stephan"그래도 이렇게 정정한 할아버지의 목소리 들으니까 정말 반가워요!"
    stephan"또……{cps=2} {/cps}이제 와서 저한테 연락 했다는 뜻은 뭔가 급한 일이 있다는 건가요?"
    grandpa"콜록{cps=2} {/cps}콜록"
    grandpa"급하다고 하면 급하다고 할 수 있지……"
    grandpa"스테반, 혹시 퍼즐이나 수수께끼 같은 거 좋아하니?"
    stephan"네, 좋아하죠"
    grandpa"다행이구나"
    grandpa"네가 좀 풀어줬으면 하는 퍼즐 같은 게 있거든……"
    grandpa"내일 오후 1시쯤에 이쪽으로 와줬으면 하는데……{cps=2} {/cps}괜찮니?"
    show stephan think
    stephan"흠……"
    "나는 한동안 고민을 했다."
    "내일은 황금 같은 주말"
    "예전부터 갖고 싶었던 PX4를 드디어 손에 넣었는데 주말에 게임을 못한다니……"
    stephan_think"어차피 HDMI케이블이 없어서 못하니까 상관없으려나"
    show stephan smile
    stephan"네!"
    extend" 내일 갈게요"
    show stephan
    stephan"근데 할아버지댁 주소가 어떻게 되는지 기억이 안 나는데요……"
    grandpa"아,{cps=2} {/cps}주소라면 내가 문자로 보내주마"
    grandpa"새로 산……{cps=2} {/cps}그……{cps=2} {/cps}뭐시냐……?"
    someone"{size=16}\'스마트폰\' 이요!{/size}"
    "수화기 너머로 다른사람의 목소리가 들려왔다."
    grandpa"그래!{cps=2} {/cps}\'스마트폰\'!"
    grandpa"새로 산 스마트폰을 써봐야 할 거 아니냐!!"
    show stephan shock2
    stephan"스마트폰 사셨어요?"
    play sound "se/phone_end.mp3"
    $ renpy.pause(3.3)
    "그대로 전화가 끊어져 버렸다."
    show stephan shock
    stephan"방금 뭐였지……"
    hide stephan shock
    play sound "se/phone_text.mp3"
    $ renpy.pause(1)
    "통화가 갑작스레 끊긴지 몇 분 후에 할아버지로 부터 문자가 왔다."
    "할아버지 댁의 주소다."
    "문자를 다 확인한 나는 번호를 연락처에 등록하고 폰을 다시 집어 넣었다."
    stop music
    show stephan yawn
    stephan"오늘은 너무 많은 일이 있었던 거 같아……"
    show stephan smile
    stephan"이 쌓인 스트레스를 풀 수 있는 건 게임밖에 없어!!"
    "나는 컴퓨터 앞에 앉아서 본체에 전원 버튼을 눌렀다."
    show effect1
    play sound "se/shock.ogg"
    stephan"스카이렘 300시간 다 채워야지!" with lshake
    scene black with dissolve
    play music "bgm/smooth5.mp3"
    "집안 사정으로 나는 아주 어렸을때 부모님과 떨어져서 할아버지와 함께 살았다."
    "처음엔 어색하고, 불편하고, 힘들었지만 시간이 지날수록 할아버지랑 같이 있는 게 즐거웠다."
    "특히 그 중 가장 좋았던 게 바로, 할아버지의 인생담을 듣거였지"
    "\'내가 젊었을 땐……\'으로 시작을 해서 할아버지가 경험을 통해서 배워온 것을 말했다.{cps=2} {/cps}뭔가 철학적인 분이라고 해야 할까?"
    "하지만 그것보다 더 기억에 남는 건 바로 나의 \'꿈\'을 적극적으로 지원해주신거 였다."
    "확실히 그때 내가 가졌던 꿈은 매우 충동적이었고, 지금 와서 생각해보면 한심하고 부끄럽지만……"
    "그래도 내 생애 최초로 꿈을 이루기 위해 노력을 했다는 사실에 의의가 있다!"
    "그리고 그런 계기를 제공 해준 것이 바로 나의 할아버지"
    "나한텐 할아버지를 도와줘야 할 의무가 있다."
    stop music
    centered"다음 날"
    play sound "se/alarm.wav"
    $ renpy.vibrate(1)
    $ renpy.pause(4)
    stephan"으으…… "
    extend"몇 시지……"
    scene bg room_stephan_day with eyeopen
    $ renpy.pause(0.6)
    play sound "se/search_bag.mp3"
    show ev alarm_clock
    "나는 알람시계를 봤다."
    "시계는 오전 12시 15분을 가리키고 있었다."
    stephan_think"흠냐……{cps=2} {/cps}12시 15분……"
    stephan_think"왜 내가 알람을 이 시간에……"
    hide ev alarm_clock
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    play music "bgm/beat1.mp3"
    stephan"{size=45}맞다!!{/size}" with lshake
    stephan"{size=45}할아버지 댁에 출발 해야지!{/size}"
    hide effect1
    hide stephan shock
    play sound "se/search_bag.mp3"
    "나는 허둥지둥 간단하게 씻고, 어차피 한 종류 밖에 없는 빨간 스웨터를 입고 밖으로 달려 나갔다."
    "현관문 바로 앞에 서 있었을 때 문득 떠오른 게 있었다."
    show stephan talk
    stephan"이것도 챙겨 가는 게 좋겠지?"
    hide stephan talk
    play sound "se/book_page.ogg"
    show ev book with dissolve:
        xalign 0.3
        yalign 0.5
    "나는 책상 옆에 있는 책꽂이에 꽂혀있는 붉은 책을 꺼내서 챙겼다."
    "그때 할아버지가 나에게 주신 책……{cps=2} {/cps}\'탐정의 서\'"
    show stephan talk at left
    stephan_think"이젠 필요가 없으니까……"
    play sound "se/book_page.ogg"
    jump chapter1
    
#######################연출 및 효과 테스트 방
label fx_test:
    stop bgs
    stop music
    stop sound
    scene bg room_stephan_day with dissolve
    "여긴 연출 및 효과 등을 테스트 하는 방 입니다."
    "이번엔 캐릭터 눈 깜빡임에 애니메이션을 추가해보겠습니다."
    show stephan with dissolve
    stephan"어떤가요?"
    
    
    "이번에 테스트 해볼 효과는 바로 \[시계\] 입니다."
    "시계는 아날로그와 디지털로 총 2개의 모습이 있습니다."
    show screen clock_screen
    "이게 바로 아날로그 시계 입니다."
    $ myClock.a_sound_on(False, True)
    $ myClock.set_time(0,45)
    "시간을 12:45로 설정하고, 알람을 켰습니다."
    "그럼 이번엔 15분을 진행 시켜보겠습니다."
    $ myClock.add_time(0,15,1)
    "시계가 15분을 넘기는데 1초가 걸렸을겁니다."
    hide screen clock_screen
    scene bg galaxy
    show expression (StarField().sm) as starfield with flash
    "이 효과는 바로 우주 별 움직임 효과 입니다."
    scene white with Dissolve(1.0)
    "이제부터 잡음(노이즈)효과를 표시해보도록 하겠습니다."
    play sound "se/static.mp3"
    scene ev dic_stephan
    show image "static" onlayer texture
    $ renpy.pause(1.0)
    scene black with Dissolve(1.0)
    "\'onlayer texture\'명령어를 이용했을땐 반드시 \'hide\'명령어로 이미지를 숨겨줘야 합니다."
    hide image "static" onlayer texture
    "이번엔 또다른 명령어로 같은 효과를 불러오겠습니다."
    play sound "se/static.mp3"
    scene ev dic_stephan
    show static
    $ renpy.pause(1.0)
    scene black with Dissolve(1.0)
    "이 잡음은 일반 이미지와 같은 원리로 불러오기 때문에 아무렇게나 없앨 수 있습니다."
    "여기까지가 바로 잡음 효과였습니다."
    
    
    
    
    
    
    
    
    return
    