import json
from math import isclose, exp, log

parameter = json.load(open("parameter.json"))

def get_parameter_list(main_name, sub_name, parameter):
    suffix = ["High", "Mid", "Low"]
    return [parameter[main_name][f"{sub_name}_{s}"] for s in suffix]

ISM_LOW = get_parameter_list("MainInkSave", "ConsumeRt_Main_Low", parameter)
ISM_MID = get_parameter_list("MainInkSave", "ConsumeRt_Main", parameter)
ISM_HIGH = get_parameter_list("MainInkSave", "ConsumeRt_Main_High", parameter)

ISS_LOW = get_parameter_list("SubInkSaver", "ConsumeRt_Sub_Low", parameter)
ISS_MID = get_parameter_list("SubInkSaver", "ConsumeRt_Sub", parameter)
ISS_HIGH = get_parameter_list("SubInkSaver", "ConsumeRt_Sub_High", parameter)

SWIMSPEED_HEAVY = get_parameter_list("SquidMoveUp", "MoveVel_Stealth_BigWeapon", parameter)
SWIMSPEED_MID = get_parameter_list("SquidMoveUp", "MoveVel_Stealth", parameter)
SWIMSPEED_LIGHT = get_parameter_list("SquidMoveUp", "MoveVel_Stealth_ShortWeapon", parameter)

RUNSPEED_HEAVY = get_parameter_list("RunSpeedUp", "MoveVel_Human_BigWeapon", parameter)
RUNSPEED_MID = get_parameter_list("RunSpeedUp", "MoveVel_Human", parameter)
RUNSPEED_LIGHT = get_parameter_list("RunSpeedUp", "MoveVel_Human_ShortWeapon", parameter)
RUNSPEED_SHOT = get_parameter_list("RunSpeedUp", "MoveVelRt_Human_Shot", parameter)
RUNSPEED_SHOTG = get_parameter_list("RunSpeedUp", "MoveVelRt_Human_ShotG", parameter)

SPECIAL_CHARGE_UP = get_parameter_list("SpecialIncreaseUp", "SpecialRt_Charge", parameter)

RESPAWNTIME_DIEFRAME = get_parameter_list("RespawnTimeSave", "Dying_AroudFrm", parameter)
RESPAWNTIME_CHASEFRAME = get_parameter_list("RespawnTimeSave", "Dying_ChaseFrm", parameter)

RESPAWN_SPECIAL_GAUGE_SAVE = get_parameter_list("RespawnSpecialGaugeSave", "SpecialRt_Restart", parameter)
RESPAWN_SPECIAL_GAUGE_SAVE_SPLASHDOWN = get_parameter_list("RespawnSpecialGaugeSave", "SpecialRt_Restart_SuperLanding", parameter)

OP_INK_JMP_MSN = get_parameter_list("OpInkEffectReduction", "OpInk_JumpGnd_Msn", parameter)
OP_INK_JMP = get_parameter_list("OpInkEffectReduction", "OpInk_JumpGnd", parameter)
OP_INK_VEL_GND_SHOTK = get_parameter_list("OpInkEffectReduction", "OpInk_VelGnd_ShotK", parameter)
OP_INK_VEL_GND_SHOT = get_parameter_list("OpInkEffectReduction", "OpInk_VelGnd_Shot", parameter)
OP_INK_VEL_GND = get_parameter_list("OpInkEffectReduction", "OpInk_VelGnd", parameter)
OP_INK_DMG_LMT = get_parameter_list("OpInkEffectReduction", "OpInk_Damage_Lmt", parameter)
OP_INK_DMG = get_parameter_list("OpInkEffectReduction", "OpInk_Damage", parameter)

MARKTIME_THERMAL = get_parameter_list("MarkingTimeReduction", "MarkingTime_ShortRt_Thermal", parameter)
MARKTIME_FAR = get_parameter_list("MarkingTimeReduction", "Silhouette_DistFar", parameter)
MARKTIME_CLOSE = get_parameter_list("MarkingTimeReduction", "Silhouette_DistNear", parameter)
MARKTIME_TRAP = get_parameter_list("MarkingTimeReduction", "MarkingTime_ShortRt_Trap", parameter)
MARKTIME_SHORTRT = get_parameter_list("MarkingTimeReduction", "MarkingTime_ShortRt", parameter)

# TODO
JUMP_SQUID = get_parameter_list("JumpTimeSave", "DokanWarp_TameFrm", parameter)
JUMP_JUMP = get_parameter_list("JumpTimeSave", "DokanWarp_MoveFrm", parameter)

IRU_STAND = get_parameter_list("InkRecoveryUp", "RecoverFullFrm_Ink", parameter)
IRU_SWIM = get_parameter_list("InkRecoveryUp", "RecoverNrmlFrm_Ink", parameter)

BOMB_DISTANCE_UP = get_parameter_list("BombDistanceUp", "BombThrow_VelZ", parameter)
BOMB_DISTANCE_UP_PIYO = get_parameter_list("BombDistanceUp", "BombThrow_VelZ_BombPiyo", parameter)
BOMB_DISTANCE_UP_POINTSENSOR = get_parameter_list("BombDistanceUp", "BombThrow_VelZ_PointSensor", parameter)

BOMB_DEF_SUBH = get_parameter_list("BombDamageReduction", "BurstDamageRt_SubH", parameter)
BOMB_DEF_SUBL = get_parameter_list("BombDamageReduction", "BurstDamageRt_SubL", parameter)
BOMB_DEF_SPECIAL = get_parameter_list("BombDamageReduction", "BurstDamageRt_Special", parameter)
BOMB_DEF_MAIN = get_parameter_list("BombDamageReduction", "BurstDamageRt_Main", parameter)

all = [IRU_STAND, IRU_SWIM]

def calcSkillPoint2Percent(points):
    result = (points * 3.3) - (points * points * 0.027)
    if  result >= 0.0:
        if result > 100.0:
            result = 100.0
    else:
        result = 0
        
    return result
    
def lerpN(slope, percentage):
    res = percentage

    if abs(slope - 0.5) >= 0.001:
        if percentage == 0:
            return 0.0
        if percentage == 1.0:
            return 1.0
        if slope >= 0.001:
            return exp(-log(percentage) * log(slope) / log(2))
        else:
            return 0.0
    return res 

def get_slope_simple(ability):
    # Thanks to Lunaji
    high, mid, low = ability
    if isclose(high, low):
        return 0.0
    return (mid-low)/(high-low)
    
def get_effect(ability, points, ninjasquid = False):
    high, mid, low = ability
    slope = round(get_slope_simple(ability), 4)
    tmp = calcSkillPoint2Percent(points)
    if ninjasquid:
        tmp *= 0.8 # ninja squid adds percentage penality
    percentage = round(tmp / 100.0, 4)
    result = low + (high - low) * lerpN(slope, percentage)
    if ninjasquid:
        return 0.9 * result # ninja squid reduces speed by 10%
    return result


if __name__ == '__main__':
    # example how to use it:
    for i in range(0, 4):
        for k in range(0, 10):
            pt = "{0}.{1}".format(i, k)
            eff1 = get_effect(IRU_STAND, i*10+3*k)
            eff2 = get_effect(IRU_SWIM, i*10+3*k)
            print(pt, round(eff1, 4))
            #print(pt, round(eff2, 4))
