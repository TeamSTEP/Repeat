# 캐릭터가 사용할 스프라이트를 정의 합니다.
image extra_math = "sprite/math_teach.png"
image extra_social = "sprite/social_teach.png"
image extra_doctor = "sprite/doctor.png"
image extra_realbugs = "sprite/realbugs.png"
#########################################스테반 초상화
image stephan = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan mouth normal", "sprite/stephan_mouth_close.png"),
    )
image stephan eyes normal: #눈 정의
    "sprite/stephan_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_eye_close.png" #감은 눈 경로
    .25
    repeat
image stephan mouth normal: #입 정의
    "sprite/stephan_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_mouth_close.png" #입 닫음 경로
    .1
    repeat

image stephan shock = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_shock eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_talk mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )
image stephan_shock eyes normal: #눈 정의
    "sprite/stephan_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_shock_eye_close.png" #감은 눈 경로
    .25
    repeat
    
image stephan blush = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_shock eyes normal", #test의 눈 좌표
    (0,0), "sprite/stephan_blush_effect.png",
    (0,0), WhileSpeaking("stephan", "stephan_talk mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )

image stephan shock2 = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_shock eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan mouth normal", "sprite/stephan_mouth_close.png"), #test의 입 경로
    )

image stephan shock3 = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_shock3 eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan mouth sirius normal", "sprite/stephan_sirius_mouth_close.png"), #test의 입 경로
    )
image stephan_shock3 eyes normal: #눈 정의
    "sprite/stephan_shock3_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_sirius_eye_close.png" #감은 눈 경로
    .25
    repeat

image stephan smile = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/stephan_smile_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan mouth normal", "sprite/stephan_mouth_close.png"), #test의 입 경로
    )
image stephan smile2 = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_smile2_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_smile2 eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_smile2 mouth normal", "sprite/stephan_smile2_mouth_close.png"), #test의 입 경로
    )
image stephan_smile2 eyes normal: #눈 정의
    "sprite/stephan_smile2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_smile2_eye_close.png" #감은 눈 경로
    .25
    repeat
image stephan_smile2 mouth normal: #입 정의
    "sprite/stephan_smile2_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_smile2_mouth_close.png" #입 닫음 경로
    .1
    repeat

image stephan talk = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_talk mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )
image stephan_talk mouth normal: #입 정의
    "sprite/stephan_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat

image stephan think = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_think_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_think eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_talk mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )
image stephan_think eyes normal: #눈 정의
    "sprite/stephan_think_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_think_eye_close.png" #감은 눈 경로
    .25
    repeat

image stephan yawn = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_yawn_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/stephan_yawn_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_yawn mouth normal", "sprite/stephan_yawn_mouth_close.png"), #test의 입 경로
    )
image stephan_yawn mouth normal: #입 정의
    "sprite/stephan_yawn_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_yawn_mouth_close.png" #입 닫음 경로
    .1
    repeat

image stephan hurt = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_hurt_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_hurt eyes normal", #test의 눈 좌표
    )
image stephan_hurt eyes normal: #눈 정의
    "sprite/stephan_hurt_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_hurt_eye_close.png" #감은 눈 경로
    .25
    repeat

image stephan hurt2 = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_hurt2_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_hurt2 eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_hurt2 mouth normal", "sprite/stephan_hurt2_mouth_close.png"), #test의 입 경로
    )
image stephan_hurt2 eyes normal: #눈 정의
    "sprite/stephan_hurt2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_hurt2_eye_close.png" #감은 눈 경로
    .25
    repeat
image stephan_hurt2 mouth normal: #입 정의
    "sprite/stephan_hurt2_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_hurt2_mouth_close.png" #입 닫음 경로
    .1
    repeat

image stephan fear = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_fear eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_fear mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )
image stephan_fear eyes normal: #눈 정의
    "sprite/stephan_fear_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_fear_eye_close.png" #감은 눈 경로
    .25
    repeat
image stephan_fear mouth normal: #입 정의
    "sprite/stephan_fear_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat

image stephan sad = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_sad eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_talk mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )
image stephan_sad eyes normal: #눈 정의
    "sprite/stephan_sad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_sad_eye_close.png" #감은 눈 경로
    .25
    repeat

image stephan mad = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/stephan_mad_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan_talk mouth normal", "sprite/stephan_talk_mouth_close.png"), #test의 입 경로
    )

image stephan sad2 = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan_sad eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan mouth normal", "sprite/stephan_mouth_close.png"), #test의 입 경로
    )
image stephan sirius = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/stephan_body.png", #몸통 스프라이트 경로
    (0,0), "stephan eyes sirius normal", #test의 눈 좌표
    (0,0), WhileSpeaking("stephan", "stephan mouth sirius normal", "sprite/stephan_sirius_mouth_close.png"),
    )
image stephan eyes sirius normal: #눈 정의
    "sprite/stephan_sirius_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/stephan_sirius_eye_close.png" #감은 눈 경로
    .25
    repeat
image stephan mouth sirius normal: #입 정의
    "sprite/stephan_sirius_mouth_open.png" #입 벌림 경로
    .1
    "sprite/stephan_sirius_mouth_close.png" #입 닫음 경로
    .1
    repeat

#########################################윌리 초상화
image willy = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_body.png", #몸통 스프라이트 경로
    (0,0), "willy eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy mouth normal", "sprite/willy_mouth_close.png"),
    )
image willy eyes normal: #눈 정의
    "sprite/willy_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy mouth normal: #입 정의
    "sprite/willy_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_mouth_close.png" #입 닫음 경로
    .1
    repeat
image willy shock = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_body.png", #몸통 스프라이트 경로
    (0,0), "willy_shock eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy_talk mouth normal", "sprite/willy_talk_mouth_close.png"),
    )
image willy_shock eyes normal: #눈 정의
    "sprite/willy_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy smile = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_smile_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/willy_smile_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy_smile mouth normal", "sprite/willy_mouth_close.png"),
    )
image willy_smile mouth normal: #입 정의
    "sprite/willy_smile_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_mouth_close.png" #입 닫음 경로
    .1
    repeat
image willy smile2 = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_smile_body.png", #몸통 스프라이트 경로
    (0,0), "willy_smile2 eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy_smile2 mouth normal", "sprite/willy_mouth_close.png"),
    )
image willy_smile2 eyes normal: #눈 정의
    "sprite/willy_smile2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_smile2_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy_smile2 mouth normal: #입 정의
    "sprite/willy_smile2_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_mouth_close.png" #입 닫음 경로
    .1
    repeat
image willy talk = LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_body.png", #몸통 스프라이트 경로
    (0,0), "willy eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy_talk mouth normal", "sprite/willy_talk_mouth_close.png"),
    )
image willy_talk mouth normal: #입 정의
    "sprite/willy_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image willy mad= LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_body.png", #몸통 스프라이트 경로
    (0,0), "willy eyes mad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy mouth mad normal", "sprite/willy_talk_mouth_close.png"),
    )
image willy eyes mad normal: #눈 정의
    "sprite/willy_mad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_mad_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy mouth mad normal: #입 정의
    "sprite/willy_mad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image willy sirius= LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_body.png", #몸통 스프라이트 경로
    (0,0), "willy eyes sirius normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy mouth sirius normal", "sprite/willy_talk_mouth_close.png"),
    )
image willy eyes sirius normal: #눈 정의
    "sprite/willy_sirius_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_sirius_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy mouth sirius normal: #입 정의
    "sprite/willy_sirius_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image willy think= LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_body.png", #몸통 스프라이트 경로
    (0,0), "willy eyes think normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy mouth talk normal", "sprite/willy_talk_mouth_close.png"),
    )
image willy eyes think normal: #눈 정의
    "sprite/willy_think_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy shock2= LiveComposite( #애니메이션 스프라이트 정의
    (392, 664), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/willy_shock2_body.png", #몸통 스프라이트 경로
    (0,0), "willy eyes shock2 normal", #test의 눈 좌표
    (0,0), WhileSpeaking("willy", "willy mouth shock2 normal", "sprite/willy_shock2_mouth_close.png"),
    )
image willy eyes shock2 normal: #눈 정의
    "sprite/willy_shock2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/willy_shock2_eye_close.png" #감은 눈 경로
    .25
    repeat
image willy mouth shock2 normal: #입 정의
    "sprite/willy_shock2_mouth_open.png" #입 벌림 경로
    .1
    "sprite/willy_shock2_mouth_close.png" #입 닫음 경로
    .1
    repeat
#########################################멜 초상화
image mel = LiveComposite( #애니메이션 스프라이트 정의
    (325, 589), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mel_body.png", #몸통 스프라이트 경로
    (0,0), "mel eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mel", "mel mouth normal", "sprite/mel_mouth_close.png"),
    )
image mel eyes normal: #눈 정의
    "sprite/mel_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mel_eye_close.png" #감은 눈 경로
    .25
    repeat
image mel mouth normal: #입 정의
    "sprite/mel_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mel_mouth_close.png" #입 닫음 경로
    .1
    repeat

image mel talk = LiveComposite( #애니메이션 스프라이트 정의
    (325, 589), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mel_body.png", #몸통 스프라이트 경로
    (0,0), "mel eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mel", "mel_talk mouth normal", "sprite/mel_talk_mouth_close.png"),
    )
image mel_talk mouth normal: #입 정의
    "sprite/mel_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mel_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat

image mel sad = LiveComposite( #애니메이션 스프라이트 정의
    (325, 589), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mel_body.png", #몸통 스프라이트 경로
    (0,0), "mel_sad eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mel", "mel_sad mouth normal", "sprite/mel_talk_mouth_close.png"),
    )
image mel_sad eyes normal: #눈 정의
    "sprite/mel_sad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mel_sad_eye_close.png" #감은 눈 경로
    .25
    repeat
image mel_sad mouth normal: #입 정의
    "sprite/mel_sad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mel_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mel sirius = LiveComposite( #애니메이션 스프라이트 정의
    (325, 589), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mel_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/mel_sirius_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("mel", "mel_talk mouth normal", "sprite/mel_talk_mouth_close.png"),
    )
image mel smile = LiveComposite( #애니메이션 스프라이트 정의
    (325, 589), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mel_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/mel_smile_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("mel", "mel_smile mouth normal", "sprite/mel_mouth_close.png"),
    )
image mel_smile mouth normal: #입 정의
    "sprite/mel_smile_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mel_mouth_close.png" #입 닫음 경로
    .1
    repeat
#########################################렌스 초상화
image lance = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth normal", "sprite/lance_mouth_close.png"),
    )
image lance eyes normal: #눈 정의
    "sprite/lance_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lance_eye_close.png" #감은 눈 경로
    .25
    repeat
image lance mouth normal: #입 정의
    "sprite/lance_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lance_mouth_close.png" #입 닫음 경로
    .1
    repeat

image lance talk = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_talk_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth talk normal", "sprite/lance_talk_mouth_close.png"),
    )
image lance mouth talk normal: #입 정의
    "sprite/lance_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lance_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat

image lance shock = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_talk_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth talk normal", "sprite/lance_talk_mouth_close.png"),
    )
image lance eyes shock normal: #눈 정의
    "sprite/lance_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lance_shock_eye_close.png" #감은 눈 경로
    .25
    repeat

image lance shock2 = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_shock2_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes shock2 normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth shock2 normal", "sprite/lance_shock2_mouth_close.png"),
    )
image lance eyes shock2 normal: #눈 정의
    "sprite/lance_shock2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lance_shock2_eye_close.png" #감은 눈 경로
    .25
    repeat
image lance mouth shock2 normal: #입 정의
    "sprite/lance_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lance_shock2_mouth_close.png" #입 닫음 경로
    .1
    repeat

image lance sad = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_talk_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes sad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth mad normal", "sprite/lance_talk_mouth_close.png"),
    )
image lance eyes sad normal: #눈 정의
    "sprite/lance_sad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lance_sad_eye_close.png" #감은 눈 경로
    .25
    repeat

image lance mad = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_talk_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes mad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth mad normal", "sprite/lance_talk_mouth_close.png"),
    )
image lance eyes mad normal: #눈 정의
    "sprite/lance_mad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lance_mad_eye_close.png" #감은 눈 경로
    .25
    repeat
image lance mouth mad normal: #입 정의
    "sprite/lance_mad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lance_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat

image lance gun = LiveComposite( #애니메이션 스프라이트 정의
    (389, 658), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lance_gun_body.png", #몸통 스프라이트 경로
    (0,0), "lance eyes gun normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lance", "lance mouth gun normal", "sprite/lance_shock2_mouth_close.png"),
    )
image lance eyes gun normal: #눈 정의
    "sprite/lance_gun_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lance_gun_eye_close.png" #감은 눈 경로
    .25
    repeat
image lance mouth gun normal: #입 정의
    "sprite/lance_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lance_shock2_mouth_close.png" #입 닫음 경로
    .1
    repeat
########################################세바스찬 초상화
image seb = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_body.png", #몸통 스프라이트 경로
    (0,0), "seb eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("seb", "seb mouth normal", "sprite/seb_mouth_close.png"),
    )
image seb eyes normal: #눈 정의
    "sprite/seb_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/seb_eye_close.png" #감은 눈 경로
    .25
    repeat
image seb mouth normal: #입 정의
    "sprite/seb_mouth_open.png" #입 벌림 경로
    .1
    "sprite/seb_mouth_close.png" #입 닫음 경로
    .1
    repeat
image seb talk = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_body.png", #몸통 스프라이트 경로
    (0,0), "seb eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("seb", "seb mouth talk normal", "sprite/seb_talk_mouth_close.png"),
    )
image seb mouth talk normal: #입 정의
    "sprite/seb_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/seb_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image seb think = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_think_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/seb_think_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("seb", "seb mouth think normal", "sprite/seb_talk_mouth_close.png"),
    )
image seb mouth think normal: #입 정의
    "sprite/seb_shock_mouth_open.png" #입 벌림 경로
    .1
    "sprite/seb_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image seb blush = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_think_body.png", #몸통 스프라이트 경로
    (0,0), "seb eyes blush normal", #test의 눈 좌표
    (0,0), "sprite/seb_blush_effect.png",
    (0,0), WhileSpeaking("seb", "seb mouth shock normal", "sprite/seb_shock_mouth_close.png"),
    )
image seb eyes blush normal: #눈 정의
    "sprite/seb_blush_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/seb_blush_eye_close.png" #감은 눈 경로
    .25
    repeat
image seb mouth shock normal: #입 정의
    "sprite/seb_shock_mouth_open.png" #입 벌림 경로
    .1
    "sprite/seb_shock_mouth_close.png" #입 닫음 경로
    .1
    repeat
image seb shock = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_shock_body.png", #몸통 스프라이트 경로
    (0,0), "seb eyes shock normal", #test의 눈 좌표
    (0,0), "sprite/seb_shock_effect.png",
    (0,0), WhileSpeaking("seb", "seb mouth shock normal", "sprite/seb_shock_mouth_close.png"),
    )
image seb eyes shock normal: #눈 정의
    "sprite/seb_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/seb_blush_eye_close.png" #감은 눈 경로
    .25
    repeat
image seb talk cat = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_cat_body.png", #몸통 스프라이트 경로
    (0,0), "seb eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("seb", "seb mouth talk normal", "sprite/seb_talk_mouth_close.png"),
    )
image seb shock cat = LiveComposite( #애니메이션 스프라이트 정의
    (385, 683), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/seb_cat_body.png", #몸통 스프라이트 경로
    (0,0), "seb eyes shock normal", #test의 눈 좌표
    (0,0), "sprite/seb_shock_effect.png",
    (0,0), WhileSpeaking("seb", "seb mouth shock normal", "sprite/seb_shock_mouth_close.png"),
    )
########################################시아 초상화
image cia = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_body.png", #몸통 스프라이트 경로
    (0,0), "cia eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth normal", "sprite/cia_mouth_close.png"),
    )
image cia eyes normal: #눈 정의
    "sprite/cia_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/cia_eye_close.png" #감은 눈 경로
    .25
    repeat
image cia mouth normal: #입 정의
    "sprite/cia_mouth_open.png" #입 벌림 경로
    .1
    "sprite/cia_mouth_close.png" #입 닫음 경로
    .1
    repeat
image cia talk = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_body.png", #몸통 스프라이트 경로
    (0,0), "cia eyes talk normal", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth talk normal", "sprite/cia_talk_mouth_close.png"),
    )
image cia eyes talk normal: #눈 정의
    "sprite/cia_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/cia_talk_eye_close.png" #감은 눈 경로
    .25
    repeat
image cia mouth talk normal: #입 정의
    "sprite/cia_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/cia_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image cia smile = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_smile_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/cia_eye_close.png", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth normal", "sprite/cia_mouth_close.png"),
    )
image cia think = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_think_body.png", #몸통 스프라이트 경로
    (0,0), "cia eyes think normal", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth think normal", "sprite/cia_think_mouth_close.png"),
    )
image cia eyes think normal: #눈 정의
    "sprite/cia_think_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/cia_talk_eye_close.png" #감은 눈 경로
    .25
    repeat
image cia mouth think normal: #입 정의
    "sprite/cia_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/cia_think_mouth_close.png" #입 닫음 경로
    .1
    repeat
image cia shock = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_think_body.png", #몸통 스프라이트 경로
    (0,0), "cia eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth talk normal", "sprite/cia_talk_mouth_close.png"),
    )
image cia eyes shock normal: #눈 정의
    "sprite/cia_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/cia_talk_eye_close.png" #감은 눈 경로
    .25
    repeat
image cia shine = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_smile_body.png", #몸통 스프라이트 경로
    (0,0), "cia eyes shine normal", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth shine normal", "sprite/cia_mouth_close.png"),
    )
image cia eyes shine normal: #눈 정의
    "sprite/cia_shine_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/cia_talk_eye_close.png" #감은 눈 경로
    .25
    repeat
image cia mouth shine normal: #입 정의
    "sprite/cia_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/cia_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image cia mad = LiveComposite( #애니메이션 스프라이트 정의
    (428,602), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/cia_think_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/cia_mad_effect.png",
    (0,0), "sprite/cia_eye_close.png", #test의 눈 좌표
    (0,0), WhileSpeaking("cia", "cia mouth normal", "sprite/cia_mouth_close.png"),
    )
########################################할아버지 초상화
init:
    image grandpa body = ConditionSwitch(
        "grandpa_body == 'normal'", "sprite/grandpa_body.png",
        "grandpa_body == 'hurt'", "sprite/grandpa_body2.png",
        )
    image grandpa glasses = ConditionSwitch(
        "grandpa_glasses == 'normal'", "sprite/grandpa_glasses.png",
        "grandpa_glasses == 'brown'", "sprite/grandpa_glasses_brown.png",
        )
image grandpa = LiveComposite( #애니메이션 스프라이트 정의
    (392,616), #전체 스프라이트 가로, 세로 해상도
    (0,0), "grandpa body", #몸통 스프라이트 경로
    (0,0), "grandpa glasses", #test의 눈 좌표
    (0,0), WhileSpeaking("edward", "grandpa mouth normal", "sprite/grandpa_mouth_close.png"),
    )
image grandpa mouth normal: #입 정의
    "sprite/grandpa_mouth_open.png" #입 벌림 경로
    .1
    "sprite/grandpa_mouth_close.png" #입 닫음 경로
    .1
    repeat
image grandpa talk = LiveComposite( #애니메이션 스프라이트 정의
    (392,616), #전체 스프라이트 가로, 세로 해상도
    (0,0), "grandpa body", #몸통 스프라이트 경로
    (0,0), "grandpa glasses", #test의 눈 좌표
    (0,0), WhileSpeaking("edward", "grandpa mouth talk normal", "sprite/grandpa_talk_mouth_close.png"),
    )
image grandpa mouth talk normal: #입 정의
    "sprite/grandpa_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/grandpa_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image grandpa shock = LiveComposite( #애니메이션 스프라이트 정의
    (392,616), #전체 스프라이트 가로, 세로 해상도
    (0,0), "grandpa body", #몸통 스프라이트 경로
    (0,0), "grandpa glasses", #test의 눈 좌표
    (0,0), "sprite/grandpa_shock_effect.png",
    (0,0), WhileSpeaking("edward", "grandpa mouth shock normal", "sprite/grandpa_talk_mouth_close.png"),
    )
image grandpa mouth shock normal: #입 정의
    "sprite/grandpa_shock_mouth_open.png" #입 벌림 경로
    .1
    "sprite/grandpa_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image grandpa think = LiveComposite( #애니메이션 스프라이트 정의
    (392,616), #전체 스프라이트 가로, 세로 해상도
    (0,0), "grandpa body", #몸통 스프라이트 경로
    (0,0), "grandpa glasses", #test의 눈 좌표
    (0,0), WhileSpeaking("edward", "grandpa mouth think normal", "sprite/grandpa_think_mouth_close.png"),
    )
image grandpa mouth think normal: #입 정의
    "sprite/grandpa_think_mouth_open.png" #입 벌림 경로
    .1
    "sprite/grandpa_think_mouth_close.png" #입 닫음 경로
    .1
    repeat
image grandpa mad = LiveComposite( #애니메이션 스프라이트 정의
    (392,616), #전체 스프라이트 가로, 세로 해상도
    (0,0), "grandpa body", #몸통 스프라이트 경로
    (0,0), "grandpa glasses", #test의 눈 좌표
    (0,0), WhileSpeaking("edward", "grandpa mouth mad normal", "sprite/grandpa_mad_mouth_close.png"),
    )
image grandpa mouth mad normal: #입 정의
    "sprite/grandpa_mad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/grandpa_mad_mouth_close.png" #입 닫음 경로
    .1
    repeat
image grandpa cough = LiveComposite( #애니메이션 스프라이트 정의
    (392,616), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/grandpa_cough_body.png", #몸통 스프라이트 경로
    (0,0), "grandpa glasses", #test의 눈 좌표
    (0,0), WhileSpeaking("edward", "grandpa mouth mad normal", "sprite/grandpa_mad_mouth_close.png"),
    )
########################################메리 초상화
#init python:
    #mary_cloth = 1
    #1 = 양복, 2 = 평상복, 3 = 잠옷/환자복
init:
    $ mary_hair = 'normal'
    $ mary_cloth = 1
    image mary hair = ConditionSwitch(
        "mary_hair == 'normal'", "system/bar_empty.png",
        "mary_hair == 'mad'", "sprite/mary_hair.png",
        )
image mary = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth normal", "sprite/mary_mouth_close.png"),
    )
image mary eyes normal: #눈 정의
    "sprite/mary_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary mouth normal: #입 정의
    "sprite/mary_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary talk = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth talk normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary mouth talk normal: #입 정의
    "sprite/mary_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary shock = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_think_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth shock normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes shock normal: #눈 정의
    "sprite/mary_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_shock_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary mouth shock normal: #입 정의
    "sprite/mary_shock_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary shock2 = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth normal", "sprite/mary_mouth_close.png"),
    )
image mary shock3 = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_think_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes shock3 normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth shock normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes shock3 normal: #눈 정의
    "sprite/mary_shock3_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_shock3_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary smile = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "sprite/mary_smile_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth normal", "sprite/mary_mouth_close.png"),
    )
image mary shy = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_think_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes shy normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth talk normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes shy normal: #눈 정의
    "sprite/mary_shy_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_shy_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary shy2 = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "sprite/mary_shock_effect.png",
    (0,0), "mary eyes shy2 normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth shy2 normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes shy2 normal: #눈 정의
    "sprite/mary_shy2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_shy_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary mouth shy2 normal: #입 정의
    "sprite/mary_shy2_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary sad = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes sad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth talk normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes sad normal: #눈 정의
    "sprite/mary_sad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_sad_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary tired = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_hurt_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes tired normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth tired normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes tired normal: #눈 정의
    "sprite/mary_tired_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_tired_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary mouth tired normal: #입 정의
    "sprite/mary_tired_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary tsun = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes tsun normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth tsun normal", "sprite/mary_tsun_mouth_close.png"),
    )
image mary eyes tsun normal: #눈 정의
    "sprite/mary_tsun_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary mouth tsun normal: #입 정의
    "sprite/mary_tsun_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_tsun_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary mad = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_hurt_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes mad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth talk normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes mad normal: #눈 정의
    "sprite/mary_mad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_mad_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary mad2 = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes mad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth normal", "sprite/mary_mouth_close.png"),
    )
image mary cry = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes cry normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth tired normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary eyes cry normal: #눈 정의
    "sprite/mary_cry_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_cry_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary tease = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_think_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes tease normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth normal", "sprite/mary_mouth_close.png"),
    )
image mary eyes tease normal: #눈 정의
    "sprite/mary_tease_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_eye_close.png" #감은 눈 경로
    .25
    repeat
image mary hurt = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_hurt_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "sprite/mary_hurt_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth hurt normal", "sprite/mary_cough_mouth_close.png"),
    )
image mary mouth hurt normal: #입 정의
    "sprite/mary_shy2_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_cough_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary think = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_think_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "sprite/mary_eye_close.png", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth talk normal", "sprite/mary_talk_mouth_close.png"),
    )
image mary cough = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_hurt_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "sprite/mary_cough_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth cough normal", "sprite/mary_cough_mouth_close.png"),
    )
image mary mouth cough normal: #입 정의
    "sprite/mary_cough_mouth_open.png" #입 벌림 경로
    .1
    "sprite/mary_cough_mouth_close.png" #입 닫음 경로
    .1
    repeat
image mary happy = LiveComposite( #애니메이션 스프라이트 정의
    (296,604), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/mary_hurt_body[mary_cloth].png", #몸통 스프라이트 경로
    (0,0), "mary hair",
    (0,0), "mary eyes happy normal", #test의 눈 좌표
    (0,0), WhileSpeaking("mary", "mary mouth normal", "sprite/mary_mouth_close.png"),
    )
image mary eyes happy normal: #눈 정의
    "sprite/mary_happy_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/mary_shy_eye_close.png" #감은 눈 경로
    .25
    repeat
########################################앤 초상화
image anne = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "anne eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth normal", "sprite/anne_mouth_close.png"),
    )
image anne eyes normal: #눈 정의
    "sprite/anne_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/anne_eye_close.png" #감은 눈 경로
    .25
    repeat
image anne mouth normal: #입 정의
    "sprite/anne_mouth_open.png" #입 벌림 경로
    .1
    "sprite/anne_mouth_close.png" #입 닫음 경로
    .1
    repeat
image anne think = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/anne_think_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth think normal", "sprite/anne_think_mouth_close.png"),
    )
image anne mouth think normal: #입 정의
    "sprite/anne_mouth_open.png" #입 벌림 경로
    .1
    "sprite/anne_think_mouth_close.png" #입 닫음 경로
    .1
    repeat
image anne shy = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/anne_blush.png",
    (0,0), "anne eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth normal", "sprite/anne_mouth_close.png"),
    )
image anne eyes shock normal: #눈 정의
    "sprite/anne_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/anne_eye_close.png" #감은 눈 경로
    .25
    repeat
image anne shock = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_shock_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/anne_blush.png",
    (0,0), "anne eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth shock normal", "sprite/anne_think_mouth_close.png"),
    )
image anne mouth shock normal: #입 정의
    "sprite/anne_shock_mouth_open.png" #입 벌림 경로
    .1
    "sprite/anne_think_mouth_close.png" #입 닫음 경로
    .1
    repeat
image anne shock2 = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_shock_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/anne_blush.png",
    (0,0), "anne eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth shock normal", "sprite/anne_think_mouth_close.png"),
    )
image anne yan = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/anne_blush.png",
    (0,0), "anne eyes yan normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth yan normal", "sprite/anne_yan_mouth_close.png"),
    )
image anne eyes yan normal: #눈 정의
    "sprite/anne_yan_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/anne_eye_close.png" #감은 눈 경로
    .25
    repeat
image anne mouth yan normal: #입 정의
    "sprite/anne_yan_mouth_open.png" #입 벌림 경로
    .1
    "sprite/anne_yan_mouth_close.png" #입 닫음 경로
    .1
    repeat
image anne yantalk = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "anne eyes yan normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth normal", "sprite/anne_mouth_close.png"),
    )
image anne yanshock2 = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_yan_body.png", #몸통 스프라이트 경로
    (0,0), "anne eyes yanshock2 normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth yanshock2 normal", "sprite/anne_yanshock2_mouth_close.png"),
    )
image anne eyes yanshock2 normal: #눈 정의
    "sprite/anne_yanshock2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/anne_yanshock2_eye_close.png" #감은 눈 경로
    .25
    repeat
image anne mouth yanshock2 normal: #입 정의
    "sprite/anne_shock_mouth_open.png" #입 벌림 경로
    .1
    "sprite/anne_yanshock2_mouth_close.png" #입 닫음 경로
    .1
    repeat
image anne yanshock = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_shock_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/anne_blush.png",
    (0,0), "anne eyes yan normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth shock normal", "sprite/anne_think_mouth_close.png"),
    )
image anne smile = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "anne eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth yan normal", "sprite/anne_yan_mouth_close.png"),
    )
image anne yanmad = LiveComposite( #애니메이션 스프라이트 정의
    (318,576), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/anne_body.png", #몸통 스프라이트 경로
    (0,0), "anne eyes yanmad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("anne", "anne mouth normal", "sprite/anne_mouth_close.png"),
    )
image anne eyes yanmad normal: #눈 정의
    "sprite/anne_yanmad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/anne_eye_close.png" #감은 눈 경로
    .25
    repeat
########################################리사 초상화
image lisa = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_body.png", #몸통 스프라이트 경로
    (0,0), "lisa eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth normal", "sprite/lisa_mouth_close.png"),
    )
image lisa eyes normal: #눈 정의
    "sprite/lisa_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lisa_eye_close.png" #감은 눈 경로
    .25
    repeat
image lisa mouth normal: #입 정의
    "sprite/lisa_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lisa_mouth_close.png" #입 닫음 경로
    .1
    repeat
image lisa talk = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_body.png", #몸통 스프라이트 경로
    (0,0), "lisa eyes normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth talk normal", "sprite/lisa_talk_mouth_close.png"),
    )
image lisa mouth talk normal: #입 정의
    "sprite/lisa_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lisa_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image lisa think = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_think_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/lisa_think_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth talk normal", "sprite/lisa_talk_mouth_close.png"),
    )
image lisa mad = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_mad_body.png", #몸통 스프라이트 경로
    (0,0), "lisa eyes mad normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth mad normal", "sprite/lisa_talk_mouth_close.png"),
    )
image lisa eyes mad normal: #눈 정의
    "sprite/lisa_mad_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lisa_mad_eye_close.png" #감은 눈 경로
    .25
    repeat
image lisa mouth mad normal: #입 정의
    "sprite/lisa_mad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lisa_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image lisa laugh = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_laugh_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("lisa", "lisa mouth laugh normal", "sprite/lisa_laugh_mouth_close.png"),
    )
image lisa mouth laugh normal: #입 정의
    "sprite/lisa_laugh_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lisa_laugh_mouth_close.png" #입 닫음 경로
    .1
    repeat
image lisa smile = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_body.png", #몸통 스프라이트 경로
    (0,0), "sprite/lisa_smile_eye.png", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth smile normal", "sprite/lisa_mouth_close.png"),
    )
image lisa mouth smile normal: #입 정의
    "sprite/lisa_smile_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lisa_mouth_close.png" #입 닫음 경로
    .1
    repeat
image lisa smile2 = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_shy_body.png", #몸통 스프라이트 경로
    (0,0), "lisa eyes smile2 normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth normal", "sprite/lisa_mouth_close.png"),
    )
image lisa eyes smile2 normal: #눈 정의
    "sprite/lisa_smile2_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lisa_eye_close.png" #감은 눈 경로
    .25
    repeat
image lisa shy = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_shy_body.png", #몸통 스프라이트 경로
    (0,0), "lisa eyes shy normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth shy normal", "sprite/lisa_talk_mouth_close.png"),
    )
image lisa eyes shy normal: #눈 정의
    "sprite/lisa_shy_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lisa_shy_eye_close.png" #감은 눈 경로
    .25
    repeat
image lisa mouth shy normal: #입 정의
    "sprite/lisa_shy_mouth_open.png" #입 벌림 경로
    .1
    "sprite/lisa_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image lisa shock = LiveComposite( #애니메이션 스프라이트 정의
    (393, 632), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/lisa_shy_body.png", #몸통 스프라이트 경로
    (0,0), "lisa eyes shock normal", #test의 눈 좌표
    (0,0), WhileSpeaking("lisa", "lisa mouth shy normal", "sprite/lisa_talk_mouth_close.png"),
    )
image lisa eyes shock normal: #눈 정의
    "sprite/lisa_shock_eye_open.png" #뜬 눈 경로
    choice:
        4.5
    choice:
        3.5
    choice:
        1
    "sprite/lisa_shock_eye_close.png" #감은 눈 경로
    .25
    repeat
#########################################아주머니 초상화
image elsara = LiveComposite( #애니메이션 스프라이트 정의
    (422,621), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/elsara_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("elsara", "elsara mouth normal", "sprite/elsara_mouth_close.png"),
    )
image elsara mouth normal: #입 정의
    "sprite/elsara_mouth_open.png" #입 벌림 경로
    .1
    "sprite/elsara_mouth_close.png" #입 닫음 경로
    .1
    repeat
image elsara talk = LiveComposite( #애니메이션 스프라이트 정의
    (422,621), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/elsara_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("elsara", "elsara mouth talk normal", "sprite/elsara_talk_mouth_close.png"),
    )
image elsara mouth talk normal: #입 정의
    "sprite/elsara_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/elsara_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image elsara mad = LiveComposite( #애니메이션 스프라이트 정의
    (422,621), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/elsara_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("elsara", "elsara mouth mad normal", "sprite/elsara_mad_mouth_close.png"),
    )
image elsara mouth mad normal: #입 정의
    "sprite/elsara_mad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/elsara_mad_mouth_close.png" #입 닫음 경로
    .1
    repeat
#########################################메리 아버지 초상화
image marydad = LiveComposite( #애니메이션 스프라이트 정의
    (400,638), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/marydad_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("dad", "marydad mouth normal", "sprite/marydad_mouth_close.png"),
    )
image marydad mouth normal: #입 정의
    "sprite/marydad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/marydad_mouth_close.png" #입 닫음 경로
    .1
    repeat
image marydad talk = LiveComposite( #애니메이션 스프라이트 정의
    (400,638), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/marydad_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("dad", "marydad mouth talk normal", "sprite/marydad_talk_mouth_close.png"),
    )
image marydad mouth talk normal: #입 정의
    "sprite/marydad_talk_mouth_open.png" #입 벌림 경로
    .1
    "sprite/marydad_talk_mouth_close.png" #입 닫음 경로
    .1
    repeat
image marydad mad = LiveComposite( #애니메이션 스프라이트 정의
    (400,638), #전체 스프라이트 가로, 세로 해상도
    (0,0), "sprite/marydad_body.png", #몸통 스프라이트 경로
    (0,0), WhileSpeaking("dad", "marydad mouth mad normal", "sprite/marydad_mad_mouth_close.png"),
    )
image marydad mouth mad normal: #입 정의
    "sprite/marydad_mad_mouth_open.png" #입 벌림 경로
    .1
    "sprite/marydad_mad_mouth_close.png" #입 닫음 경로
    .1
    repeat





