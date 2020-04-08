##############################################################################################
########################################챕터4: 의식하는 오미너스#########################################
##############################################################################################
label chapter4:
    $ save_name = "4.의식하는 오미너스"
    scene chapter4 with moveright
    $ renpy.pause(2)
    stop music
    scene black with moveright
    if knows_grandpa == True:
        centered"1주일 전"
        play music "bgm/sad3.mp3"
        scene bg test2 with memory # 할아버지의 방 배경
        stephan"혹시 할아버지의 치료를 하고 있는 의사 선생님 이신가요?"
        doc"네"
        stephan"할아버지는 어떻죠?!"
        stephan"상태가 심각한가요……?"
        doc"아뇨"
        doc"그렇게 까지 심한건 아니에요"
        doc"그냥 당뇨병 증상이 조금 보여가지고 치료를 하고 있었습니다"
        stephan"당뇨병이면 심각한거잖아요!!"
        doc"걱정 하실정도는 아닙니다"
        doc"적어도 아직까진……"
        stephan"무슨 뜻이죠?"
        doc"토머 씨가 연세가 있으시다보니 합병증이 생길 위험이 있어서 이렇고 있습니다"
        stephan"…………"
        scene black with memory
    play music "bgm/smooth2.mp3"
    centered"9월 21일 일요일"
    centered"오전 8시 40분"
    scene bg mansion_hall with dissolve
    show stephan yawn
    stephan_think"어제 할아버지의 생일 파티를 하는 바람에 일기장 진도를 제대로 나가지 못했네……"
    stephan_think"할아버지가 건강하신 동안 퍼즐을 풀려면 오늘은 하루종일 일기장을 읽어야겠어"
    hide stephan yawn
    play sound "se/footsteps_wood.mp3"
    "내가 도서실로 발길을 옮기려고 하는데 위에서 누군가 내려오는 소리가 들렸다."
    grandpa"스테반"
    grandpa"일찍 일어났구나"
    "위에서 내려오던 사람이 할아버지 였던 모양이다."
    show stephan shock at left
    stephan"할아버지야말로 평소보다 일찍 일어나셨네요"
    grandpa"지금 일기 장을 읽으러 가는 길이니?"
    show stephan at left
    stephan"네"
    grandpa"열심히 하는 모습이 정말 보기 좋구나"
    if knows_grandpa == True:
        stephan"할아버지가 건강하게 계시는 동안 퍼즐을 풀고 싶거든요."
        grandpa"건강한 동안이라니?"
        grandpa"무슨 뜻이니?"
        show stephan talk at left
        stephan"사실……"
        stephan"저번 주에 할아버지의 주취의 한테서 할아버지의 몸상태가 많이 좋지 않으시다고 들었어요."
        stephan"당뇨 증상이 있으시다고……"
        grandpa"그렇구나……"
        grandpa"저번주 부터 알고 있었다고 했지?"
        stephan"네"
        grandpa"스테반……"
        grandpa"이미 알고 있다고 하니까 내가 너한테만 말하마……"
        play music "bgm/sad1.mp3"
        scene bg test with dissolve # 할아버지의 중풍이 온 왼손 일러스트
        stephan"하,{cps=2} {/cps}할아버지?!"
        grandpa"내 몸이 이젠 내 마음대로 움직이질 않는구나……"
        stephan_think"어제 내가 느꼈던 위화감이 바로 이거였어……"
        "할아버지가 어제 한손으로만 지팡이를 들고 있었던 이유가 바로 이거였었다."
        "할아버지한테 중풍이 왔었던 것이다."
        scene bg mansion_hall with dissolve
        show stephan shock at left
        stephan"이거 언제부터 그랬어요?!"
        grandpa"어제 아침에……"
        grandpa"시아가 날 깨우러 올때 알게 됐단다"
        stephan"빨리 의사를 부르는 게……"
        grandpa"아니"
        grandpa"더이상 남에게 피해를 주고 싶지가 않아……"
        show effect1
        show stephan sad at left
        play sound "se/shock.ogg"
        stephan"{size=40}할아버지가 건강하지 못한게 더 피해라는 걸 모르세요?!{/size}" with lshake
        "너무 울컥한 나머지 나도 모르게 소리를 질러 버렸다."
        "그러지 말았어야 했는데……"
        "뒤늦게 후회하고 있었다."
        hide effect1
        grandpa"의사를 부른다고 해서 뭐가 바뀌진 않아"
        grandpa"메리가 한 말은 언제나 맞는거 같네……"
        grandpa"자기가 갈땐 정말 자기가 아는법 인거 같구나"
        stephan"도대체 왜 그런 말씀을 하시는 거예요?"
        stephan"어제만 해도 정말 즐겁게 계셨잖아요!"
        grandpa"그래서 내가 너한테만 말을 하는거란다……"
        grandpa"혹시 내가 먼저 죽더라도……"
        grandpa"메리의 퍼즐을 찾는 건 절대 포기하지 말아줘"
        grandpa"그게 메리의 마지막 소원이자……{cps=2} {/cps}나의 마지막 소원이거 같구나……"
        show effect1
        play sound "se/shock.ogg"
        stephan"{size=40}왜 벌써부터 돌아가시겠다는 듯이 말씀을 하시는거예요?!{/size}" with lshake
        stephan"{size=40}제가 반드시 할아버지가 돌아가시기 전에 퍼즐을 풀거니까!{/size}"
        stephan"{size=40}걱정 하지 마시고 그냥 편하게 계세요!{/size}"
        hide stephan sad
        hide effect1
        play sound "se/footsteps_running.mp3"
        $ renpy.pause(2)
        "나는 그대로 도서실로 달려갔다."
        "더이상 할아버지의 약한 모습을 보고싶지가 않았었다."
    else:
        stephan"제가 할아버지를 위해서 해줄수 있는 일인걸요."
        stephan"당연히 열심히 해야죠!"
        grandpa"그렇게 해주니까 정말 고맙구나……"
        grandpa"내가 조금만 더 오래 살수 있었어도……"
        show stephan shock at left
        stephan"그런 말씀 마세요!"
        stephan"할아버지는 아직 건강 하시잖아요?"
        grandpa"그래……"
        grandpa"건강 하고말고……"
        grandpa"그래도 나이가 들면 그런게 있잖느냐?"
        grandpa"이곳 저곳이 뻐근해진다든가……"
        show stephan at left
        stephan"할아버지가 에너지 드링크만 끊으신다면 몇년은 더 오래 사실수 있을거예요."
        stephan"또, 할머니가 남기신 퍼즐도 제가 대신 풀고 있으니까 할아버지 께선 그냥 편하게 계세요!"
        grandpa"어―{cps=2} {/cps}정말 든든하구나"
        grandpa"하지만 아무것도 안하면 불안해서……"
        show stephan shock at left
        stephan"그것도 병이에요."
        stephan"정말로 오래 살고 싶으시면 일단 그 병 부터 고치시고 모든걸 저한테 맡기세요."
        grandpa"그래……"
        grandpa"이거, 내가 널 너무 붙잡은거 같구나"
        grandpa"그럼 너무 무리해서 일기장을 읽진 말고……"
        show stephan at left
        stephan"할아버지 한테 듣고 싶진 않네요~"
        grandpa"허허허……"
        "나는 할아버지와 대화를 마치고 바로 윗층으로 올라갔다."
    ################################1963년 11월 1일 일기장 시작############################
    scene black with memory
    play music "bgm/sirius1.mp3"
    nvl clear
    narrator_nvl"1963년 11월 1일 금요일"
    narrator_nvl"에드워드 토머 30세"
    narrator_nvl"날씨 - 눈이 많이 옴"
    nvl clear
    narrator_nvl"우리나라에 \'레고\'라고 하는 장난감이 출시 되었다."
    narrator_nvl"레고는 플라스틱으로 된 벽돌 장난감인데"
    narrator_nvl"그 인기가 엄청나다."
    narrator_nvl"당연하겠지만 그 인기 때문에 노스탤지어 토이즈의 상태가 조금 위험하다."
    narrator_nvl"어쩌면 구조조정을 위해서 일부 직원들을 짤라야 할지도 모른다고……"
    narrator_nvl"하지만 내가 걱정인건 이 회사가 아닌, 바로 메리의 몸상태다."
    narrator_nvl"잦은 야근 때문에 많이 피곤할텐데"
    narrator_nvl"기침도 조금 하는거 같고……"
    narrator_nvl"혹시 몸이 다시 나빠지기 시작한건가?"
    centered"오후 4시"
    scene bg employee_lounge with dissolve
    edward_think"어후……"
    edward_think"커피를 너무 많이 마신거 같네……"
    edward_think"소화라도 할 겸 좀 돌아다녀야겠어……"
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(3)
    scene bg employee_garden with slideawayleft
    "나는 아무생각 없이 화단을 지나가고 있었는데 앉아 있는 메리가 보였다."
    edward"메리?"
    show mary with dissolve
    "화단을 보고 있던 메리는 일어나 나에게 말했다."
    mary"요즘 많이 힘들지?"
    edward"어……{cps=2} {/cps}그래도 나보단 자기가 더 고생이지……"
    edward"최근에 잠도 잘 못자고 있었잖아"
    mary"후후"
    mary"이게 내 일 인걸 어쩌겠어"
    edward"아무리 일이라도 혼자서 모든걸 할 필요는 없잖아"
    mary"그래도 뭔가 새로운걸 떠올리지 않으면 장난감 시장에서 살아남을 수가 없어"
    mary"이럴때 일 수록 더욱 열심히 하는 수 밖에……"
    "그때 난 한가지 의문이 들었다."
    "확실히 새로운 장난감을 개발하는것도 회사를 살리는데 중요할지 몰라도……"
    "회사를 살리는 방법엔 장난감만 있는 건 아니다."
    edward_think"한번 물어봐야겠다."
    edward"나 궁금 한게 있어"
    $ renpy.vibrate(0.4)
    mary"콜록{cps=2} {/cps}콜록"
    mary"으……"
    mary"{size=20}몸이 좀 으슬으슬한게 감기라도 걸린걸까……{/size}"
    mary"궁금한게 뭔데?"
    edward"아냐, 그냥 나중에 다시 말 할게"
    edward"그보다 내일은 주말이기도 하니까 그냥 조퇴해"
    mary"그게 좋을거 같아……"
    "메리는 퇴근을 하려고 걸어가는데 갑자가 나를 보면서 말했다."
    mary"자기는 안와?"
    edward"회사 상태도 그렇고, 역시 난 남는 게 좋지 않을까?"
    mary"그래도 난 자기가 간호 해줬으면 좋겠는데~♡"
    edward"그,{cps=2} {/cps}그래도……!"
    edward"회사가……"
    mary"회사 걱정은 하지마"
    edward"뭔가 좋은 계획 이라도 있어?"
    mary"아니,{cps=2} {/cps}딱히 없어"
    edward"그럼 왜?"
    mary"회사 걱정은 내가 대신 할테니까, 자기는 내 걱정을 해줬으면 하거든~♡"
    edward"하여간……"
    edward"그렇게 말해 놓고서 나중에 나한테 전부 맡기는 건 아니겠지?"
    mary"후후{cps=2} {/cps}그럴리가~"
    edward"하긴,{cps=2} {/cps}나보단 자기가 경영쪽에 훨씬 뛰어나니까"
    mary"그보다 빨리 가자"
    play sound "se/footsteps_concrete.mp3"
    scene black with dissolve
    $ renpy.pause(0.3)
    play music "bgm/smooth3.mp3"
    scene bg test2 with slideleft # 침실 배경
    "역시 감기엔 휴식이 좋다."
    "그래서 나는 메리를 침대에 눕혀 최대한 휴식을 취하도록 했다."
    show mary
    edward"자기가 부재중인 동안 집안일은 내가 할테니까 오늘은 그냥 누워있어"
    mary"정말 괜찮겠어?"
    edward"이 기회에 연습을 하는거지 뭐……"
    edward"그보다 자기는 뭐가 먹고싶은지 생각 해둬!"
    mary"음……"
    mary"\'치킨 수프\'가 먹고 싶네"
    edward"알았어"
    mary"조리법은 알아?"
    edward"요리책을 뒤지다 보면 나오겠지"
    mary"그,{cps=2} {/cps}그래……"
    mary"너무 무리 하진 말고"
    edward"자기랑 결혼 하기 전엔 계속 혼자서 살아왔었으니까 너무 걱정하지마"
    mary"그래,{cps=2} {/cps}한번 믿어 볼게"
    play sound "se/move.mp3"
    scene bg test2 with moveright# 부엌 배경
    edward_think"흠……"
    edward_think"근데 치킨 수프는 어떻게 만드는 거지?"
    "나는 메리가 요리 할때 읽는 요리책을 훑어봤다."
    edward_think"이렇게 만드는거란 말이지?"
    play sound "se/comic_fuss.mp3"
    show bg test2 with vpunch
    $ renpy.pause(1)
    show bg test2 with hpunch
    $ renpy.pause(1)
    show bg test2 with vpunch
    $ renpy.pause(1)
    show bg test2 with hpunch
    $ renpy.pause(0.5)
    scene black with dissolve
    $ renpy.pause(1)
    scene bg test2 with dissolve # 부엌 배경
    play sound "se/scream.mp3"
    show badcurry with lshake
    edward"이런;;"
    "나 같이 요리의 \'요\'자도 모르는 사람이 기초 연습도 없이 바로 실전으로 들어가서 그런지"
    "치킨 수프는 정말 맛이 없어 보였다."
    "아니, 맛이 없어 보인다를 넘어서서 다크 메터를 만들어버렸다……"
    edward_think"역시 이걸 메리 한테 주긴 힘들겠지;;"
    edward_think"이제 어쩌냐"
    edward_think"음……"
    "나는 메리를 실망 시킬순 없었다!"
    "하지만 그렇다고 해서 내가 다시 요리를 할 순 없고……"
    "지금것 때문에 설거지가 이렇게나 더럽게 쌓였는데 이 이상 일을 늘리는 것도 여러므로 피해가 될것 같았다."
    edward_think"그래!"
    edward_think"밖에서 캔 치킨 수프를 사가지고 오는거야!"
    play sound "se/move.mp3"
    scene black with moveleft
    centered"얼마 후"
    scene bg test2 with moveleft # 부엌 배경
    show mary
    mary"어?{cps=2} {/cps}자기가 정말로 치킨 수프를 만들줄이야"
    mary"맛도 괜찮고"
    edward"나도 한다면 하는 사람이야"
    mary"내가 자기를 너무 과소평가 한……"
    "메리는 엄청나게 쌓인 설거지을 보더니 말을 바꿨다."
    mary"……줄 알았는데 그런것도 아닌거 같고……"
    mary"괜찮아!{cps=2} {/cps}괜찮아!"
    mary"그래도 결과적으로 이렇게 맛있는 치킨 수프가 완성됐으니까!"
    mary"다음에도 부탁할게 ♡"
    edward"어……"
    edward_think"집에 캔을 여러개 준비 해둬야겠군;;"
    edward_think"아!{cps=2} {/cps}생각해보니까 지금 메리한테 물어볼수 있는 기회잖아!"
    edward"메리, 나 궁금한게 있어"
    mary"뭔데?"
    edward"밥먹는데 꺼내기는 조금 그런 주제 일수도 있겠지만……"
    edward"노스탤지어 토이즈의 상태 말이야……"
    edward"왜 그렇게 장난감만 고집하는거야?"
    edward"언제까지 계속 장난감만 만들어선 회사가 살아남기 힘들다는 건 누구보다 자기가 더 잘 알고 있잖아"
    mary"회사에서 나한테 물어보고 싶었던게 이거였구나"
    edward"응……"
    mary"자기"
    mary"회사를 경영하는데 중요한건 돈이 아니야"
    mary"가장 중요한건 자신이 무엇을 만들고 싶냐는거지"
    edward"그렇긴 해도……"
    edward"맨날 말도 안되는 꿈만 쫓다간 현실에서 뒤쳐지게 될지도 모르잖아!"
    mary"…………"
    "메리는 내가 한 말에 대해서 조금 놀란 기색을 보였다."
    mary"서,{cps=2} {/cps}설마 자기 입에서 그런 소리가 나올줄이야"
    mary"뭔가 신기하네"
    edward"응?"
    extend" 신기하다니?"
    mary"아무것도 아냐……"
    mary"그보단 내가 왜 장난감에만 고집을 하는 이유 말이야……"
    mary"사실 그 이유는 간단해……"
    mary"자기는 기억이 안 날지도 모르겠지만……"
    extend" 장난감 덕분에 우리 둘의 인연이 생겼거든……"
    mary"난 그 때의 추억을 잊고싶지가 않아"
    mary"생각해보면 장난감이 우리 둘을 잇는 연결고리인거나 마찬가지니까"
    mary"그런데 그것 마저도 사라져 버린다면……"
    edward_think"확실히 나랑 메리는, 내가 장난감 회사에 취직을 하고 싶었기 때문에 만날수 있었다."
    edward"메리, 난 그때 있었던 일이 생생하게 기억나"
    edward"그때 우리 둘이서 면접실에서 처음 만났던 순간도……"
    mary"거봐, 기억 못하고 있잖아……"
    edward"어?{cps=2} {/cps}그게 아니었어?"
    mary"그리고 회사의 자금 상태는 걱정하지마"
    mary"얼마 전에 근처 대학에서 강의 의뢰를 받았거든"
    mary"그거랑 내 사비로 어느정도 해결할 수 있을거 같아"
    edward"정말로 그렇게 까지 해야되는거야?"
    edward"그 정도로 장난감이 자기한텐 소중한거야?"
    mary"내가 아니라 자기한테 더 소중한거겠지……"
    edward"나한테 소중하다고……?"
    mary"아마 내가 무슨 말을 하는지 전혀 이해 못하고 있을거야"
    mary"그래도 괜찮아~"
    mary"나도 잊으려고 노력하고 있으니까……"
    edward"그,{cps=2} {/cps}그래……?"
    "메리는 작은 미소를 보이며 치킨 수프를 한 숟갈 떠먹으려고 했다."
    "하지만……"
    stop music
    $ renpy.vibrate(0.4)
    mary"{size=45}윽!!{/size}" with lshake
    "메리는 숟가락을 그자리에서 떨어뜨리곤 입을 가리며 애써 구토를 참으려고 했다."
    play music "bgm/sirius3.mp3"
    edward"메리, 괜찮아?!"
    mary"욱……{cps=2} {/cps}읍……"
    mary"……괘,{cps=2} {/cps}괜찮은것 같아……"
    edward_think"혹시 캔 안에 있던게 상하기라도 한걸까?"
    edward"그만 먹는 게 좋을거 같은데……"
    mary"욱……{cps=2} {/cps}미안……"
    $ renpy.vibrate(0.4)
    mary"{size=45}욱!!{/size}" with lshake
    hide mary
    play sound "se/footsteps_running.mp3"
    "이번엔 정말로 위험했는지, 메리는 화장실로 달려갔다."
    "나도 많이 걱정이되어 따라갔다."
    scene bg diary_mansion_hall with slideawayleft
    centered"얼마 후"
    show mary with dissolve
    mary"어후―"
    mary"죽는줄 알았네……"
    "나는 힘들어 하는 메리의 등을 토닥이면서 말했다."
    edward"괜찮아?"
    mary"글쎄……"
    edward"혹시 몸 상태가 다시 나빠지거나 한건 아니겠지?!"
    mary"아,{cps=2} {/cps}아닐거야!"
    mary"{size=25}……아마도{/size}"
    edward"병원 가보자!"
    mary"그게 좋을거 같긴 한데……"
    "메리가 조금 망설이는듯한 느낌이 들었다."
    edward_think"혹시 그때 의사 선생님이 별로 맘에 들지 않았던 것일까?"
    edward"걱정마!{cps=2} {/cps}이번엔 좀 다른 병원으로 가보자!"
    mary"으,{cps=2} {/cps}응……"
    mary"신경 써줘서 고마워"
    edward_think"후훗"
    edward_think"뭔가 메리랑 손발이 척척 맞는거 같아서 기분이 좋은걸"
    "근데 한가지 걸리는 게 있었다."
    "과연 메리가 정말로 병이 다시 생겨 난것인가?"
    "지금까지 내가 관찰한 메리의 폐암 증세는 대체로 혈담, 기침, 호흡 곤란, 흉부 압박 정도 였었다."
    "구토는 전혀 없었다."
    edward_think"설마……?"
    edward_think"그래도 혹시 모르니 종합 병원이 있는곳으로 가는 게 좋을것 같아"
    scene black with dissolve
    stop music
    centered"얼마 후"
    scene bg test2 with slideleft # 병원 배경 (처음것과 다른 병원)
    "우리는 새로운 병원에 도착했다."
    "메리가 의사 선생님께 증상을 설명하고 있는동안 난 메리 뒤에 서서 지켜보기만 했다."
    show mary at left
    doc"그래서 몸이 막 어지럽단 말씀이시죠?"
    mary"네"
    doc"혹시 헛구역질 하신적 있으십니까?"
    mary"네?!{cps=2} {/cps}그걸 어떻게?!"
    doc"역시 그랬군요."
    mary"이거, 의사 하지 마시고 점쟁이 하셔도 괜찮을 지도?!"
    doc"아니, 이건 엄연히 의학적인 사실을 바탕으로;;"
    doc"에헴"
    doc"검사 결과도 그렇고, 환자분의 증상을 봐도 그런데……"
    doc"축하드립니다."
    extend" 임신 입니다."
    show effect1
    play sound "se/shock.ogg"
    play music "bgm/happy4.mp3"
    edward"{size=45}네네네?!{/size}" with lshake
    edward"임신?!"
    "설마 했던게 들어 맞았다."
    "예상하곤 있었지만 서도……"
    "역시 직접 들으니까 놀라게 되었다."
    hide effect1
    mary"여,{cps=2} {/cps}여보……"
    mary"흑흑……"
    edward"그,{cps=2} {/cps}그렇게 까지 기쁜거냐;;"
    edward"뭐 나도 기쁘긴 하지만"
    "사실은 기쁜 마음만 있는 건 아니다……"
    "아빠가 된다는것에 조금 걱정이 됐다."
    "내가 과연 아빠로써 잘 할 수 있을지……"
    extend" 아이가 건강하게 자랄수 있을지……"
    edward"그그그그!"
    edward"아이는 남자예요?!{cps=2} {/cps}여자예요?!"
    doc"허허허{cps=2} {/cps}기쁜 마음인건 잘 이해 합니다."
    doc"근데 아직은 성별을 확인 할 수 있을정도로 태아가 자라질 않았어요."
    doc"그러니까 걱정하지 마시고 천천히, 때가 될때까지 기다려 주세요."
    edward"그,{cps=2} {/cps}그럼 예정일은 언제쯤이죠?!"
    doc"음……"
    doc"아내분의 증상으로 미루어 짐작했을땐 어림 잡아서 현재 임신 3주째 일겁니다."
    doc"보통은 9개월 정도 지나서 예정일이 돼니까……"
    doc"내년 8월 초에 예정일이 될겁니다."
    edward"네!{cps=2} {/cps}정말 감사합니다!"
    scene black with dissolve
    "나와 메리는 병원에서 나가 집으로 향했다."
    scene bg diary_mansion_hall with dissolve
    show mary
    mary"자기는 의사 선생님 말을 똑똑히 들었지?"
    edward"어,{cps=2} {/cps}어……"
    mary"그럼 출산 까지 자기가 나 대신에 집안일을 해줘"
    play sound "se/shock2.mp3"
    show effect2
    edward"으엑?!"
    edward"뭐……{cps=2} {/cps}이렇게 될줄 알고 있었지만……"
    hide effect2
    edward"하지만 나도 출근은 해야 하니까 오전 중엔 좀 힘들거 같은데"
    edward"고용인 같은거라도 고용할까?"
    mary"그건 싫은데……"
    edward"왜?"
    edward"집도 이렇게 넓은데 고용인 한두면 정돈 있는 게 좀더 폼나고……"
    mary"그래도 난 자기랑 단 둘이 있는 게 더 좋단 말이야♡"
    play sound "se/heartbeat.mp3"
    edward_think"(두근)"
    mary"자기 방금전에 두근 거렸지?"
    edward"그,{cps=2} {/cps}그럴리가!"
    mary"내 눈은 절대로 못속이니까 포기하는 게 좋을거야"
    edward"그래, 솔직히 조금 두근 거리긴 했다……"
    mary"그럴줄 알았어"
    mary"근데 이거 어쩌지……"
    mary"내가 임신이면 회사에 출근하기 힘들거 같은데……"
    "메리의 표정과 어투로 보았을때 아마 메린 내가 대신 회사를 나가줬으면 하는듯 하다."
    edward"그래 그래……"
    edward"집안일과 함께, 회사도 내가 대신해서 돌보면 되는거지?"
    mary"후훗 잘부탁할게~♡"
    edward"근데 회사의 상태가 이런데 자기 없이 나 혼자서 일을 하라니……"
    mary"이것도 하나의 교육이라고 생각하면서 즐겨~"
    mary"어쩌면 내가 자기한테 회사의 경영권을 완전히 넘겨야 할 날이 올지도 모르니까……"
    edward"갑자기 그렇게 불안한 소리를 하면 어떻게"
    edward"뱃속에 애한테 안 좋겠다."
    mary"그런가……?"
    edward"이렇게 된거 자기는 회사 생각 하지 말고 편하게 쉬고있어"
    edward"내가 열심히 할테니까"
    mary"그럼 이 서류좀 부탁해도 될까?"
    edward"어?!"
    hide mary
    play sound "se/search_bag.mp3"
    "메리는 일어나서 출근 할때 들고 다니는 서류 가방 안에서 엄청난 분량의 서류를 꺼냈다."
    show mary
    mary"다음주 월요일에 면접이 있을꺼거든"
    mary"이건 입사 희망자 명단이야"
    edward"아까 전까지 회사 자금 사정이 뭐시고 했으면서 이렇게 사람을 고용해도 괜찮은거야?"
    mary"이건 예전부터 계획 했던거라서 말이지……"
    mary"회사 상태가 조금 안 좋아졌다고 해서 입사를 희망한 사람들보고 \'죄송합니다. 돌아가 주세요.\'라고 할순 없잖아?"
    edward"뭐……{cps=2} {/cps}그것도 그렇네……"
    mary"면접땐 아빠도 참석하겠다고 하니까 궁금한건 부담갖지 말고 물어보도록해"
    edward"어……"
    "나는 명단을 간단하게 살펴 봤다."
    "근데 사람들이 더럽게 많다……"
    edward"설마 이걸 전부 외워야 되는 건 아니겠지?"
    mary"아니, 이 명단은 입사를 희망한 사람들이야"
    mary"여기서 자기의 역할은 면접을 봐도 좋겠다고 하는 사람을 고르는거고"
    edward"그렇군……"
    edward"근데 어떤 사람을 고르는 게 좋을지……"
    mary"그냥 자기가 생각하는 \'인재 혹은 뛰어난 사람\'을 고르기만 하면 돼"
    mary"참고로, 그중에서 엄청난 거물도 있는거 같더라"
    mary"자기도 내가 누굴 말하는지 보면 금방 알거야"
    edward_think"거물이라……"
    edward_think"이런 회사에 입사를 희망할 정도의 거물 이라고 해봤자 겠지만……"
    edward"인원은 몇명까지 뽑으면 되는거야?"
    mary"딱히 제한은 없어"
    mary"그냥 회사 상태를 잘 고려해서 자기가 알아서 고르면 돼"
    edward"그렇단 말이지……"
    mary"근데 이 상황이 뭔가 신기하지 않아?"
    edward"응?"
    extend" 뭐가?"
    mary"한 4년 전엔 자기가 면접을 보러 왔었는데……{cps=2} {/cps}이젠 자기가 면접관으로 서있잖아♡"
    edward"생각해보니까 그렇네……"
    mary"이제 슬슬 \'프로젝트 코넙적\'도 끝맞쳐도 되지 않을까?"
    edward"새,{cps=2} {/cps}생각해보니까 그거 아직까지 있었구나……!"
    "난 완벽하게 까먹고 있었다……"
    mary"우리 둘이 너무 러브러브 하고 있어서 까먹고 있었어? ♡"
    edward"뭐……{cps=2} {/cps}그렇지……"
    edward"그보다 자긴 아까전부터 평상시 보다 많이 들떠 있네"
    mary"그래?"
    mary"난 잘 모르겠는데♡"
    edward"아니, 말 끝에 ♡가 들어가는 횟수도 명백히 늘어났고;;"
    mary"어쩌면……"
    mary"이 뱃속에 우리 둘의 아이가 있다는 사실이 너무 기뻐서 그런가봐……"
    mary"막 심장이 계속 두근두근거리고……{cps=2} {/cps}둘째, 셋째, 넷째 까지 가능할거 같은 느낌이야"
    edward"나도 자기랑 비슷한 감정이야"
    edward_think"후자는 조금 자신이 없지만;;"
    "나는 메리의 이마에 입을 맞춘 뒤 바로 서류를 읽으려고 방으로 들어갔다."
    scene black with moveleft
    centered"새벽"
    play bgs "bgs/night.mp3"
    play music "bgm/smooth2.mp3"
    scene bg test2 with moveleft # 저택 침실 밤
    "나는 몇 시간 동안이나 면접자 명단을 훑어봤다."
    "서류를 통과 시킨 사람들은 대체로 스펙이 높은 사람을 기준으로 했다."
    "조금 고리타분 하다고 할수도 있겠지만, 그래도 인재를 찾아내는데 가장 확실하고 단순한 방법이기 때문에 나는 바로 선택할수 있었다."
    "게다가 나에게 있어서 \'대단한 사람\'이란……{cps=2} {/cps}역시 학교를 다녀본 사람들이다."
    edward_think"꽤 오랫동안 한거 같은데도 앞으로 12명이나 남았다니……"
    play sound "se/book_page.ogg"
    "내가 다음 입사 희망자의 서류를 살피자 그 경력에 눈이갔다."
    show effect1
    play sound "se/shock.ogg"
    edward_think"이 사람 뭐지?!" with lshake
    edward_think"어째서 이런 사람이 우리 회사에?!"
    hide effect1
    "나는 이사람의 스펙만 봐도 메리가 말한\'거물\'이라는것을 알 수 있었다."
    edward_think"자세한건 면접 당일 날에 확인해 봐야겠네"
    edward_think"아니, 어떤 사람인지 직접 확인해보고 싶어졌어!"
    scene black with dissolve
    play bgs "bgs/birds.mp3"
    stop music
    centered"다음 날 아침"
    mary"후아아암~"
    mary"여보……?"
    show bg test2 with dissolve # 에드워드 침실
    "잠에서 깨어난 메리의 목소리가 나를 깨웠다."
    "나는 어제부터 계속 면접 서류를 통과시킬 사람을 고르느라 피곤해서 책상위에 엎드려서 잠들었는듯 했다."
    show mary
    mary"밤새서 열심히 했나보네?"
    edward"으응……"
    edward"면접을 볼때랑은 정말 다른 부담감이 느껴지더라고……"
    mary"얼마나 잘했는지 봐도 괜찮을까?"
    play sound "se/book_page.ogg"
    edward"자"
    "나는 밤새서 골라낸 면접자들의 서류를 메리에게 건네줬다."
    edward"자기가 말한 대로, 내가\'인재\'라고 생각 되는 사람을 기준으로 골랐어"
    mary"흠……"
    play music "bgm/sirius1.mp3"
    mary"이거 자기가 한게 맞지?"
    edward"무슨 문제라도 있어?!"
    mary"그게 아니라……"
    mary"여기 있는 사람들 대부분 스펙이 높길래……"
    edward"그야 똑똑한 사람을 고용하는 게 좋으니까 그렇지"
    mary"어휴……{cps=2} {/cps}결국엔 자기도 알지 못했구나"
    edward"뭘?"
    mary"혹시 내가 프로젝트 코넙적을 만들었을때 했던말 기억해?"
    edward"4년전에 한번했던 말을 내가 어떻게 기억하냐……"
    mary"그럼 대충 개요는 알아?"
    edward"그게 분명히……{cps=2} {/cps}나같이 학력이 낮은 사람도 성공을 할수있다{cps=2} {/cps}……였었던가?"
    mary"그래,{cps=2} {/cps}그럼 이번엔 자기가 골라낸 사람들의 공통점을 찾아봐"
    edward"저,{cps=2} {/cps}전부 학력이 높은 사람이다……"
    mary"에드워드는 내가 그때 말했던 실수를 반복하고 있었어"
    mary"솔직히 자기는 남들과 조금 다른 기준으로 고를 줄 알았거든"
    mary"이제 와서 내가 면접에 참석 할수있게 해준것도 충분히 경험을 쌓았다고 생각해서 였었는데"
    "생각해보니까 내가 엄청난 실수를 저질러버렸다."
    play sound "se/think.mp3"
    play bgs"bgs/night.mp3"
    scene bg ravine_night with memory
    edward"그놈의 학업, 학업, 학업!"
    edward"벌컥 벌컥"
    show effect1
    play sound "se/shock.ogg"
    edward"지겹다고!!" with lshake
    edward"돈이없는 걸 어쩌라고!!"
    play sound "se/think.mp3"
    play bgs"bgs/birds.mp3"
    scene bg test2 with memory # 침실
    show mary
    "이런말을 했었던 내가……{cps=2} {/cps}회사에 취직을 해서 높은 자리까지 올라왔다고 너무 우쭐하고 있었던걸까……?"
    "결국엔 나 자신도 학력을 고집하게 됐어……"
    edward"메리……{cps=2} {/cps}어떻게 해야 인재를 고를수 있는거야……?"
    mary"그건 따로 정답이 없어……"
    mary"사람마다 인재의 기준이 너무나도 다르니까"
    mary"하지만 말이야"
    extend" 모든 사람들에게 동등한 \'기회\'를 준다면 누구나 인재가 될수있어"
    mary"그런데 대부분은 학력이라는 표면만 보고 섣불리 판단을 해버려"
    edward"그럼 말이야……"
    edward"모든 사람에게 동등한 기회를 주면 누구나 인재가 된다고 생각할때……"
    edward"똑똑한 사람에게 더 많은 기회를 주면 더 큰 인재가 되지 않을까?"
    mary"맞아, 하지만 그 똑똑하다의 기준은?"
    edward"보통은 학력이지"
    mary"내가 미국에서 공부를 하는동안 알게된건데……"
    mary"확실히 해외에선 자기의 말처럼 학력이 높으면 똑똑한 사람일 확률이 높아……"
    mary"왜냐면 거긴 가능한 모두에게 공평한 기회를 주려고 노력을 하고있고, 하고싶은 말, 배우고 싶은 것을 배울수가 있어"
    mary"근데 \'오리엔스\'는 주입식 교육을 채택하고 있잖아?"
    edward"주입식 교육?"
    edward"난 학교를 다니지 않아서 그게 뭔지 잘 모르겠네……"
    mary"아……"
    mary"근데 내가 이런말을 하게 되는 게 정말 아이러니하게 느껴지네……"
    edward"어?"
    mary"비슷한 말을 몇번인가 해본적이 있었던거 같지만……{cps=2} {/cps}이 말은 자기한테서 내가 배운거였었거든……"
    mary"아주 오래전에……"
    edward"내가 자기한테?"
    mary"뭐, 자기는 전혀 기억을 못하고 있겠지만……"
    mary"어쨌건, 주입식 교육이란 학생의 특기, 적성과 관계없이 모두에게 같은 교육을 집어 넣는 교육방식이야"
    mary"교육의 기회가 한정되어있거나, 환경이 열악하거나, 학생에게 특기및 적성이 없을경우엔 효과적일지도 모르겠지만"
    mary"이미 재능을 가지고 있는 학생들에겐 별로 좋진않아"
    edward"왜?"
    mary"주입식 교육은 모든 학생에게 같은 교육만을 시키는거야……{cps=2} {/cps}그러니 학생의 개성을 없애게 되기도 하지"
    mary"선생들에겐 매우 편할진 몰라도……{cps=2} {/cps}한 학생의 인생에 있어선 참 안타까워……"
    edward"그래도 여전히 내가 뭘 어떻게 해야할지 모르겠어……"
    mary"자기의 선택이 잘못된건 아니니까 너무 걱정하진 마!"
    mary"아까 내가 인재를 고르는덴 정답이 없다고 했잖아?"
    mary"어쩌면 자기가 고른게 정답일수도 있는 건데"
    edward"그렇겠지?"
    mary"응"
    "나는 내 자신을 위로하려고 했는데……"
    "문득, 아까 메리가 나에게 한 말이 떠올랐다."
    "\'에드워드는 내가 그때 말했던 실수를 반복하고 있었어\'"
    "\'솔직히 자기는 남들과 조금 다른 기준으로 고를 줄 알았거든\'"
    "돈이 없는 사람들에겐 돈을 벌 기회 조차도 주지않는 세상을 욕했던 내가……"
    "같은일을 했다는 건 용납할수 없었다."
    edward"그래도 오늘은 주말이니까……{cps=2} {/cps}역시 이건 다시 고르는 게 나을거 같아"
    mary"장하다.{cps=2} {/cps}우리 자기♡"
    edward"어,{cps=2} {/cps}어린이 취급은 하지마!"
    scene black with dissolve
    "메리는 정말로 똑똑하다."
    "처음엔 \'역시 하버드생 이기때문에 똑똑하다\'고 생각 했었지만……"
    "메리랑 대화를 하고 나서 이젠 \'역시 메리 이기때문에 똑똑하다\'고 생각하게 된다."
    "지적 수준은 그 사람의 기록으로만 알수 있는것이 아니다."
    "그 사람과 함께 시간을 보내봐야 비로서 확인을 할수가 있는것 인것 같다."
    "메리의 말을 빌리자면……"
    "\'사람은 뭐든지 단순화 하려는 사상 때문에 피해를 초례한다.\'"
    "\'무언가를 생각하는 과정이 복잡할수록 그 결과에 대해서도 더 신경을 쓰게 된다.\'"
    "\'그러니 복잡함을 두려워하지 말라, 복잡함은 인간의 권리이다.\'"
    stop music
    stop bgs
    nvl clear
    narrator_nvl"1963년 11월 5일 화요일"
    narrator_nvl"에드워드 토머 30세"
    narrator_nvl"날씨 - 눈이 많이 옴"
    nvl clear
    narrator_nvl"오늘은 면접이 있는 날이다."
    narrator_nvl"아무리 \'인재\'를 고르려고 해도 힘들었던 나는 아주 큰 결단을 내리게 되었다."
    narrator_nvl"바로, 서류를 낸 모든 사람에게 면접을 볼수 있도록 해준것이다."
    narrator_nvl"메리는 나를 보면서 \'역시 에드워드는 달라\'라고 말을 해줬지만……"
    narrator_nvl"장인 어른을 포함한 다른 면접관들은 내가 한 결정에 대해서 불만이 많았다."
    narrator_nvl"하지만 평상시에도 면접 관리는 메리가 혼자서 다 했었고, 메리는 그 권한을 나에게 넘겼으니 그 사람들에게는 딱히 선택권이 많진 않았다."
    "그런데……{cps=2} {/cps}서류를 낸사람 전원이랑 면접을 봐야하다보니까 집에 일찍 가기엔 글렀다."
    centered"오후 4시 20분"
    play music"bgm/smooth3.mp3"
    scene bg test2 with dissolve # 에드워드 시점으로 면접실 책상에 앉아있는 일러스트 (라기보단 배경)
    edward_think"역시 사람이 너무 많아……"
    $ extra_name = '메리의 아버님'
    extra"{size=50}53번 들어오세요!{/size}"
    play sound "se/footsteps_concrete.mp3"
    "대기번호 53번, 이 사람이 바로 그 \'거물\'이다."
    extra"그럼 간단하게 자기 소개를 해주세요"
    someone"안녕하세요"
    nixon"제 이름은 \'루드윅 닉슨(Ludwik Nixon)\'입니다"
    nixon"서류에서 미리 보셨을지도 모르겠지만……"
    nixon"태어난곳은 미국 유타 주 이고, 하버드 경영대학원에서 박사 취득을 했습니다"
    "그렇다."
    "닉슨 이라는 사람은 메리랑 같은 대학교 출신이다."
    "게다가 스펙을 보면 볼수록 점점 더 천재라는 느낌이 들었다……"
    "하버드 경영대학원 박사 취득, UN에서 근무 까지……"
    "우리 메리도 하버드 졸업생 이긴 하지만 이 정도는 아니다."
    "또, 나이도 나보다 8살은 더 많아서, 혹시라도 이 회사에 들어오게 된다면 어떻게 말을 거는 게 좋을지……"
    nixon"또한 제가 12년 전까지 5년간 UN 사무국에서 국제공무원으로 활동한적이 있었습니다"
    nixon"그 뒤, UN을 떠나서 일본 교토에 있는 작은 장난감 회사에서 상품 아이디어 개발 쪽으로 활동한 적이 있습니다"
    extra"이 회사에 입사한 동기는 있습니까?"
    nixon"동기라……"
    nixon"솔직히 말해서 전 이 회사에 들어온 이유는 없습니다"
    nixon"저는 \'오리엔스\'에 대해서 공부를 하기 위해서 왔거든요"
    nixon"하지만 도시쪽에 물가가 워낙 비싸다 보니까 일을 안하고 살수도 없고"
    nixon"그래서 이전 직종이랑 같은 장난감 회사에서 일을 해보는 게 좋겠다 싶어서 왔습니다"
    extra"장난감 회사는 여기 말고도 많은데 굳이 여기로 온 이유는 따로 있는 건가요?"
    extra"아니면 그냥 집에 가까워서?"
    nixon"아니요!{cps=2} {/cps}절대 그런건 아닙니다!"
    nixon"이 회사에 제가 아는 사람도 다닌다고 하길래 관심이 생겨서 오게 되었습니다"
    extra"알겠습니다"
    "장인 어른이 나를 보면서 말을 했다."
    extra"자네도 뭔가 질문이 하고 싶은 게 있나?"
    edward"어,{cps=2} {/cps}음……!"
    edward_think"뭔가 질문할게……{cps=2} {/cps}뭘 물어보지……"
    edward"그,{cps=2} {/cps}5년간 UN에서 일을 하다가 나중에 떠났다고 하셨는데……"
    edward"뭔가 이유가 있었나요?!"
    edward_think"이런!{cps=2} {/cps}딱히 관련없는 말을!"
    nixon"그게……"
    nixon"그냥 UN측의 의견과 제 의견이 달라서 마찰이 생겼다고만 말해 둘게요……"
    edward_think"의견차?{cps=2} {/cps}혹시 쫓겨난걸까?"
    nixon"질문은 이게 전부인가요?"
    $ extra_name = '면접관 1'
    extra"네,{cps=2} {/cps}잠시만 기다려주세요."
    "우리 면접관 3명은 서로를 바라보며 이 사람을 어떻게 할지 작은 목소리로 의논을 했다."
    extra"닉슨 씨를 통과 시킬까요?"
    extra"글쎄……{cps=2} {/cps}확실히 스펙은 좋지만 태도가 저래서 과연 다른 사람들과 잘 어울릴수 있을지……"
    edward"저,{cps=2} {/cps}전 통과 시켜도 괜찮을거 같다고 생각 합니다……"
    extra"왜 그런가?"
    edward"뭐라고 해야할까……"
    edward"일단 여기 오기 전에도 장난감 회사에서 일을 했다고 했으니까 일을 하는덴 크게 지장이 없을거 같고……"
    edward"또, 닉슨 씨 정도의 인재라면 저희에게 꼭 필요할거 같습니다."
    extra"그렇게 나온다면……"
    extra"그래, 그럼 닉슨은 합격 시키게"
    extra"알겠습니다."
    scene black with dissolve
    "나는 오랜 시간동안 면접을 치뤄서 피곤해진 몸을 이끌고 집으로 향했다."
    centered"오후 7시 20분"
    scene bg diary_mansion_hall with dissolve
    play music "bgm/happy2.mp3"
    show mary with dissolve
    mary"여보!{cps=2} {/cps}오늘 면접은 어땟어?"
    "집에선 메리가 나를 반겨줬다."
    "그런데 뭐랄까……"
    "메리의 한마디가 나의 피료했던 기분을 치유해주는 듯한 느낌이 들었다."
    edward_think"결혼 하길 잘했다~"
    edward_think"여기서 \'식사부터 하실래요?{cps=2} {/cps}아니면 목욕부터?{cps=2} {/cps}그것도 아{cps=2}.{/cps}니{cps=2}.{/cps}면\'같은 말만 해줬더라면!"
    mary"여보?"
    edward"어,{cps=2} {/cps}어—!"
    mary"많이 피곤한가봐?"
    edward"아니야!{cps=2} {/cps}난 괜찮아!"
    edward"오히려 덕분에 기운이 나는 걸!"
    mary"그래?{cps=2} {/cps}그렇다면 다행이고"
    mary"그래서 면접은 어땟어?!"
    edward"뭐……{cps=2} {/cps}엄청 길었지……"
    mary"혹시 \'루드윅 닉슨\'이라는 사람도 왔었어?"
    edward"어"
    mary"어때?{cps=2} {/cps}괜찮은 사람 이라고 생각해?"
    edward"그렇긴 한데……{cps=2} {/cps}혹시 메리가 아는 사람이야?"
    mary"어!{cps=2} {/cps}내가 대학원에 있었을때 정말 많은 신세를 졌거든!"
    mary"과제가 막혔을때 자주 도와줬고"
    mary"정말 좋은 사람이야"
    edward"생각해보니까 둘다 하버드 출신이었지……"
    stop music
    "…………"
    show effect1
    play sound "se/shock.ogg"
    edward_think"{size=45}잠깐?!{/size}" with lshake
    edward_think"그럼 닉슨은 나보다 메리랑 더 오랫동안 알고 있었던 사이?!"
    edward_think"호,{cps=2} {/cps}혹시 전 애인 같은 사이는 아니겠지?!"
    scene black with dissolve
    edward_think"이거……{cps=2} {/cps}그 사람을 면접에서 통과시켜준게 잘한 일 이었을까……"
    "내가 너무 단정짓고 있다는 건 나도 잘 알고 있었다."
    "하지만……{cps=2} {/cps}닉슨 같이 완벽한 사람이 메리랑 오랫동안 알고지냈던 사이라는 건 역시 나에겐 조금 위협이 되었다."
    "그래도 메리의 남편은 나야!{cps=2} {/cps}그러니까 자신감을 가져보는거야!"
    ################################1963년 11월 5일 일기장 끝############################
    scene bg lib_day with memory
    play music "bgm/smooth4.mp3"
    centered"오전 11시"
    show stephan think
    stephan_think"\'루드윅 닉슨\'……"
    stephan_think"어디서 많이 들어본 이름인데……"
    stephan_think"그것도 내가 아주 많이 들어본 사람 이었던것 같은……"
    show stephan shock
    show effect1
    play sound "se/shock.ogg"
    stephan_think"{size=45}그래!{cps=2} {/cps}떠올랐다!{/size}" with lshake
    hide effect1
    "\'루드윅 닉슨\'……{cps=2} {/cps}그 사람은 바로 \'러시 주식회사\'의 현 회장이다!"
    "내가 그 회사에 취직을 목표로 하고 있다보니까 회장의 이름을 자주 들어봤던것이다!"
    show stephan smile
    stephan_think"그나저나 우리나라 최고의 대기업의 회장이 한땐 우리 할아버지의 밑에서 일을 했었다니"
    stephan_think"이거, 내가 간접적으로 대단한 사람이 된것만 같은 느낌이네~"
    hide stephan smile
    play sound "se/book_page.ogg"
    $ renpy.pause(0.7)
    play sound "se/door_open.ogg"
    "내가 일기장의 다음 페이지를 넘기려고 할때 문이 열리면서 세바스찬이 안으로 들어왔다."
    show stephan talk at left
    seb"도련님,{cps=2} {/cps}혹시 여기서 수의학 교재 같은거  못보셨나요?"
    stephan"아니, 그런건 못봤는데?"
    stephan"근데 어쩌면 하루종일 일기장만 읽고 있어서 못봤던걸수도 있으니까 한번 뒤져봐"
    seb"네……"
    play sound "se/search_bag.mp3"
    "세바스찬은 도서실 책장 안에 있는 책들을 하나하나씩 살펴보기 시작했다."
    "나는 어떻게 할까……"
    hide stephan talk
    menu:
        "세바스찬의 교재 찾는 걸 도와준다.":
            show stephan smile at left
            stephan"나도 찾는 걸 도와줄게"
            seb"아니에요.{cps=2} {/cps}도련님은 계속 일기장을 읽으셔도 괜찮아요."
            stephan"사양 안해도 돼~{cps=2} {/cps}찾는데 얼마 걸린다고"
            stephan"그래서 찾겠다는 책은 어떤거야?"
            seb"그게……{cps=2} {/cps}파란색 표지에, 꽤 두꺼워요."
            seb"또, 책의 제목이 \'color atlas of veterinary pathology\'입니다."
            show stephan think at left
            stephan"알았어"
            hide stephan think
            play sound "se/search_bag.mp3"
            "나랑 세바스찬은 같이 책장을 하나하나씩 살펴봤다."
            play sound "se/move.mp3"
            scene black with moveleft
            centered"7분 후……"
            play sound "se/move.mp3"
            scene bg lib_day with moveleft
            show stephan talk at left
            play sound "se/book_page.ogg"
            show ev book2 with dissolve
            stephan"혹시 이거야?"
            "나는 3번째 책장 깊숙히서 세바스찬이 찾고 있는 걸로 추정되는 책을 꺼내들면서 말했다."
            seb"네!{cps=2} {/cps}그거예요!"
            play sound "se/book_page.ogg"
            hide ev book2 with dissolve
            seb"휴~{cps=2} {/cps}찾아서 정말 다행이다~"
            stephan"그거……{cps=2} {/cps}수의학 교재라고 했지?"
            seb"네"
            stephan"세바스찬은 직업이 가정부가 아니었던가?"
            stephan"왜 수의학 교재가?"
            seb"아,{cps=2} {/cps}가정부는 그냥 아르바이트 겸사로 일하는 중이에요."
            seb"실제로 전 수의사를 목표로 공부중인 대학생입니다."
            show stephan at left
            stephan"꿈이 의사란 말이지……{cps=2} {/cps}뭔가 멋있네"
            stephan"근데 의사 하려면 공부를 잘 해야한다던데……{cps=2} {/cps}공부를 잘하는가봐?!"
            seb"잘한다기보단……{cps=2} {/cps}지금으론 진짜 아슬아슬하게 통과될 정도밖에 안돼요……"
            seb"할아버님께선 여기서 마음것 공부를 해도 된다고 말씀 하시지만, 시아가 항상 일거리를 만들어 놓아서 공부를 하려고 해도 불안하다랄까……"
            seb"그래도 시아 덕분에 언제나 긴장을 할수가 있어서 괜찮아요!"
            show stephan smile at left
            stephan"공부가 잘돼서 꼭 의사가 되기를 빌게!"
            seb"감사합니다.{cps=2} {/cps}도련님"
            seb"도련님 께서도 할아버지의 일기장을 통해서 빨리 원하는 정보를 얻으셨으면 좋겠네요."
            stephan"응"
            seb"그럼 전 이만……"
            play sound "se/footsteps_wood.mp3"
            $ renpy.pause(3)
            play sound "se/door_open.ogg"
            "세바스찬은 다시 공부를 하러 돌아갔다."
            stephan_think"나도 계속해서 일기장을 읽어야겠다."
        "계속 일기장을 읽는다.":
            show stephan talk
            stephan_think"나는 일기장이나 계속 읽어야겠다."
            jump diary_1963
    ################################1963년 11월 7일 일기장 시작############################
label diary_1963:
    scene black with dissolve
    play music "bgm/smooth1.mp3"
    nvl clear
    narrator_nvl"1962년 11월 7일 목요일"
    narrator_nvl"에드워드 토머 30세"
    narrator_nvl"날씨 - 눈이 조금 내림"
    nvl clear
    narrator_nvl"오늘은 면접에서 통과된 사람들의 첫 출근일 이다."
    narrator_nvl"다른건 모르겠고 나에겐 \'루드윅 닉슨\' 이라는 사람이 가장 큰 문제다……"
    narrator_nvl"만나면 뭐라고 인사를 해야하는거지?"
    narrator_nvl"말투에 조금 신경을 써야 하는가?"
    narrator_nvl"역시 나보다 나이도 많고, 능력도 많은 사람을 부하 직원으로써 대하는 건 정말 힘든것 같다."
    centered"오전 8시 10분"
    scene bg diary_mansion_hall with dissolve
    edward"나 출근할게"
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}잠깐!{/size}" with lshake
    hide effect1
    play sound "se/footsteps_wood.mp3"
    $ renpy.pause(3)
    show mary with dissolve
    mary"오늘은 나도 같이 출근할게"
    edward"괜찮겠어?!"
    mary"의사말론 아직 임신 3개월 밖에 안됐다고 했잖아"
    mary"잠깐만 움직이는 건 괜찮겠지"
    edward"3개월이면 돌아다니는 게 조금 위험할거 같은데……"
    mary"그렇게 걱정이면 오늘만 나가고 내일부턴 쉬면 되잖아~"
    edward"그,{cps=2} {/cps}그래도……"
    "솔직히 말해서 조금 걱정이 되었다."
    "메리와 아기의 걱정도 있었지만……"
    "그것보다 더 큰 걱정은 과연 내가 좋은 아빠가 될수 있을지……"
    "역시 공부를 해두는 게 좋을것 같은 기분이 조금씩 들었다."
    edward_think"회사 퇴근하고 같이 서점이라도 들려야겠다……"
    play sound "se/move.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    play sound "se/move.mp3"
    scene bg employee_office_day with moveleft
    play bgs "bgs/people.mp3"
    show mary at left
    nixon"메리!{cps=2} {/cps}정말 오랫만이다!"
    nixon"아니지,{cps=2} {/cps}여기선 메리 사장님 이라고 불러야 하나~?"
    mary"이거 이거,{cps=2} {/cps}내가 너한테 사장님 소리를 듣게 될줄이야~"
    mary"왠지 좋은데?"
    edward_think"좋다고?!"
    "나는 이런 상황이 좀 많이 어색했다."
    "신입 주제에 우리 메리를 바로 이름으로 부르다니……"
    "그래 뭐, 확실히 대학때 알고 지냈었던 사이라고 해도 말이지!"
    "그냥 뭐랄까……"
    "일단 나는 메리의 남편인데……"
    edward"그……"
    edward"둘이서 아는 사이라고……{cps=2} {/cps}했었나……요?"
    nixon"네,{cps=2} {/cps}대학원 시절 당시에 친하게 지냈죠"
    nixon"근데 그걸 어떻게 아셨어요?!"
    mary"당근 내가 말해줬지"
    nixon"메리가 말해줬다고……?"
    nixon"두,{cps=2} {/cps}둘이 무슨 관계인지 물어봐도 괜찮을까요?"
    edward"{size=30}저흰……{/size}"
    mary"우린 부부야!"
    nixon"…………"
    nixon"그렇구나……"
    nixon"뭐,{cps=2} {/cps}메리 라면 분명 결혼 할 수 있을거 같았지만"
    nixon"암튼 정말로 축하해"
    nixon"그쪽 성함이 어떻게 되시나요?"
    edward"에드워드 토머 라고 합니다."
    nixon"그럼 이제부턴 토머 부인 이라고 불러야하나?"
    mary"부인 이라는 호칭은 빼줘……"
    mary"벌써 아줌마가 된것같은 기분이야……"
    nixon"하하하"
    nixon"그래서 둘은 결혼 한지 어느정도 됐어?"
    mary"이제 2년 정도 됐으려나~?"
    nixon"한참 좋을때네"
    mary"응,{cps=2} {/cps}매일매일이 어찌나 행복하던지~"
    nixon"아직 까지 결혼 못한 날 놀리는거냐;;"
    mary"어머,{cps=2} {/cps}미혼 인지 몰랐네"
    nixon"내 입사 서류를 봤으면 알고 있었을텐데?"
    mary"후후"
    mary"서류라고 하니까 그러는 건데, 루드윅도 참 대단하더라?"
    mary"대학교 시절때 부터 세계 평화니 뭐니 계속 말했다가 결국엔 UN에 들어갔었잖아?"
    nixon"뭐……{cps=2} {/cps}확실히 그랬지……"
    mary"UN에서 일 안하고 여기 있다는 건 무슨일이 있었다는 거야?"
    nixon"그냥 의견 차이가 있었다고만 해둘게……"
    nixon"에헴,{cps=2} {/cps}그래서 \'사장님\', 제가 해야할 일은 뭔가요?"
    mary"첫날은 회사 구조에 익숙해지는 게 좋을거 같으니까 내가……"
    edward"제,{cps=2} {/cps}제가 이 회사에 대해서 안내 시켜 드릴게요!"
    edward"저를 따라오세요!"
    nixon"아,{cps=2} {/cps}네……!"
    play sound "se/footsteps_concrete.mp3"
    hide mary with dissolve
    "나는 제빨리 닉슨 씨를 데리고 회사 내부를 돌아 다녔다."
    "역시 이 녀석을 메리랑 같이 보내는 건 싫다."
    "어떻게 해서든 메리랑 너무 같이 있지 못하도록 뭐라고 말을 해두는 게 좋을지도 몰라……"
    "질투라고 생각하면 그렇게 생각하라고!"
    "질투건 아니건, 난 메리가 나 말고 다른 남자랑 어울리는 건 정말 느낌이 이상하다."
    play sound "se/move.mp3"
    scene bg employee_lounge with slideawayright
    edward"여긴 직원 휴게실 입니다."
    edward"예전엔 커피를 마시거나, 잡담 하는 걸 제외하곤 할게 그다지 없었지만"
    edward"최근에 매점이 새로 들어서면서 좀더 편리하게 있을수 있도록 됐어요."
    nixon"역시 회사는 다르군요……"
    edward"예전 직장엔 이런게 없었어요?"
    nixon"아주 작은 회사다 보니까……"
    nixon"회사가 아니라 가게라고 해도 될정도 였었죠;;"
    edward"저……"
    edward_think"확실하게 말하는거야……"
    edward"메리랑 아는 사이라고 하셨던데……{cps=2} {/cps}과거에 메리랑 어떤 사이셨는지……"
    edward_think"어……{cps=2} {/cps}내가 지금 무슨말을 하는거지……?!"
    edward_think"이런걸 말하려는 게 아니었는데……"
    edward_think"역시 닉슨 씨에게서 뿜어져 나오는 하버드 출신의 지적인 아우라 때문에 나도 모르게 약자 본능이 나와버린건가……"
    nixon"저랑 메리의 사이요?!"
    nixon"딱히 별 관계도 아니었어요."
    nixon"그냥 제가 대학교 말년때 제 후배로 들어온거 뿐이니까요."
    edward"그,{cps=2} {/cps}그렇군요……"
    edward_think"역시 나보다 더 오래전에 메리랑 알고 지냈었던 사이였어……"
    nixon"딱히 저희 관계를 오해 하시거나 하실 필욘 없으니까 안심하세요~"
    edward_think"(뜨끔)"
    nixon"{size=30}미래라는 건 아무도 예측하지 못하는거네요……{/size}"
    edward"무슨 뜻이죠?"
    nixon"아,{cps=2} {/cps}아니에요."
    nixon"그냥 이쪽 얘기였어요……"
    nixon"그보다 다음은 어딜 소개 시켜 주실건가요?"
    edward"흠……"
    "나는 이 기회를 이용해서 메리의 대학 시절을 좀더 알수 있을것 같은 기분이 들었다."
    "그렇게 돼면 좀더 메리에 대해서 이해를 할수있겠지……"
    "그리고……{cps=2} {/cps}닉슨 씨랑 친해질수 있을지도 모르겠다고 생각되었다."
    "이 회사에서 메리 외에 친한 사람 한두명 있는것도 정말 좋을거 같은데"
    edward"회사 탐방은 나중에 하고, 저기 앉아서 같이 얘기라도 해보는 건 어떤가요?"
    nixon"그래도 괜찮은건가요?"
    edward"걱정 마세요."
    extend" 전 이 회사의 전무니까 어떻게든 되겠죠"
    edward_think"잠깐……{cps=2} {/cps}이 대사……"
    edward_think"나 지금 4년전에 메리가 나에게 해줬던걸 그대로 반복하고 있는거 같네……"
    "나는 닉슨 씨에게 마실걸 한잔 사주고 나서 같이 앉아, 천천히 대화를 하기로 했다."
    play sound "se/move.mp3"
    scene black with moveleft
    $ renpy.pause(0.5)
    scene bg employee_lounge with moveleft
    nixon"제가 다녔던 경영학과에서 메리{cps=2} {/cps}……가 아니라 사장님이 신입생으로 왔을때 처음 만났어요."
    nixon"외국에 처음 와보는거 라면서 많이 당황하고 있을때 제가 이곳저곳을 소개 시켜주는것을 계기로 서로 알게 됐죠"
    edward"그,{cps=2} {/cps}그럼 혹시……"
    edward"사사사,{cps=2} {/cps}사귀거나 하진……"
    nixon"역시 그게 걸리셨군요."
    edward"음……"
    nixon"이렇게 말해도 괜찮을진 모르겠지만……{cps=2} {/cps}아쉽게도 저희 둘은 사귀진 못했어요."
    nixon"사장님이 워낙 철벽 이셔서 말이죠~"
    "왠지 모르게 마음속에서 안도의 한숨이 나왔다."
    nixon"대학교 시절땐 제가 더 공부를 잘했고, 사장님한테 이것저것 알려줬고, 도와도줬는데……"
    nixon"어째서인지 결국엔 제가 사장님 밑에서 일을 하게 됐네요."
    play sound "se/think.mp3"
    scene bg employee_office_day with memory
    show mary
    mary"너한테 사장님 소리를 듣게 될줄이야~"
    mary"왠지 좋은데?"
    play sound "se/think.mp3"
    scene bg employee_lounge with memory
    edward_think"그래서 그런말을 했던거였군……"
    edward_think"한때 자기보다 뛰어났던 사람이 이젠 자기를 높히 불러야 하니까 기뻤던거야……"
    edward_think"메리답네……"
    nixon"저……{cps=2} {/cps}토머 전무님?"
    edward"ㄴ,{cps=2} {/cps}네?"
    nixon"실례되는 말일지도 모르겠지만……"
    extend" 어떻게해서 사장님을 꼬셨어요?!"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}네?!{/size}" with lshake
    hide effect1
    nixon"제가 알고있는 사장님은 진짜 공부밖에 몰랐던 사람이었는데!"
    nixon"저도 사실 당시에 꽤 인기 있었거든요?{cps=2} {/cps}근데 제가 고백을 해도 깔끔하게 거절을 하고……"
    edward"고,{cps=2} {/cps}고백?!"
    "처음 봤을땐 잘 몰랐지만……{cps=2} {/cps}역시 메리의 말대로 사람은 오랫동안 대화를 나눠봐야 그 성격을 확실히 알수 있다."
    "닉슨 씨의 성격은 그다지 좋은 편은 아니었다."
    nixon"그래서 어떻게 고백을 했길래 사장님이 넘어 오신거예요?!"
    edward"따,{cps=2} {/cps}딱히 제가 먼저 고백을 한건 아니에요……"
    nixon"네에?!"
    nixon"그럼 사장님이 먼저 고백을 했어요?!"
    edward"네……"
    nixon"와……"
    nixon"사장님은 똑똑한 사람이 취향이라고 하던데,{cps=2} {/cps}혹시 그쪽도 하버드 출신 이신가요?!"
    edward"아니요……"
    nixon"그럼 옥스퍼드?"
    edward"저,{cps=2} {/cps}전 대학교를 안나왔어요……"
    nixon"대학교를 안나왔다고요……?"
    edward"ㄴ,{cps=2} {/cps}네에……"
    "뭔가 엄청나게 민망했다."
    "또, 짜증났다."
    nixon"이 회사에서 오래전부터 있었군요?!"
    edward"이 회사도 메리 덕분에 있을수 있게 된거예요……"
    nixon"학교도, 회사도 아니면 도대체 어떻게 해서 사장님이랑 알게 된거예요?"
    stop music
    edward"…………"
    scene bg ravine_night with memory
    show mary
    play bgs "bgs/night.mp3"
    show effect1
    play sound "se/shock.ogg"
    mary"면접에서 당신을 무시했던 면접관들의 코를 넙적하게 만들고 싶죠?!" with lshake
    hide effect1
    mary"제가 도와드리겠습니다!"
    scene bg employee_lounge with memory
    play bgs "bgs/people.mp3"
    edward_think"나는 왜 메리랑 친한거지……?"
    edward_think"어쩌다가 메리를 알게된거지?"
    edward_think"무엇보다 그때 당시 메리는 이미 나에 대해서 잘 알고 있었던 기분이 들어……"
    "정말 머리가 아픈 주제였다."
    "예전에도 비슷한 주제를 가지고 생각을 해본적이 있었던것 같았지만……"
    "왜 나랑 메리는 친한걸까……?"
    "나도 모르는 걸 내가 어떻게 대답을 하겠는가"
    "하지만 그렇다고 해서 대답을 안할수도 없는 노릇이다."
    "그래서 나는 최대한 간단하게 줄여서 말했다."
    edward"운……{cps=2} {/cps}이었죠……"
    scene black with dissolve
    play bgs"bgs/night.mp3"
    centered"오후 7시 20분"
    scene bg sidewalk_night with squares
    show snow
    "퇴근 시간이 되어 나랑 메리는 같이 집으로 향했다."
    "그런데 그때 문득 아침에 서점에 들리겠다고 했던게 떠올랐다."
    show mary
    edward"여보,{cps=2} {/cps}집에 가기 전에 잠깐 서점에 들리고 갈래?"
    mary"서점?"
    mary"생각해보니까 나도 서점에서 사고 싶었던게 있었는데!"
    edward"그럼 잘됐네"
    edward_think"혹시 나랑 같은 생각인걸까?"
    edward_think"메리 역시도 엄마가 되기 위해 이것저것 공부하려는 거겠지?"
    scene bg book_store with slidedown # 서점 배경
    stop bgs
    play music "bgm/beat5.mp3"
    "이곳은 서점이다."
    "나는 공부랑은 거리가 있는 사람이다 보니까 서점에 자주 들릴일이 없었지만……"
    "메리는 이곳에 자주 온다는듯 하다."
    show mary
    mary"나는 소설 코너에 있을테니까 필요하면 불러"
    edward"응……"
    play sound "se/footsteps_concrete.mp3"
    hide mary with dissolve
    "나는 육아 코너에서 필요한 책을 찾고 있었다."
    show effect2
    play sound "se/shock2.mp3"
    edward_think"그런데 도대체 무슨 책이 좋은걸까……"
    edward_think"일단 내가 원하는 건 임신을 했을때와 출산을 했을때의 증상과 대처 방법이 적혀 있는 책인데……"
    edward_think"또, 육아에 관한것도 좋을거 같고……"
    hide effect2
    "그때 내 눈에 띄는 제목의 책이 있었다."
    play sound "se/book_page.ogg"
    show ev book3 with dissolve
    edward_think"\'임신, 출산, 육아 대백과\'란 말이지……?"
    edward_think"내가 원하는 걸 다 모아놓은것 같은 제목이군"
    hide ev book3 with dissolve
    play sound "se/book_page.ogg"
    "\'임신, 출산, 육아 대백과\'를 손에 쥐고 이번엔 메리가 있는 쪽으로 걸어갔다."
    play music "bgm/beat4.mp3"
    scene bg test with slideleft # 메리가 많은 책을 들고있는 일러스트
    mary"어?{cps=2} {/cps}자기 책 다골랐어?"
    show effect1
    play sound "se/shock.ogg"
    edward"그 많은 책은 또 뭐야?!" with lshake
    hide effect1
    mary"뭐긴 뭐야"
    mary"내가 사고 싶었던 소설 책이지"
    edward"그렇게나 많이?!"
    mary"전집이니까 어쩔 수 없잖아?"
    "도대체 무슨 소설 이길래 이렇게나 시리즈가 많은지 궁금해서 한번 제목을 살펴 봤다."
    "제목은 \'셜록 홈즈\' 였다."
    edward"처음 보는 소설이군……"
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}셜록 홈즈를 모른다고?!{/size}" with lshake
    hide effect1
    edward"깜짝이야"
    mary"어떻게 셜록 홈즈를 모를수가 있는거지?!"
    edward"난 책을 별로 안읽으니까 모를수도 있는거지……"
    mary"아무리 그래도!"
    mary"셜록 홈즈가 얼마나 유명한데?{cps=2} {/cps}살면서 한번이라도 들어봤을거 아니야?"
    edward"들어본것 같기도 하지만……{cps=2} {/cps}딱히 흥미가 없으니까……"
    mary"자기는 뭐든지 흥미가 없잖아"
    edward"으……"
    edward"그,{cps=2} {/cps}그래서 셜록 홈즈는 어떤 내용인데?"
    mary"요약하자면……{cps=2} {/cps}엄청나게 똑똑한 탐정이 범죄와 싸우는 내용이야!"
    edward"탐정?"
    edward"생각해보니까 자기는 예전에 \'탐정의 서\'라는 책도 쓰고 있었지……"
    edward"탐정을 어지간히도 좋아하는가 보네……"
    mary"범죄와 싸우는 게 얼마나 멋있는데?!"
    edward"그,{cps=2} {/cps}그래도 그런 책은 어린애가 읽기엔 좀 그렇지 않나?"
    mary"어?{cps=2} {/cps}무슨 소리야?"
    mary"이 책은 내가 읽으려고 사는 건데?"
    edward"그런거였어?!"
    edward"엄마가 될 사람이 언젠간 태어날 아이보단 자기를 먼저 생각하다니!"
    scene bg book_store with dissolve
    show mary
    mary"뭐……{cps=2} {/cps}임신중에 책을 읽는 건 태교에도 좋다고 하니까 간접적으로 아이를 위해서 사는거라고 할수도 있겠네……"
    mary"그보다 자기가 들고있는 그책이야말로 애가 읽기엔 너무 이른거 아닐까?"
    edward"음?"
    edward_think"\'임신, 출산, 육아 대백과\'를 말하는 건가?"
    edward"이건 내가 읽을거야!"
    mary"거봐, 자기도 결국엔 자기가 원하는 걸 짚었네"
    edward"하지만 소설과는 다르게 이건 아이에게 직접적으로 도움이 되는거라고!"
    mary"이 소설도 태교로써 도움이 된다 뭐!"
    edward"그렇게 많은 책을 다 읽을수 있기나 하겠어?"
    mary"어이, 내 평생의 독서량이 아마 자기보단 100배는 많을걸?"
    mary"{size=40}그리고 이 책은 단순히 태교나 나를 위한게 아니라 \'탐정의 서\'를 완성하는데도 필요한거야!{/size}"
    "갑자기 메리의 언성이 높아진걸 느낄수가 있었다."
    edward"자,{cps=2} {/cps}자기……"
    edward"주변에 사람들도 있으니까 여기까지만 하자……"
    mary"자기가 먼저 시작했잖아!"
    edward"그래……{cps=2} {/cps}내가 미안……"
    edward_think"그냥 다 사면 될걸……{cps=2} {/cps}이게 왜 싸움이 될뻔한 상황으로 까지 번진걸까……"
    mary"뭐……{cps=2} {/cps}확실히 나도 너무 내가 읽을 소설만 산거 같기도 하네……"
    mary"이왕 온거, 우리 아기도 읽을수 있을만한 동화 같은거라도 사는 게 좋겠어……"
    edward"그래"
    play sound "se/search_bag.mp3"
    "메리는 동화 코너에서 \'아기 돼지 삼형제\'를 꺼냈다."
    hide mary with dissolve
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(3)
    $ extra_name = '점원'
    extra"총 합해서 35 달러 75센트 입니다."
    show effect1
    play sound "se/shock.ogg"
    edward_think"{size=45}힉!{cps=2} {/cps}비싸다!{/size}" with lshake
    edward_think"역시 책만 20권 넘게 사니까 이런 가격이 나올수 있는 건가?!"
    hide effect1
    show mary
    mary"그럼 난 먼저 나가있을게~"
    edward"어……"
    show effect2
    play sound "se/shock2.mp3"
    edward_think"생각해보니까 이 많은 책도 나 혼자서 들고가야 하는구나……"
    scene black with dissolve
    play music "bgm/beat2.mp3"
    nvl clear
    narrator_nvl"1963년 11월 13일 수요일"
    narrator_nvl"에드워드 토머 30세"
    narrator_nvl"날씨 - 눈이 조금 내림"
    nvl clear
    narrator_nvl"나는 며칠간 육아에 대해서 공부를 했다."
    narrator_nvl"정말 대학교에서 육아 전공이 있다면 벌써 박사 학위까지 땄을정도로 공부를 많이했다."
    narrator_nvl"메리 역시도 공부를 하는듯 하지만……"
    narrator_nvl"맨날 셜록홈즈만 읽으니 원……"
    narrator_nvl"그래도 그 \'탐정의 서\'인가 뭐신가 하는 책도 다시한번 쓴다는듯 하다."
    narrator_nvl"솔직히 무슨책을 쓰는지, 왜 그 책을 쓰는지 나는 관심없다."
    narrator_nvl"그냥 무언가에 푹 빠진 메리의 모습이 나에겐 너무나도 귀엽고, 아름답게 보여서 좋다."
    scene bg employee_office_day with dissolve
    play bgs"bgs/people.mp3"
    centered"점심시간 몇분 전"
    edward_think"임신을 하면 가슴이 커진단 말이지?"
    edward_think"하긴……{cps=2} {/cps}모유 수유를 위해서 그럴수 있어……"
    edward_think"가슴이 큰 메리라……"
    edward_think"내,{cps=2} {/cps}내가 무슨 생각을!"
    "나는 오늘도 6일 전에 산 \'임신, 출산, 육아 대백과\'를 읽으면서 공부를 하고 있었다."
    "하지만 책에 적혀있는 내용과 지금의 메리를 비교하면서 읽다보니까 자주 삼천포로 빠져들기도 했다……"
    nixon"전무님!"
    play sound "se/book_page.ogg"
    edward"어,{cps=2} {/cps}{size=45}어?!{/size}"
    "나는 깜짝 놀라서 무의식적으로 읽고 있었던 \'임신, 출산, 육아 대백과\'을 덮어버렸다."
    "뭐, 딱히 숨길것도 아니었는데……{cps=2} {/cps}왜 나는 갑자기 덮어버렸을까……"
    nixon"왜 그렇게 놀라시고 그러세요?"
    edward"아,{cps=2} {/cps}아무것도 아닙니다!"
    edward"그보다 닉슨 씨는 무슨 용무로 오신건가요?"
    nixon"보니까 전무님은 항상 혼자서만 점심을 드시던데……"
    nixon"혹시 같이 점심이라도 드실래요?"
    edward_think"벌써 시간이 이렇게나 됐군……"
    edward_think"오늘도 메리는 출근을 안했으니까 혼자서 먹을뻔했는데……"
    edward"그럼 같이 먹도록 하죠"
    play sound "se/move.mp3"
    play music "bgm/smooth1.mp3"
    scene bg employee_lounge with moveleft
    nixon"냠냠냠……"
    "나는 닉슨 씨랑 같이 직원 휴게실에 앉아서 센드위치를 먹고 있었다."
    edward"우물우물……"
    "들리는거라곤 다른 직원들의 대화소리랑 우리 둘의 센드위치를 씹는 소리 뿐이었다……"
    "근데 같이 점심 먹자고 부른건 닉슨 씨면서 왜 내가 이렇게 까지 어색해 해야하는거지……"
    nixon"토머 전무님?"
    edward_think"드디어 말을 걸어줬다!"
    edward"네?"
    nixon"최근에 어떤 책을 몰래 읽고 계시던데"
    nixon"무슨 책이길래 그렇게 몰래 보셨어요?"
    nixon"혹시 좋은 거라면 저도 좀……"
    show effect1
    play sound "se/shock.ogg"
    edward"{size=45}그런게 아니야!{/size}" with lshake
    hide effect1
    nixon"하하하"
    extend" 당황하는 게 더 수상한데요?"
    edward"끙……"
    edward"그런게 아니라,{cps=2} {/cps}이 책은 말이죠……"
    edward_think"이걸 보여줘야 하나……"
    edward_think"역시 계속 숨겼다간 지금같이 괜한 오해를 살수도 있으니까 빨리 보여주는 게 좋을지도 몰라"
    play sound "se/book_page.ogg"
    show ev book3 at right with dissolve
    "나는 품에 계속 지니고 있었던 \'임신, 출산, 육아 대백과\'를 꺼내들었다."
    edward"이,{cps=2} {/cps}이거예요……"
    nixon"이 책은……"
    nixon"서,{cps=2} {/cps}설마?!"
    nixon"설마 사장님께서 임신을?!"
    edward"네……"
    edward_think"잠깐?{cps=2} {/cps}왜 내가 미안하다는 듯이 있는거지?"
    edward_think"메리는 내 아내이고, 결혼한지 2년이 넘게 지났으니까 이상할게 없잖아?"
    edward_think"그리고 닉슨 씨랑 메리는 과거에 아무런 사이가 아니라고 했어!"
    edward_think"자랑스러워 한다면 자랑스러워 하는거지, 내가 주늑들어할 이유는 절대 없다고!"
    play sound "se/book_page.ogg"
    hide ev book3
    nixon"그래서 회사에 자주 안오시는 거였군요……"
    nixon"예정일은 언제쯤 인가요?"
    edward"아직 3개월 밖에 안돼서……"
    nixon"그렇군요."
    nixon"아무튼, 전무님 정말로 축하드립니다!"
    nixon"예쁘고 능력있는 사모님에 곧있으면 자녀까지……"
    nixon"정말 모든걸 가지셨네요~"
    edward"그,{cps=2} {/cps}그런가요?{cps=2} {/cps}에헤헤……"
    nixon"부러워요……"
    edward"하지만 닉슨 씨는 좋은 대학교도 졸업 하셨고……{cps=2} {/cps}친구도 저보다 많으시잖아요……?"
    nixon"그게 무슨 소용이겠어요……"
    edward_think"부정은 안하겠다는 건가……"
    nixon"전 결국엔 결혼도 못했고, 어렸을때 부터 계속 꿈꿔왔던 직업도 스스로 차버리고……"
    nixon"솔직히 말해서 지금 제가 뭘 해야하는지 모르겠어요."
    "그때 나는 꽤나 신기한 기분이 들었다."
    "루드윅 닉슨은 엄친아 라고 불릴정도의 초 앨리트 였다."
    "그런데 그 앨리트가 사회적으로 방황을 하고있다니……"
    "역시 메리가 말한데로 학력은 곧 인재를 뜻하는것이 아닌듯 하다."
    "정말 메리의 말은 언제나 들어맞는다니까……"
    edward"정말 힘드시겠네요……"
    nixon"전무님……{cps=2} {/cps}오늘 끝나고 같이 술 한잔 어떠세요?"
    edward"술이요?"
    nixon"네"
    extend", 생각해보니까 제가 오리엔스에 이사오고 나선 한번도 술을 못해봤거든요~"
    edward"뭐……{cps=2} {/cps}저도 술은 안한지 오래되긴 했으니까……"
    nixon"제가 일본에 있었을땐 다같이 회식 같은것도 하고 그랬는데, 여기선 그런게 없으니까 조금 놀랐어요."
    edward"우리나라에도 회식같은건 있어요."
    edward"그냥 이 회사 사람들이 회식을 그렇게 즐겨 하지 않는거 뿐이에요."
    nixon"하긴……{cps=2} {/cps}회식 자리에서 상사 비위 맞춰주는 게 어지간히 부담스러워야 말이죠……"
    edward_think"그런 말을 하면서 나랑 같이 회식을 하자는 건가……!"
    scene black with dissolve
    "이런 저런말을 해도 결국에 우리 둘은 퇴근하고 같이 술을 하기로 했다."
    "닉슨 씨는 나의 첫 회사 친구이기도 하니까……"
    stop music
    stop bgs
    centered"새벽 2시"
    "너무 오랫동안 놀았는지 시간이 벌써 이렇게 되었다."
    "주량이 많진 않아서 취하진 않았지만……{cps=2} {/cps}그래도 머리가 조금 지끈지끈 거리긴 한다……"
    "그나저나 사전에 메리한테 연락을 주지 못했는데……"
    "화났으려나?{cps=2} {/cps}아니면 자고있을까?"
    play bgs "bgs/night.mp3"
    scene bg diary_mansion_hall with dissolve # 밤
    "나는 소리가 들리지 않게 살짝 문을 열고 나서 들어갔다."
    edward"여……{cps=2} {/cps}보……?"
    "불이 꺼진걸로 짐작했을때, 다행히도 자고있는듯 하다."
    edward_think"깨지 않도록 조심히 들어가야겠지……"
    play sound "se/footsteps_wood.mp3"
    scene black with dissolve
    $ renpy.pause(2)
    "술때문에 지끈거리는 머리로 소리나지 않게 걷는다는 건 역시 힘들었다……"
    "그래도 열심히 침실을 향해 발걸음을 옮겼다."
    play sound "se/footsteps_wood.mp3"
    scene ev lib_night_door with Dissolve(3.0)
    edward_think"어?"
    "그런데 다른곳은 전부 불이 꺼져있으면서 어째서인지 도서실에만 불이 켜져있다."
    "혹시 메린가?"
    play sound "se/door_open.ogg"
    play music "bgm/smooth2.mp3"
    scene bg lib_night with flash
    "안엔 메리가 책을 읽고 있었다."
    "책에 얼마나 집중을 하고 있었던건지 내가 들어온것도 눈치체지 못했다."
    edward_think"이렇게 늦게까지 책을 읽고 있다니……"
    play sound "se/search_bag.mp3"
    show mary with dissolve
    mary"여보 왔……"
    mary"이 냄새는 뭐야……"
    edward"어?!"
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}설마 술마셨어?!{/size}" with lshake
    hide effect1
    edward"이,{cps=2} {/cps}이건 말이지……"
    "난 술을 그렇게 까지 많이 마시진 않았다."
    "많이 마셨다면 그건 루드윅 닉슨이지……"
    "녀석 때문에 2차에서 4차까지 가게 되었으니……"
    "하지만 난 닉슨 때문에 이렇게 늦었다면서 남탓을 하고싶진 않다."
    "그래서 딱잘라, 닉슨 이라는 이름은 언급하지 않기로 했다."
    edward"치,{cps=2} {/cps}친구랑 같이 너무 마셔버려서……"
    edward"미안……{cps=2} {/cps}사전에 연락을 했어야 했는데 말이야……"
    mary"친구?"
    show effect1
    play sound "se/shock.ogg"
    mary"{size=45}자기한테 친구가 생겼어?!{/size}" with lshake
    hide effect1
    edward"그건 또 무슨 뜻이야?!"
    mary"자기한테 나 말고 다른 친구가 생겼다니……"
    edward"다른 여자는 아니니까 걱정 하지 않아도 괜찮아"
    mary"남자든 여자든……"
    mary"자기한테 나 말고 다른 친구가 생겼다니……"
    edward"계속 들어보니까 기분이 좀 나쁜데……?"
    mary"기분 나빴다면 미안……"
    mary"그냥 좀 놀라서……"
    edward"어……"
    edward_think"놀랐다는 게 기분이 더 나쁘다만……?"
    mary"그래서 그 친구 이름은 뭐야?!"
    edward"혹시 의심 하는거야?"
    mary"어"
    mary"어쩌면 자기가 혼자서 술마셨는데 외로워 보이지 않으려고 거짓말 하는 걸수도 있으니까"
    edward"내가 그런 이미지였어?!"
    edward"그리고 내가 그런 거짓말을 할 이유가 없잖아"
    mary"하지만……{cps=2} {/cps}자기한테 친구가 생겼다는 건 뭔가 믿기지가 않아서……"
    edward"듣자듣자 하니까……"
    edward"그래,{cps=2} {/cps}그 친구 이름은 루드윅 닉슨이야"
    edward"자기도 잘 알고있는 그 닉슨"
    edward"이제 됐지?"
    mary"루드윅이랑 친하다고?!"
    mary"더 믿기 힘든데?!"
    edward"…………"
    "내가 메리 눈엔 친구 하나없는 한심한 이미지로 보였었던걸까?"
    "어째서 나한테 친구가 생겼다는 걸 믿지 못하는 걸까?"
    "뭐……{cps=2} {/cps}솔직히 메리 앞에 있을땐 대체로 한심한 모습만 보이긴 했지만……"
    "그래도 언제나 혼자였던 남편에게 친구가 생겼다고 하면 보통은 좋아하지 않나?"
    edward"믿기 싫으면 믿지 말든지……"
    edward"난 자러 갈테니까 자기도 빨리 자"
    mary"지금 시간이 몇시길래……"
    show effect2
    play sound "se/shock2.mp3"
    mary"헉……{cps=2} {/cps}벌써 새벽 2시네"
    mary"왜 이렇게 시간이 빨리가는 걸까……"
    hide effect2
    edward_think"책에 얼마나 집중을 하면 시간 감각을 그렇게 까지나 상실할 수 있는거지;;"
    scene black with dissolve
    stop bgs
    play music "bgm/beat2.mp3"
    nvl clear
    narrator_nvl"1963년 11월 14일 목요일"
    narrator_nvl"에드워드 토머 30세"
    narrator_nvl"날씨 - 눈이 조금 내림"
    nvl clear
    narrator_nvl"내가 메리한테 그런 이미지 였었다니……"
    narrator_nvl"어제 메리의 반응을 봐도 그렇고……"
    narrator_nvl"메리의 눈엔 내가 그저 불쌍한 왕따로 보였었던걸까……?"
    narrator_nvl"그럼 나랑 같이 있어준것도 전부 내가 불쌍해서?!"
    narrator_nvl"하지만 동정심에 이렇게 까지 해줄리는 없었다."
    narrator_nvl"어제 메리는 그냥 순전히 놀랐기 때문에 그러한 반응을 보였을거라 믿고 있다."
    play bgs "bgs/people.mp3"
    centered"오전 10시"
    scene bg employee_office_day with dissolve
    play sound "se/footsteps_concrete.mp3"
    $ renpy.pause(3)
    nixon"안녕하세요오―"
    edward"닉슨 씨,{cps=2} {/cps}2시간 지각입니다."
    nixon"죄송해요."
    nixon"어제 너무 마셔버렸는지, 아직도 머리가 아퍼서요……"
    edward"뭐……{cps=2} {/cps}저도 어제 늦게 자서 피곤한 건 마찬가지 이니까 뭐라 할 처지는 아니지만요……"
    "내가 어색한 미소를 보이고 다시 일에 몰두를 하려고 할때, 누군가 나에게 말을 걸었다."
    $ extra_name ='직원'
    extra"토머 전무님"
    stop music
    extend", 회장님께서 회의실로  호출 하십니다."
    edward"회장님께서?"
    edward_think"도대체 무슨일이지?"
    play sound "se/footsteps_concrete.mp3"
    "나는 하려고 했던 일을 즉시 중단하고 회장실로 회의실로 향했다."
    scene black with dissolve
    stop bgs
    $ renpy.pause(0.5)
    scene bg employee_meeting_room with movedown
    edward"좋은 아침입니다.{cps=2} {/cps}회장님"
    $ extra_name = "장인 어른"
    extra"자네 왔는가……?"
    extra"아직 참석하지 못한 사람들이 몇몇 있으니 잠시만 기다려 주게"
    edward_think"다른 사람들도 호출 받은건가?"
    play sound "se/move.mp3"
    scene black with moveleft
    centered"얼마 후……"
    play sound "se/move.mp3"
    scene bg employee_meeting_room with moveleft
    "회의실엔 내가 잘 알지 못하는 사람들로 가득했다."
    "전혀 모르는 사람들은 아니고, 그냥 나랑 별로 친하지 않은……"
    "이름도 잘 모르는 그런 사람들로 가득했다."
    "하지만 나이를 통해서 대부분 높은 직급이거나, 오랫동안 회사에 있었던 간부급 사원들 인것은 알 수 있었다."
    "이런 날이 올 줄 알았으면 좀더 높은 사람들이랑 자주 돌아다니고 하는거 였는데……"
    "괜히 뻘쭘해지네……"
    extra"전부 출석 했는가요?"
    $ extra_name = '모두'
    extra"네"
    $ extra_name = '장인 어른'
    extra"제가 여러분들을 이 자리에 모은 이유는 다름이 아니라……"
    play music "bgm/sirius1.mp3"
    extra"곧 은퇴를 할까 합니다……"
    play bgs"bgs/people.mp3"
    edward"은퇴?!"
    "회장님의 갑작스런 은퇴 선언에 주변에선 소근거리기 시작했다."
    stop bgs
    play sound "se/search_bag.mp3"
    "그때 회사의 고위 간부 중 한명이 일어나서 회장님의 말에 의문을 제기했다."
    $ extra_name = '회사 간부'
    extra"회장님은 아직 60대 밖에 되지 않으셨잖아요?!"
    extra"은퇴를 하기엔 아직 이른거 같다고 생각합니다."
    $ extra_name = '높은 직원'
    extra"맞습니다!"
    $ extra_name = '장인 어른'
    extra"잠깐 내 말을 끝까지 들어보게"
    extra"에헴,{cps=2} {/cps}다들 몇주 전에 있었던 노스탤지어 토이즈의 주가 폭락 사건을 알고 있을겁니다."
    extra"그 타격 때문에 일부 직원들은 직장을 잃기도 했죠……"
    extra"그런 일이 있었으면서 저는 제대로된 대처도 하지 못했고……"
    $ extra_name = '높은 직원'
    extra"하지만 그건 외국 회사의 제품이 국내에 상륙을 하는바람에 발생한 일이지!"
    extra"결코 회장님의 잘못이 아닙니다!"
    $ extra_name = '장인 어른'
    extra"그럴지도 모르네……"
    extra"하지만……{cps=2} {/cps}최근에 메리가 나에게 새로운 사업 전략서를 작성해서 내줬다네"
    edward_think"메리가?"
    extra"내용은 대충, 신 제품의 디자인 컨셉과 마케팅 방법에 대해서 간단하게 적혀 있었어"
    $ extra_name = '높은 직원'
    extra"그럼 문제는 해결된게……?"
    $ extra_name = '장인 어른'
    extra"맞아,{cps=2} {/cps}이걸로 숨은 돌릴수 있게 되었지……"
    extra"하지만 한번 생각해보게"
    extra"계속 회사를 쉬고 있었던 메리가 홀몸 임에도 불구하고 주가 폭락 사건에 대해서 좋은 해결책을 마련 해줬다네"
    extra"그에 비해서 난 아무것도 하지 못하고 속수무책으로 기다리고만 있었어……"
    show effect1
    play sound "se/shock.ogg"
    stop music
    extra"그런 내가 계속 이 자리에 있는 게 괜찮을거라고 생각 하는가?!" with lshake
    $ extra_name = '모두'
    hide effect1
    extra"…………"
    "회장님의 말 한마디에 다들 조용해지기 시작했다."
    "다들 회장님과 오랜 세월을 보내온 사람들……"
    "갑자기 그들의 표정은 전부 이런 날이 올거라는 걸 예상하고 있었다는 듯이 변했다."
    "지금 이 상황을 제대로 이해하지 못하는 건 나 뿐인건가……?"
    $ extra_name = '회사 간부'
    extra"……회장님께서 말씀을 그렇게 하시니까 은퇴가 아니라 해임을 하는거 같네요"
    $ extra_name = '장인 어른'
    play music "bgm/smooth1.mp3"
    extra"그런가……{cps=2} {/cps}허허……"
    "간부의 말 한마디로 분위기가 어느정도 가벼워진듯 했다."
    extra"그리고 다들 내가 갑자기 은퇴를 하겠다고 생각을 하는가 본데……"
    extra"언젠간……{cps=2} {/cps}어쩌면 빠른 시일내에 할지도 모를것 같아서 이렇게 미리 말 하는거 뿐이니까 당장은 걱정 할 필요가 없다네"
    play bgs "bgs/people.mp3"
    "회장님이 바로 은퇴를 하는것이 아니라는 말에 안심을 하고 있었다."
    stop bgs
    $ extra_name = '회사 간부'
    extra"그런 건 미리 말씀을 해주셨어야;;"
    $ extra_name = '장인 어른'
    extra"내가 \'곧 은퇴\'를 한다고 했잖은가"
    $ extra_name = '회사 간부'
    extra"생각해보니까 그런것 같기도……"
    $ extra_name = '높은 직원'
    extra"그렇다면 후계자도 미리 생각 하셨나요?"
    play bgs "bgs/people.mp3"
    "후계자 라는 말을 꺼내자, 다시 주변이 소란스러워지기 시작했다."
    "솔직히 말해서 나도 조금 궁금했다."
    "일단은 같이 일을 하게 될 사람이니까……"
    edward_think"하지만 직위 적으로도, 족보 적으로도, 능력 적으로도 가장 유력한 후계자는 메리겠지?"
    stop bgs
    $ extra_name = '장인 어른'
    extra"당연히 후계자는 미리 생각해두었지"
    extra"에헴……"
    stop music
    extend" 차기 화장은……{cps=2} {/cps}\'메리 토머\'로 할 생각인데 어떻게 생각 하시는가요?"
    play bgs "bgs/people.mp3"
    edward_think"역시……"
    "나는 메리가 회장님의 후계자로 뽑힐걸 미리 예상해서 아무런 반응이 없었지만……"
    "그런데 어째서인지 주변에선 소란서러워졌다."
    play music "bgm/sirius5.mp3"
    "아니, 분위기도 갑자기 바꼈다."
    "모두들 소근거리기 시작하고……"
    "어째 불만이 가득한 표정들이었다."
    $ extra_name = '회사 간부'
    stop bgs
    extra"회장님……{cps=2 } {/cps}그거 진심 이십니까?"
    $ extra_name = '장인 어른'
    extra"그렇다만……{cps=2} {/cps}혹시 문제라도 있는가?"
    $ extra_name = '회사 간부'
    extra"…………"
    $ extra_name = '높은 직원'
    extra"솔직히 말하겠습니다……"
    extra"다른 분들은 어떤지 모르겠지만……{cps=2} {/cps}전 토머 사장님이 회장님의 후계자로 서는것에 적극 반대 합니다."
    $ extra_name = '회사 간부'
    extra"사실 저도 반대 합니다……"
    play bgs "bgs/people.mp3"
    "그리고 차례대로 메리가 회장님의 후계자로 서는것에 반대하기 시작했다."
    "나는 이 상황이 전혀 이해가 안갔다……"
    "메리는 공부도 잘하고, 실제 능력도 있고, 학력도 높은데……{cps=2} {/cps}왜 다들 반대를 하는 걸까……?"
    stop bgs
    $ extra_name = '장인 어른'
    extra"의외로군?{cps=2} {/cps}다들 찬성을 할줄 알았는데 말이지"
    $ extra_name = '회사 간부'
    extra"확실히 토머 사장님께서 주가 폭락 사건의 해결 방안을 제시해준 덕분에 이 이상의 피해는 막았을지 모르겠습니다……"
    extra"하지만 사장님 께서는 회장의 자리에 서기엔 아직 경험이 부족하지 않을까요?"
    $ extra_name = '장인 어른'
    extra"경험이 부족하다고?"
    extra"메리는 이곳에서 5년 가까이 일을 해왔는데도 경험이 부족하다는 건가?!"
    $ extra_name = '회사 간부'
    extra"저는 회장님 밑에서 10년 이상을 일 해왔습니다……"
    extra"그리고 제가 말한 경험은 회사에서 얼마나 오랫동안 일을 했냐는 게 아니고……"
    extend" 인생의 경험이 부족하다는 뜻입니다."
    extra"회장님께선 사업만 30년 가까이 하셨지만,{cps=2} {/cps}방면 토머 사장님은 이제 겨우 30세 인걸로 알고있습니다!"
    $ extra_name = '장인 어른'
    extra"……자네에게 있어서 경험의 기준이란 무엇인가?"
    extra"나이랑 비례 하는것인가?"
    $ extra_name = '회사 간부'
    extra"음……"
    $ extra_name = '장인 어른'
    extra"평생을 오리엔스 내에서만 생활해온 자네보단 외국에서 살다온 메리가 더 많은 경험을 했다는것 만큼은 내가 장담하지……!"
    "회장님의 어투가 조금 높아졌다."
    "여기서 진정하라는 말을 하는 게……"
    play sound "se/search_bag.mp3"
    $ extra_name = '높은 직원'
    extra"회장님!{cps=2} {/cps}침착해주세요!"
    "……내가 나설 타이밍을 놓쳐버렸다."
    extra"그리고 이사님도 사장님에 대해서 함부로 말씀하지 말아주세요!"
    $ extra_name = '회사 간부'
    extra"죄송합니다……{cps=2} {/cps}회장님……"
    $ extra_name = '장인 어른'
    extra"나야말로 너무 흥분을 했구나……"
    $ extra_name = '회사 간부'
    extra"하지만 전 여전히 토머 사장님이 회장님의 뒤를 잇는 건 반대합니다"
    $ extra_name = '장인 어른'
    extra"자네, 정말 그렇게 나올건가……"
    $ extra_name = '회사 간부'
    extra"회장님께서 말씀하신대로 경험을 나이와 비례해서 생각한건 저의 불찰 이었습니다"
    extra"하지만 토머 사장님이 회장 자리에 서는 건 회사의 이미지와 관련이 있는 일 입니다!"
    $ extra_name = '장인 어른'
    extra"이미지?{cps=2} {/cps}도대체 뭐가 문제인겐가?"
    extra"오리엔스에서 몇 안되는 하버드 대학교 졸업생, 노스탤지어 토이즈에서 디자인 팀장 경력 1년에 사장 경력 4년"
    extra"이정도면 주주들도 신뢰를 할거라 생각한다만?"
    $ extra_name = '회사 간부'
    extra"하지만 사장님은……"
    stop music
    extend" 여자잖아요……"
    extra"여자가 집안일을 제외한 다른 일을 한다는것도 전 맘에 안들긴 했지만……"
    extra"확실히 토머 사장님은 \'일\'을 하는덴 문제가 없다고 생각합니다"
    extra"하지만 \'대표\'를 하는 건 다른 이야기 입니다"
    $ extra_name = '장인 어른'
    extra"또 그 얘기를 꺼는 건가……"
    edward_think"또 라고?"
    edward_think"그렇다는 건 예전에도……"
    extra"그 얘기는 메리가 사장 자리에 설때 다 끝나지 않았는가?"
    $ extra_name = '회사 간부'
    extra"사장 자리는 회장님의 보좌로 어느정도 메꾸는 게 가능하지만, 회장자리는 어찌할 방법이 없습니다"
    extra"그리고 만약 이 회사가 여자 하나에 의해서 운영되고 있다는 사실을 알았다간 주주들이 어떻게 생각을 할지……"
    $ extra_name = '장인 어른'
    extra"자네가 말한 회사 이미지 라는 게 이런 걸 뜻하는 거였나……?"
    $ extra_name = '회사 간부'
    extra"맞습니다……"
    extra"방금 말씀 드렸다시피 사장 자리 까지는 어떻게든 됐었지만……{cps=2} {/cps}역시 회장 자리는……"
    edward_think"잠깐?!"
    edward_think"다른것도 아니고, 지금 메리가 여자라는 이유 만으로 회장 자리를 넘겨줄수 없다는거야?!"
    $ extra_name = '장인 어른'
    extra"다른 분들도 같은 생각이신지?"
    $ extra_name = '모두'
    extra"…………"
    "다들 가만히 침묵을 하고있었다."
    "지금 내가 알 수 있는 건……{cps=2} {/cps}이 침묵은 긍정의 의미라는것 정도……"
    "정말 너무하단 생각이 들었다……"
    "그 누구보다 노스탤지어 토이즈를 생각했던 메리가 이런 대우를 받다니……"
    "게다가 이게 처음이 아니었어……"
    "메리는 내가 모르는 사이에 계속해서 싸워왔던거야……"
    "내가 메리를 위해서 해줄 수 있는것은 무엇인가……"
    stop music
    edward"저,{cps=2} {/cps}저는 메리가 이 회사를 대표 하는것에 찬성합니다!"
    edward_think"말해버렸다……"
    $ extra_name = '회사 간부'
    play music "bgm/sirius3.mp3"
    extra"토머 차장,{cps=2} {/cps}자네가 그런 말을 해도 설득력이 없다네"
    edward"네?"
    $ extra_name = '높은 직원'
    extra"이사님의 말씀이 맞습니다……"
    extra"차장님 께서는 그냥 가만히 계시는 게……"
    edward"네?{cps=2} {/cps}네?"
    "나는 갑자기 어리둥절했다."
    edward_think"내가 뭘 잘못말했나?"
    $ extra_name = '회사 간부'
    extra"본인의 면전에다가 말을 하는것도 좀 그렇긴 하지만……"
    extra"회장님 께서는 차장님을 보고 못 느끼시겠 습니까?"
    extra"순전히 토머 사장님의 결정에 의해서 아무런 능력도 없는 토머 차장을 저희 회사에 취직 시켰습니다"
    extra"그것도 모자라선 차장이라는 자리까지 아무런 성과도 없이 고속 승진시켰고요!"
    $ extra_name = '장인 어른'
    extra"부,{cps=2} {/cps}분명 메리도 생각이……"
    edward_think"이 상황……"
    "난 왜 내 말이 설득력이 없다는 것인지 알았다……"
    "내가 바로 메리의 \'실패\'를 증명하고 있었기 때문이다."
    $ extra_name = '회사 간부'
    extra"토머 사장님은 여기있는 에드워드 차장을 만나고 나서부터 회사일도 게을리하고"
    extra"회사를 자주 몰래 빠져나오고, 결혼 후에는 출근 조차 하지 않습니다!"
    extra"이래서 전 여자가 무언가를 대표 하는것에 반대 하는것입니다!"
    extra"논리와 이성적인 생각이 아닌 오직 감성적인 시각으로만 바라보려고 하고……"
    $ extra_name = '장인 어른'
    extra"하지만 자네도 메리가 주가 폭락 사건을 혼자서 해결 했다는 걸 알고 있잖은가?!"
    $ extra_name = '높은 직원'
    extra"회장님……"
    extra"혹시 메리 사장님이 회장님의 따님이라는 이유만으로 너무 높게 평가하시는 게 아니신지……?"
    $ extra_name = '장인 어른'
    extra"으……"
    extra"메리는……{cps=2} {/cps}그냥 평범한 여자가 아니란 말이다……"
    $ extra_name = '회사 간부'
    extra"죄송한 말씀이지만{cps=2} {/cps}에드워드 차장을 보고있으면 설득이 전혀 안됩니다"
    "나는 화를 내고싶었다."
    "하지만……{cps=2} {/cps}내가 뭘 할 수 있다고……"
    "언제나 이랬었다……"
    "난 언제나 약자니까……"
    extra"고작 여자가 회사의 회장이 된다는 것에 부적합 하다는 건 저 뿐만 아니라 오리엔스 전체도 알고 있을겁니다"
    $ extra_name = '장인 어른'
    extra"결론은……{cps=2} {/cps}여자이기 때문에 회장 자리엔 앉힐 수 없다는 건가?"
    $ extra_name= '회사 간부'
    extra"그렇다고 할 수도 있죠……"
    extra"예로부터 여성은 집안일을, 남성은 밖에서 사냥을 해왔습니다"
    extra"여성은 남자들이 지켜야 할 존재 이지, 결코 일을 시켜선 안된다고 생각합니다"
    stop music
    $ extra_name = '장인 어른'
    extra"자네의 그 \'전통\'과 \'고정관념\'이 이 세상의 발전을 멈추고 있다면 어쩔겐가?"
    $ extra_name = '회사 간부'
    extra"그건 무슨 뜻이죠?"
    $ extra_name = '장인 어른'
    play music "bgm/sirius1.mp3"
    extra"혹시 \'리제 마이트너(Lise Meitner)\'라고 아는가?"
    extra"호주 출신의 물리학자 인데, 나 같은 유대계 가족에서 태어났다고 해"
    extra"그녀는 실력이 있음에도 불구하고 거의 평생을 여자라는 이유만으로 많은 피해와 손해를 봤지"
    extra"하지만 훗날, 마이트너는 핵분열의 발견과, 그 유명한 물리 학자 \'오토 한(Otto Hahn)\'의 연구에 가장 큰 영향을 주게 되지"
    extra"그 사람들은 고작 여자라는 이유만으로,{cps=2} {/cps}고작 여자에 대한 근거 없는 편견 때문에 세기적인 인재를 놓칠뻔했어"
    extra"게다가 이런식으로 다수의 편견 때문에 지금의 인류를 만든 위인을 없앨뻔 한 적이 많다고 하더군"
    extra"아니, 어쩌면 벌써 말도 안되게 많은 인재를 놓쳤을 수도 있겠지"
    extra"……어쨌건 내가 하고싶은 말은, 역사적으로도 많았던 실수를 계속 반복 해야 할 이유는 없다는 거야"
    $ extra_name = '회사 간부'
    extra"하지만 그렇다고 해서 토머 사장님이 회장 자리에 오른다고 꼭 성공한다는 건 아니잖습니까?"
    $ extra_name = '장인 어른'
    extra"흠……{cps=2} {/cps}이게 그나마 낫구나"
    $ extra_name = '회사 간부'
    extra"네?"
    play music "bgm/smooth1.mp3"
    $ extra_name = '장인 어른'
    extra"그런식으로 생각 하는 게 자네의 처음 의견보다 훨씬 낫다는 걸세"
    extra"앞으로도 \'여자\'같이 어쩔 수 없는 이유가 아닌, \'실력\'으로 사람을 평가 하자고"
    extra"오늘은 시간이 이렇게 됐으니 후계자 얘기는 다음 회의로 미루겠네"
    play sound "se/search_bag.mp3"
    $ renpy.pause(0.5)
    extra"다음 회의는 메리 토머가 회사에 출근을 하는 즉시 시작하도록 하고, 그때 까진 내가 회장 자리에 있겠어"
    scene black with moveright
    "이렇게 해서 긴급 회의는 일단 끝이 났다."
    "그런데 정말……{cps=2} {/cps}오늘은 배운 게 많은 거 같다……"
    "처음엔 메리도 아버지가 회장 이기 때문에 나같은 낙하산으로 들어온 줄 알았는데……"
    "나름대로 노력을 하고 있었어"
    stop music
    "정말 난 메리에 대해서 아는 게 하나도 없었구나……"
    "나는 좀 더 알고싶다는 생각이 들었다."
    play bgs "bgs/people.mp3"
    play music "bgm/beat2.mp3"
    scene bg employee_office_day with moveright
    show effect1
    play sound "se/shock.ogg"
    nixon"{size=45}네?!{/size}" with lshake
    hide effect1
    nixon"메리{cps=2} {/cps}……가 아니라, 토머 사장님의 대학 시절에 대해서 알려 달라뇨?!"
    nixon"이거 좀 갑작스러운데……{cps=2} {/cps}회의실에서 무슨 일 있었어요?"
    edward"그게……"
    
    
    
    
    
    
    
    
    
    
return
