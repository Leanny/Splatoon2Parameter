import json
from math import isclose, log2

parameter = json.load(open("parameter.json"))

def get_parameter_list(main_name, sub_name, parameter):
    suffix = ["High", "Mid", "Low"]
    return [parameter[main_name][sub_name+'_'+s] for s in suffix]

abilities = {
    'Ink Saver Main - Low': get_parameter_list('MainInkSave', 'ConsumeRt_Main_Low', parameter),
    'Ink Saver Main - Mid': get_parameter_list('MainInkSave', 'ConsumeRt_Main', parameter),
    'Ink Saver Main - High': get_parameter_list('MainInkSave', 'ConsumeRt_Main_High', parameter),
    'Ink Saver Sub - Low': get_parameter_list('SubInkSaver', 'ConsumeRt_Sub_Low', parameter),
    'Ink Saver Sub - Mid': get_parameter_list('SubInkSaver', 'ConsumeRt_Sub', parameter),
    'Ink Saver Sub - High': get_parameter_list('SubInkSaver', 'ConsumeRt_Sub_High', parameter),
    'Swim Speed - Heavy': get_parameter_list('SquidMoveUp', 'MoveVel_Stealth_BigWeapon', parameter),
    'Swim Speed - Mid': get_parameter_list('SquidMoveUp', 'MoveVel_Stealth', parameter),
    'Swim Speed - Light': get_parameter_list('SquidMoveUp', 'MoveVel_Stealth_ShortWeapon', parameter),
    'Run Speed - Heavy': get_parameter_list('RunSpeedUp', 'MoveVel_Human_BigWeapon', parameter),
    'Run Speed - Mid': get_parameter_list('RunSpeedUp', 'MoveVel_Human', parameter),
    'Run Speed - Light': get_parameter_list('RunSpeedUp', 'MoveVel_Human_ShortWeapon', parameter),
    'Run Speed - Shooting': get_parameter_list('RunSpeedUp', 'MoveVelRt_Human_Shot', parameter),
    'Run Speed - Shooting, Splatling': get_parameter_list('RunSpeedUp', 'MoveVelRt_Human_ShotG', parameter),
    'Special Charge Up': get_parameter_list('SpecialIncreaseUp', 'SpecialRt_Charge', parameter),
    'Quick Respawn - Die Frames': get_parameter_list('RespawnTimeSave', 'Dying_AroudFrm', parameter),
    'Quick Respawn - Deathcam Frames': get_parameter_list('RespawnTimeSave', 'Dying_ChaseFrm', parameter),
    'Special Saver': get_parameter_list('RespawnSpecialGaugeSave', 'SpecialRt_Restart', parameter),
    'Special Saver - Splashdown': get_parameter_list('RespawnSpecialGaugeSave', 'SpecialRt_Restart_SuperLanding', parameter),
    'Ink Resistance - Jump(story)': get_parameter_list('OpInkEffectReduction', 'OpInk_JumpGnd_Msn', parameter),
    'Ink Resistance - Jump': get_parameter_list('OpInkEffectReduction', 'OpInk_JumpGnd', parameter),
    'Ink Resistance - Shoot K': get_parameter_list('OpInkEffectReduction', 'OpInk_VelGnd_ShotK', parameter),
    'Ink Resistance - Shoot': get_parameter_list('OpInkEffectReduction', 'OpInk_VelGnd_Shot', parameter),
    'Ink Resistance - Run': get_parameter_list('OpInkEffectReduction', 'OpInk_VelGnd', parameter),
    'Ink Resistance - Dmg Limit': get_parameter_list('OpInkEffectReduction', 'OpInk_Damage_Lmt', parameter),
    'Ink Resistance - Dmg Per Frame': get_parameter_list('OpInkEffectReduction', 'OpInk_Damage', parameter),
    'Cold Blooded - Thermal Ink Time Reduction': get_parameter_list('MarkingTimeReduction', 'MarkingTime_ShortRt_Thermal', parameter),
    'Cold Blooded - Silhouette Far': get_parameter_list('MarkingTimeReduction', 'Silhouette_DistFar', parameter),
    'Cold Blooded - Silhouette Close': get_parameter_list('MarkingTimeReduction', 'Silhouette_DistNear', parameter),
    'Cold Blooded - Ink Mine': get_parameter_list('MarkingTimeReduction', 'MarkingTime_ShortRt_Trap', parameter),
    'Cold Blooded - Point Sensor': get_parameter_list('MarkingTimeReduction', 'MarkingTime_ShortRt', parameter),
    'Quick Super Jump - Prepare': get_parameter_list('JumpTimeSave', 'DokanWarp_TameFrm', parameter),
    'Quick Super Jump - Jump': get_parameter_list('JumpTimeSave', 'DokanWarp_MoveFrm', parameter),
    'Ink Recovery Up - In Ink': get_parameter_list('InkRecoveryUp', 'RecoverFullFrm_Ink', parameter),
    'Ink Recovery Up - Standing': get_parameter_list('InkRecoveryUp', 'RecoverNrmlFrm_Ink', parameter),
    'Bomb Distance Up': get_parameter_list('BombDistanceUp', 'BombThrow_VelZ', parameter),
    'Bomb Distance Up - Fizzy': get_parameter_list('BombDistanceUp', 'BombThrow_VelZ_BombPiyo', parameter),
    'Bomb Distance Up - Point Sensor': get_parameter_list('BombDistanceUp', 'BombThrow_VelZ_PointSensor', parameter),
    'Bomb Defense - Heavy Sub': get_parameter_list('BombDamageReduction', 'BurstDamageRt_SubH', parameter),
    'Bomb Defense - Heavy Light': get_parameter_list('BombDamageReduction', 'BurstDamageRt_SubL', parameter),
    'Bomb Defense - Special': get_parameter_list('BombDamageReduction', 'BurstDamageRt_Special', parameter),
    'Bomb Defense - Additional': get_parameter_list('BombDamageReduction', 'BurstDamageRt_Main', parameter),
}

def calcSkillPoint2Percent(points):
    return min(max(0.0, 3.3*points-0.027*points**2), 100.0)
    
def lerpN(slope, percentage):
    if isclose(percentage, 0.0) or not slope >= 0.001:
        return 0.0
    return 1/percentage**(log2(slope))

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
    print("""
                ____        _       _                      ____  
               / ___| _ __ | | __ _| |_ ___   ___  _ __   |___ \ 
               \___ \| '_ \| |/ _` | __/ _ \ / _ \| '_ \    __) |
                ___) | |_) | | (_| | || (_) | (_) | | | |  / __/ 
               |____/| .__/|_|\__,_|\__\___/ \___/|_| |_| |_____|
                     |_|                                         
                ____                                _            
               |  _ \ __ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __ 
               | |_) / _` | '__/ _` | '_ ` _ \ / _ \ __/ _ \ '__|
               |  __/ (_| | | | (_| | | | | | |  __/ ||  __/ |   
               |_|   \__,_|_|  \__,_|_| |_| |_|\___|\__\___|_|   
                                                                 
    """)    
    
    names = sorted([*abilities.keys()])
    
    for i in range(0, len(names)-1,2):
        print('{:<50}{:<}'.format(str(i+1).rjust(2)+'. '+names[i], str(i+2).rjust(2)+'. '+names[i+1]))
