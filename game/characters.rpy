define config.rollback_enabled = False
# Определение персонажей игры.
define mc = Character("[mc_name]", color="#006400")
define asuka = Character("Асука", color="#DC143C", image = "asuka")
define yuki = Character("Юки", color= "#20B2AA", image = "yuki")
define ray = Character("Рей", color="#00FFFF")



define alexandr = Character("Александр", color="#FFD700", image = "alexandr")
define andrew = Character("Андрей", color="#0000CD", image = "andrew") 
define ben = Character("Бенжамин", color="#808000", image = "ben")
define alexei = Character("Алексей", color="#FF4500", image = "alexei")
define vladislav = Character("Владислав", color="#800080", image = "vladislav")


define vs = Character("Военный советник", color="#FFD700")
define ds = Character("Дипломатический советник", color="#FFD700")
define fs = Character("Финансовый советник", color="#FFD700")
define o = Character("Организатор", color="#FFD700")
define mu = Character("Министр услуг", color="#FFD700")

define config.say_attribute_transition = Dissolve(0.3)

# Variables
define dressed_by_asuka = False
define asuka_love_points = 0
define is_loved_by_asuka = False
define conf_started = False
define prepared_for_conf = False


# Images resized
image alexandr serious2:
    "alexandr serious"
    zoom 1.05
image alexandr scared2:
    "alexandr scared"
    zoom 1.05

image ben crying2:
    "ben crying"
    zoom 1.05
image ben nervous2:
    "ben nervous"
    zoom 1.05
image ben serious2:
    "ben serious"
    zoom 1.05

image andrew scared2:
    "andrew scared"
    zoom 1.05
image andrew serious2:
    "andrew serious"
    zoom 1.05   

image alexei confused2:
    "alexei confused"
    zoom 1.05
image alexei evil2:
    "alexei evil"
    zoom 1.05
image alexei sad2:
    "alexei sad"
    zoom 1.05
image alexei serious2:
    "alexei serious"
    zoom 1.05
image alexei smile2:
    "alexei smile"
    zoom 1.05

image vladislav serious2:
    "vladislav serious"
    zoom 1.05
image vladislav scared2:
    "vladislav scared"
    zoom 1.05



# Positions
define center2 = Position(xalign = 0.5, yalign = 0.4)

define left2 = Position(xalign = 0.0, yalign = 1.0)
define leftMid = Position(xalign = 0.35, yalign = 1.0)
define center3 = Position(xalign=0.5, yalign = 1.0)
define rightMid = Position(xalign = 0.7, yalign = 1.0)
define right2 = Position(xalign = 1.0, yalign = 1.0)

define leftMid2 = Position(xalign=0.25, yalign=1.2)
define rightMid2 = Position(xalign=0.8, yalign=1.0)
# Videos
#image documentary = Movie(channel = "movie", play = "videos/VID01_R4_Heads.mp4")