label chapter2_2:
    stop bgs
    play sound "se/think.mp3"
    scene black with flash
    show phone2:
        zoom 1.5 xalign 0.5 yalign  0.5
    "생각해보니까 윌리가 병결로 학교에 나오지 못 하기 전 날에 모르는 번호로 문자가 왔었다."
    "어쩌면……"
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(161,182,687,386),0.0) with flash
    play bgs "bgs/people.mp3"
    show lisa talk:
        zoom 1.2 xalign 0.3 yalign -2.0
    show stephan talk:
        zoom 1.2 xalign 0.8 yalign -0.2
    stephan"어쩌면 단서가 있을지도 몰라"
    lisa"……?!"
    lisa"저,{cps=2} {/cps}정말?"
    stephan"혹시 크라운이 언제부터 가출했는지 알아?"
    lisa"전혀……"
    stephan"며칠 전에 네가 크라운한테 전화를 했었다고 했잖아?"
    stephan"그때 통화를 한 시간이 언제 였지?"
    lisa"그건 통화기록을 뒤져보면 나올거야"
    show lisa think
    lisa"…………"
    show lisa talk
    lisa"9월 15일 오후 8시 20분 이네"
    "밤 8시에 크라운에게 연락 했더니 울먹이면서 \'미안해\'라는 의미 심장한 답이 왔었다."
    play sound "se/search_bag.mp3"
    show phone2:
        alpha 0.0 zoom 0.3 yalign 0.5 xalign 0.8
        linear 0.5 xalign 0.5 alpha 1.0
    "나는 윌리의 폰에 온 문자를 보우만 에게 보여줬다."
    "보우만은 문자를 읽으면서 말 했다."
    lisa"\'지금 기다리고 있다\'고?"
    lisa"이 문자 뭔데?"
    stephan"이거 크라운의 번호로 온거지?"
    show lisa think
    lisa"음……"
    show lisa shock
    lisa"마,{cps=2} {/cps}맞아"
    stephan_think"그랬군……"
    stephan"이 문자는 크라운이 윌리한테 보낸거야"
    lisa"정말?!"
    show stephan
    stephan_think"아직은 단서가 적긴 하지만, 그래도 이정도면 찾을 수 있을지도 몰라"
    show stephan talk
    stephan"네가 스스로 친구를 찾을지, 아니면 경찰들이 찾을때 가지 기다릴지는 모르겠지만……"
    stephan"난 내가 할 수 있는 걸 다 생각이야"
    lisa"나도……{cps=2} {/cps}찾고 싶긴 하지만……"
    show stephan
    stephan"그럼 열심히 해보자"
    stop bgs
    scene black with dissolve
    centered"방과 후"
    play music "bgm/sad2.mp3"
    scene bg room_stephan_eve at Zoom((1280,720),(0,0,1280,720),(0,334,687,386),0.0) with moveup
    show stephan think:
        zoom 1.5 xalign 0.6 yalign -0.4
    "지금 내가 가지고 있는 단서……"
    "보우만이 전화를 건 게 크라운의 가출 전 인지 후 인지는 전혀 모르겠다."
    "가장 확실한 방법은 크라운의 부모님 에게 직접 물어보는거 겠지만……"
    "학생 둘이서 가봤자 좋은 결과가 나올거 같진 않고"
    "생각해보니까 오후 4시 10분에 윌리의 폰에서 울렸던 SOS 알람은 또 뭘 뜻하는 걸 까?"
    "왜 하필 이름을 SOS로 짓고, 왜 4시 10분에 울리도록 맞춘 거지……?"
    "내가 알고있는 윌리는 의미 없는 짓을 하지 않는다."
    play sound "se/think.mp3"
    scene bg room_stephan_night with flash
    show stephan:
        xalign 0.25 yalign 1.0
    show willy talk:
        xalign 0.75 yalign 1.0
    willy"맞다.{cps=2} {/cps}혹시 나 휴대폰 좀 충전 해도 괜찮을까?"
    scene bg room_stephan_eve at Zoom((1280,720),(0,0,1280,720),(0,334,687,386),0.0) with flash
    show stephan think:
        zoom 1.5 xalign 0.6 yalign -0.4
    "다음날 까지 윌리는 잠을 자지 않았다고 했다."
    "즉, 그렇게 쉽사리 폰을 집에 깜빡하진 않을거다."
    "그렇다는 건 일부러 놔두고 갔다는 뜻인가?"
    "하지만 왜?"
    stop music
    scene black with eyeshut
    show phone2:
        zoom 0.1 xalign 0.5 yalign 0.5
        linear 8.0 zoom 2.0
    "보우만이 전화를 건 같은 날 오후 4시 45분 정도에 윌리 폰으로 모르는 번호로 부터 문자가 왔었다."
    "내용은 \'지금 기다리고 있는데 어디쯤 왔어요?\'"
    "그리고 오늘 그 번호가 크라운 꺼 라는 사실을 보우만이 확인 했다."
    "잠깐……"
    play music "bgm/sirius2.mp3"
    "보우만의 말에 의하면 윌리랑 크라운은 같이 데이트를 했다고 했다!"
    "문자의 내용을 봤을때 이 걸 보냈을 상황은 어쩌면 데이트를 하기 전"
    "그렇게 되면 둘의 실종 날짜는 4시 45분 이후로 추정 할 수 있겠어"
    "생각해보니까 4시 45분이면 SOS알람이 울리기 약 35분 후……"
    "게다가 윌리가 병결로 학교를 빠지기 시작한 지 다음 날에 울렸어……"
    "알람 래이블이 SOS인걸로 봐선 뭔가 있는거 같은데"
    play sound "se/think.mp3"
    scene bg mansion_hall at Zoom((1280,720),(539,273,646,363),(539,273,646,363),0.0) with flash
    show stephan talk
    willy"며칠 전 부터 나한테 계속 이상한 일이 발생 했거든"
    willy"집에 들어오면 정리 해 뒀을 침대 커버가 엉망이고, 길을 걸을때 마다 누군가 뒤에서 따라 다니는 느낌도 들고……"
    willy"언제는 내 칫솔 까지도 사라졌다니까?!"
    show stephan shock
    stephan"완전 스토커의 짓이네……"
    scene black with flash
    "스토커……"
    "혹시……{cps=2} {/cps}데이트는 표면적인거고, 실제론 스토커와 만나러 간걸까?"
    "그렇게 된다면 이 폰은 일부러 놔두고 갔을 확률이 없진 않다."
    play sound "se/think.mp3"
    scene bg outside_road with flash
    show willy talk at right
    show stephan at left
    willy"아마 오늘은 안 자도 괜찮을 거야"
    willy"어쩌면 스토커 사건의 결착이 지어질지도 모르니까"
    scene black with flash
    "알람의 레이블이 SOS인것도, 알람이 2일 후에 울린것도 전부 스토커와 만난 뒤에 일어난 변수를 위해서"
    "하지만 왜 굳이 데이트를 한 날로부터 2일 씩이나 지나서 알람이 울렸을까?"
    "어쩌면……{cps=2} {/cps}스토커랑 만난 뒤에 아무 일도 없었을때 본인이 회수 하기 위해서?"
    "일단 이렇게 생각하면 윌리의 행동은 어느정도 앞뒤가 맞다."
    "다만……"
    "그렇게 되면 이 사건은 단순히 크라운의 가출과 윌리의 장기 결석이 아니라……"
    stop music
    "실종 사건이다."
    stephan_think"혹시 렌스 사건이랑 연관이 있는 걸까……"
    centered"같은 날 오후 8시 12분"
    play bgs "bgs/night.mp3"
    play sound "se/search_bag.mp3"
    willy_think"으……"
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,244,576,324),0.0) with eyeopen
    "나는 눈을 뜨면서 주변을 잠깐 살폈다."
    "하지만 어두워서 잘 보이진 않았다."
    show willy shock:
        yalign -5.0 zoom 1.4  xalign 0.0
        linear 0.9 yalign -0.6
    "일단은 불편하게 있었던 자세를 바로 잡았다."
    willy"여긴 어디지?"
    play sound "se/footsteps_concrete.mp3"
    show anne shy:
        zoom 1.4 xalign 2.5 yalign -1.3
        linear 2.2 xalign 1.0
    $ renpy.pause(2.7)
    anne"이,{cps=2} {/cps}일어 났어요?{cps=2} {/cps}윌리?"
    willy"너……"
    play sound "se/swing.mp3"
    show willy shock:
        linear 0.2 xalign 0.2
    $ renpy.pause(0.3)
    show willy shock:
        linear 0.2 xalign 0.0
    willy_think"이런"
    play sound "se/chain.mp3"
    show ev willy_cuffed at Zoom((1280,720),(0,0,1280,720),(0,507,378,213),0.0) with dissolve
    "나는 어떻게든 움직이려고 했지만, 양 손이 뒤에 있는 파이프에 수갑으로 채워져 있어서 꿈쩍도 할 수 없었다."
    "혹시라도 이런일이 있을때를 대비해서 열쇠 따기용으로 페이퍼 클립 2개를 들고 다니지만……"
    "보지도 않고 감각만으로 따는 건 나에겐 불가능하다."
    hide ev willy_cuffed with dissolve
    anne"저어……{cps=2} {/cps}배 고프실꺼 같아서 콘 스프 가져 왔어요……"
    show anne shock
    anne"수수수,{cps=2} {/cps}수제 스프 이에요……!"
    willy_think"일단 침착 하자……"
    willy_think"이 수갑만이라도 어떻게 되면……"
    show willy talk
    willy"지금 손이 이래가지곤 못먹겠는데,{cps=2} {/cps}좀 풀어줄 수 없을까?"
    show anne shy
    anne"그럼 제가……"
    anne"{size=20}먹여 드릴 수 있는데……{/size}"
    show anne shock
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}으아아!{/size}" with lshake
    extend" 말 해버렸다!"
    hide effect1
    show willy shock
    willy_think"이래가지곤 가망이 없겠어……"
    show anne shy
    anne"다운스 언니가 만든 것 만큼 맛 있을진 모르겠지만……"
    show anne shy:
        linear 0.3 xalign 0.8
    anne"여기……{cps=2} {/cps}아─ 해보세요……"
    willy"…………"
    anne"걱정 마세요.{cps=2} {/cps}저번처럼 수면재 같은건 안 넣었으니까요"
    anne"…………"
    show anne shy:
        linear 0.3 xalign 1.0
    play sound "se/search_bag.mp3"
    "앤은 숟가락을 내려놨다."
    show anne
    anne"윌리……"
    extend" 평상시에 피로가 엄청 쌓여 있었나봐요?"
    anne"3일 동안 계속 주무셨는데……"
    willy"3일 동안 잤다고?!{cps=2} {/cps}그럼 지금은……"
    anne"네, 9월 18일 이에요"
    willy_think"젠장……"
    play sound "se/heartbeat.mp3"
    "이거 큰일이다."
    "내가 로날드 라지오 라는 사람이랑 만나기로 한 날은 내일 오후……"
    "그 약속을 잡는데 얼마나 고생 했는데……{cps=2} {/cps}평상시에 잠을 제대로 자지 못한게 내 발목을 붙잡게 될 줄이야"
    "거기다 지금까지 날 스토킹 한 범인이 앤 크라운 이다."
    "내 예상과는 전혀 다른 인물이라서 매우 곤란하다……"
    "어쩔 수 없이, 지금부턴 오직 탈출만을 중점으로 해서 행동 해야겠다."
    "이 이상 시간을 지체했다간 더 곤란해진다."
    anne"지금은 피로가 다 풀려서 개운 하세요……?"
    willy"장난은 집어 치우고,{cps=2} {/cps}여긴 어디야?!"
    show anne yantalk
    anne"위치를 알면 어쩌려고요?"
    play music "bgm/sirius5.mp3"
    anne"또 뭔가 계획을 세워서 다른 사람에게 여기 위치를 알릴건가요?"
    willy"…………"
    show anne yan
    anne"전 윌리에 대해서 전부 알고 있어요!"
    play sound "se/search_bag.mp3"
    show phone2:
        zoom 0.3 xalign 0.75 yalign 0.65
    anne"먼저 이 휴대폰"
    anne"이건 윌리의 폰이 아니잖아요?"
    anne"제가 알고 있는 거랑 폰에 써져있는 번호랑 다르더라고요"
    anne"어쩌면 윌리의 진짜폰은 다른데 있고……{cps=2} {/cps}이걸로 그 폰을 \'미러링(Mirroring)\'하고 있었던게 아닌가요?"
    anne"그래서 제가 문자를 보냈다는 걸 알 수 있었잖아요?"
    willy"으……"
    anne"진짜 폰으로 제가 보낸 문자가 도착 하게 되면 저랑 윌리가 만났다는 사실과 그 시간이 전달되죠……"
    anne"그리고 자세한 사항은 나중에 뭔가가 발생 했을때 추가로 보낼 생각 이었고……"
    hide phone2 with dissolve
    anne"진짜 폰을 가지고 있는 사람이 누군진 잘 모르겠지만……"
    anne"어차피 그 계획은 윌리가 여기를 모르고 있다면 상관없게 돼요"
    show anne yantalk
    anne"처음엔 윌리의 계획 치곤 많이 허술하다고 생각 했었거든요……"
    anne"하지만 그것도 그럴 수 밖에 없었겠죠……"
    show anne yan
    anne"저를 \'하데스\'랑 관련 있는 사람 이라고 착각 했으니까"
    willy"그 이름을 알고 있어……?"
    anne"처음엔 하데스가 저를 이용해서 윌리를 아무도 모르게 납치 할거라고 생각 했겠지만……"
    anne"설마 제가 직접 윌리를 그렇게 사람이 많은 커피숍에서 바로 잠 재워버릴거라곤 예상도 못 했겠죠"
    show anne yantalk
    anne"하,{cps=2} {/cps}하지만 전 그런 사람이랑은 전혀 관계 없어요!"
    willy"그럼 어떻게 거기까지 알고 있는거야?!"
    anne"그건……{cps=2} {/cps}이 폰을 뒤지면서 온 문자를 통해서 알게 됐어요"
    anne"렌스 클라크……{cps=2} {/cps}멜 다운스……"
    anne"마르쿠스 고드윈……"
    anne"그리고 라지오……{cps=2} {/cps}였던가요?"
    anne"또, 저장돼있지 않은 번호로부터 계속 하데스와 같이 의미심장한 암호 같은것도 많이 왔더라고요"
    willy"네가 정말로 하데스랑 전혀 관련이 없다면, 동기가 전혀 이해 안 가는데?"
    show anne talk
    anne"역시……"
    extend" 설령 윌리라고 해도 이해하긴 힘들겠죠……"
    willy"…………"
    anne"저의 동기는 단 한가지 뿐입니다"
    play sound "se/heartbeat.mp3"
    scene bg case2_inside3_night at Zoom((1280,720),(0,244,576,324),(149,361,378,212),0.5) with dissolve
    show anne yan:
        zoom 1.6 yalign -0.4 xalign 0.5
    anne"같이 있기 위해서 였어요……"
    willy_think"같이 있기 위해서?"
    willy"우리 둘이 계속 학교를 나오지 않으면 다들 수상 하다고 여기고, 경찰에 신고 할 텐데?"
    willy"고작 같이 있기 위해서 그런 리스크에 걸겠다고?"
    show anne yantalk
    anne"수색 이라면 당분간은 걱정 하실 필요 없을거예요"
    anne"아마 다들 제가 가출 했다고 생각 하고 있을걸요?"
    anne"원래 부모님 이랑은 학업 관련으로 자주 싸웠으니까……"
    show anne yan
    anne"무엇보다 제 실종 사유가 가출 이라고 생각 하면 다들 수색의 방향이 바뀌죠!"
    anne"상식적으로 가출청소년이 갈만 한 PC방, 카페, 사우나 등을 집중적으로 조사 하고……"
    anne"하지만 여기는 그런 곳 이랑은 정 반대예요~"
    anne"그리고 또, 윌리가 집에 있는 사람들한테 자기가 부제 일 경우 학교에는 병결로 처리 해달라고 부탁 했었던데……"
    willy"…………"
    willy"그럼 내 주변인 한테 보낸 모스부호로 된 문자는 뭐지?"
    show anne talk
    anne"그 문자를 어떻게 해서 알게 됐어요?"
    willy"같은 반의 여자애가 보여줬어……"
    show anne shy
    anne"그,{cps=2} {/cps}그 문자를 본 뒤, 윌리는 그 사람들을 멀리 하게 됐죠……?"
    willy"당연하지!{cps=2} {/cps}어쩌면 나 때문에 주변 사람들도 위험한 일에 말려 들 수 있었는데!"
    willy"……설마 네 목적이?!"
    show anne yan
    anne"네……"
    extend" 윌리가 다른 사람들을 멀리 하기 위해서 보냈어요!"
    show anne yantlak
    anne"다른……{cps=2} {/cps}사람이랑 만나는 게 정말 싫었거든요……"
    anne"저 이외에 여자랑 같이 친하게 지내고……"
    willy"그런 이기적인 생각만으로 보낸거냐……"
    show anne shock2
    anne"저도 그 쯤은 자각하고 있어요……"
    anne"또, 이대로 계속 갔다간 되돌아 갈 수 없을지도 모른다는 생각도 들었고요"
    willy"그림 지금이라도 풀어 줘!"
    show anne yan
    anne"하지만 제가 충동적으로 떠오른 계획이 이렇게까지 효과를 발휘 할 수 있었던건 몰랐어요!"
    anne"모스 부호로 된 문자만 해도 그랬죠"
    anne"윌리는 학교에서 인기가 많고, 대부분의 여자애들이 대화를 섞고 싶어하는 그런 존재"
    anne"확실히 모스 부호는 인터넷을 통해서 쉽게 해석 할 수도 있지만, 윌리를 좋아하는 애라면 분명 윌리에게 물어봤겠죠!"
    anne"이걸로 전 문자 한통으로 윌리를 사랑하는 애들만 걸러낼 수 있었어요"
    show anne
    anne"그리고 제가 왜 굳이 다른 암호가 아닌 모스 부호를 이용했는지 아세요?"
    willy"아니"
    anne"그, 그게 조금 상징적인 의미를 담았는데……"
    anne"모스 부호를 발명 한 사람의 이름은 \'새뮤얼 모스(Samuel Morse)\'라고 해요"
    anne"그가 연구를 시작하기 전에……{cps=2} {/cps}직업으로 화가를 했대요"
    anne"어느 날 모스는 어떤 사람의 초상화를 그리기 위해서 미국 워싱턴 DC. 로 장기간 출장을 가게 됐죠"
    anne"그러다……{cps=2} {/cps}편지로 자신의 아내가 아프다는 소식을 듣게 됐어요……"
    anne"편지를 읽자마자 바로 집으로 돌아갔지만……"
    extend" 도착햇을땐 이미 아내의 장례까지 다 치뤄진 뒤였어요"
    anne"그 뒤로 모스는 장거리에서도 빠르게 교신할 수 있는 방법을 연구하기 시작했대요"
    anne"그가 사랑하는 사람과의 거리를 좁히기 위해서 발명을 시작 했듯이……"
    show anne shock
    anne"저저저 저 역시도 윌리와의 거리를 좁히기 위해서 라는 의미로……"
    show anne shock2
    anne"이렇게 말 하고 나니까 좀 쑥스럽네요……"
    willy"만약 네가 중간에 잡히기 된다면 어쩔거지?"
    anne"경찰에게요?"
    willy"그래,{cps=2} {/cps}일단 넌 가출로 돼있다고 했으니까 누군가 널 찾으러 오긴 할 거 아니야"
    anne"상관 없어요"
    anne"전 윌리랑 이렇게 단 둘이서 있었으니까……"
    anne"가까이……{cps=2} {/cps}한 지붕 아래에서 자기도 했고……"
    show anne yanshock
    anne"히익!"
    anne"어어어,{cps=2} {/cps}어쨌건! 이렇게 하면 당분간은 저랑 윌리와의 사랑의 도피는 아무도 방해 할 수 없을거예요"
    willy"으……"
    "이런 예상치도 못한 사건 때문에 위기감이 느껴졌다."
    "하지만 이 모든 계획이 고작 충동적으로 떠오른 거 라면, 앤은 내가 생각 했던것 보다 똑똑한 애 일지도 모른다."
    "우선 지금 상황을 냉정하게 분석해보자"
    "수갑때문에 자력으로 빠져나오는 건 힘들다.{cps=2} {/cps}주변엔 열쇠 대용으로 쓸 수 있는 게 아무것도 없다."
    "그렇다면 내가 사전에 세워 놓은 탈출 계획 B랑 C에 걸어보는 게 상책 일지도 모르지만……"
    "문제는 지금 상황에선 현재 내 위치를 알 수 있는 방법이 없다."
    "나 자신도 모르는 걸"
    willy_think"아니지……"
    "생각해보니까 지금 앤 손엔 내 폰이 있다."
    "저 폰에 전원만 꺼지지 않았다면……{cps=2} {/cps}C계획은 실행 할 수 있을지도 모른다."
    "그리고 내가 입막음을 당하고 있는것도 아니니까, 앤이랑 대화를 통해서 빠져 나가는 것도 가능할지도 모른다."
    willy_think"생각보다 빠져나갈 수 있는 길은 많네"
    anne"제 계획 어, 어때요?"
    willy"다시 한번 정리를 하자면……{cps=2} {/cps}넌 나랑 같이 있기 위해서 이 모든 일을 꾸몄다는거야?"
    willy"정말 그 외엔 아무런 목적도?!"
    show anne yantalk
    anne"맞아요……{cps=2} {/cps}정말 이해가 안 되죠?"
    willy"그래"
    stop music
    anne"사실 저도 조금은 그래요……"
    anne"그, 그래도 사랑 이니까……"
    willy"어……?"
    scene bg case2_inside3_night at Zoom((1280,720),(149,361,378,212),(0,244,576,324),0.5) with dissolve
    play music "bgm/smooth1.mp3"
    show willy shock:
        yalign -0.6 zoom 1.4  xalign 0.0
    show anne shock:
        zoom 1.4 xalign 1.0 yalign -1.3
    anne"지,{cps=2} {/cps}지금부터 제가 아주 부끄러운 말을 할거예요!"
    show anne shy
    anne"하지만 전부 제 진심 이라는 걸 명심 해주세요"
    anne_think"(꿀꺽)"
    anne"전……{cps=2} {/cps}전……"
    anne"하아……"
    show anne shock2
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}전 윌리를 엄청 좋아해요!{/size}" with lshake
    anne"이 세상에서 그 누구보다도!"
    hide effect1
    "엄청나게 당황했다."
    "날 납치한 사람한테서 구속된 상태로 고백을 받다니……"
    "과연 무슨 대답을 해야 빠져나갈 수 있을까?"
    "나는 조금만 더 생각 할 시간을 벌기 위해서, 마음에 없던 대답을 했다."
    willy"그럼……{cps=2} {/cps}넌 언제부터 날 좋아하기 시작했어?"
    show anne shy
    anne"그,{cps=2} {/cps}그건……"
    stop bgs
    stop music
    scene black with memory
    "제가 중학생 이었을때 였었던가요……"
    "당시 전 곤충 채집과 관찰일기를 기록하는데 푹 빠져 있었어요."
    play music "bgm/sad2.mp3"
    "하지만 제 주변에선 언제나……"
    show text"그런 건 나중에 대학 들어가고 나서 해도 늦지 않잖아?" with dissolve:
        xalign 0.1 yalign 0.1
    $ renpy.pause(3.0)
    show text"지금 성적 가지곤 도시에 있는 고등학교 들어가기 힘들지도 모르니까……" with dissolve:
        xalign 0.9 yalign 0.25
    $ renpy.pause(3.0)
    show text"넌 곤충 같은 게 무섭지도 않니?!" with dissolve:
        xalign 0.1 yalign 0.4
    $ renpy.pause(3.0)
    show text"정말 생긴거랑 다르네" with dissolve:
        xalign 0.9 yalign 0.55
    $ renpy.pause(3.0)
    show text"으엑! 깬다!" with dissolve:
        xalign 0.1 yalign 0.7
    $ renpy.pause(3.0)
    scene black with moveright
    "아무도 저를 이해하지 못했어요."
    play bgs "bgs/birds.mp3"
    scene ev watching_bug with Dissolve(1.0)
    anne"와아……"
    "저에게 곤충이라는 존재는 너무나도 흥미로웠습니다."
    "하지만 제가 딱히 곤충을 좋아했던건 아니에요.{cps=2} {/cps}왜냐면 전\'인간 이외에 자의식을 갖춘 모든 생물\'의 회로에 대해서 흥미를 가졌던거니까요."
    "인간은 서로간의 의사소통이 가능하기 때문에 대충 어떤 생각을 하고 있는지 \'이해\'할 수 있어요."
    "허나 곤충들을 이해한다는 건 얘기가 다르죠"
    "사람이라면 대부분 삶의 목표를 가지고 있거나, 언젠간 찾아올 미래를 기다리면서 하루하루를 보내고……{cps=2} {/cps}삶에대한 가치를 느끼지 못하면 자살을 합니다."
    "……그럼 곤충들은 무엇을 위해서 살고 있을까요?"
    "무엇을 위해서 당장 자살을 하지 않고, 오늘 내일을 살아갈까요?"
    "그것이 바로 저의 궁금증 이었습니다."
    "사실 제가 곤충을 좋아하지 않았단것도 아니에요."
    "실제로 전 집 근처에 있는 산으로 올라가서 곤충을 채집하고, 기록이 끝나면 놔주고를 반복 했으니까요."
    "그들에 대한 제의 궁금증을 해소하기 위해서 제 나름대로 연구를 했죠"
    stop music
    stop bgs
    scene black
    "하지만 아무도 그런 저를 이해하지 못했어요."
    "그냥 단순히 제가 얌전한 여학생 이면서 곤충을 좋아하는 조금 별난 애 라고만 단정짓고"
    "어차피 전 남의 이해를 원하지 않았기 때문에 크게 신경쓰지 않으려고 했지만……"
    show text"넌 왜 맨날 그러는거니?" with dissolve:
        xalign 0.1 yalign 0.1
    $ renpy.pause(3.0)
    show text"얼굴은 귀여운데……" with dissolve:
        xalign 0.9 yalign 0.25
    $ renpy.pause(3.0)
    show text"조금만 더 노력을 하면 분명 좋아질거야" with dissolve:
        xalign 0.1 yalign 0.4
    $ renpy.pause(3.0)
    show text"좀 그만 멍때리고 생산성이 있는 일을 해!" with dissolve:
        xalign 0.9 yalign 0.55
    $ renpy.pause(3.0)
    hide text with dissolve
    anne"나에 대해서 뭘 안다고……"
    "저에 대해서 아는것도 없는 사람들이 함부로 평가하는 건 정말 싫었어요."
    "그것도 단순히 제가 곤충을 좋아하는 것만 평가하는 게 아니라, 관련 없는 저의 평상시 행동까지도 평가하고, 단정짓고……"
    "언제부터 였는진 잘 모르겠지만……{cps=2} {/cps}학교에선 다들 저를 \'이상한 애\'취급 하면서 멀리하기 시작했죠"
    play music "bgm/sirius5.mp3"
    "그런 짜증나는 생활의 반복으로 저는 \'이 세상을 없애버리고 싶다.\'{cps=2} {/cps}\'저 사람을 죽여버리고 싶다.\' 와 같이 위험한 충동에 휩쌓여버렸어요."
    "하지만 제가 가장 무서웠던 건, 왠지 진짜로 남을 죽일 것 만 같은 저의 생각이었어요."
    "남을 보면 반사적으로 상대를 마음속으로 저주하고, 만약 그들을 죽인다면 언제 어디서 어떤 무기로 어떻게 죽일지 매우 상세한 살인 계획까지 짜고 있었고……"
    "그런 생각을 했다는 제 자신을 돌아보면서 왠지모를 위협감이 느껴졌어요."
    "당장이라도 이 쌓인 감정을 어딘가로 해소를 하지 않으면……{cps=2} {/cps}진짜로 저지를 것만 같았어요."
    "그래서 전……"
    play sound "se/hit2.mp3"
    scene ev watching_bug
    show red with lshake:
        alpha 0.7
    $ renpy.pause(1.0)
    "지금까지 관찰해오고, 아껴왔던 곤충들을 죽이기 시작했어요."
    "동물을 죽이는 것보단 건전하다고 생각했고, 인간을 죽이는것보단 100번 좋았고"
    "평상시엔 관찰을 목적으로 했던 채집을, 이젠 죽이는 목적으로 하기 시작했어요."
    "처음엔 칼로 곤충의 다리 하나하나를 자르면서, 몸만 있는채로 꿈틀거리는 걸 보면서 기분을 풀었죠"
    "혹은 기름을 부운 후, 불로 태워버리거나"
    "특히 수많은 개미떼 위에서 그렇게 하면 엄청난 희열이 느껴졌어요."
    "나중엔 조금 더 창의성을 발휘해서, 화학 물질을 사용하기 시작했죠"
    "곤충의 먹이에 독극물을 타서 어떻게 죽어가는지 본다든가, 강한 염산을 구해서 녹여본다든가……"
    "언제는 채집 통 안에서 사마귀 암 수를 데리고 짝짓기를 시켜봤어요"
    "그리고 암컷이 수컷의 머리를 먹는 모습을 지켜보면서 생각했죠"
    "제가 직접 죽이는 것보단, 다른 생물이 잡아먹는 걸 보는것도 나쁘진 않다고"
    scene black with Dissolve(1.0)
    stop music
    "그러다……{cps=2} {/cps}또 한번 지금까지 저의 행동을 되돌아보게 됐습니다."
    "처음엔 순수하게 \'알고 싶다\'는 이유로 함께하던 곤충을……"
    extend" 그저 화풀이 대상으로 삼고 있었던 자신을"
    "애초에 남들이 자신을 이해하지 못했다는 이유만으로 이렇게까지 화를 내다니……"
    "자신이 한심하게 느껴졌습니다."
    "남들이 저를 잘 모른채 함부로 평가 했다는 이유 만으로……{cps=2} {/cps}한때 소중했던 곤충들에게 화풀이를 하다니……"
    "생각해보면 이중에서 가장 나쁜건 바로 저 였어요."
    "처음부터 살인 충동을 느꼈던 제 자신이 가장 나쁜 존재……"
    "그걸 깨달는 순간,{cps=2} {/cps}자기 자신이 정말 싫어졌습니다."
    "내가 왜 이런 위험한 성격을 지녔는지……{cps=2} {/cps}나는 왜 남들과 다르게 태어났는지……"
    "과거에 남을 속으로 저주하고, 남을 죽이겠다는 충동에 빠지고, 죄 없는 곤충들에게 화풀이를 하고……"
    "전부 후회하면서, 자신을 더더욱 싫어하게 됐고……"
    "결국엔 자신을 무서워하게 됐어요."
    "계속 살아있으면……{cps=2} {/cps}나중에 더 많은 생물들을 죽일지도 모를 것 같았고……"
    "심하면 살인 이라도 저지를 것만 같았아요."
    "저같은 사람을 잠재범죄자 라고 하죠……"
    "이 증상을 고치기 위해서 여러 행동을 다 해봤지만, 오히려 자기 자신이 얼마나 싫은 존재인지만 더 확인 시켰고……"
    play sound "se/cutter.mp3"
    play music "bgm/sad5.mp3"
    $ renpy.pause(1.0)
    "……그때 저는 결심했어요."
    play sound "se/hit3.mp3"
    show red:
        alpha 0.6
    $ renpy.pause(1.0)
    "\'내가 죽는 게 남을 위한거야\'{cps=2} {/cps}\'내가 죽는 게 남을 위한거야\' 라며 자해를 반복하고……"
    "그때부터 저는 자신의 손목을 베는 습관이 생겼어요."
    "하지만 마지막엔 언제나 피가 굳어서 멈춰버리고……{cps=2} {/cps}죽는 경우는 없었죠"
    "저의 그런 생활은 거의 몇 달간 계속 반복 됐어요."
    "버틸 수 없을 정도로……"
    play bgs "bgs/street.mp3"
    scene bg diary_country at Zoom((1280,720),(0,0,1280,720),(655,302,625,351),0.0) with dissolve
    show anne yantalk:
        xalign 1.0 yalign 1.0
    anne"오늘……{cps=2} {/cps}하는거야"
    "방과후 귀가길에 사고로 가장해서 자살을 하기로 결심 했어요."
    "역시……{cps=2} {/cps}자살보단 사고로 죽었다는 게 부모님을 덜 슬프게 만들 거 같았거든요……"
    play sound "se/footsteps_concrete.mp3"
    show bg diary_country at Zoom((1280,720),(655,302,625,351),(310,302,625,351),2.0)
    show anne yantalk:
        linear 2.3 xalign 0.5
    $ renpy.pause(2.3)
    "끝이 찾아오기를 기다렸어요."
    stop music
    stop bgs
    play sound "se/car_horn.mp3"
    scene black with flash
    $ renpy.pause(1.5)
    play sound "se/fall.ogg"
    $ renpy.vibrate(0.3)
    $ renpy.pause(1.0)
    anne_think"끙……"
    $ extra_name = '운전자'
    extra"길 한가운데에서 멍 때리면 어떻게!"
    extra"잘못하면 사고 날 뻔 했잖아!"
    $ extra_name = '남성의 목소리'
    extra"정말 죄송해요!{cps=2} {/cps}제가 다음부턴 조심 하라고 일러 둘게요!"
    $ extra_name = '운전자'
    extra"나, 참……"
    $ extra_name = '남성의 목소리'
    extra"너 괜찮아?"
    anne_think"어……?"
    play bgs"bgs/street.mp3"
    scene white with eyeopen
    play music "bgm/sad2.mp3"
    scene bg diary_country at blur with dissolve:
        crop(58,374,474,266)
        size(1280,720)
    show willy talk:
        xalign 0.5 yalign -0.1 zoom 1.8
    "차에 치이려고 했던 절, 윌리가 구해줬어요."
    "하지만 당시에 전 그 행동이 정말 짜증나게 느꼈어요."
    anne"왜 그런거죠……"
    willy"어?{cps=2} {/cps}무슨……"
    anne"이렇게까지 하는데 얼마나 많은 용기가 필요 했는데……"
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}왜 저를 막은거냐고요!{/size}" with lshake
    show willy mad
    willy"너, 설마 자살 하려고 했던거야?!"
    hide effect1
    anne"그, 그게 그쪽이랑 무슨 상관이에요……"
    willy"상관 없긴 왜 없어?!{cps=2} {/cps}자기 목숨을 소중히 여기느……"
    anne"그런식으로……{cps=2} {/cps}아무것도 모르면서 쉽게 말 하고……"
    show willy shock
    willy"……?"
    anne"아무것도 모르는 주제에 멋대로 단정짓고, 평가하고……"
    anne"이렇게라도 하지 않으면 더 큰 문제가 발생 할 거 같단 말이에요……{cps=2} {/cps}더이상 남에게 피해를 주고싶지가 않고……"
    anne"{size=22}무엇보다 자신이 너무 싫은 걸……{/size}"
    "솔직히 조금 무서웠어요……"
    "그때 윌리가 구해줘서 다행이라고 내심 생각 하기도 했죠"
    show willy talk
    willy"…………"
    willy"그런 생각 이라면 네 말대로 내가 쓸대없는 참견을 했을지도 모르겠네"
    willy"난 너에대해서 아는것도 없으면서 멋대로 자기 목숨을 소중히 여기라고 말 하고"
    willy"분명 너도 내가 이해 못 할 너만의 이유가 있으니까 그런 선택을 했던거겠지?"
    anne"그, 그런거예요"
    willy"그럼 난 너의 그런 선택을 존중해"
    anne"…………"
    show willy
    willy"하지만, 네가 그런 이해 못 할 선택을 한 만큼, 나도 널 구하는덴 네가 이해 못 할 이유가 있어"
    willy"그러니까 내가 널 구해준 것에 대해서 존중 해 줄 수 있을까?"
    anne"…………"
    show willy talk
    willy"그리고 네 인생에 멋대로 참견 한 김에 한번더 하겠는데……"
    willy"자기 자신을 싫어하는 건 그만 둬"
    anne"정말 말은 쉽게 하네요……{cps=2} {/cps}아무것도 모르면서……"
    willy"그래, 난 너에 대해서 아무것도 몰라"
    extend". 하지만 넌 너에 대해서 알고 있잖아?"
    willy"남의 생각을 증명하는 건 불가능하지만, 자기 자신의 생각을 증명하는 건 가능해"
    show willy
    willy"그런데도 너 자신을 이해할 수 있는 유일 한 존재를 스스로가 배척하는 건……{cps=2} {/cps}왠지 쓸쓸하잖아?"
    willy"자기혐오는 너를 이 넓은 세계에서 혼자 남아있는거 보다 더 외로운 존재로 만들텐데"
    anne"……!"
    "정말 마음에 와닿는 말이었어요."
    "지금까지의 사람들은 나에 대해서 알고있다는 듯이 멋대로 평가 했지만……{cps=2} {/cps}윌리는 달랐으니까요."
    "무엇보다 제가 하고 있었던 일의 잘못을 지적해주는 게……"
    willy"어쨌건, 지금 네가 살아있으면 됐어"
    anne"…………"
    willy"근데 혹시 이름이 앤 크라운 이야?"
    willy"1학년 2반에 있는"
    anne"네?"
    anne"어, 어떻게 아셨어요?!"
    willy"어쩐지 본 것 같은 느낌이 들더라"
    willy"난 1반이거든"
    anne_think"가, 같은 학교라……"
    anne_think"방과후 라서 딱히 이상 할 건 없지만……"
    willy"내 이름은\'윌리엄 R 제임스(William R. James)\'라고 해"
    extend". 그냥 짧게 \'윌리(Willy)\' 라고 불러줘"
    anne"왜 갑자기 친한척 하는거예요……"
    anne"그보다 같은 반인것도 아닌데 어떻게 제 이름을 알고 있는거죠?"
    willy"그냥 이름만 알고있어.{cps=2} {/cps}같은 학교 학생들의 이름은 전부 외우고 다니는 편이라서"
    anne"…………"
    show willy shock
    willy"그리고 난 어떤 의미에선 네 생명의 은인인데 말이야……"
    anne"딱히 원했던 생명도 아니라서 별로 은인같은 느낌은 안들어요"
    willy"뭔가 짜증나는 말투네……"
    play sound "se/search_bag.mp3"
    show bg diary_country at blur:
        linear 0.3 crop(100,374,474,266)
    show willy shock:
        linear 0.3 xalign 0.3
    anne"그럼 이제 비켜주시겠어요?"
    show willy sirius
    willy"또 이런 일은 하지 않을거지?"
    anne"…………"
    willy"난 자살 하는것에 대해선 반대하지만, 부정 할 수 없는 이유가 있다면 강하게 반대도 안 할거야"
    willy"하지만 너의 행동은 뭔가 모순돼서 봐주기가 힘드네"
    play music "bgm/sad4.mp3"
    show bg diary_country at blur:
        linear 0.3 crop(58,374,474,266)
    show willy shock:
        linear 0.3 xalign 0.5
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}아무것도 이해 못한다면서 모순을 말 하는 건가요?!{/size}" with lshake
    hide effect1
    willy"생각해봐,{cps=2} {/cps}많을지 어떨련진 모르겠지만, 세상엔 널 소중하게 여기는 사람들이 분명 있을거야"
    willy"부모님이나, 친구라든가……"
    willy"그리고 넌 더이상 남에게 피해를 주고싶지 않다면서 자살을 시도했잖아?"
    willy"근데 네가 죽게 되면 그 사람들에게 피해를 주는 게 돼"
    willy"넌 남을 위해서 하겠다는 행동이 오히려 남에게 피해를 주고 있다는 걸 몰라?"
    anne"……!"
    anne_think"생각해보니까……"
    stop bgs
    play sound "se/think.mp3"
    show ev watching_bug
    show red with flash:
        alpha 0.7
    anne_think"사람을 죽이는 걸 피하기 위해서 소중했던 곤충들을 죽였고……"
    anne_think"남들이 나를 이해하지 못한것에 불만을 했으면서도 내 자신을 싫어했고……"
    anne_think"남에게 피해 주기 싫어서 자살을 하려고 했고……"
    play bgs "bgs/street.mp3"
    hide ev watching_bug
    hide red with flash
    "……윌리는 그때 저의 모든 행동은 모순 투성이라는 걸 깨달게 해줬어요."
    "생각해보면 지금까지 저는 잘못된 판단 후, 뒤늦게 그걸 깨달고 계속 후회했어요."
    "그리고 그 후회를 만회하기 위한 행동이 또다른 후회를 낳고……"
    show willy shock at blur with dissolve:
        xalign -0.25
    anne"흑……"
    willy"잠깐?!{cps=2} {/cps}왜 울어?!"
    anne"아, 아니에요……"
    anne"그냥……"
    anne"…………"
    play sound "se/footsteps_running.mp3"
    scene black with moveright
    stop bgs
    "집에 돌아와서 엄청나게 고민했어요."
    "그리고 다시한번 \'후회\'했죠"
    "자신의 모순되는 행동과……{cps=2} {/cps}지금까지 후회했던 일들에 대해서……"
    "그러다 언제부턴가 윌리의 존재가 신경쓰이기 시작했어요."
    "도대체 어떤 사람이길래 저렇게 맞는 말 만 하는 걸까……"
    "어떻게 하면 나도 저렇게 될 수 있을까……"
    play bgs "bgs/people.mp3"
    "그때부터 저는 학교에서 몰래 윌리를 \'관찰\'하기 시작했어요."
    "매일매일 관찰일기를 기록하고, 사진 자료를 찍고……"
    "한때 제가 곤충들을 관찰 했을때 느꼈던 그 순수한 감정이 다시 살아나기 시작하면서……{cps=2} {/cps}인생이 다시 즐거워졌어요."
    "더이상 후회를 하지도, 극단적인 선택을 하지도 않고……{cps=2} {/cps}모든게 정상적으로……"
    play bgs "bgs/night.mp3"
    play music "bgm/sad2.mp3"
    scene bg case2_inside3_night at Zoom((1280,720),(0,244,576,324),(149,361,378,212),0.5) with memory
    show anne smile:
        zoom 1.6 yalign -0.4 xalign 0.5
    anne"윌리는 여러 의미에서 저의 생명의 은인이에요"
    show anne shock
    anne"그, 근데 지금와서 다시 떠올려보니까 좀 부끄럽네요……"
    "당시 앤 크라운은 같은 학교에 있는 애라는 것만 알고 있었지, 그 외엔 아무것도 몰랐고, 구해주는데 특별한 이유가 있었던것도 아니었다."
    "내가 누군가를 도와줄 수 있다면 좋겠다고 생각해서 했던건데……"
    willy_think"설마 이렇게 이어질 줄이야……"
    "그보다 앤 크라운은 그 날 이후로부터 계속 나를 스토킹 했다고 했다."
    "하지만 내가 그녀의 기척을 알기 시작한건 꽤 최근이다."
    "왜 이제서야 눈에 띄는 스토킹 짓에, 납치극 까지 벌이게 된걸까"
    willy"앤……"
    anne"네!"
    willy"만약 그때부터 계속해서 내 스토킹을 했다면……{cps=2} {/cps}왜 이제와서 이런일을 하는거야?"
    show anne shock2
    anne"그그그 그건……!"
    show anne
    anne"더이상……{cps=2} {/cps}놓치고 싶지가 않아서 라고 해야 할까요……"
    anne"중학교 3학년때 윌리가 갑작스레 도시로 전학을 가게 되면서 더이상 만나질 못하니까……"
    anne"전 앞으로 어떻게 살아가야 할지 몰랐어요"
    show anne shock
    anne"그래도 윌리가 저한테 해준 말을 가슴에 새기면서 열심히 살아가려고 노력했어요!"
    show anne
    anne"기존의 저를 바꾸기 위해서 평상시에 해보지도 않은 공부 라는 걸 해보고……{cps=2} {/cps}조금 꾸며보기도 하고……"
    anne"여차저차해서 겨우 도시에 있는 고등학교에 들어 갈 수 있을 정도로 학업을 유지 했어요"
    anne"그리고 제가 고등학교에 입학 후 며칠 뒤에……"
    play sound "se/think.mp3"
    play bgs"bgs/people.mp3"
    scene bg school_cafe with flash
    show stephan:
        zoom 1.5 xalign -0.5 yalign -0.2
    show willy:
        zoom 1.5 xalign 0.2 yalign -0.2
    willy"……맞아"
    play sound "se/footsteps_concrete.mp3"
    show anne:
        zoom 1.5 xalign 2.0 yalign -0.6
        linear 2.0 xalign 1.0
    $ renpy.pause(2.0)
    anne"어?"
    extend" 윌리?"
    show willy talk:
        linear 0.3 xalign 0.3
    willy"……?"
    willy"혹시 앤 크라운?"
    show willy
    willy"여기서 만날 줄이야!{cps=2} {/cps}너 여기 고등학교 다녀?"
    show anne shock
    anne"히이이익!"
    play sound "se/footsteps_running.mp3"
    show anne shock:
        linear 0.4 xalign 2.0
    show willy shock
    willy"…………"
    play sound "se/move.mp3"
    scene black with moveright
    $ renpy.pause(0.5)
    scene bg school_cafe at Zoom((1280,720),(0,0,1280,720),(573,343,549,309),0.0) with moveright
    show anne shock2:
        xalign 0.4 yalign -0.4 zoom 1.4
    anne_think"위, 윌리가……{cps=2} {/cps}이 학교에……"
    anne_think"같은 고등학교라니……"
    "더이상 만나지 못 할줄 만 알았던 윌리랑 같은 고등학교를 다닌다는 게, 정말 운명 같았어요."
    scene bg school_hall with moveleft
    show anne shy:
        xalign 0.5 yalign 1.0
    show willy smile:
        zoom 1.7 xalign 0.9 yalign -0.3
    show stephan:
        zoom 1.7 xalign 1.5 yalign -0.3
    "……하지만 아무리 같은 학교에 다녀도 저는 윌리 근쳐에 가면 너무 부끄러워서 말 걸기 힘들었어요."
    scene bg school_hall with flash
    show anne shock:
        xalign 0.7 yalign 1.0
    show willy:
        xalign 0.3 yalign 1.0
    "아주 가끔, 서로 부딫힐 때 몇마디 섞는 게 고작이었으니까……"
    stop bgs
    show black:
        alpha 0.0
        linear 1.0 alpha 1.0
    "그리고 정신 차려보니까 벌써 고등학교 2학년이 돼있었죠……"
    "아무리 운명적인 만남을 가져도, 그 운명을 잡지 못하면 아무런 의미가 없었어요."
    "그러다 어느날 이었어요."
    play sound "se/think.mp3"
    scene bg school_hall at Zoom((1280,720),(464,106,559,315),(464,106,559,315),0.0) with flash
    show anne:
        xalign 1.0 yalign 1.0
    show lisa:
        xalign 0.6 yalign 1.0
    lisa"다른 방법을 찾는것보단 용기를 내서 걔한테 직접 말해"
    lisa"방금 토머…… {size=25}(푸흡){/size} ……를 봤잖아"
    lisa"저건 너보고 용기를 내서 스스로에게 솔직해지라는 하늘의 뜻인거야!"
    anne"스스로에게 솔직해지라고……?"
    "\'스스로에게 솔직해진다\'라는 말이 엄청 마음에 닿았어요."
    "전 하고싶은 게 있어도 남에게 피해를 줄 것 같다는 이유로 꺼려하고……{cps=2} {/cps}자신을 속여왔어요."
    "하지만 이젠 생각을 고쳐먹기로 했어요."
    scene black
    "전 윌리를 사랑해요."
    "그리고 곁에 있고 싶어요."
    "더이상 부끄러워 하지 않고, 당당하게 말을 걸고, 옆에서 제가 몰랐던 윌리의 모습도 보고싶어요."
    play bgs"bgs/night.mp3"
    scene bg case2_inside3_night at Zoom((1280,720),(0,244,576,324),(149,361,378,212),0.0) with memory
    show anne:
        zoom 1.6 yalign -0.4 xalign 0.5
    anne"그래서 전 스스로에게 솔직해지기로 했어요"
    show anne shy
    anne"그 결과, 이렇게 윌리 옆에 있을 수 있게 됐고, 많은 대화를 나눌 수 있게 됐고……"
    anne"윌리의 알지 못한 점을 알게 된 매우 의미깊은 시간을 보냈다고 생각해요"
    willy"…………"
    anne"저,{cps=2} {/cps}전 윌리를 너무 사랑해요……"
    anne"겨겨겨겨,결혼 하고 싶은 만큼……"
    show anne shock
    anne"하지만 처음부터 그렇게 큰 욕심은 없어요!!"
    show anne shy
    anne"{size=20}연인 부터 라도 좋으니까……{/size}"
    anne"그냥 윌리를 조금이라도 더 알고 싶어요……{cps=2} {/cps}그것도 가까이서……"
    willy_think"앤이……{cps=2} {/cps}나를 좋아한다라……"
    "난 살면서 연애 같은걸 해본적이 없기 때문에 이런거에 대해서 잘 모른다."
    "하지만 만약 앤이 나에게 마음이 있는거라면……{cps=2} {/cps}거기다 날 납치한 이유가 단순히 나랑 같이 있기 위해서라면……"
    "여길 나가는것도 크게 문제되진 않는다."
    willy"만약 너랑 사귄다면……{cps=2} {/cps}날 풀어 줄 수 있어?"
    show anne shock
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}다,{cps=2} {/cps}당연하죠!!{/size}" with lshake
    hide effect1
    stop music
    willy"…………"
    willy_think"망설이지마"
    willy_think"그냥 연애에 불과해……{cps=2} {/cps}가끔씩 통화하고, 같이 돌아다니기만 하면 되는거야"
    willy"좋아……{cps=2} {/cps}너랑 사귈게……"
    show anne
    anne"네……?"
    show anne shock
    play music "bgm/happy2.mp3"
    anne"저저저저 정말이에요?!"
    willy"어"
    willy"이런걸 스톡홀름 증후근 이라고 생각 할 수도 있겠지만……{cps=2} {/cps}너에 대해서 알고 나니까 왠지 마음에 들어서……"
    willy"그리고 솔직히 말해서……"
    willy"널 처음 봤을때……"
    willy"꽤 귀엽다고 생각 했거든……"
    show anne shock2
    anne"나랑 윌리가……"
    anne"사사사사, 사귄다니……"
    anne"나랑 윌리가……{cps=2} {/cps}연애를……"
    "앤은 내가 방금 한 말을 제대로 듣지 못한 듯 하다."
    "……그래도 내가 한 말 중에서 가장 오글거린거라 다행 이라는 생각이 살짝 들었다."
    willy"그래서 말인데……{cps=2} {/cps}이 수갑을 좀 풀어줄 수 있을까?"
    show anne yanshock
    anne"나랑 윌리가……"
    willy"음……"
    stop music
    show anne yantalk
    anne"사랑……{cps=2} {/cps}이라는 건 서로를 알아가는 거죠?"
    willy"갑자기 무슨 소리야……"
    anne"어떻게 생각하세요?"
    willy"확실히 사랑은 서로를 알아가는 게 맞겠지……"
    willy"처음부터 서로를 완벽하게 알 수는 없으니까"
    play music "bgm/sirius5.mp3"
    show anne yan
    anne"근데 전 아직 윌리에 대해서 알지 못한게 많아요……"
    anne"윌리가 지금 제 눈앞에 속박 되어 있는 상태로 무력하게 앉아있고……{cps=2} {/cps}우리 둘은 이제 사귀고 있고……"
    show anne yantalk
    anne"전 윌리가 좀 더 알기 위해서 해보고 싶은 게 많아요……"
    anne"지금 여기서 좀 더 서로를 알아가고 싶어요……"
    anne"제가 입수 한 정보에 의하면, 윌리는 극 심한 \'폐쇄 공포증(Claustrophobia)\'을 앓고 있다고 하던데……"
    anne"극 심하다는 게 어디까지 심한건지 알고싶어요……"
    willy"지금 뭘 할 생각이야?!"
    anne"제가 꽤 큰 박스를 하나 준비 했거든요……{cps=2} {/cps}혹시 들어 가 주실 수 있을까요?"
    show anne yan
    anne"뭐어……{cps=2} {/cps}어차피 거절해도 강제로 넣을 생각 이지만요♡"
    anne"전 윌리의 약한 모습도 정말로 보고 싶거든요!"
    anne"원래 연인간은 서로의 약한 모습을 보여줘도 괜찮은거잖아요?"
    anne"아니, 보여줘야 되는거잖아요?"
    willy_think"폐,{cps=2} {/cps}폐쇄 공포증?!"
    "앤의 말대로 나한텐 극심한 폐쇄 공포증이 있다."
    "일어나지 못할 정도로 낮은 천장이나, 팔을 뻗을 수 없을 정도로 벽이 좁은곳에 있으면……"
    "몇 초도 지나지 않아서 반응이온다."
    "과거에 있었던 일이……{cps=2} {/cps}끊임없이 무한으로 플레쉬백 되고……{cps=2} {/cps}그저 죽고싶다는 생각만 들게 된다."
    willy_think"하지만 그 정보는 어디서 얻은거지?!"
    scene bg case2_inside3_night at Zoom((1280,720),(149,361,378,212),(0,244,576,324),0.5) with dissolve
    show willy shock:
        yalign -0.6 zoom 1.4  xalign 0.0
        linear 0.4 xalign -0.1
    show anne yan:
        zoom 1.4 xalign 1.0 yalign -1.3
        linear 0.3 xalign 0.9
    willy"안 돼……"
    anne"어떻게 해서 윌리가 폐쇄 공포증을 앓게 됐는지도 궁금해요……"
    show willy shock:
        linear 0.4 xalign -0.2
    show anne yan:
        linear 0.3 xalign 0.8
    willy"그만……"
    anne"걱정 마세요……{cps=2} {/cps}순순히 따라주시면 빨리 끝날테니까요"
    play sound "se/hit.ogg"
    show anne yan:
        linear 0.2 xalign 0.0
    $ renpy.pause(0.2)
    scene black with flash
    scene bg case2_outside_night at Zoom((1280,720),(0,0,1280,720),(480,80,647,364),0.8)
    $ renpy.pause(1.0)
    show effect1
    play sound "se/shock.ogg"
    willy"{size=45}으아아아아아─!!{/size}" with lshake
    scene black with Dissolve(1.0)
    stop music
    stop bgs
    centered"30분 후, 할아버지의 저택"
    play music "bgm/smooth2.mp3"
    scene bg mansion_hall_night at Zoom((1280,720),(0,0,1280,720),(905,83,375,211),0.0) with moveright
    show stephan think:
        zoom 1.5 xalign 0.6 yalign -0.3
    stephan_think"도대체 이 금고 너머엔 뭐가 있는 걸까……"
    stephan_think"혹시 내가 읽은 일기장의 구간에서 미리 언급 됐을까?"
    "나는 오늘도 일기장을 늦게까지 읽었다."
    "근데 금고에 관한건 전혀 얻을 수 없었다……"
    "어쩌면 할머니와 할아버지가 같이 결혼한 1960년 부터 읽으면 뭔가 나올지도 모른다."
    "하지만 잘못하면 그 이전에 있었던 중요한 일을 놓치게 된다."
    "조금 귀찮을지도 모르겠지만, 내가 할 수 있는거라곤 일기장을 꾸준히 읽는거 뿐"
    stephan_think"그리고 모래가 토요일 이었지?{cps=2} {/cps}이번 주말엔 여기서 자야지"
    stephan_think"…………"
    stephan_think"그나저나 윌리는 어쩌고 있을까……"
    "내 추리가 맞다면 윌리는 스토커랑 만나다가 봉변을 당했다."
    "그렇다면 같이 데이트를 간 앤 크라운이 범인 인가?"
    "그건 말도 안된다고 생각한다.{cps=2} {/cps}동기를 전혀 알 수 없다."
    "그렇다면 그 애도 윌리와 같은 피해자 일지도 모른다……"
    "범인이 누구건, 단순히 가출 청소년들이 갈 만한 장소를 찾는다고 해서 나오는 건 없을것이다."
    "……난 모든 가능성을 배제하고 싶진 않다."
    stephan_think"근데 애초에 왜 윌리가 납치를 당했을까?"
    "녀석이 뭔가 위험한 일에 연류 되어있는 걸까? 하고 생각 하기도 했지만……"
    play sound "se/think.mp3"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0) # 렌스 시점
    show lance talk with flash:
        zoom 1.5 yalign -0.2 xalign 0.5
    $ renpy.pause(1.5)
    scene bg mansion_hall_night at Zoom((1280,720),(0,0,1280,720),(905,83,375,211),0.0)
    show stephan think with flash:
        zoom 1.5 xalign 0.6 yalign -0.3
    stephan_think"혹시……{cps=2} {/cps}저번 주 토요일에 있었던 일과 관련이 있는가?"
    "만약 그게 사실이라면 과연 나 혼자서 이렇게 머리를 쥐어 짠다고 해서 바뀌는 것이 있을까?"
    play sound "se/think.mp3"
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(161,182,687,386),0.0) with flash
    play bgs "bgs/people.mp3"
    show lisa shock:
        zoom 1.2 xalign 0.3 yalign -2.0
    show stephan talk:
        zoom 1.2 xalign 0.8 yalign -0.2
    stephan"네가 스스로 친구를 찾을지, 아니면 경찰들이 찾을때 가지 기다릴지는 모르겠지만……"
    stephan"난 내가 할 수 있는 걸 다 생각이야"
    stop bgs
    scene bg mansion_hall_night at Zoom((1280,720),(0,0,1280,720),(905,83,375,211),0.0) with flash
    show stephan shock:
        zoom 1.5 xalign 0.6 yalign -0.3
    "……허나 그렇게 보우만 앞에서 폼 잡았으니까 이대로 포기할 순 없다."
    show stephan
    "윌리는 내 친구 이고, 친구가 힘들어하면 도와주는것이 바로 친구의 의무!"
    "왜냐면 걔는 내가 힘들때 많이 도와줬으니까……"
    "거기다 할아버지의 일기는 잘 돌아가고 있으니까 걱정 할 필요는 없고"
    play sound "se/door_open.ogg"
    $ renpy.pause(0.8)
    play sound "se/footsteps_running.mp3"
    $ renpy.pause(1.0)
    cia"세바스찬 씨, 오늘은 장을 늦게까지 보셨네요"
    cia"그보다 표정이 왜그래요?!"
    show stephan talk
    stephan_think"……?"
    scene bg mansion_hall_night at Zoom((1280,720),(905,83,375,211),(0,167,750,422),0.9)
    $ renpy.pause(0.9)
    show seb shock:
        zoom 1.5 xalign 0.0 yalign -0.2
    show cia shock:
        zoom 1.5 xalign 1.0 yalign -0.5
    seb"허어……{cps=2} {/cps}허어……"
    "세바스찬은 양 손에 식재료가 든 검은 비닐봉지를 들고 숨을 헐떡이고 있었다."
    seb"아,{cps=2} {/cps}아무것도 아니에요"
    cia"아무것도 아니긴요!{cps=2} {/cps}오늘은 평상시보다 더 늦게까지 장을 봤잖아요?"
    show cia think
    cia"혹시 폭풍 세일을 하는 바람에 이것 저것 사느라 늦은건가요?"
    show stephan talk:
        zoom 1.5 xalign 2.0 yalign -0.2
        linear 0.3 xalign 1.2
    show cia think:
        linear 0.3 xalign 0.6
    stephan"그런것 치고는 짐이 많은거 같지는 않은데……"
    show cia
    cia"아!"
    show cia smile
    play music "bgm/beat2.mp3"
    cia"오늘도 고양이를 쫓느라 늦은거죠~?"
    show seb blush
    seb"읍……!"
    show stephan shock
    stephan_think"정답?!"
    cia"근데 오늘은 고양이를 몇 마리나 찾았길래 이렇게까지 늦어요?"
    seb"확실히 제가 고양이를 쫓다가 이렇게 늦은 건 사실이지만……"
    extend" 그거 말고 더 있어요!"
    show stephan smile
    show cia talk
    show seb talk
    stephan"혹시 네코미미 로리 소녀 라도 만났어?"
    $ extra_name = '시아 & 세바스찬'
    extra"…………"
    show stephan shock
    stephan"머,{cps=2} {/cps}뭐야……?"
    seb"에헴"
    seb"그런게 아니라, 음침한 폐 건물에서 무서운 비명 소리를 들었어요"
    show cia smile
    cia"오?{cps=2} {/cps}그거 \'미스테리—비전\'에 제보하면 좋겠네요!"
    "참고로 미스테리—비전은 우리나라에서 하는 미스테리를 전문으로 하는 방송 프로그램 이다."
    "……근데 요즘은 걔네들이 아이디어가 없는지, 계속 현실의 귀신 목격 사례만 방송한다."
    cia"거기 보니까 출연료가 빵빵 하던데……"
    show seb think
    seb"지금와서 생각해보니까 그래도 될거 같긴 한데……"
    stephan_think"진짜로 방송 할 생각이었어?!"
    show seb shock
    seb"근데 저도 길을 잃어서 발견 한 장소라서 어딨는지 몰라요!"
    show cia talk
    cia"에이~{cps=2} {/cps}재미 없게"
    stephan"근데 얼마나 고양이를 쫓았길래 길을 잃어버리는거지;;"
    seb"저도 정신차리고 보니까 어두 컴컴한 폐건물 앞까지 와 있더라고요……"
    stop music
    play sound "se/think.mp3"
    play bgs "bgs/night.mp3"
    scene bg case2_outside_night at Zoom((1280,720),(0,0,1280,720),(467,356,647,364),0.0) with flash
    play sound "se/footsteps_running.mp3"
    show seb:
        zoom 1.2 xalign 2.0 yalign -0.2
        linear 0.4 xalign 0.5
    seb"냥냥아~{cps=2} {/cps}우쭈쭈"
    play sound "se/cat_meow.mp3"
    $ renpy.pause(0.7)
    show effect2
    play sound "se/shock2.mp3"
    show seb think
    seb"또 도망가버렸네……"
    seb"근데 여긴 어디지?"
    show seb talk:
        linear 0.5 xalign 0.9
    $ renpy.pause(0.5)
    scene bg case2_outside_night at Zoom((1280,720),(467,356,647,364),(480,80,647,364),0.3)
    show effect1
    play sound "se/shock.ogg"
    $ extra_name = '비명소리'
    play music "bgm/sirius5.mp3"
    extra"{size=45}으아아아아아─!!{/size}" with lshake
    scene bg case2_outside_night at Zoom((1280,720),(467,356,647,364),(467,356,647,364),0.0)
    play sound "se/footsteps_running.mp3"
    show seb shock:
        zoom 1.4 xalign 0.5 yalign -0.2
        linear 0.4 xalign 2.5
    seb"{size=45}히익!!{/size}"
    stop bgs
    scene bg mansion_hall_night at Zoom((1280,720),(905,83,375,211),(0,167,750,422),0.0) with flash
    show seb shock:
        zoom 1.5 xalign 0.0 yalign -0.2
    show cia think:
        zoom 1.5 xalign 0.6 yalign -0.5
    show stephan shock:
        zoom 1.5 xalign 1.2 yalign -0.2
    stephan"…………"
    stephan_think"어떡해?!{cps=2} {/cps}갑자기 나도 무서워졌어!"
    stephan_think"집에 돌아갈때 큰일인데……"
    cia"그러니까─{cps=2} {/cps}이야기를 정리 하자면, 세바스찬 씨는 얼마 전에 들은 무서운 비명 소리 때문에 집에 못 가겠다는 건가요?"
    show cia smile
    cia"설마 세바스찬 씨가 겁이 많을줄 몰랐어요"
    stop music
    show seb talk
    seb"…………"
    show seb
    seb"아,{cps=2} {/cps}아니에요. 전 별로 무섭지 않아요"
    seb"그냥 밤에 나가면 위험하다고 생각 했던거 뿐이에요"
    seb"그러니까 도련님, 집에 돌아가실때 조심 하세요"
    stephan"…………"
    play music "bgm/beat3.mp3"
    show stephan shock2
    stephan"걱정할거 없어!"
    extend" 어렸을때 검도 학원 다녔으니까!"
    "……딱 7개월 만 다녔다.{cps=2} {/cps}그것도 엄청 대충대충"
    show cia
    cia"정말요?"
    cia"와~!{cps=2} {/cps}역시 사람은 생긴걸로만 판단하면 안 되는거네요!"
    show stephan shock
    stephan"그건 무슨 뜻이야?!"
    show cia talk
    cia"그보다 세바스찬 씨 장은 제대로 봤겠죠?"
    stephan_think"무시?!"
    seb"네, 냉장고에 과일이 떨어져서 다 사왔고, 시아 씨가 부탁하신 포테이토칩 치즈맛이랑 파 맛 과자랑 크림치즈 빵이랑……"
    show cia smile
    cia"저한테 주세요!"
    show seb:
        linear 0.3 xalign 0.3
    play sound "se/search_bag.mp3"
    "세바스찬은 시아에게 다가가서 비닐 봉투를 넘기고, 시아는 안에 있던 물건을 하나씩 꺼내기 시작했다."
    cia"흠음흠흠흠~♪"
    show cia talk
    cia"어라?"
    "물건을 꺼내던 손이 갑자기 멈췄다."
    show seb talk
    seb"왜그러세요?"
    cia"안에 크림 치즈 빵이 없는데요?"
    seb"그럴리가요. 제가 분명 제대로 사왔는데……"
    show seb shock:
        linear 0.3 xalign 0.0
    seb"앗……!"
    show cia mad
    seb"어,{cps=2} {/cps}어쩌면 제가 놀라서 달리던 중에……"
    cia"제가 크림 치즈 빵을 {cps=5}어~~~엄청{/cps} 기대하고 있었는데요……"
    seb"대신에 다른 건 전부 무사하니까……"
    cia"내 크림 치즈 빵……"
    cia"지금 당장 나가서 다시 사오세요"
    seb"히익─!"
    seb"하,{cps=2} {/cps}하지만 이 시간엔!"
    show cia mad:
        linear 0.3 xalign 0.3
    cia"24시 편의점에도 팔잖아요?"
    seb"거긴 좀 먼데요……"
    show seb shock:
        linear 0.3 xalign -0.2
    show cia mad:
        linear 0.3 xalign 0.2
    cia"그게 어쨌다고요?"
    cia"저번에도 저의 신성한 야식을 깜빡하더니 오늘도……!"
    cia"제가 야식으로 크림 치즈 빵을 먹지 않으면 어떻게 되는지 아시죠~?"
    play sound "se/footsteps_running.mp3"
    show seb shock:
        linear 0.3 xalign -2.0
    seb"{size=45}죄송합니다─!{/size}"
    play sound "se/door_open.ogg"
    hide seb shock
    "그대로 세바스찬은 밖으로 나갔다."
    "……설마 진짜로 다시 사러 가는 건가?"
    "아니면 그냥 집으로 갔을까?"
    play sound "se/move.mp3"
    stop music
    scene black with moveleft
    $ renpy.pause(0.5)
    play bgs"bgs/night.mp3"
    scene bg sidewalk_night with moveleft
    show stephan shock2:
        zoom 1.6 xalign 0.3 yalign -0.2
    "세바스찬이 무서운 소리를 하는 바람에 나의 귀갓길이 힘들어졌다."
    stephan_think"세상에 귀신은 없어…… 세상에 귀신은 없어……"
    show stephan shock
    stephan_think"하,{cps=2} {/cps}하지만 \'폴터가이스트(Poltergeist)\' 현상 같은 초자연 적인 건 어떻게 봐야 하지?!"
    show stephan shock2
    stephan_think"일단 침착하자……{cps=2} {/cps}귀신은 사람한테 해코지 못할거야"
    stephan_think"왜냐면 내가 죽어서 귀신이 되고 난 뒤 서로 만나면 뻘쭘 할테니까 말이야!"
    stephan_think"분명 그렇겠지?"
    play sound "se/search_bag.mp3"
    "갑자기 어디선가 움직이는 소리가 들렸다."
    show stephan fear
    stephan"{size=45}히익!{/size}" with sshake
    stephan"나,{cps=2} {/cps}난 태권도 초록띠에 검도 노랑띠, 유도 흰띠라고!{cps=2} {/cps}다가오면 큰일날 줄 알아!"
    "…………"
    show stephan shock2
    stephan"후우~"
    "아무래도 아까 들었던 소리는 그냥 바람 때문에 흔들리던 나뭇잎 이었나보다."
    stephan_think"빠,{cps=2} {/cps}빨리 가야겠다"
    play sound "se/footsteps_running.mp3"
    show stephan fear:
        linear 0.5 xalign 2.5
    scene black with moveleft
    stop bgs
    centered"9월 19일 금요일"
    centered"1교시 쉬는시간 직전"
    play music "bgm/beat2.mp3"
    scene bg school_hall with dissolve
    "어차피 윌리가 학교에 나오지 않을거라는 게 확실해진 이상, 걔 폰을 학교에 들고 오는 게 무의미 하다고 생각해서 오늘은 집에 놔두고 왔다."
    "그거만 가지고도 왠지 마음이 한결 가벼워진 것 같았다."
    play sound "se/school2.mp3"
    play bgs "bgs/people.mp3"
    "쉬는 시간을 알리는 종이 울리자마자 학생들이 밖으로 우글우글 모여들기 시작했다."
    play sound "se/footsteps_concrete.mp3"
    show stephan talk:
        xalign -1.0 yalign 1.0
        linear 2.1 xalign 0.8
    "그 중에서 화장실로 향하고 있는 나도 포함 되어있다."
    "……그런데 왠 여자 무리들이 날 둘러싸기 시작했다!"
    scene bg school_hall at Zoom((1280,720),(0,0,1280,720),(665,240,607,341),0.5) with dissolve
    show stephan shock2:
        zoom 1.7 xalign 0.7 yalign -0.2
    $ extra_name ='분장녀'
    "그때 화장을 분장 했다고 할 정도로 진하게 한 여학생이 입을 열었다."
    extra"있잖아~{cps=2} {/cps}혹시 네가 스테반?"
    stephan"으,{cps=2} {/cps}응……"
    extra"오~{cps=2} {/cps}드디어 찾았다!"
    extra"역시 빨간 애를 찾으면 된다는 게 사실 이었구나~"
    $ extra_name = '생각과 치마가 짧은 여자'
    "이번엔 치마를 아주 짧게—교칙 위반 수준으로— 한 여학생이 말했다."
    extra"너 윌리랑 많이 친하잖아?{cps=2} {/cps}혹시 걔가 요즘 학교에 안 나오는 이유 알고 있어?"
    show stephan shock
    stephan_think"역시 여학생이 날 찾으러 온다면 이유는 이거 뿐인가……"
    show stephan shock2
    stephan"나,{cps=2} {/cps}나도 잘은 모르는데……"
    stephan"그냥 뭔가 사고가 나서 장기간동안 입원을 해야 된다는 거 같기도 하고……"
    "일단 그럴싸하게 얼버무렸다."
    $ extra_name = '평범한 여자'
    "특징이 없는 게 특징 일것만 같은 여학생이 입을 열었다."
    extra"정말?"
    extend" 근데 내가 아무리 문자를 보내도 답이 없던데……"
    extra"그거에 대해선 뭔가 아는거 있어?"
    stephan"아니……{cps=2} {/cps}내가 알 리가 없잖아"
    stephan_think"윌리가 납치 당했을 수 있다고 말 할 수는 없고"
    show stephan shock
    stephan"그리고 윌리한테 친구가 나 한명 뿐인것도 아니고, 그냥 다른 애한테 가보는 게……"
    $ extra_name = '분장녀'
    extra"으흠~{cps=2} {/cps}근데 다른 애들한테 가봐도 별로 아는 게 없다던데~"
    extra"맞다 맞다!{cps=2} {/cps}그러고 보니까 옆반에 앤 이었던가?"
    stop music
    extra"걔 가출 했다고 했지?"
    $ extra_name = '평범한 여자'
    extra"그래─{cps=2} {/cps}근데 지금 쯤 어디 있을까?"
    $ extra_name = '생각과 치마가 짧은 여자'
    extra"막 가출하는데 돈이 필요하니까 아저씨들이랑 놀거나 하진 않겠……"
    show stephan talk
    stephan"어이,{cps=2} {/cps}말이 좀 심하잖아"
    $ extra_name = '분장녀'
    extra"오오~?{cps=2} {/cps}왜 갑자기 앤을 감싸는거야?"
    extra"혹시 앤을 좋아 하는 건 아니겠지~?"
    stephan"한번도 만나본적은 없어……"
    show stephan mad
    stephan"하지만……{cps=2} {/cps}뒤에서 남을 욕하는 네녀석들 보단 훨씬 좋은 애라고 생각 하는데?"
    $ extra_name = '생각과 치마가 짧은 여자'
    extra"아,{cps=2} {/cps}아니 난 딱히 걜 욕하려는 의도로 말 한 건 아닌데……"
    extra"그 왜!{cps=2} {/cps}원래 순수하게 생긴 애 일 수록 마음속이 검잖아!"
    $ extra_name = '평범한 여자'
    extra"야, 그건 아무리 봐도 네가 앤을 욕하는 걸로 밖에 안 보여"
    $ extra_name = '생각과 치마가 짧은 여자'
    extra"정말?!{cps=2} {/cps}내 생각이 너무 짧았나봐!"
    $ extra_name = '분장녀'
    show stephan shock:
        linear 0.4 xalign 0.8
    extra"근데 말이야~?"
    "그때 분장녀가 무서운 표정을 지으면서 나에게 다가왔다."
    play music "bgm/sirius5.mp3"
    extra"너 말이 좀 띠껍다?"
    extend" 방금 \'네녀석들\'이라고 했잖아~?"
    play sound "se/heartbeat.mp3"
    stephan_think"…………"
    extra"왜 갑자기 눈을 피하는거야~?"
    play sound"se/static.mp3"
    show black
    $ renpy.pause(0.3)
    hide black
    extra"좀 똑바로 봐 봐!"
    "여자는 날 잡아 먹으려는 표정을 지으면서 목소리를 높였다."
    "갑자기 다리가 떨리고……{cps=2} {/cps}심박수가 증가했다."
    "중학교때 있었던 일 이랑 뭔가 비슷했다."
    play sound "se/think.mp3"
    scene black with flash
    $ extra_name = '일진 #1'
    extra"이 새끼, 방금 나보고 뭐라고 했냐?"
    stephan"그,{cps=2} {/cps}그냥……"
    extend" 복도에 껌을 뱉으면 안된다고……"
    extra"그래─{cps=2} {/cps}아주 착해서 잘~났다"
    extra"그러고보니까 얘, 자기가 명탐정 이라고 나대던 녀석 아니었던가?"
    stephan"…………"
    $ extra_name = '일진 #2'
    extra"옛날엔 탐정 이었고……{cps=2} {/cps}지금은 뭐냐?{cps=2} {/cps}환경 미화원?"
    extra"넌 그런짓 하면 쪽팔리지도 않냐?"
    play sound "se/shock.ogg"
    extra"시발,{cps=2} {/cps}눈 똑바로 쳐다보라고!"
    stephan"……!"
    $ extra_name = '일진 #1'
    extra"이딴 관종은 놔두고 다시 돌아가자"
    $ extra_name = '일진 #2'
    extra"복도에 껌 뱉는 게 떫으면 네가 치워"
    extra"진짜 기분 잡쳤네"
    stephan"…………"
    stop music
    $ extra_name = '목소리'
    extra"얘들아"
    scene ev willy_mid with dissolve #중학교때 교복을 입고 있는 윌리가 인상을 쓰며 말 함
    extra"계속 듣자 하니까 좀 너무한거 같은데?"
    "나랑 윌리가 처음 만났을때……"
    scene black with eyeshut
    $ renpy.pause(0.2)
    scene white with eyeopen
    scene bg school_hall at blur with Dissolve(1.0)
    show lisa mad at blur:
        zoom 1.3 xalign 2.5 yalign -0.2
        linear 0.4 xalign -1.0
    show effect1
    play sound "se/shock.ogg"
    lisa"{size=45}이것들이 뭔짓이야?!{/size}" with lshake
    $ extra_name = '여자 3인'
    extra"리사?!"
    "어디선가 보우만이 달려왔다."
    "……왠지 모르게 윌리랑 겹쳐보게 됐다."
    lisa"지금 애가 울면서 까지 싫어하잖아!"
    hide effect1
    stephan_think"내가……?"
    show black with eyeshut
    show bg school_hall
    show lisa mad:
        zoom 1.3 xalign 0.5 yalign -0.2
    $ renpy.pause(0.5)
    hide black with eyeopen
    "난 눈을 한 번 깜빡 거렸는데……{cps=2} {/cps}뭔가 촉촉한게 내려오는 느낌이 있었다."
    "아무래도 과거 트라우마의 플래쉬 백 때문에 무의식적으로 눈물이 나왔나보다……"
    "게다가 완전 울상 까지 돼버렸고……{cps=2} {/cps}쪽팔려"
    $ extra_name = '분장녀'
    extra"엇!{cps=2} {/cps}미안……"
    extra"딱히 울릴 의도는 아니었는데……"
    lisa"너희 둘도 얼른 사과 해"
    $ extra_name = '평범한 여자'
    extra"왜 나까지?{cps=2} {/cps}아무것도 안 했는데?!"
    $ extra_name = '분장녀'
    extra"그냥 리사가 시키는데로 사과 해!"
    $ extra_name = '여자 둘'
    extra"미,{cps=2} {/cps}미안……"
    show lisa smile
    lisa"좋아~{cps=2} {/cps}좋아~"
    play sound "se/footsteps_running.mp3"
    "사과를 끝으로 여자 세명은 즉시 현장을 떳다."
    play music "bgm/happy2.mp3"
    show lisa talk with dissolve:
        zoom 1.8 xalign 0.5 yalign -0.2
    lisa"토머, 싫으면 싫다고 확실히 말 해"
    stephan"으,{cps=2} {/cps}응?!"
    stephan"뭔가 말이 이상한데?!{cps=2} {/cps}그리고 나 아무 문제도 없다고!"
    lisa"방금전까지 울고 있었잖아"
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}딱히 내가 울거나 한 건 아니다!{cps=2} {/cps}바보!{/size}" with lshake
    hide effect1
    "내가 여자애들이 한 말에 울었다는 사실을 숨기기 위해서 아무렇게나 말 했는데……{cps=2} {/cps}본의치 않게 츤데레 같은 대사가 나왔다……"
    show lisa mad
    lisa"방금전까지 널 도와준 은인한테 바보가 뭐냐!"
    stephan"어,{cps=2} {/cps}어쨌건, 난 울지 않았어!"
    stephan"알겠지?!"
    show lisa smile2
    lisa"즉, 네가 여자들 앞에서 질질 짰다는 사실을 비밀로 해달라는 거지~?"
    stephan"윽……!"
    lisa"공짜론 힘들거 같은뎅~?"
    "젠장, 녀석한테 약점을 잡혀버렸다."
    lisa"내 입의 무게는 보상의 가치에 비례 한다구!"
    stephan"으……"
    extend" 뭘 원하는거지?"
    show lisa
    lisa"방과후에 밥이라도 사"
    show lisa smile
    lisa"딱히 널 상대로 협박 하거나 하고 싶진 않으니까"
    stephan"그,{cps=2} {/cps}그래!"
    "보우만이 나쁜 애는 아니라서 다행이다."
    "……하지만 방금 전에 있었던 여자 3명은 어떨련지"
    stephan_think"내가 여자 때문에 운 찌질이 라는 소문이 돌면 좀 곤란한데……"
    stephan_think"그보다 화장실 이나 빨리 가야겠다"
    stop bgs
    stop music
    scene black with moveup
    centered"오후 5시 20분"
    centered"UFC 치킨 집"
    play music "bgm/happy1.mp3"
    play bgs "bgs/people.mp3"
    scene ev fastfood_sit with dissolve
    show lisa:
        zoom 1.8 yalign -0.1 xalign 0.9
    "나는 방과후에 보우만에게 햄버거를 사주기로 했다."
    "남자가 자신을 구해준 여자 은인에게 주는 음식이 뭐 그거냐고 생각 할지도 모르겠지만……"
    "이건 보우만 스스로가 가자고 한거다."
    stephan"근데 네가 햄버거를 좋아 할 줄이야……"
    show lisa talk
    lisa"왜?{cps=2} {/cps}떫냐?"
    stephan"아니, 나도 햄버거를 엄청 좋아해서"
    show lisa smile
    lisa"오?!{cps=2} {/cps}이거 우리 둘이서 좋은 친구가 될 수 있겠군!"
    stephan_think"친구라……"
    "생각해보니까 고등학교로 올라 온 뒤론, 윌리 외에는 제대로 사교 활동을 해보지 못한 거 같다."
    show lisa
    lisa"집에서 부모님이 \'너, 이런거 먹으면 살찐다!\'라고 하니까 정말 짜증나더라고"
    lisa"그래도 난 매일매일 땀이 날 정도로 운동을 하니까 살찌거나 하진 않지"
    stephan"어쩐지 나도 살이 잘 안찌더라"
    show lisa talk
    lisa"너도 운동 해?"
    stephan"그럼!{cps=2} {/cps}매일매일 땀나는 스포츠를 즐긴다고"
    show lisa smile2
    lisa"정말 의외네?"
    lisa"그럼 언젠간 축구부에 와!{cps=2} {/cps}내가 상대해줄테니까!"
    stephan"자,{cps=2} {/cps}잠깐……"
    show lisa smile
    lisa"내가 정말 토머를 너무 얕잡아 봤나보네……!"
    lisa"생긴게 너무 여성 스러워서 운동과는 거리가 전혀 멀거라 생각 했거든"
    stephan"그,{cps=2} {/cps}그럼!"
    stephan"나도 사나이니까!{cps=2} {/cps}당연히 끓어 넘치는 파워를 푼다고!"
    lisa"그럼 다음주에 나랑 같이 농구로 승부 해볼래?"
    stephan"노,{cps=2} {/cps}농구?!"
    lisa"응!{cps=2} {/cps}아쉽게도 여긴 농구부가 없지만, 나 사실은 농구가 특기거든"
    lisa"지는 사람은 이온음료 대짜 사오기!"
    extend" 어때?"
    stephan"나,{cps=2} {/cps}난 초보자니까 살살 부탁할게……"
    lisa"그래!"
    stephan_think"이거, 어떻게든 승부는 피해야겠군"
    show lisa smile2
    lisa"참고로 승부에 참석하지 않으면 운동장 10바퀴"
    show effect2
    play sound "se/shock2.mp3"
    stephan"히익!"
    "망했다!{cps=2} {/cps}내가 매일매일 땀나게 하는 스포츠가 사실은 \'e스포츠(eSports)\'라고는 못 말 하게 됐다!"
    "그,{cps=2} {/cps}그냥 운동 하는 건가……"
    hide effect2
    show lisa talk
    lisa"근데 너 아침에 무슨 일이 있었어?{cps=2} {/cps}막 눈물까지 흘리던데"
    stephan"그,{cps=2} {/cps}글쎄 안 울었다니까!"
    stephan"그냥 눈에서……"
    stephan"그보다 네가 알아서 뭐하게?!"
    show lisa talk
    lisa"딱히 어떻게 하겠다는 건 아니고……"
    lisa"혹시 내가 도움이 될 수 있을까 해서"
    stephan"…………"
    play sound "se/think.mp3"
    scene ev willy_mid with flash
    $ renpy.pause(0.5)
    scene ev fastfood_sit with flash
    show lisa:
        zoom 1.8 yalign -0.1 xalign 0.9
    "그때 있었던 일은 아주 생생하게 기억한다."
    "가장……{cps=2} {/cps}떠올리기 싫었을때……"
    stephan"별로 말 하고 싶진 않은데……"
    show lisa smile
    lisa"그렇게 계속 마음속에 가둬두는 것보단, 밖으로 내뱉는 게 더 시원해!"
    lisa"다른 사람들한테 까발리거나 할 생각은 없으니까 걱정 하지말고"
    "짜증난다……{cps=2} {/cps}저런식으로 남일 같이 쉽게 말 하는 \'방관자\'들은……"
    show lisa smile2
    lisa"솔직히 네가 눈물을 흘릴 정도로 큰 일이라면 빨리 해소하고 싶을텐데……"
    stop music
    show effect1
    play sound "se/shock.ogg"
    show lisa shock
    stop bgs
    stephan"{size=45}그만해!{/size}" with lshake
    stephan"넌 그렇게 남 일처럼 쉽게 보고 있겠지만, 일을 당한 내 입장에선그걸 떠올리는 게 얼마나 힘든지 알아?"
    hide effect1
    lisa"…………"
    "나의 갑작스런 행동 때문에 순간 정적이 흘렀다."
    lisa"미안……"
    lisa"그냥 너한테 조금이라도 도움이 되지 않을까 생각했는데……"
    stephan"…………"
    play music "bgm/sad2.mp3"
    stephan"아, 아무튼. 알았으면 됐어"
    scene black with Dissolve(1.0)
    "중학교때 나는 조금 어려운 학교생활을 하고 있었다."
    "과거에 내가 스스로를 \'명탐정 스테반\'이라고 칭하면서 돌아다녔던것도 원인 중 하나이지만……"
    "일단 남들이랑은 잘 어울리지 못하는 성격이 가장 큰 이유였다."
    "내가 남들이랑 어울리지 못해서 친구는 없었지만, 그래도 남들에게 대놓고 괴롭힘을 받았던 적은 그리 없었다."
    "하지만 내가 중학교 3학년 이었을때……"
    "학교에서 좀 잘나가는─소위 말 하는 \'일진\'들이 학교 복도에 껌을 뱉는 걸 보고 뭐라고 지적 했을때 일이 발생 했던거다."
    $ extra_name = '일진 #2'
    extra"옛날엔 탐정 이었고……{cps=2} {/cps}지금은 뭐냐?{cps=2} {/cps}환경 미화원?"
    scene ev willy_mid with Dissolve(1.0)
    "그러다 당시 우리 학교로 막 전학 온 윌리가 나를 구해줘서……{cps=2} {/cps}나랑 윌리가 친해졌다 랄까……"
    "뭐가 어쨌건, 나한텐 별로 좋은 기억이 아니었다."
    play bgs"bgs/people.mp3"
    scene ev fastfood_sit with dissolve
    show lisa shock:
        zoom 1.8 yalign -0.1 xalign 0.9
    stephan_think"하지만 그게 딱히 보우만의 잘못은 아니니까……"
    stephan"아까 화내서……{cps=2} {/cps}미안……"
    lisa"아니야!{cps=2} {/cps}나야말로 아무런 생각도 없이 그렇게 말 해서 미안한걸!"
    show lisa talk
    lisa"솔직히 말해서, 네가 아까 복도에서 울었던게 엄청나게 걸렸거든"
    show lisa shy
    lisa"넌 나랑 처음 만났을때도 앤을 찾는데 열심히 도와줬는데……{cps=2} {/cps}나도 뭔가 해줄 수 있는 게 없을까 싶어서……"
    stephan"그건 네가 따로 걱정하지 않아도 잘 되고 있어"
    "물론 가장 중요한 \'그들이 어디 있는가\'는 아직 해결되지 않은 상태지만……"
    lisa"그, 그런가"
    lisa"…………"
    stephan"…………"
    "나는 대화의 끝으로 다 식어버린 치킨 조각을 한 입 먹었다."
    show lisa
    lisa"아!{cps=2} {/cps}나 좋은거 떠올랐다!"
    stephan"……?"
    show lisa smile
    lisa"너 긍지높은 닭을 뭐라 하는지 알아?"
    stephan"뭔데?"
    show lisa smile
    stop music
    lisa"프라이드 치킨!"
    stephan"…………"
    show lisa shock
    lisa"……!"
    stephan"못 들은걸로 해 줄게"
    show lisa shy
    lisa"고,{cps=2} {/cps}고마워"
    "방금전까 돌았던 어색한 공기를 어떻게든 하겠다는 의도로 친 드립 인거 같은데……"
    "너무 심했다."
    "오히려 이거때문에 더 심하게 뻘쭘해진거 같았다."
    lisa"…………"
    stephan"…………"
    play music "se/phone_ring.mp3"
    "그때 보우만이 친 개드립 때문에 생겨난 정적을 깨며 전화 한통이 왔다."
    stephan"나한테 전화가?"
    play sound "se/search_bag.mp3"
    "나는 주머니에서 휴대폰을 꺼내 확인 하려고 했는데……"
    stop bgs
    play sound "se/think.mp3"
    scene phone_unknown with flash
    $ renpy.pause(1.0)
    stephan"어?!"
    play sound "se/think.mp3"
    show phone_unknown at Zoom((1280,720),(0,0,1280,720),(298,136,457,257),0.0) with flash
    show phone_unknown at Zoom((1280,720),(298,136,457,257),(704,313,457,257),1.5)
    $ renpy.pause(2)
    show phone_unknown at Zoom((1280,720),(298,136,457,257),(0,0,1280,720),0.5) with dissolve
    "발신번호 표시제한으로 걸려왔다."
    "왠지 불안한 기분이 내 등골을 타고 내려왔다."
    stephan_think"……일단 받아야겠지?"
    play bgs"bgs/people.mp3"
    scene ev fastfood_sit with dissolve
    show lisa talk:
        zoom 1.4 yalign -0.2 xalign 0.85
    show phone:
        yalign 10.0 xalign 0.9
        linear 1.0 yalign 1.5
    stop music
    stephan"여보세요……?"
    $ extra_name = '통화 상대'
    extra"혹시 스테반 토머 인가?"
    "수화기 너머로 뭔가 어두운 남성의 목소리가 들려왔다."
    stephan_think"그보다 내 이름을 알고 있다니……"
    stephan"지금 누구죠?"
    extra"내가 누군진 중요하지 않아"
    play music "bgm/sirius3.mp3"
    extra"중요한 건……{cps=2} {/cps}난 윌리가 어디 있는지 알고 있어"
    stephan"……!"
    "나도 모르게 숨을 삼켜버렸다."
    stephan_think"윌리……"
    "이 사람은 누구지?{cps=2} {/cps}혹시 범인?"
    "왠지모르게 위험한 느낌이 들었다."
    lisa"갑자기 왜그래?"
    show phone:
        linear 0.3 yalign 7.0
    "나는 반사적으로 휴대폰을 숨겼다."
    "보우만 한테 숨길 필요는 딱히 없을지도 모르겠지만……"
    "혹시 윌리랑 앤이 납치 됐을지도 모른다는 사실을 알게 되면 괜한 걱정을 사게 될거다."
    "우선은 통화 상대랑 천천히 얘기를 한 뒤에 보우만에게 알릴지 말지 판단 해야겠다."
    stephan"나,{cps=2} {/cps}나 잠깐만 화장실에 다녀 올게"
    play sound "se/footsteps_running.mp3"
    scene black with moveright
    stop bgs
    $ renpy.pause(0.5)
    scene bg fastfood_bathroom with moveright
    show phone:
        yalign 10.0 xalign 0.9
        linear 1.0 yalign 1.5
    "다시 폰을 들고 연락을 재개했다."
    stephan"여보세요?"
    extend" 방금 윌리가 어디있는지 알고 있다고 했죠?!"
    extra"그래"
    extra"길게 말 하진 않고, 요점으로 바로 넘어 가도록 하지"
    extra"난 네가 원하는 정보—윌리의 위치를 알고있다.{cps=2} {/cps}그렇지?"
    stephan"그래요"
    extra"그리고 넌 내가 원하는 물건을 가지고 있어……"
    stephan"원하는 물건을……{cps=2} {/cps}내가 가지고 있다고……?"
    extra"그래"
    "무슨 물건일까?"
    "내가 가지고 있는 것 중에서 이렇게 위험해 보이는 사람이 원할만한게 뭘까……"
    stephan"도대체 무슨 물건이죠?"
    extra"후후후……"
    extra"그 보다 어쩔거지?{cps=2} {/cps}윌리의 위치와 내가 원하는 물건……"
    extra"나랑 거래를 할 건가?"
    stephan"우선 물건의 이름을……"
    extra"이름이 뭐가 중요하겠어?{cps=2} {/cps}네 하나뿐인 친구의 목숨이 달려 있을 수도 있다고?"
    stephan"큭……"
    "너무 불안했다."
    "확실히 윌리는 내 친구다."
    "그런 친구가 며칠전 부터 위기에 빠진 듯 했고, 지금 나한테 그 친구의 위치를 알려준다는 전화가 왔다."
    "다만 상대방이 원하는 물건……{cps=2} {/cps}무슨 물건이간에, 사람의 목숨보다 소중한 건 없다."
    "……하지만 여기서 내가 상대방이 원하는 걸 모른체 제안하는 거래를 받아들이면 난 그 사람의 노예가 되는거나 마찬가지"
    "이땐 신중해야한다."
    stephan"내가 그쪽에게 있어서 소중한 물건을 가지고 있다고 했는데……{cps=2} {/cps}당신에겐 그게 윌리의 목숨보다 소중 하다는 뜻이겠지?"
    extra"호오?{cps=2} {/cps}지금 거래의 주도권을 손에 넣겠다는 건 가?"
    extra"하지만 넌 내가 뭘 원하는지 모르고있어……{cps=2} {/cps}협박을 할거면 일단 정보부터 모아 꼬맹아"
    "꼬맹이 라……{cps=2} {/cps}내 번호를 알고 있었던 것도 그렇고, 상대방은 나의 개인 정보에 대해서 잘 알고있을 확률이 있다."
    "반대로 생각한다면 나랑 접점이 있는 인물……{cps=2} {/cps}혹은 윌리를 통해서 날 알았다."
    stephan_think"슬슬 정보가 모이는군"
    stephan"당신이 뭘 원하는지 몰라선 판단 할 수가 없겠는데?"
    extra"네 친구의 목숨이 달렸어, 생각의 여지가 있을까?"
    "상대방은 윌리 근처에 있는 건가?"
    stephan_think"만약 그게 사실이라면 정말 위험해!"
    "정말 그 자리에서 윌리를 즉시 죽일 수 있다면……{cps=2} {/cps}이 승부는 내가 졌을 수도 있다."
    stephan"젠장……"
    extra"지금 상황이 어떤지 이해 했지?"
    "상대방이 뭘 원하는 진 전혀 모르겠지만……{cps=2} {/cps}이대로……"
    stephan"그래……{cps=2} {/cps}네가 원하는 물건은 도대체 뭐야……"
    "상대방이 원하는 게 정확히 뭔지 모른 상태로 난 동의했다."
    extra"내가 원하는 것……"
    extra"그것은……"
    extend" 바로 PX4……"
    stop music
    play sound "se/hit.ogg"
    extra"아얏!"
    "꽤나 찰진 소리가 났다."
    play music "bgm/beat3.mp3"
    extra"지금 나한테 무슨짓을 하는거임?!"
    $ extra_name = '다른 목소리'
    extra"{size=20}대화에 진전이 없었던 거 같던데, 이유가 고작 그거였냐……{/size}"
    "전화기로부터 멀리서 말 하고 있는지, 목소리가 작게 들렸다."
    $ extra_name = '통화 상대'
    extra"고작이라고?!{cps=2} {/cps}내가 그 PX4 때문에 잠도 제대로 못잤단 말이야!"
    $ extra_name = '다른 목소리'
    extra"{size=20}하루종일 게임 하고 있었으니까 당연하지{/size}"
    $ extra_name = '통화 상대'
    extra"중요한건 그게 아니라 내 PX4를 가져간 놈의 번호가 지금 내 수중 안에 있다는거임!"
    extra"어떻게 해서든 다시 받아내야……"
    play sound "se/hit.ogg"
    extra"(퍽)"
    extra"아야!"
    $ extra_name = '다른 목소리'
    extra"{size=20}그보다 윌리가 있을 것 같은 위치나 전해{/size}"
    $ extra_name = '통화 상대'
    extra"힝……"
    extra"여,{cps=2} {/cps}여보세효↗?"
    stop music
    extra"에헴,{cps=2} {/cps}여보세요?"
    "상대방은 목소리가 갈라졌던 걸 없었던 척 하며 다시 진지하게 말 하기 시작했다."
    extra"아직 있나?"
    "방금전까지의 실랑이를 듣고 나니까……{cps=2} {/cps}너무 맥이 풀렸다."
    "PX4를 원하는 것도 그렇고, 내 번호를 안 것도 그렇고……"
    "100\%의 확률로 윌리의 룸메이트다."
    stephan"윌리의 룸메이트 되시죠?"
    extra"윽!"
    extra"그래……{cps=2} {/cps}그리고 방금전에 거래 얘기는 전부 장난이었어……"
    stephan_think"허어─{cps=2} {/cps}윌리의 안부를 물으려 번호를 남겼더니 PX4의 원한을 풀다니……"
    stephan_think"잠깐만……"
    play music "bgm/sirius1.mp3"
    "전개가 너무 허무맹랑하게 끝나서 그런지 잠깐 잊었지만, 상대방은 지금 윌리가 납치된 걸, 그것도 위치까지 알고있다고 했다."
    stephan"윌리의 위치를 알고 있다고 하셨는데……{cps=2} {/cps}설마 그것도 장난 이거나 하진 않겠죠?"
    extra"아니!{cps=2} {/cps}절대 아니야!"
    extra"다만……"
    stephan"다만……?"
    extra"나도 정확한 위치는 몰라. 그냥 있을거라 추정되는 장소가 몇 곳 있을 뿐"
    "갑자기 정신이 밧짝 들었다."
    "정확한 장소는 아니더라도, 있을거라 추정되는 장소!{cps=2} {/cps}이건 엄청난 진전이다!"
    "윌리가 납치된 장소만 알게 된다면 나머진 경찰에게 신고해서 사건을 깜끔하게 끝내면 된다."
    "마침 앤 크라운이 가출을 해준 덕분에, 크라운을 목격 했다고 말 하면 바로 움직여 줄 터!"
    "그런데……"
    "몇 가지가 이상한게 있었다."
    "첫째, 어떻게 해서 이 사람은 윌리의 위치—로 추정되는 장소—를 알고 있는가?"
    "둘째, 본인이 알고 있었으면 먼저 가거나 경찰에게 신고를 하지, 왜 나한테 알려주는가?"
    extra"혹시 폰 기종이 뭐야?"
    stephan"저기……{cps=2} {/cps}물어보고 싶은 게 있는데 괜찮을까요?"
    extra"어?"
    extend" 뭐어 내가 대답 할 수 있는 한에선 ㅇㅋ"
    stephan"어떻게 해서 윌리가 있을거라 추정되는 장소를 찾았죠?"
    extra"그건 윌리가 있을법 한 후보지들을 본 다음에 알아서 추리 해보시지?"
    extra"솔직히 요즘같은 정보화 시대에서 불가능한 건 없다고"
    "저 대답이 오히려 더 많은 의문점을 낳았다."
    stephan_think"혹시 뒷 세계 정보원 같은거라도 있는 건가……"
    stephan"그럼 또 질문이 있어요"
    stephan"왜 번거롭게 저한테 주소를 주는거죠?{cps=2} {/cps}그냥 이 위치에 사람이 납치 됐다고 경찰들한테 신고 하면 더 빨리 끝날 거라 생각 하는데……"
    extra"그건……"
    extra"내가 이 정보를 입수한 경로가 경찰들에게 알려지면 좀 곤란 한 것도 있고……"
    stephan_think"위험 하다니, 정말로 뒷 세계 정보원 이라도 있는겨?!"
    extra"윌리가 자기의 신호가 떨어지기 전까진 절대로 나가거나 다른 행동을 하면 안된다고 하니까 어쩔 수 없지……"
    extra"저번에 살짝 어겼다가 내 PX4가 날라가버렸다고!"
    extend" 이번에도 어기면 뭐가 날라가게 될지…… 으으……"
    extra"내가 녀석한테 특별히 부탁 받은거라곤 \'결석 하게 될 경우 병결로 처리\'해 달라는 거 뿐이고……"
    extra"정말 자신이 무능력하게 느껴졌어……"
    stephan_think"그래서 윌리가 학교에선 병결로 알려졌구나……"
    extra"그래도 처음엔 그냥 시키는데로 학교에 전화를 하고, 가만히 집에서 손가락이나 빨면서 기다리고 있었지"
    extra"그런데 걔가 며칠이 지나도 아무런 소식이 없는거야"
    extra"계속 불안해 하던 참에 네가 우리집 앞에 번호를 남겼더라고, 그래서 번쩍 하고 아이디어가 떠올랐지"
    extra"혹시 윌리가 좀 빠져 나올 수 없는 상황에 놓였을때를 대비해서 널 보낸다.{cps=2} {/cps}이렇게 하면 난 아무것도 안 했으면서 뭔가를 한게 되니까"
    extra"게다가 윌리 말론 네가 멜 누나를 구하는데 도움이 됐다는거 같더라?"
    extra"정말 최적의 상대라고 생각 했……"
    show phone:
        linear 0.4 yalign 10.0
    "멜 누나……"
    play sound "se/static.mp3"
    scene bg police_meeting at Zoom((1280,720),(430,231,495,279),(430,231,495,279),0)
    show lance talk:
        zoom 1.5 yalign -0.2 xalign 0.5
    $ renpy.pause(0.5)
    scene bg fastfood_bathroom
    show phone:
        xalign 0.9 yalign 10.0
    "순간 내 머리에 한가지 생각이 스쳐 지나갔다."
    "\'왜 윌리가 납치 됐는가\'"
    show phone:
        linear 0.4 yalign 1.5
    stephan"저기!"
    extra"ㅇ?"
    stephan"윌리가 납치 된 이유……"
    extend" 혹시 렌스 클라크랑 관련 있나요?"
    extra"……!"
    "숨을 삼키는 소리가 들렸다."
    "상대방은 지금 당황하고 있다."
    stop music
    show phone:
        linear 0.5 yalign 10.0
    stephan_think"그럼 정말로……{cps=2} {/cps}윌리는 마르쿠스 고드윈 이라는 사람을 찾으려고 하다가……"
    "솔직히 조금은 예상했다.{cps=2} {/cps}\'법과 경찰을 뛰어넘는다\'고 할 정도로 위험해 보이는 사람을 없애겠다고 선언 했으니까"
    stephan_think"만약 내가 윌리를 찾아 나서게 된다면 나도 함께 위험한 일에 관여 될 수도 있는데……"
    extra"솔직히 말 해서 말이야……"
    extra"네 질문에 대답하기 귀찮으니까, 윌리를 찾으면 걔한테 직접 물어봐"
    stephan_think"…………"
    extra"뭐야? 왜 갑자기 대답이 없어?"
    "나는 과연 윌리를 구하러 갈 수 있을까……"
    stephan_think"…………"
    "내가 윌리를 찾으러 갔다간 위험한 일에 연류될 확률이 있다."
    "만약 그렇게 된다면 상대방은 권력이 꽤 높다고 생각 되는 마르쿠스 고드윈."
    "그럼 남들에게 도움을 청하는것도 힘들어 지게 된다……"
    play sound "se/think.mp3"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(531,286,553,312),0.0) with flash# 스테반이 윌리에게 가까이옴
    show willy talk:
        zoom 1.4 yalign -0.3 xalign 0.8
    show stephan sirius:
        zoom 1.4 yalign -0.3 xalign 0.35
    willy"내가 바꿀 수 있다는 사실을 알면서 모른척 할 순 없어"
    show willy
    willy"안 그러면 죄책감이 들잖아?"
    scene ev willy_mid with flash #중학교때 교복을 입고 있는 윌리가 인상을 쓰며 말 함
    willy"계속 듣자 하니까 좀 너무한 거 같은데?"
    scene bg fastfood_bathroom with flash
    show phone:
        xalign 0.9 yalign 10.0
    stephan_think"젠장……"
    stephan_think"왜……{cps=2} {/cps}왜 녀석의 말은 항상 정답 처럼 들리는거냐고?!"
    play music "bgm/sirius2.mp3"
    "난 살면서 녀석한테 몇번이고 도움을 받아왔다."
    "……그렇다면 나도 도와주는거다."
    "만약 나중에 위험한 일에 처하게 된다면, 그때도 윌리가 도와줄테니까"
    show phone:
        linear 0.3 yalign 1.5
    stephan"알겠어요"
    extra"좋아,{cps=2} {/cps}그럼 얼른 네 폰 기종을 알려줘"
    stephan"제 폰 기종은 왜요?"
    extra"지금부터 내가 이메일로 지도 좌표값을 보낼 생각이거든"
    extra"폰 기종에 따라서 사용하는 지도 프로그램이 다르다 보니까 맞춰야 해서"
    stephan"굳이 그렇게까지 해야되나요?"
    extra"알고보면 그렇게 하는 편이 훨씬 깔끔하고 쉬워"
    stephan"네에……"
    stephan"전 아이퐁 5S 써요"
    extra"아이퐁이면, eyeOS란 말이지……"
    "저쪽에서 키보드 치는 소리가 작게 들렸다."
    extra"이번엔 네 이메일을 알려줘"
    "난 이메일을 알려줬다."
    extra"흠……"
    extra"좋았어, 보냈다"
    extra"메일에 걸린 링크를 클릭하면 자동으로 아이퐁 지도에 위치 두개가 마킹 될거야"
    stephan"음……"
    extra"잠깐!{cps=2} {/cps}지도를 확인하기 전에 몇가지 당부할게 있어"
    stephan"뭐죠?"
    extra"첫째, 절대 경찰에게 신고하지 말 것"
    extra"아까 말했듯이 내가 그 주소를 얻은 경로가 좀 거시기 해서 말이야……"
    extra"두번짼……{cps=2} {/cps}절대로 윌리한테 내 얘기를 하지 마"
    extra"……내가 시키지도 않은 일을 했다는 게 알려지면 다음엔 PX4보다 더 큰게 없어 질 수 있을지도 모르니까"
    stephan_think"그쪽이 걱정인거냐!"
    extra"그럼 ㅂ2"
    stop music
    play sound "se/phone_end.mp3"
    $ renpy.pause(1.0)
    "상대방은 전화를 끊었다."
    show phone:
        linear 0.5 yalign 10.0
    stephan"후우─"
    "나도 모르게 다리에 힘이 풀렸다."
    stephan_think"일단 위치부터 확인 해봐야겠다"
    show phone with dissolve:
        xalign 0.5 yalign 0.5
        linear 0.4 zoom 2.5
    scene black with Dissolve(1.0)
    "나는 메일로 온 링크를 클릭했다."
    "그랬더니 전화에서 말했던데로 지도 앱이 열리더니, 총 두곳에 핀이 지정 됐다."
    "첫번째 위치는 시장에서 조금 떨어진 외딴 지역"
    "마지막 주소는……"
    play music "bgm/sad2.mp3"
    extend" 우리 집"
    scene bg fastfood_bathroom with eyeopen
    show stephan shock:
        zoom 1.7 xalign 0.5 yalign -0.2
    stephan_think"왜 리스트 중에서 우리 집이 있는거지?!"
    show stephan think
    "이럴땐 냉정하게 생각해보는거다.{cps=2} {/cps}어쩌면 이 위치에 숨겨진 비밀이 있을지도 모르니까"
    "도대체 어째서 윌리가 납치 되어 있을거라 생각 한 장소 중 한 곳에 우리집이 있는 걸까?"
    stephan_think"혹시 윌리의 룸메이트 라는 사람은 내가 범인 이라고 생각 하고 있는 건가?!"
    "아니야, 그렇다면 방금 같이 전화를 하진 않을거다."
    "그 사람이 했던 말도 그렇고, 일부러 이메일을 통해서 이런 복잡한 링크를 만든 걸 보면, 상대방은 상당한 컴퓨터 실력자 일지도 모른다."
    stephan_think"어쩌면……{cps=2} {/cps}윌리의 폰이 있는 위치를 표시한 걸까?"
    "그렇게 생각하면 왜 우리 집이 후보지 중 한 곳인지 설명이 된다."
    "난 오늘 윌리가 학교에 나오지 않을 걸 알고 있었기 때문에 폰을 집에 놔두고 왔으니까"
    "하지만……{cps=2} {/cps}그러면 첫번째 위치인 시장에서 조금 떨어진 곳은 뭐지?"
    "혹시 윌리가 폰을 두개 가지고 있는 걸까?{cps=2} {/cps}하지만 보통 사람은 두개 가지고 다니질 않을텐데……"
    "우리 집엔 윌리가 있을 법한 위치를 알리는거라곤 폰 하나 뿐이다."
    "그 외엔 아무것도 없다."
    show stephan yawn
    stephan_think"이래하든, 저래하든. 우리 집엔 윌리가 있을리가 없으니까 갈 필요는 없어"
    "어쩌면 윌리한테 위험 한 일이 벌어지고 있을지도 모르니까, 빨리 행동하는 게 좋을거라 생각해. 시장에서 좀 떨어진 천번째 위치로 가보기로 했다."
    scene black with moveright
    play sound "se/door_open.ogg"
    $ renpy.pause(0.5)
    play bgs"bgs/people.mp3"
    scene ev fastfood_sit with moveright
    show lisa talk:
        zoom 1.4 yalign -0.2 xalign 0.85
    lisa"너 화장실 진짜 오래 있네"
    show lisa smile2
    lisa"혹시 천년 변비라도 걸린거냐?"
    stephan"여자가 돼가지고 그런 더러운 소리를 하다니"
    show lisa talk
    lisa"그러는 넌 남자가 돼가지고 그런 사소한거에나 신경쓰고"
    stephan"윽……"
    stephan"서,{cps=2} {/cps}성 고정관념은 이쯤 해 두자"
    lisa"네가 먼저 시작했잖아"
    stephan"그래, 미안"
    lisa"그보다 안에서 진짜로 무슨 일이 있었는데?"
    stephan"그게……"
    menu:
        "애들이 있는 장소를 알아냈어 (진실)":
            stephan"어떤 통화를 받았는데……{cps=2} {/cps}어쩌면 네 친구가 어디 있는지 알고 있데"
            show lisa shock
            show effect1
            play sound"se/shock.ogg" 
            lisa"{size=45}정말?!{/size}" with lshake
            lisa"그거 사실이야?"
            hide effect1
            stephan"어"
            stephan"그래서 지금 갈까 생각중인데 어때?"
            lisa"그야 당연히 가야지!"
            "얘는 크라운의 절친 이다.{cps=2} {/cps}그러니 앤의 위치를 알아야 할 필요가 있다."
            scene black with Dissolve(1.0)
            play bgs"bgs/street.mp3"
            scene ev sky_eve with moveup
            "나랑 보우만은 지도에 표시 되어있는 위치로 계속 걸어갔다."
            "약 20분 가량 걷는데만 에너지를 소비……{cps=2} {/cps}거기다 휴대폰 배터리도 왕창 소비……"
            "곧 있으면 전원이 꺼져 버릴듯 했다."
            "하지만 이걸로 윌리랑 크라운이 있을 것으로 추정되는 장소에 도착 했으니 상관 없다."
            stephan_think"근데……"
            stop bgs
            scene bg case2_outside with movedown
            "그곳은 매우 무서워 보이는 폐건물 이다."
            "주변엔 도로나 통행로 같은 게 없다보니까 엄청나게 조용했다."
            stephan_think"원랜 뭘 하는 건물 이었을까……"
            show bg case2_outside at Zoom((1280,720),(0,0,1280,720),(315,397,575,323),1.6) with dissolve
            $ renpy.pause(1.6)
            show lisa shock:
                zoom 1.4 xalign 0.8 yalign -0.3
            show stephan shock:
                zoom 1.4 xalign 0.0 yalign -0.2
            lisa"여기에 있단 말이지……?"
            stephan"응……{cps=2} {/cps}아마도……"
            show lisa talk
            lisa"여길 알려준 사람이 누구야?"
            stephan"윌리랑 아는 사람 같았어"
            stephan"자세한 건 못들었고……{cps=2} {/cps}윌리랑 앤을 목격했다고 할까나?"
            lisa"하지만 왜 걔네들이 여기에 있겠어?"
            stephan"그냥 목격자의 증언을 들었을 뿐이니까 나한테 뭐라 하지마"
            stephan"일단 안에 들어가보면 애들이 있는지 없는지 확실해지겠지"
            show lisa
            lisa"그래!"
            lisa"단 1\%의 확률이라도 난……!"
            show lisa talk
            lisa"……근데 저거 뭐야?"
            "보우만은 땅에 떨어진 물체를 가리키며 말 했다."
            stephan"빵……"
            extend" 같은데?"
            play sound "se/search_bag.mp3"
            show stephan talk:
                linear 0.4 xalign 0.2 yalign -0.4
                linear 0.4 xalign 0.0 yalign -0.2
            $ renpy.pause(0.5)
            show ev cheese_cream with dissolve:
                xalign 0.3 yalign 0.6
            "나는 땅에 떨어진 빵 같은 걸 주웠다."
            lisa"땅에 떨어진거 치곤 좀 멀쩡하네?"
            stephan"꽤 최근에 떨어진 거 같은데……"
            show stephan shock
            stop music
            stephan"그보다 이거 크림 치즈 빵 아니야?!"
            show lisa
            lisa"어, 정말이다.{cps=2} {/cps}그거 맛있던데"
            "크림 치츠 빵이 여기에 떨어져 있다는 건……"
            play sound "se/static.mp3"
            scene bg mansion_hall_night at Zoom((1280,720),(905,83,375,211),(0,167,750,422),0.0)
            show seb shock:
                zoom 1.5 xalign 0.0 yalign -0.2
            $ renpy.pause(0.4)
            scene bg case2_outside at Zoom((1280,720),(480,80,647,364),(315,397,575,323),0.0)
            show lisa:
                zoom 1.4 xalign 0.8 yalign -0.3
            show stephan shock:
                zoom 1.4 xalign 0.0 yalign -0.2
            show ev cheese_cream:
                xalign 0.3 yalign 0.6
            "어제 세바스찬이 들었다는 비명소리는 여기서 나온거다……"
            "그렇게 되면……"
            stephan_think"아,{cps=2} {/cps}아닐거야……"
            "나는 애써 마음속으로 부정 했다."
            play music "bgm/sirius5.mp3"
            "하지만 어제 내가 들은 게 사실 이라면 안엔 꽤 위험할지도 모른다."
            play sound "se/think.mp3"
            scene bg case2_outside_night at Zoom((1280,720),(315,397,575,323),(315,397,575,323),0.0) with flash
            $ renpy.pause(0.5)
            scene bg case2_outside_night at Zoom((1280,720),(315,397,575,323),(480,80,647,364),0.3)
            show effect1
            play sound "se/shock.ogg"
            $ extra_name = '비명소리'
            extra"{size=45}으아아아아아─!!{/size}" with lshake
            scene bg case2_outside at Zoom((1280,720),(480,80,647,364),(480,80,647,364),0.0) with flash
            $ renpy.pause(0.5)
            scene bg case2_outside at Zoom((1280,720),(480,80,647,364),(315,397,575,323),0.6)
            $ renpy.pause(0.6)
            show lisa talk:
                zoom 1.4 xalign 0.8 yalign -0.3
            show stephan shock:
                zoom 1.4 xalign 0.0 yalign -0.2
            show ev cheese_cream:
                xalign 0.3 yalign 0.6
            stephan_think"제발 아무 일도 없어야 할텐데……"
            lisa"그래서 안으로 들어 갈거?"
            stephan"그,{cps=2} {/cps}글쎄……"
            "어쩌면 윌리는 위험한 녀석들한테 납치 당했을 수 있다."
            "그리고 크라운은 윌리랑 데이트를 하다가 말려 들었을 확률이 있다."
            "게다가 어제 밤에 여기서 비명 소리가 나왔다고 했다……"
            stephan_think"내가 이렇게 노골적으로 위험해 보이는 곳에 들어 갈 수 있을리가 없잖아!"
            show lisa:
                linear 0.2 xalign 0.5
            lisa"뭘 망설이는거야?! 얼른 안으로 들어 가자!"
            stephan"어?!"
            play sound "se/footsteps_running.mp3"
            scene bg case2_outside at Zoom((1280,720),(315,397,575,323),(156,359,350,197),0.4)
            "보우만은 내 팔을 잡더니, 안으로 끌고 갔다."
            scene black with moveright
            $ renpy.pause(0.5)
            scene bg case2_inside at Zoom((1280,720),(496,259,196,110),(406,214,366,206),0.5) with dissolve
            $ renpy.pause(1.0)
            show bg case2_inside at Zoom((1280,720),(406,214,366,206),(718,242,529,297),0.6) with Dissolve(0.6)
            show stephan fear:
                xalign 0.2 yalign -0.2 zoom 1.3
            show lisa talk:
                xalign 1.0 yalign -0.3 zoom 1.3
            "내부도 외부 묻지 않게 으리으리하다."
            stephan"저기 리……"
            show effect1
            play sound "se/shock.ogg"
            lisa"{size=45}애애애앤~! 어딨어?!{/size}" with lshake
            show stephan fear
            stephan"히익!"
            hide effect1
            "보우만은 깡패들이라도 나올 것 같은 장소에서 크게 소리질렀다."
            stephan_think"확실히 애들을 찾기 위해서 그게 가장 최상책 이긴 하겠지만……"
            "문제는 그 애들을 \'납치\'한 범인 역시도 여기에 있을 수 있기에 위험하다."
            show lisa shock
            play sound "se/footsteps_concrete.mp3"
            $ renpy.pause(1.0)
            stop sound
            $ extra_name = '스테반 & 리사'
            extra"……!"
            lisa"누군가 있어!"
            "엄청나게 위험한 생각이 들었다."
            play sound "se/footsteps_running.mp3"
            show lisa shock:
                linear 0.3 xalign 2.0
            lisa"가보자!"
            "하지만 보우만은 아무런 위기감도 없이 바로 달려갔다."
            stephan"가, 같이 가!"
            show stephan fear:
                linear 0.4 xalign 2.0
            scene black with moveright
            $ renpy.pause(0.5)
            scene bg case2_inside2 with moveright
            show stephan fear:
                zoom 1.6 xalign 0.2 yalign -0.1
            show lisa talk:
                zoom 1.6 xalign 0.6 yalign -0.2
            lisa"{size=45}아무도 없나요~?{/size}"
            stephan"어, 어이……{cps=2} {/cps}계속 큰 소리 내면서 다닐거야?"
            lisa"그렇지 않으면 어떻게 사람을 부르려고?"
            stephan"…………"
            show lisa mad
            lisa"……그보다 너, 언제까지 붙어 있을거냐"
            show stephan fear:
                linear 0.3 xalign 0.0
            stephan"미, 미안!"
            stephan"근데 여기 어쩌면 위험한 사람이 있을지도 모른단 말이야!"
            stephan"그렇게 큰 소리를 내면서 다니는 건 좀……"
            show lisa shock
            lisa"어?!"
            lisa"위험한 사람이 있다니……?"
            lisa"그건 무슨 뜻이야?"
            "생각해보니까 난 보우만한테 윌리랑 앤이 위험한 사람한테 납치 됐을지도 모른다는 말을 한번도 한적이 없다."
            stephan_think"말 해야 하나……"
            stephan"그,{cps=2} {/cps}그게……"
            stephan"어쩌면 네 친구가 납……!"
            stop music
            scene bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(272,276,612,344),0.0) with dissolve
            show anne:
                zoom 1.7 xalign 0.5 yalign -0.3
            anne"{size=45}리사─!{/size}"
            "그때 내 말을 끊으며, 누군가 보우만의 이름을 불렀다."
            lisa"앤?!"
            stephan"앤 이라고?!"
            stephan_think"쟤가 앤 크라운?"
            "뭔가 이상했다."
            extend" 왜 앤 크라운이 여기서 돌아다니고 있는거지?"
            "녀석은 분명 윌리랑 같이 납치 됐을거라 생각 했다."
            "윌리가 마르쿠스 고드윈을 찾는다고 이런저런 짓을 하다가 같이 있었던 앤 크라운이 함께 피해를 봤다고 생각 하고 있었다."
            "하지만……{cps=2} {/cps}녀석은 지금 자유롭게 건물을 돌아다니고 있다."
            stephan_think"설마……"
            play sound "se/footsteps_running.mp3"
            show lisa shock:
                zoom 2.0 xalign -3.0 yalign -0.1
                linear 0.6 xalign 0.0
            "그때 보우만은 크라운을 향해서 전력으로 달렸다."
            play music "bgm/happy2.mp3"
            lisa"정말로 여기 있었구나~!"
            lisa"나, 네가 엄청나게 보고 싶었어!"
            show lisa smile with dissolve:
                zoom 1.7
            show lisa smile:
                linear 0.3 xalign 0.3
            show anne shock
            anne"으윽……"
            "보우만은 크라운을 쎄게 껴안았다."
            show lisa mad
            lisa"내가 너때문에 얼마나 걱정 했는지 알아?!"
            lisa"막 가출 했다는 소식이 들려오고……"
            lisa"도대체 어떻게 된거야……!"
            anne"그, 그게……"
            show anne shy
            anne"최근들어서 힘든 일이 많았거든……{cps=2} {/cps}그래서……"
            lisa"그런 일이라면 나한테 상담 했어야지!"
            extend" 혼자서 고민 한다고 해결되는 것 없다고!"
            anne"하지만 말 하기 힘든 고민 이었던걸……"
            anne"그래서 가출을……"
            show lisa shock
            lisa"그럼 너 계속 여기 있었어?!"
            anne"으, 응"
            anne"그래도 생각하는 것 만큼 나쁘진 않아……!"
            lisa"아무리 그래도 아무런 말도 없이 가출 하면 어떻게!"
            lisa"내가 정말……{cps=2} {/cps}엄청 걱정 했다고!"
            anne"미안……"
            show lisa talk:
                linear 0.4 xalign 0.0
            lisa"앤, 얼른 집으로 돌아가자!"
            anne"어,{cps=2} {/cps}어……"
            anne"근데 여긴 어떻게 알고 온거야?"
            show lisa
            lisa"토머가 널 목격 했다는 사람한테서 연락을 받았대!"
            anne"토머……?"
            lisa"응, 스테반 토머 라고 있잖아!{cps=2} {/cps}윌리 따라다니는 애"
            show anne
            stop music
            anne"…………"
            "크라운은 나를 노려보기 시작했다."
            anne"리사, 나 잠깐 토머 한테 하고 싶은 말이 있어……"
            show lisa talk
            lisa"응?"
            hide anne
            play sound "se/footsteps_concrete.mp3"
            show anne with dissolve:
                zoom 2.0 xalign 0.5 yalign 0.0
            "내 쪽으로 다가왔다."
            scene bg case2_inside2 with movedown
            show anne:
                zoom 1.8 xalign 1.0 yalign -0.3
            show stephan talk:
                zoom 1.8 xalign 0.0 yalign 0.0
            anne"저어……{cps=2} {/cps}잠깐 하고 싶은 말이……"
            stephan"마침 나도 하고 싶은 말이 있었어"
            play music "bgm/sirius1.mp3"
            stephan"……윌리는 어디 있지?"
            show lisa shock with dissolve:
                zoom 1.8 xalign 0.5 yalign -0.1
            lisa"그러고 보니까 토머 말로 윌리-윌리가 너랑 같이 있을거라던데!"
            show stephan shock
            stephan"저기, 보우만. 잠깐 비켜주면 안될까?"
            lisa"응?"
            anne"나랑 토머……{cps=2} {/cps}대화 중이었어"
            show lisa talk
            lisa"알았어……"
            hide lisa talk with dissolve
            show stephan talk
            "윌리의 룸메이트의 증언이 확실하다면 여기엔 윌리가 있다."
            "적어도 윌리의 휴대폰은 있다."
            "……게다가 마지막으로 윌리를 만났던 사람이 앤 크라운"
            "설령 윌리의 행방에 대해서 자세히 알지 못한다 해도, 최소한의 단서는 얻을 수 있을거다."
            stephan"……그래서 윌리가 어디 있는지 알아?"
            anne"네……{cps=2} {/cps}어디 있는지 알아요……"
            show stephan shock
            stephan"어디 있는데?!{cps=2} {/cps}지금 여기 있어!?"
            anne"잠깐……{cps=2} {/cps}자리를 옮겨도 될까요?"
            stephan"왜?"
            anne"윌리가 어디 있는지……{cps=2} {/cps}알려 드리게요……"
            show stephan talk
            stephan"좋아"
            scene bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(272,276,612,344),0.0) with dissolve
            show anne:
                zoom 1.7 xalign 1.0 yalign -0.4
            show lisa shock:
                zoom 1.7 xalign 0.0 yalign -0.2
            anne"리사……{cps=2} {/cps}나 잠깐 토머랑 어디 좀 갈게……"
            lisa"어?!{cps=2} {/cps}집에 안가?!"
            anne"그, 금방 끝날거야……"
            anne"윌리에 관해서 꼭 전해야 돼서……"
            show lisa talk
            lisa"그럼 나도 같이갈래!"
            show anne shock
            anne"아니!{cps=2} {/cps}넌 여기 있어줘!"
            lisa"하지만……"
            show anne
            anne"금방 돌아 올거야……{cps=2} {/cps}약속 할게……"
            lisa"…………"
            lisa"꼭 돌아와!"
            lisa"널 다시 잃어버리고 싶진 않으니까"
            anne"응"
            show anne:
                linear 0.5 xalign 2.0
            play sound "se/footsteps_concrete.mp3"
            scene black with Dissolve(1.0)
            "나는 크라운을 따라서 옆에 있는 녹슨 철문으로 들어갔다."
            "그리고 어떤 방으로 이어 졌는데……"
            stop music
            scene bg case2_inside2 with eyeopen
            "……이전 방과 완전히 똑같은 형태 였다."
            "아무래도 이 건물은 같은 방이 여러개로 이어져 있나보다."
            stephan_think"길 잃기 엄청 쉽겠는데……"
            show bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(372,216,716,403),0.4)
            $ renpy.pause(0.4)
            show anne:
                zoom 1.7 xalign 1.0 yalign -0.4
            show stephan talk:
                zoom 1.7 xalign 0.0 yalign 0.0
            stephan"근데 왜 날 여기로 데리고 온거야?"
            show stephan shock
            stephan"혹시 뭔가 큰 일이라도 있는 건 아니지?!"
            anne"{size=20}널……{cps=2} {/cps}절대 용서 못해……{/size}"
            "크라운이 작게 중얼거렸다."
            stephan"어?"
            anne"윌리도 뺏더니 이젠 내 친한 친구 까지……"
            show stephan shock
            show anne yantalk
            play music "bgm/sirius5.mp3"
            anne"널 죽여버리겠어……"
            stephan"자, 잠깐……{cps=2} {/cps}너 갑자기 왜 그래?"
            "크라운의 상태가 이상해졌다."
            stephan"윌리는 어디 있는거야?!"
            show anne yanmad
            anne"윌리…… 윌리…… 윌리…… 윌리……!"
            anne"할 줄 아는 게 윌리 찾기 뿐인가요?"
            extend" 스테반 토머"
            anne"언제나 윌리 근처에서 방긋하게 쪼개기나 하고, 항상 옆에 달라붙고!"
            anne"당신을 볼때마다 전 \'저 눈알을 칼로 후벼버리고 싶다\'는 충동에 휩싸여요……"
            show stephan shock3
            stephan"……!"
            anne"제가 아무리 윌리를 보고 싶어도……{cps=2} {/cps}항상 당신이 옆에 붙어있고!"
            anne"정말 짜증 난다고……"
            "마치 날 계속 지켜 봤다는 듯 한 말투였다."
            stephan_think"하지만 난 처음 보는……"
            play sound "se/static.mp3"
            show ev anne_watching
            $ renpy.pause(0.5)
            hide ev anne_watching
            "며칠 전에 내가 봤던 여자 아이……{cps=2} {/cps}앤 크라운 이었던건가……"
            anne"윌리를 빼앗은것도 모자라서 이젠 나의 친한 친구 까지……"
            anne"왜 계속 제 인생을 엉망으로 만드는거예요?!"
            stephan"무, 무슨 소리야?!"
            anne"토머, 당신 때문에 제 인생이 얼마나 꼬였는지 아세요?!"
            anne"항상 윌리 주변에 붙어다니고……{cps=2} {/cps}친한듯이 싱글벙글하게 웃으면서 대화하고!"
            anne"엄청나게 부러웠어요"
            anne"당신은 저랑 윌리가 같이 있는데 가장 큰 장애물 이었죠"
            anne"윌리랑 함게 있기 위해선 토머를 죽이거나……{cps=2} {/cps}아니면 윌리를 강제로라도 제 주변에 있게 만들거나……"
            anne"이 두가지 뿐이었습니다"
            stephan"둘다 뭔가 잘못된거 같은데?"
            stephan"굳이 그렇게 극단적이지 않아도 분명……"
            anne"가능 할 거 같아요?!"
            anne"하지만 토머의 말대로 전 남에게 피해를 주고 싶지 않아요……"
            anne"그래서 최대한 사람이 덜 다치는 쪽……{cps=2} {/cps}윌리를 선택했어요"
            anne"그렇게 해서 드디어 둘만의 행복한 시간이 찾아왔는데 토머가 찾아오면서 모든걸 망쳐놓고……"
            anne"그것도 모자라서 아무 관련 없는 제 친구까지 불러들이고!"
            anne"당신이 그러고도 인간인가요?"
            anne"최대한 남에게 피해가 가지 않는쪽으로 행동 할 수 없었던거냐고요?!"
            stephan"이건 완전 억지 잖아!"
            stephan"왜 내가 나쁜거야?"
            anne"당신은 이렇게 위험한 장소에 리사를 데리고 왔어요……"
            anne"당신 때문에 내가 어떤 애 인지 들킬뻔 했다고!"
            show stephan shock3:
                linear 0.3 xalign -0.1
            stephan"…………"
            "나는 크라운의 살기에 겁먹어서 무의식적으로 뒷걸음질 했다."
            anne"예전부터 계속 당신을 죽이고 싶은 충동에 휩싸였었는데……"
            show anne yan
            play sound "se/cutter.mp3"
            anne"이젠 이룰 수 있겠어……!"
            "크라운은 주머니에서 커터 칼 하나를 꺼내 들면서 기분 나쁘게 웃기 시작했다."
            show anne yan:
                linear 0.3 xalign 0.1
            $ renpy.pause(0.2)
            play sound "se/fall.ogg"
            stop music
            scene black with flash
            $ renpy.pause(1.0)
            scene ev anne_killing_body at Zoom((1280,720),(0,0,1280,720),(63,0,775,436),0.0)
            show anne_killing cutter at Zoom((1280,720),(0,0,1280,720),(63,0,775,436),0.0)
            show anne_face talk at Zoom((1280,720),(0,0,1280,720),(63,0,775,436),0.0)
            show white
            show black
            stephan"으……"
            "나는 크라운의 갑작스런 행동에 당황해, 힘을 잃고 땅 바닥에 쓰러져 버렸다."
            "정신을 차리고 천천히 눈을 떴는데……"
            hide black with eyeopen
            hide white with dissolve
            stephan"……!"
            anne"토머……"
            anne"전 이러고 싶지 않아요……"
            "크라운은 내 위에 올라타면서 커터칼로 위협했다."
            "이 상황이 너무 무서웠다.{cps=2} {/cps}눈물이 나올 정도로 무서웠다."
            stephan"그그그, 그만해……"
            "손이 떨리고, 다리고 떨리고, 말대 제대로 잇기 힘들었다."
            anne"하지만……"
            play music"bgm/sirius3.mp3"
            hide anne_face talk
            extend" 드디어 저의 오랜 꿈을 이룰 수 있는 기회가 찾아 왔는 걸요?"
            anne"윌리도 당신 때문에 많이 고생 한 거 같던데……{cps=2} {/cps}당신이 죽어주면 분명 힘들어 할 필요가 없겠죠~?"
            stephan"난 딱히 너한테 아무짓도 하려는 게……"
            show ev anne_killing_body at Zoom((1280,720),(63,0,775,436),(415,490,471,265),0.3)
            show anne_killing cutter at Zoom((1280,720),(63,0,775,436),(415,490,471,265),0.3)
            stephan"으읍……!" with lshake
            "크라운은 왼손으로 내 입을 강하게 눌렀다."
            anne"그 입부터 찟어버리기 전에 닥쳐주세요"
            stephan"으흐흡……!"
            show ev anne_killing_body at Zoom((1280,720),(415,490,471,265),(240,126,521,293),0.5)
            show anne_killing cutter at Zoom((1280,720),(415,490,471,265),(240,126,521,293),0.5)
            show anne_face talk at Zoom((1280,720),(415,490,471,265),(240,126,521,293),0.5)
            anne"정말 메사에 도움이 안되는 쓰레기 같은 존재네요"
            anne"학교에선 자기가 무슨 주인공 인듯 당당하게 나대더니, 위협감을 느끼면 빌빌 떨기 시작하고……"
            anne"당신 따위는 절대 윌리의 발 끝 만큼도 못되요"
            hide anne_face talk
            anne"그런데도 자기는 윌리 친구라면서 자랑스러워 하고~"
            anne"윌리에 대해서 아는 게 있기나 하나요?"
            anne"윌리 생일?{cps=2} {/cps}혈액형?{cps=2} {/cps}키?{cps=2} {/cps}좋아하는 음식?"
            anne"제가 전~부 알려 드릴게요"
            anne"윌리는 12월 28일 생 이고, 혈액형 AB형에 키는 181cm, 좋아하는 음식은 다운스 언니가 해주는 콘 스프"
            stephan"으읍……"
            "혈액형을 제외하곤……{cps=2} {/cps}하나도 몰랐던 사실이었다."
            show anne_face mad at Zoom((1280,720),(415,490,471,265),(240,126,521,293),0.0)
            anne"이딴 녀석이 윌리의 친구라니……"
            show anne_face talk at Zoom((1280,720),(415,490,471,265),(240,126,521,293),0.0)
            anne"그래도 자비를 베풀어서 조금이라도 오래 살려드릴게요"
            anne"물론 살아있는 동안이 그리 좋게 느껴지진 않겠지만……"
            scene ev anne_killing_bodyb at Zoom((1280,720),(240,126,521,293),(0,120,905,509),0.5)
            show anne_killing cutter2 at Zoom((1280,720),(240,126,521,293),(0,120,905,509),0.5)
            show anne_face mad at Zoom((1280,720),(240,126,521,293),(0,120,905,509),0.5)
            show anne_faceb at Zoom((1280,720),(240,126,521,293),(0,120,905,509),0.5)
            play sound "se/hit3.mp3"
            $ renpy.vibrate(0.3)
            show red with sshake:
                alpha 0.4
            stephan"{size=45}으으으으읍!{/size}"
            "내 어깨에 커터칼이 쎄게 박히면서 나온 피가 크라운의 얼굴로 튀었다."
            "고통 때문에 소리 지르고 싶어도, 입이 막혀서 목소리는 전혀 나오지 못했다."
            anne"전 이러고 싶지 않아요……{cps=2} {/cps}하지만……"
            hide anne_face mad
            extend" \'사랑\'을 위해선 어쩔 수 없어요"
            stephan_think"사랑……?!"
            "역시 윌리를 납치 했던건 앤 크라운 이다."
            "……하지만 이제와서 그걸 알았다고 해도 바뀌는 건 없었다."
            "빨리 집에 가고 싶다는 생각만 들었다……"
            show anne_killing cutter at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            hide anne_faceb
            hide red
            show anne_face talk at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            show anne_faceb at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            show red:
                alpha 0.4
            anne"당신의 피 때문에 제 얼굴이 더럽혀졌네요……"
            anne"어떻게 죽어가면서 까지 남에게 피해만 주는거죠?"
            anne"윌리가 이런 녀석이랑 2년 반 가까이 있었다니……"
            show ev anne_killing_bodyb at Zoom((1280,720),(0,120,905,509),(434,486,478,269),0.4)
            show anne_killing cutter at Zoom((1280,720),(0,120,905,509),(434,486,478,269),0.4)
            show anne_face talk at Zoom((1280,720),(0,120,905,509),(434,486,478,269),0.4)
            show anne_faceb at Zoom((1280,720),(0,120,905,509),(434,486,478,269),0.4)
            stephan"으흐흐흡!"
            "나는 필사적으로 몸부림 쳤다."
            "하지만 내가 평상시에도 체력이 많이 약했고, 거기다 현재 취하고 있는 자세로는 풀려나가는 게 힘들다."
            show ev anne_killing_bodyb at Zoom((1280,720),(434,486,478,269),(289,192,439,247),0.3)
            show anne_killing cutter at Zoom((1280,720),(434,486,478,269),(289,192,439,247),0.3)
            show anne_face talk at Zoom((1280,720),(434,486,478,269),(289,192,439,247),0.3)
            show anne_faceb at Zoom((1280,720),(434,486,478,269),(289,192,439,247),0.3)
            anne"눈이 정말 아름답네요……"
            anne"크게 빛나는 에메랄드 빛의 눈……"
            show anne_face mad at Zoom((1280,720),(434,486,478,269),(289,192,439,247),0.0)
            anne"너무 부러워"
            play sound "se/heartbeat.mp3"
            scene ev anne_killing_bodyb at Zoom((1280,720),(246,97,508,286),(49,0,439,247),0.0)
            show anne_killing cutter at Zoom((1280,720),(246,97,508,286),(49,0,439,247),0.0) with dissolve
            show anne_face mad at Zoom((1280,720),(246,97,508,286),(49,0,439,247),0.0)
            show anne_faceb at Zoom((1280,720),(246,97,508,286),(49,0,439,247),0.0)
            $ renpy.pause(1.0)
            scene ev anne_killing_bodyb at Zoom((1280,720),(246,97,508,286),(14,127,898,505),0.0)
            show anne_killing cutter2 at Zoom((1280,720),(246,97,508,286),(14,127,898,505),0.0)
            show anne_face mad at Zoom((1280,720),(246,97,508,286),(14,127,898,505),0.0)
            show anne_faceb at Zoom((1280,720),(246,97,508,286),(14,127,898,505),0.0)
            play sound "se/hit3.mp3"
            show red:
                alpha 0.4
            $ renpy.vibrate(0.3)
            stephan"{size=45}으으윽!{/size}" with lshake
            "고통……"
            "이 상황에서 떠오르는 것은 고통 뿐이었다."
            "조금 다른 생각을 해서 느껴지는 고통을 최소한으로 해보기로 했다."
            stephan_think"내가 여기에 온 이유……"
            play sound "se/heartbeat.mp3"
            scene ev willy_mid with flash #중학교때 교복을 입고 있는 윌리가 인상을 쓰며 말 함
            $ renpy.pause(0.5)
            scene ev anne_killing_bodyb at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            show anne_killing cutter2 at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            show anne_face mad at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            show anne_faceb at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            show red with flash:
                alpha 0.4
            stephan_think"나도 누군가에게 도움이 되고 싶었는데……"
            show anne_killing cutter at Zoom((1280,720),(246,97,508,286),(0,120,905,509),0.0)
            stephan_think"크라운의 말이 맞아……{cps=2} {/cps}난 메사에 도움따윈 안돼……"
            stephan_think"그런 내가 누군가에게 도움이 될 수 있다고 생각 했었는데……"
            "이젠 머릿속이 새하얗다."
            "이젠 뭐가 어떻게 되든 상관 없게 느껴졌다."
            "그때 크라운은 내 입을 막고 있던 왼손으로 내 볼을 살짝 만지기 시작했다."
            show ev anne_killing_bodyb at Zoom((1280,720),(246,97,508,286),(218,136,615,346),0.7)
            show anne_killing cutter at Zoom((1280,720),(246,97,508,286),(218,136,615,346),0.7)
            show anne_face talk at Zoom((1280,720),(246,97,508,286),(218,136,615,346),0.7)
            show anne_faceb at Zoom((1280,720),(246,97,508,286),(218,136,615,346),0.7)
            anne"정말 피부도 곱네요……"
            anne"남자 라고는 믿기 힘들 정도로 뽀얗 피부를 가지고 있어요"
            "이번엔 내 목을 만지기 시작했다."
            anne"비결이 뭐예요?"
            "나는 입에서 손이 떨어진 이 순간을 이용해서 보우만을 부르려고 했다."
            "하지만……"
            show lisa smile:
                zoom 2.0 xalign 0.5 yalign 0.0 alpha 0.0
                linear 0.6 alpha 0.5
            "만약 보우만이 이 상황을 보게 된다면 어떻게 생각 할까?"
            "자신이 소중하게 여겼던 친구가 이런 미치광이 살인마 라는 걸 알게 된다면……"
            "한편으론 보고 싶다는 생각도 했다.{cps=2} {/cps}또 한편으론 슬프다고도 생각 했다."
            show lisa smile:
                linear 0.5 alpha 0.0
            "허나 지금은 내 목숨이 가장 중요했다."
            stephan_think"일단 내가 살아 있어야……"
            hide lisa smile
            "나는 큰 소리를 내려고 숨을 들이 쉬었다. 그리고……"
            stephan"{size=45}리ㅅ……{/size}"
            show ev anne_killing_bodyb at Zoom((1280,720),(218,136,615,346),(452,496,460,259),0.3)
            show anne_killing cutter at Zoom((1280,720),(218,136,615,346),(452,496,460,259),0.3)
            show anne_face talk at Zoom((1280,720),(218,136,615,346),(452,496,460,259),0.3)
            show anne_faceb at Zoom((1280,720),(218,136,615,346),(452,496,460,259),0.3)
            play music "bgm/sirius5.mp3"
            play sound "se/heartbeat.mp3"
            $ renpy.pause(0.5)
            stephan"크아아악!"
            "크라운은 내 목을 강하게 조르기 시작했다."
            stephan_think"녀석……{cps=2} {/cps}일부러……!"
            "크라운은 내가 소리 지를때 가지 기다렸던거다."
            "덕분에 몸엔 산소가 없어서 얼마 못 버틸것 같았다."
            stephan"그……{cps=2} {/cps}마안……"
            play sound "se/heartbeat.mp3"
            stephan"크으으윽!"
            "크라운은 무게를 실어서 내 목을 더 쎄게 조를 뿐이었다."
            show ev anne_killing_bodyb at Zoom((1280,720),(452,496,460,259),(120,97,660,372),0.5)
            show anne_killing cutter at Zoom((1280,720),(452,496,460,259),(120,97,660,372),0.5)
            show anne_face talk at Zoom((1280,720),(452,496,460,259),(120,97,660,372),0.5)
            show anne_faceb at Zoom((1280,720),(452,496,460,259),(120,97,660,372),0.5)
            anne"정말 보기 추하네요.{cps=2} {/cps}고통에 몸부림 치는 표정이 정말 보기 추하고, 힘들어요"
            anne"한시라도 빨리 고통에서부터 해방 시켜드릴게요……"
            "그대로……"
            show anne_face mad at Zoom((1280,720),(452,496,460,259),(120,97,660,372),0.0)
            show anne_killing cutter2 at Zoom((1280,720),(452,496,460,259),(120,97,660,372),0.0)
            play sound "se/hit3.mp3"
            stop music
            scene white with flash
            "온 몸이 아픈 탓에 마지막엔 어디가 찔렸는지 기억하기도 힘들었다."
            stephan_think"이젠……"
            show grandpa:
                alpha 0.0 zoom 1.8 xalign 0.5 yalign -0.2
                linear 1.0 alpha 0.8
            stephan_think"할아버지랑 한 약속……"
            stephan_think"지키기 힘들겠는데……"
            scene black with dissolve
            "그대로 몸에서 힘이 풀리고……{cps=2} {/cps}의식이 사라졌다……"
            $ renpy.pause(0.5)
            scene bg case2_inside2 with Dissolve(1.0)
            show anne yanmad:
                zoom 1.7 xalign 0.5 yalign -0.5
            anne"하아……{cps=2} {/cps}하아……"
            anne"이걸로 좀……"
            show anne
            play music "bgm/sad4.mp3"
            anne"자, 잠깐만……"
            "지금 내 눈앞에 믿기 힘든 광경이 보였다."
            show anne:
                linear 0.4 yalign -0.7 zoom 2.0
                linear 0.4 yalign -0.5 zoom 1.7
            play sound"se/search_bag.mp3"
            anne"토, 토머……{cps=2} {/cps}괜찮으세요?"
            "나는 피범벅이가 된 토머를 좌우로 흔들어 보았다."
            show anne yanshock2
            anne_think"움직이질 않아……"
            anne_think"혹시 죽은건가?"
            anne"내, 내가 죽인거야?!"
            show effect1
            play sound "se/shock.ogg"
            anne"{size=45}꺄아아아악─!{/size}" with lshake
            hide effect1
            "남에게 피해를 줘버렸다."
            "아주 오래전부터 내가 우려했던 일이 발생해버렸다!"
            anne_think"아무리 그래도……{cps=2} {/cps}내가 사, 살인 이라니……"
            anne_think"윌리를 납치한 건 나중에 수습이 가능할지라도 살인은……!"
            anne"우, 우윽……!"
            "처참한 모습이 되어버린 토머를 보니까 속이 울렁거렸다."
            play sound "se/footsteps_running.mp3"
            scene bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(0,224,711,400),0.3)
            show lisa talk:
                zoom 1.7 xalign -1.5 yalign -0.3
                linear 0.5 xalign 0.8
            lisa"{size=45}무슨 일이야?!{/size}"
            lisa"방금 비명 같은 게……"
            show lisa shock
            lisa"……!"
            anne"아, 안돼……"
            anne_think"리사가 봤어……"
            anne_think"다른 사람도 아닌 리사가……"
            scene bg case2_inside2 at Zoom((1280,720),(0,224,711,400),(358,241,711,400),0.5) with dissolve
            show anne shock2:
                zoom 1.2 xalign 0.3 yalign 1.0
            show lisa shock:
                zoom 2.0 xalign 0.0 yalign -0.2
                linear 0.3 xalign 0.5
            lisa"토머!{cps=2} {/cps}정신 차려!"
            lisa"앤! 이거 어떻게 된거야?!"
            lisa"누가 이런짓을 한거냐고!!"
            "리사는 절대로 날 의심하지 않았다."
            "하지만 지금 이 상황에선 들킨는 건 시간문제……"
            "리사가 날 싫어하게 되는 건 싫다.{cps=2} {/cps}죽어도 싫다!"
            show anne shock2 with dissolve:
                zoom 2.0 xalign 0.0 yalign -0.4
            anne"누, 누군가 와서……{cps=2} {/cps}토머를 칼로 찔렀어……"
            lisa"그 사람 지금 어디 있어?!"
            anne"몰라……"
            lisa"큭……"
            lisa"그, 그래!{cps=2} {/cps}어서 경찰에 신고를……!"
            "리사는 폰으로 경찰서 번호를 눌렀다."
            lisa"여보세요?!{cps=2} {/cps}여기 지금……"
            show anne shock2 with Dissolve(1.0):
                zoom 1.2 xalign 0.3 yalign 1.0
            scene black with eyeshut
            anne_think"거짓말을 해버렸어……"
            "난 사랑 하는 사람과 같이 있기 위해서 가족을 속였다."
            "아주 잠깐만 같이 있기 위해서 사랑하는 사람의 친구를 죽이기 까지 했다."
            "하지만 이젠 나의 친한 친구까지 속여버렸다."
            anne_think"윌리랑 같이 있기 위해서……{cps=2} {/cps}이렇게까지는 할 필요가 없었는데……"
            "또다시 내가 한 행동에 후회를 한다."
            "언제나 저지른 다음에 후회……"
            "난 내 자신이 정말로 싫다."
            play sound "se/think.mp3"
            scene bg diary_country at blur with flash:
                crop(58,374,474,266)
                size(1280,720)
            show willy:
                xalign 0.5 yalign -0.1 zoom 1.8
            willy"자기혐오는 너를 이 넓은 세계에서 혼자 남아있는거 보다 더 외로운 존재로 만들텐데"
            scene black with flash
            anne"큭……"
            "가슴이 찡해졌다."
            "난 과연 내 자신을 싫어해도 되는 걸까……"
            "같은 실수를, 잘못된 판단을 계속 반복하는 나로 있어도 괜찮은걸까……"
            stop music
            anne_think"한 번 만 더 기회가 있다면……"
            hide black with eyeopen
            scene bg case2_inside2 at Zoom((1280,720),(0,224,711,400),(358,241,711,400),0.5) with dissolve
            show anne:
                zoom 1.2 xalign 0.3 yalign 1.0
            show lisa shock:
                zoom 2.0 xalign 0.5 yalign -0.2
            "……리사는 여전히 경찰에게 상황 설명을 하기 있다."
            "얼마나 당황 했는지, 뒤에 내가 있었다는 것도 완전히 잊고 있는 듯 했다."
            show anne yantalk
            "뒤에서 찔러도……{cps=2} {/cps}전혀 눈치 체지 못 할 거 같았다……"
            anne_think"그래……"
            anne_think"어차피 난 사람을 죽인 살인자야……"
            extend" 한명 더 죽인다고 해서 상황이 바뀌는 건 없어"
            show anne yan
            anne_think"그리고 여기 주변엔 아무도 없어!{cps=2} {/cps}목격자만 없으면 난 안전해……"
            show anne yantalk with dissolve:
                zoom 1.5 yalign -0.3
            anne_think"이대로 끝내고 현장을 뜬다면, 오늘 있었던 일은 아무도 몰라"
            anne_think"그렇게 하면 한 번 더 기회를 만들 수 있어……"
            show anne yanshock2 with dissolve:
                zoom 1.2 yalign 1.0
            play music "bgm/sad3.mp3"
            anne"……!"
            "지금 또다시 위험한 생각을 해버렸다."
            "그것도 다른 사람이 아닌 리사를……"
            play sound "se/static.mp3"
            show ev anne_killing_bodyb at Zoom((1280,720),(452,496,460,259),(0,58,912,514),0.0)
            show anne_killing cutter2 at Zoom((1280,720),(452,496,460,259),(0,58,912,514),0.0)
            show anne_face mad at Zoom((1280,720),(452,496,460,259),(0,58,912,514),0.0)
            show anne_faceb at Zoom((1280,720),(452,496,460,259),(0,58,912,514),0.0)
            $ renpy.pause(0.5)
            hide ev anne_killing_bodyb
            hide anne_killing cutter2
            hide anne_face mad
            hide anne_faceb
            "만약 이번에도 내 충동대로 했다면……{cps=2} {/cps}난 망가져버릴지도 모른다."
            "충분히 죄가 많은 나 자신을……"
            "더욱 싫어하게 될지도 모른다."
            anne_think"하지만 어떻게 해야 되는거야……"
            "이 상황에서 어떻게 해야 좋은 결말이 나올 수 있을까?"
            "어떻게 해야 더이상 후회를 하지 않고,{cps=2} {/cps}내가 사랑하는 사람들이 행복하게 살 수 있을까?"
            "행복해지는 건 잘 몰라도……{cps=2} {/cps}적어도 더이상 고통받지 않는 방법은 있다."
            play sound "se/search_bag.mp3"
            scene bg case2_inside2 at Zoom((1280,720),(638,270,642,362),(638,270,642,362),0.0) with dissolve
            show anne talk with dissolve:
                zoom 1.7 xalign 0.4 yalign -0.4
            "어차피 난 이런 인간이다."
            "극단적인 생각밖에 할 줄 모르고, 순간의 충동에 몸을 맡기고……"
            "나중에 후회를 하는……"
            "그런 인간"
            anne_think"그런 인간의 최후 역시도 극단적이겠지……"
            "나는 손에 들고있는 피로 범벅이 된 커터 칼을 바라봤다."
            "지금 내가 생각 하고 있는 행동도, 지금까지 내가 해왔던 행동들 처럼 매우 극단적이고 충동적이다."
            "하지만 한가지 차이가 있다."
            "난 후회를 하지 않을거다."
            "설령 후회를 하고 싶다고 해도, 억지로라도 웃어 보일거다."
            "왜냐면 이것이 나의 마지막 충동이니까"
            play sound "se/hit2.mp3"
            $ renpy.vibrate(0.3)
            scene black
            anne"윽……" with lshake
            "짧은 신음을 토했다."
            "엄청난 고통이 몸 전체를 맴돌았다."
            "혹시 토머도 이런 고통을 느끼지 않았을까? 하면서 생각 해봤다."
            "하지만 난 절대로 알 수 없을거다."
            "왜냐면 남의 생각을 증명하는 건 절대로 불가능 하니까"
            "내가 남의 생각을 알 수 없듯이, 남들도 내 생각을 알 수 없다."
            "그저 우린 서로의 생각을 알고 있다고 믿을 뿐이다."
            play sound"se/fall.ogg"
            $ renpy.vibrate(0.3)
            "나는 피를 너무 많이 쏟은 탓에, 힘을 잃고 쓰러졌다."
            play sound "se/footsteps_running.mp3"
            "그때 내 소리를 들었는지, 누군가 이쪽으로 달려왔다."
            lisa"{size=45}앤─!!{/size}"
            "리사가 매우 서글픈 목소리로 내 이름을 불렀다."
            "하지만 그 이후에 리사가 하는 말은 나에겐 소음처럼 들릴 뿐이었다."
            anne_think"이런……"
            "좋지 않은 장면을 보여주고 말았다."
            "어쩌면 이중에서 가장 아픈 경험을 하고 있는 건 내가 아니라, 리사일지도 모른다."
            "난 왜 이럴까"
            "또다시 내가 한 행동에 대해서 후회감이 느껴졌다."
            "내 목적을 위해서 또다시 극단적인 선택을 해버렸고……{cps=2} {/cps}지금 또다시 뒤늦게 내 행동의 심각성을 깨달아버렸다."
            "난 마지막 조차도 같은 실수를 반복 하는 건가?"
            "이 루프를 깨기 위해서 한 행동이 오히려 이 루프를 초례하고 있었다니"
            "아니다……"
            "절대로 같은 실수를 반복하지 않을거다."
            "후회되더라도 꾹 참는거다!"
            "난 마지막까지 남은 기력을 짜내서 힘겹게 입을 열었다."
            anne"리사……{cps=2} {/cps}사랑해……"
            "필사적으로 \'미안해\'라는 말이 나오지 않도록 참았다."
            "왜냐면 난 나의 행동을 후회하고 싶지 않으니까"
            "설령 나의 행동이 충동적일지라도……{cps=2} {/cps}그 사실을 깨달고 어떻게 하려고 한 내 자신을 칭찬해주고 싶다."
            "왜냐면……"
            "난 내 자신 뿐이니까"
            "남의 생각은 증명이 불가하고, 그저 신뢰만으로 이루어지지만……{cps=2} {/cps}자신의 생각은 증명이 가능하다."
            "유일하게 알 수 있는 존재, \'자신\'마저도 싫어하게 된다면……{cps=2} {/cps}윌리의 말대로 외롭다."
            jump game_over
        
        "잠깐 급한 용무가 생겨서 (거짓)":
            stephan"잠깐 급한 용무가 생겼어"
            stephan"그러니까 먼저 가봐야 될거 같은데 괜찮을까……?"
            lisa"어디 갈건데?"
            stephan"그건 개인적인거라 말 하기 힘들어"
            show lisa
            lisa"알았어, 그럼 나도 집에 가봐야겠네"
            show lisa smile
            lisa"오늘 즐거웠다고, 토머"
            stephan"나도"
            "보우만은 같이 데려갈 수 없었다."
            "어쩌면 위험한 사람이 있을지도 모르는데……{cps=2} {/cps}괜히 위험에 처하게 되면 전부 내 잘못이니까"
            scene black with dissolve
            stop music
            play bgs"bgs/street.mp3"
            scene ev sky_eve with moveup
            "나는 혼자서 폰에 표시된 지도를 따라 이동했다."
            "폰을 계속 켜둔 탓인지 배터리가 벌써 다 떨어졌다."
            "그래도 이렇게 무사히 윌리가 있을거라 생각 되는 장소에 도착 했는데……"
            stop bgs
            scene bg case2_outside with movedown
            "……꽤나 무서워 보이는 폐건물 이었다."
            "여기 근처엔 도로가 없어서 그런지 정말 조용했다."
            stephan_think"아무래도 이렇게 통행이 없으니까 폐건물로 남아 있는거겠지 하하……"
            stephan"후우─"
            "나는 크게 심호흡을 하고 안으로 들어가기로 했다."
            play sound "se/footsteps_concrete.mp3"
            show bg case2_outside at Zoom((1280,720),(0,0,1280,720),(315,397,575,323),2.0) with dissolve
            $ renpy.pause(2.0)
            show stephan talk:
                zoom 1.8 xalign 0.4 yalign 0.0
            stephan"어?"
            "안으로 들어가려는 중 뭔가 눈에 띄었다."
            stephan_think"비닐로 포장된게……{cps=2} {/cps}빵 같은 건가?"
            "편의점 이나 마트 같은데서 볼 수 있는 그런 종류의 빵 이었다."
            play sound "se/search_bag.mp3"
            show stephan talk:
                linear 0.4 xalign 0.5 yalign -0.2
                linear 0.4 xalign 0.4 yalign 0.0
            $ renpy.pause(0.4)
            show ev cheese_cream with dissolve:
                xalign 0.6 yalign 0.9 zoom 1.6
            "나는 빵을 들어서 좀 더 자세히 살펴봤다."
            stephan_think"이건……"
            extend" 크림 치즈 빵 이로군……"
            "게다가 땅에 떨어진 거 치곤 상태가 매우 깨끗했다."
            stephan_think"마치 어제 떨어진 것 처럼……"
            play sound "se/static.mp3"
            scene bg mansion_hall_night at Zoom((1280,720),(905,83,375,211),(0,167,750,422),0.0)
            show seb shock:
                zoom 1.5 xalign 0.0 yalign -0.2
            $ renpy.pause(0.4)
            scene bg case2_outside at Zoom((1280,720),(480,80,647,364),(315,397,575,323),0.0)
            show stephan shock:
                zoom 1.8 xalign 0.4 yalign 0.0
            show ev cheese_cream:
                xalign 0.6 yalign 0.9 zoom 1.6
            stephan_think"…………"
            "갑자기 불안했다."
            "어제 밤에 세바스찬이 오는 길에 들었다는 비명 소리가……{cps=2} {/cps}혹시 여기서 나온게 아닌가……"
            play music "bgm/sirius5.mp3"
            "만약 그게 사실 이라면 안엔 꽤 위험할지도 모른다."
            play sound "se/think.mp3"
            scene bg case2_outside_night at Zoom((1280,720),(315,397,575,323),(315,397,575,323),0.0) with flash
            $ renpy.pause(0.5)
            scene bg case2_outside_night at Zoom((1280,720),(315,397,575,323),(480,80,647,364),0.3)
            show effect1
            play sound "se/shock.ogg"
            $ extra_name = '비명소리'
            extra"{size=45}으아아아아아─!!{/size}" with lshake
            scene bg case2_outside at Zoom((1280,720),(480,80,647,364),(480,80,647,364),0.0) with flash
            $ renpy.pause(0.5)
            scene bg case2_outside at Zoom((1280,720),(480,80,647,364),(315,397,575,323),0.6)
            $ renpy.pause(0.6)
            show stephan shock:
                zoom 1.8 xalign 0.4 yalign 0.0
            show ev cheese_cream:
                xalign 0.6 yalign 0.9 zoom 1.6
            stephan_think"제발……{cps=2} {/cps}아무 일도 없어야 할텐데"
        
    "다시 한번 크게 심호흡을 하고 건물로 다가간다."
    play sound "se/footsteps_concrete.mp3"
    scene bg case2_outside at Zoom((1280,720),(315,397,575,323),(156,359,350,197),2.4)
    $ renpy.pause(2.4)
    scene bg case2_inside with moveright
    "내부도 외부 묻지 않게 낡았다."
    "곳곳엔 쓰레기와 거미줄, 거기다 왠지 곰팡이 냄새가 나는 것 같기도 하고……"
    "어림잡아서 몇 년간은 방치된 건물 같은 느낌이 들었다."
    scene bg case2_inside at Zoom((1280,720),(0,0,1280,720),(743,342,491,277),0.3)
    $ renpy.pause(0.3)
    show stephan fear:
        zoom 1.8 yalign 0.0 xalign 0.4
    stephan_think"머머머머, 뭔가 혼자서 오니까 더 무섭다"
    stephan_think"이럴 줄 알았으면 그냥 보우만 이랑 같이 오는 건데……!"
    "하지만 지금와서 이렇게 생각해도 의미가 없다는 건 잘 알고있다……{cps=2} {/cps}거기다 보우만을 위험에 빠뜨리지 않겠다고 혼자 약속 했으니까"
    "일단 여기에 윌리가 있다고 지도엔 표시 되어 있지만, 그래도 난 신중하고 싶다."
    "아무도 없는 평범한 폐건물에 혼자 방황 하는 건 원치 않으니까"
    stephan_think"우선은 여기에 사람이 살고 있다는 증거를 찾아보는거야"
    scene bg case2_inside with dissolve
    show inspect_mode: # 탐색모드 시작
        alpha 1.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
    $ renpy.pause(2)
label case2_search:
    call screen case2_imagemap
    $ result = _return
    if result == "wall":
        scene bg case2_inside at Zoom ((1280,720),(0,0,1280,720),(905,335,375,211),0.5) with dissolve
        $ renpy.pause(0.5)
        show stephan shock with dissolve:
            zoom 1.3 xalign 0.5 yalign -0.1
        "나는 벽에 나가가서 손으로 살짝 만져봤다."
        "그랬더니 흙먼지가 손에 묻어 나오면서 땅에 떨어졌다."
        stephan_think"정말 건들기만 해도 무너져 버릴 것 같이 오래된 건물이네……"
        stephan_think"이런 건물에 윌리랑 크라운이 진짜로 있는 걸까?"
        scene bg case2_inside at Zoom((1280,720),(905,335,375,211),(0,0,1280,720),0.5) with dissolve
        jump case2_search
    if result == "entrance":
        scene bg case2_inside at Zoom ((1280,720),(0,0,1280,720),(459,240,270,152),0.5) with dissolve
        $ renpy.pause(0.5)
        "……정말 다시 나가고 싶은 마음은 굴뚝같다."
        "하지만 그렇다고 윌리랑 크라운을 버릴 수도 없다."
        "한때 윌리가 말했던 것 처럼……"
        play sound "se/think.mp3"
        scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(531,286,553,312),0.0) with flash
        show willy talk:
            zoom 1.4 yalign -0.3 xalign 0.8
        show stephan sirius:
            zoom 1.4 yalign -0.3 xalign 0.35
        willy"설령 그것이 나랑 관련 없는 사람 이라고 해도!"
        willy"내가 바꿀 수 있다는 사실을 알면서 모른척 할 순 없어"
        show willy
        willy"안 그러면 죄책감이 들잖아?"
        scene bg case2_inside at Zoom ((1280,720),(0,0,1280,720),(459,240,270,152),0.0) with flash
        stephan_think"…………"
        "만약 이대로 돌아 간다면, 녀석들이 내 꿈속에서 계속 나를 괴롭히겠지"
        stephan_think"하지만 여기에 최근까지 사람이 있었다는 증거가 없으면 그냥 돌아가도 될지도……?"
        scene bg case2_inside at Zoom ((1280,720),(459,240,270,152),(0,0,1280,720),0.5) with dissolve
        jump case2_search
    if result == "floor":
        scene bg case2_inside at Zoom((1280,720),(0,0,1280,720),(689,466,429,242),0.5) with dissolve
        $ renpy.pause(0.5)
        show stephan shock:
            zoom 1.5 xalign 0.4 yalign -0.3
        "나는 무릎을 꿇고 바닥에 손을 짚었다."
        stephan_think"먼지가 엄청나네……"
        "거기다 흙도 장난 아니었다."
        "먼지를 손으로 이리저리 털어보니까 콘크리트 바닥이 보였다."
        "사람 이라곤 눈꼽 만큼도 없었을 것 같았다."
        stephan_think"윌리……{cps=2} {/cps}정말로 여기에 있는거야?"
        "혼자서 생각 해보지만, 역시나 답은 오지 않았다."
        scene bg case2_inside at Zoom((1280,720),(689,466,429,242),(0,0,1280,720),0.5) with dissolve
        jump case2_search
    if result == "2ndfloor":
        scene bg case2_inside at Zoom((1280,720),(0,0,1280,720),(0,181,566,319),0.5) with dissolve
        $ renpy.pause(0.5)
        "나는 입구 중앙에서 가만히 난간 쪽을 바라봤다."
        "저긴 2층으로 이어져 있다."
        stephan_think"내 기억이 맞다면 이 건물은 최대 5층 까지 있었어"
        stephan_think"정말로 여기에 윌리가 있다는 걸 알게 된다고 해도, 이 건물 어디에 있는 진 알 수 없겠는데;;"
        stephan_think"그래도 시도는 해보자"
        stephan_think"이건 단순히 윌리를 구하기 위한게 아니라, 보우만의 친구인 앤 크라운을 되찾는 거 이기도 하니까"
        stephan_think"나 혼자서 멋대로 포기 할 순 없어!"
        scene bg case2_inside at Zoom((1280,720),(0,181,566,319),(0,0,1280,720),0.5) with dissolve
        jump case2_search
    if result == "garbage":
        scene bg case2_inside at Zoom((1280,720),(0,0,1280,720),(677,273,337,191),0.5) with dissolve
        $ renpy.pause(0.5)
        show stephan shock:
            xalign 0.3 yalign 1.0
        "나는 쓰레기가 모여있는 구석진 곳에 다가갔다."
        "플라스틱 쓰레기에 각종 고철과 의자……"
        "아무래도 이 건물이 폐쇄되기 전에 필요 없는 물건들은 전부 여기로 폐기처분이 됐나보다."
        stephan_think"근데 뭔가 부자연스러워……"
        "왜 쓰레기 중에서 최근에 버려진 것 같은 게 있을까?"
        show stephan fear
        stephan_think"정말 여기에 사람이 살고 있는 건가?!"
        "게다가 버려진 쓰레기 들은 대부분 식품의 포장지……{cps=2} {/cps}누군가 여기서 생활 하고 있었다."
        stop music
        play sound "se/footsteps_running.mp3"
        scene bg case2_inside at Zoom((1280,720),(677,273,337,191),(0,181,566,319),0.3)
        "그때 윗쪽 난간에서 누군가 달리는 들렸다."
        stephan"{size=45}누, 누구세요?!{/size}"
        "아무런 대답이 없었다."
        "하지만 방금 쓰레기도 그렇고, 발소리도 그렇고. 여기엔 누군가 있다."
        "그리고 그 사람은 윌리와 크라운을 납치한 인물 일 가능성이 매우 높다."
        stephan_think"일단 발소리가 났던곳으로 가보자"
        stephan_think"혹시 아무것도 없다면 다시 돌아오면 되는거고……"
        play sound "se/footsteps_concrete.mp3"
        scene black with moveright
        "나는 아까전에 발소리가 들렸던 곳을 향해서 계속 걸었다."
    scene bg case2_inside2 with moveright
    stephan_think"여기가 2층 인가……"
    "일단 방 구조는 매우 단순했다."
    "역시 폐건물이라 그런지 안엔 아무런 인테리어도 없고, 먼지만 가득했다."
    show bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(0,264,561,316),0.5)
    stephan_think"발소리가 저 쪽에서 나왔던 거 같던데……"
    play sound "se/footsteps_concrete.mp3"
    scene black with moveright
    scene bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(387,325,435,245),0.0) with moveright
    stephan"……?"
    stephan_think"기분 탓인가?"
    scene black with moveright
    scene bg case2_inside2 at Zoom((1280,720),(0,0,1280,720),(29,404,476,269),0.0) with moveright
    stephan_think"뭐지……"
    scene black with moveright
    scene bg case2_inside2 with moveright
    stephan_think"…………"
    play sound "se/shock.ogg"
    show effect1
    stephan_think"{size=45}이건 뭐냐고?!{/size}" with lshake
    hide effect1
    "처음엔 그냥 기분탓 인 줄 알았다."
    extend" 하지만 계속 돌아 다녀 본 결과, 그게 아니라는 걸 알았다."
    stephan_think"이 건물……{cps=2} {/cps}방 구조가 똑같아……"
    "완벽하게 똑같은 건 아니지만, 인테리어가 워낙 없다보니까 구분하는데 매우 힘들었다."
    stephan_think"조금만 더 이동해보자……{cps=2} {/cps}어쩌면 같은 방을 몇번이고 돌았던 걸 수도 있으니까……"
    scene black with Dissolve(1.0)
    play music "bgm/sad4.mp3"
    "벌써 몇 시간째 걸은 거 같다……"
    "윌리를 찾기 전에 우선 내가 어디 있는지 부터 알고 싶다."
    play bgs "bgs/night.mp3"
    scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(448,369,478,269),0.5) with dissolve
    $ renpy.pause(0.5)
    show stephan fear:
        zoom 1.6 xalign 0.2 yalign -0.2
    stephan_think"원래부터 비슷 한 구조와 텅 빈 인테러에다가 날 까지 어두워 졌으니……"
    "길을 완전히 잃어버렸다."
    "내가 왔던 길을 되돌아가겠다는 의도로 움직였다가 오히려 더 길을 잃어버렸다."
    stephan"조난……{cps=2} {/cps}당한건가……"
    show stephan
    stephan_think"그래 전화를!"
    show stephan talk
    "하지만 누구한테 전화를 해야 할까……"
    "경찰?"
    play sound "se/think.mp3"
    scene bg fastfood_bathroom with flash
    $ extra_name = '통화 상대'
    show phone:
        xalign 0.9 yalign 1.5
    extra"잠깐!{cps=2} {/cps}지도를 확인하기 전에 몇가지 당부할게 있어"
    stephan"뭐죠?"
    extra"첫째, 절대 경찰에게 신고하지 말 것"
    extra"아까 말했듯이 내가 그 주소를 얻은 경로가 좀 거시기 해서 말이야……"
    scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(448,369,478,269),0.0) with flash
    show stephan shock:
        zoom 1.6 xalign 0.2 yalign -0.2
    "……그건 힘들 거 같았다."
    "윌리의 룸메이트한테 전화를 걸어보는 것도 좋겠지만, 발신자 표시제한으로 걸려 왔으니……"
    stephan_think"그냥 경찰이나 구조 대원에게 전화 걸고, 장소를 알게 된 경위는 숨길까?"
    show stephan
    "확실히 좋은 방법 일지도 모른다.{cps=2} {/cps}그렇게 하면 나도 여기서 나갈 수 있고, 윌리랑 크라운도 찾을 수 있으니까"
    scene bg case2_inside2_night at Zoom((1280,720),(448,369,478,269),(664,343,478,269),0.0)
    stephan"당장 전화를!"
    show phone:
        xalign 0.9 yalign 10.0
        linear 0.3 yalign 1.5
    stephan_think"…………"
    "어째서인지 폰에 전원이 안들어온다."
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}왜?!{/size}" with lshake
    stephan"왜 폰에 전원이?!"
    stephan_think"아차……{cps=2} {/cps}여기 오면서 계속 폰을 켜둔 바람에 배터리가 다 나갔었지……"
    scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(448,369,478,269),0.0) with Dissolve(1.0)
    show stephan shock:
        zoom 1.6 xalign 0.2 yalign -0.2
    stephan_think"이제 어쩌지……"
    stephan_think"이런 상태에선 계속 돌아다니기만 해도 내 다리만 아프고……"
    "나한테 매우 큰 위기가 찾아 왔다는 걸 느꼈다."
    "여기서 죽어도……{cps=2} {/cps}아무도 모를거다……"
    show stephan mad
    stephan_think"난 왜 이렇게 멍청할까……"
    stephan_think"여기 오기 전에 미리 준비라도 했으면 좋았을텐데……!"
    play sound "se/think.mp3"
    show phone_unknown with flash
    "전화가 끝나자마자 난 바로 여기로 오겠다고 생각 했다."
    "사전에 미리 준비를 했을 시간은 분명 있음에도!"
    hide phone_unknown with memory
    stephan_think"정말 멍청해……"
    show stephan sirius:
        linear 0.3 xalign 0.5
        linear 0.3 xalign 0.2
    play sound "se/hit.ogg"
    "나는 화풀이로 벽을 쳤다."
    "허나 내 주먹만 아팠지……{cps=2} {/cps}상황은 바뀐게 없었다."
    "내가 멍청하다는 또다른 증거다……"
    extend" 변화를 추구 하면서도 변화를 가져올 행동은 전혀 안 하니……"
    stephan_think"젠장……"
    stephan"젠장! 젠장! 젠장! 젠장!"
    "울고싶다."
    extend" 아주 큰 소리로 엉엉 울고싶다는 충동에 휩쌓였다."
    play sound "se/fall.ogg"
    scene bg case2_inside2_night with dissolve
    stephan"으……"
    "나는 힘없이 먼지로 가득한 땅 바닥에 누워서 천장을 올려다봤다."
    stephan_think"길은 잃었고, 폰에 배터리는 없고, 주변엔 아무것도 없고……"
    stephan_think"친구를 구하겠다는 놈이 가는 길에 길을 잃어버리다니……"
    stephan"하…… 하…… 하……"
    "지금 상황을 되돌아보니, 허탈한 웃음만 나왔다."
    scene black with eyeshut
    "이대로 눈을 감고 조금이나마 안식을 처하려고 했다."
    "지금 난 정신적, 육체적으로 많이 지친 상황이니까……"
    "나는 필사적으로 안 좋은 생각을 떨쳐 내려고 했다."
    "하지만……"
    "내 행동을 곰곰히 생각 해볼수록 화가 치밀어 올랐다."
    "처음엔 친구를 돕겠다는 의지로 여기에 왔지만……{cps=2} {/cps}나의 어리석음 때문에 앞길이 막히고……"
    "근거없는 정의감에 불타 올라버리고……"
    stephan_think"젠장……"
    show ev dic_stephan:
        alpha 0.0
        linear 1.0 alpha 0.7
    stephan_think"그때랑 다를게 하나도 없잖아……!"
    "나는 꽤 성장 했다고 생각했었다."
    "하지만 전부 나의 희망사항에 불과했다는 걸 뼈저리게 느꼈다."
    show ev dic_stephan:
        linear 0.4 alpha 0.0
    stephan_think"아직……{cps=2} {/cps}할아버지의 부탁을 들어주지 못했는데……"
    hide ev dic_stephan
    "며칠 전에 할아버지한테서 연락이 왔을때……{cps=2} {/cps}난 정말 기뻤다."
    "어렸을때 나에게 많은 걸 알려줬던 사람에게 도움이 될 수 있다고 생각했기 때문이었다."
    "난 그저 할아버지한테 도움이 되고 싶었다."
    "그리고 윌리한테도 도움이 되고 싶었다."
    "……하지만 난 자기 자신 조차도 제대로 도울 수 없었다."
    "왜……"
    stephan_think"난 아무것도 못 하는 걸까……"
    stephan_think"만약 이 상황에 처한게 내가 아니라 윌리 였다면……"
    "녀석이라면 분명 이 상황을 극복 할 수 있는 무언가를 찾았을거다."
    show willy:
        zoom 1.7 xalign 0.5 yalign -0.1 alpha 0.0
    stephan_think"걘……{cps=2} {/cps}언제나 정답을 알고 있으니까"
    show willy:
        linear 0.5 alpha 1.0
    "겉으론 윌리를 부정하고, 짜증 나다고 생각하고 있었지만……"
    extend" 실제론 녀석이 하는 말이 전부 정답 이었다는 걸 알고 있었다."
    "난 그런 녀석을 따라잡고 싶었다."
    "처음 만났을때 부터……"
    play bgs"bgs/people.mp3"
    scene ev willy_mid with Dissolve(1.0)
    $ extra_name = '일진 #1'
    extra"정말 괜찮겠어?"
    willy"그래,{cps=2} {/cps}그러니까 지금 당장 꺼져줘"
    extra"그래~ 그래~ 지금은 마음껏 짓걸여도 좋아"
    extra"어이 가자"
    $ extra_name = '일진 #2'
    extra"어……"
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(2.0)
    willy"너, 괜찮아?"
    stephan"으, 응……"
    stephan"그보다 너야말로 괜찮겠어?{cps=2} {/cps}쟤네들……"
    willy"상관없어"
    show willy_mid2
    willy"……라기보단 지금와서 후회해도 소용없겠지?"
    stephan"뭔가 무책임 한 말이잖아"
    willy"그럼 어떻게 할까?{cps=2} {/cps}울면서 후회라도 할까?"
    stephan"…………"
    willy"이름이 분명 스테반 토머 였지?"
    stephan"어……"
    willy"나 여기 전학온지 얼마 안돼서 친구가 없어"
    willy"아까 쟤네들 이랑은 친해질 가능성이 낮아졌지만, 대신에 너랑 친해질 가능성이 생겼지"
    willy"어때?{cps=2} {/cps}나랑 친구가 되어 줄래?"
    stephan"어어?!"
    willy"싫어……?"
    stephan"그런 건 아니지만……{cps=2} {/cps}날 도와준 이유가 그거야?"
    stephan"나랑 친해지려고?"
    willy"아니, 그건 아니야"
    willy"난 그저 \'지금\'할 수 있는 일을 한 거 뿐이야"
    willy"누군갈 도와줄 수 있는 처지에 놓여 있으니까 구해 준 거 뿐. 친구를 만들 수 있으니까 만든 것 뿐"
    stephan"뭔가 복잡한 녀석이네……"
    hide willy_mid2
    willy"그냥 네가 할 만한 대사로 해본건데?"
    stephan"네가 그런 이미지?!"
    willy"어"
    stephan"에헴……{cps=2} {/cps}조, 좋아"
    stephan"네가 친구가 없다고 하니까 특별히 되어 줄게"
    show willy_mid2
    willy"너도 친구 없구나?"
    stephan"으, 응?!"
    scene black with Dissolve(1.0)
    stop bgs
    stop music
    "윌리는 예전부터 뭔가 특이한 녀석이었다."
    "하지만 걔가 이상해서 특이한게 아니라……{cps=2} {/cps}다른 애들과는 다르게 말과 행동이 일치했다."
    "망설임 없이 자신이 지금 할 수 있는 일만 하고……"
    "동요하지 않고 목적만 추구하고……"
    "그럼 나는 어떤가?{cps=2} {/cps}목적은 추구하지만 작은 변수에도 동요하면서 시간을 낭비하고"
    "나는 조금이라도 녀석을 본받고 싶었다."
    stephan_think"그럼 지금 내가 하고 싶은 것은 무엇인가?"
    "윌리와 앤 크라운을 찾는 것"
    stephan_think"나는 나의 목적을 이룰 수 있는가?"
    play bgs"bgs/night.mp3"
    scene bg case2_inside2_night at Zoom((1280,720),(271,0,478,269),(271,0,478,269),0.0) with eyeopen
    stephan_think"…………"
    stephan"그래……"
    play music "bgm/sirius2.mp3"
    "뭘까……{cps=2} {/cps}마음 한쪽에서 뭔가 뜨거워지는 기분이 들었다."
    "지금까지 나는 너무 애매한 상태였다.{cps=2} {/cps}윌리를 구하고는 싶었지만, 내가 할 수 있는지는 전혀 모르고……"
    "과거에 자신을 한탄하면서 후회한다고 여기서 시간을 버리고 있고"
    "하지만 이 문제는 매우 간단했다."
    stephan_think"불가능 하지 않아"
    stephan_think"이 상황에서 반드시 \'진리\'는 존재 해!"
    scene bg case2_inside2_night at Zoom((1280,720),(271,0,478,269),(448,369,478,269),1.0)
    $ renpy.pause(1.0)
    show stephan think:
        zoom 1.6 xalign 0.2 yalign -2.0
        linear 0.4 yalign -0.2
    "나는 자리에서 일어나, 생각했다."
    stephan_think"입구쪽에서 방금 사용 한것 같은 생활 쓰레기가 발견됐어"
    stephan_think"그리고 사람의 발소리도 들렸고……"
    "한가지 확실한게 있다면 \'아직도 이 건물 안에 누군가 있다\'"
    "즉, 절대로 불가능 하지 않다."
    show stephan
    stephan_think"생각해보면 그 사람이 윌리의 행방을 알고있는 인물이건 아니건 사실 상관 없어!"
    "왜냐면 그 사람은 일부러 쓰레기를 입구에다가 버릴 정도로 길을 잘 알고 있다."
    "만약 윌리를 알고 있다면 좋고, 설령 모른다고 해도 이 건물에서 나갈 순 있을테니까 그것도 좋다."
    show stephan talk
    "근데 생각해보니까……"
    show stephan mad
    stephan_think"젠장……{cps=2} {/cps}뭔가 도 윌리한테 도움 받은 거 같은 느낌이네"
    show stephan talk
    "어쨌든, 지금의 난 마음이 많이 진정됐다."
    stephan_think"고작 생각을 바꾸는 것만 가지고 지쳤던 몸도 이렇게 힘이 나오다니……"
    show stephan think
    stephan_think"하지만 마음 가짐을 바꿨다고 해도 근본적인 문제는 해결되지 않았어"
    stephan_think"어떻게 해야 사람을 찾을 수 있을까?"
    "큰 소리를 내면서 돌아다니는 것도 방법이다."
    "하지만 입구에서 들렸던 발소리는 뭔가 도망치는 거 같았다."
    stephan_think"그러면 만나고 싶어도 만나기 힘들겠네……"
    "나는 계속 생각해봤다."
    "이 건물 안에 있는 사람을 찾을 수 있을만한 단서……"
    stephan_think"…………"
    show stephan talk
    stephan_think"그러고 보니까 이 건물은 오래 돼서 그런지, 바닥에 흙먼지가 많았어"
    "그리고 내가 들은 발소리는 누군가 달리는 소리 였다."
    "걸을때 보단 달리때 발 끝에 가해지는 충격이 크다고 한다.{cps=2} {/cps}즉, 이렇게 먼지가 많은 바닥에서 누군가 달리면 먼지가 부자연스러운 형태를 하고있을거다."
    show stephan
    stephan_think"그럴땐 바닥만 열심히 보면서 걸으면 돼"
    "밤이라 잘 안 보이기 때문에 그게 쉽진 않겠지만, 그래도 무력하게 여기서 좌절하는 것보단 훨씬 낫다."
    "그리고 사람의 눈은 어둠에 익숙해질 수 있기 때문에 당장은 힘들더라도, 시간이 지나면 괜찮아질거다."
    stop music
    "즉, 이건 말 그대로 시간 문제다."
    scene black with Dissolve(1.5)
    centered"같은 시각"
    play sound "se/footsteps_concrete.mp3"
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(85,230,669,376),0.0) with Dissolve(0.5)
    show anne yantalk:
        xalign -1.0 yalign -0.4 zoom 1.6
        linear 2.0 xalign 0.3
    anne"위, 윌리……"
    extend" 저 돌아 왔어요"
    willy"…………"
    show anne yan
    anne"그리고 제가 오면서 윌리의 친구를 만났어요!"
    willy"…………"
    show anne yantalk
    anne"근데 한가지 이해가 안되는 게 있어요……"
    play music "bgm/sad2.mp3"
    anne"어떻게 해서 부른거예요?"
    anne"전 분명 이 장소를 알릴만한 단서를 남기지 않았을 텐데……"
    anne"무엇보다 윌리 본인도 여기가 어디 인지 모르도록 제가 조심했어요……"
    anne"일단 제가 건물을 빙 돌아서 길을 잃게 만들었기 때문에 친구는 당분간은 보기 힘들겠지만……"
    anne"그래도 궁금합니다"
    show anne yan:
        linear 0.4 xalign 0.6 yalign -0.7
    anne"무슨 마법을 써서 토머를 이쪽으로 불러들인거예요?"
    scene ev willy_cuffed with dissolve# 동공에 빛을 잃은 상태로 가만히 축 처져서 벽에 기대어 앉아있는 윌리
    willy"…………"
    anne_think"윌리는 어제부터 계속 이런 상태여서 다른 사람에게 신호를 보내는 건 불가능해……"
    anne_think"도대체 무슨 신기한 방법을 사용해서 토머를 이쪽으로 불러 들인걸까?"
    anne_think"하지만 역시 윌리 다워"
    anne_think"이런 위기의 상황에서도 반드시 탈출구를 만들다니♡"
    scene bg case2_inside3_night at Zoom((1280,720),(85,230,669,376),(85,230,669,376),0.0) with dissolve
    play sound "se/search_bag.mp3"
    show anne think:
        yalign -2.0 xalign 0.5 zoom 1.5
        linear 0.4 yalign -0.3
    anne_think"하지만 문제는 그 애를 어떻게 하느냐 인가……"
    anne_think"이런 아무도 찾아올리가 없는 장소에 윌리의 친구가 왔다는 건, 윌리가 무슨 일에 쳐해있는지 알고 있을 확률이 높아"
    anne_think"아직 내가 윌리를 납치 했다는 사실을 알고있다는 보장은 없으니까 잘만 한다면 괜찮을지도 모르겠지만……"
    play sound "se/think.mp3"
    scene bg case2_inside at Zoom((1280,720),(0,0,1280,720),(677,273,337,191),0.0) with flash
    show stephan shock:
        xalign 0.3 yalign 1.0
    $ renpy.pause(1.0)
    scene bg case2_inside3_night at Zoom((1280,720),(85,230,669,376),(85,230,669,376),0.0) with flash
    show anne think:
        yalign -0.3 xalign 0.5 zoom 1.5
    anne_think"상대는 스테반 토머……"
    show anne yanmad
    anne_think"윌리 근쳐에 붙어있는 걸 볼때마다 정말 죽여버리고 싶었던 인물……"
    show anne yan
    anne_think"하지만 여기라면 마음껏 죽여도 괜찮아!"
    anne_think"아무리 비명을 질러도 사람이 있는곳 까지는 닿일리가 없으니까"
    anne_think"그럼 마음껏 괴롭혀도 문제 없겠어……"
    scene ev willy_cuffed at Zoom((1280,720),(572,0,708,401),(0,0,824,467),0.6) with dissolve
    anne_think"한번 윌리의 눈 앞에서 죽여보는 건 어떨까?"
    anne_think"윌리의 절망하는 표정도 보고싶은데……"
    anne_think"윌리의 모든 표정을……"
    stop music
    scene bg case2_inside3_night at Zoom((1280,720),(85,230,669,376),(85,230,669,376),0.0)
    show anne shock:
        yalign -0.3 xalign 0.5 zoom 1.5
    anne"……!"
    anne"내가……"
    play music "bgm/sad3.mp3"
    show anne yanshock2
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}내가 또 이런 생각을 하다니!{/size}" with lshake
    hide effect1
    anne_think"이 이상 가면 안 돼……"
    anne_think"잘못하다간 정말로 사람을 죽이게 될거같아……!"
    anne_think"그래도 토머한테 지금 상황이 들키는 건 위험해……"
    show anne
    anne_think"그, 그럼 토머한테 경고 하는거야"
    anne_think"아직 토머는 내가 가출만 했다고 생각하고 있지, 윌리를 납치했다고는 생각 못 할테니까"
    anne_think"잘만 한다면 아무 문제없이 넘길 수 있어!"
    anne"위, 윌리……{cps=2} {/cps}여기 잠시만 있어주세요……"
    scene black with moveright
    play sound "se/footsteps_running.mp3"
    scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(321,177,772,434),0.0) with moveup
    show stephan think:
        xalign 0.6 yalign 1.0
    stephan_think"이쪽 발 자국은 좀 옅어……"
    stephan_think"여기서부턴 범인이 걸어서 이동 했다는 건가?"
    "그렇다면 여기 근처에 범인의 목적지가 있었다고 할 수도 있다."
    show stephan talk
    stephan_think"그러고 보니까 저기 앞에 위층으로 올라가는 계단이 있어. 혹시 그걸로 위층에 갔나?"
    "지금 나는 —기억 상으론-3층에 있다."
    "여기서 위층으로 이동 했다면 목적지는 4층, 혹은 5층에 있다는 건데……"
    show stephan shock
    stephan_think"그렇다면 구조가 비슷한 방을 1, 2번 더 돌아야 한다는거군"
    "생각만 해도 지친다……"
    show stephan talk
    stephan_think"그래도 조금만 더 힘 내자"
    stephan_think"발자국이 계단 쪽으로 향하는 걸로 봐선 위층에 있을 확률이 높아"
    stephan_think"이정도면 꽤 많은 진전이 있었어!"
    play sound "se/footsteps_concrete.mp3"
    scene bg case2_inside2_night at Zoom((1280,720),(321,177,772,434),(0,177,772,434),1.0)
    "나는 긍정적인 마음 가짐을 가지면서 위층으로 올라갔다."
    scene black with moveup
    centered"4층"
    scene bg case2_inside2_night with moveup
    "역시나 똑같은 방 구조……"
    show bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(403,165,647,364),0.5)
    show stephan think:
        zoom 1.7 xalign 0.5 yalign -0.6
    "나는 바로 발자국을 살폈다."
    show stephan talk:
        linear 0.3 yalign -0.1
    stephan_think"여기서부턴 발자국이 전체적으로 옅어……"
    "범인은 여기서도 걸어서 이동하기 시작했다는 뜻이다."
    stephan_think"하지만 왜 걸어서 이동 했을까?{cps=2} {/cps}계속 달리니까 지쳐서?"
    "이곳은 4층. 그리고 발소리가 들렸던건 2층 난간 쪽"
    "거기서부터 여기 까지의 정확한 거리는 잘 모르지만, 일단 범인이 충분히 지칠만한 거리라는 건 확신 한다."
    show stephan shock
    stephan_think"그럼 엄청 곤란한데……"
    "이유가 어쨌건, 범인이 여기서부터 걷기 시작했기 때문에 발자국이 매우 옅게 나왔다."
    "이곳은 모래사장이 아니라 엄청 오래된 폐건물.{cps=2} {/cps}바닥은 먼지와 모래 뿐이라서 옅은 발자국은 분간하기 힘들다."
    stephan_think"여기서부터 길이 막히기 시작하는군"
    "어차피 지금의 나한텐 선택권이 그리 많지 않다."
    "그냥 발자국의 모양을 봐서 어느 방향으로 이동 했는지 추리해볼 수 밖에 없다."
    show stephan talk
    stephan_think"그럼 이쪽으로 가볼까……"
    play sound "se/footsteps_concrete.mp3"
    show stephan talk:
        linear 1.0 xalign 2.0
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(361,159,746,420),0.0) with moveleft
    "이젠 같은 방만 계속 돌아서 그런지 별로 신기하다는 느낌이 없었다."
    "오히려 이게 더 자연스럽다는 생각에 살짝 안심했다."
    show stephan think:
        zoom 1.8 xalign 0.8 yalign -0.2
    stephan_think"여기도 발자국이 많이 옅어……"
    show stephan shock
    play music "se/footsteps_concrete.mp3"
    "그때 꽤 가까운곳에서 발소리가 들렸다!"
    scene bg case2_inside2_night at Zoom((1280,720),(361,159,746,420),(629,213,651,367),0.3)
    stephan_think"누군가 이쪽으로 오고 있어……!"
    "나는 재빨리 기둥 뒤로 몸을 숨겼다."
    play sound "se/heartbeat.mp3"
    "심박수가 증가하기 시작하면서 긴장됐다."
    "혹시 지금 오는 게 범인 일까?{cps=2} {/cps}여기서 생활하고 있던 노숙자 일까?"
    "어느쪽이든 나한텐 이득이기 때문에 좋았다."
    stop music
    "발소리가 멈췄다."
    stephan_think"혹시 날 봤나?"
    "한동안 정적이 흘렀다."
    "나는 애써 숨죽이고 기다리곤 있었지만……{cps=2} {/cps}긴장감은 어떻게 할 수 없었다."
    "몇 분간 계속 기다렸는데도 아무런 반응이 없었다."
    "왜 그런지 매우 궁금했다."
    menu:
        "숨어서 상태를 확인 한다.":
            "위험한 사람일지도 모르니, 일단 상황을 좀 더 지켜보기로 했다."
            play music "se/footsteps_concrete.mp3"
            "기다린지 3분 정도 지나자, 발소리가 들렸다."
            play sound "se/search_bag.mp3"
            scene bg case2_inside2_night at Zoom((1280,720),(629,213,651,367),(450,213,651,367),1.0)
            "나는 조심스럽게 고개를 내밀어서 상대방을 확인하려고 했다."
            show anne:
                xalign -1.0 yalign 1.0
                linear 3.0 xalign 0.5
            $ renpy.pause(3.0)
            stop music
            stephan_think"……!"
            "어디 본적 있는것 같기도 하고, 아닌것 같기도 한 여자가 왔다."
            "그보다 왜 여기 있는지가 더 중요했다."
            "여기에, 그것도 이렇게 늦은 시간까지 있다는 뜻은 노숙자이거나, 윌리와 크라운을 납치한 범인과 관련 인물 이라는 뜻이다."
            "……근데 분위기가 어느쪽도 아닌 거 같기도 하다."
            play music "se/footsteps_concrete.mp3"
            show anne:
                linear 2.0 xalign -1.0
            $ renpy.pause(2.0)
            "여자는 아무도 없다는 걸 확인 하고는 바로 다음 방으로 이동했다."
            stop music
        
        "상대방을 부른다.":
            play sound "se/search_bag.mp3"
            scene bg case2_inside2_night at Zoom((1280,720),(629,213,651,367),(68,60,938,527),0.5) with dissolve
            show stephan talk:
                zoom 1.3 xalign 0.8 yalign -0.7
                linear 0.3 xalign 0.6 yalign -0.1
            stephan"거기 누구 있나요?"
            show stephan shock
            play music"bgm/sirius5.mp3"
            play sound "se/footsteps_running.mp3"
            "내 말이 끝나기가 무섭게 이쪽으로 달려오는 발소리가 들렸다."
            show stephan shock:
                linear 0.3 xalign 0.5
            "무서워진 나는 무의식적으로 뒷걸음질 쳤다."
            show stephan shock:
                linear 0.2 xalign 0.4
            $ renpy.pause(0.2)
            play sound "se/hit.ogg"
            $ renpy.vibrate(0.3)
            show stephan yawn
            stephan"윽……!" with sshake
            "뒤에 있던 기둥을 눈치체지 못하고 부딫혀 버렸다."
            show stephan shock
            stephan_think"저, 정신 차리자!"
            stephan_think"누군가 이쪽으로 달려오고 있다고!"
            play sound "se/footsteps_concrete.mp3"
            show anne:
                zoom 1.3 xalign 3.0 yalign -3.5
                linear 2.3 xalign 1.1
            $ renpy.pause(2.3)
            stop music
            show stephan talk
            stephan"어?"
            "왠 여자 아이가 이쪽으로 걸어왔다."
            stephan_think"노숙자……{cps=2} {/cps}는 아닌거 같고……"
            "그리고 범인 이라고 하기에도 뭔가 많이 부족한 느낌 이었다."
            stephan_think"그럼 누구지?"
            show stephan shock
            stephan"음……{cps=2} {/cps}저기……?"
            anne"여, 여기서 뭐 하는거예요?"
            "말투도 그렇고, 키나 외모를 통해서 봤을때 약 중학생 정도인거 같다."
            show stephan shock2
            play music "bgm/smooth3.mp3"
            stephan"아하하하……{cps=2} {/cps}그, 그게 내가 길을 잃어 버려가지고……"
            stephan"근데 너야말로 이렇게 늦은 시간에 왜 여기에 있는거야?"
            anne"저, 전……"
            anne"가출……{cps=2} {/cps}했어요……"
            show stephan shock
            stephan"가출?!"
            stephan_think"잠깐만……"
            stephan_think"여긴 어쩌면 윌리랑 크라운이 납치 되어있는 장소야……{cps=2} {/cps}거기다 크라운은 학교에선 가출을 했다고 알려져 있어"
            stephan"혹시 너, 앤 크라운이야?"
            show anne shock
            show stephan
            anne"네,{cps=2} {/cps}맞아요"
            "내가 예상했던 앤 크라운의 이미지랑은 조금 달랐다."
            show lisa smile:
                alpha 0.0
                linear 1.0 alpha 0.4
            "보우만의 친구라길래, 좀 더 키가 크고 밝은 성격일 줄 알았는데……"
            show lisa smile:
                linear 0.5 alpha 0.0
            "이미지야 어쨌건, 찾고싶어했던 인물을 드디어 찾았다!"
            hide lisa smile
            show stephan talk
            "하지만 크라운은 윌리랑 같이 납치 됐을거라 생각 했는데……{cps=2} {/cps}내가 봤을땐 딱히 납치 당한거 같지는 않다."
            anne"그보다 빨리 여기를 떠나주세요!"
            stop music
            stephan"왜?"
            show anne
            anne"여, 여긴 위험해요……"
            stephan"그건 각오하고 왔어"
            stephan"혹시 윌리가 어디있는지 알아?"
            anne"윌리……{cps=2} {/cps}라면 그 3반에 있는 윌리엄 제임스를 말 하는 건가요?"
            stephan"그래, 마지막으로 너랑 같이 있었다는데"
            anne"글쎄요……{cps=2} {/cps}전 계속 여기에 혼자 있었거든요……"
            anne"혹시 무슨 일 있어요?"
            play music "bgm/sad2.mp3"
            stephan"너랑 같이 한 데이트를 마지막으로, 학교에 나오질 않고있어"
            stephan"분명 너라면 걔에 대해서 알고 있을거라고 생각 하는데……"
            anne"제, 제가 어떻게 알겠어요……"
            anne"아까 말씀 드렸다시피 계속 여기 있었는지라"
            stephan"네가 윌리에 대해서 모르겠다면 어쩔 수 없지……"
            stephan"근데 방금 넌 여기가 위험하다고 했던데,{cps=2} {/cps}뭐가 위험한거야?"
            stephan"그보다 여기가 위험하다면서 왜 넌 여기에 있는거야?"
            anne"그야…… 전……"
            "역시나 수상했다."
            "이 장소는 윌리가 있는—적어도 윌리의 휴대폰이 있는—장소인데……{cps=2} {/cps}같이 납치 됐을거라 생각한 크라운이 돌아다니고 있다니"
            show anne yantalk
            play music "bgm/sirius5.mp3"
            play sound "se/cutter.mp3"
            anne"큭……"
            anne"정말 절 참지 못하게 하네요……"
            show stephan shock
            stephan"머, 뭐야……"
            "크라운은 어디선가 꺼낸 커터칼을 들면서 위협했다."
            anne"죽이는 거 만큼은 정말 하기 싫었는데……"
            anne"역시나 토머 스럽게 사람을 짜증나게 하고……"
            show anne yanmad:
                linear 0.3 xalign 0.8
            show stephan shock3
            stephan"……!"
            anne"그냥 토머를 돌려보내는 건 역시 할 수 없어요"
            show anne yan
            anne"제가 아주 오래전부터 꿈꿔왔던 걸 놓치게 되니까……"
            stephan"지, 지금 무슨 소리를 하는거야……!"
            show anne yanmad
            anne"죽이겠어요"
            show anne yanmad:
                linear 0.3 xalign 0.0
            show stephan shock3:
                linear 0.3 xalign 0.0
            $ renpy.pause(0.2)
            play sound "se/hit3.mp3"
            stop music
            scene black with flash
            $ renpy.vibrate(0.3)
            stephan"컥……!" with sshake
            "목에서 엄청난 통증이 왔다."
            "고통을 꾹 참으면서 눈을 천천히 떴는데……"
            scene bg case2_inside2_night with eyeopen
            play sound "se/think.mp3"
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(144,214,476,269),0.0)
            show stephan hurt2 with flash:
                zoom 3.0 xalign 0.5 yalign 0.3
            $ renpy.pause(2.0)
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(42,173,663,374),0.0)
            show stephan hurt2 with flash:
                zoom 1.8 xalign 0.5 yalign -0.1
            play music "bgm/sirius3.mp3"
            "내 목에서 피가 나오고 있었다."
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(399,205,630,356),0.0)
            show anne yan:
                zoom 1.5 xalign 0.3 yalign -0.5
            anne"어때요?{cps=2} {/cps}아프죠?"
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(42,173,663,374),0.0)
            show stephan hurt2:
                zoom 1.8 xalign 0.5 yalign -0.1
            stephan"크으으윽……"
            "말을 하려고 해도 목소리가 제대로 나오지 못했다."
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(399,205,630,356),0.0)
            show anne yantalk:
                zoom 1.5 xalign 0.3 yalign -0.5
            anne"평소엔 윌리한테 딱 달라붙어서 맨날 귀찮게 굴더니"
            anne"정말 꼴이 좋네요"
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(42,173,663,374),0.0)
            show stephan hurt2:
                zoom 1.8 xalign 0.5 yalign -0.1
            "나는 이 여자를 처음 본다……{cps=2} {/cps}하지만 그녀는 마치 예전부터 날 지켜봤다는 듯이 얘기하고 있었다."
            stephan_think"혹시……"
            play sound "se/static.mp3"
            show ev anne_watching
            $ renpy.pause(0.4)
            hide ev anne_watching
            stephan_think"하지만 왜……{cps=2} {/cps}왜 나를 죽이려고……"
            "말은 하고 싶었지만, 목소리는 전혀 나오지 못했다."
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(399,205,630,356),0.0)
            show anne yan:
                zoom 1.5 xalign 0.3 yalign -0.5
            anne"토머, 당신의 괴로워하는 표정도 계속 보고싶긴 하지만……{cps=2} {/cps}윌리가 절 기다리고 있기에 빨리 끝내도록 할게요"
            anne"어차피 제 목적은 윌리를 지킨는 거 뿐이었고요"
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(42,173,663,374),0.0)
            show stephan hurt2:
                zoom 1.8 xalign 0.5 yalign -0.1
            stephan_think"역시 윌리가 어디 있는지 알고 있었어……"
            stephan"넌……"
            $ renpy.vibrate(0.3)
            stephan"으윽……!" with sshake
            "말을 이으려고 했지만, 통증 때문에 쉽지 않았다."
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(399,205,630,356),0.0)
            show anne yantalk:
                zoom 1.5 xalign 0.3 yalign -0.5
                linear 0.3 zoom 4.0 yalign 0.2
            $ renpy.pause(0.3)
            show red:
                alpha 0.8
            $ renpy.vibrate(0.3)
            stop music
            play sound "se/hit3.mp3"
            $ renpy.pause(1.0)
            "크라운은 커터칼을 내 가슴에 박았다."
            play sound "se/stab.mp3"
            show anne yantalk:
                linear 0.5 zoom 1.7 yalign -0.5
            stephan_think"으으윽!"
            "그리고 그대로 칼을 내 몸에서 뽑았다."
            play sound "se/fall.ogg"
            stop bgs
            scene black
            "나는 그자리에서 힘 없이 쓰러졌다."
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(399,205,630,356),0.0) with Dissolve(1.5)
            show anne yanmad:
                zoom 1.5 xalign 0.3 yalign -0.4
            anne"하아……{cps=2} {/cps}하아……"
            anne"드디어 끝났어……"
            anne"내가……"
            show anne yantalk
            anne"내가……"
            show anne yanshock2
            play music "bgm/sad4.mp3"
            anne"아, 안돼……!"
            anne_think"내가 토머를 찔러버렸어!"
            anne_think"이렇게 만은 하지 않겠다고 생각 했는데……"
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(572,454,441,251),0.0)
            show stephan hurt2:
                zoom 1.6 yalign 1.0 xalign 0.5
            "나는 처참하게 쓰러져있는 토머의 모습을 봤다."
            "아직 몸을 움찔 거리는 걸로 봐선 숨은 붙어있는 듯 했다."
            anne_think"지금이라도 지혈을 한다면 괜찮을지도 몰라!"
            "게다가 내가 집에서 나오기 전에 생필품은 다 가져왔었다."
            "그중에서 구급통도 있었다."
            play sound "se/footsteps_running.mp3"
            scene black with moveleft
            "빨리 간다면 토머의 목숨만이라도 건질 수 있을지도 모른다!"
            scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(329,360,442,251),0.5) with Dissolve(1.0)
            show anne:
                zoom 1.6 xalign 0.6 yalign -0.4
            anne"하아……{cps=2} {/cps}하아……"
            play sound "se/search_bag.mp3"
            anne_think"구급약을 여기 어딘가에 내가 놔뒀을텐데……"
            anne"찾았다!"
            anne_think"이걸로 나중에 후회 할 짓은 피할 수 있어!"
            play sound "se/footsteps_running.mp3"
            scene bg case2_inside3_night at Zoom((1280,720),(329,360,442,251),(0,0,1280,720),0.5) with dissolve
            "나는 빨리 토머가 있던곳으로 달려가려는 찰나……"
            scene ev willy_cuffed with dissolve
            "옆에 힘없이 앉아있는 윌리의 모습이 눈에 띄었다."
            "그리고 곰곰히 생각해봤다……"
            anne_think"난 사랑하는 사람과 같이 있기 위해서 그를 납치하고, 부모님을 속여서 이런곳에 며칠간 지내고 있고……"
            anne_think"밖에선 다들 날 찾으려고 경찰에 신고 하고, 윌리의 친구도 여기로 왔고……"
            anne_think"다시 원래대로 되돌아 오기엔 너무 많은 짓을 해버렸어……"
            anne_think"……만약 내가 토머를 만났을때 그냥 순순히 윌리가 있는곳을 알려주고, 나도 같이 돌아갔으면 모든게 정상적으로 됐을지도 몰랐는데"
            anne_think"그런데도 난……"
            play sound "se/think.mp3"
            scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(572,454,441,251),0.0)
            show stephan hurt2 with flash:
                zoom 1.6 yalign 1.0 xalign 0.5
            $ renpy.pause(0.7)
            "내가 지금까지 저지른 만행을 전부 원래대로 되돌릴 수 있는 남자를 칼로 찔러버렸다."
            "설령 내가 당장 달려가서 토머에게 응급 치료를 한다고 해도……{cps=2} {/cps}토머를 살려준다고 해도……"
            "내가 그를 찔렀다는 사실은 바뀌지 않는다."
            scene ev willy_cuffed with flash
            "거기다 윌리를 납치 했다는 사실도 만회하기 힘들어졌다."
            "지금 나는 후회해도 소용없을 정도로 나가버렸다."
            play sound "se/search_bag.mp3"
            scene bg case2_inside3_night at Zoom((1280,720),(0,275,499,283),(0,229,499,283),0.5)
            "……그럼 과연 토머를 치료해주러 가도 아무런 의미가 있는가?"
            "내가 지금 당장 죽어가는 토머를 지혈 해준다고 해서 상황이 더 좋아지진 않는다."
            "지금 난, 나빠지면 나빠지지, 더이상 좋아질 수 없는 상황까지 와버렸으니까"
            stop music
            anne"그렇다면……"
            anne"흐름에 맡기면 되는거야……"
            anne"어차피 좋아 질 수 없다면……{cps=2} {/cps}하고싶은데로……"
            play sound "se/footsteps_concrete.mp3"
            stop bgs
            scene black with Dissolve(1.0)
            centered"몇 분 후"
            $ renpy.pause(1.0)
            stephan_think"으, 윽……"
            scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(640,299,563,319),0.0) with eyeopen
            play bgs"bgs/night.mp3"
            show anne:
                zoom 1.7 xalign 0.5 yalign -0.4
            anne"저, 정신이 좀 드셨나요……?"
            stephan"……!"
            "나는 놀라서 소리치려고 했으나, 목이 아파오면서 하지 못했다."
            anne"이, 일단 제가 할 수 있는 응급 처치는 다 했어요……"
            anne"근데 목은 조금 힘들어서……"
            stephan_think"서, 설마……{cps=2} {/cps}크라운이 날 구해준건가?"
            "하지만 날 이렇게 만든것도 앤 크라운……"
            "얼마나 병주고 약주는 상황인가……"
            anne"저, 저기에……{cps=2} {/cps}윌리가 있어요……"
            stephan"……?!"
            scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(250,294,563,319),0.0)
            play sound "se/search_bag.mp3"
            show stephan shock:
                xalign 2.0 yalign -1.5
                linear 1.0 xalign 1.0 yalign 1.0
            "일단 난 자리에서 일어나, 주변을 살폈다."
            "근데 정말로 크라운의 말대로 윌리가 있었다!"
            scene ev willy_cuffed
            show effect1
            play sound "se/shock.ogg"
            play music "bgm/happy3.mp3"
            stephan_think"{size=45}윌리─!{/size}" with lshake
            "드디어 윌리를 만날 수 있게 됐다."
            "정말 감격의 눈물이 나올뻔했다."
            hide effect1
            anne"윌리……{cps=2} {/cps}토머가 왔어요……!"
            willy"……?"
            "왜 갑자기 크라운이 날 윌리가 있는쪽으로 안내 해준걸까"
            "혹시 날 공격한게 걸렸던걸까?"
            "아니면 뭔가 다른 이유가 있는 걸끼?"
            "……이유야 어쨌건!{cps=2} {/cps}지금은 윌리가 더 중요했다."
            "날 찌른 이유는 나중에 돌아가서 천천히 물어보면 될테니까"
            "그리고 왜 윌리가 이렇게 돼있는지도…… 전부!"
            play sound "se/search_bag.mp3"
            show ev willy_cuffed at Zoom((1280,720),(0,0,1280,720),(0,0,895,507),0.3) with lshake
            stephan"위……{cps=2} {/cps}리……!"
            "나는 윌리를 쎄게 흔들면서 있는 힘껏 목소리를 냈다."
            show bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,314,483,274),0.0) with dissolve
            show anne yanmad:
                xalign 0.5 yalign 1.0 alpha 0.0
            show stephan sad2:
                zoom 1.7 xalign 0.7 yalign -0.2
            show willy shock:
                zoom 1.7 xalign -0.2 yalign -0.2
            willy"스테반……?"
            play sound "se/shock.ogg"
            willy"{size=45}스테반─!{/size}" with lshake
            willy"네가 왜 여기에?!"
            stephan_think"드디어……"
            stephan_think"드디어 내가……"
            show anne yanmad:
                linear 0.5 alpha 1.0
            stephan_think"윌리를 구했어!"
            willy"스테반!"
            stop music
            stop bgs
            show anne yanmad:
                linear 0.3 zoom 1.7 yalign -0.4
            $ renpy.pause(0.3)
            play sound "se/hit2.mp3"
            scene red
            $ renpy.vibrate(0.4)
            willy"……!"
            willy"아, 안돼……"
            scene black
            anne"윌리의 절망하는 표정은 그렇군요……"
            jump game_over
        
    stephan"후우─"
    "나도 모르게 다리에 힘이 풀리면서 안도의 한숨이 나왔다."
    play sound "se/search_bag.mp3"
    scene bg case2_inside2_night at Zoom((1280,720),(0,0,1280,720),(242,141,878,512),0.5) with dissolve
    show stephan talk
    "하지만 아직 안심 하기엔 많이 이르다."
    "여기서 내가 다음에 취해야 할 행동을 생각해보는거다."
    "내가 그녀를 쫓아가면 애들이 있는 곳으로 갈 수 있을지도 모른다."
    "……하지만 만약 저 여자가 내가 처음 입구에서 들었던 발소리의 주인일 경우엔 얘기가 다르다."
    "그땐 날 피했으면서, 지금은 날 찾으려고 한다……"
    "괜히 따라 갔다간 오히려 애들로부터 멀어질 확률이 있다."
    stephan_think"그렇다면 다른 길을 가보자"
    stop bgs
    scene black with Dissolve(1.0)
    centered"얼마 후"
    centered"4층 끝 방"
    scene bg case2_inside3_night with moveup
    play bgs"bgs/night.mp3"
    play sound "se/footsteps_running.mp3"
    show stephan talk:
        zoom 1.8 xalign -2.0 yalign -0.3
        linear 0.5 xalign 0.6
    stephan_think"건물의 끝 쪽이라 그런지, 입구도 하나 뿐이고, 구조도 뭔가 다르네"
    show stephan shock
    "오면서 방 안을 잠깐 둘러봤는데 인기척이 느껴졌다."
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,360,367,206),0.5)
    play sound "se/footsteps_running.mp3"
    $ renpy.pause(0.5)
    scene black with dissolve
    stephan"이건……!"
    play music "bgm/sad4.mp3"
    scene ev willy_cuffed with Dissolve(1.0)
    "윌리가 있었다!"
    stephan"야!{cps=2} {/cps}너 괜찮아?!"
    "윌리의 어깨를 붙잡고 살짝 흔들어 봤지만 큰 반응이 없었다."
    "일단 숨은 쉬고 있고, 눈도 드믈게 깜빡이는 걸로 봐선 살아는 있다."
    "그리고 뭔가 작게 중얼 거리는 거 같기도 한데 들리진 않았다."
    stephan_think"근데 앤 크라운은 어디있지?"
    play sound "se/search_bag.mp3"
    scene bg case2_inside3_night at Zoom((1280,720),(0,360,367,206),(0,83,967,544),0.0) with dissolve
    "다시한번 살펴봤지만 여긴 윌리 한명 뿐이다."
    stephan_think"혹시 다른 방에 있나?"
    stephan_think"아니야……{cps=2} {/cps}그렇게 하면 범인 혼자선 힘들거야"
    "만약 범인이 다수 일 경우엔 크게 문제가 없지만, 내가 지금까지 본 증거들을 토대로 생각해보면 범인은 한 명일 가능성이 높다."
    "그럼 크라운은 어디에 있는 걸까……"
    "내가 지금 생각해 볼 수 있는 가능성은 총 3개"
    "크라운은 어떠한 이유에 의해서 풀려나갔고, 지금은 다른데 있다."
    "아니면 크라운은 사실 윌리의 납치나, 고드윈 이랑 아무런 관련이 없고, 학교에서 알려진 대로 가출이며, 둘이 동시에 결석을 한 건 우연이다."
    "마지막으로……"
    play sound "se/static.mp3"
    scene bg case2_inside2_night at Zoom((1280,720),(629,213,651,367),(450,213,651,367),0.0)
    show anne:
        xalign 0.5 yalign 1.0
    $ renpy.pause(0.5)
    scene bg case2_inside3_night at Zoom((1280,720),(0,360,367,206),(0,83,967,544),0.0)
    "내가 오면서 본 여자 아이가 사실 앤 크라운이다."
    "처음 두 가설은 그렇다 쳐도 마지막 가설이 진실일 경우 꽤 문제가 된다."
    "왜냐면 크라운이 윌리를 납치한 흑막 이라는 뜻이 되니까……"
    "하지만 그건 어찌됐든 상관 없다!"
    "내가 여기까지 온 이유는 단 하나, 윌리를 데리고 나오는 것"
    "범인이 누구건, 왜 납치했건, 진실은 지금 나에게 중요하지 않다."
    "괜히 진실을 알려고 했다간, 내가 처음 가졌던 목적을 잃어버릴 수도 있으니까"
    "일단 윌리부터 깨워 보는거다.{cps=2} {/cps}자세한 탈출 계획은 그때 짜면 된다."
    scene ev willy_cuffed with dissolve
    stephan"윌리!{cps=2} {/cps}정신 차려!" with sshake
    willy"…………"
    "여전히 들리지 않을 정도 작게 뭐라고 중얼거리고 있었다."
    stephan"도대체 무슨 일이 있었던거야……"
    "지금 윌리의 상태를 봤을때……{cps=2} {/cps}어제 세바스찬이 들었다는 비명소리의 주인은 윌리가 맞는가보다."
    "무슨 일을 당했는진 모르겠지만, 지금은 움직이기 힘든 상태다."
    "게다가 손이 수갑으로 파이프랑 연결 돼있어서 강제로 옮기는것도 힘들 것 같고……"
    "설령 성공한다 해도 내 체력으론 녀석을 업고 나가는 건 절대 무리다."
    play sound "se/search_bag.mp3"
    scene bg case2_inside3_night at Zoom((1280,720),(0,263,532,299),(48,274,646,363),0.6) with dissolve
    show stephan mad:
        xalign 0.6 yalign 1.0
    "겨우 길을 찾았다 싶었더니 다시한번 시련이 찾아오다니……"
    "화가 치밀어 올랐다."
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,360,392,220),0.0)
    show phone:
        xalign 0.9 yalign 10.0
        linear 0.3 yalign 1.5
    "지금 내가 가지고 있는 건 방전돼서 쓸모가 없어진 이 휴대폰 뿐"
    "게다가 나에게 주어진 시간도 얼마 없다."
    "빨리 윌리의 수갑을 풀 방법을 찾지 않으면 내가 오면서 본 여자가 다시 이쪽으로 올지도 모르는데……"
    "그 여자가 누군진 몰라도, 여기 있다는 건 위험한 인물 일 확률이 있으므로 되도록이면 피하는 게 좋다."
    show black with eyeshut
    stephan_think"자원도, 시간도 얼마 없는 상황에서 수갑으로 구속되어있는 건장한 남성을 데리고 출구가 어디 있는지 모르는 건물을 나가라니……"
    stephan_think"이건 정말로 불가능해"
    stop music
    "지금 나에게 주어진 선택권……{cps=2} {/cps}윌리를 계속 깨워보거나, 누군가 이쪽으로 올때까지 기다린다."
    "하지만 내가 아무리 윌리를 깨우려고 해도, 아무런 반응이 없었다."
    stephan_think"뭘 어떻게 해야 되는지……"
    "나는 속수무책으로 가만히 앉아 있어야 했다."
    "가만히……"
    "아무것도 안 하면서 무기력하게……"
    $ renpy.pause(1.0)
    stop bgs
    play sound "se/heartbeat.mp3"
    scene bg galaxy at blur with flash
    play music "bgs/space.mp3"
    $ renpy.pause(1.0)
    show black with eyeshut
    $ renpy.pause(0.4)
    scene bg galaxy with eyeopen
    show expression (StarField().sm) as starfield with dissolve
    "우주……" with moveup
    "매우 신비롭고 우리가 아직 모르는 게 많은 미지의 공간……"
    "우주는 \'무(無)\'라고 할 수도 있으며 \'유(有)\'라고 할 수 있다."
    "우주에선 속도와 질서가 무의미 해진다."
    "지금 내가 우주 한복판에 멈춰 있을 수도 있고, 어쩌면 빛의 속도로 이동 하고 있을 수도 있다."
    "왜냐면 우린 공기에 있는 입자간의 마찰로 속도를 체감 하기 때문이다."
    "지구엔 공기가 널렸기 때문에 우리가 빠른 속도로 이동하면 바람이 스쳐지나가는 게 느껴진다."
    "하지만 우주는 계속해서 빠른 속도로 팽창 하다보니까 입자간의 간격이 넓여지면서 거의 완벽한 진공상태에 가까워 지고있다."
    "그러니 우주에서 아무리 빠른 속도로 이동을 해도 이동하는 당사자는 아무것도 느낄 수 없다."
    "거기다 우주에선 별들간의 간격이 천문학적으로 멀리 떨어져 있다."
    "설령 사람이 빛의 속도로 이동하고 있다고 해도 시각상으론 차이를 느끼기 힘들다."
    "우주에서 나의 속도는 무 이기도 하며 유 이기도 하다."
    "정지해 있거나, 빠른 속도로 이동 하거나, 당사자는 아무런 차이를 느낄 수 없다."
    "그래서 중요한건 진실이 아닌, 지금 나의 상태에 대한 \'해석\'"
    "지금 내가 이동하고 있는지, 정지해 있는지를 어떻게 해석 하는지가 중요하다."
    "그리고 그 해석은 다른 이들에겐 무의미 하기 때문에 내 자신만 이해 할 수 있는 방법으로 해석하면 된다."
    "수학이랑 마찬가지다."
    "곱셈 공식을 어떻게 외우든 상관 없다."
    extend" 그냥 자신이 이해 할 수만 있으면 된다."
    "그리고 이 법칙은 나 뿐만 아니라, 다른 이들에게도 적용된다."
    "진실이 어찌됐건, 내가 그들의 이해를 조작하는 것이 가능하다."
    "남의 이해를 조작해서 자신이 원하는 결과를 얻어내는 걸 사람들은 \'사기\'라고 부른다."
    "하지만 사기꾼이 뭘 말했든, 그들이 한 말을 이해한 건 바로 사기를 당하는 사람"
    "그렇다면 나 자신에게 사기를 치는것이 가능한가?"
    "내가 이해하고 있는 \'진실\'을 내가 원한는 진실로 조작 하는것이 가능한가?"
    "이런걸 \'자기암시\'라고 한다."
    "나쁘게 표현하면 \'현실도피\'"
    "하지만 내가 아까 말했듯이, 객관적인 진실은 무의미하다."
    "그것에 의미를 부여하는 것은 바로 나 자신이며, 그걸 이해하는 것도 나 자신이다."
    "그렇다면 지금 내가 이해하고 있는 진실을 한번 재해석 해보자"
    "그리고 사기를 쳐보자"
    stop music
    scene black with eyeshut
    play bgs "bgs/night.mp3"
    $ renpy.pause(1.0)
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,360,392,220),0.0) with eyeopen
    stephan"…………"
    stephan_think"또 이런 느낌이……"
    "얼마전에 수업시간에서 느꼈던 느낌이랑 정말 비슷했다."
    "앞에 우주가 펼쳐져 있는거 같았고, 몸이 붕 떠있는 느낌에 왠지 모르게 머리가 맑아지는 기묘한 기분"
    "도대체 뭘까……"
    "최근엔 할아버지 일과 윌리의 일로 난 게임을 단 한시간도 하지 못했다."
    "즉, 이건 단순히 게임을 많이 해서 나오는 현상은 아니라는거다."
    play sound "se/search_bag.mp3"
    show phone:
        xalign 0.9 yalign 10.0
        linear 0.3 yalign 1.5
    stephan_think"하지만……"
    stop bgs
    scene black
    extend" 이 상황을 어떻게 하면 견뎌낼 수 있는지 알 거 같아!"
    centered"3층 4번째 복도"
    play bgs "bgs/night.mp3"
    play music "bgm/sirius5.mp3"
    scene bg case2_inside2_night with Dissolve(1.0)
    show anne think:
        zoom 1.6 xalign 0.3 yalign -0.4
    anne_think"여기도 없는 건가……"
    show anne
    anne_think"이제 슬슬 잠 잘 시간이 된거 같으니까 얼른 돌아가야겠어"
    anne_think"토머는 가만히 놔두면 알아서 죽어 주겠지"
    stop bgs
    scene black with moveright
    $ renpy.pause(0.5)
    play bgs "bgs/night.mp3"
    scene bg case2_inside3_night with moveright
    play sound "se/footsteps_concrete.mp3"
    show stephan sirius:
        zoom 1.5 xalign -2.0 yalign -0.2
    show anne:
        zoom 1.6 xalign 2.0 yalign -0.4
        linear 2.1 xalign 0.5
    $ renpy.pause(2.1)
    show stephan sirius:
        linear 0.3 xalign 0.3
    stop music
    stephan"움직이지마"
    show anne yanmad
    anne"……!"
    show bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(350,97,579,327),0.0) #앤 강조
    show anne yanmad:
        zoom 3.0 yalign -0.1 xalign 0.5
    show stephan sirius:
        zoom 2.9 yalign 0.0 xalign -2.0
    play music "bgm/sirius5.mp3"
    stephan"지금 내 손에 있는 게 뭔지 알겠으면 가만히 있는 게 좋을거야"
    anne_think"이 목소리는 토머 인가?"
    anne_think"그리고 지금 내 목 뒤에 느껴지는 감촉……"
    anne_think"차가운 금속 재질이야"
    anne_think"총?{cps=2} {/cps}아니면 칼?"
    anne_think"어느쪽이든, 이 건물 안에선 있을리가 없는 거야"
    anne_think"즉, 여기 오기 전부터 소지 하고 있었다는 뜻"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),1.0) #스테반 강조
    show anne yanmad:
        linear 1.0 xalign 1.6
    show stephan sirius:
        linear 1.0 xalign 0.5
    $ renpy.pause(1.0)
    stephan_think"반응을 보니까 넘어 온 듯 하군"
    stephan_think"이대로 계속 속아주기만 하면 괜찮을지도 몰라……"
    stephan"저기 있는 수갑의 열쇠……{cps=2} {/cps}네가 가지고있지?"
    anne"네……"
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne yanmad:
        linear 0.3 xalign 0.5
    show stephan sirius:
        linear 0.3 xalign -2.0
    anne_think"역시 지금 내 뒤에 있는 사람은 스테반 토머야"
    anne_think"그리고 목적은 윌리를 데리고 가는거 같고"
    anne_think"하지만 토머 따위의 사람이 총이나 칼 같은 위험한 무기로 사람을 위협 할 리가 없을텐데……"
    anne_think"혹시 모두 허세?"
    anne_think"하지만 윌리가 여기에 감금돼 있다는 걸 알고 왔어"
    anne_think"무엇보다 윌리에 대해서 아는 사람이라면 날 하데스랑 아는 사람이라고 생각하고 있을거야"
    anne_think"위험한 사람들이 윌리를 납치 했을지도 모르는데 아무것도 없이 혼자서 무턱대고 쳐들어갈 바보는 없지"
    anne_think"즉, 호신용품 한 두개 정도는 소지하고 있을 확률이 높아"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne yanmad:
        linear 0.3 xalign 1.6
    show stephan sirius:
        linear 0.3 xalign 0.5
    stephan_think"조용한걸로 봐선, 지금 쯤 이 상황에 대해서 이것저것 분석과 추리를 하고 있겠는가보군"
    stephan_think"저대로 혼자서 상황을 멋대로 \'해석\'하도록 놔두는 게 좋아"
    stephan_think"괜히 상대방의 생각을 어지럽혀서 내가 지금 들고 있다는 게 뭔지 들키면 곤란하니까"
    stephan_think"지금 난 상대방이 내가 흉기를 들고 있다고 해석하도록 생각을 유도하기만 하면 돼"
    stephan"당장 열쇠를 내놔,{cps=2} {/cps}안 그러면 널 죽이겠어"
    stephan"참고로 여긴 사람의 발길이 전혀 닿이지 않는다는 걸 알고 있겠지?"
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne yanmad:
        linear 0.3 xalign 0.5
    show stephan sirius:
        linear 0.3 xalign -2.0
    anne"큿……"
    anne_think"토머가 정말로 그런 짓을 할 거라고는 생각 하지 않지만……"
    anne_think"실제로 여기라면 죽여도 아무도 모를거야"
    anne_think"게다가 난 지금 가출한 상태이기 때문에 토머가 용의선상에 들어올 확률은 거의 없어"
    show anne yanshock2
    anne_think"죽으면……{cps=2} {/cps}윌리랑 같이 있을 수가 없게 돼……"
    anne_think"그거 만큼은 절대로 싫어!"
    show anne yanmad
    anne_think"아, 아니지……"
    extend" 벌써부터 다 끝났다고 생각하지 마"
    anne_think"우선 상대의 무기만이라도 파악한다면 그에 따라서 반격이 가능해"
    anne"열쇠는 드릴게요"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne yanmad:
        linear 0.3 xalign 1.6
    show stephan sirius:
        linear 0.3 xalign 0.5
    stephan_think"좋았어"
    stephan_think"이 관문만 넘긴다면 윌리를 풀어주고 바로 도망가면 돼"
    anne"근데……"
    extend" 열쇠가 2층에 있어서요……"
    anne"거기까지 이동 해야 되는데요……"
    show stephan shock3
    stephan_think"이런……!"
    stephan_think"젠장할……{cps=2} {/cps}쓸대없는 짓을 해가지고……!"
    stephan_think"이대로 움직였다간 내가 지금 손에 들고 있는 게 뭔지 들켜버려……"
    stephan_think"녀석을 데리고 같이 이동을 해도 부딫히는 모양새 때문에 간파 당할 확률도 있어"
    stephan_think"어, 어떻게 해야 되지……"
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne yan:
        linear 0.3 xalign 0.5
    show stephan shock3:
        linear 0.3 xalign -2.0
    anne_think"여기서부터 어떻게 반응을 하는지 잘 살펴보기만 하면 돼"
    anne_think"토머는 열쇠를 찾으러 날 데리고 같이 이동 하거나, 정확한 장소를 물은 뒤 혼자서 이동하거나, 다른데 있다는 건 거짓말이라면서 날 의심할 수 있어"
    anne_think"어차피 열쇠는 지금 내 주머니 안에 있으니까 어느쪽이든 문제 없지만"
    show anne yantalk
    anne"어쩔거예요?"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne yanmad:
        linear 0.3 xalign 1.6
    show stephan shock3:
        linear 0.3 xalign 0.5
    stephan_think"젠장……{cps=2} {/cps}젠장……!"
    stephan_think"이동하지만 않는다면 들키지 않을 거 같지만……"
    stephan_think"오히려 그 행동이 의심을 사게 될지도 몰라"
    stephan_think"으……"
    stephan_think"윌리만 깨어난다면 어떻게 될 수 있을지도 모르지만……"
    show ev willy_cuffed:
        alpha 0.0
        linear 0.7 alpha 0.5
    stephan_think"지금 상태로 봤을땐 답이 없어"
    hide ev willy_cuffed
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne yan:
        linear 0.3 xalign 0.5
    show stephan shock3:
        linear 0.3 xalign -2.0
    anne_think"어쩔거지?{cps=2} {/cps}스테반 토머"
    anne_think"네가 들고있는 흉기만 파악하면 내 커터칼로 어떻게든 반격이 가능해"
    anne_think"후후후……"
    anne_think"넌 절대로 윌리 만큼 똑똑 해 질 수 없어"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne yanmad:
        linear 0.3 xalign 1.6
    show stephan shock3:
        linear 0.3 xalign 0.5
    stephan_think"그보다 이 사람은 무슨 의도로 그런 말을 한거지?!"
    stephan_think"정말로 열쇠는 2층에 있어서?{cps=2} {/cps}아니면 이동 중 반격을 위해?"
    stephan_think"일단 한가지 확실한 건, 자리를 이동하면 나에게 리스크가 생긴다는 점이야"
    show stephan sirius
    stephan_think"근데……{cps=2} {/cps}열쇠가 2층에 있다는 게 사실일까?"
    stephan_think"애초에 왜 2층에 열쇠를 놔두지?"
    extend" 뭔가 많이 비효율적인데……"
    stephan_think"혹시 거짓말?!"
    stephan_think"일단 나한테 그런 거짓말을 할 이유는 충분히 있어"
    stephan_think"내가 이동하게 되면 지금 들고있는 흉기의 정체가 들키게 되니까"
    stephan_think"그리고 그 흉기가 뭐냐에 따라서 다른 전략을 세우려는 계획이겠지"
    stephan_think"하지만 그 수는 읽었다고"
    stephan"거짓말 하지마……{cps=2} {/cps}열쇠는 지금 네가 가지고 있잖아"
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne yantalk:
        linear 0.3 xalign 0.5
    show stephan sirius:
        linear 0.3 xalign -2.0
    anne_think"이동하려고 하지 않는 게 수상해……"
    anne_think"하지만 왜 그런 행동을 보였는지에 대한 이유는 무수히 많아,{cps=2} {/cps}내 목숨이 달린 일인 만큼 섣불리 확신하는 건 금물"
    show anne
    anne"정말 제가 가지고 있다고 생각 하신다면 몸수색 하셔도 좋아요"
    anne"제가 없다고 계속 말 해도 못 믿으실테니까요"
    show anne yan
    anne_think"들고있는 무기가 뭐건, 수색 하려고 주머니에 손을 넣는 순간 이 커터칼로……"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne yanmad:
        linear 0.3 xalign 1.6
    show stephan sirius:
        linear 0.3 xalign 0.5
    stephan_think"그렇게 나오겠단 말이지……"
    stephan_think"확실히 이 자세론 흉기를 들키지 않고도 주머니를 뒤질 수 있어"
    stephan_think"하지만 상대방도 무기를 가지고 있을 경우, 내가 몸 수색을 위해서 주머니에 손을 넣는 순간을 노릴 수 있어"
    stephan_think"그럴땐 재빨리 손을 넣었다가 빼서 피하면 될지도 모르지만……"
    stephan_think"아냐,{cps=2} {/cps}혹시 그랬는데 내가 뒤진 주머니 안에 열쇠가 없게 된다면 큰일이야"
    stephan_think"실제로 피할 수 있을 확률과 열쇠가 들어있는 주머니를 한번에 고를 수 있는 확률……"
    extend" 확률에 확률이 겹치는 상황은 되도록 피하는 게 좋아"
    stephan_think"뭔가 리스크가 적은 방법이 없을까……"
    stephan_think"상대에 대한 정보가 조금이라도 더 있으면 좋을텐데……"
    stephan_think"고드윈이 보낸 사람인지……{cps=2} {/cps}아니면 여기에 있을 것 같았던 앤 크라운 인지……"
    stephan_think"주제를 조금 바꿔보자"
    stephan"혹시 리사 보우만 이라고 알아?"
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne shock:
        linear 0.3 xalign 0.5
    show stephan sirius:
        linear 0.3 xalign -2.0
    stop music
    anne"네?!"
    anne_think"머, 뭐지……"
    anne_think"왜 갑자기 걜……{cps=2} {/cps}무엇보다 어떻게……"
    anne_think"나도 모르게 반응 해버리긴 했지만, 도대체 왜 리사를……"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne shock:
        linear 0.3 xalign 1.6
    show stephan shock3:
        linear 0.3 xalign 0.5
    play music "bgm/sirius1.mp3"
    stephan_think"바, 반응했어……!"
    stephan_think"그럼 범인은 정말로 리사를 알고 있는 앤 크라운 이야?!"
    stephan_think"믿긴 힘들지만 윌리랑 마지막까지 있었던 인물임을 생각해보면 앞뒤는 들어맞아"
    stephan_think"……하지만 왜?"
    stephan_think"뭘 위해서 납치한거지?"
    stephan_think"혹시 고드윈이랑 아는사람 인가?"
    show stephan sirius
    stephan_think"아니야, 그렇다고 하기엔 뭔가 말이 안 돼"
    stephan_think"분명 다른 이유가 있어"
    stephan_think"하지만 상대방이 앤 크라운 임을 알았다면 열쇠를 좀 더 쉽게 꺼내는 방법을 써보자"
    show stephan talk
    stephan"크라운……"
    stop music
    stephan"넌 지금 네가 쳐해 있는 상황을 후회하고 있어?"
    show bg case2_inside3_night at Zoom((1280,720),(195,67,579,327),(350,97,579,327),0.3) #앤 강조
    show anne:
        linear 0.3 xalign 0.5
    show stephan talk:
        linear 0.3 xalign -2.0
    anne"네?"
    stephan"아직 세상에선 널 단순한 가출 청소년으로만 생각하고 있지만……"
    play music "bgm/sad2.mp3"
    stephan"지금 넌 죄없는 한 학생을 납치해서 장기간 동안 감금시킨 범죄자야"
    stephan"뭘 했는진 모르겠지만, 지금 윌리의 상태를 봐바"
    stephan"그리고 저런 짓을 한게 너였다는 걸 다른 사람들이 알게됐을때의 표정을 생각해봐"
    stephan"널 뭐라고 생각할 거 같아?"
    show anne yanshock2
    stephan"다들 널 괴물이라고 생각하면서 피할 걸?"
    anne"그건…… 안 돼……"
    anne_think"내가 윌리를 만나기 전이랑 똑같아져……"
    show stephan sirius
    stephan"앤 크라운!{cps=2} {/cps}이성적으로 생각해봐!"
    stephan"네가 지금 당장이라도 윌리를 풀어준다면 지금까지 아무일도 없었던 것 처럼 해줄 수 있어!"
    stephan"그냥 평범하게 가출한 걸로 만 끝낼 수 있다고!"
    play sound "se/think.mp3"
    show black with flash
    show lisa shock with dissolve:
        zoom 1.8 xalign 0.5 yalign -0.3
    lisa"앤……?"
    lisa"네가 정말로 그랬다고?"
    lisa"거짓말이지……?"
    extend" 그치?"
    anne_think"내가 윌리를 납치해서……{cps=2} {/cps}이리저리 고문한게 알려지면……"
    hide lisa shock
    hide black with flash
    anne_think"난 정말 못살아……"
    show stephan talk
    stop music
    stephan"지금 당장 윌리를 풀어줘……{cps=2} {/cps}그럼 내가 지금까지 본건 전부 없었던걸로 해줄게"
    stephan"어차피 지금 이 상황에 대해서 알고 있는 건 나 뿐이니까"
    anne"…………"
    show anne yantalk
    anne_think"생각해보니까 지금 이 상황은 토머만 알고 있지……?"
    play music "bgm/sad4.mp3"
    show anne yan
    anne_think"그럼 간단해……"
    play sound "se/cutter.mp3"
    anne_think"내가 정체모를 흉기 하나 때문에 겁먹고 있을 이유는 없으니까"
    show bg case2_inside3_night at Zoom((1280,720),(350,97,579,327),(195,67,579,327),0.3) #스테반 강조
    show anne yan:
        linear 0.3 xalign 1.6
    show stephan shock3:
        linear 0.3 xalign 0.5
    stephan_think"잠깐?!"
    play sound "se/fall.ogg"
    stop music
    scene black with flash
    "크라운은 재빨리 커터칼을 꺼내면서 나를 덮쳤다."
    "일단 이리저리 발버둥을 쳐서 칼에 찔리는 건 면했지만……"
    scene ev anne_ontop #앤이 스테반을 덮치고 있는 일러
    show anne_ontop 1
    show black
    hide black with eyeopen
    "몸을 움짝달싹 할 수 없게 됐다."
    "갑작스런 행동 때문에 내 손에서 떨어져 나간 무기를 보면서 크라운은 입을 열었다."
    anne"쳇……{cps=2} {/cps}내가 고작 그딴 휴대폰 따위에 겁먹고 있었다니"
    stephan_think"내가 들고 있었던 무기의 정체를 모른 상태로 덤볐다는 건가?"
    "그렇다. 내가 크라운을 위협하는데 사용한 무기의 진짜 정체가 바로 그거다."
    show phone:
        alpha 0.0
        linear 0.3 alpha 0.6
    "스마트폰"
    "하지만 평범한 스마트폰이 아닌, 아이퐁 5S다."
    "아이퐁은 태두리가 알루미늄 제질로 되어있기 때문에 감촉이 칼이나 총과 비슷하다."
    "거기다 이렇게 어두운곳에서 분위기만 제대로 연출한다면 속아넘어가는것도 무리는 아니다."
    show phone:
        linear 0.3 alpha 0.0
    stephan"스스로가 어떻게 생각 하느냐에 따라서 폰도 위험한 무기처럼 느껴지는 법이야"
    anne"그딴건 이제 상관 없어요.{cps=2} {/cps}토머만 죽으면 조용히 끝낼 수 있어요."
    stephan"…………"
    "나는 지금 앤 크라운의 모습을 보면서 한가지 위화감이 느껴졌다."
    "방금전까지 보였던 침착한 성향이 완전히 없어졌다."
    play sound "se/heartbeat.mp3"
    show bg galaxy with flash
    hide bg galaxy with flash
    play music "bgm/sirius4.mp3"
    "그래도 덕분에 앤 크라운 이라는 사람을 파악했다."
    anne"토머……{cps=2} {/cps}당신만 조용히 하면 들키지 않고 얌전히 끝 낼 수 있어요"
    stephan"정말 그걸로 끝이라 생각 해?"
    stephan"날 죽인 뒤엔 납치범에다가 살인마 라는 죄명만 더 붙을 뿐이야"
    anne"어차피 전 충분히 나쁜 여자예요"
    anne"이 이상 죄명이 늘어난다고 해서 바뀌는 게 있나요?"
    stephan"넌 후회할거야"
    anne"…………"
    stephan"솔직히 말해봐,{cps=2} {/cps}넌 지금도 윌리를 납치한 것에 대해서 계속 후회하고 있잖아?"
    anne"전 그렇지가……"
    "난 눈 한 번 깜빡하지 않고 침착한 어조로 말 했다."
    stephan"네가 학교를 나오지 않게 된 첫 날에 리사 보우만이 너한테 전화 걸었던거 기억나?"
    anne"그, 그건……"
    stephan"그때 넌 이렇게 대답 했다고 했어"
    stop bgs
    play sound "se/think.mp3"
    show black with flash
    show lisa talk:
        zoom 1.4 yalign -0.5 xalign 0.5
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
    hide lisa shock
    play bgs "bgs/night.mp3"
    hide black with flash
    stephan"가장 친한 친구한테 울면서 미안하다고 사과까지 했으면서 후회하고 있지 않다고?"
    anne"아니에요……"
    stephan"지금만 해도 그렇잖아?"
    stephan"아까 전 까지 내가 들고 있었던 무기의 존제를 숙지하고 분석해가는 침착함을 보였다가, 너의 정체에 대해서 알고 있는 게 나 혼자라는 사실을 알자 흥분해서 바로 덤벼들었어"
    stephan"만약 내가 들고 있었던 무기가 진짜였더라면 넌 너의 행동을 깨달고 후회 했겠지"
    show anne_ontop 2 with dissolve
    anne"그, 그럴리가……"
    "나는 눈물을 흘리고 있는 크라운의 마음에 큰 쐐기를 박는 듯 한 말을 했다."
    stephan"너같은 사람을 \'양극성장애 (Bipolar Disorder)\', 혹은 \'조울증(躁鬱症)\'이라고 해"
    stephan"너무 이상적인 결과만 바라보면서 그 과정은 생각 하지도 않고, 그 결과가 불러올 수 있는 다른 일들도 안중에 없고"
    stephan"나중엔 자기가 저지른 일에 후회하면서 자해, 심하면 자살까지 하고"
    stephan"어때?{cps=2} {/cps}뭔가 찔리지 않아?"
    play sound "se/cutter.mp3"
    show anne_ontop 1
    anne"으……!"
    stephan"그건 내려 놔, 여기서 날 죽이는 건 내 추리를 증명하는 꼴이 돼니까"
    anne"도대체 저에 대해서 뭘 안다고 그렇게 말 하는거예요!"
    anne"생각해보면 저랑 제대로 마주어보면서 대화 해보는 게 이번이 처음이잖아요"
    anne"아무것도 모르면서 그렇게 절 환자취급 하는 건가요?!"
    stephan"난 지금 너에게 말 하고 있어!"
    stephan"나의 시각에서 바라본 너가 아니라, 너 자신이 봤을때의 너를"
    play sound "se/heartbeat.mp3"
    stop music
    show bg diary_country at blur with flash:
        crop(58,374,474,266)
        size(1280,720)
    show willy talk:
        xalign 0.5 yalign -0.1 zoom 1.8
    $ renpy.pause(0.5)
    hide willy talk
    hide bg diary_country with flash
    anne"……!"
    show anne_ontop 2 with dissolve
    "크라운은 뭔가를 떠올렸는지, 갑자기 당황하면서 눈물을 흘리기 시작했다."
    play music "bgm/sad2.mp3"
    anne_think"윌리가 왜 그런 말을 했는지, 이제서야 그 진심을 알 거 같아……"
    anne_think"아무리 나에 대해서 모르는 사람이 하는 평가라 해도……"
    extend" 내 자신이 그걸 조금이라도 인정 했다면 그건 막연한 평가가 아닌, 진실이야"
    anne_think"내가 인정하게 된다면……"
    anne_think"하지만……"
    anne_think"{size=35}하지만……!{/size}"
    show effect1
    play sound "se/shock.ogg"
    anne"{size=45}윌리를 사랑하는 걸 어떡하냐고요!!{/size}" with lshake
    hide effect1
    stephan"뭐?"
    anne"전 윌리가 너무 좋은데……{cps=2} {/cps}근데 윌리는 저를 좋아하지 않고……"
    stephan"그럼 넌 납치를 하면 윌리가 널 좋아하게 될거라 생각 했어?"
    anne"그런게 아니라……{cps=2} {/cps}아무런 방해를 받지 않고 둘이서 서로를 알아가는 시간을 만들고 싶었어요……"
    anne"그렇게 해서 윌리도 절 다시보고……"
    scene ev willy_cuffed
    show effect1
    play sound "se/shock.ogg"
    stephan"{size=45}지금 윌리를 봐!!{/size}" with lshake
    stephan"어떻게 같이 시간을 보내면 저런 상태가 돼?!"
    scene ev anne_ontop
    show anne_ontop 3
    anne"윌리의 모든 모습이 보고 싶었던걸요!"
    anne"약한 모습, 웃는 모습, 화내는 모습, 사랑 하는 모습 전부……!"
    stephan"정말 미쳤어……"
    anne"하지만 제가 윌리를 데리고 온 덕분에 이제 둘이서 사귈 수 있게 됐는 걸요?"
    stephan"진짜?"
    stephan_think"도대체 어떻게 된거야……"
    stephan"어쨌건 네가 정말로 윌리를 사랑한다면 그냥 놔둬!"
    show anne_ontop 2 with dissolve
    anne"왜……{cps=2} {/cps}그래야 하는거죠……"
    stephan"넌 뭐가 윌리를 위한건지 알고 행동하는거야?!"
    stephan"너만 좋다고 해서 다 되는 게 아니라고!"
    anne"하지만……"
    extend" 제가 윌리를 위해서 할 수 있는 게 없는 걸 어떻게요……!"
    anne"윌리는 언제나 이성적이고, 빈틈이 없고, 혼자서도 뭐든지 잘하고……"
    anne"무엇보다 다른 사람들에게 인기도 많고"
    anne"제가 계속 혼자서 가만히 있으면 빼앗길까봐 두려웠단 말이에요!"
    anne"이렇게라도 하지 않으면……"
    stephan"정말로 어쩔 수 없었다면 넌 후회같은 걸 하지 않았을거야"
    stephan"안 그래?{cps=2} {/cps}앤 크라운"
    anne"…………"
    stephan"지금 여기서 네가 앞으로 후회하지 않기 위한 행동은 단 하나"
    stephan"윌리를 풀어주는거야"
    stephan"납치 당한 당사자는 어떨련지 모르겠지만, 난 너에 대해서 단 한마디도 안 할거야"
    stephan"그러니까……{cps=2} {/cps}윌리를 구속하고 있는 저 수갑의 열쇠를 줘"
    show anne_ontop 1 with dissolve
    anne"토머가 어떻게 행동하든 전 상관 없어요!"
    anne"하지만……"
    anne"제가 지금까지 윌리한테 그런 짓을 해놓고서 윌리가 과연 가만히 있어줄지……"
    "크라운의 저런 생각이 정말 짜증났다."
    $ extra_name = '목소리'
    stop music
    extra"그거라면……"
    anne"……!"
    "그때 누군가 크라운의 말에 긴박한 목소리로 대답했다."
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,287,482,271),0.4) with dissolve
    play sound "se/chain.mp3"
    show willy shock with sshake:
        zoom 1.7 xalign -0.1 yalign -0.4
    willy"아무런……{cps=2} {/cps}걱정 하지도 않아도 돼……"
    willy"난 절대로 널 원망하지 않을거니까"
    stephan"윌리!{cps=2} {/cps}정신 들었구나!"
    willy"둘이서 꽤 시끄러웠으니까……"
    show willy shock:
        linear 0.4 xalign 0.0
    willy"그보다 앤,{cps=2} {/cps}지금 당장이라도 원래대로 되돌리겠다면 난 너에게 책임을 묻지 않아"
    willy"잘못을 저지르는 것 보다 더 나쁜게 바로 잘못을 해결하려고 하지 않는거니까"
    scene ev anne_ontop
    show anne_ontop 2
    anne_think"윌리……"
    anne_think"내가 그렇게까지 했는데도……{cps=2} {/cps}날 용서하겠다니……"
    stop music
    stop bgs
    scene black
    "지금까지 계속 내가 나빴던거야……"
    "내가 원했던 사랑의 형태가 아니라는 걸 계속 알고 있었으면서도, 잘 모른다는 이유로 이랬으니까……"
    "윌리랑 단 둘이 있으면 어떻게든 될거라고 생각 했던 내가 나쁜거야"
    play bgs "bgs/night.mp3"
    scene bg case2_inside3_night with Dissolve(1.0)
    play sound "se/search_bag.mp3"
    show stephan sirius:
        zoom 1.5 xalign 0.4 yalign -4.0
    show anne yantalk:
        zoom 1.6 xalign 0.5 yalign -0.4
        linear 0.4 xalign 0.8
    $ renpy.pause(0.5)
    show stephan sirius:
        linear 0.4 yalign -0.2 xalign 0.3
    "크라운이 내 위에서 내려오면서 말 했다."
    anne"열쇠는 여기 있어요……"
    stephan"…………"
    play sound "se/footsteps_running.mp3"
    show stephan sirius:
        linear 0.6 xalign -2.0
    "나는 크라운에게 대답하는 대신에 즉시 윌리 쪽으로 갔다."
    scene bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(0,287,482,271),0.4) with moveleft
    play sound "se/footsteps_running.mp3"
    show willy shock:
        zoom 1.7 xalign -0.1 yalign -0.4
    show stephan talk:
        zoom 1.7 xalign 2.0 yalign -0.2
        linear 0.5 xalign 0.5
    willy"네가 왜 여기 있는지 나중에 설명을 들어봐도 될까?"
    stephan"……?"
    stephan"내가 여기 올 걸 모르고 있었어?"
    willy"어"
    show phone2_alarm:
        zoom 2.0 xalign 0.5 alpha 0.0
        linear 0.5 alpha 0.6
    "분명 윌리 폰에서 SOS신호가 나왔는데……{cps=2} {/cps}내가 여기에 올 걸 예상하지 않았다고?"
    hide phone2_alarm with dissolve
    show stephan talk:
        linear 0.3 xalign 0.4
    play sound "se/chain.mp3"
    "나는 윌리의 수갑을 풀어줬다."
    show stephan talk:
        linear 0.3 xalign 0.5
    show willy shock2 with dissolve:
        xalign 0.0 yalign -0.2 zoom 1.6
    willy"으으……"
    show stephan shock
    stephan"괜찮아?"
    willy"네가 내 걱정을 하게 될 줄이야……"
    stephan"며칠간 갑작스럽게 소식이 끊겼잖아"
    extend", 당연히 걱정하지!"
    stephan"거기다 네 폰에 미리 구하러 오라는 SOS 신호를 보내기도 했고……"
    stop music
    willy"내가 그 SOS를 보낸 이유는 따로 있었는데……"
    show stephan talk
    stephan"어?"
    stephan"SOS 면 \'지금 위험한 일에 처해있으니까 구하러 와줘\'라는 의미로 보낸게 아니야?"
    play music "bgm/sirius1.mp3"
    willy"내가 위험한 일에 쳐해 있었다는 건 맞지만……"
    willy"구하러 오라는 의미가 아니라, 앤에게 온 문자를 증거로 경찰들에게 알려주라는 의도였어"
    willy"설마 내가 미쳤다고 위험할지도 모르는곳에 고작 널 보냈겠냐……"
    show stephan shock
    stephan"고작 이라는 말은 좀 너무한데……"
    willy"그보다 여긴 어떻게 알고 왔어?"
    stephan"그보다 고맙다는 인사는 어때?"
    willy"내가 여기서 구출되는 건 계획에 있었던 일이야.{cps=2} {/cps}그냥 구해주는 사람이 조금 바뀌었을 뿐"
    willy"그러니 여기서 불필요한 잡담으로 시간을 낭비하는 건……"
    show stephan mad
    stephan"여기까지 오는데 얼마나 고생했는데……"
    stephan"말 진짜 짜증나게하네"
    willy"…………"
    show willy shock with dissolve
    show stephan talk
    willy"미안……{cps=2} {/cps}어제밤 부터 있었던 일 때문에 머리가 어떻게 됐나봐……"
    willy"와줘서 고마워, 스테반"
    show stephan shock
    stephan"여기서 무슨 일이 있었어?"
    willy"일단 나간 다음에 얘기하자……"
    stephan"어"
    show stephan shock
    stephan"……근데 이 건물에서 나가는 길 알아?"
    willy"아니, 설마 너도 몰라?"
    show stephan shock2
    stephan"오는 길에 헤맸거든"
    willy"…………"
    willy"앤 이라면 알고 있겠지……"
    stop music
    scene bg case2_inside3_night at Zoom((1280,720),(0,287,482,271),(0,0,1280,720),1.0)
    $ renpy.pause(1.0)
    show anne yanshock2 with dissolve:
        zoom 0.9 xalign 0.8 yalign 1.0
    "말이 끝나자, 나랑 윌리는 크라운 쪽을 봤다."
    "……근데 상태가 조금 이상했다."
    play music "bgm/sirius5.mp3"
    "오른손엔 커터칼을 들고 있고, 혼자서 뭐라고 중얼거리는 게 매우 불안한 예감이 들었다."
    "우리 둘은 크라운에게 다가갔다."
    play sound "se/footsteps_concrete.mp3"
    hide anne yanshock2 with dissolve
    show bg case2_inside3_night at Zoom((1280,720),(0,0,1280,720),(633,253,647,364),2.0)
    $ renpy.pause(2.0)
    show anne yanshock2 with dissolve:
        zoom 1.7 xalign 0.6 yalign -0.3
    anne"{size=20}모든게나때문에모든게나때문에모든가나때문에모든게나때문에모든게나때문에모든가나때문에모든게나때문에모든게나때문에모든가나때문에……{/size}"
    "근처에 가니 크라운의 목소리가 작게 들렸다."
    stephan_think"\'모든게 나 때문에\'라니……"
    anne"{size=20}나 같은 게 지금까지 윌리를……{/size}"
    anne"{size=20}난 아무런 쓸모도 없고……{cps=2} {/cps}남들에게 민폐만 끼치는 존재였어……{/size}"
    show ev anne_ontop:
        alpha 0.0
        linear 0.5 alpha 0.5
    show anne_ontop 1:
        alpha 0.0
        linear 0.5 alpha 0.5
    "크라운의 태도가 아까전이랑은 확연하게 바뀌었다."
    stephan_think"조울증이 정말 무서운 병이긴 하구나……"
    stop music
    hide ev anne_ontop
    hide anne_ontop 1
    show anne yantalk:
        zoom 1.8
    "순식간이었다."
    "갑자기 크라운은 자신의 손에 들고있던 커터칼을 높이 들어올리며, 스스로를 찌를듯한 자세를 취했다."
    play sound "se/swing.mp3"
    show willy sirius:
        zoom 1.7 xalign 0.3 yalign -0.2
    show black
    $ renpy.pause(1.0)
    hide black with Dissolve(1.0)
    "윌리는 빠른 동작으로 크라운이 들고있던 커터칼을 낚아챘다."
    willy"너……{cps=2} {/cps}왜 그러는거야……"
    play music "bgm/sad4.mp3"
    show anne yanshock2 with dissolve
    anne"왜그라냐니……"
    extend" 제가 이러지 말아야 할 이유가 있나요?!"
    anne"전 계속 남에게 피해만 주고, 스스로가 생각해서 뭔가를 하면 마지막엔 후회만 하게 되고……"
    anne"제 자신에게 조차 사랑받지 못하는 전……{cps=2} {/cps}이렇게 살아있을 가치가 있을까요……"
    willy"우리가 처음 만났을때 내가 말 했잖아, 자기를 싫어하는 건 그만 두라고"
    willy"근데 보니까 내가 한 말은 전혀 안 지키고 있네……"
    anne"하, 하지만……"
    willy"네가 왜 너를 싫어하는지 혹시 알아?"
    show anne yantalk with dissolve
    anne"아니요……"
    willy"네가 과거에 남의 평가를 싫어했던 성향의 반작용 이라고 생각해"
    willy"넌 남의 평가를 받는 걸 싫어했다보니까 너 자신도 남을 최대한 평가하지 않으려는거겠지"
    willy"그러다보니까 너의 남은 평가대상은 너 자신 뿐"
    willy"그래서 넌 너 자신이 한 선택을 계속 평가하고, 점점 부정적으로 바뀌기 시작하는거라……{cps=2} {/cps}생각해"
    anne"서, 설령 그렇다고 해도……{cps=2} {/cps}어쩌라는거죠"
    willy"널 도와주고 싶어"
    show anne shock
    anne"네……?"
    willy"물론 난 너에 대해서 잘 모르기 때문에 내 제안에 대한 신빙성은 너 자신만 알고 있겠지만……"
    willy"그래도 어떻게든……"
    show anne shock2
    anne"전 어떻게 하면 되는거죠?"
    willy"이제부터 내가 너의 생각을 대신 해줄게"
    willy"네가 충동적으로 생각해낸 행동이 아닌, 내가 너에게 제시해주는 방향을 가"
    willy"그리고 뭔가 후회할 일이 생기면, 너 자신을 탓하지 말고, 나를 책망해"
    willy"그걸 시작으로 계속 무족건 너만 낮게 보려는 성향을 고친다면……{cps=2} {/cps}언젠간 괜찮아지겠지"
    show willy
    willy"나를 믿는다면 말이지"
    show anne with dissolve
    anne"윌리……"
    stop bgs
    scene black
    stop music
    play sound "se/case_start.mp3"
    show case_close
    $ renpy.pause(1.0)
    hide case_close with dissolve
    if pick_game == True:
        play bgs "bgs/night.mp3"
        scene bg sidewalk_night with moveup
        play music "bgm/smooth5.mp3"
        show willy talk:
            zoom 1.6 xalign 1.0 yalign 0.0
        show anne:
            zoom 1.6 xalign 0.0 yalign -0.4
        willy"여기 근처가 네 집이지?"
        willy"집에 돌아가면 부모님한테 꼭 사과 하도록 해"
        anne"조, 조금 두려워요……"
        show willy
        willy"그래도 납치범으로 경찰서에서 만나는거 보단 훨씬 좋잖아?"
        anne"…………"
        show willy talk
        willy"어쨌건 네가 날 납치한거에 관해선 전부 불문으로 쳐 줄게"
        willy"그러니까 안심하고, 앞으로도 괜히 후회할 짓은 하지마"
        anne"근데 윌리는 그것만으로도 괜찮은건가요?"
        anne"정말 모든걸 없었던걸로 하고……"
        show willy shock
        willy_think"내가 거기서 그런 말을 하지 않았더라면 나중에 더 큰 일로 벌어질지도 몰랐는데……"
        show willy
        willy"난 괜찮아"
        willy"거기다 앞으론 네가 혼자서 괴로워하지 말고, 나랑 같이 얘기 하기로 했으니까 문제없고"
        show willy smile
        willy"네가 지금까지 계속 혼자서 괴로워 했으니까 최종으로 그런 선택을 했을거 아니야?"
        willy"혼자서 괴로워하는 게 얼마나 슬프고, 괴로운지 나도 잘 아니까, 도와줄 수 있어서 기뻐"
        show anne shock
        anne"저저저, 저야말로!"
        anne"제가 또다시……{cps=2} {/cps}정신이 나가서 누군가에게 큰 피해를 주지 않을 수 만 있다면 정말 좋아요"
        show willy
        willy"사소한거라도 좋으니까 뭔가 있거나, 잘 모를때 전화 해"
        show anne shock2
        anne"정말 윌리는……"
        anne"너무 자상하고……"
        show willy shock
        willy"근데 아까 스테반이랑 대화하는거 보니까, 내가 완벽하다고 그러던데……"
        extend" 날 너무 과대평가 하지는 말아줘"
        willy"알고보면 나나 너나 비슷하니까"
        show willy
        show anne shock
        willy"그럼 난 이만 가볼게"
        play sound "se/footsteps_concrete.mp3"
        show willy talk:
            linear 1.0 xalign 2.0
        anne"윌리……"
        anne_think"잘생기고, 착하고, 똑똑한데다 겸손까지……"
        show anne shock2
        anne"하아……"
        stop bgs
        scene black with moveright
        $ renpy.pause(0.5)
        play bgs"bgs/night.mp3"
        play music "bgm/sirius1.mp3"
        scene bg diary_park_night at Zoom((1280,720),(0,0,1280,720),(291,249,393,222),0.5) with moveright
        show willy shock:
            zoom 1.6 xalign 0.5 yalign -0.2
        willy"으윽……"
        "어떻게든 괜찮은 척 했지만, 사실 앤이 날 상자에 가두면서 느낀 \'공포증\'에 의한 휴유증이 아직도 남아있다."
        "그래서 난 집 근처에 있는 공원 벤치에 일단 숨을 돌리기로 했다."
        willy_think"근데 앤이 나의 공포증을 알고 있었다니……"
        willy_think"거기다 내가 처음 세웠던 계획에는 없었던 스테반이 나를 구하러 왔어"
        "아무리 생각해도 이 사건에 대해서 여러가지 위화감이 느껴졌다."
        "특히나 내가 남들에게 말하지 않았던 폐쇄 공포증에 대한 사실을 앤이 알고 있었다는 것이다."
        "나의 공포증에 대해선 멜 누나랑, 나와 동거하는 룸메이트 2명 만 알고 있을 텐데……"
        "하지만 내 기억대로라면 누나는 앤 이랑 만나본적이 없다."
        "그럼 남은 건 룸메이트들 뿐……"
        willy"전화를 해봐야겠네……"
        play sound "se/phone_calling.mp3"
        $ renpy.pause(3.0)
        stop sound
        willy"여보ㅅ……"
        play sound "se/shock.ogg"
        show effect1
        $ extra_name = '룸메이트'
        play music "bgm/beat3.mp3"
        show willy shock
        extra"{size=45}윌리이이이~!{/size}" with lshake
        extra"정말 보고싶었어"
        hide effect1
        $ extra_name = '데이브'
        willy"그건 됐고, \'데이브(Daive)\'너한테 몇가지 물어볼게 있어"
        show willy sirius
        willy"혹시 앤 크라운이라고 알아?"
        extra"아아아, 아니!!"
        willy_think"엄청 수상하게 반응하네"
        willy"그럼 내가 납치 됐을때를 대비해서 세운 계획 B랑 C 중에서 실행된 C에 스테반이 대신 온 건?"
        extra"으, 음……"
        "계획 B는, 내가 장기간동안 소식이 없을때, 스테반이 내가 놔둔 폰과 앤에게 온 문자를 근거로 경찰에 신고를 해주는거다."
        "그리고 C 계획은, 데이브가 내 스마트폰의 GPS를 추적해서 \'그 녀석\'을 보내는 거다."
        extra"너라면 금방 알거라 생각 했다……"
        extra"그, 그게……{cps=2} {/cps}듣고 화내지 않는다고 약속해줘……"
        show willy talk
        willy"그래, 말 해봐"
        extra"사, 사실……"
        extra"앤 크라운이 널 납치했을거라는 걸 대충 알고 있었어"
        show willy shock
        willy"정말?!"
        extra"으, 응"
        extra"얼마 전이었어, 네가 나간 사이에 집에 어떤 여학생이 찾아 왔더라고"
        extra"처음엔 와도 그냥 무시 했는데, 시간이 지나도 계속 오는 게 널 얼마나 좋아하는지 느껴 지더라고……"
        extra"솔직히 네가 몇년 동안 계속 하데스를 찾는다고 엄청나게 고생 했잖아?"
        extra"그래서 쉬는 겸사, 연애같은거라도 해보라는 의미로 널 좋아한다는 여자애를 도와줬지"
        willy"혹시 그때 내 공포증에 대해서 말 했어?"
        extra"으, 응……"
        extra"데이트 할때 좁은 곳은 무족건 피하라는 의미에서 말 해줬는데……"
        extra"근데 그건 왜?"
        show willy shock2
        willy"너 때문에 내가 엄청나게 고생 했거든……"
        extra"설마……?"
        willy"맞아"
        extra"그 여자 완전 싸이코네"
        willy"네가 원인이잖아"
        extra"네가 뭘!"
        extra"난 그냥 널 도와주겠다는 좋은 의도로……"
        willy"알았어 알았어……"
        willy"이걸로 왜 앤이 나의 공포증에 대해서 알고 있는지는 납득 했어"
        willy"그럼 혹시 스테반이 날 구하러 온 이유도 너 때문이야?"
        extra"그것도……{cps=2} {/cps}맞아"
        willy_think"이 자식이 진짜……"
        extra"솔직히 원래 계획했던대로─구조로 \'녀석\'을 보내면 앤 이라는 애를 가차없이 죽여버릴 거 같았거든"
        extra"일단 널 납치하긴 했어도, 널 좋아한다는 순수한 마음에서 그런거였는데…… 죽으면 좀 불쌍하잖아?"
        extra"그런데 어느날 네가 렌스 사건때 의외의 활약을 했다는 스테반이 집 앞에 연락처를 남겼더라고"
        extra"거기다 걔라면 앤을 죽이거나 하진 않을 거 같아서 걔한테 네 위치를 줬지"
        show willy shock
        willy"설마 걔랑 연락했어?!"
        extra"어……"
        willy"괜한 정보는 안 알렸지?!"
        extra"내가 알려준 거라곤, 네 위치 뿐이고……"
        extra"오히려 내가 걔 정보를 받아갔지!"
        show willy talk
        willy"그건 또 무슨 뜻이야?"
        extra"걔 어찌나 멍청하던지~{cps=2} {/cps}모르는 사람한테서 온 메일에 걸려있는 링크를 함부로 클릭 하더라고"
        extra"덕분에 지금 걔 폰은 내 손안에 있는거나 마.찬.가.지☆"
        show willy shock
        willy"너……"
        extra"히익!"
        stop music
        extra"그, 그래도 네가 부재인 동안, 원래 가기로 한 로날드와의 미팅에 내가 대신 가줬어!"
        extra"그 사람의 사망 예상 날짜는 앞으로 3일 정도라는 듯 해!"
        show willy sirius
        willy"그나마 좋은 소식이네"
        "내가 지금 가장 필요했던 정보는 얻어서 다행이다."
        "하지만……{cps=2} {/cps}혹시 이걸로 내가 스테반을 위험한 일에 말려들게 한게 아닌가 조금 걱정이다."
        "렌스때는 처음부터 끝까지 계획이 있었기 때문에 문제는 없었지만, 이번 건 전혀 달랐다."
        "다행히 날 납치한 건 하데스 관련 인물이 아니라, 앤 크라운이었지만……"
        "그래도 언제 또 이런 일이 있을지 모르니까……"
        extra"화……{cps=2} {/cps}안 낼 거지?"
        play music "bgm/beat2.mp3"
        show willy smile
        willy"어"
        willy"오늘은 정신병을 앓고 있는 여성에게 장기간동안 납치 당하고, 친구가 위험에 빠질 뻔 한걸 제외하면 아주 기뻐"
        extra"뭔가 말에 가시가 있는데?"
        willy"그래도 네가 나 대신에 로날드 씨와의 미팅에 나가줘서 정말로 기쁜 걸?"
        extra"그, 그치!{cps=2} {/cps}나 잘 했지?!"
        willy"응"
        willy"이걸로 네가 나한테 얼마나 소중한 존재인지를 알게 됐어"
        extra"후후훗!"
        extend" 칭찬 더 해줘도 된다고"
        willy"이렇게 소중한 사람이 병에 걸리거나, 일찍 죽으면 정말 곤란할 거 같아"
        show willy smile2
        willy"근데 하루종일 게임만 하면 언젠간 네가 그렇게 될지도 모르잖아?"
        willy"그러니까 내가 널 건강하게 만들어 줄게"
        extra"응……?"
        extra"그건 무슨 뜻이야?"
        stop bgs
        stop music
        scene black with Dissolve(1.0)
    centered"스테반의 집"
    play music "bgm/smooth1.mp3"
    scene bg room_stephan_night at Zoom((1280,720),(0,0,1280,720),(819,379,440,248),0.0) with eyeopen
    "나는 지친 몸을 이끌고 침대위에 쓰러지듯이 누웠다."
    stephan"후우~"
    stephan"침대가 이렇게까지 편하게 느껴질 줄이야"
    stephan"근데……{cps=2} {/cps}크라운은 내가 하라는대로 했을까……"
    play sound "se/think.mp3"
    play bgs "bgs/night.mp3"
    scene bg case2_outside_night at Zoom((1280,720),(0,0,1280,720),(307,360,524,294),0.0) with flash
    show stephan talk:
        zoom 1.6 xalign -0.2 yalign -0.1
    show anne:
        zoom 1.6 xalign 0.5 yalign -0.3
    show willy talk:
        zoom 1.6 xalign 1.2 yalign -0.1
    anne"토머……{cps=2} {/cps}오늘 정말 죄송했어요……"
    stephan"난 됐고, 집에 도착하면 바로 보우만한테 연락 줘"
    stephan"널 많이 걱정 했으니까"
    play sound "se/think.mp3"
    stop bgs
    scene bg room_stephan_night at Zoom((1280,720),(0,0,1280,720),(819,379,440,248),0.0) with flash
    stephan_think"이젠 아무런 상관이 없겠지만……"
    play sound "se/phone_text.mp3"
    $ renpy.pause(0.3)
    stephan"……?"
    "충전중인 폰에서 문자음이 울렸다."
    scene bg room_stephan_night at Zoom((1280,720),(819,379,440,248),(78,426,524,294),0.5)
    $ renpy.pause(0.5)
    play sound "se/search_bag.mp3"
    show stephan talk with dissolve:
        zoom 1.9 xalign 0.0 yalign -0.3
        linear 0.6 yalign -0.6
        linear 0.6 yalign -0.3
    $ renpy.pause(1.2)
    "전화번호부에 등록되지 않은─모르는─번호로 왔다."
    show black
    show phone2:
        zoom 3.0 xalign 0.5 yalign 0.5
    nvl clear
    narrator_nvl"\'안녕 스테반, 나 윌리야."
    narrator_nvl"이 번호는 내가 일 할때 쓰는 거라서 너 한텐 등록 돼 있지 않았겠지"
    narrator_nvl"뭔가 제대로 고맙다는 인사를 전달하지 못한거 같아서 미안, 그리고 정말 고마워"
    narrator_nvl"날 구해준 답례 라고 하긴 뭣 하지만, 혹시 SBOX Two랑 PX3는 어때?"
    narrator_nvl"혹시 괜찮다면 윌요일에 학교에서 만나서 줄게\'"
    scene bg room_stephan_night at Zoom((1280,720),(819,379,440,248),(78,426,524,294),0.0)
    show stephan smile:
        zoom 1.9 xalign 0.0 yalign -0.3
    stephan"콘솔을 두개나?!"
    stephan"당근 좋지!"
    play sound "se/phone_send_text.mp3"
    "나는 즉시 윌리한테 답장을 보냈다."
    show stephan talk
    stop music
    "근데……"
    "방금 읽은 문자의 내용을 통해서 윌리에겐 폰이 2대가 있다는 걸 알게 됐다."
    "그렇다는 건─"
    play sound "se/think.mp3"
    show phone_unknown with flash
    $ renpy.pause(0.3)
    play sound "se/think.mp3"
    scene bg fastfood_bathroom with flash
    show phone:
        xalign 0.9 yalign 1.5
    scene bg room_stephan_night at Zoom((1280,720),(819,379,440,248),(78,426,524,294),0.0) with flash
    show stephan talk:
        zoom 1.9 xalign 0.0 yalign -0.3
    play music "bgs/creepy.mp3"
    "윌리의 룸메이트 라는 사람이 알려준 두개의 위치는─내 추리대로─모두 윌리의 폰의 GPS 신호 였다는 뜻이 된다."
    "윌리의 룸메이트……{cps=2} {/cps}대체 정체가 뭐지?"
    "윌리랑은 또 무슨 관계인걸까?"
    "조금 궁금했다."
    "하지만……"
    play sound "se/think.mp3"
    scene bg office_inside at Zoom((1280,720),(0,381,602,339),(0,381,602,339),0.0) with flash
    show lance gun :
        zoom 1.5 yalign -0.2 xalign 0.3
    lance"……이렇게라도 안하면 내가 죽는 걸 어떡하냐고!"
    stephan"그런 문제라면 경찰에 가서……"
    lance"해봤어……"
    lance"근데 전부 소용 없었어……{cps=2} {/cps}녀석의 상사는……"
    lance"법과 경찰을 넘는다고……"
    play sound "se/think.mp3"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(531,286,553,312),0.0) with flash
    show willy shock:
        zoom 1.4 yalign -0.3 xalign 0.8
    show stephan mad:
        zoom 1.4 yalign -0.3 xalign 0.35
    willy"맞아……{cps=2} {/cps}네 말대로 내가 렌스 씨를 구한 목적은 따로 있었어"
    willy"애초에 렌스 씨의 목숨은 별 상관도 없었지"
    willy"……하지만 그게 잔인 하다고?"
    willy"그럼 마르쿠스 고드윈 이라는 사람이랑 그의 상사가 하는 짓은?!"
    willy"그녀석들 이라도 잡지 않으면 렌스같은 사람들이 더 많이 나온다고!"
    scene bg room_stephan_night at Zoom((1280,720),(819,379,440,248),(78,426,524,294),0.0) with flash
    show stephan shock:
        zoom 1.9 xalign 0.0 yalign -0.3
    "……나는 두려웠다."
    "게다가 이번 사건을 통해서─저번에 윌리가 고드윈에 대해서 했던 말이 단순히 정의감에 불타서 한 말이 아니라, 진심으로 수행에 옮기는게 가능하다는 걸 알았다."
    stephan_think"그런데, 잘 생각해보니까 걔가 이런 말도 했었는데……"
    play sound "se/think.mp3"
    scene bg police_meeting at Zoom((1280,720),(319,257,769,433),(531,286,553,312),0.0) with flash
    show willy talk:
        zoom 1.4 yalign -0.3 xalign 0.8
    show stephan sirius:
        zoom 1.4 yalign -0.3 xalign 0.35
    willy"내가 왜 이런 일을 하는지……{cps=2} {/cps}이유는 매우 단순해"
    willy"그저 \'할 수 있으니까\' 하는 것 뿐이야"
    willy"만약 이 손으로 한 사람이 죽을 운명을 바꿀 수 있다면……"
    willy"설령 그것이 나랑 관련 없는 사람 이라고 해도!"
    willy"내가 바꿀 수 있다는 사실을 알면서 모른척 할 순 없어"
    scene bg room_stephan_night at Zoom((1280,720),(819,379,440,248),(78,426,524,294),0.0) with flash
    show stephan shock:
        zoom 1.9 xalign 0.0 yalign -0.3
    stephan_think"설마 그때 말 했던 \'할 수 있으니까\'의 의미가 그런거 였을 줄이야……"
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    "처음엔 몰랐지만, 이렇게 다시 생각해보니까 모든게 너무 현실과 동떨어진듯 한 느낌이었다."
    "크라운이 갑자기 윌리를 납치한 건 그렇다 쳐도, 윌리의 룸메이트는……"
    "하지만 나는─지금 일어난다고 생각하는─보이지도 않고, 알 수도 없는 전쟁이랑 아무런 상관이 없다."
    "조금 흥미롭다면 흥미롭지, 결코 내가 직접적으로 관여여하고 싶은 마음도 없고"
    "왜냐면─나한텐 그것보다 더 중요한 일이 있으니까"
    show grandpa:
        alpha 0.0 xalign 0.5 yalign 1.0
        linear 1.0 alpha 1.0
    "……바로 나의 \'가족\'의 일"
    stop music
    jump chapter3