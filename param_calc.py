import json

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

# TODO
RESPAWN_SPECIAL_GAUGE_SAVE = get_parameter_list("RespawnSpecialGaugeSave", "SpecialRt_Restart", parameter)

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

BOMB_DEF_SUBH = get_parameter_list("BombDamageReduction", "BurstDamageRt_SubH", parameter)
BOMB_DEF_SUBL = get_parameter_list("BombDamageReduction", "BurstDamageRt_SubL", parameter)
BOMB_DEF_SPECIAL = get_parameter_list("BombDamageReduction", "BurstDamageRt_Special", parameter)
BOMB_DEF_MAIN = get_parameter_list("BombDamageReduction", "BurstDamageRt_Main", parameter)

irreg_param = {
# TODO: 0.4, 0.75
    0.6: {
        0.0: 0,
        0.0966: 0.178623288,
        0.1883: 0.29218274,
        0.2751: 0.3863455,
        0.303: 0.4148842,
        0.3571: 0.46831826,
        0.3834: 0.49343004,
        0.4342: 0.5408631,
        0.4589: 0.56332386,
        0.5065: 0.60589504,
        0.5295: 0.62600624,
        0.552: 0.64544154,
        0.5739: 0.664335,
        0.5953: 0.6824292,
        0.6162: 0.69998694,
        0.6365: 0.71694326,
        0.6562: 0.7332308,
        0.6755: 0.749066,
        0.6942: 0.76424248,
        0.7123: 0.77892972,
        0.7299: 0.79311324,
        0.747: 0.8065945,
        0.7635: 0.81987094,
        0.7795: 0.8324398,
        0.795: 0.90745044,
        0.8099: 0.85626316,
        0.8242: 0.86740506,
        0.8381: 0.8779408,
        0.8514: 0.88833732,
        0.8641: 0.89817,
        0.8763: 0.90745044,
        0.8991: 0.9247668,
        0.9097: 0.93285114,
        0.9293: 0.94754428,
        0.9383: 0.95417988,
        0.9546: 0.96646452,
        0.9619: 0.97200036,
        0.9807: 0.98596412,
        0.9947: 0.99615108,
        1.0: 1.0,
    },
}

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
        if slope >= 0.001:
            return irreg_param[slope][percentage]
        else:
            v6 = percentage < 0.999
            return 0.0
    return res 
  
def get_effect(ability, points):
    high, mid, low = ability
    if low <= high:
        slope = 0.0
        if mid > low:
            if mid >= high:
                slope = 1.0
            else:
                slope2 = high - low
                if high - low != 0.0:
                    c3 = mid - low
                    slope = round(c3 / slope2, 4)

    else:
        slope2 = 0
        if mid > high:
            if mid >= low:
                slope2 = 1.0
            elif (low - high) != 0.0:
                slope2 = round((mid - high) / (low - high), 4)

        c3 = 1.0
        slope = 1.0 - slope2

    tmp = calcSkillPoint2Percent(points)
    percentage = round(tmp / 100.0, 4)
    return low + (high - low) * lerpN(slope, percentage)

# example how to use it:
print(get_effect(ISM_MID, 10))