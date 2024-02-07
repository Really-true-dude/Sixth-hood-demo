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


# Variables
define dressed_by_asuka = False
define asuka_love_points = 0
define is_loved_by_asuka = False

define prepared_for_conf = False

# Positions
define center2 = Position(xalign = 0.5, yalign = 0.4)

define left2 = Position(xalign = 0.2, yalign = 0.4)
define leftMid = Position(xalign = 0.3, yalign = 0.4)
define rightMid = Position(xalign = 0.7, yalign = 0.4)
define right2 = Position(xalign = 0.9, yalign = 0.4)
# Videos
#image documentary = Movie(channel = "movie", play = "videos/VID01_R4_Heads.mp4")