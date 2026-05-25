from .Data import star_locations
from .Options import StarShuffle


def westside(state, player):
    return state.has("Contact Lens", player) or state.has("Bobbery", player) or tube_curse(state, player) or ultra_hammer(state, player)


def super_hammer(state, player):
    return state.has("Progressive Hammer", player, 1)


def ultra_hammer(state, player):
    return state.has("Progressive Hammer", player, 2)


def super_boots(state, player):
    return state.has("Progressive Boots", player, 1)


def ultra_boots(state, player):
    return state.has("Progressive Boots", player, 2)


def tube_curse(state, player):
    return state.has("Paper Mode", player) and state.has("Tube Mode", player)


def petal_left(state, player):
    return state.has("Plane Mode", player)

def petal_left_glitches(state, player):
    return extended_yoshi_hover(state, player)


def hooktails_castle(state, player):
    return state.has("Sun Stone", player) and state.has("Moon Stone", player) and (state.has("Koops", player) or state.has("Bobbery", player))


def boggly_woods(state, player):
    return state.has("Paper Mode", player)


def great_tree(state, player):
    return state.has("Flurrie", player)


def glitzville(state, player):
    return state.has("Blimp Ticket", player)


def glitzville_glitches(state, player):
    return yoshi_teleport_horizontal(state, player)


def twilight_town(state, player):
    return (
        (sewer_westside(state, player) and state.has("Yoshi", player)) or
        (sewer_westside_ground(state, player) and ultra_boots(state, player))
    )


def twilight_trail(state, player):
    return twilight_town(state, player) and tube_curse(state, player)


def steeple(state, player):
    return state.has("Paper Mode", player) and state.has("Flurrie", player) and super_boots(state, player)


def keelhaul_key(state, player):
    return state.has("Yoshi", player) and tube_curse(state, player) and state.has("Old Letter", player)

def keelhaul_key_glitches(state, player):
    return yoshi_teleport_vertical(state, player) and state.has("Old Letter", player) # Ultra boots are sufficient to use blue pipe, but if blue pipes are disabled...


def pirates_grotto_front_door(state, player):
    return state.has("Yoshi", player) and state.has("Bobbery", player) and state.has("Skull Gem", player) and super_boots(state, player)


def pirates_grotto_front_door_glitches(state, player):
    return (
        (state.has("Yoshi", player) or super_jump(state, player)) # Normal way or superjump in putrid piranhas room
        and state.has("Bobbery", player)
        and (
            (state.has("Skull Gem", player) and super_boots(state, player)) # Normal way or Pirate's Grotto Early using Goombella Buffer + seamwalk
            or state.has("Goombella", player)
        )
    )


def pirates_grotto_back_door_glitches(state, player):
    return state.has("Ms. Mowz", player) and state.has("Yoshi", player)


def pirates_grotto_main_to_ship(state, player):
    return state.has("Yoshi", player) and state.has("Bobbery", player) and state.has("Boat Mode", player)


def pirates_grotto_main_to_ship_glitches(state, player):
    return tube_curse(state, player)


def pirates_grotto_main_to_end(state, player):
    return state.has("Gate Handle", player) and state.has("Yoshi", player) and state.has("Bobbery", player) and state.has("Boat Mode", player)


def pirates_grotto_end_to_ship(state, player):
    return state.has("Boat Mode", player)


def pirates_grotto_ship_to_end(state, player):
    return state.has("Boat Mode", player)


def excess_express(state, player):
    return state.has("Train Ticket", player)


def riverside(state, player):
    return state.has("Vivian", player) and state.has("Autograph", player) and state.has("Ragged Diary", player) and state.has("Blanket", player) and state.has("Vital Paper", player)


def poshley_heights(state, player):
    return state.has("Station Key 1", player) and state.has("Elevator Key (Station)", player) and ultra_boots(state, player)


def fahr_outpost(state, player):
    return ultra_hammer(state, player) and twilight_town(state, player)


def moon(state, player):
    return state.has("Bobbery", player) and state.has("Goldbob Guide", player)


def ttyd(state, player):
    return (state.has("Plane Mode", player) or super_hammer(state, player)
            or (state.has("Flurrie", player) and (state.has("Bobbery", player) or tube_curse(state, player)
            or (state.has("Contact Lens", player) and state.has("Paper Mode", player)))))


def pit(state, player):
    return state.has("Paper Mode", player) and state.has("Plane Mode", player)


def pit_glitches(state, player):
    return super_jump(state, player)


def pit_westside_ground(state, player):
    return state.has("Flurrie", player)
# TODO: Investigate weird Koops jump thing to boat panel in this room?


def palace(state, player, chapters: int, star_shuffle: int):
    return ttyd(state, player) and (state.has("stars", player, chapters) if star_shuffle == StarShuffle.option_all else state.has("required_stars", player, chapters))


def palace_firebar_room(state, player):
    return tube_curse(state, player) or state.has("Vivian", player)


def palace_firebar_room_glitches(state, player):
    return state.has("Koops", player) or state.has("Yoshi", player)

def palace_far_backroom_1(state, player):
    return state.has("Yoshi", player) and state.has("Flurrie", player) and (state.has("Koops", player) or state.has("Bobbery", player))

def palace_far_backroom_2(state, player):
    return palace_far_backroom_1(state, player) and ultra_boots(state, player) and state.has("Bobbery", player)

def palace_far_backroom_3(state, player):
    return palace_far_backroom_2(state, player) and state.has("Palace Key", player, 3) and state.has("Paper Mode", player) and ultra_hammer(state, player)

def palace_far_backroom_1_glitches(state, player):
    return palace_far_backroom_1(state, player) or (extended_yoshi_hover(state, player) and (state.has("Koops", player) or state.has("Bobbery", player)))

def palace_far_backroom_2_glitches(state, player):
    return palace_far_backroom_2(state, player) or (palace_far_backroom_1_glitches(state, player) and ultra_boots(state, player) and (extended_yoshi_hover(state, player) or state.has("Bobbery", player)))

def palace_far_backroom_3_glitches(state, player):
    return (
        (palace_far_backroom_2_glitches(state, player) and state.has("Paper Mode", player) and state.has("Flurrie", player) and ultra_hammer(state, player))
        or
        (palace_far_backroom_1_glitches(state, player) and extended_yoshi_hover(state, player))
    )


def riddle_tower(state, player, glitches=False):
    return (
        palace_firebar_room(state, player) or (glitches and palace_firebar_room_glitches(state, player))
    ) and state.has("Palace Key", player) and state.has("Bobbery", player) and state.has("Boat Mode", player) and state.has("Star Key", player) and state.has("Palace Key (Tower)", player, 8)


def sewer_east_to_west(state, player):
    return tube_curse(state, player) or state.has("Bobbery", player)


def sewer_east_to_west_ground(state, player):
    return ultra_hammer(state, player)


def sewer_west_ground_to_west(state, player):
    return ultra_boots(state, player) or state.has("Paper Mode", player)


def sewer_westside(state, player):
    return tube_curse(state, player) or state.has("Bobbery", player) or (state.has("Paper Mode", player) and state.has("Contact Lens", player)) or (ultra_hammer(state, player) and (state.has("Paper Mode", player) or (ultra_boots(state, player) and state.has("Yoshi", player))))


def sewer_westside_glitches(state, player):
    return state.has("Paper Mode", player)


def sewer_westside_ground(state, player):
    return (state.has("Contact Lens", player) and state.has("Paper Mode", player)) or state.has("Bobbery", player) or tube_curse(state, player) or ultra_hammer(state, player)

def key_any(state, player):
    return state.has("Red Key", player) or state.has("Blue Key", player)

def chapter_completions(state, player, count):
    return len([location for location in star_locations if state.can_reach(location, "Location", player)]) >= count

def super_blue_pipes(state, player):
    return super_hammer(state, player) and super_boots(state, player)

def ultra_blue_pipes(state, player):
    return ultra_hammer(state, player) and super_boots(state, player)


def hooktail_castle_staircase(state, player):
    return (state.has("Yoshi", player) or state.has("Plane Mode", player)) and state.has("Castle Key", player, 1)

def hit_distant_object(state, player):
    return state.has("Koops", player) or state.has("Bobbery", player)


# GLITCH LOGIC SPECIFIC FUNCTIONS BELOW


# Superjump logic will only consider using Koops with either the teleporter door or Bobbery's door.
# This is because it's impossible to be sure that the player will always be able to get jump storage with Yoshi at any given point.
def super_jump(state, player):
    return state.has("Koops", player) and (
        # TRE
        (state.has("Paper Mode", player) and state.has("Elevator Key 2", player))
        or
        # Yoshi teleport into Bobbery's house
        # If you can tube mode in, then you can already do TRE
        yoshi_teleport_vertical(state, player)
    )

def text_storage(state, player):
    return state.has("Goombella", player) and ultra_boots(state, player)

def yoshi_teleport_vertical(state, player):
    return state.has("Yoshi", player) and text_storage(state, player)

def yoshi_teleport_horizontal(state, player):
    return state.has("Ms. Mowz", player) and yoshi_teleport_vertical(state, player)

def extended_yoshi_hover(state, player):
    return yoshi_teleport_vertical(state, player) # same requirements... but just for better readability

def teleporter_room_early(state, player):
    return state.has("Paper Mode", player) or yoshi_teleport_horizontal(state, player)

# Can beat them with 91 punies or can pass with JHS with only 11 punies
def hundred_jabbi_fight(state, player):
    return state.has("Puni Orb", player) and (
        (state.has("Blue Key", player) and state.has("Flurrie", player))
        or 
        (state.has("Goombella", player) and state.has("Paper Mode", player) and state.has("Red Key", player))
    )

def cage_skip(state, player):
    return state.has("Paper Mode", player) or super_boots(state, player)

def hooktail_castle_staircase_superjump(state, player):
    return super_jump(state, player) and tube_curse(state, player) and state.has("Bobbery", player)
